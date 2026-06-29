import streamlit as st
import os

# Set page configuration
st.set_page_config(
    page_title="COSMOS X AI | Mission Control",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import internal modules
from styles.theme import apply_custom_theme
from components.sidebar import render_sidebar
from dashboard.home import render_home

def main():
    # Apply custom CSS and animations
    apply_custom_theme()
    
    # Render Sidebar and get navigation state
    current_page = render_sidebar()
    
    # Route to the selected page
    if current_page == "Dashboard":
        render_home()
    elif current_page == "Galaxy Explorer":
        from dashboard.galaxy_explorer import render_galaxy_explorer
        render_galaxy_explorer()
    elif current_page == "Targets":
        from dashboard.targets import render_targets
        render_targets()
    elif current_page == "Mission Status":
        from dashboard.mission_status import render_mission_status
        render_mission_status()
    elif current_page == "Settings":
        from dashboard.settings import render_settings
        render_settings()
    elif current_page == "Favorites":
        st.markdown("<h1 class='page-title'>Favorites</h1>", unsafe_allow_html=True)
        st.info("No favorites selected yet. Add targets from the Explorer.")
    else:
        st.markdown(f"<h1 class='page-title'>{current_page}</h1>", unsafe_allow_html=True)
        st.info("Module under construction.")

if __name__ == "__main__":
    main()