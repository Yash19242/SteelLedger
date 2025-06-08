
# 🧾 SteelLedger – Tally-Style GST Invoice Generator in Python

SteelLedger is a command-line billing system designed for brokers, traders, and firms in the India . It helps users generate GST-compliant tax invoices, track payment status, and export professional PDF bills. Built with Python and created for real-world business use.

---

## 🚀 Features

- 🧾 Generate tax invoices with CGST/SGST or IGST (based on buyer state)
- 🗃️ Save buyer and seller details for future reuse
- 📦 Add multiple products with HSN, quantity, rate, and discount
- 📄 Export print-ready PDF invoices (with invoice number + amount in words)
- 📊 Track outstanding (unpaid) invoices
- 📁 Save all invoice records to CSV automatically
- ⚙️ Fully terminal-based — no need for web or GUI setup

---

## 📂 Folder Structure

```
SteelLedger/
├── main.py                  # Main CLI logic
├── README.md
├── bills.csv                # Invoice data (auto-updated)
├── data/
│   ├── buyers.json          # Saved buyers
│   └── seller.json          # Your firm details
├── invoices/                # PDF invoice exports
├── core/                    # Project modules
│   ├── buyers.py
│   ├── products.py
│   ├── seller.py
│   ├── tax.py
│   ├── pdf_export.py
│   └── report.py
```

---

## 💻 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/yashsheth/SteelLedger.git
cd SteelLedger
```

2. **Install required packages**

```bash
pip install fpdf num2words
```

3. **Run the app**

```bash
python main.py
```

---

## 🧪 Example Use Case

This project was created by [Yash Sheth](https://www.linkedin.com/in/yash-sheth-83710136a) to help his father’s steel brokerage business automate tax invoice generation — replacing manual paperwork with smart Python automation.

---

## 📸 Screenshots
> Invoice Screenshot- file:///Users/yashsheth/Desktop/SteelLedger/invoices/invoice_MSH_001_2025-26.pdf

---

## 📌 Tech Stack

- **Python 3.10+**
- `fpdf` (PDF export)
- `num2words` (amount to words)
- `csv` / `json` for data tracking
- Terminal CLI (no GUI required)

---

## 🔮 Upcoming Features

- ✅ QR Code or E-Way bill field  
- ✅ Streamlit-based web GUI  
- ✅ Backup/export buyer database  
- ✅ Auto-email invoice feature  
- ✅ Monthly summary report

---

## 👨‍💻 Author

**Yash Sheth**  
Python Developer in Progress | Real-World Project Builder  
🔗 [LinkedIn](https://www.linkedin.com/in/yash-sheth-83710136a)

---

## 🆓 License

This project is open-sourced under the MIT License.
