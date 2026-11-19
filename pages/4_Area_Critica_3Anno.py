import streamlit as st

st.set_page_config(page_title="Area Critica 3° Anno", page_icon="🚑", layout="wide")

st.title("🚑 Modulo 4: Area Critica, Terapia Intensiva e Urgenza (3° Anno)")
st.markdown("Calcoli avanzati per pompe siringa, farmaci vasoattivi, bilancio idrico ed emogasanalisi clinica.")

st.warning("⚠️ **Uso didattico:** Strumento per la preparazione agli esami di Area Critica e tirocinio avanzato. Seguire sempre i protocolli clinici aziendali.")

tab1, tab2, tab3, tab4 = st.tabs([
    "⏱️ Pompa Siringa (mcg/kg/min)", 
    "⚖️ Bilancio Idrico 24h", 
    "🫁 EGA Avanzato & Gap Anionico", 
    "📝 Casi Clinici Urgenza"
])

# --- TAB 1: POMPA SIRINGA (MCG/KG/MIN E UI/ORA) ---
with tab1:
    st.header("Infusioni Continue in Pompa Siringa (Terapia Intensiva)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Farmaci Vasoattivi (mcg/kg/min -> ml/h)")
        st.caption("Es. Dopamina, Dobutamina, Noradrenalina diluiti in siringa da 50 ml.")
        peso_icu = st.number_input("Peso del paziente (kg):", min_value=1.0, max_value=250.0, value=70.0, step=1.0, key="peso_icu")
        farmaco_mg = st.number_input("Quantità di farmaco in siringa (mg):", min_value=0.1, value=200.0, step=10.0)
        vol_siringa = st.number_input("Volume totale della siringa (ml):", min_value=1.0, value=50.0, step=5.0)
        dose_mcg_kg_min = st.number_input("Dosaggio prescritto (mcg/kg/min):", min_value=0.01, value=5.0, step=0.5)
        
        if st.button("Calcola Velocità Pompa (ml/h)", key="btn_vaso"):
            farmaco_mcg = farmaco_mg * 1000.0
            conc_mcg_ml = farmaco_mcg / vol_siringa
            mcg_ora = dose_mcg_kg_min * peso_icu * 60.0
            ml_ora_vaso = mcg_ora / conc_mcg_ml
            
            st.success(f"⚙️ **Impostare Pompa Siringa a: {ml_ora_vaso:.2f} ml/h**")
            st.info(f"""
            **Passaggi del calcolo:**
            1. **Concentrazione siringa:** ${farmaco_mg}\\text{{ mg}} = {farmaco_mcg:.0f}\\text{{ mcg}}$ in ${vol_siringa}\\text{{ ml}} \\rightarrow \\mathbf{{{conc_mcg_ml:.1f}\\text{{ mcg/ml}}}}$
            2. **Fabbisogno orario paziente:** ${dose_mcg_kg_min}\\text{{ mcg}} \\times {peso_icu}\\text{{ kg}} \\times 60\\text{{ min}} = \\mathbf{{{mcg_ora:.1f}\\text{{ mcg/h}}}}$
            3. **Velocità in ml/h:** $\\frac{{{mcg_ora:.1f}}}{{{conc_mcg_ml:.1f}}} = \\mathbf{{{ml_ora_vaso:.2f}\\text{{ ml/h}}}}$
            """)

    with col2:
        st.subheader("2. Infusione Continua (UI/ora -> ml/h)")
        st.caption("Es. Insulina rapida o Eparina sodica in infusione continua.")
        ui_tot = st.number_input("Unità totali nella siringa/sacca (UI):", min_value=1.0, value=50.0, step=10.0)
        vol_ui = st.number_input("Volume totale soluzione (ml):", min_value=1.0, value=50.0, step=10.0, key="vol_ui")
        ui_ora_prescr = st.number_input("Prescrizione medica (UI/ora):", min_value=0.1, value=4.0, step=0.5)
        
        if st.button("Calcola ml/h (UI)", key="btn_ui"):
            conc_ui_ml = ui_tot / vol_ui
            ml_h_ui = ui_ora_prescr / conc_ui_ml
            st.success(f"⚙️ **Impostare Pompa a: {ml_h_ui:.2f} ml/h**")
            st.info(f"**Concentrazione:** {conc_ui_ml:.2f} UI/ml $\\rightarrow$ $\\frac{{{ui_ora_prescr}}}{{{conc_ui_ml:.2f}}} = {ml_h_ui:.2f}\\text{{ ml/h}}$")

