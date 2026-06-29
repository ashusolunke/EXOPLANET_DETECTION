import streamlit as st
import plotly.express as px
import pandas as pd
import time

def render_mission_status():
    st.markdown("<h1 class='page-title animate-fade-in'>Mission Status</h1>", unsafe_allow_html=True)
    
    col_ai, col_analytics = st.columns([1, 2])
    
    with col_ai:
        st.markdown("<h3 style='color: #8B5CF6;'>🤖 AI Scientist</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="mission-card" style="height: 500px; overflow-y: auto;">
                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                    <div style="width: 40px; height: 40px; border-radius: 50%; background: #12192D; border: 2px solid #8B5CF6; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">🤖</div>
                    <div style="margin-left: 15px;">
                        <span style="color: #00E5FF; font-weight: bold;">Dr. NOVA</span><br>
                        <span style="color: #aaa; font-size: 0.8rem;">Senior Exoplanetary Analyst</span>
                    </div>
                </div>
                
                <div style="background: rgba(139, 92, 246, 0.1); border-left: 3px solid #8B5CF6; padding: 15px; margin-bottom: 15px; border-radius: 0 10px 10px 0;">
                    <p style="color: #fff; margin: 0; font-family: monospace;">> Analyzing target KOI-456.04...</p>
                </div>
                
                <div style="background: rgba(0, 229, 255, 0.1); border-left: 3px solid #00E5FF; padding: 15px; margin-bottom: 15px; border-radius: 0 10px 10px 0;">
                    <p style="color: #fff; margin: 0; font-family: monospace;">> Transit pattern is <strong style="color: #00FF88;">stable</strong>. Low stellar noise detected.</p>
                </div>
                
                <div style="background: rgba(0, 255, 136, 0.1); border-left: 3px solid #00FF88; padding: 15px; margin-bottom: 15px; border-radius: 0 10px 10px 0;">
                    <p style="color: #fff; margin: 0; font-family: monospace;">> Radius indicates <strong style="color: #00FF88;">Earth-like</strong> characteristics. Possible atmosphere presence.</p>
                </div>
                
                <div style="border: 1px solid #FF9800; padding: 15px; border-radius: 10px;">
                    <h4 style="color: #FF9800; margin-top: 0;">RECOMMENDATION:</h4>
                    <p style="color: #fff; margin-bottom: 0;"><strong>HIGH PRIORITY.</strong> Target for secondary observation with JWST.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_analytics:
        st.markdown("<h3 style='color: #00E5FF;'>Analytics & Distributions</h3>", unsafe_allow_html=True)
        
        # Mock Data for charts
        dist_data = pd.DataFrame({
            "Status": ["Confirmed", "Candidate", "False Positive"],
            "Count": [4102, 1139, 2800]
        })
        
        # Pie Chart
        fig1 = px.pie(dist_data, values='Count', names='Status', hole=0.4, 
                      color_discrete_sequence=['#00FF88', '#00E5FF', '#FF9800'])
        fig1.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#fff'),
            margin=dict(l=0, r=0, t=30, b=0),
            height=200
        )
        st.plotly_chart(fig1, width="stretch")
        
        # Bar Chart
        rad_data = pd.DataFrame({
            "Size Class": ["Earth-size", "Super-Earth", "Neptune-like", "Gas Giant"],
            "Count": [180, 520, 1400, 1900]
        })
        fig2 = px.bar(rad_data, x='Size Class', y='Count', 
                      color='Size Class', color_discrete_sequence=['#8B5CF6', '#00E5FF', '#00FF88', '#FF9800'])
        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(18,25,45,0.5)',
            font=dict(color='#fff'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            margin=dict(l=0, r=0, t=30, b=0),
            height=250
        )
        st.plotly_chart(fig2, width="stretch")
