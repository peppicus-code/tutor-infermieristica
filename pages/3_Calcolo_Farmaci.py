import streamlit as st

st.set_page_config(page_title="Calcolo Farmaci", page_icon="💉", layout="wide")

st.title("💉 Modulo 3: Calcolo Farmacologico e Infusione (2°/3° Anno)")
st.markdown("Simulatori clinici per la preparazione sicura della terapia e la gestione delle pompe infusionali.")

st.warning("⚠️ **Uso didattico:** Questo strumento serve esclusivamente per esercitarsi e verificare i calcoli di studio. In ambito clinico fare sempre riferimento ai protocolli di reparto.")

tab1, tab2, tab3, tab4 = st.tabs([
    "💊 Dosaggi e Proporzioni", 
    "💧 Velocità Infusione (gtt/min e ml/h)", 
    "🧪 Diluizioni e Unità (UI)", 
    "📝 Simulazione Esame"
])

with tab1:
    st.header("Calcolo del Volume da Aspirare (Proporzione Standard)")
    st.latex(r"\text{Dose Disponibile (mg)} : \text{Volume Fiala (ml)} = \text{Dose Prescritta (mg)} : X\text{ (ml)}")
    
    col1, col2 = st.columns(2)
    with col1:
        unita = st.selectbox("Unità di misura del farmaco:", ["mg (milligrammi)", "mcg / gamma (microgrammi)", "g (grammi)", "UI (Unità Internazionali)"])
        dose_disp = st.number_input("Dose contenuta nella fiala/flacone:", min_value=0.01, value=500.0, step=10.0)
        vol_fiala = st.number_input("Volume totale della fiala/solvente (ml):", min_value=0.1, value=5.0, step=0.5)
        dose_prescr = st.number_input("Dose prescritta dal medico:", min_value=0.01, value=125.0, step=5.0)
        
    with col2:
        st.subheader("Risultato e Procedimento")
        if st.button("Calcola Volume da Somministrare", key="btn_dose"):
            vol_da_aspirare = (dose_prescr * vol_fiala) / dose_disp
            st.success(f"💉 **Aspirare: {vol_da_aspirare:.2f} ml**")
            st.info(f"""
            **Impostazione della proporzione:**
            * ${dose_disp} : {vol_fiala}\\text{{ ml}} = {dose_prescr} : X$
            * $X = \\frac{{{dose_prescr} \\times {vol_fiala}}}{{{dose_disp}}} = {vol_da_aspirare:.2f}\\text{{ ml}}$
            """)

with tab2:
    st.header("Calcolo Velocità di Infusione (Fleboclisi)")
    
    col1, col2 = st.columns(2)
    with col1:
        vol_inf = st.number_input("Volume totale da infondere (ml):", min_value=1.0, value=500.0, step=50.0)
        tipo_tempo = st.radio("Il tempo è espresso in:", ["Ore", "Minuti"], horizontal=True)
        tempo_val = st.number_input(f"Durata dell'infusione ({tipo_tempo}):", min_value=1.0, value=4.0 if tipo_tempo == "Ore" else 60.0, step=1.0)
        deflusso = st.selectbox(
            "Fattore goccia (Deflussore):", (20, 15, 60), 
            format_func=lambda x: f"{x} gtt/ml ({'Standard / Macrogocce' if x==20 else 'Sangue / Emocomponenti' if x==15 else 'Microgocce / Pediatrico'})"
        )
        
    with col2:
        st.subheader("Velocità Impostata")
        if st.button("Calcola Velocità", key="btn_inf"):
            minuti_totali = tempo_val * 60.0 if tipo_tempo == "Ore" else tempo_val
            ore_totali = tempo_val if tipo_tempo == "Ore" else tempo_val / 60.0
            
            ml_ora = vol_inf / ore_totali
            gtt_min = (vol_inf * deflusso) / minuti_totali
            
            st.metric("Pompa Infusionale (ml/ora)", f"{ml_ora:.1f} ml/h")
            st.metric("Conteggio Manuale (gocce/minuto)", f"{round(gtt_min)} gtt/min", delta=f"Valore esatto: {gtt_min:.2f}")
            
            st.info(f"""
            **Formule utilizzate:**
            * **ml/ora:** $\\frac{{\\text{{Volume}}}}{{\\text{{Ore}}}} = \\frac{{{vol_inf}}}{{{ore_totali:.2f}}} = {ml_ora:.1f}\\text{{ ml/h}}$
            * **gtt/min:** $\\frac{{\\text{{Volume}} \\times \\text{{Fattore Goccia}}}}{{\\text{{Minuti Totali}}}} = \\frac{{{vol_inf} \\times {deflusso}}}{{{minuti_totali:.0f}}} = {gtt_min:.2f} \\approx {round(gtt_min)}\\text{{ gtt/min}}$
            """)

