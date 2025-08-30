# Use an official, slim Python runtime as a base image
FROM python:3.9-slim

# Set a specific working directory inside the container
WORKDIR /app

# --- Install Google Chrome ---
# First, update the package list and install necessary dependencies for Chrome
RUN apt-get update && apt-get install -y wget gnupg ca-certificates --no-install-recommends

# Download Google's signing key and add it to the system's list of trusted keys
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Add the official Google Chrome repository to the system's sources
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

# Update the package list again (to include Chrome) and install the stable version of Chrome
RUN apt-get update && apt-get install -y google-chrome-stable --no-install-recommends

# --- Install Python Dependencies ---
# Copy only the requirements file first to leverage Docker's layer caching
COPY requirements.txt .

# Install the Python packages specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy Application Code ---
# Copy the rest of your application's code into the working directory
COPY . .

# --- Run the Application ---
# Expose the port the app will run on
EXPOSE 10000

# Set the command to run your application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]

