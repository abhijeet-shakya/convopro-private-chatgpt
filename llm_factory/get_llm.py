# from llama_index.llms.ollama import Ollama # type: ignore
from langchain_groq import ChatGroq

from config.settings import Settings

settings = Settings() # type: ignore
GROQ_API_KEY=settings.GROQ_API_KEY
# OLLAMA_URL = settings.OLLAMA_URL
# print(OLLAMA_URL)

# Module - level cache for model and instance
_current_model_name = None
_current_llm_instance = None

def get_groq_llm(model_name: str): 
    global _current_model_name, _current_llm_instance

    if _current_model_name == model_name and _current_llm_instance is not None:
        return _current_llm_instance
    
    # llm = Ollama(base_url=OLLAMA_URL, model=model_name)
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model = model_name,
        temperature=0.2,
        streaming=True,
        max_tokens=1024
    )
    
    _current_model_name = model_name
    _current_llm_instance = llm
    return llm

# Example Usage
# check_llm = get_ollama_llm(model_name="llama3.2")
# print(check_llm)
# print(type(check_llm))