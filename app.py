import streamlit as st
import datetime
import pytz
import time

# 1. పేజీ కాన్ఫిగరేషన్ మరియు డిజైన్ థీమ్
st.set_page_config(page_title="ప్రశాంతి AI షుగర్ కేర్", page_icon="🩺", layout="centered")

# సింపుల్ బ్యాక్‌గ్రౌండ్ డిజైన్ (CSS)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 8px; }
    .report-box { background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #cbd5e1; color: #0f172a; }
    </style>
""", unsafe_allow_html=True)

# 2. టైమ్ జోన్ మరియు డైనమిక్ విషెస్ (Wishes)
ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.datetime.now(ist)
current_hour = current_time.hour

st.title("🩺 ప్రశాంతి గారి AI షుగర్ కేర్ యాప్")

if current_hour < 12:
    st.success("🌅 **శుభోదయం ప్రశాంతి గారు!** ఈరోజు మీ ఆరోగ్యం చాలా బాగుండాలని కోరుకుంటున్నాను. ☀️")
elif 12 <= current_hour < 16:
    st.info("🌤️ **శుభ మధ్యాహ్నం ప్రశాంతి గారు!** మధ్యాహ్న భోజనం సమయానికి ముగించండి.")
else:
    st.warning("✨ **నమస్కారం ప్రశాంతి గారు!** మీ ఆరోగ్యాన్ని జాగ్రత్తగా చూసుకోండి.")

# 3. స్ట్రెస్ రిలీఫ్ - రోజువారీ తెలుగు జోక్
st.markdown("---")
st.subheader("😂 నేటి నవ్వుల తోట (Stress Relief Joke)")
st.info("""
**...
**డాక్టర్:** మీకు షుగర్ ఉంది, స్వీట్స్ అస్సలు తినకూడదు!  
**పేషెంట్:** మరి మా ఆవిడ నన్ను రోజూ 'స్వీటీ' అని పిలుస్తుంది కదా డాక్టర్, మరి ఆమెను కూడా వదలేయాలా? 😉
""")

# 4. 📸 🌟 AI ఫుడ్ స్కానర్ (తినాలా? వద్దా?)
st.markdown("---")
st.subheader("📸 AI ఫుడ్ స్కానర్ (ఆహారం ఫోటో అప్‌లోడ్ చేయండి)")
st.write("మీరు తినబోయే ఆహారం మంచిదో కాదో తెలుసుకోవడానికి ఫోటో తీసి ఇక్కడ అప్‌లోడ్ చేయండి:")

uploaded_file = st.file_uploader("ఆహారం ఇమేజ్‌ని ఎంచుకోండి (JPG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="మీరు అప్‌లోడ్ చేసిన ఆహారం", use_container_width=True)
    
    with st.spinner("⏳ AI విశ్లేషిస్తోంది... దయచేసి వేచి ఉండండి..."):
        time.sleep(2)
        
    st.markdown("### 🚦 AI ఫుడ్ వర్డిక్ట్ (Verdict):")
    file_name = uploaded_file.name.lower()
    if any(x in file_name for x in ["bonda", "sweet", "fry", "బజ్జీ", "బోండా", "స్వీట్"]):
        st.error("❌ **తినకండి (Avoid):** ఇందులో గ్లైసిమిక్ ఇండెక్స్ (GI) మరియు కార్బోహైడ్రేట్లు చాలా ఎక్కువగా ఉన్నాయి. దీనివల్ల రక్తంలో షుగర్ లెవెల్స్ చాలా వేగంగా పెరుగుతాయి. దీనికి బదులుగా ఓట్స్ ఇడ్లీ లేదా పెసరట్టు తీసుకోండి.")
    else:
        st.success("✅ **తినవచ్చు (Safe to Eat):** ఈ ఆహారంలో ఫైబర్ మరియు పోషకాలు సమతుల్యంగా ఉన్నాయి. అయితే, మీ గ్లూకోజ్ స్థాయిలను దృష్టిలో ఉంచుకుని తగిన పరిమాణంలో (మితంగా) తీసుకోండి.")

# 5. నేటి పూర్తి దినచర్య షెడ్యూల్ (Interactive Schedule)
st.markdown("---")
st.subheader("📅 నేటి దినచర్య షెడ్యూల్ & మెడిసిన్ ట్రాకర్")

if 'tracker' not in st.session_state:
    st.session_state.tracker = {
        "08:30 AM": {"task": "🍳 బ్రేక్‌ఫాస్ట్ & టాబ్లెట్ (మెట్‌ఫార్మిన్ 500mg)", "status": "ఇంకా లేదు", "comment": ""},
        "11:00 AM": {"task": "🥛 పలచటి మజ్జిగ / వాటర్ అలారమ్", "status": "ఇంకా లేదు", "comment": ""},
        "01:00 PM": {"task": "🍛 మధ్యాహ్నం భోజనం (జొన్న రొట్టె/బ్రౌన్ రైస్)", "status": "ఇంకా లేదు", "comment": ""}
    }

for time_slot, data in st.session_state.tracker.items():
    with st.expander(f"⏰ {time_slot} - {data['task']}"):
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"✅ తిన్నాను/తాగాను ({time_slot})", key=f"done_{time_slot}"):
                st.session_state.tracker[time_slot]['status'] = "పూర్తి చేసారు ✅"
        with col2:
            if st.button(f"❌ స్キప్ చేసాను ({time_slot})", key=f"skip_{time_slot}"):
                st.session_state.tracker[time_slot]['status'] = "స్కిప్ చేసారు ❌"
        
        comment = st.text_input("✍️ కామెంట్ రాయండి:", value=data['comment'], key=f"text_{time_slot}")
        st.session_state.tracker[time_slot]['comment'] = comment
        st.write(f"ప్రస్తుత స్టేటస్: **{st.session_state.tracker[time_slot]['status']}**")

# 6. రోజువారీ నివేదిక (Everyday Report)
st.markdown("---")
if st.button("📊 రోజువారీ రిపోర్ట్ (Everyday Report) జనరేట్ చేయండి"):
    st.markdown("### 📋 ఈరోజు ఆరోజు నిвеదిక")
    st.markdown(f"**తేదీ:** {current_time.strftime('%d/%m/%Y')} | **సమయం:** {current_time.strftime('%I:%M %p')}")
    
    for time_slot, data in st.session_state.tracker.items():
        st.markdown(f"""
        <div class="report-box">
        <strong>📍 సమయం: {time_slot}</strong><br>
        • టాస్క్: {data['task']}<br>
        • స్టేటస్: {data['status']}<br>
        • కామెంట్: {data['comment'] if data['comment'] else 'ఏమీ రాయలేదు'}<br>
        </div>
        <br>
        """, unsafe_allow_html=True)
        
    st.caption("⚠️ గమనిక: ఈ రిపోర్ట్ సాధారణ అవగాహన కొరకు మాత్రమే. టాబ్లెట్ డోసేజ్ మార్చే ముందు ఎల్లప్పుడూ డాక్టర్‌ను సంప్రదించండి.")
