import pickle
import numpy as np
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="CardioGuard | Heart Disease Predictor",
    page_icon="🩺",
    layout="wide",
)

# 2. Enhanced Custom Styling (CSS)
custom_css = """
<style>
    /* Main App Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }
    
    /* Headers & Text colors */
    h1, h2, h3, p, label {
        color: #f1f5f9 !important;
    }
    
    /* Make cards/containers look professional */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 5px;
    }
    
    /* Main Action Button Style */
    .stButton>button {
        background: linear-gradient(90deg, #ec4899 0%, #8b5cf6 100%);
        color: white !important;
        border: none;
        padding: 12px 30px;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
        background: linear-gradient(90deg, #f43f5e 0%, #a855f7 100%);
    }
    
    /* Custom Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #8b5cf6;
        margin-bottom: 10px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# 3. Model Loading (With caching for optimization)
@st.cache_resource
def load_model():
    # Using your absolute path; ensure it is correct on your local system
    model_path = (
        "model.pkl"
    )
    try:
        with open(model_path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        # Fallback dummy for demonstration if file path misses
        st.error(f"Could not find model at: {model_path}")
        return None


model = load_model()

# 4. Header Section
st.title("🩺 CardioGuard AI")
st.subheader("Advanced Cardiovascular Risk Assessment Dashboard")
st.write(
    "Utilize machine learning to analyze patient clinical metrics and evaluate heart disease risk factors."
)
st.markdown("---")

# 5. Dashboard Layout & Inputs
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 👤 Patient Clinical Vitals")

    age = st.number_input(
        "Age (Years)", min_value=1, max_value=120, value=45, step=1
    )

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=50,
        max_value=250,
        value=120,
        help="Resting blood pressure on admission to the hospital.",
    )

    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        min_value=100,
        max_value=600,
        value=200,
        help="Serum cholesterol level in mg/dl.",
    )

    thalach = st.number_input(
        "Maximum Heart Rate Achieved",
        min_value=60,
        max_value=220,
        value=150,
        help="Maximum heart rate achieved during stress testing.",
    )

with col2:
    st.markdown("### 🧪 Diagnostic & ECG Features")

    cp = st.selectbox(
        "Chest Pain Type",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "0: Typical Angina",
            1: "1: Atypical Angina",
            2: "2: Non-anginal Pain",
            3: "3: Asymptomatic",
        }[x],
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No",
        help="Did exercise cause chest pain/angina?",
    )

    oldpeak = st.number_input(
        "ST Depression (Oldpeak)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
        help="ST depression induced by exercise relative to rest.",
    )

    slope = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0: Upsloping",
            1: "1: Flat",
            2: "2: Downsloping",
        }[x],
    )

    ca = st.selectbox(
        "Major Vessels Colored by Fluoroscopy",
        options=[0, 1, 2, 3, 4],
        help="Number of major vessels (0-4) colored by fluoroscopy.",
    )

st.markdown("---")

# 6. Live Vitals Summary Metrics
st.markdown("### 📊 Quick Patient Summary")
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.markdown(
        f'<div class="metric-card"><strong>Age:</strong> {age} yrs</div>',
        unsafe_allow_html=True,
    )
with m_col2:
    st.markdown(
        f'<div class="metric-card"><strong>BP / Chol:</strong> {trestbps} / {chol} mg/dl</div>',
        unsafe_allow_html=True,
    )
with m_col3:
    st.markdown(
        f'<div class="metric-card"><strong>Max HR:</strong> {thalach} bpm</div>',
        unsafe_allow_html=True,
    )

st.write("")  # Spacing

# 7. Prediction Execution
if st.button("RUN RISK ASSESSMENT"):
    if model is not None:
        input_data = np.array(
            [[age, cp, trestbps, chol, thalach, exang, oldpeak, slope, ca]]
        )
        prediction = model.predict(input_data)

        # Presentation of results
        st.markdown("### 🎯 Assessment Result")
        if prediction[0] == 1:
            st.error(
                "### ⚠️ High Risk Detected\nThe model indicates a high probability of heart disease. Immediate clinical consultation is advised."
            )
        else:
            st.success(
                "### ✅ Low Risk Detected\nThe model indicates a low probability of heart disease based on the provided clinical data."
            )
    else:
        st.error(
            "Prediction could not be run because the model file was not loaded."
        )

# Footer
st.markdown("---")
st.caption(
    "🔒 **Disclaimer:** This app is a decision support tool for informational purposes only and does not substitute professional medical advice."
)