with tab3:
    st.header("Conversioni Rapide e Calcolo Dose/Peso")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Convertitore Unità Cliniche")
        val_conv = st.number_input("Valore da convertire:", min_value=0.0, value=0.5, step=0.1, format="%.3f")
        tipo_conv = st.selectbox("Tipo di conversione:", [
            "Grammi (g) -> Milligrammi (mg)",
            "Milligrammi (mg) -> Microgrammi (mcg / gamma)",
            "Microgrammi (mcg) -> Milligrammi (mg)",
            "Milligrammi (mg) -> Grammi (g)"
        ])
        if st.button("Converti", key="btn_conv"):
            if "g) -> Milligrammi" in tipo_conv or "mg) -> Microgrammi" in tipo_conv:
                res = val_conv * 1000
                st.success(f"**Risultato:** {res:,.2f}")
            else:
                res = val_conv / 1000
                st.success(f"**Risultato:** {res:.6f}")

    with col2:
        st.subheader("Calcolo Dose su Peso Corporeo (mg/kg)")
        peso = st.number_input("Peso del paziente (kg):", min_value=1.0, max_value=250.0, value=70.0, step=1.0)
        dose_kg = st.number_input("Dosaggio prescritto (mg/kg):", min_value=0.01, value=15.0, step=0.5)
        if st.button("Calcola Dose Totale Paziente", key="btn_peso"):
            tot_paz = peso * dose_kg
            st.success(f"**Dose totale da somministrare:** {tot_paz:.2f} mg")

with tab4:
    st.header("Casi Clinici di Verifica")
    
    c1 = st.radio(
        "1. Devi infondere 1000 ml di Soluzione Fisiologica in 8 ore usando un deflussore standard (20 gtt/ml). A quante gocce al minuto devi regolare il morsetto?",
        ["21 gtt/min", "42 gtt/min", "62 gtt/min", "125 gtt/min"],
        index=None
    )
    if c1:
        if c1 == "42 gtt/min":
            st.success("✅ Perfetto! (1000 ml × 20 gtt/ml) / 480 minuti = 41,66 -> arrotondato a 42 gtt/min.")
        else:
            st.error("❌ Errore! Converti prima le 8 ore in minuti (8 × 60 = 480 min), poi fai (1000 × 20) / 480.")

    c2 = st.radio(
        "2. Prescrizione: Morfina 4 mg ev. Hai a disposizione una fiala da 10 mg in 1 ml. Quanti ml aspiri nella siringa?",
        ["0,25 ml", "0,4 ml", "2,5 ml", "4 ml"],
        index=None
    )
    if c2:
        if c2 == "0,4 ml":
            st.success("✅ Esatto! (4 mg × 1 ml) / 10 mg = 0,4 ml (puoi diluire poi con fisiologica fino a 10 ml per avere 1 mg/ml).")
        else:
            st.error("❌ Attenzione! 10 mg : 1 ml = 4 mg : X -> X = 4 / 10 = 0,4 ml.")

    c3 = st.radio(
        "3. Un flacone di Eparina contiene 25.000 UI in 5 ml. Quanti ml devi prelevare per somministrare 5.000 UI sottocute?",
        ["0,5 ml", "1 ml", "1,5 ml", "2 ml"],
        index=None
    )
    if c3:
        if c3 == "1 ml":
            st.success("✅ Esatto! 25.000 UI : 5 ml = 5.000 UI : X -> X = 1 ml.")
        else:
            st.error("❌ Riprova! 25.000 UI in 5 ml significa che ogni millilitro contiene 5.000 UI.")
