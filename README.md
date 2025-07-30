# 📧 Website Email Extractor (GUI + Excel Export)

This is a Python desktop GUI application that extracts email addresses from a list of websites provided in a `.txt` file. It checks the homepage and also searches for emails on "contact" or "career" pages if needed.

---

## ✅ Features

- GUI interface using `tkinter`
- Upload list of websites from a `.txt` file
- Automatically follows redirects
- Extracts emails using pattern matching
- Fallback to "contact" or "career" subpages if homepage has no email
- Displays results live in GUI
- Saves results to Excel (`.xlsx`) in column format
- Includes websites with no emails found

---

## 📦 Requirements

Install required Python packages:

```bash
pip install requests beautifulsoup4 openpyxl
```

---

## 📁 Input Format (websites.txt)

Example contents of `websites.txt`:

```
https://example.com
royalwrist.pk
https://anotherdomain.org
```

Each website should be on a new line. You can include or omit `http://` or `https://`.

---

## 🚀 How to Use

1. Run the Python script:

```bash
python email_extractor_gui.py
```

2. In the GUI:
   - Click **"Upload Website List"** to choose your `.txt` file.
   - The app will fetch emails and display results live.
   - After processing, click **"Save Results to Excel"** to export.

---

## 🧾 Output Format (Excel)

| Website              | Emails                                      |
|----------------------|----------------------------------------------|
| https://example.com  | info@example.com                             |
| royalwrist.pk        | hr@royalwrist.pk, support@royalwrist.pk      |
| https://abc.com      | No emails found                              |

---

## ❗ Notes

- Email detection is regex-based and works for standard formats.
- Sites using JavaScript to load email data are not supported in this version.
- Every website is included in the output, even if no email is found.

---

## 📍 Author

Made with ❤️ using Python for automated email scraping tasks.
