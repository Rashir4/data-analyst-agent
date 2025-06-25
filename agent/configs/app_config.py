from pydantic_settings import BaseSettings, PydanticBaseSettingsSource
from agent.configs import ChatModelConfig, BaseConfig
from agent.configs.graphs_cfg import GraphConfig
from agent.utils.config_loader import ChatCfg, GraphCfg


class AppSettings(BaseSettings):
    graph: GraphCfg
    chat_model: ChatCfg
    page_title: str = "CSV Agent"

    @classmethod
    def load_from_yaml(cls, path: str) -> "AppSettings":
        import yaml

        with open(path, "r") as file:
            data = yaml.safe_load(file)
        return cls.model_validate(data)
