from abc import abstractmethod
from ast import arg
from typing import TYPE_CHECKING, Literal, Optional
from agent.configs.base_cfg import BaseConfig
from langchain_ollama import ChatOllama
 

class ChatModelConfig(BaseConfig):
    type: Literal["chat_model"] = "chat_model"
    model_path: Optional[str]
    temperature: float = 0.7
    max_tokens: int = 512
    n_ctx: int = 40960

    @abstractmethod
    def instantiate_model():
        raise NotImplementedError
    

class LlamaCPPChatConfig(ChatModelConfig):
    type: Literal["llama_cpp_chat_model"] = "llama_cpp_chat_model"
    model_path: str = "./models/Qwen3-0.6B-BF16.gguf"
    verbose: bool = False
    n_ctx: int = 40960
   
    
    def instantiate_model(self):
        from langchain_community.chat_models import ChatLlamaCpp
        return ChatLlamaCpp(model_path=self.model_path, temperature=self.temperature, max_tokens=self.max_tokens, n_ctx=self.n_ctx, verbose=self.verbose)
    
class OllamaChatConfig(ChatModelConfig):
    type: Literal["ollama_chat_model"] = "ollama_chat_model"
    model_path: str = "qwen3:1.7b"
    
    def instantiate_model(self):
        from langchain_ollama import ChatOllama
        return ChatOllama(model=self.model_path, temperature=self.temperature)