# --- TAB 2: BILANCIO IDRICO ---
with tab2:
    st.header("Calcolo del Bilancio Idrico nelle 24 ore")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("➕ Entrate (ml)")
        infusioni = st.number_input("Terapia infusionale EV (ml):", min_value=0, value=1500, step=100)
        os = st.number_input("Assunzione per os / SNG (ml):", min_value=0, value=800, step=50)
        acqua_endogena = st.number_input("Acqua endogena metabolica (standard ~300 ml):", min_value=0, value=300, step=50)
        
    with col2:
        st.subheader("➖ Uscite (ml)")
        diuresi = st.number_input("Diuresi 24h (ml):", min_value=0, value=1600, step=100)
        drenaggi = st.number_input("Drenaggi / Ristagno gastrico / Alvo (ml):", min_value=0, value=200, step=50)
        peso_bil = st.number_input("Peso paziente per Perspiratio (kg):", min_value=1.0, value=70.0, step=1.0)
        febbre = st.checkbox("Paziente febbrile (> 38°C) o tachipnoico (+500 ml)")
        
    if st.button("Calcola Bilancio Idrico", key="btn_bil"):
        perspiratio = (0.5 * peso_bil * 24) + (500 if febbre else 0)
        tot_entrate = infusioni + os + acqua_endogena
        tot_uscite = diuresi + drenaggi + perspiratio
        bilancio = tot_entrate - tot_uscite
        
        st.metric("Bilancio Idrico Finale", f"{bilancio:+.0f} ml", delta="Positivo (ritenzione)" if bilancio > 0 else "Negativo (perdita)")
        st.info(f"**Dettaglio:** Entrate Totali ({tot_entrate:.0f} ml) - Uscite Totali ({tot_uscite:.0f} ml, di cui {perspiratio:.0f} ml di *perspiratio insensibilis*).")

# --- TAB 3: EGA AVANZATO E GAP ANIONICO ---
with tab3:
    st.header("Calcolo del Gap Anionico (Acidosi Metabolica)")
    st.markdown("Utile per distinguere le acidosi metaboliche con accumulo di acidi (es. chetoacidosi diabetica, acidosi lattica) da quelle da perdita di bicarbonati.")
    st.latex(r"\text{Gap Anionico (AG)} = [Na^+] - ([Cl^-] + [HCO_3^-])")
    
    c1, c2, c3 = st.columns(3)
    na = c1.number_input("Sodio [Na+] (mEq/L):", min_value=100.0, max_value=180.0, value=140.0, step=1.0)
    cl = c2.number_input("Cloro [Cl-] (mEq/L):", min_value=70.0, max_value=140.0, value=104.0, step=1.0)
    hco3_ag = c3.number_input("Bicarbonati [HCO3-] (mEq/L):", min_value=5.0, max_value=45.0, value=24.0, step=1.0)
    
    if st.button("Calcola Gap Anionico", key="btn_ag"):
        ag = na - (cl + hco3_ag)
        st.metric("Gap Anionico (Valore normale: 8 - 16 mEq/L)", f"{ag:.1f} mEq/L")
        if ag > 16:
            st.error("🔴 **Gap Anionico Aumentato:** Sospetto accumulo di acidi organici (Chetoacidosi, Acidosi Lattica, Insufficienza Renale, Intossicazioni).")
        elif 8 <= ag <= 16:
            st.success("🟢 **Gap Anionico nella norma:** Se presente acidosi, valutare perdita di bicarbonati (es. diarrea profusa) o acidosi ipercloremica.")
        else:
            st.warning("🟡 **Gap Anionico Ridotto:** Valutare ipoalbuminemia severa.")

# --- TAB 4: CASI CLINICI 3° ANNO ---
with tab4:
    st.header("Simulazione Esame di Area Critica")
    
    q1 = st.radio(
        "1. Paziente di 80 kg in Terapia Intensiva. Prescrizione: Dopamina a 5 mcg/kg/min. Hai preparato una siringa con 200 mg di Dopamina in 50 ml di fisiologica. A quanti ml/h imposti la pompa?",
        ["3 ml/h", "6 ml/h", "12 ml/h", "24 ml/h"],
        index=None
    )
    if q1:
        if q1 == "6 ml/h":
            st.success("✅ Esatto! Concentrazione = 200.000 mcg / 50 ml = 4.000 mcg/ml. Fabbisogno = 5 × 80 × 60 = 24.000 mcg/h. Velocità = 24.000 / 4.000 = 6 ml/h.")
        else:
            st.error("❌ Riprova! Converti 200 mg in 200.000 mcg, dividi per 50 ml (4.000 mcg/ml) e poi calcola il fabbisogno orario (5 × 80 × 60).")

    q2 = st.radio(
        "2. Un paziente in chetoacidosi diabetica presenta: Na+ = 138 mEq/L, Cl- = 100 mEq/L, HCO3- = 12 mEq/L. Quanto vale il Gap Anionico?",
        ["12 mEq/L (Normale)", "26 mEq/L (Aumentato)", "38 mEq/L (Aumentato)", "6 mEq/L (Ridotto)"],
        index=None
    )
    if q2:
        if q2 == "26 mEq/L (Aumentato)":
            st.success("✅ Perfetto! AG = 138 - (100 + 12) = 26 mEq/L, tipico dell'accumulo di corpi chetonici.")
        else:
            st.error("❌ Attenzione alla formula: Na+ meno (Cl- + HCO3-) = 138 - 112 = 26 mEq/L.")
