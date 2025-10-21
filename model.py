# 🚢 Multimodal Marine Monitoring System - Dark Theme Dashboard
# Developed by Loveleen Kaur | IIT Mandi

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------------#
# PAGE CONFIG
# ---------------------------#
st.set_page_config(
    page_title="Multimodal Marine AI",
    layout="wide"
)

# ---------------------------#
# CUSTOM DARK THEME CSS
# ---------------------------#
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
}
h1, h2, h3, h4 {
    color: #00FFFF;
    text-shadow: 0px 0px 10px #00FFFF;
}
.sidebar .sidebar-content {
    background-color: #111111;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
div.stButton > button {
    background-color: #00FFFF;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #00FFFF;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------#
# HEADER
# ---------------------------#
st.title("Multimodal Marine Monitoring System")
st.markdown("### **Smart AI-Powered Maritime Dashboard** ")
st.markdown("This dark-themed app simulates multimodal sensor fusion for marine navigation, safety, and predictive maintenance.")

# ---------------------------#
# SIDEBAR
# ---------------------------#
st.sidebar.header("⚙️ Simulation Settings")
num_points = st.sidebar.slider("Select Number of Data Points", 20, 200, 60)
st.sidebar.markdown("Adjust to control the amount of simulated sensor readings.")
st.sidebar.markdown("---")
st.sidebar.write("Developed by: **Loveleen Kaur** 💙")

# ---------------------------#
# SIMULATED SENSOR DATA
# ---------------------------#
np.random.seed(42)
data = pd.DataFrame({
    "Visual_Sensor": np.random.randint(30, 100, num_points),
    "Thermal_Sensor": np.random.randint(10, 90, num_points),
    "Radar_Distance": np.random.randint(100, 500, num_points),
    "Acoustic_Level": np.random.randint(40, 120, num_points),
    "Time": pd.date_range("2025-01-01", periods=num_points, freq="min")
})

# ---------------------------#
# VISUALS
# ---------------------------#
st.subheader("📊 Real-Time Sensor Overview")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.line(data, x="Time", y="Radar_Distance",
                   title="📡 Radar Distance Over Time",
                   color_discrete_sequence=["#00FFFF"])
    fig1.update_layout(
        paper_bgcolor="#000000",
        plot_bgcolor="#000000",
        font_color="white"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(data, x="Visual_Sensor", y="Thermal_Sensor",
                      color="Acoustic_Level", color_continuous_scale="Viridis",
                      title="Visual vs Thermal Sensor Fusion")
    fig2.update_layout(
        paper_bgcolor="#000000",
        plot_bgcolor="#000000",
        font_color="white"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------#
# RISK PREDICTION LOGIC
# ---------------------------#
st.markdown("---")
st.subheader(" AI-Based Risk Assessment")

avg_v = np.mean(data["Visual_Sensor"])
avg_t = np.mean(data["Thermal_Sensor"])
avg_r = np.mean(data["Radar_Distance"])
avg_a = np.mean(data["Acoustic_Level"])

risk_score = (100 - avg_v) * 0.3 + (100 - avg_t) * 0.3 + (avg_a / 2) * 0.4

if risk_score > 65:
    status = "HIGH RISK – Obstacle or Fault Detected!"
    color = "#FF3C3C"
elif risk_score > 40:
    status = "MODERATE RISK – Monitor Conditions Carefully"
    color = "#FFA500"
else:
    status = "SAFE CONDITIONS – Normal Operation"
    color = "#00FF7F"

st.markdown(f"<h2 style='color:{color}; text-align:center;'>{status}</h2>", unsafe_allow_html=True)

# ---------------------------#
# SENSOR SUMMARY
# ---------------------------#
st.markdown("---")
st.subheader("📈 Sensor Summary Insights")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Visual", f"{avg_v:.1f}")
col2.metric("Avg Thermal", f"{avg_t:.1f}")
col3.metric("Avg Radar", f"{avg_r:.1f} m")
col4.metric("Avg Acoustic", f"{avg_a:.1f} dB")

# ---------------------------#
# FOOTER
# ---------------------------#
st.markdown("---")
st.markdown("<h4 style='text-align:center; color:#00FFFF;'>© 2025 Multimodal Marine AI | Made by Loveleen Kaur 💙</h4>", unsafe_allow_html=True)

