# Use an official, slim Python runtime as a base image
FROM python:3.9-slim

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Set a specific working directory inside the container
WORKDIR /app

# --- Install Google Chrome & Dependencies ---
# Update package list and install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    --no-install-recommends

# Add Google's official GPG key using the modern, recommended method
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome-archive-keyring.gpg

# Add the Google Chrome repository
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Update package list again and install Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends

# Clean up apt cache to reduce image size
RUN rm -rf /var/lib/apt/lists/*

# --- Install Python Dependencies ---
# Copy only the requirements file first to leverage caching
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy Application Code ---
COPY . .

# --- Run the Application ---
# Expose the port Gunicorn will run on
EXPOSE 10000

# Set the command to run Gunicorn with a longer timeout (120 seconds)
# This is the key fix to prevent the server from timing out during scraping.
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--timeout", "120", "app:app"]

