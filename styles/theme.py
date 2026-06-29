import streamlit as st
import os

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    try:
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Could not find style.css")

def apply_custom_theme():
    load_css()
    # Add space background effect
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #050816;
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(139, 92, 246, 0.05), transparent 25%),
                radial-gradient(circle at 85% 30%, rgba(0, 229, 255, 0.05), transparent 25%);
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
