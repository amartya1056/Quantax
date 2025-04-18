import streamlit as st
from gemini_interface import ask_gemini
from quantum_optimizer import optimize_tax_structure
from tax_data import treaties_db

st.set_page_config(page_title="Quantum AI Tax Engineer", layout="wide")
st.title("AI Powered Quantum Tax Engineer")

query = st.text_area("Ask your Tax Structuring Question:")

if st.button("Analyze"):
    st.subheader("Gemini AI Interpretation")
    gemini_output = ask_gemini(query)
    st.write(gemini_output)

    st.subheader("Quantum-Optimized Tax Strategy")
    optimized_strategy = optimize_tax_structure(gemini_output, treaties_db)
    st.json(optimized_strategy)