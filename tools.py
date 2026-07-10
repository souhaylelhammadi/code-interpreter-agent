"""Outillage Python (optionnel).

Ce fichier n'est pas nécessaire au fonctionnement actuel de l'app, puisque
`agent.py` utilise `create_pandas_dataframe_agent` directement.

On le conserve (corrigé) pour éviter les erreurs d'import lors du chargement
du module.
"""

from __future__ import annotations

from typing import Any


def get_code_execution_tool(dataframe_context: Any):
    """Retourne (si disponible) un outil d'exécution Python connecté au contexte.

    NOTE: Si l'import de l'outil LangChain change selon la version installée,
    on bascule silencieusement sur `None` plutôt que de casser l'application.
    """

    try:
        # Import correct selon les versions LangChain.
        from langchain_experimental.tools import PythonREPLTool

        tool = PythonREPLTool()
        # Certains outils exposent un champ `globals`.
        if hasattr(tool, "globals"):
            tool.globals = {"df": dataframe_context}
        return tool
    except Exception:
        return None

