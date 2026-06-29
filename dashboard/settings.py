import streamlit as st
from fpdf import FPDF
import datetime

def generate_pdf(target_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, f"COSMOS X AI - Scientific Report", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font("Helvetica", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Target System: {target_name}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    
    # Mock data depending on target
    status = "Confirmed" if "Kepler" in target_name or "TRAPPIST" in target_name else "Candidate"
    confidence = "99.9%" if status == "Confirmed" else "84.5%"
    
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Prediction & AI Analysis", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(0, 10, f"AI Model Prediction: {status} Exoplanet", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Confidence Score: {confidence}", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10)
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Transit Parameters (Estimated)", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", '', 12)
    pdf.cell(0, 10, "Orbital Period: Varies by target", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, "Transit Duration: ~4.5 Hours", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, "Transit Depth: 500 ppm", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, "Planet Radius: ~1.5 Earth Radii", new_x="LMARGIN", new_y="NEXT")
    
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
            <p style="color: #aaa;">Select a target to generate a comprehensive PDF report including prediction, confidence, transit parameters, and AI analysis.</p>
        </div>
        """, unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        target = st.selectbox("Select Target", ["KOI-456.04", "Kepler-186f", "TRAPPIST-1e"])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
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
