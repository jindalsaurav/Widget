from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


FORM_HEIGHT = 760


st.set_page_config(page_title="Enquire Now", layout="centered")

st.markdown(
    """
    <style>
        .block-container {
            max-width: 720px;
            padding-top: 4rem;
            text-align: center;
        }

        div[data-testid="stButton"] button {
            min-width: 220px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_enquiry_form() -> None:
    form_page = Path(__file__).with_name("enquiry_form.html")
    components.html(
        form_page.read_text(encoding="utf-8"),
        height=FORM_HEIGHT,
        scrolling=True,
    )


if hasattr(st, "dialog"):
    @st.dialog("Enquiry Form", width="large")
    def enquiry_form_dialog() -> None:
        render_enquiry_form()


    if st.button("Open Enquiry Form", type="primary"):
        enquiry_form_dialog()
else:
    if st.button("Open Enquiry Form", type="primary"):
        render_enquiry_form()
