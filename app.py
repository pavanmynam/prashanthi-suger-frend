<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ప్రశాంతి AI షుగర్ కేర్ యాప్</title>
    <style>
        :root {
            --primary: #1e3a8a;
            --secondary: #0284c7;
            --success: #16a34a;
            --danger: #dc2626;
            --light: #f8fafc;
            --dark: #0f172a;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #e2e8f0;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .app-container {
            width: 100%;
            max-width: 450px;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            overflow: hidden;
            padding: 20px;
            box-sizing: border-box;
        }

        .screen { display: none; }
        .screen.active { display: block; }

        /* Login Screen Styles */
        .login-screen { text-align: center; padding: 40px 20px; }
        .logo { font-size: 50px; margin-bottom: 10px; }
        h2 { color: var(--primary); margin-bottom: 25px; font-size: 24px; }
        .input-group { margin-bottom: 20px; text-align: left; }
        label { display: block; margin-bottom: 5px; color: var(--dark); font-weight: 600; }
        input { width: 100%; padding: 12px; border: 2px solid #cbd5e1; border-radius: 10px; box-sizing: border-box; font-size: 16px; }
        button { width: 100%; padding: 14px; background: var(--primary); color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: bold; cursor: pointer; transition: 0.3s; }
        button:hover { background: var(--secondary); }

        /* Dashboard Styles */
        .wishes-box { background: linear-gradient(135deg, #1e3a8a, #0284c7); color: white; padding: 15px; border-radius: 15px; margin-bottom: 15px; }
        .joke-box { background: #fef3c7; border-left: 5px solid #d97706; padding: 15px; border-radius: 10px; margin-bottom: 15px; color: #92400e; font-weight: 500; }
        .music-box { background: #f0fdf4; border: 1px solid #bbf7d0; padding: 15px; border-radius: 10px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; }
        
        /* Schedule Styles */
        .card { background: var(--light); border: 1px solid #e2e8f0; border-radius: 12px; padding: 15px; margin-bottom: 15px; }
        .card-header { display: flex; justify-content: space-between; font-weight: bold; color: var(--primary); margin-bottom: 10px; }
        .btn-group { display: flex; gap: 10px; margin: 10px 0; }
        .btn-done { background: var(--success); color: white; padding: 8px; border: none; border-radius: 6px; flex: 1; cursor: pointer; }
        .btn-skip { background: var(--danger); color: white; padding: 8px; border: none; border-radius: 6px; flex: 1; cursor: pointer; }
        .comment-input { width: 100%; padding: 8px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 14px; box-sizing: border-box; }

        /* Scanner Styles */
        .scanner-box { background: #edf2f7; padding: 15px; border-radius: 12px; text-align: center; margin-bottom: 15px; border: 2px dashed #cbd5e1; }
        .verdict { margin-top: 10px; padding: 10px; border-radius: 6px; font-weight: bold; display: none; }

        .footer-nav { display: flex; justify-content: space-between; margin-top: 20px; border-top: 1px solid #e2e8f0; padding-top: 15px; }
        .btn-report { background: #475569; color: white; padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer; width: auto; }
    </style>
</head>
<body>

<div class="app-container">

    <!-- 1. లాగిన్ స్క్రీన్ -->
    <div id="loginScreen" class="screen active">
        <div class="login-screen">
            <div class="logo">🩺</div>
            <h2>ప్రశాంతి గారి AI షుగర్ కేర్</h2>
            <div class="input-group">
                <label>మొబైల్ నంబర్ / యూజర్ ఐడీ:</label>
                <input type="text" id="username" value="Prashanthi" placeholder="Enter User ID">
            </div>
            <div class="input-group">
                <label>4-అంకెల పిన్ (PIN):</label>
                <input type="password" id="pin" value="1234" placeholder="••••">
            </div>
            <button onclick="login()">యాప్‌లోకి లాగిన్ అవ్వండి</button>
        </div>
    </div>

    <!-- 2. మెయిన్ డాష్‌బోర్డ్ స్క్రీన్ -->
    <div id="dashboardScreen" class="screen">
        <!-- సమయాన్ని బట్టి విషెస్ -->
        <div class="wishes-box" id="wishesBox">శుభోదయం ప్రశాంతి గారు! ☀️</div>

        <!-- రోజువారీ తెలుగు జోక్ -->
        <div class="joke-box">
            <strong>😂 నేటి నవ్వుల తోట:</strong><br>
            <span id="dailyJoke">డాక్టర్: మీకు షుగర్ ఉంది, స్వీట్స్ తినకూడదు!<br>పేషెంట్: మరి మా ఆవిడ నన్ను రోజూ 'స్వీటీ' అని పిలుస్తుంది, ఆమెను వదలేయాలా డాక్టర్? 😉</span>
        </div>

        <!-- రిలాక్సేషన్ మ్యూజిక్ ప్లేయర్ -->
        <div class="music-box">
            <span>🎵 స్ట్రెస్ రిలీఫ్ మ్యూజిక్ (వేణుగానం)</span>
            <button id="musicBtn" onclick="toggleMusic()" style="width: auto; padding: 6px 12px; background: var(--secondary);">Play 🎧</button>
            <audio id="bgMusic" loop src="https://soundhelix.com"></audio> 
            <!-- నోట్: పైన ఉన్నది శాంపిల్ మ్యూజిక్ లింక్, మీకు నచ్చిన ఆడియో లింక్ మార్చుకోవచ్చు -->
        </div>

        <!-- AI ఫుడ్ స్కానర్ ఆప్షన్ -->
        <div class="scanner-box">
            <strong>📸 AI ఫుడ్ స్కానర్ (తినాలా? వద్దా?)</strong>
            <p style="font-size: 13px; color:#4a5568;">మీరు తినబోయే ఆహారం ఫోటో అప్‌లోడ్ చేయండి</p>
            <input type="file" id="foodImage" accept="image/*" onchange="scanFood()" style="font-size: 12px;">
            <div id="scanResult" class="verdict"></div>
        </div>

        <!-- పూర్తి షెడ్యూల్ టేబుల్ ఫార్మాట్ -->
        <h3>📅 నేటి దినచర్య షెడ్యూల్</h3>
        
        <div class="card">
            <div class="card-header"><span>⏰ 08:30 AM</span> <span>🍳 బ్రేక్‌ఫాస్ట్ & టాబ్లెట్</span></div>
            <small style="color: #64748b;">💊 సూచన: మెట్‌ఫార్మిన్ 500mg (టిఫిన్ తర్వాత)</small>
            <div class="btn-group">
                <button class="btn-done" onclick="setStatus(this, 'తిన్నాను & వేసుకున్నాను ✅')">తిన్నాను ✅</button>
                <button class="btn-skip" onclick="setStatus(this, 'స్కిప్ చేసాను ❌')">స్కిప్ ❌</button>
            </div>
            <input type="text" class="comment-input" placeholder="✍️ ఈ టాస్క్ గురించి కామెంట్ రాయండి...">
        </div>

        <div class="card">
            <div class="card-header"><span>⏰ 11:00 AM</span> <span>🥛 మజ్జిగ / వాటర్ అలారమ్</span></div>
            <small style="color: #64748b;">💧 సూచన: ఒక గ్లాసు పలచటి మజ్జిగ తాగండి.</small>
            <div class="btn-group">
                <button class="btn-done" onclick="setStatus(this, 'తాగాను ✅')">తాగాను ✅</button>
                <button class="btn-skip" onclick="setStatus(this, 'స్కిప్ చేసాను ❌')">స్కిప్ ❌</button>
            </div>
            <input type="text" class="comment-input" placeholder="✍️ ఈ టాస్క్ గురించి కామెంట్ రాయండి...">
        </div>

        <div class="card">
            <div class="card-header"><span>⏰ 01:00 PM</span> <span>🍛 మధ్యాహ్నం భోజనం (Lunch)</span></div>
            <small style="color: #64748b;">🌾 సూచన: జొన్న రొట్టె లేదా బ్రౌన్ రైస్ తీసుకోండి.</small>
            <div class="btn-group">
                <button class="btn-done" onclick="setStatus(this, 'తిన్నాను ✅')">తిన్నాను ✅</button>
                <button class="btn-skip" onclick="setStatus(this, 'స్కిప్ చేసాను ❌')">స్కిప్ ❌</button>
            </div>
            <input type="text" class="comment-input" placeholder="✍️ ఈ టాస్క్ గురించి కామెంట్ రాయండి...">
        </div>

        <div class="footer-nav">
            <button class="btn-report" onclick="showReport()">📊 రోజువారీ రిపోర్ట్ చూడండి</button>
        </div>
    </div>

    <!-- 3. రోజువారీ నివేదిక స్క్రీన్ (Report View) -->
    <div id="reportScreen" class="screen">
        <h3>📊 ఈరోజు ఆరోజు నివేదిక (Daily Report)</h3>
        <div id="reportContent" style="background: #f8fafc; padding: 15px; border-radius: 10px; font-size: 14px; line-height: 1.6; border: 1px solid #cbd5e1;">
            <!-- రిపోర్ట్ డేటా ఇక్కడ జనరేట్ అవుతుంది -->
        </div>
        <button onclick="goBack()" style="margin-top: 15px; background: #475569;">⬅️ వెనక్కి వెళ్ళండి</button>
    </div>

</div>

<script>
    // 1. లాగిన్ ఫంక్షన్
    function login() {
        const user = document.getElementById('username').value;
        const pin = document.getElementById('pin').value;
        
        if(user === "Prashanthi" && pin === "1234") {
            document.getElementById('loginScreen').classList.remove('active');
            document.getElementById('dashboardScreen').classList.add('active');
            setDynamicWishes();
        } else {
            alert("సరైన యూజర్ ఐడీ మరియు పిన్ నమోదు చేయండి!");
        }
    }

    // 2. సమయాన్ని బట్టి విష్ చేసే ఫంక్షన్
    function setDynamicWishes() {
        const hrs = new Date().getHours();
        const wishesBox = document.getElementById('wishesBox');
        if (hrs < 12) {
            wishesBox.innerHTML = "💡 శుభోదయం ప్రశాంతి గారు! ☀️ ఈరోజు మీ ఆరోగ్యం చాలా బాగుండాలని కోరుకుంటున్నాను.";
        } else if (hrs >= 12 && hrs < 16) {
            wishesBox.innerHTML = "💡 శుభ మధ్యాహ్నం ప్రశాంతి గారు! 🌤️ మధ్యాహ్న భోజనం సమయానికి ముగించండి.";
        } else {
            document.getElementById('wishesBox').innerHTML = "💡 నమస్కారం ప్రశాంతి గారు! ✨ మీ ఆరోగ్యాన్ని జాగ్రత్తగా చూసుకోండి.";
        }
    }

    // 3. రిలాక్సేషన్ మ్యూజిక్ కంట్రోల్
    let isPlaying = false;
    function toggleMusic() {
        const music = document.getElementById('bgMusic');
