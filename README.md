# 🌌 COSMOS X AI - Mission Control Dashboard

**AI Powered Exoplanet Mission Control System**

Built for the **Bharatiya Antariksh Hackathon 2026 (ISRO)**, COSMOS X AI is a next-generation dashboard that visualizes exoplanetary data and provides AI-driven insights. Designed with the aesthetics of an advanced Space Agency Mission Control, this platform seamlessly combines beautiful user interfaces with scientific rigor.

---

## 🚀 Key Features

* **Interactive 3D Galaxy Explorer**: A full WebGL-powered 3D visualization of exoplanetary systems using Three.js. Users can rotate the galaxy, zoom into star systems, and view interactive glassmorphism data panels.
* **AI Scientist Core (Dr. NOVA)**: An automated AI analysis system that parses transit patterns, predicts habitability, and outputs human-readable recommendations for secondary observations (e.g., JWST).
* **Transit Visualization**: Live-animated light curve graphs utilizing Plotly to show planetary transits and stellar noise.
* **Habitable Zone Simulator**: An interactive physics slider that calculates climate status based on orbital distance.
* **Advanced Analytics**: Real-time distributions of candidate statuses, planet sizes, and model confidence scores.
* **Scientific Report Generator**: Export capabilities for comprehensive PDF reports of targeted systems.

---

## 🛠️ Technology Stack

* **Frontend**: Streamlit, HTML, CSS (Vanilla), JavaScript
* **3D Rendering**: Three.js (WebGL)
* **Visualizations**: Plotly
* **Backend Data/ML**: Python, Pandas, Scikit-Learn, NumPy
* **Design Philosophy**: Glassmorphism, Dark Space Theme, Neon Colors, Smooth Animations

---

## 📂 Project Structure

```text
Exoplanet_Detection/
│
├── .streamlit/               # Streamlit theme configuration
│   └── config.toml
│
├── components/               # Reusable UI components
│   └── sidebar.py            # Custom navigation sidebar
│
├── dashboard/                # Application views/pages
│   ├── home.py               # Main telemetry dashboard
│   ├── galaxy_explorer.py    # 3D Three.js integration
│   ├── mission_status.py     # AI Scientist & Analytics
│   ├── settings.py           # Report Generation
│   └── targets.py            # Search & Transit Visualization
│
├── notebooks/                # Jupyter notebooks for EDA and Model Training
│   └── data.ipynb            
│
├── styles/                   # Custom CSS injection
│   ├── style.css             # Glassmorphism, animations, custom scrollbars
│   └── theme.py              # Loader for custom CSS
│
├── threejs/                  # WebGL assets
│   └── galaxy.html           # Standalone Three.js galaxy rendering
│
├── utils/                    # Helper scripts
│   └── prediction.py         # ML model inference pipeline
│
├── model/                    # Serialized machine learning models
│   ├── model.pkl
│   └── label_encoder.pkl
│
├── app.py                    # Main Streamlit Application Entry Point
├── requirements.txt          # Python dependencies
└── README.md                 # Project Documentation
```

---

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/Exoplanet_Detection.git
   cd Exoplanet_Detection
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Mission Control Dashboard:**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`.

---

## 🎨 UI/UX Highlights
- **No static images**: All visualizations (including the galaxy) are fully interactive mathematical renderings.
- **Glassmorphism UI**: Uses `backdrop-filter: blur()` alongside semi-transparent gradients to achieve a NASA/ISRO futuristic feel.
- **Micro-interactions**: Hover effects, glow animations, and CSS keyframes dynamically guide the user's attention to critical telemetry data.

---

*“To look up at the stars and not down at our feet.”*
