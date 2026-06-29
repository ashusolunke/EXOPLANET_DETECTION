import streamlit as st
import streamlit.components.v1 as components
import os

def render_galaxy_explorer():
    st.markdown("<h1 class='page-title animate-fade-in'>Galaxy Explorer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #aaa; margin-top: -20px; margin-bottom: 20px;'>Interactive 3D visualization of exoplanetary systems. Click on glowing systems to view details.</p>", unsafe_allow_html=True)
    
    # Read the HTML file
    try:
        html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "threejs", "galaxy.html")
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # Render the component
        components.html(html_content, height=700, scrolling=False)
    except FileNotFoundError:
        st.error("Error: threejs/galaxy.html not found.")
