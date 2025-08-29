# app.py - The Flask Web Server with CORS
# --- Installation ---
# pip install Flask Flask-Cors selenium webdriver-manager pandas

import io
import pandas as pd
from flask import Flask, request, render_template, Response, jsonify
from flask_cors import CORS # Import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

# Initialize the Flask application
app = Flask(__name__)
# --- NEW: Enable CORS for all routes ---
# This allows your frontend (on GitHub Pages) to make requests to this backend.
CORS(app)

# --- Main Route: Serves the HTML frontend ---
# This route is now mostly for local testing, as the main frontend will be on GitHub Pages.
@app.route('/')
def index():
    """Renders the main HTML page."""
    return "<h1>Cookie Scraper Backend</h1><p>This is the server. The frontend is hosted separately.</p>"

# --- API Route: Handles the scraping logic ---
@app.route('/scrape', methods=['POST'])
def scrape():
    """
    Receives a URL, runs the Selenium scraper in headless mode,
    and returns the cookies as a CSV file.
    """
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required."}), 400

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = None
    try:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        driver.get(url)
        cookies = driver.get_cookies()

        if not cookies:
            return jsonify({"error": "No cookies found for this URL."}), 404

        df = pd.DataFrame(cookies)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        return Response(
            csv_buffer,
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=exported_cookies.csv"}
        )

    except WebDriverException as e:
        return jsonify({"error": f"Could not process the URL. Please check if it is valid. Details: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    finally:
        if driver:
            driver.quit()

# --- Run the application ---
if __name__ == '__main__':
    # For production, use a WSGI server like Gunicorn: gunicorn app:app
    app.run(debug=False)
