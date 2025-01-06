# Power BI Embedded Viewer using Streamlit

## Overview
This project is a simple Streamlit app that embeds a Power BI report using a public link. The app is configured to use a wide layout and centers the embedded report, ensuring a clean and user-friendly presentation. Additionally, the navigation bar in the Power BI report is hidden for a streamlined viewing experience.

## Features
- **Wide Layout:** The app uses Streamlit's `wide` layout for better utilization of screen space.
- **Centered Content:** The Power BI iframe is centered on the page.
- **Navigation Bar Hidden:** The `nav=false` parameter is included in the Power BI URL to hide the navigation bar.

## Prerequisites
- Python 3.7 or higher
- Streamlit library installed

## Installation
1. Clone this repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

## Usage
1. Save the code to a file named `app.py`.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided URL in your web browser to view the app.

## Customization
- **Report URL:** Update the `iframe` `src` attribute with your desired Power BI public report link.
- **Dimensions:** Modify the `width` and `height` attributes of the iframe for custom sizing.
- **Additional Content:** Add custom content to the app by using Streamlit's markdown or other layout functions.

## Example Screenshot
![image](https://github.com/user-attachments/assets/4d72321b-0e6b-4375-a03b-3650c6828f53)

## Acknowledgements
This app uses Streamlit for its lightweight and intuitive interface, making it easy to embed external content such as Power BI reports.

## Streamlit Link
https://goat-performance-dashboard.streamlit.app/
