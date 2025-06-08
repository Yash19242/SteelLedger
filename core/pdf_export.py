from fpdf import FPDF
import os
from num2words import num2words

def export_pdf(invoice_id, date, seller, buyer, products, transport,
               total, cgst, sgst, igst, round_off, grand_total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "TAX INVOICE", ln=True, align="C")
    pdf.set_font("Arial", "", 10)
    pdf.cell(100, 6, f"Seller: {seller['firm_name']}")
    pdf.cell(100, 6, f"Invoice No: {invoice_id}", ln=True)
    pdf.cell(100, 6, f"GSTIN: {seller['gstin']}")
    pdf.cell(100, 6, f"Date: {date}", ln=True)
    pdf.multi_cell(0, 6, f"Address: {seller['address']}")
    pdf.cell(0, 6, f"Buyer: {buyer['name']} - {buyer['gstin']}", ln=True)
    pdf.cell(0, 6, f"{buyer['address']} ({buyer['state']})", ln=True)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(10, 6, "No")
    pdf.cell(50, 6, "Item")
    pdf.cell(20, 6, "HSN")
    pdf.cell(20, 6, "Qty")
    pdf.cell(25, 6, "Rate")
    pdf.cell(25, 6, "Discount")
    pdf.cell(30, 6, "Amount", ln=True)
    pdf.set_font("Arial", "", 10)
    for i, p in enumerate(products, 1):
        pdf.cell(10, 6, str(i))
        pdf.cell(50, 6, p["item"])
        pdf.cell(20, 6, p["hsn"])
        pdf.cell(20, 6, str(p["qty"]))
        pdf.cell(25, 6, str(p["rate"]))
        pdf.cell(25, 6, str(p["discount"]))
        pdf.cell(30, 6, f"{p['amount']:.2f}", ln=True)
    pdf.cell(0, 6, f"Subtotal: {total:.2f}", ln=True)
    if cgst:
        pdf.cell(0, 6, f"CGST @9%: {cgst:.2f}", ln=True)
        pdf.cell(0, 6, f"SGST @9%: {sgst:.2f}", ln=True)
    else:
        pdf.cell(0, 6, f"IGST @18%: {igst:.2f}", ln=True)
    pdf.cell(0, 6, f"Round Off: {round_off:.2f}", ln=True)
    pdf.cell(0, 6, f"Grand Total: {grand_total:.2f}", ln=True)
    pdf.multi_cell(0, 6, "In Words: " + num2words(grand_total, lang="en_IN").title())
    pdf.cell(0, 6, f"Transport: {transport}", ln=True)
    path = f"invoices/invoice_{invoice_id.replace('/', '_')}.pdf"
    pdf.output(path)
    print(f"✅ Saved PDF to {path}")