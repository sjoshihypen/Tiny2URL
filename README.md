# Tiny2URL

The Streamlit app titled "URL Shortener With QR Code Generation" offers a straightforward yet powerful tool for users to shorten URLs and generate corresponding QR codes. Upon launching the app, users are greeted with a clean interface where they can input any URL they wish to shorten. This input field is complemented by buttons for generating QR codes and clearing the input, neatly organized using Streamlit's column layout.

Behind the scenes, the app leverages libraries like pyshorteners to quickly shorten URLs using services like TinyURL. It also utilizes qrcode to create QR codes that encode these shortened URLs. Users receive immediate feedback with the generated shortened URL displayed alongside the QR code, making it convenient for sharing or using in various applications.To enhance user experience, the app includes session state management to keep track of how many URLs have been processed. If users attempt to exceed a predefined limit of five URLs, they are notified to consider a premium subscription for further use, demonstrating potential scalability options for monetization.


# Steps to Download and Run the Streamlit Project
# 1. Prepare Your Streamlit Project:
     Ensure your Streamlit app script (app.py or any other filename) is ready with all dependencies and necessary files (e.g., images, if used).
# 2. Setup Requirements:
     Create a requirements.txt file listing all Python dependencies required by your Streamlit app. 
     Include packages like streamlit, pyshorteners, qrcode, and Pillow (PIL).
**Example :  requirements.txt:**
             streamlit
             pyshorteners
             qrcode
             Pillow
# 3. Instructions for Users:
     Provide clear instructions for users on how to set up and run your Streamlit app. 
     You can include these instructions in a README.md file.
# Streamlit URL Shortener with QR Code Generation
**Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
**1. Install dependencies:**
    bash
    pip install -r requirements.txt
**2.Run the Streamlit app:**
    bash
    streamlit run app.py
**3. Access the app:**
    Open a web browser and go to http://localhost:8501 (or the URL shown in the terminal after running Streamlit).
    Use the app interface to shorten URLs, generate QR codes, and manage sessions.
# 4. Functionality
Shorten URLs: Enter a URL to get a shortened version and generate a QR code.
Clear Inputs: Use the "Clear" button to reset input fields.
Session Management: Limits users to generating a maximum of 5 URLs unless they log in or purchase a premium subscription.
Enjoy using the app!
Welcome to the Nexus Streamlit app for URL shortening and QR code generation!
![ss qr](https://github.com/sjoshihypen/Tiny2URL/assets/79572922/6d972197-4726-40af-9896-10002cfafe15)




