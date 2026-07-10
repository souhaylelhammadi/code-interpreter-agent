from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import config
import prompts

def create_code_interpreter_agent(df):
    """
    Initialise et retourne l'agent de prompt/exécution Pandas avec Groq.
    """
    # Initialisation du LLM via Groq
    llm = ChatGroq(
        model=config.MODEL_NAME, 
        temperature=config.TEMPERATURE,
        groq_api_key=config.GROQ_API_KEY
    )
    
    # Création de l'agent
    agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, # Optimisé pour l'interaction textuelle standard
        allow_dangerous_code=True,
        prefix=prompts.SYSTEM_PROMPT
    )
    return agent