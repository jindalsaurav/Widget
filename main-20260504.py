import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Enquire Now", layout="centered")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enquire Now</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            min-height: 100vh;
            padding: 20px;
        }

        /* Ensure button is clickable and on top */
        .npfWidgetButton {
            z-index: 999999 !important;
            padding: 10px 20px;
            background-color: #ff0000;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
    </style>
</head>

<body>

<h2>Welcome</h2>
<p>Click below to open enquiry form:</p>

<!-- Button to trigger popup -->
<button type="button" class="npfWidgetButton npfWidget-249018df2e55bbbfa2ad419f91c0d54e">
    Click Here!
</button>

<!-- Embedded form container -->
<div class="npf_wgts" data-height="400px" data-w="249018df2e55bbbfa2ad419f91c0d54e"></div>

<!-- Load Popup Script -->
<script src="https://cdn.npfs.co/js/widget/npfwpopup.js"></script>

<!-- Initialize Widget AFTER script loads -->
<script>
window.onload = function () {
    new NpfWidgetsInit({
        "widgetId":"249018df2e55bbbfa2ad419f91c0d54e",
        "baseurl":"widgets.nopaperforms.com",
        "formTitle":"Feedback Form",
        "titleColor":"#FF0033",
        "backgroundColor":"#ddd",
        "iframeHeight":"500px",
        "buttonbgColor":"#ff0000",
        "buttonTextColor":"#FFF"
    });
};
</script>

<!-- Load Embed Widget Script -->
<script type="text/javascript">
var s = document.createElement("script");
s.type = "text/javascript";
s.async = true;
s.src = "https://widgets.nopaperforms.com/emwgts.js";
document.body.appendChild(s);
</script>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
