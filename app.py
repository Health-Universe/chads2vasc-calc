import streamlit as st
from util import (
    calculate_chads2vasc_score,
    ischemic_stroke_risk_dict,
    stroke_tia_se_risk_dict,
)

st.title("CHA₂DS₂-VASc Score Calculator")
st.markdown("---")

# Get input from user
col1, col2 = st.columns(2)

with col1:
    st.write(f"#### Demographics")
    age = st.slider("Age", min_value=0, max_value=120, value=50, step=1)
    is_male = st.radio("Sex", options=["Male", "Female"]) == "Male"

with col2:
    st.write(f"#### History")
    chf_history = st.checkbox("Congestive Heart Failure")
    htn_history = st.checkbox("Hypertension")
    stroke_tia_vte_history = st.checkbox("Stroke/TIA/Thromboembolism")
    cvd_history = st.checkbox("Vascular Disease")
    dm_history = st.checkbox("Diabetes")

st.markdown("---")

# Calculate CHA₂DS₂-VASc Score and risks
chads2vasc_score = calculate_chads2vasc_score(
    age,
    is_male,
    chf_history,
    htn_history,
    stroke_tia_vte_history,
    cvd_history,
    dm_history,
)

# Display results
st.write(f"**CHA₂DS₂-VASc Score:** {chads2vasc_score}")
st.write(f"**Risk of ischemic stroke:** {ischemic_stroke_risk_dict[chads2vasc_score]}%")
st.write(
    f"**Risk of stroke/TIA/systemic embolism:** {stroke_tia_se_risk_dict[chads2vasc_score]}%"
)
