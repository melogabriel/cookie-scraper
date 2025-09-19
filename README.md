# Web Cookie Exporter

A full-stack web application that allows users to enter a URL and download the website's cookies as a `.csv` file. The frontend is hosted on GitHub Pages, and the backend is a containerized Flask and Selenium service deployed on Render.

## Live Demo

  * **Frontend Interface:** https://melogabriel.github.io/cookie-scraper/
  * **Backend Health Check:** https://cookie-scrapper.onrender.com/

**Note:** The backend is hosted on Render's free tier and will "go to sleep" after 15 minutes of inactivity. The first request may take up to a minute to "wake up" the service.

## Features

  * **User-Friendly Web Interface:** A clean, simple frontend for entering a target URL.
  * **Server-Side Scraping:** Utilizes a powerful backend to handle browser automation.
  * **Headless Chrome Automation:** Uses **Selenium** to run a headless Chrome instance in a Docker container.
  * **CSV Export:** Dynamically generates and serves a `.csv` file of the captured cookies.
  * **Robust Error Handling:** Provides clear feedback to the user if the server times out or encounters an error.
  * **Containerized & Scalable:** Uses **Docker** for a consistent and reproducible deployment environment.

## Tech Stack

  * **Backend:** Python, Flask, Gunicorn
  * **Web Scraping:** Selenium, webdriver-manager
  * **Data Handling:** pandas
  * **Frontend:** HTML, Tailwind CSS, JavaScript (`fetch` API)
  * **Deployment:** Docker, GitHub Pages, Render

## Architecture

This project uses a client-server model, separating the user interface from the heavy processing work.

  * **Frontend (Client):** A static `index.html` file hosted on **GitHub Pages**. It captures the user's input and uses JavaScript to make an API call to the backend.
  * **Backend (Server):** A **Flask** application running inside a **Docker** container on **Render**. It exposes a `/scrape` API endpoint that receives a URL, launches a headless Chrome browser using Selenium, scrapes the cookies, and sends back a CSV file.

## Deployment Instructions

To deploy your own version of this application, follow these steps:

1.  **Fork this Repository:**
    Click the "Fork" button at the top right of this page to create your own copy.

2.  **Deploy the Backend to Render:**
    a. Create a new "Web Service" on Render and connect it to your forked repository.
    b. **Crucially, set the "Environment" to `Docker`**.
    c. Render will automatically detect your `Dockerfile`. Use the default settings for the service name and branch.
    d. Click **"Create Web Service"**. The first build may take several minutes as it installs Google Chrome inside the container.

3.  **Configure GitHub Pages for the Frontend:**
    a. In your forked repository, go to **Settings \> Pages**.
    b. Under "Build and deployment," select the source as **`Deploy from a branch`**.
    c. Set the branch to **`main`** and the folder to **`/ (root)`**. Click **Save**.

4.  **Connect Frontend to Backend:**
    a. Once your Render service is live, copy its URL (e.g., `https://your-app-name.onrender.com`).
    b. In your GitHub repository, edit the `index.html` file.
    c. Find the `apiUrl` variable in the `<script>` section and replace the placeholder URL with your live Render URL.

    ```javascript
    // Change this line in index.html
    const apiUrl = 'https://your-app-name.onrender.com/scrape';
    ```

    d. Commit and push this change. Your GitHub Pages site will update automatically.

## Troubleshooting

**"Network Error: Could not connect to the server."**
This is the most common issue. It means your browser timed out waiting for a response.

  * **Cause:** The free server on Render "goes to sleep." The first request has to wake it up, which can take over 30 seconds.
  * **Solution:** First, visit your backend URL (e.g., `https://your-app-name.onrender.com/`) to wake the server up. Once you see the `{"status":"healthy"}` message, go back to your frontend and try again.

**"Error: Could not process the URL..."**
This means the backend started but crashed while running Selenium.

  * **Cause:** The target website might be slow, or there could be an issue with the Chrome driver.
  * **Solution:** Check the **"Logs"** tab for your service on Render. The traceback will provide details on the specific error. The backend code includes a 120-second timeout to handle most cases.

## License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
