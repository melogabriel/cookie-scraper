# Website Cookie Exporter

A Python-based tool using Selenium and Jupyter Notebook to automatically visit a web page, extract its cookies, and save them into a `.csv` file. This project is designed for developers, QA testers, and researchers who need to analyze the cookies set by a website.

---

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [The Challenge of Third-Party Cookies](#the-challenge-of-third-party-cookies)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Understanding the Output](#understanding-the-output)
- [Advanced Usage: Using a Persistent Profile](#advanced-usage-using-a-persistent-profile)
- [License](#license)

---

## 🚀 Introduction

This project provides a Jupyter Notebook (`cookie_exporter.ipynb`) that automates the process of web cookie extraction. It launches a real browser, navigates to a specified URL, captures all accessible cookies (primarily first-party), and exports them into a clean, readable CSV format.

This is particularly useful for:
-   Debugging website login and session issues.
-   Analyzing a site's tracking and analytics strategy.
-   Educational purposes to understand how websites use cookies.

---

## ✨ Features

-   **Automated Browser Control:** Uses **Selenium** to programmatically control a Chrome browser.
-   **Automatic Driver Management:** Integrates `webdriver-manager` to automatically download the correct browser driver, eliminating manual setup.
-   **Easy to Use:** Structured as a Jupyter Notebook, allowing you to run the script step-by-step.
-   **CSV Export:** Saves the cookie data in a universally compatible `.csv` file using the **pandas** library.
-   **Detailed Output:** Captures key cookie attributes like `name`, `value`, `domain`, `path`, `expiry`, `secure`, and `httpOnly`.

---

## 🔒 The Challenge of Third-Party Cookies

As of 2025, modern web browsers like Google Chrome have implemented significant privacy enhancements, most notably the **Privacy Sandbox initiative**, which aggressively blocks third-party tracking cookies by default.

This means that scripts like this one will primarily capture **first-party cookies** (set by the domain you are visiting). Capturing third-party cookies is often not possible because the browser itself prevents them from being set. This script is a practical demonstration of these modern privacy features in action.

---

## 🛠️ Requirements

-   Python 3.7+
-   Jupyter Notebook or JupyterLab
-   Google Chrome browser installed on your machine

The following Python libraries are required:
-   `selenium`
-   `webdriver-manager`
-   `pandas`

---


## 📖 How to Use

1.  **Launch Jupyter:**
    Open your terminal, navigate to the project directory, and run:
    ```bash
    jupyter notebook
    ```

2.  **Open the Notebook:**
    Click on `cookie_exporter.ipynb` to open it in your browser.

3.  **Configure the Target:**
    In **Cell 3**, edit the `target_url` variable to the full URL of the website you want to analyze.
    ```python
    # --- ⬇️ PASTE THE URL YOU WANT TO SCRAPE HERE ⬇️ ---
    target_url = '[https://www.example.com](https://www.example.com)'
    ```

4.  **Run the Cells:**
    Execute the cells in order from top to bottom. The main script in **Cell 4** will launch a Chrome window, perform the extraction, and close itself automatically.

5.  **Find Your File:**
    Once the script is finished, a file named `exported_cookies.csv` will be created in the same directory.

---

## 📊 Understanding the Output

The output file `exported_cookies.csv` will contain the following columns:

| Column     | Description                                                              |
| :--------- | :----------------------------------------------------------------------- |
| **name** | The name of the cookie.                                                  |
| **value** | The value stored in the cookie.                                          |
| **domain** | The domain the cookie is valid for.                                      |
| **path** | The URL path the cookie is valid for.                                    |
| **expiry** | The expiration date and time of the cookie (converted from a timestamp). |
| **secure** | `TRUE` if the cookie is only sent over HTTPS.                            |
| **httpOnly** | `TRUE` if the cookie cannot be accessed by client-side scripts.          |

---

## 💡 Advanced Usage: Using a Persistent Profile

If you need to scrape cookies from a session where you are already logged in or have accepted a cookie banner, you can configure Selenium to use a persistent Chrome profile. This loads an existing browser session with all its stored data.

See the documentation within the notebook for instructions on how to find your profile path and enable this feature.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
