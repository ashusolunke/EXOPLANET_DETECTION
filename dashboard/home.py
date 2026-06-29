import streamlit as st

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
        st.markdown(
            """
            <div class="mission-card animate-fade-in" style="animation-delay: 0.5s; height: 300px;">
                <h3 style="color: #00E5FF;">Global Telemetry</h3>
                <p style="color: #aaa;">Data streams from Kepler & TESS synchronized.</p>
                <div style="width: 100%; height: 200px; display: flex; align-items: center; justify-content: center; border: 1px dashed rgba(120,120,255,0.3); border-radius: 10px;">
                    <span style="color: #8B5CF6; font-style: italic;">Live Telemetry Visualization (Plotly)</span>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with col_b:
        st.markdown(
            """
            <div class="mission-card animate-fade-in" style="animation-delay: 0.6s; height: 300px;">
                <h3 style="color: #00FF88;">AI Scientist Core</h3>
                <div style="margin-top: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                        <span style="color: #fff;">Average Confidence</span>
                        <span style="color: #00E5FF; font-weight: bold;">94.2%</span>
                    </div>
                    <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px;">
                        <div style="width: 94.2%; height: 100%; background: linear-gradient(90deg, #8B5CF6, #00E5FF); border-radius: 3px;"></div>
                    </div>
                </div>
                <div style="margin-top: 30px; text-align: center;">
                    <p style="color: #aaa; font-size: 0.9rem;">Model loaded: model.pkl</p>
                    <button style="background: linear-gradient(45deg, #12192D, #050816); border: 1px solid #8B5CF6; border-radius: 8px; color: #00E5FF; padding: 10px 20px; cursor: pointer; width: 100%; margin-top: 20px;">RUN DIAGNOSTICS</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
