import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1. యాప్ పేజీ మరియు స్టైలింగ్ సెటప్ (Good Looking UI)
st.set_page_config(page_title="Prashanthi AI Sugar Care", page_icon="💖", layout="centered")

# యాప్‌ను మరింత అందంగా మార్చడానికి కస్టమ్ CSS
st.markdown("""
    <style>
    .main { background-color: #f9fbfd; }
    .report-card { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 5px solid #2e7d32; margin-bottom: 15px; }
    .wish-box { background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 20px; border-radius: 15px; text-align: center; font-size: 20px; font-weight: bold; color: #0d47a1; margin-bottom: 20px; }
    .alarm-box { background-color: #ffebee; border-left: 5px solid #c62828; padding: 15px; border-radius: 8px; font-weight: bold; color: #c62828; }
    </style>
""", unsafe_allow_html=True)

# --- సెషన్ స్టేట్ మెయింటెనెన్స్ ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'water_liters' not in st.session_state:
    st.session_state.water_liters = 0.0
if 'tasks_done' not in st.session_state:
    st.session_state.tasks_done = {}

# 2. లాగిన్ స్క్రీన్
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align: center; color: #1565c0;'>🔐 AI Sugar Care Login</h2>", unsafe_allow_html=True)
    st.write("---")
    username = st.text_input("యూザー ఐడి (Username):")
    password = st.text_input("పాస్‌వర్డ్ (Password):", type="password")
    
    if st.button("🚀 లాగిన్ అవ్వండి"):
        if username == "prashanthi" and password == "sugarfree2026":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ తప్పుడు వివరాలు! మళ్లీ ప్రయత్నించండి.")
