import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

def render_metric_card(label, value, delta, delay=0):
    """Renders a custom HTML metric card with glassmorphism and animation"""
    st.markdown(
        f"""
        <div class="mission-card animate-fade-in" style="animation-delay: {delay}s;">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta">{delta}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_home():
    st.markdown("<h1 class='page-title animate-fade-in'>Mission Control</h1>", unsafe_allow_html=True)
    
    # Overview Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_metric_card("Total Systems", "5,241", "+12 this week", delay=0.1)
    with col2:
        render_metric_card("Confirmed Planets", "4,102", "+5 this week", delay=0.2)
    with col3:
        render_metric_card("Candidate Planets", "1,139", "Pending verification", delay=0.3)
    with col4:
        render_metric_card("Habitable Candidates", "42", "High priority", delay=0.4)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Secondary Row
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.markdown("<h3 style='color: #00E5FF; padding-left:10px;'>Global Telemetry</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #aaa; padding-left:10px;'>Simulated live Kepler & TESS synchronized datastream.</p>", unsafe_allow_html=True)
        
        # Generate simulated live telemetry data
        np.random.seed(int(time.time() % 100)) # Change slightly over time
        x_time = np.linspace(0, 100, 200)
        y_flux_1 = 1.0 + np.random.normal(0, 0.005, 200) + np.sin(x_time / 5.0) * 0.01
        y_flux_2 = 1.0 + np.random.normal(0, 0.003, 200) + np.cos(x_time / 3.0) * 0.005
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_time, y=y_flux_1, mode='lines', line=dict(color='#00E5FF', width=1.5), name='TESS Sector 42'))
        fig.add_trace(go.Scatter(x=x_time, y=y_flux_2, mode='lines', line=dict(color='#8B5CF6', width=1.5), name='Kepler Field K2'))
        
        fig.update_layout(
            plot_bgcolor='rgba(18,25,45,0.4)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#fff'),
            xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', showticklabels=False, title='Time (Live)'),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title='Normalized Flux'),
            margin=dict(l=10, r=10, t=10, b=10),
            height=280,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, width="stretch")
        
    with col_b:
        st.markdown("<h3 style='color: #00FF88;'>AI Scientist Core</h3>", unsafe_allow_html=True)
        
        st.markdown(
            """
            <div style="margin-top: 10px; background: rgba(18,25,45,0.5); padding: 15px; border-radius: 10px; border: 1px solid rgba(139, 92, 246, 0.3);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span style="color: #fff;">Average Confidence</span>
                    <span style="color: #00E5FF; font-weight: bold;">94.2%</span>
                </div>
                <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px;">
                    <div style="width: 94.2%; height: 100%; background: linear-gradient(90deg, #8B5CF6, #00E5FF); border-radius: 3px;"></div>
                </div>
                <p style="color: #aaa; font-size: 0.8rem; margin-top: 15px; text-align: center;">Model Architecture: Random Forest Classifier</p>
                <p style="color: #aaa; font-size: 0.8rem; text-align: center; margin-top:-10px;">Status: <span style="color:#00FF88;">Online (model.pkl)</span></p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🔧 RUN SYSTEM DIAGNOSTICS", use_container_width=True):
            # Create a placeholder for diagnostics logs
            log_placeholder = st.empty()
            progress_bar = st.progress(0)
            
            # Simulate a real diagnostic sequence
            logs = [
                "Initializing diagnostic sequence...",
                "Verifying model.pkl checksum...",
                "Checksum valid. Loading weights...",
                "Testing Label Encoder mapping...",
                "Running sample telemetry through pipeline...",
                "AI Pipeline Latency: 14ms (Optimal).",
                "Diagnostics Complete."
            ]
            
            for i, log in enumerate(logs):
                log_placeholder.markdown(f"<p style='color: #00E5FF; font-family: monospace; font-size: 0.9rem;'>&gt; {log}</p>", unsafe_allow_html=True)
                progress_bar.progress(int(((i + 1) / len(logs)) * 100))
                time.sleep(0.4)
                
            st.success("All systems optimal. Dr. NOVA AI is ready for mission parameters.")
