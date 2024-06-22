import streamlit as st
import pyshorteners
import qrcode
from PIL import Image
from io import BytesIO

# Initialize the session state variable for URL count
if 'url_count' not in st.session_state:
    st.session_state['url_count'] = 0

# Initialize the session state variable for URL input
if 'url' not in st.session_state:
    st.session_state['url'] = ""

# Initialize the session state variable for the clear input flag
if 'clear' not in st.session_state:
    st.session_state['clear'] = False

# Function to clear the URL input and reset URL count
def clear_input():
    st.session_state['clear'] = True
    st.experimental_rerun()  # Refresh the page to clear the input field

if st.session_state['clear']:
    st.session_state['url'] = ""
    st.session_state['url_count'] = 0
    st.session_state['clear'] = False

st.title("Welcome Nexus 👋")
st.title("URL Shortener With QR Code Generation ")

url = st.text_input(" ", key='url')

# Use st.columns with specific widths for spacing
col1, _, col2 = st.columns([22, 1, 3])

with col1:
    if st.button("Generate QR Code & Tiny URL"):
        if st.session_state['url_count'] < 5:
            if url:
                try:
                    # Shorten the URL
                    s = pyshorteners.Shortener()
                    short_url = s.tinyurl.short(url)

                    # Generate QR code
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=20,
                        border=4,
                    )
                    qr.add_data(short_url)
                    qr.make(fit=True)

                    img = qr.make_image(fill_color="black", back_color="white")

                    # Display shortened URL
                    st.write("Shortened URL:", short_url)

                    # Display QR code
                    buf = BytesIO()
                    img.save(buf)
                    buf.seek(0)
                    st.image(Image.open(buf), caption="QR Code", use_column_width=True)

                    # Increment URL count
                    st.session_state['url_count'] += 1

                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.error("Please Enter A Valid URL")
        else:
            st.error("Maximum limit reached. Please purchase a premium subscription.")

        st.write("Designed & Developed: Sushant Joshi")

with col2:
    if st.button("Clear"):
        clear_input()

# Additional check to display a message when user tries to input more than 5 URLs
if st.session_state['url_count'] >= 5:
    st.error("Maximum limit reached. Please purchase a premium subscription.")
