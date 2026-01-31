from langchain_core.prompts import PromptTemplate
from llm_factory.get_llm import get_groq_llm  # Groq-based LLM factory


def get_chat_title(model: str, user_query: str) -> str:
    llm = get_groq_llm(model)

    title_prompt_template = """
    You are a helpful assistant that generates short, clear, and catchy titles.

    Task:
    - Read the given user query.
    - Create a concise title (max 7 words).
    - The title should summarize the intent of the query.
    - Avoid unnecessary words, punctuation, or filler.
    - Keep it professional and easy to understand.

    User Query:
    {user_query}

    Output:
    Title:
    """

    prompt = PromptTemplate(
        input_variables=["user_query"],
        template=title_prompt_template
    )

    formatted_prompt = prompt.format(user_query=user_query)

    response = llm.invoke(formatted_prompt)
    return response.content.strip()
