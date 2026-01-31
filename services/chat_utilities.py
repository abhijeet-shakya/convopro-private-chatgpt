# from llama_index.core.llms import ChatMessage, MessageRole

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from llm_factory.get_llm import get_groq_llm

def get_answer(model_name: str, chat_history: list[dict]):
    llm = get_groq_llm(model_name)

    SYSTEM_PROMPT = """
    You are a helpful assistant.

    IMPORTANT RESPONSE RULES:
    - Give a complete and correct answer.
    - Be concise and avoid repetition.
    - Use short paragraphs or bullet points.
    - Do NOT exceed 1024 tokens in your response.
    - If the topic is large, summarize the key points instead of going deep.
    FORMAT RULES (IMPORTANT):
    - Use proper mathematical notation.
    - Use markdown formatting.
    - Write formulas on separate lines.
    - Use bullet points for explanations.
    - Avoid repetition.
    - Keep the answer clean and structured like study notes.

    When explaining math:
    - First show the formula
    - Then explain symbols
    - Then explain special cases clearly
    """


    message = [
        SystemMessage(content=SYSTEM_PROMPT)
    ]

    for msg in chat_history:
        role = msg["role"].lower()
        content = msg["content"]

        if role in ("user", "human"):
            message.append(HumanMessage(content=content))
        elif role in ("assistant", "ai"):
            message.append(AIMessage(content = content))
        elif role == "system":
            message.append(SystemMessage(content=content))
        else:
            raise ValueError(f"Unsupported role : {role}")
    
    for chunk in llm.stream(message):
        if chunk.content:
            yield chunk.content