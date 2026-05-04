from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Enquire Now", layout="centered")

st.markdown(
    """
    <style>
        .block-container {
            max-width: 720px;
            padding-top: 4rem;
            text-align: center;
        }

        div[data-testid="stLinkButton"] a {
            min-width: 220px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.query_params.get("form") == "open":
    form_page = Path(__file__).with_name("enquiry_form.html")
    components.html(form_page.read_text(encoding="utf-8"), height=760, scrolling=True)
else:
    st.link_button("Open Enquiry Form", "?form=open", type="primary")
