<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Scraper</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        .spinner {
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-top-color: #fff;
            border-radius: 50%;
            width: 16px;
            height: 16px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-lg shadow-xl w-full max-w-lg mx-4">
        <h1 class="text-2xl font-bold text-center text-gray-800 mb-2">Website Cookie Exporter</h1>
        <p class="text-center text-gray-500 mb-6">Enter a URL to download its cookies as a .csv file.</p>
        
        <form id="cookie-form">
            <div class="mb-4">
                <label for="url-input" class="block text-gray-700 text-sm font-bold mb-2">Target URL</label>
                <input type="url" id="url-input" placeholder="https://www.google.com" required
                       class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <button type="submit" id="submitButton"
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition-colors duration-300 flex items-center justify-center">
                <span id="buttonText">Download Cookies</span>
                <div id="buttonSpinner" class="spinner hidden"></div>
            </button>
        </form>

        <div id="messageDiv" class="mt-4 text-center text-sm text-gray-600 min-h-[40px] p-2 border border-transparent rounded-md"></div>
    </div>

    <script>
        document.getElementById('cookie-form').addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const url = document.getElementById('url-input').value;
            const submitButton = document.getElementById('submitButton');
            const buttonText = document.getElementById('buttonText');
            const buttonSpinner = document.getElementById('buttonSpinner');
            const messageDiv = document.getElementById('messageDiv');

            // --- UI Feedback ---
            submitButton.disabled = true;
            buttonText.classList.add('hidden');
            buttonSpinner.classList.remove('hidden');
            messageDiv.className = 'mt-4 text-center text-sm p-2 border rounded-md border-blue-200 bg-blue-50 text-blue-700';
            messageDiv.innerHTML = 'Connecting to the server... <br><small>This may take up to a minute if the server is waking up from sleep.</small>';

            try {
                // --- Use your new, working Render URL ---
                const apiUrl = 'https://cookie-scrapper.onrender.com/scrape'; 
                
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url: url })
                });

                if (response.ok) {
                    const contentType = response.headers.get("content-type");
                    if (contentType && contentType.includes("text/csv")) {
                        messageDiv.className = 'mt-4 text-center text-sm p-2 border rounded-md border-green-200 bg-green-50 text-green-700';
                        messageDiv.textContent = 'Success! Your download is starting.';
                        const blob = await response.blob();
                        const downloadUrl = window.URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.href = downloadUrl;
                        a.download = 'cookies.csv';
                        document.body.appendChild(a);
                        a.click();
                        a.remove();
                    } else {
                        const result = await response.json();
                        messageDiv.className = 'mt-4 text-center text-sm p-2 border rounded-md border-gray-200 bg-gray-50 text-gray-700';
                        messageDiv.textContent = result.message || 'Received a success response but no file.';
                    }
                } else {
                    const errorData = await response.json();
                    messageDiv.className = 'mt-4 text-center text-sm p-2 border rounded-md border-red-200 bg-red-50 text-red-700';
                    messageDiv.innerHTML = `<strong>Error:</strong> ${errorData.error}<br><small class="text-xs">${errorData.details || ''}</small>`;
                }

            } catch (error) {
                console.error('Fetch error:', error);
                messageDiv.className = 'mt-4 text-center text-sm p-2 border rounded-md border-red-200 bg-red-50 text-red-700';
                messageDiv.innerHTML = '<strong>Network Error:</strong> Could not connect to the server. It might be asleep or has crashed. Please try again in a minute.';
            } finally {
                submitButton.disabled = false;
                buttonText.classList.remove('hidden');
                buttonSpinner.classList.add('hidden');
            }
        });
    </script>
</body>
</html>

