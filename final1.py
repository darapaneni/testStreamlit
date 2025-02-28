import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import pydicom
from io import BytesIO
import base64

# Explicitly set the environment variable
os.environ['GOOGLE_API_KEY'] = "AIzaSyA1Su6Tn9Anjdjp5hyVw_8-UINvWxwfYf8"

# API configuration
#api_key = os.getenv('GOOGLE_API_KEY')
api_key = "AIzaSyA1Su6Tn9Anjdjp5hyVw_8-UINvWxwfYf8"
genai.configure(api_key=api_key)
image_model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model version

def get_caption(prompts, platform, image):
    max_length = 20
    min_length = 10
    captions = []
    unwanted_captions = [
        "This is a medical image and it's not appropriate to generate a caption for it. Medical images are sensitive and should only be interpreted by qualified medical professionals.",
        "This is a medical image and it is not appropriate to provide a caption for it. Medical images are often sensitive and require professional interpretation.",
        "This is a medical image and it is not appropriate to provide a caption for it. Medical images are sensitive and should only be interpreted by qualified medical professionals."
    ]

    for prompt in prompts:
        if platform is None:
            text = f"{prompt}. Generate a caption for this image with a max length of {max_length} and min length of {min_length}."
        else:
            text = f"{prompt}. Generate a caption for this image for {platform} with a max length of {max_length} and min length of {min_length}."
        
        response = image_model.generate_content([text, image])
        if response.text not in unwanted_captions:
            captions.append(response.text)

    return captions

def generate_paragraph_report(captions, platform):
    report = "## GL AI Gen Radiology Report\n\n"
    report += f" {platform}\n\n" if platform else "**** \n\n"
    if captions:
        report += "### Report:\n\n"
        # Join captions into a single paragraph with appropriate punctuation
        report += " ".join(captions)
    else:
        report += "No captions were generated.\n\n"
    return report

def dicom_to_image(dicom_file):
    ds = pydicom.dcmread(dicom_file)
    pixel_array = ds.pixel_array
    image = Image.fromarray(pixel_array)
    return image

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to the logo
logo_path = "techDocsLogo.png"  # Replace with the actual path to your logo
logo_base64 = get_base64_image(logo_path)

# Display the logo at the top right corner using HTML and CSS
st.markdown(
    f"""
    <style>
    .top-right-logo {{
        position: fixed;
        top: 100px;
        right: 20px;
        width: 400px;
        height: 100px;
    }}
    </style>
    <img src="data:image/png;base64,{logo_base64}" class="top-right-logo">
    """,
    unsafe_allow_html=True
)

st.title("GL AI Gen Radiology Report")
st.write("This app generates detailed paragraph reports for multiple images based on your prompts.")

# Initialize session state for authentication
#if "authenticated" not in st.session_state:
#    st.session_state.authenticated = True

# Default credentials
DEFAULT_USERNAME = "narayana"
DEFAULT_EMAIL = "darapaneni@gmail.com"
DEFAULT_PASSWORD = "123"

# Login page
authenticated = True
#if not st.session_state.authenticated:
if authenticated:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")

    if st.button("Login"):
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD and email == DEFAULT_EMAIL:
            #st.session_state.authenticated = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials. Please try again.")

# Main app
#if st.session_state.authenticated:
if authenticated:
    uploaded_files = st.file_uploader("Choose images or DICOM files...", type=["jpg", "jpeg", "png", "dcm"], accept_multiple_files=True)

    # Multi-line text input for prompts
    prompts = st.text_area("Enter prompts for the captions (one per line)").split('\n')

    if st.button("Generate Reports"):
        if uploaded_files:
            for uploaded_file in uploaded_files:
                file_extension = os.path.splitext(uploaded_file.name)[1].lower()
                if file_extension == ".dcm":
                    # Convert DICOM to image
                    image = dicom_to_image(uploaded_file)
                else:
                    # Load the image directly
                    image = Image.open(uploaded_file)

                st.image(image, caption="Uploaded Image.", use_column_width=True)
                st.write("")
                st.write("Generating report for this image...")
                try:
                    captions = get_caption(prompts, None, image)
                    report = generate_paragraph_report(captions, None)
                    st.markdown(report)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.info("Please ensure the Generative Language API is enabled and try again.")
                st.write("-----")  # Separator between reports
        else:
            st.write("Please upload at least one image file.")
else:
    st.write("Please log in to access the app.")
