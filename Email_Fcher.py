
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from openpyxl import Workbook
import threading

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def extract_emails_from_url(url, result_holder):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        soup = BeautifulSoup(response.text, "html.parser")
        emails = set(re.findall(EMAIL_REGEX, response.text))

        if emails:
            result_holder["status"] = "found"
            result_holder["emails"] = list(emails)
            return

        # Fallback: check for 'contact' or 'career' page
        links = soup.find_all("a", href=True)
        for link in links:
            href = link['href'].lower()
            if "contact" in href or "career" in href:
                next_url = urljoin(url, link['href'])
                extract_emails_from_url(next_url, result_holder)
                return

        result_holder["status"] = "no_email"
    except:
        return

def extract_emails_from_url_with_timeout(url, max_time=15):
    result_holder = {}
    thread = threading.Thread(target=extract_emails_from_url, args=(url, result_holder))
    thread.start()
    thread.join(timeout=max_time)
    if thread.is_alive():
        return ("timeout", [])
    if result_holder.get("status") == "found":
        return ("found", result_holder.get("emails", []))
    return ("no_email", [])

class EmailExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Email Extractor")
        self.root.geometry("750x550")

        tk.Button(root, text="Upload Website List", command=self.upload_file).pack(pady=10)
        self.output = scrolledtext.ScrolledText(root, width=90, height=25)
        self.output.pack(padx=10, pady=10)

        tk.Button(root, text="Save Results to Excel", command=self.save_results).pack(pady=5)
        self.results = []  # list of (website, status_str)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        threading.Thread(target=self.process_websites, args=(file_path,), daemon=True).start()

    def process_websites(self, file_path):
        with open(file_path, 'r') as f:
            websites = [line.strip() for line in f if line.strip()]

        self.output.delete("1.0", tk.END)
        self.results = []

        for site in websites:
            if not site.startswith("http"):
                site = "http://" + site
            self.output.insert(tk.END, f"{site} | ")

            status, emails = extract_emails_from_url_with_timeout(site, max_time=15)
            if status == "found":
                email_str = ', '.join(emails)
                self.output.insert(tk.END, f"{email_str}\n")
                self.results.append((site, email_str))
            elif status == "no_email":
                self.output.insert(tk.END, "No emails found\n")
                self.results.append((site, "No emails found"))
            elif status == "timeout":
                self.output.insert(tk.END, "Timed out\n")
                self.results.append((site, "Timed out"))

            self.output.see(tk.END)
            self.root.update()

        messagebox.showinfo("Done", "✅ All websites processed.")

    def save_results(self):
        if not self.results:
            messagebox.showinfo("Nothing to Save", "No results to save yet!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx")])
        if save_path:
            wb = Workbook()
            ws = wb.active
            ws.append(["Website", "Emails / Status"])

            for site, result in self.results:
                ws.append([site, result])

            wb.save(save_path)
            messagebox.showinfo("Saved", f"✅ Results saved to Excel:\n{save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailExtractorApp(root)
    root.mainloop()
