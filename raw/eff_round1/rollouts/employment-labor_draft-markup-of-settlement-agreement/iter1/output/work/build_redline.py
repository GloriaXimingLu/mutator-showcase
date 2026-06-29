#!/usr/bin/env python3
"""Insert tracked-change (<w:ins>/<w:del>) revisions into the unpacked
settlement agreement XML, preserving all original run/paragraph formatting.
Operates on work/revised/word/document.xml in place."""
import copy
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
AUTHOR = "Greenleaf GC Review"
DATE = "2025-05-14T00:00:00Z"

# Ensure the 'w' prefix is preserved on serialization.
etree.register_namespace("w", W)

_id = [1000]
def next_id():
    _id[0] += 1
    return _id[0]

def w(t):
    return "{%s}%s" % (W, t)

# ---------- element builders ----------
def rpr_el(style):
    """style in {'normal','bold','boldu'}"""
    rpr = etree.Element(w("rPr"))
    rf = etree.SubElement(rpr, w("rFonts"))
    rf.set(w("ascii"), "Times New Roman")
    rf.set(w("hAnsi"), "Times New Roman")
    if style in ("bold", "boldu"):
        etree.SubElement(rpr, w("b"))
    col = etree.SubElement(rpr, w("color"))
    col.set(w("val"), "000000")
    sz = etree.SubElement(rpr, w("sz"))
    sz.set(w("val"), "22")
    if style == "boldu":
        u = etree.SubElement(rpr, w("u"))
        u.set(w("val"), "single")
    return rpr

def run_el(text, rpr, is_del=False):
    r = etree.Element(w("r"))
    if rpr is not None:
        r.append(copy.deepcopy(rpr))
    tname = w("delText") if is_del else w("t")
    t = etree.SubElement(r, tname)
    t.set("{%s}space" % XML, "preserve")
    t.text = text
    return r

def ins_wrap(run, rid):
    ins = etree.Element(w("ins"))
    ins.set(w("id"), str(rid))
    ins.set(w("author"), AUTHOR)
    ins.set(w("date"), DATE)
    ins.append(run)
    return ins

def del_wrap(run, rid):
    d = etree.Element(w("del"))
    d.set(w("id"), str(rid))
    d.set(w("author"), AUTHOR)
    d.set(w("date"), DATE)
    d.append(run)
    return d

# ---------- paragraph helpers ----------
def ptext(p):
    return "".join(t.text or "" for t in p.findall(".//" + w("t")))

def find_para(body, sub):
    for p in body.findall(w("p")):
        if sub in ptext(p):
            return p
    raise RuntimeError("paragraph not found for: %r" % sub)

def replace_in_para(p, old, new):
    """Find the run whose <w:t> contains `old`; split into
    [before][del old][ins new][after], preserving the run's rPr."""
    for r in list(p):
        if r.tag != w("r"):
            continue
        t = r.find(w("t"))
        if t is None or t.text is None:
            continue
        txt = t.text
        if old not in txt:
            continue
        # sanity: run should only contain rPr + t
        kids = [c.tag for c in r]
        assert all(k == w("rPr") or k == w("t") for k in kids), \
            "unexpected run children: %r" % kids
        i = txt.index(old)
        before, after = txt[:i], txt[i + len(old):]
        rpr = r.find(w("rPr"))
        rpr_copy = copy.deepcopy(rpr) if rpr is not None else None
        new_elems = []
        if before:
            new_elems.append(run_el(before, rpr_copy))
        new_elems.append(del_wrap(run_el(old, rpr_copy, is_del=True), next_id()))
        if new:
            new_elems.append(ins_wrap(run_el(new, rpr_copy), next_id()))
        if after:
            new_elems.append(run_el(after, rpr_copy))
        parent = r.getparent()
        idx = list(parent).index(r)
        parent.remove(r)
        for off, el in enumerate(new_elems):
            parent.insert(idx + off, el)
        return True
    raise RuntimeError("old text not found in any run: %r" % old)

