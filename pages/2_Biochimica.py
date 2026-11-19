import streamlit as st
import math

st.set_page_config(page_title="Biochimica", page_icon="🧬", layout="wide")

st.title("🧬 Modulo 2: Propedeutica Biochimica (1° Anno)")
st.markdown("Focus clinico su equilibrio acido-base ematico (EGA), biomolecole, enzimi e metabolismo energetico.")

tab1, tab2, tab3, tab4 = st.tabs([
    "🩸 Tampone Ematico (Henderson-Hasselbalch)", 
    "🧱 Biomolecole", 
    "⚡ Enzimi e Metabolismo", 
    "📝 Quiz di Verifica"
])

with tab1:
    st.header("Sistema Tampone Bicarbonato e Lettura Base EGA")
    st.markdown("Il pH del sangue arterioso è mantenuto tra **7.35 e 7.45** dall'equazione di **Henderson-Hasselbalch**:")
    st.latex(r"pH = 6.1 + \log_{10} \left( \frac{[HCO_3^-]}{0.03 \times PaCO_2} \right)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Simulatore pH Ematico (EGA)")
        hco3 = st.slider("Bicarbonati [HCO3-] (mEq/L) - Valore normale: 22-26", 5.0, 45.0, 24.0, 0.5)
        paco2 = st.slider("Pressione Parziale CO2 [PaCO2] (mmHg) - Valore normale: 35-45", 15.0, 90.0, 40.0, 1.0)
        
        ph_sangue = 6.1 + math.log10(hco3 / (0.03 * paco2))
        st.metric(label="pH Ematico Calcolato", value=f"{ph_sangue:.2f}")
        
    with col2:
        st.subheader("Interpretazione Fisiopatologica")
        if 7.35 <= ph_sangue <= 7.45:
            st.success("🟢 **pH nella norma (Eubremia / Compenso)**")
        elif ph_sangue < 7.35:
            st.error("🔴 **ACIDEMIA (pH < 7.35)**")
            if paco2 > 45:
                st.write("- **Componente Respiratoria:** Ipoventilazione con accumulo di $CO_2$ (Acidosi Respiratoria).")
            if hco3 < 22:
                st.write("- **Componente Metabolica:** Perdita o consumo di bicarbonati $HCO_3^-$ (Acidosi Metabolica).")
        else:
            st.warning("🟠 **ALCALEMIA (pH > 7.45)**")
            if paco2 < 35:
                st.write("- **Componente Respiratoria:** Iperventilazione con perdita di $CO_2$ (Alcalosi Respiratoria).")
            if hco3 > 26:
                st.write("- **Componente Metabolica:** Eccesso di bicarbonati $HCO_3^-$ (Alcalosi Metabolica).")

with tab2:
    st.header("Schema Rapido delle 4 Biomolecole")
    
    with st.expander("🍞 1. Glucidi (Carboidrati)", expanded=True):
        st.markdown("""
        * **Funzione principale:** Energetica immediata (4 kcal/g).
        * **Monomeri (Monosaccaridi):** Glucosio (glicemia normale a digiuno: **70 - 100 mg/dL**), Fruttosio, Galattosio.
        * **Polisaccaridi di riserva:** **Glicogeno** (accumulato nel fegato per mantenere la glicemia e nei muscoli per lo sforzo).
        """)
        
    with st.expander("🥑 2. Lipidi"):
        st.markdown("""
        * **Funzione principale:** Riserva energetica a lungo termine (9 kcal/g), isolante termico, struttura delle membrane.
        * **Trigliceridi:** Glicerolo + 3 acidi grassi (forma di deposito nel tessuto adiposo).
        * **Fosfolipidi:** Molecole *anfipatiche* (testa polare idrofila + code apolari idrofobe) che formano il doppio strato delle membrane cellulari.
        * **Colesterolo:** Precursore degli ormoni steroidei, della vitamina D e dei sali biliari.
        """)
        
    with st.expander("🥩 3. Proteine"):
        st.markdown("""
        * **Monomeri:** 20 Amminoacidi uniti dal **legame peptidico**.
        * **Strutture:** Primaria (sequenza), Secondaria ($\\alpha$-elica e foglietto-$\\beta$), Terziaria (forma 3D funzionale), Quaternaria (es. **Emoglobina**, 4 subunità con gruppo Eme e $Fe^{2+}$).
        * **Denaturazione:** Perdita della struttura 3D (e quindi della funzione) dovuta a febbre altissima o variazioni estreme di pH.
        """)
        
    with st.expander("🧬 4. Acidi Nucleici (DNA e RNA)"):
        st.markdown("""
        * **Monomeri (Nucleotidi):** Zucchero pentoso (Desossiribosio nel DNA, Ribosio nell'RNA) + Gruppo Fosfato + Base Azotata.
        * **Complementarietà delle basi:** Nel DNA **A-T** e **C-G**. Nell'RNA la Timina è sostituita dall'**Uracile (U)**.
        * **ATP (Adenosina Trifosfato):** Nucleotide specializzato che funge da "moneta energetica" della cellula.
        """)

