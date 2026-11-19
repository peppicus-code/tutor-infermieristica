import streamlit as st

st.set_page_config(
    page_title="Tutor Infermieristica",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Portale di Studio: Infermieristica (1° - 3° Anno)")
st.subheader("Chimica, Propedeutica Biochimica, Calcolo Farmacologico e Area Critica")

st.markdown("""
Benvenuta nel tuo strumento di studio interattivo! Usa il **menu laterale a sinistra** (clicca su `>` in alto a sinistra su tablet) per navigare tra i moduli del corso di laurea:

* **🧪 1. Chimica Base (1° Anno):** Calcolo moli, molarità, osmolarità, concentrazioni % p/v e pH.
* **🧬 2. Propedeutica Biochimica (1° Anno):** Simulatore tampone ematico (EGA), biomolecole, enzimi e metabolismo.
* **💉 3. Calcolo Farmaci (2° Anno):** Proporzioni per dosaggi, velocità di infusione (`ml/h` e `gtt/min`), conversioni e dose/peso.
* **🚑 4. Area Critica 3° Anno (3° Anno):** Pompe siringa (`mcg/kg/min` e `UI/h`), bilancio idrico 24h e Gap Anionico.
""")

st.success("💡 **Suggerimento:** Ogni sezione include sia i calcolatori con i passaggi matematici spiegati, sia i quiz di autovalutazione.")