def make_inserted_para(segments, ppr_template):
    """segments: list of (text, style). Whole paragraph is an insertion."""
    p = etree.Element(w("p"))
    ppr = copy.deepcopy(ppr_template)
    # inserted paragraph mark (pilcrow) -> rPr/ins as last child of pPr
    rpr = etree.SubElement(ppr, w("rPr"))
    ins = etree.SubElement(rpr, w("ins"))
    ins.set(w("id"), str(next_id()))
    ins.set(w("author"), AUTHOR)
    ins.set(w("date"), DATE)
    p.append(ppr)
    for text, style in segments:
        if text == "":
            continue
        run = run_el(text, rpr_el(style))
        p.append(ins_wrap(run, next_id()))
    return p

def insert_after(ref, new_paras):
    cur = ref
    for np in new_paras:
        cur.addnext(np)
        cur = np

# ---------- main ----------
def main():
    path = "work/revised/word/document.xml"
    tree = etree.parse(path)
    body = tree.getroot().find(w("body"))
    paras = body.findall(w("p"))

    # pPr templates (deep-copied from real paragraphs)
    body_ppr = paras[31].find(w("pPr"))      # justified body paragraph
    hdr_ppr = paras[30].find(w("pPr"))       # bold section header (keepNext)

    def body_para(text):
        return make_inserted_para([(text, "normal")], body_ppr)

    def hdr_para(text):
        return make_inserted_para([(text, "bold")], hdr_ppr)

    # ===== TEXT MODIFICATIONS =====
    mods = [
        # (find-substring, old, new, label)
        ('This Settlement Agreement and General Release of All Claims ("Agreement") is entered into',
         'May 5, 2025 ("Effective Date")',
         'the date of the last signature affixed below (the "Effective Date," as defined in Section 1(b))',
         "Preamble Effective Date"),
        ('(b) "Effective Date" means',
         'May 5, 2025, the date first set forth above.',
         'the eighth (8th) calendar day after the date on which Delano signs this Agreement, '
         'provided that Delano does not revoke his acceptance during the seven (7) calendar day '
         'revocation period set forth in Section 16. If Delano timely revokes his acceptance '
         'pursuant to Section 16, this Agreement shall be null and void and of no force or effect.',
         "Sec 1(b) Effective Date def"),
        ('(d) Accelerated Vesting of Restricted Stock Units.',
         'Ten Dollars ($10.00) per share, based on the most recent independent valuation conducted '
         'by Ridgepoint Valuation Services, representing a total value of Fifty Thousand Dollars ($50,000.00)',
         'Twelve Dollars and Fifty Cents ($12.50) per share, based on the most recent independent '
         '409A valuation conducted by Ridgepoint Valuation Services dated January 15, 2025, '
         'representing a total value of Sixty-Two Thousand Five Hundred Dollars ($62,500.00)',
         "Sec 3(d) RSU valuation"),
        ('(e) Total Settlement Value.',
         'Five Hundred Twenty-Five Thousand Dollars ($525,000.00), comprised of the compensatory '
         'damages payment ($275,000.00), the back pay payment ($125,000.00), the attorney fees '
         'payment ($75,000.00), and the RSU acceleration ($50,000.00).',
         'Five Hundred Thirty-Seven Thousand Five Hundred Dollars ($537,500.00), comprised of the '
         'compensatory damages payment ($275,000.00), the back pay payment ($125,000.00), the '
         'attorney fees payment ($75,000.00), and the RSU acceleration ($62,500.00).',
         "Sec 3(e) total value"),
        ('(c) Delano has been given a period of fourteen',
         'fourteen (14) calendar days from the date of receipt of this Agreement within which to consider',
         'twenty-one (21) calendar days from the date of receipt of this Agreement within which to consider',
         "Sec 5(c) 21-day period"),
        ('Neither Party shall, at any time after the Effective Date, make, publish',
         'shall continue in perpetuity.',
         'shall continue for a period of five (5) years following the Effective Date.',
         "Sec 7 perpetuity -> 5 yrs"),
        ('For a period of eighteen (18) months following the Separation Date, Delano shall not',
         'within the states of Oregon, Washington, Idaho, and California.',
         'within the states of Oregon, Washington, and Idaho.',
         "Sec 9 remove California"),
        ('(ii) He has not filed any lawsuit, complaint, charge, or other proceeding',
         'except as may be required by law or to enforce the terms of this Agreement;',
         'except as may be required by law or to enforce the terms of this Agreement; provided, '
         'however, that nothing in this Agreement shall prohibit, restrict, or discourage Delano '
         'from reporting possible violations of law to any governmental agency, communicating with '
         'or participating in any investigation or proceeding conducted by any governmental agency, '
         'or receiving a monetary award or other compensation from any governmental agency for doing '
         'so, in each case without notice to or approval from Greenleaf;',
         "Sec 15(a)(ii) gov carve-out"),
        ('Delano shall have fourteen (14) calendar days from the date of receipt of this Agreement to review',
         'Delano shall have fourteen (14) calendar days from the date of receipt of this Agreement to review',
         'Delano shall have twenty-one (21) calendar days from the date of receipt of this Agreement to review',
         "Sec 16 21-day period"),
        ('this offer of settlement shall automatically expire',
         'within the fourteen (14) calendar day period',
         'within the twenty-one (21) calendar day period',
         "Sec 16 21-day period (2)"),
    ]
    for sub, old, new, label in mods:
        p = find_para(body, sub)
        ok = replace_in_para(p, old, new)
        print("MOD [%s] -> %s" % (label, ok))

    # ===== NEW PARAGRAPH INSERTIONS =====
    # INS A: Section 2 - 401(k) preservation
    ref = find_para(body, "Delano confirms that he has received all wages")
    insert_after(ref, [body_para(
        "Nothing in this Agreement shall affect Delano's vested benefits under the "
        "Greenleaf Organic Foods, Inc. 401(k) Plan, including his vested account balance "
        "and any vested employer matching contributions, which shall remain governed by "
        "the terms of the 401(k) Plan and the applicable plan administrator. Delano shall "
        "be entitled to elect a direct rollover or distribution of his vested 401(k) account "
        "balance in accordance with the terms of the 401(k) Plan and applicable law.")])
    print("INS [Sec 2 401(k)]")

    # INS B: Section 5 - (g) attorney advisement, (h) revocation acknowledgment
    ref = find_para(body, "Delano has not been coerced, threatened, or otherwise pressured into signing")
    insert_after(ref, [
        body_para("(g) Delano acknowledges that he has been advised in writing to consult with an "
                  "attorney of his choosing prior to executing this Agreement and has had a full and "
                  "adequate opportunity to do so."),
        body_para("(h) Delano understands that, for a period of seven (7) calendar days following his "
                  "execution of this Agreement, he may revoke this Agreement as provided in Section 16, "
                  "and that this Agreement shall not become effective or enforceable, and no payments "
                  "shall be due, until the expiration of that seven (7) calendar day revocation period."),
    ])
    print("INS [Sec 5 (g)/(h)]")

    # INS C: Section 6 - (v) government-agency exception
    ref = find_para(body, "as required by applicable law, regulation, court order, subpoena")
    insert_after(ref, [body_para(
        "(v) to any governmental agency, regulator, or law enforcement authority, including without "
        "limitation the U.S. Equal Employment Opportunity Commission, the U.S. Securities and Exchange "
        "Commission, Oregon OSHA, the Oregon Bureau of Labor and Industries, the National Labor "
        "Relations Board, and the U.S. Department of Labor, in connection with the reporting of "
        "possible violations of law or participation in any investigation or proceeding; provided, "
        "however, that Delano may not disclose the terms of this Agreement except as permitted by law "
        "or as necessary to participate in such investigation or proceeding.")])
    print("INS [Sec 6 (v)]")

    # INS D: Section 6 - general government carve-out sentence
    ref = find_para(body, "In the event that Delano is compelled by legal process")
    insert_after(ref, [body_para(
        "Nothing in this Section 6 shall prohibit, restrict, or discourage Delano from reporting "
        "possible violations of law to any governmental agency, communicating with or participating "
        "in any investigation or proceeding conducted by any governmental agency, or receiving a "
        "monetary award or other compensation from any governmental agency for doing so, in each case "
        "without notice to or approval from Greenleaf.")])
    print("INS [Sec 6 general carve-out]")

    # INS E: Section 7 - non-disparagement government carve-out
    ref = find_para(body, "Neither Party shall, at any time after the Effective Date, make, publish")
    insert_after(ref, [body_para(
        "Nothing in this Section 7 shall prohibit, restrict, or discourage either Party from reporting "
        "possible violations of law to any governmental agency, communicating with or participating in "
        "any investigation or proceeding conducted by any governmental agency, or receiving a monetary "
        "award or other compensation from any governmental agency for doing so, in each case without "
        "notice to or approval from the other Party.")])
    print("INS [Sec 7 carve-out]")

    # INS F: Section 16 - revocation period
    ref = find_para(body, "Delano shall have twenty-one (21) calendar days from the date of receipt of this Agreement to review")
    insert_after(ref, [body_para(
        "Delano further acknowledges and agrees that he may revoke this Agreement for a period of "
        "seven (7) calendar days following his execution of this Agreement by delivering written "
        "notice of revocation to Greenleaf's General Counsel. If Delano does not revoke within such "
        "seven (7) calendar day period, this Agreement shall become effective on the eighth (8th) "
        'calendar day after the date of Delano\'s execution (the "Effective Date," as defined in '
        "Section 1(b)). If Delano timely revokes this Agreement, this Agreement shall be null and "
        "void and of no force or effect, and neither Party shall have any obligation hereunder. No "
        "payments or benefits under this Agreement shall be made or provided until the Effective Date.")])
    print("INS [Sec 16 revocation]")

    # INS G: New Sections 19-24 after Section 18 body, before IN WITNESS WHEREOF
    ref = find_para(body, "This Agreement constitutes the entire agreement between the Parties")
    new_sections = [
        hdr_para("Section 19. Return of Company Property"),
        body_para("Delano represents and warrants that he has returned, or shall return within five "
                  "(5) business days of the Effective Date, all property of Greenleaf in his possession, "
                  "custody, or control, including without limitation all keys, access cards, credit "
                  "cards, laptop computers, mobile phones, tablets, documents, files, records, data, "
                  "and other tangible and intangible property of Greenleaf, and that he has not "
                  "retained any copies, extracts, or summaries thereof. Delano further represents and "
                  "warrants that he has returned or destroyed all Confidential Information of Greenleaf "
                  "(as defined in Section 21) in his possession and has not retained any copies thereof."),
        hdr_para("Section 20. Cooperation"),
        body_para("Following the Effective Date, Delano shall reasonably cooperate with Greenleaf in "
                  "connection with (a) the transition of his former duties and responsibilities, "
                  "(b) any matter, project, or engagement with which Delano was materially involved "
                  "during his employment, and (c) any investigation, audit, claim, dispute, or "
                  "litigation involving Greenleaf to which Delano has relevant knowledge, including by "
                  "providing truthful information and, if reasonably requested, making himself "
                  "available for interviews, depositions, or testimony subject to reasonable "
                  "scheduling accommodations. Greenleaf shall reimburse Delano for reasonable, "
                  "documented out-of-pocket expenses incurred in providing such cooperation. Nothing "
                  "in this Section 20 shall require Delano to provide cooperation that conflicts with "
                  "his obligations to a subsequent employer, except as required by law or legal process."),
        hdr_para("Section 21. Confidential Information of Greenleaf"),
        body_para("Delano acknowledges that, during his employment, he had access to and became "
                  "familiar with confidential and proprietary information of Greenleaf, including "
                  "without limitation information regarding Greenleaf's supply chain operations, "
                  "vendor and supplier relationships and pricing, cold-chain and food safety "
                  "protocols, distribution logistics, customer lists, business strategies, financial "
                  'information, and trade secrets (collectively, "Confidential Information"). Delano '
                  "agrees that, following the Separation Date, he shall not use, disclose, or make "
                  "available to any third party any Confidential Information, except (a) as required "
                  "by law or legal process, (b) in connection with the cooperation obligations of "
                  "Section 20, or (c) as otherwise permitted by this Agreement. The obligations of "
                  "this Section 21 shall continue for so long as the information remains "
                  "confidential. Pursuant to the Defend Trade Secrets Act of 2016 (18 U.S.C. "
                  "\u00a7 1833(b)), Delano is hereby notified that an individual shall not be held "
                  "criminally or civilly liable under any federal or state trade secret law for the "
                  "disclosure of a trade secret that is made (i) in confidence to a federal, state, "
                  "or local government official or to an attorney solely for the purpose of reporting "
                  "or investigating a suspected violation of law, or (ii) in a complaint or other "
                  "document filed in a lawsuit or other proceeding, if such filing is made under "
                  "seal. Nothing in this Agreement is intended to conflict with 18 U.S.C. "
                  "\u00a7 1833(b) or to limit Delano's rights thereunder."),
        hdr_para("Section 22. Governing Law and Venue"),
        body_para("This Agreement shall be governed by and construed in accordance with the laws of "
                  "the State of Oregon, without regard to its conflict-of-laws principles. Any action "
                  "or proceeding arising out of or relating to this Agreement shall be brought "
                  "exclusively in the state or federal courts located in Multnomah County, Oregon, "
                  "and each Party hereby consents to the exclusive jurisdiction and venue of such "
                  "courts and waives any objection based on forum non conveniens."),
        hdr_para("Section 23. Enforcement and Attorneys' Fees"),
        body_para("The Parties acknowledge and agree that any breach of this Agreement may cause "
                  "irreparable harm for which monetary damages would be an inadequate remedy, and "
                  "that the non-breaching Party shall be entitled to seek injunctive relief, specific "
                  "performance, and other equitable remedies, in addition to all other remedies "
                  "available at law or in equity, without the necessity of posting a bond. In any "
                  "action or proceeding to enforce this Agreement, the prevailing Party shall be "
                  "entitled to recover its reasonable attorneys' fees and costs incurred in "
                  "connection with such action or proceeding, in addition to any other relief awarded."),
        hdr_para("Section 24. Acknowledgment Regarding Government Investigations"),
        body_para("The Parties acknowledge that the Oregon OSHA investigation referenced in the "
                  "Recitals (Complaint No. OR-OSHA-2024-11872) is a governmental proceeding that may "
                  "proceed independently of this Agreement and that neither Party can control or "
                  "dismiss by private agreement. Nothing in this Agreement shall be construed to "
                  "limit the authority of Oregon OSHA or any other governmental agency to "
                  "investigate, make findings, or take action with respect to any matter within its "
                  "jurisdiction, or to limit either Party's right to respond to lawful inquiries from "
                  "such agencies. The release of claims in Section 4 applies to Delano's private "
                  "claims against the Releasees and does not purport to release, waive, or affect any "
                  "rights or claims of any governmental agency."),
    ]
    insert_after(ref, new_sections)
    print("INS [Sections 19-24]")

    # ---------- write ----------
    tree.write(path, xml_declaration=True, encoding="UTF-8", standalone=True)
    print("WROTE", path)

if __name__ == "__main__":
    main()