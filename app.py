import streamlit as st
import pandas as pd 
from PIL import Image
import os

# ---- PAGE CONFIG ---
st.set_page_config(page_title="Design-o-Pedia", page_icon="🎨", layout="wide")

# ---- HEADER ----
img_path = "dp.png"

# check if the image exists
if os.path.exists(img_path):
    img= Image.open(img_path)
    st.image(img ,caption="Dp", use_container_width=True)
else:
    st.error ("Image not found")


st.title("Design-o-Pedia")
st.markdown("Welcome to Design-o-Pedia! Showcase your web & graphic design projects.")

# ---- SIDEBAR NAVIGATION ----
page = st.sidebar.radio("Navigate", ["Home", "Submit Project", "Projects Gallery", "Resources"])

# ---- USER INPUT FORM (Submit Project) ----
def submit_project():
    st.subheader("📤 Submit Your Project")
    with st.form("project_form"):
        name = st.text_input("Your Name")
        title = st.text_input("Project Title")
        category = st.selectbox("Category", ["Web Design", "Graphic Design", "UI/UX", "Other"])
        description = st.text_area("Project Description")
        file = st.file_uploader("Upload Project File (Image, PDF, etc.)")
        behance = st.text_input("Behance Link")
        github = st.text_input("GitHub Repo")
        vercel = st.text_input("Vercel Deployment")
        streamlit_code = st.text_input("Streamlit Raw Code Link")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"✅ Thanks {name}! Your project '{title}' has been submitted.")

# ---- DISPLAY PROJECTS (Gallery) ----
def show_projects():
    st.subheader("🎭 Projects Gallery")
    sample_data = {
        "Title": ["Portfolio Website", "Minimal Logo", "E-commerce UI"],
        "Category": ["Web Design", "Graphic Design", "UI/UX"],
        "Description": ["A simple portfolio site.", "Modern minimalistic logo.", "E-commerce UI with smooth UX."],
        "Behance": ["https://behance.net/sample1", "https://behance.net/sample2", "https://behance.net/sample3"],
    }
    df = pd.DataFrame(sample_data)
    st.dataframe(df)  # Simple project display (Can be customized)

# ---- EXTERNAL RESOURCES ----
def show_resources():
    st.subheader("📌 Useful Resources Where Display Your Projects")
    st.markdown("[📂 Behance](https://www.behance.net/)")
    st.markdown("[💻 GitHub](https://github.com/)")
    st.markdown("[🚀 Vercel](https://vercel.com/)")
    st.markdown("[🖥️ Streamlit](https://streamlit.io/)")

# ---- PAGE LOGIC ----
if page == "Home":
    # st.image(img, use_container_width=True)
    st.write("Design-o-Pedia is a hub for creative minds to showcase their work.")

elif page == "Submit Project":
    submit_project()

elif page == "Projects Gallery":
    show_projects()

elif page == "Resources":
    show_resources()

# ---- FOOTER ----
st.markdown("---")
st.text("© 2025 Design-o-Pedia | Built with Streamlit")
