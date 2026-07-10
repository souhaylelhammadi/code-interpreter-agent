# 🤖 Groq Code Interpreter Agent

Une application moderne et modulaire construite avec **Streamlit**, **LangChain** et **Groq**. Elle permet à un utilisateur de téléverser un fichier CSV, de poser des questions en langage naturel, puis de générer et d'exécuter automatiquement du code Python pour afficher la réponse ainsi que des graphiques.

---

## 🚀 Fonctionnalités
- **Analyse en langage naturel** : Posez des questions simples comme *"Quel est le produit le plus vendu ?"*.
- **Génération & Exécution de code** : L'agent écrit le script Pandas, l'exécute localement et interprète le résultat.
- **Visualisation automatique** : Génération automatique de graphiques (Matplotlib/Seaborn) si demandée.
- **Vitesse Groq** : Propulsé par l'infrastructure ultra-rapide de Groq.

---
<img width="1470" height="956" alt="Capture d’écran 2026-07-10 à 21 47 46" src="https://github.com/user-attachments/assets/e322e5bc-290e-4c4f-a005-bb63d592f10a" />

## 📂 Structure du Projet
```text
code-interpreter-agent/
│
├── app.py             # Interface utilisateur Streamlit
├── agent.py           # Logique de création de l'agent LangChain & Groq
├── tools.py           # Outils d'exécution de code (REPL)
├── prompts.py         # Instructions système de l'agent
├── config.py          # Configuration et gestion des clés API
├── requirements.txt   # Dépendances du projet
└── .env               # Variables d'environnement (Non suivi par Git)

'''
