# Tiny2URL

The Streamlit app titled "URL Shortener With QR Code Generation" offers a straightforward yet powerful tool for users to shorten URLs and generate corresponding QR codes. Upon launching the app, users are greeted with a clean interface where they can input any URL they wish to shorten. This input field is complemented by buttons for generating QR codes and clearing the input, neatly organized using Streamlit's column layout.

Behind the scenes, the app leverages libraries like pyshorteners to quickly shorten URLs using services like TinyURL. It also utilizes qrcode to create QR codes that encode these shortened URLs. Users receive immediate feedback with the generated shortened URL displayed alongside the QR code, making it convenient for sharing or using in various applications.To enhance user experience, the app includes session state management to keep track of how many URLs have been processed. If users attempt to exceed a predefined limit of five URLs, they are notified to consider a premium subscription for further use, demonstrating potential scalability options for monetization.



![ss qr](https://github.com/sjoshihypen/Tiny2URL/assets/79572922/5554007c-3068-4705-b90a-25e94f63bfc2)





