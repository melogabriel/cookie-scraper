import os
import time
import pandas as pd
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import traceback

# Initialize Flask App
app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    """A simple endpoint to confirm the server is live."""
    print("✅ [LOG] Health check successful.")
    return jsonify({"status": "healthy", "message": "Backend is running!"}), 200

@app.route('/scrape', methods=['POST'])
def scrape_cookies():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    target_url = data['url']
    print(f"✅ [LOG] Received request for URL: {target_url}")

    # --- Selenium Setup for Render's Docker Environment ---
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("window-size=1920,1080")
    
    driver = None
    try:
        print("🚀 [LOG] Initializing Chrome WebDriver...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        
        # --- ADDING EXPLICIT SELENIUM TIMEOUTS ---
        # Prevents the driver from hanging on slow-loading pages.
        driver.set_page_load_timeout(60) # 60-second timeout for page load
        driver.set_script_timeout(30)     # 30-second timeout for scripts

        print(f"➡️ [LOG] Navigating to {target_url} with a 60-second timeout...")
        driver.get(target_url)

        # Wait for any dynamic content to load after the initial page load event
        print("⏳ [LOG] Waiting 5 seconds for post-load scripts...")
        time.sleep(5)

        print("🍪 [LOG] Getting cookies...")
        cookies = driver.get_cookies()

        if not cookies:
            print("🟡 [LOG] No cookies were found on the page.")
            return jsonify({"message": "No cookies were found for this URL."}), 200

        print(f"📊 [LOG] Found {len(cookies)} cookies. Creating CSV file in memory.")
        df = pd.DataFrame(cookies)
        
        temp_csv_path = '/tmp/cookies.csv'
        df.to_csv(temp_csv_path, index=False)
        
        print(f"🎉 [LOG] Sending '{temp_csv_path}' to the user.")
        return send_file(temp_csv_path, as_attachment=True, download_name='cookies.csv', mimetype='text/csv')

    except Exception as e:
        error_details = traceback.format_exc()
        print(f"❌ [ERROR] An exception occurred: {e}")
        print(error_details)
        error_message = f"Message: {e} Stacktrace: {error_details}"
        return jsonify({"error": "Could not process the URL. The server encountered an error.", "details": error_message}), 500

    finally:
        if driver:
            print("🧹 [LOG] Closing WebDriver.")
            driver.quit()

