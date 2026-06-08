import pickle
import numpy as np
import streamlit as st

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="CardioGuard | Heart Disease Predictor",
    page_icon="🩺",
    layout="wide",
)

# =========================
# Custom CSS
# =========================
custom_css = """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }

    h1, h2, h3, p, label {
        color: #f1f5f9 !important;
    }

    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 5px;
    }

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

# =========================
# Load Model
# =========================
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

try:
    model = load_model()
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")
    model = None

# =========================
# Header
# =========================
st.title("🩺 CardioGuard AI")
st.subheader("Advanced Cardiovascular Risk Assessment Dashboard")

st.write(
    "Utilize machine learning to analyze patient clinical metrics and evaluate heart disease risk factors."
)

st.markdown("---")

# =========================
# Input Section
# =========================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 👤 Patient Clinical Vitals")

    age = st.number_input(
        "Age (Years)",
        min_value=1,
        max_value=120,
        value=45,
    )

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=50,
        max_value=250,
        value=120,
    )

    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        min_value=100,
        max_value=600,
        value=200,
    )

    thalach = st.number_input(
        "Maximum Heart Rate Achieved",
        min_value=60,
        max_value=220,
        value=150,
    )

with col2:
    st.markdown("### 🧪 Diagnostic & ECG Features")

    cp = st.selectbox(
        "Chest Pain Type",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "Typical Angina",
            1: "Atypical Angina",
            2: "Non-anginal Pain",
            3: "Asymptomatic",
        }[x],
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No",
    )

    oldpeak = st.number_input(
        "ST Depression (Oldpeak)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
    )

    slope = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "Upsloping",
            1: "Flat",
            2: "Downsloping",
        }[x],
    )

    ca = st.selectbox(
        "Major Vessels Colored by Fluoroscopy",
        options=[0, 1, 2, 3, 4],
    )

st.markdown("---")

# =========================
# Summary Cards
# =========================
st.markdown("### 📊 Quick Patient Summary")

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(
        f"""
        <div class="metric-card">
            <strong>Age:</strong> {age} yrs
        </div>
        """,
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        f"""
        <div class="metric-card">
            <strong>BP / Chol:</strong> {trestbps} / {chol}
        </div>
        """,
        unsafe_allow_html=True,
    )

with m3:
    st.markdown(
        f"""
        <div class="metric-card">
            <strong>Max HR:</strong> {thalach} bpm
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# =========================
# Prediction
# =========================
if st.button("🚀 RUN RISK ASSESSMENT"):

    if model is None:
        st.error("Model is not available.")
    else:

        input_data = np.array([
            [
                age,
                cp,
                trestbps,
                chol,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
            ]
        ])

        try:
            prediction = model.predict(input_data)

            st.markdown("### 🎯 Assessment Result")

            if prediction[0] == 1:
                st.error(
                    """
                    ### ⚠️ High Risk Detected

                    The model indicates a high probability of heart disease.

                    Please consult a qualified healthcare professional for further evaluation.
                    """
                )
            else:
                st.success(
                    """
                    ### ✅ Low Risk Detected

                    The model indicates a low probability of heart disease based on the provided information.
                    """
                )

            # Optional probability output
            if hasattr(model, "predict_proba"):
                probability = model.predict_proba(input_data)[0][1]

                st.progress(float(probability))

                st.info(
                    f"Estimated Heart Disease Risk: **{probability * 100:.2f}%**"
                )

        except Exception as e:
            st.error(f"Prediction failed: {e}")

# =========================
# Footer
# =========================
st.markdown("---")

st.caption(
    "🔒 Disclaimer: This application is for educational and informational purposes only and does not replace professional medical advice, diagnosis, or treatment."
)
