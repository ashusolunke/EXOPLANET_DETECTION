import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 30px;">
                <h2 style="color: #00E5FF; text-shadow: 0 0 10px rgba(0, 229, 255, 0.5); letter-spacing: 2px;">COSMOS X AI</h2>
                <p style="color: #8B5CF6; font-size: 0.8rem; text-transform: uppercase;">Mission Control System</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Navigation
        st.markdown("<h3 style='color: rgba(255,255,255,0.5); font-size: 0.9rem; margin-bottom: 15px;'>NAVIGATION</h3>", unsafe_allow_html=True)
        
        page = st.radio(
            "Select Module",
            ["Dashboard", "Galaxy Explorer", "Targets", "Favorites", "Mission Status", "Settings"],
            label_visibility="collapsed"
        )
        
        st.markdown("<hr style='border-color: rgba(120, 120, 255, 0.2);'>", unsafe_allow_html=True)
        
        # System Status Indicators
        st.markdown(
            """
            <div style="margin-top: 20px;">
                <p style="font-size: 0.8rem; color: #aaa;">SYSTEM STATUS</p>
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #00FF88; box-shadow: 0 0 8px #00FF88; margin-right: 10px;"></div>
                    <span style="color: #fff; font-size: 0.9rem;">AI Core Online</span>
                </div>
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #00FF88; box-shadow: 0 0 8px #00FF88; margin-right: 10px;"></div>
                    <span style="color: #fff; font-size: 0.9rem;">Telemetry Sync</span>
                </div>
                <div style="display: flex; align-items: center;">
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #00E5FF; box-shadow: 0 0 8px #00E5FF; margin-right: 10px; animation: blink 2s infinite;"></div>
                    <span style="color: #fff; font-size: 0.9rem;">Model Ready</span>
                </div>
            </div>
            <style>
                @keyframes blink { 0% {opacity: 1;} 50% {opacity: 0.5;} 100% {opacity: 1;} }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        return page
