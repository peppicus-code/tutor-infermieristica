import streamlit as st
import math

st.set_page_config(page_title="Chimica Base", page_icon="🧪", layout="wide")

st.title("🧪 Modulo 1: Chimica Generale e Inorganica (1° Anno)")
st.markdown("Strumenti di calcolo passo-passo e quiz per preparare l'esame di Chimica.")

tab1, tab2, tab3, tab4 = st.tabs([
    "⚖️ Moli e Molarità", 
    "💧 Concentrazioni % e Osmolarità", 
    "🌡️ Calcolo del pH", 
    "📝 Quiz di Verifica"
])

with tab1:
    st.header("Calcolo delle Moli e della Molarità (M)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Da Grammi a Moli (n)")
        massa = st.number_input("Massa del soluto (grammi):", min_value=0.0, value=5.85, step=0.1)
        pm = st.number_input("Peso Molecolare - PM (g/mol):", min_value=0.1, value=58.44, step=0.1, help="Es. NaCl = 58.44 g/mol, Glucosio = 180.16 g/mol")
        
        if st.button("Calcola Moli", key="btn_moli"):
            moli = massa / pm
            st.success(f"**Risultato:** {moli:.4f} mol ({moli*1000:.2f} mmol)")
            st.info(f"**Formula applicata:** $n = \\frac{{massa}}{{PM}} = \\frac{{{massa}}}{{{pm}}} = {moli:.4f}$ mol")

    with col2:
        st.subheader("2. Calcolo Molarità (M = mol/L)")
        moli_in = st.number_input("Numero di moli (mol):", min_value=0.0, value=0.1, step=0.01, format="%.4f")
        vol_ml = st.number_input("Volume della soluzione (ml):", min_value=1.0, value=500.0, step=10.0)
        
        if st.button("Calcola Molarità", key="btn_mol"):
            vol_l = vol_ml / 1000.0
            molarita = moli_in / vol_l
            st.success(f"**Molarità:** {molarita:.4f} M (mol/L)")
            st.info(f"**Passaggi:**\n1. Converto ml in Litri: ${vol_ml} \\text{{ ml}} = {vol_l} \\text{{ L}}$\n2. Divido moli per Litri: $M = \\frac{{{moli_in}}}{{{vol_l}}} = {molarita:.4f}$ M")

with tab2:
    st.header("Concentrazioni Percentuali e Osmolarità Clinica")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Concentrazione % peso/volume (% p/v)")
        st.caption("Indica quanti grammi di soluto sono sciolti in 100 ml di soluzione (es. Fisiologica 0.9% = 0.9 g in 100 ml).")
        perc = st.number_input("Percentuale della soluzione (% p/v):", min_value=0.0, value=0.9, step=0.1)
        vol_sol = st.number_input("Volume totale flacone (ml):", min_value=1.0, value=500.0, step=50.0)
        
        if st.button("Calcola Grammi Totali", key="btn_perc"):
            grammi_tot = (perc * vol_sol) / 100.0
            st.success(f"**Soluto presente:** {grammi_tot:.2f} grammi ({grammi_tot*1000:.0f} mg)")
            st.info(f"**Proporzione:** ${perc}\\text{{ g}} : 100\\text{{ ml}} = X : {vol_sol}\\text{{ ml}}$")

    with col2:
        st.subheader("Osmolarità Teorica (mOsm/L)")
        st.caption("Fondamentale per capire se una soluzione è isotonica (~280-300 mOsm/L), ipotonica o ipertonica.")
        molarita_osm = st.number_input("Molarità della soluzione (M):", min_value=0.0, value=0.154, step=0.01, format="%.3f", help="Es. NaCl 0.9% è circa 0.154 M")
        coeff_i = st.number_input("Coefficiente di dissociazione (i):", min_value=1, max_value=5, value=2, help="NaCl si dissocia in Na+ e Cl- (i=2). Il Glucosio non si dissocia (i=1).")
        
        if st.button("Calcola Osmolarità", key="btn_osm"):
            osm = molarita_osm * coeff_i * 1000
            st.success(f"**Osmolarità:** {osm:.1f} mOsm/L")
            if 275 <= osm <= 305:
                st.info("🟢 **Soluzione ISOTONICA** rispetto al plasma umano.")
            elif osm < 275:
                st.warning("🟡 **Soluzione IPOTONICA** (rischio emolisi se infusa pura).")
            else:
                st.error("🔴 **Soluzione IPERTONICA** (richiama acqua dalle cellule).")

with tab3:
    st.header("Calcolo del pH (Acidi e Basi Forti)")
    tipo = st.radio("Tipo di sostanza:", ["Acido Forte (es. HCl)", "Base Forte (es. NaOH)"], horizontal=True)
    conc_h = st.number_input("Concentrazione Molare (M):", min_value=0.0000001, max_value=1.0, value=0.001, format="%.6f")
    
    if st.button("Calcola pH", key="btn_ph"):
        if "Acido" in tipo:
            ph = -math.log10(conc_h)
            st.success(f"**pH = {ph:.2f}** (Ambiente Acido)")
            st.info(f"**Formula:** $pH = -\\log_{{10}}[H^+] = -\\log_{{10}}({conc_h}) = {ph:.2f}$")
        else:
            poh = -math.log10(conc_h)
            ph = 14.0 - poh
            st.success(f"**pH = {ph:.2f}** (Ambiente Basico | pOH = {poh:.2f})")
            st.info(f"**Passaggi:**\n1. $pOH = -\\log_{{10}}[OH^-] = {poh:.2f}$\n2. $pH = 14 - pOH = 14 - {poh:.2f} = {ph:.2f}$")

with tab4:
    st.header("Metti alla prova le tue conoscenze")
    
    q1 = st.radio(
        "1. Quanti grammi di NaCl sono contenuti in un flacone di soluzione fisiologica (0,9%) da 250 ml?",
        ["0,9 grammi", "2,25 grammi", "9 grammi", "22,5 grammi"],
        index=None
    )
    if q1:
        if q1 == "2,25 grammi":
            st.success("✅ Esatto! (0,9 g : 100 ml = X : 250 ml -> X = 2,25 g)")
        else:
            st.error("❌ Riprova! Imposta la proporzione: 0,9 g stanno a 100 ml come X sta a 250 ml.")

    q2 = st.radio(
        "2. Una soluzione di Glucosio al 5% (PM = 180 g/mol, i = 1) ha un'osmolarità di circa 278 mOsm/L. Come viene definita rispetto al plasma?",
        ["Ipertonica", "Ipotonica", "Isotonica"],
        index=None
    )
    if q2:
        if q2 == "Isotonica":
            st.success("✅ Esatto! L'osmolarità plasmatica normale è tra 275 e 295 mOsm/L.")
        else:
            st.error("❌ Sbagliato. Il plasma umano ha un'osmolarità di circa 285 mOsm/L, quindi 278 mOsm/L è isotonica.")
