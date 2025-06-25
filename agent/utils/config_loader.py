# agent/utils/config_loader.py
from typing import Annotated
import yaml
from pydantic import Field, TypeAdapter

from agent.configs.chat_models_cfg import (
    ChatModelConfig,
    LlamaCPPChatConfig,
    OllamaChatConfig,
)
from agent.configs.graphs_cfg import (
    GraphConfig,
    PandasDfAnalysisGraphConfig,
    DataAnalysisGraphConfig,
)

ChatCfg = Annotated[
    ChatModelConfig | OllamaChatConfig | LlamaCPPChatConfig,
    Field(discriminator="type"),
]
GraphCfg = Annotated[
    GraphConfig | PandasDfAnalysisGraphConfig | DataAnalysisGraphConfig,
    Field(discriminator="type"),
]
