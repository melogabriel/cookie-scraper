# **Web Cookie Exporter**

**Web Cookie Exporter** is a professional-grade, full-stack tool designed to extract browser cookies from any website and export them directly into a clean .csv format.

By leveraging **Selenium** and **Headless Chrome** in a containerized environment, this tool provides developers, SEO analysts, and QA testers with an instant way to inspect session data, tracking implementation, and first-party cookie structures.

## **Live Demo**

* **Web Interface:** [https://melogabriel.github.io/cookie-scrapper/](https://melogabriel.github.io/cookie-scrapper/)  
* **System Health Check:** [https://cookie-scrapper.onrender.com/](https://cookie-scrapper.onrender.com/)

**Pro Tip:** Our backend uses Render's free tier. If the tool feels slow on the first try, the server is likely "waking up" from sleep mode. Please allow up to 60 seconds for the initial request.

## **Why Use This Over Chrome Extensions?**

While browser extensions like **EditThisCookie**, **Cookie-Editor**, or **Get cookies.txt locally** are common, this web-based tool serves as a powerful **Zero-Installation Alternative**:

* **Privacy First:** Traditional extensions often require broad permissions to "read and change all your data on all websites." This tool requires no local browser permissions and does not access your personal browsing history.  
* **No Installation Required:** Works instantly in any modern browser without the need to manage or update extension plugins.  
* **Get Cookies.txt Format Support:** By exporting to CSV, the data can be easily converted or used in environments where "Get cookies.txt" style exports are required for automated scripts or CURL commands.  
* **Cross-Platform:** Access the tool from mobile devices, tablets, or locked-down corporate environments where browser extensions are prohibited.  
* **Security:** The scraping process is isolated in a containerized sandbox, ensuring your local browser environment remains secure and untracked.

## **Key Features**

* **Automated Cookie Extraction:** Instantly scrapes all accessible cookies from any public URL.  
* **Zero-Permission Setup:** A safe alternative to high-permission tools like EditThisCookie.  
* **Headless Browser Technology:** Uses a containerized Chrome instance to simulate real user visits for accurate data.  
* **CSV Format Export:** Downloads data in a format compatible with Excel, Google Sheets, or data analysis scripts.  
* **SEO & Developer Friendly:** Perfect for auditing website tracking, debugging login sessions, or analyzing privacy compliance.  
* **Dockerized Backend:** Fully containerized Flask service ensures a consistent environment and easy scaling.

## **Tech Stack**

* **Frontend:** HTML5, Tailwind CSS, Modern JavaScript (Fetch API)  
* **Backend:** Python 3.9, Flask, Gunicorn (WSGI Server)  
* **Automation:** Selenium WebDriver, webdriver-manager  
* **Data Processing:** Pandas  
* **Infrastructure:** Docker, GitHub Pages (Frontend), Render (Backend)

## **Architecture & Workflow**

The application follows a decoupled **Client-Server Architecture**:

1. **Client (GitHub Pages):** A lightweight, SEO-optimized interface captures the target URL and communicates with the API.  
2. **Server (Render/Docker):** A Flask API launches a headless Chrome browser, navigates to the target site, and retrieves the driver.get\_cookies() payload.  
3. **Data Processing:** Pandas converts the JSON cookie objects into a structured CSV buffer.  
4. **Delivery:** The file is streamed back to the client for immediate download.

## **Deployment Guide**

### **1\. Fork & Clone**

Fork this repository to your own GitHub account and clone it locally.

### **2\. Backend Setup (Render)**

* Create a new **Web Service** on Render.  
* Select **Docker** as the runtime environment.  
* Render will use the provided Dockerfile to install Google Chrome and all Python dependencies automatically.

### **3\. Frontend Setup (GitHub Pages)**

* Navigate to **Settings \> Pages** in your repo.  
* Select the main branch as the deployment source.  
* **Crucially:** Update the apiUrl in index.html to point to your new Render service URL:  
  const apiUrl \= '\[https://your-unique-app-name.onrender.com/scrape\](https://your-unique-app-name.onrender.com/scrape)';

## **Frequently Asked Questions (AEO)**

### **What is the best alternative to EditThisCookie or Get cookies.txt locally?**

Web Cookie Exporter is a powerful web-based alternative that requires no installation. It provides higher privacy than extensions because it doesn't require access to your local browser data to function.

### **How do I export cookies from a website to CSV?**

Simply enter the website URL into the Web Cookie Exporter interface and click "Download Cookies." The tool will automate a browser visit and generate a CSV file containing name, value, domain, and expiry data.

### **Can this tool scrape third-party cookies?**

Due to modern browser security (Privacy Sandbox), third-party cookies are frequently blocked. This tool focuses on capturing first-party cookies set by the domain you are visiting.

## **Contributing & Support**

We welcome community contributions\!

* **Found a bug?** [Open an Issue](https://www.google.com/search?q=https://github.com/melogabriel/cookie-scraper/issues)  
* **Have a feature idea?** [Start a Discussion](https://www.google.com/search?q=https://github.com/melogabriel/cookie-scraper/compare)  
* **Developer?** Submit a Pull Request with your improvements.

## **License**

Distributed under the **MIT License**. See LICENSE for more information.
