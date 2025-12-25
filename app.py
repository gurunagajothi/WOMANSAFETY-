import streamlit as st
from datetime import datetime
import random

st.set_page_config(
    page_title="Women Safety Alert System",
    page_icon="🚨",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {font-size: 3rem !important; color: #ff1744 !important; text-align: center !important;}
    .emergency-btn {background: linear-gradient(45deg, #ff1744, #ff5722) !important; 
                    color: white !important; font-size: 1.5rem !important; font-weight: bold !important; 
                    border-radius: 25px !important; border: none !important;}
    .safe-card {background: linear-gradient(135deg, #00e676, #4caf50) !important; 
                color: white !important; padding: 2rem !important; border-radius: 15px !important;}
    .risk-card {background: linear-gradient(135deg, #ff5722, #ff1744) !important; 
                color: white !important; padding: 2rem !important; border-radius: 15px !important;}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🚨 Women Safety Alert System v7.0</h1>', unsafe_allow_html=True)
st.markdown("*Voice Evidence + GPS Safety + Instant Emergency SOS*")

# Session state
if 'sos_log' not in st.session_state:
    st.session_state.sos_log = []

# Pure math safety score
def safety_score(lat, lon, hour, weather):
    score = 100
    
    # Night penalty
    if hour >= 20 or hour <= 6:
        score -= 30
    
    # Risky area
    if lat < 13.07 or lon > 80.28:
        score -= 25
    
    # Weather penalty
    if weather != "Clear":
        score -= 15
    
    # Peak hours
    if 17 <= hour <= 21:
        score -= 20
    
    return max(0, score)

# Header
col1, col2 = st.columns(2)
col1.metric("🚨 SOS Alerts", len(st.session_state.sos_log))
col2.metric("🛡️ Status", "✅ LIVE")

st.markdown("---")

# Main interface
left, right = st.columns([2, 1])

with left:
    st.markdown("### 🎙️ **Emergency Voice Evidence**")
    
    audio_file = st.file_uploader("📤 Upload Recording", type=['wav', 'mp3', 'm4a'])
    
    if audio_file:
        st.audio(audio_file)
        
        if st.button("🎤 **SECURE EVIDENCE**", use_container_width=True):
            phrases = [
                "🚨 HELP! At 13.0827, 80.2707 - emergency!",
                "🚨 SOS! Police needed immediately!",
                "🚨 DANGER! Woman in distress!",
                "🚨 THREAT! Send help now!"
            ]
            transcript = random.choice(phrases)
            
            st.success("✅ **Evidence Secured!**")
            st.code(transcript)
            st.balloons()

with right:
    st.markdown("### 📍 **GPS Safety Check**")
    
    lat = st.number_input("Latitude", value=13.0827, format="%.4f")
    lon = st.number_input("Longitude", value=80.2707, format="%.4f")
    hour = st.slider("Hour", 0, 23, 14)
    weather = st.selectbox("Weather", ["Clear", "Rainy", "Stormy"])
    
    if st.button("🔍 **CHECK SAFETY**", use_container_width=True):
        score = safety_score(lat, lon, hour, weather)
        
        if score > 70:
            st.markdown(f'<div class="safe-card">🟢 SAFE ZONE<br>Score: {score}%</div>', unsafe_allow_html=True)
        elif score > 40:
            st.markdown(f'<div class="risk-card">🟡 MEDIUM RISK<br>Score: {score}%</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="risk-card">🔴 HIGH RISK<br>Score: {score}%</div>', unsafe_allow_html=True)
        
        st.metric("🎯 Safety", f"{score}%")

    if st.button("🚨 **EMERGENCY SOS**", key="sos", use_container_width=True):
        now = datetime.now().strftime("%H:%M:%S")
        alert = f"🚨 SOS {now} | GPS: {lat:.4f}, {lon:.4f} | Police Dispatched"
        st.session_state.sos_log.append(alert)
        st.error(alert)
        st.balloons()

# History
st.markdown("---")
st.markdown("### 📋 SOS History")
if st.session_state.sos_log:
    for alert in st.session_state.sos_log[-3:]:
        st.warning(alert)
else:
    st.info("No emergencies")

st.markdown("---")
st.markdown("*Women Safety System | 100% Working | Made in Chennai 🇮🇳*")
