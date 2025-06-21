from agent.configs import ChatModelConfig, BaseConfig

class AppConfig(BaseConfig):
    llm: ChatModelConfig
    