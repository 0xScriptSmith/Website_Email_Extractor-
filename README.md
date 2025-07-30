# 📧 Website Email Extractor (GUI + Excel Export + Timeout & Status)

This is a Python desktop GUI application that extracts email addresses from a list of websites provided in a `.txt` file. It checks the homepage and also searches for emails on "contact" or "career" pages if needed. Each website is processed with a timeout to avoid freezing on slow or unresponsive sites.

Now supports detailed status output:
- ✅ Found emails
- 🚫 No emails found
- ⏱️ Timed out

---

## ✅ Features

- GUI interface using `tkinter`
- Upload list of websites from a `.txt` file
- Automatically follows redirects
- Extracts emails using regex
- Fallback to "contact" or "career" subpages if homepage has no email
- Timeout: skips any website taking more than 15 seconds
- Displays results live in GUI
- Saves results to Excel (`.xlsx`) in column format
- Distinguishes between:
  - Found emails
  - No emails found
  - Timed out websites

---

## 📦 Requirements

Install required Python packages:

```bash
pip install requests beautifulsoup4 openpyxl
```

---

## 📁 Input Format (websites.txt)

Example:

```
https://example.com
royalwrist.pk
https://anotherdomain.org
```

Each line should be a full or partial website address. The script auto-adds `http://` if missing.

---

## 🚀 How to Use

1. Run the script:

```bash
python Email_Fcher.py
```

2. In the GUI:
   - Click **"Upload Website List"** to choose your `.txt` file.
   - The app will process and display emails or status.
   - When done, click **"Save Results to Excel"** to export.

---

## 🧾 Output Format (Excel)

| Website              | Emails / Status                         |
|----------------------|------------------------------------------|
| https://example.com  | contact@example.com                     |
| royalwrist.pk        | hr@royalwrist.pk, info@royalwrist.pk   |
| https://slow-site.com| Timed out                               |
| https://empty.com    | No emails found                         |

---

## ❗ Notes

- Sites using JavaScript to load email content are **not supported** in this version.
- Every website is included in the output with clear status.
- Timeout is currently set to **15 seconds** per website.

---

## 📍 Author

Made with ❤️ in Python for scraping and organizing emails from websites efficiently.