else:
    # ⏱️ ఆటో-రీఫ్రెష్ సెటప్ (ప్రతి 10 సెకన్లకు సమయాన్ని కరెక్ట్‌గా చెక్ చేస్తుంది)
    st_autorefresh(interval=10000, key="datarefresh")

    # సైడ్ బార్ లాగౌట్
    if st.sidebar.button("🔒 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # ప్రస్తుత సమయం
    now = datetime.datetime.now()
    current_time_str = now.strftime("%H:%M")
    current_hour = now.hour

    # 🌅 1. ఆటోమేటిక్ విషింగ్ మెసేజ్ లాజిక్ (Wishing Msg)
    st.markdown("<div class='wish-box'>", unsafe_allow_html=True)
    if 5 <= current_hour < 12:
        st.write("🌅 శుభోదయం ప్రశాంతి గారు! ఈరోజు మీ షుగర్ కంట్రోల్ చేయడానికి ఒక అద్భుతమైన రోజూవారీ ప్రణాళికతో ప్రారంభిద్దాం. కీప్ ఇట్ అప్! 💪")
    elif 12 <= current_hour < 16:
        st.write("☀️ శుభ మధ్యాహ్నం ప్రశాంతి గారు! భోజన నియమాలను పక్కాగా పాటించండి. అన్నం వద్దు, జొన్న రొట్టెలే ముఖ్యం! 🥗")
    elif 16 <= current_hour < 20:
        st.write("🌇 శుభ సాయంత్రం ప్రశాంతి గారు! కాస్త రిలాక్స్ అవ్వండి, కొన్ని నట్స్ తీసుకోండి మరియు వాకింగ్ సిద్ధమవ్వండి. 🍏")
    else:
        st.write("🌌 శుభ రాత్రి ప్రశాంతి గారు! రాత్రి టాబ్లెట్ వేసుకుని, ప్రశాంతంగా నిద్రపోవడానికి సిద్ధమవ్వండి. రేపు మరింత ఆరోగ్యంగా ఉందాం! 🛌")
    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader(f"⏰ ప్రస్తుత సమయం: {now.strftime('%I:%M:%S %p')}")
    st.write("---")

    # 📊 డైలీ టైమ్-టేబుల్ డేటాబేస్
    DAILY_ALARM_ROUTINE = [
        {"id": "t1", "time": "06:30", "title": "💧 వాటర్ అలారమ్ (ఉదయం)", "msg": "నిద్రలేచి ఒక పెద్ద గ్లాసు గోరువెచ్చని నీరు తాగండి. ఇది బాడీని క్లీన్ చేస్తుంది."},
        {"id": "t2", "time": "07:00", "title": "🏃‍♂️ నడక అలారమ్ (వాకింగ్)", "msg": "షుగర్ తగ్గడానికి 30 నిమిషాల పాటు వేగంగా నడవండి (Brisk Walking)."},
        {"id": "t3", "time": "08:30", "title": "🍳 ఉదయం బ్రేక్‌ఫాస్ట్ & మెడిసిన్", "msg": "మొలకెత్తిన గింజలు/రాగి జావ తీసుకోండి. తిన్న వెంటనే ఉదయం షుగర్ టాబ్లెట్ వేసుకోండి!"},
        {"id": "t4", "time": "11:00", "title": "💧 వాటర్ అలారమ్ (మధ్యాహ్నానికి ముందు)", "msg": "మరో గ్లాసు నీరు లేదా పలచటి మజ్జిగ తాగండి. షుగర్ పేరుకుపోకుండా కాపాడుతుంది."},
        {"id": "t5", "time": "13:00", "title": "🥗 మధ్యాహ్న భోజనం (Lunch Time)", "msg": "తెల్ల అన్నం వద్దు! 2 జొన్న రొట్టెలు, ఎక్కువ ఆకుకూరలు, వెజిటబుల్ సలాడ్ మాత్రమే తినండి."},
        {"id": "t6", "time": "13:30", "title": "🚶‍♀️ భోజనం తర్వాత నడక", "msg": "ఇంట్లోనే లేదా బయట కనీసం 10-15 నిమిషాల పాటు మెల్లగా నడవండి. దీనివల్ల షుగర్ పెరగదు."},
        {"id": "t7", "time": "16:00", "title": "💧 వాటర్ అలారమ్ (సాయంత్రం)", "msg": "బాడీ హైడ్రేషన్ కోసం ఒక గ్లాసు నీరు తాగే సమయం అయింది."},
        {"id": "t8", "time": "17:30", "title": "🍏 సాయంత్రం స్నాక్స్", "msg": "కొన్ని నానబెట్టిన బాదం పప్పులు తినండి. టీ/కాఫీలలో చక్కెర అస్సలు వద్దు."},
        {"id": "t9", "time": "20:00", "title": "🍲 రాత్రి భోజనం (Dinner Time)", "msg": "రాత్రి భోజనం చాలా తేలికగా ఉండాలి. వెజిటబుల్ సూప్ లేదా ఓట్స్ తీసుకోండి."},
        {"id": "t10", "time": "20:30", "title": "💊 రాత్రి మెడిసిన్ అలారమ్ (Night Tablet)", "msg": "భోజనం పూర్తయింది కదా! డాక్టర్ సూచించిన రాత్రి పూట షుగర్ టాబ్లెట్ వేసుకోండి."},
        {"id": "t11", "time": "22:00", "title": "🛌 ప్రశాంతమైన నిద్ర అలారమ్", "msg": "రాత్రి 10 అయింది. ఫోన్ పక్కన పెట్టేసి పడుకోండి. 7-8 గంటల నిద్ర చాలా ముఖ్యం!"}
    ]

    # ⏳ రాబోయే అలారమ్ కౌంట్‌డౌన్ (Proper Setting & Loading Time)
    next_alarm = None
    min_diff = float('inf')
    for alarm in DAILY_ALARM_ROUTINE:
        alarm_time = datetime.datetime.strptime(alarm["time"], "%H:%M").time()
        alarm_datetime = datetime.datetime.combine(now.date(), alarm_time)
        if alarm_datetime < now:
            alarm_datetime += datetime.timedelta(days=1)
        diff = (alarm_datetime - now).total_seconds()
        if diff < min_diff:
            min_diff = diff
            next_alarm = alarm

    if next_alarm:
        hours_left = int(min_diff // 3600)
        minutes_left = int((min_diff % 3600) // 60)
        st.info(f"👉 **రాబోయే టాస్క్:** {next_alarm['title']} ({next_alarm['time']})")
        st.metric(label="⏱️ అలారమ్‌కు మిగిలి ఉన్న సమయం (Countdown)", value=f"{hours_left} గంటల {minutes_left} నిమిషాలు")

    # 🚨 లైవ్ అలారమ్ ట్రిగ్గర్
    for alarm in DAILY_ALARM_ROUTINE:
        if current_time_str == alarm["time"]:
            st.markdown(f"<div class='alarm-box'>🚨 {alarm['title']}<br>{alarm['msg']}</div>", unsafe_allow_html=True)
            alarm_sound_url = "https://google.com"
            st.markdown(f'<iframe src="{alarm_sound_url}" allow="autoplay" style="display:none;"></iframe>', unsafe_allow_html=True)

    st.write("---")

    # 💧 వాటర్ ట్రాకర్
    st.header("📊 Daily Health Tracker")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        if st.button("🥤 1 గ్లాసు నీరు తాగాను (250ml)"):
            st.session_state.water_liters += 0.25
    with col_w2:
        if st.button("🔄 రీసెట్ వాటర్ కౌంటర్"):
            st.session_state.water_liters = 0.0

    st.metric(label="💧 మొత్తం తాగిన నీరు", value=f"{st.session_state.water_liters:.2f} L / 3.00 L")
    
    st.write("---")

    # 📋 2. రోజువారీ మానిటర్ నివేదిక (Day Monitor Report)
    st.header("📋 నేటి దినచర్య రిపోర్ట్ (Day Monitor Report)")
    st.write("ప్రశాంతి గారు ఈరోజు పూర్తి చేసిన పనుల వివరాలు:")
    
    total_tasks = len(DAILY_ALARM_ROUTINE)
    completed_tasks = sum(1 for t in DAILY_ALARM_ROUTINE if st.session_state.tasks_done.get(t["id"], False))
    
    st.progress(completed_tasks / total_tasks)
    st.write(f"📊 **టాస్క్ పూర్తయిన రేటు:** {completed_tasks} / {total_tasks} పనులు పూర్తయ్యాయి.")

    # 📅 దినచర్య పట్టిక చెక్‌బాక్స్‌లతో (Good Looking List)
    st.write("### 📝 టాస్క్ లిస్ట్ (సమయం కాగానే టిక్ చేయండి):")
    for alarm in DAILY_ALARM_ROUTINE:
        is_current = (current_time_str == alarm["time"])
        box_key = f"chk_{alarm['id']}"
        
        # సెషన్ స్టేట్ ఆధారంగా చెక్‌బాక్స్ సెట్ చేయడం
        st.session_state.tasks_done[alarm["id"]] = st.checkbox(
            f"⏰ {alarm['time']} - {alarm['title']}", 
            value=st.session_state.tasks_done.get(alarm["id"], False),
            key=box_key
        )
        if st.session_state.tasks_done[alarm["id"]]:
            st.markdown(f"<p style='color: green; margin-left: 30px;'>✅ Done: {alarm['msg']}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: #757575; margin-left: 30px;'>⏳ pending: {alarm['msg']}</p>", unsafe_allow_html=True)
