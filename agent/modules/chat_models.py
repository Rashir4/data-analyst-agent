from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import PromptTemplate
from agent.configs import LlamaCPPChatConfig

# Path to your local model
MODEL_PATH = "./models/DeepSeek-R1-0528-Qwen3-8B-BF16.gguf"

class LlamaCPPChat(ChatLlamaCpp):
    chat_config: LlamaCPPChatConfig