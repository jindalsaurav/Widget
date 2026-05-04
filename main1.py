from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Enquire Now", layout="centered")

st.markdown(
    """
    <style>
        .block-container {
            max-width: 720px;
            padding: 0.5rem;
        }

        iframe {
            display: block;
            width: 100%;
            min-height: 760px;
            border: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

form_page = Path(__file__).with_name("enquiry_form.html")

st.iframe(form_page, height=760)
