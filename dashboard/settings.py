import streamlit as st

def render_settings():
    st.markdown("<h1 class='page-title animate-fade-in'>Settings & Reports</h1>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #00E5FF;'>Scientific Report Generator</h3>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="mission-card">
            <p style="color: #aaa;">Select a target to generate a comprehensive PDF report including prediction, confidence, transit parameters, and AI analysis.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Select Target", ["KOI-456.04", "Kepler-186f", "TRAPPIST-1e"])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("📄 GENERATE PDF REPORT")
        
    st.markdown("<hr style='border-color: rgba(120, 120, 255, 0.2);'>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #8B5CF6;'>System Settings</h3>", unsafe_allow_html=True)
    
    st.checkbox("Enable Background Particle Animations", value=True)
    st.checkbox("Sound Effects", value=False)
    st.slider("UI Glow Intensity", 0, 100, 50)
    
    st.button("💾 SAVE CONFIGURATION")