with tab3:
    st.header("Enzimi e Vie Metaboliche Principali")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Catalisi Enzimatica")
        st.markdown("""
        * Gli enzimi sono **catalizzatori biologici** (quasi sempre proteine) che **abbassano l'energia di attivazione** accelerando le reazioni senza consumarsi.
        * **Sito Attivo:** Tasca specifica dove si lega il substrato (modello *adattamento indotto*).
        * **Marcatori Clinici:** L'aumento nel sangue di specifici enzimi indica danno d'organo (es. *Transaminasi AST/ALT* per il fegato, *Amilasi/Lipasi* per il pancreas, *CPK* per il muscolo).
        """)
    with col2:
        st.subheader("Respirazione Cellulare (Resa Energetica)")
        st.markdown("""
        1. **Glicolisi (Citoplasma - Anaerobica):** 1 Glucosio $\\rightarrow$ 2 Piruvato + **2 ATP** + 2 NADH. *(In assenza di $O_2$, il piruvato diventa **Acido Lattico**)*.
        2. **Ciclo di Krebs (Matrice Mitocondriali - Aerobico):** Ossidazione completa dell'Acetil-CoA con produzione di $CO_2$, NADH e $FADH_2$.
        3. **Fosforilazione Ossidativa (Creste Mitocondriali):** Catena di trasporto degli elettroni con $O_2$ come accettore finale. Resa totale: **~30-32 ATP** per molecola di glucosio.
        """)

with tab4:
    st.header("Quiz di Autovalutazione")
    
    q1 = st.radio(
        "1. Un paziente con grave crisi d'ansia iperventila eliminando molta CO2. Che alterazione del pH rischia di sviluppare?",
        ["Acidosi respiratoria", "Alcalosi respiratoria", "Acidosi metabolica", "Alcalosi metabolica"],
        index=None
    )
    if q1:
        if q1 == "Alcalosi respiratoria":
            st.success("✅ Esatto! Eliminando troppa CO2 (acido volatile), il pH ematico sale sopra 7.45.")
        else:
            st.error("❌ Riprova! La CO2 in acqua forma acido carbonico: se la elimini troppo velocemente, il sangue diventa più basico.")

    q2 = st.radio(
        "2. In condizioni di ipossia (carenza di ossigeno nei tessuti), in cosa viene convertito il piruvato prodotto dalla glicolisi?",
        ["Acetil-CoA", "Glicogeno", "Acido Lattico (Lattato)", "Colesterolo"],
        index=None
    )
    if q2:
        if q2 == "Acido Lattico (Lattato)":
            st.success("✅ Esatto! La fermentazione lattica permette di rigenerare NAD+ per continuare a produrre almeno 2 ATP in assenza di ossigeno.")
        else:
            st.error("❌ Sbagliato. In assenza di ossigeno i mitocondri si bloccano e il piruvato viene ridotto a lattato.")
