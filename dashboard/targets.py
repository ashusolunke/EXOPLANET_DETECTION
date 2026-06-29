import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

def render_targets():
    st.markdown("<h1 class='page-title animate-fade-in'>Target Analysis</h1>", unsafe_allow_html=True)
    
    # Target Search
    st.markdown("<h3 style='color: #8B5CF6;'>Search Catalog</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.text_input("Enter Target ID (TOI, KOI, or Name)", placeholder="e.g. KOI-456.04")
    with col2:
        st.selectbox("Filter by Status", ["All", "Confirmed", "Candidate", "False Positive"])
    with col3:
        st.button("SEARCH TARGET")
        
    st.markdown("<hr style='border-color: rgba(120, 120, 255, 0.2);'>", unsafe_allow_html=True)
    
    # Transit Visualization
    st.markdown("<h3 style='color: #00E5FF;'>Transit Visualization</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #aaa;'>Animated transit light curve analysis</p>", unsafe_allow_html=True)
    
    # Generate mock light curve data
    time_pts = np.linspace(0, 10, 200)
    flux = np.ones_like(time_pts)
    # create a dip (transit)
    dip_center = 5
    dip_width = 0.5
    transit_mask = np.abs(time_pts - dip_center) < dip_width
    flux[transit_mask] -= 0.02 * np.cos((time_pts[transit_mask] - dip_center) / dip_width * np.pi/2)
    # add noise
    flux += np.random.normal(0, 0.001, len(time_pts))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_pts, y=flux, mode='markers', marker=dict(color='#00E5FF', size=4), name='Flux'))
    fig.update_layout(
        plot_bgcolor='rgba(18,25,45,0.5)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#fff'),
        xaxis=dict(title='Time (days)', gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(title='Relative Flux', gridcolor='rgba(255,255,255,0.1)'),
        margin=dict(l=20, r=20, t=20, b=20),
        height=300
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Control buttons for transit
    c1, c2, c3 = st.columns(3)
    with c1: st.button("▶ PLAY ANIMATION")
    with c2: st.button("⏸ PAUSE")
    with c3: st.button("🔄 REPLAY")
    
    st.markdown("<hr style='border-color: rgba(120, 120, 255, 0.2);'>", unsafe_allow_html=True)
    
    # Habitable Zone
    st.markdown("<h3 style='color: #00FF88;'>Habitable Zone Simulator</h3>", unsafe_allow_html=True)
    
    orbit_distance = st.slider("Orbital Distance (AU)", min_value=0.1, max_value=2.0, value=1.0, step=0.01)
    
    hz_status = "Habitable" if 0.9 <= orbit_distance <= 1.2 else ("Too Hot" if orbit_distance < 0.9 else "Too Cold")
    hz_color = "#00FF88" if hz_status == "Habitable" else ("#FF9800" if hz_status == "Too Hot" else "#00E5FF")
    
    st.markdown(
        f"""
        <div class="mission-card" style="text-align: center;">
            <p style="color: #aaa; margin: 0;">Predicted Climate Status</p>
            <h2 style="color: {hz_color}; margin: 10px 0;">{hz_status}</h2>
            <div style="width: 100%; height: 20px; background: linear-gradient(90deg, #FF9800, #00FF88, #00E5FF); border-radius: 10px; position: relative;">
                <div style="position: absolute; left: {(orbit_distance/2.0)*100}%; top: -5px; width: 6px; height: 30px; background: white; border-radius: 3px; box-shadow: 0 0 10px white;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 5px; color: #aaa; font-size: 0.8rem;">
                <span>0.1 AU</span>
                <span>2.0 AU</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
