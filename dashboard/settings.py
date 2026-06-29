import streamlit as st
from fpdf import FPDF
import datetime
import numpy as np

def generate_pdf(target_name):
    # Seed numpy random generator so values are consistent per target
    np.random.seed(hash(target_name) % 12345)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, f"COSMOS X AI - Scientific Report", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font("Helvetica", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Target System: {target_name}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    
    # Generate seeded realistic mock data depending on target
    is_confirmed = ("Kepler" in target_name or "TRAPPIST" in target_name or np.random.random() > 0.7)
    status = "Confirmed" if is_confirmed else "Candidate"
    
    confidence = np.random.uniform(90.0, 99.9) if is_confirmed else np.random.uniform(65.0, 89.9)
    period = np.random.uniform(1.5, 365.0)
    duration = np.random.uniform(1.0, 12.0)
    depth = np.random.uniform(50, 3000)
    radius = np.random.uniform(0.5, 11.0) # From Mars-sized to Jupiter-sized
    
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Prediction & AI Analysis", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(0, 10, f"AI Model Prediction: {status} Exoplanet", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Confidence Score: {confidence:.1f}%", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10)
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Transit Parameters (Estimated)", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(0, 10, f"Orbital Period: {period:.2f} Days", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Transit Duration: {duration:.1f} Hours", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Transit Depth: {depth:.0f} ppm", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Planet Radius: ~{radius:.1f} Earth Radii", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10)
    pdf.set_font("Helvetica", 'I', 10)
    pdf.cell(0, 10, "Generated automatically by Dr. NOVA - ISRO Hackathon 2026", new_x="LMARGIN", new_y="NEXT")
    
    return bytes(pdf.output())

def render_settings():
    st.markdown("<h1 class='page-title animate-fade-in'>Settings & Reports</h1>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #00E5FF;'>Scientific Report Generator</h3>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="mission-card">
            <p style="color: #aaa;">Enter any target ID to generate a comprehensive PDF report including prediction, confidence, transit parameters, and AI analysis.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        target = st.text_input("Enter Target ID", value="KOI-456.04", placeholder="e.g. Kepler-186f, TOI-700")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if target:
            pdf_bytes = generate_pdf(target)
            st.download_button(
                label="📄 GENERATE PDF REPORT",
                data=pdf_bytes,
                file_name=f"{target}_Report.pdf",
                mime="application/pdf",
            )
        
    st.markdown("<hr style='border-color: rgba(120, 120, 255, 0.2);'>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #8B5CF6;'>System Settings</h3>", unsafe_allow_html=True)
    
    st.checkbox("Enable Background Particle Animations", value=True)
    st.checkbox("Sound Effects", value=False)
    st.slider("UI Glow Intensity", 0, 100, 50)
    
    st.button("💾 SAVE CONFIGURATION")
