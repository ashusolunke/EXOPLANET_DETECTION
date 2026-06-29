import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.lightcurve import fit_lightcurve, calculate_snr

def render_targets():
    st.markdown("<h1 class='page-title animate-fade-in'>Target Analysis & Parameter Estimation</h1>", unsafe_allow_html=True)
    
    # Target Search
    st.markdown("<h3 style='color: #8B5CF6;'>Search Catalog</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        target_id = st.text_input("Enter Target ID", value="KOI-456.04")
    with col2:
        st.selectbox("Filter by Status", ["All", "Confirmed", "Candidate", "False Positive"])
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_btn = st.button("RUN SCIENTIFIC ANALYSIS")
        
    st.markdown("<hr style='border-color: rgba(120, 120, 255, 0.2);'>", unsafe_allow_html=True)
    
    # Synthetic Data Generation for Demonstration
    # In a real scenario, this data would be fetched from MAST/NASA API based on target_id
    np.random.seed(hash(target_id) % 12345)
    time_pts = np.linspace(0, 10, 300)
    true_t0 = 5.0 + np.random.uniform(-1, 1)
    true_depth = np.random.uniform(0.005, 0.05)
    true_duration = np.random.uniform(0.2, 0.8)
    
    # Raw flux with a dip
    raw_flux = np.ones_like(time_pts)
    mask = np.abs(time_pts - true_t0) < (true_duration / 2.0)
    raw_flux[mask] -= true_depth
    
    # Add noise
    noise_level = np.random.uniform(0.001, 0.005)
    raw_flux += np.random.normal(0, noise_level, len(time_pts))

    # Perform Mathematical Light Curve Fitting
    fit_results = fit_lightcurve(time_pts, raw_flux)
    
    st.markdown("<h3 style='color: #00E5FF;'>Mathematical Light Curve Fitting</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #aaa;'>Utilizing non-linear least squares optimization (Scipy) to extract physical parameters.</p>", unsafe_allow_html=True)
    
    if fit_results["success"]:
        est_depth = fit_results["depth"]
        est_duration = fit_results["duration"]
        est_t0 = fit_results["t0"]
        fitted_flux = fit_results["fitted_flux"]
        
        snr = calculate_snr(raw_flux, fitted_flux, est_depth)
        
        # Determine classification heuristically for the hackathon
        if snr > 7.0 and est_depth < 0.1:
            classification = "Likely Exoplanet Transit"
            class_color = "#00FF88"
        elif snr > 7.0 and est_depth >= 0.1:
            classification = "Eclipsing Binary (Blend)"
            class_color = "#FF9800"
        else:
            classification = "Inconclusive / High Noise"
            class_color = "#FF3366"
            
        # Display extracted parameters
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"<div class='mission-card'><p style='color:#aaa; font-size:12px; margin:0;'>Estimated Depth</p><h2 style='color:#00E5FF; margin:0;'>{est_depth*10000:.1f} ppm</h2></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='mission-card'><p style='color:#aaa; font-size:12px; margin:0;'>Estimated Duration</p><h2 style='color:#8B5CF6; margin:0;'>{est_duration*24:.1f} hrs</h2></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='mission-card'><p style='color:#aaa; font-size:12px; margin:0;'>Signal-to-Noise (SNR)</p><h2 style='color:#00FF88; margin:0;'>{snr:.1f}</h2></div>", unsafe_allow_html=True)
        with c4:
            st.markdown(f"<div class='mission-card'><p style='color:#aaa; font-size:12px; margin:0;'>Signal Classification</p><h3 style='color:{class_color}; margin:0; margin-top:5px;'>{classification}</h3></div>", unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)

        # Plotting
        fig = go.Figure()
        
        # Raw Data (Scatter)
        fig.add_trace(go.Scatter(
            x=time_pts, y=raw_flux, 
            mode='markers', 
            marker=dict(color='rgba(255, 255, 255, 0.4)', size=4), 
            name='Raw Photometry'
        ))
        
        # Fitted Model (Line)
        fig.add_trace(go.Scatter(
            x=time_pts, y=fitted_flux, 
            mode='lines', 
            line=dict(color='#00E5FF', width=3), 
            name='Fitted Transit Model'
        ))
        
        fig.update_layout(
            plot_bgcolor='rgba(18,25,45,0.5)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#fff'),
            xaxis=dict(title='Time (days)', gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(title='Relative Flux', gridcolor='rgba(255,255,255,0.1)'),
            margin=dict(l=20, r=20, t=20, b=20),
            height=400,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, width="stretch")
        
    else:
        st.error(f"Curve fitting failed: {fit_results.get('error')}")
        
    st.markdown("<hr style='border-color: rgba(120, 120, 255, 0.2);'>", unsafe_allow_html=True)
    
    # Habitable Zone Simulator
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
