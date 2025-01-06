# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 03:01:21 2025

@author: ASHNER_NOVILLA
"""

import streamlit as st

# Configure the page layout
st.set_page_config(layout="wide")

# Title of the Streamlit app
st.title("Power BI Goat Embedded Viewer Report")

st.markdown(
    """---
    **Tip:** You can customize the dimensions or add interactivity as needed - simply "control" + "+" or "control" + "-"
    """
)

# Description of the app
st.markdown(
    """This app allows you to view the embedded Power BI report using the public link provided."""
)

# Center the embedded Power BI iframe
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiZjBkODZjMjctNDY4MS00YjU1LWJjODktMzczNjgzMDYzNzc0IiwidCI6IjY2NTc2OGRjLWQzYWMtNGZlMS04MzNjLTU1OTZkODY5MTBhMiIsImMiOjJ9&nav=false" 
        width="1920" height="1080" style="border: none;"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# Add any additional content if needed
st.markdown(
    """---
    **Tip:** You can customize the dimensions or add interactivity as needed.
    """
)