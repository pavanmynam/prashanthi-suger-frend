import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# యాప్ పేజీ సెటప్
st.set_page_config(page_title="Prashanthi AI Sugar Care", page_icon="📱", layout="centered")

# 🔄 ప్రతి 30 సెకన్లకు యాప్ ఆటోమేటిక్‌గా టైమ్ చెక్ చేసుకోవడానికి రీఫ్రెష్ సెటప్
st_autorefresh(interval=30000, key="datarefresh")

st.title("📱 ప్రశాంతి గారి AI షుగర్ కేర్ & ఆటోమేటిక్ అలారమ్ యాప్")
st.write("---")

# ⏱️ ప్రస్తుత సమయం మరియు తేదీ
now = datetime.datetime.now()
current_time = now.strftime("%H:%M")
st.subheader(f"⏰ ప్రస్తుత సమయం: {now.strftime('%I:%M %p')}")

# 📊 9.9% HbA1c కి సరిపోయే పక్కా డైలీ టైమ్-టేబుల్ (రాత్రి టాబ్లెట్‌తో సహా)
DAILY_ALARM_ROUTINE = [
    {"time": "06:30", "title": "💧 వాటర్ అలారమ్ (ఉదయం)", "msg": "ప్రశాంతి గారు, వెంటనే నిద్రలేచి ఒక పెద్ద గ్లాసు గోరువెచ్చని నీరు తాగండి. ఇది బాడీని క్లీన్ చేస్తుంది."},
    {"time": "07:00", "title": "🏃‍♂️ నడక అలారమ్ (వాకింగ్)", "msg": "సమయం అయింది! మీ షుగర్ తగ్గడానికి 30 నిమిషాల పాటు వేగంగా నడవండి (Brisk Walking)."},
    {"time": "08:30", "title": "🍳 ఉదయం బ్రేక్‌ఫాస్ట్ & మెడిసిన్", "msg": "టిఫిన్ తినే సమయం. మొలకెత్తిన గింజలు లేదా రాగి జావ తీసుకోండి. తిన్న వెంటనే డాక్టర్ ఇచ్చిన ఉదయం షుగర్ టాబ్లెట్ వేసుకోండి!"},
    {"time": "11:00", "title": "💧 వాటర్ అలారమ్ (మధ్యాహ్నానికి ముందు)", "msg": "మరో గ్లాసు నీరు లేదా పలచటి మజ్జిగ తాగండి. రక్తంలో షుగర్ పేరుకుపోకుండా ఇది కాపాడుతుంది."},
    {"time": "13:00", "title": "🥗 మధ్యాహ్న భోజనం (Lunch Time)", "msg": "భోజన సమయం! తెల్ల అన్నం (వైట్ライズ) అస్సలు ముట్టవద్దు. 2 జొన్న రొట్టెలు, ఎక్కువ ఆకుకూరలు, వెజిటబుల్ సలాడ్ మాత్రమే తినండి."},
    {"time": "13:30", "title": "🚶‍♀️ భోజనం తర్వాత నడక", "msg": "తిన్న వెంటనే కూర్చోవద్దు. ఇంట్లోనే లేదా బయట కనీసం 10-15 నిమిషాల పాటు మెల్లగా నడవండి. దీనివల్ల షుగర్ లెవెల్స్ షూట్ అప్ అవ్వవు."},
    {"time": "16:00", "title": "💧 వాటర్ అలారమ్ (సాయంత్రం)", "msg": "బాడీ హైడ్రేషన్ కోసం ఒక గ్లాసు నీరు తాగే సమయం అయింది."},
    {"time": "17:30", "title": "🍏 సాయంత్రం స్నాక్స్", "msg": "ఆకలి వేస్తే కొన్ని నానబెట్టిన బాదం పప్పులు లేదా వాల్‌నట్స్ తినండి. టీ/కాఫీలలో చక్కెర అస్సలు వద్దు."},
    {"time": "20:00", "title": "🍲 రాత్రి భోజనం (Dinner Time)", "msg": "రాత్రి భోజనం చాలా తేలికగా ఉండాలి. వెజిటబుల్ సూప్ లేదా ఓట్స్ తీసుకోండి. ఆలస్యం చేయకుండా ఇప్పుడే తినేయండి."},
    {"time": "20:30", "title": "💊 రాత్రి మెడిసిన్ అలారమ్ (Night Tablet)", "msg": "రాత్రి భోజనం పూర్తయింది కదా! డాక్టర్ సూచించిన రాత్రి పూట షుగర్ టాబ్లెట్ వేసుకోవడం అస్సలు మర్చిపోకండి."},
    {"time": "22:00", "title": "🛌 ప్రశాంతమైన నిద్ర అలారమ్", "msg": "రాత్రి 10 అయింది. ఫోన్ పక్కన పెట్టేసి పడుకోండి. 7-8 గంటల నిద్ర లేకపోతే స్ట్రెస్ హార్మోన్లు పెరిగి షుగర్ అస్సలు తగ్గదు!"}
]

# 🚨 ఆటోమేటిక్ అలారమ్ ట్రిగ్గర్ లాజిక్
alarm_triggered = False
active_alarm = None

for alarm in DAILY_ALARM_ROUTINE:
    if current_time == alarm["time"]:
        alarm_triggered = True
        active_alarm = alarm
        break

if alarm_triggered and active_alarm:
    st.error(f"🚨🚨 {active_alarm['title']} 🚨🚨")
    st.markdown(f"### **{active_alarm['msg']}**")
    
    # ఆటో-ప్లే అలారమ్ సౌండ్
    alarm_sound_url = "https://google.com"
    st.markdown(
        f'<iframe src="{alarm_sound_url}" allow="autoplay" style="display:none;" id="iframeAudio"></iframe>',
        unsafe_allow_html=True
    )
    st.balloons()
else:
    st.success("🤖 AI మోడ్ ఆన్‌లో ఉంది: ప్రశాంతి గారి దినచర్యను బ్యాక్‌గ్రౌండ్‌లో మానిటర్ చేస్తున్నాను. సమయం కాగానే అలారమ్ మోగుతుంది.")

# 📋 టైమ్-టేబుల్ వ్యూ
st.write("### 📅 ప్రశాంతి గారి నేటి దినచర్య పట్టిక:")
for alarm in DAILY_ALARM_ROUTINE:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.info(f"⏰ {alarm['time']}")
    with col2:
        with st.expander(alarm["title"]):
            st.write(alarm["msg"])
