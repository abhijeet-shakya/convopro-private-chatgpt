from config.settings import Settings

settings = Settings()  # type: ignore


def get_groq_model_list() -> list[str]:
    model_list = settings.GROQ_MODEL
    return [
        model.strip()
        for model in model_list.split(",")
        if model.strip()
    ]
