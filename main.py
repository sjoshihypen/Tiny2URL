import streamlit as st
import pyshorteners
import qrcode
import mysql.connector
from PIL import Image
from io import BytesIO
from streamlit_option_menu import option_menu
import time

# Initialize session state
if 'url_count' not in st.session_state:
    st.session_state['url_count'] = 0
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'selected_menu' not in st.session_state:
    st.session_state['selected_menu'] = "Home"

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

with st.sidebar:
    selected = option_menu(
        menu_title="Tiny2QR",
        options=["Home", "Contact", "Signup", "Login"],
        icons=["house", "envelope", "door-open", "key"],
        default_index=0,
        orientation="vertical",
        menu_icon="cast",
        styles={
            "icon": {"font-size": "17px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "3px", "--hover-color": "#262730"}
        },
        key="sidebar_menu"
    )

    st.session_state['selected_menu'] = selected

    if selected == "Contact":
        st.write("\n\n")
        st.write("# Contact Us")
        with st.form("Contact"):
            CName = st.text_input('Name', placeholder='Enter Name')
            CPhone = st.text_input('Mobile', placeholder='Enter Mobile')
            CEmail = st.text_input('Email', placeholder='Enter Email')
            CMessage = st.text_area('Message', placeholder='Enter Your Message Here...')
            st.write("\n\n")
            Contact_submit = st.form_submit_button('Submit')
            if Contact_submit:
                st.success("Shortly We Will Reach You\n Thanks for Valuable Feedback...", icon="✅")
        st.write("\n\n")

    if selected == "Signup":
        st.write("\n\n")
        st.write("# Hello 👋, Sign Up Here")
        with st.form("Registration"):
            conn = init_connection()
            RName = st.text_input('Name', placeholder='Enter Name')
            RPhone = st.text_input('Mobile', placeholder='Enter Mobile')
            REmail = st.text_input('Email', placeholder='Enter Email')
            RPassword = st.text_input('Password', placeholder='Enter Password', type="password")
            st.write("\n\n")
            Signup = st.form_submit_button('Register Me')
            if Signup:
                cursor = conn.cursor()
                sql = f"""INSERT INTO register(Fname, Phone, Email, Pass) VALUES ('{RName}', '{RPhone}', '{REmail}', '{RPassword}')"""
                cursor.execute(sql)
                conn.commit()
                st.success("Congratulations! You are part of Tiny2URL", icon="✅")

    if selected == "Login":
        st.write("\n\n")
        st.write("# Hello 👋, Login Here")
        with st.form("Login"):
            conn = init_connection()
            LEmail = st.text_input('Email', placeholder='Enter Email')
            LPassword = st.text_input('Password', placeholder='Enter Password', type="password")
            st.write("\n\n")
            Login = st.form_submit_button('Login')
            if Login:
                cursor = conn.cursor()
                sql = f"""SELECT * FROM register WHERE Email = '{LEmail}' AND Pass = '{LPassword}';"""
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 1:
                    st.session_state['logged_in'] = True
                    st.session_state['user'] = LEmail
                    st.success("Welcome! Logged in Successfully", icon="✅")
                else:
                    st.error("OOPS!!! Invalid ID or Password", icon="🚨")
        st.write("\n\n")

if st.session_state['logged_in']:
    st.title("URL Shortener With QR Code Generation")
    st.write("Enter A URL To Shorten & Generate A QR Code:")

    url = st.text_input("URL")

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
else:
    st.title("Welcome Tiny2QR")
    st.write("Signup to access the URL Shortener & QR Code Generation features...🔐😊 ")

    # Image slider
    st.write("### Check out some features")
    images = ["Images/QR.png", "Images/QR1.png", "Images/QR2.png"]  # Add your image paths here
    placeholder = st.empty()

    while True:
        for i in range(len(images)):
            img = Image.open(images[i])
            placeholder.image(img, caption=f"Image {i+1}", use_column_width=True)
            time.sleep(3)  # Wait for 3 seconds before showing the next image
