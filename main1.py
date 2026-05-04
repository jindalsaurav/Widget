from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Enquire Now", layout="centered")
st.write("🔍 Debug Mode")

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

st.write("File exists:", form_page.exists())
st.write("File path:", form_page)

if form_page.exists():
    st.success("HTML file found")
else:
    st.error("HTML file missing ❌")
#st.iframe(form_page, height=760)

html_content = form_page.read_text(encoding="utf-8")
st.write("HTML loaded, length:", len(html_content))
components.html(html_content, height=760, scrolling=True)
