import streamlit as st

st.set_page_config(page_title="Strumenti di Reparto", page_icon="🏥", layout="wide")

st.title("🏥 Modulo 5: Strumenti di Reparto e Tirocinio")
st.markdown("Valori di riferimento degli esami ematochimici e calcolatori rapidi per le scale di valutazione infermieristica.")

st.warning("⚠️ **Nota clinica:** I range di laboratorio possono variare leggermente in base alla metodica del singolo ospedale. Fare sempre riferimento ai valori riportati sul referto della struttura.")

tab1, tab2, tab3, tab4 = st.tabs([
    "🩸 Valori di Laboratorio", 
    "🧠 Glasgow Coma Scale (GCS)", 
    "🛏️ Scala di Braden (Lesioni)", 
    "🚶 Scala di Conley (Cadute)"
])

# --- TAB 1: VALORI DI LABORATORIO ---
with tab1:
    st.header("Range di Riferimento Ematochimici Principali")
    
    categoria = st.selectbox("Seleziona il pannello di esami:", [
        "Emocromo Completo",
        "Elettroliti e Funzionalità Renale",
        "Coagulazione e Marcatori Cardiaci/Flogosi",
        "Funzionalità Epatica e Metabolismo",
        "Emogasanalisi Arteriosa (EGA)"
    ])
    
    if categoria == "Emocromo Completo":
        st.table({
            "Parametro": ["Globuli Rossi (RBC)", "Emoglobina (Hb)", "Ematocrito (Hct)", "Globuli Bianchi (WBC)", "Piastrine (PLT)", "MCV (Volume Corpuscolare Medio)"],
            "Valori Normali (Uomo / Donna)": [
                "U: 4,5 - 5,9 milioni/µL | D: 4,0 - 5,2 milioni/µL",
                "U: 13,5 - 17,5 g/dL | D: 12,0 - 16,0 g/dL",
                "U: 41 - 53 % | D: 36 - 46 %",
                "4.000 - 10.000 /µL (4,0 - 10,0 × 10³/µL)",
                "150.000 - 400.000 /µL (150 - 400 × 10³/µL)",
                "80 - 100 fL"
            ]
        })
    elif categoria == "Elettroliti e Funzionalità Renale":
        st.table({
            "Parametro": ["Sodio (Na+)", "Potassio (K+)", "Cloro (Cl-)", "Calcio Totale (Ca2+)", "Magnesio (Mg2+)", "Creatininemia", "Azotemia (Urea)"],
            "Valori Normali": [
                "135 - 145 mEq/L",
                "3,5 - 5,0 mEq/L",
                "98 - 107 mEq/L",
                "8,5 - 10,5 mg/dL",
                "1,7 - 2,2 mg/dL",
                "0,6 - 1,2 mg/dL",
                "15 - 50 mg/dL"
            ]
        })
    elif categoria == "Coagulazione e Marcatori Cardiaci/Flogosi":
        st.table({
            "Parametro": ["INR (Tempo di Protrombina)", "aPTT (Tempo Tromboplastina Parziale)", "Fibrinogeno", "D-Dimero", "PCR (Proteina C Reattiva)", "Procalcitonina (PCT)", "Troponina I / T (hs)"],
            "Valori Normali": [
                "0,8 - 1,2 (In terapia con Warfarin: 2,0 - 3,0)",
                "25 - 35 secondi",
                "200 - 400 mg/dL",
                "< 500 ng/mL (o < 0,50 µg/mL)",
                "< 0,5 mg/dL (o < 5 mg/L)",
                "< 0,05 ng/mL",
                "Negativa (secondo cut-off laboratorio)"
            ]
        })
    elif categoria == "Funzionalità Epatica e Metabolismo":
        st.table({
            "Parametro": ["AST (GOT)", "ALT (GPT)", "Bilirubina Totale", "Bilirubina Diretta", "Amilasi", "Lipasi", "Glicemia a digiuno", "Albumina"],
            "Valori Normali": [
                "10 - 40 U/L",
                "7 - 56 U/L",
                "0,2 - 1,2 mg/dL",
                "< 0,3 mg/dL",
                "30 - 110 U/L",
                "10 - 140 U/L",
                "70 - 100 mg/dL",
                "3,5 - 5,0 g/dL"
            ]
        })
    elif categoria == "Emogasanalisi Arteriosa (EGA)":
        st.table({
            "Parametro": ["pH Arterioso", "PaO2", "PaCO2", "Bicarbonati (HCO3-)", "Saturazione O2 (SaO2)", "Lattati"],
            "Valori Normali": [
                "7,35 - 7,45",
                "80 - 100 mmHg",
                "35 - 45 mmHg",
                "22 - 26 mEq/L",
                "95 - 100 %",
                "< 2,0 mmol/L"
            ]
        })

