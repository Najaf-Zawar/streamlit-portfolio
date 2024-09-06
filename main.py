import base64
import streamlit as st
from streamlit_card import card


# Display your image
img_path = "openai.png"
with open(img_path, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")


col_1, _ = st.columns(2)

with col_1:
    hasClicked_home = card(
        title="",
        text="",
        image=data,  # Replace with your own image URL or file path
        styles={
            "card": {
                # "width": "500px",
                # "height": "500px",
                "border-radius": "50px",
                # "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "filter": {
                "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore
            }, 
        }
    )
# Page title and subtitle
st.title("Najaf Portfolio")
st.write("I am an AI Engineer with 1+ year of experience in building machine learning models, deploying AI systems, and working with data.")

# Create two columns for side-by-side card layout
col1, col2 = st.columns(2)

# Home Card in the first column
with col1:
    hasClicked_home = card(
        title="",
        text="",
        image=data,  # Replace with your own image URL or file path
        styles={
            "card": {
                # "width": "500px",
                # "height": "500px",
                "border-radius": "50px",
                # "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "filter": {
                "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore
            },
            "text": {
            "font-family": "serif",
            }   
        }
    )

# Projects Card in the second column
with col2:
    hasClicked_projects = card(
        title="Projects",
        text="View my AI and Machine Learning projects",
        image=data,  # Replace with your own image URL or file path
        styles={
            "card": {
                # "width": "500px",
                # "height": "500px",
                "border-radius": "50px",
                # "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            },
            "filter": {
                "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore
            },
            "text": {
            "font-family": "serif",
            }   
        }
    )

# Navigate based on card click
if hasClicked_home:
    st.switch_page("pages/openai.py")  # Ensure the path matches your file structure

if hasClicked_projects:
    st.switch_page("projects.py")  # Ensure the path matches your file structure
