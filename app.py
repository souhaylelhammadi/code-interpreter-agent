import streamlit as st
import pandas as pd
import os
from agent import create_code_interpreter_agent

st.set_page_config(page_title="Groq Code Interpreter", layout="wide")
st.title("🤖 Code Interpreter Agent (Powered by Groq)")

# S'assurer que le dossier 'generated' existe
os.makedirs("generated", exist_ok=True)

uploaded_file = st.file_uploader("Chargez un fichier CSV pour l'analyse", type=["csv"])

if uploaded_file is not None:
    @st.cache_data
    def load_data(file):
        return pd.read_csv(file)
        
    df = load_data(uploaded_file)
    
    st.subheader("📊 Aperçu de vos données")
    st.dataframe(df.head(3))
    
    # Initialisation de l'agent connecté à Groq
    agent = create_code_interpreter_agent(df)
    
    user_query = st.text_input("Posez votre question sur les données :")
    
    if user_query:
        plot_path = "generated/plot.png"
        if os.path.exists(plot_path):
            os.remove(plot_path)
            
        with st.spinner("Groq analyse et exécute le code en un temps record..."):
            try:
                response = agent.run(user_query)
                
                st.subheader("💡 Réponse")
                st.write(response)
                
                if os.path.exists(plot_path):
                    st.subheader("📈 Graphique généré")
                    st.image(plot_path)
                    
            except Exception as e:
                st.error(f"Une erreur est survenue : {e}")