# --- TAB 2: GLASGOW COMA SCALE (GCS) ---
with tab2:
    st.header("Glasgow Coma Scale (GCS) — Valutazione Neurologica")
    
    occhi = st.selectbox("1. Apertura degli Occhi (E):", [
        "4 - Spontanea",
        "3 - Allo stimolo verbale",
        "2 - Allo stimolo doloroso",
        "1 - Nessuna apertura"
    ])
    verbale = st.selectbox("2. Risposta Verbale (V):", [
        "5 - Orientata e appropriata",
        "4 - Confusa",
        "3 - Parole inappropriate",
        "2 - Suoni incomprensibili",
        "1 - Nessuna risposta"
    ])
    motoria = st.selectbox("3. Risposta Motoria (M):", [
        "6 - Obbedisce ai comandi",
        "5 - Localizza il dolore",
        "4 - Retrae al dolore",
        "3 - Flessione anomala al dolore (decorticazione)",
        "2 - Estensione al dolore (decerebrazione)",
        "1 - Nessuna risposta"
    ])
    
    p_occhi = int(occhi[0])
    p_verbale = int(verbale[0])
    p_motoria = int(motoria[0])
    tot_gcs = p_occhi + p_verbale + p_motoria
    
    st.metric("Punteggio Totale GCS (Range: 3 - 15)", f"{tot_gcs} / 15", delta=f"E{p_occhi} V{p_verbale} M{p_motoria}")
    
    if tot_gcs >= 13:
        st.success("🟢 **Trauma cranico / compromissione LIEVE** (13 - 15)")
    elif 9 <= tot_gcs <= 12:
        st.warning("🟡 **Compromissione MODERATA** (9 - 12)")
    else:
        st.error("🔴 **COMA / Compromissione GRAVE** (≤ 8 — Valutare protezione vie aeree)")

# --- TAB 3: SCALA DI BRADEN ---
with tab3:
    st.header("Scala di Braden — Rischio Lesioni da Pressione")
    
    col1, col2 = st.columns(2)
    with col1:
        b1 = st.selectbox("Percezione Sensoriale:", ["1 - Completamente limitata", "2 - Molto limitata", "3 - Leggermente limitata", "4 - Non limitata"], index=3)
        b2 = st.selectbox("Umidità:", ["1 - Costantemente umida", "2 - Molto umida", "3 - Occasionalmente umida", "4 - Raramente umida"], index=3)
        b3 = st.selectbox("Attività:", ["1 - Allettato", "2 - In poltrona", "3 - Cammina occasionalmente", "4 - Cammina frequentemente"], index=3)
    with col2:
        b4 = st.selectbox("Mobilità:", ["1 - Completamente immobile", "2 - Molto limitata", "3 - Parzialmente limitata", "4 - Limitazioni assenti"], index=3)
        b5 = st.selectbox("Nutrizione:", ["1 - Molto povera", "2 - Probabilmente inadeguata", "3 - Adeguata", "4 - Eccellente"], index=2)
        b6 = st.selectbox("Frizione e Scivolamento:", ["1 - Problema presente", "2 - Problema potenziale", "3 - Senza problemi apparenti"], index=2)
        
    tot_braden = int(b1[0]) + int(b2[0]) + int(b3[0]) + int(b4[0]) + int(b5[0]) + int(b6[0])
    st.metric("Punteggio Braden (Range: 6 - 23)", f"{tot_braden} / 23")
    
    if tot_braden <= 9:
        st.error("🔴 **Rischio ALTISSIMO** (≤ 9)")
    elif 10 <= tot_braden <= 12:
        st.error("🟠 **Rischio ALTO** (10 - 12)")
    elif 13 <= tot_braden <= 14:
        st.warning("🟡 **Rischio MODERATO** (13 - 14)")
    elif 15 <= tot_braden <= 18:
        st.info("🔵 **Rischio LIEVE** (15 - 18)")
    else:
        st.success("🟢 **Nessun rischio significativo** (> 18)")

# --- TAB 4: SCALA DI CONLEY ---
with tab4:
    st.header("Scala di Conley — Valutazione Rischio Cadute")
    
    st.subheader("Domande al paziente / caregiver")
    c1 = st.checkbox("È caduto nel corso degli ultimi 3 mesi? (+2 punti)")
    c2 = st.checkbox("Ha mai avuto vertigini o capogiri negli ultimi 3 mesi? (+1 punto)")
    c3 = st.checkbox("Le è mai capitato di perdere urina o feci mentre si recava in bagno? (+1 punto)")
    
    st.subheader("Osservazione infermieristica")
    c4 = st.checkbox("Compromissione della marcia, passo strisciante, ampia base d'appoggio o instabilità? (+1 punto)")
    c5 = st.checkbox("Agitato (eccessiva attività motoria, irrequietezza)? (+2 punti)")
    c6 = st.checkbox("Deterioramento del giudizio / mancanza del senso del pericolo? (+3 punti)")
    
    tot_conley = (2 if c1 else 0) + (1 if c2 else 0) + (1 if c3 else 0) + (1 if c4 else 0) + (2 if c5 else 0) + (3 if c6 else 0)
    st.metric("Punteggio Conley (Range: 0 - 10)", f"{tot_conley} / 10")
    
    if tot_conley >= 2:
        st.error("🔴 **PAZIENTE A RISCHIO CADUTA (Punteggio ≥ 2):** Attivare protocollo di prevenzione (spondine valutate, campanello a portata di mano, calzature chiuse, letto basso).")
    else:
        st.success("🟢 **Rischio minimo** (0 - 1 punti)")
