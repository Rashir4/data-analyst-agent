from abc import abstractmethod
from ast import arg
from typing import TYPE_CHECKING, Optional
from agent.configs.base_cfg import BaseConfig

if TYPE_CHECKING:
    from agent.modules import LlamaCPPChat    

class ChatModelConfig(BaseConfig):
    model_path: Optional[str]
    temperature: float = 0.7
    max_tokens: int = 512
    n_ctx: int = 2048

    @abstractmethod
    def load_llm():
        raise NotImplementedError
    

class LlamaCPPChatConfig(ChatModelConfig):
    model_path: str = "./models/DeepSeek-R1-0528-Qwen3-8B-BF16.gguf"

    def load_llm(self):
        from agent.modules import LlamaCPPChat
        return LlamaCPPChat(model_path=self.model_path, temperature=self.temperature, max_tokens=self.max_tokens, n_ctx=self.n_ctx,chat_config=self)