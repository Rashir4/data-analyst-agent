#!/usr/bin/env python
"""
Quick sanity-check for PyodideSandboxTool (langchain-sandbox PR-37).

• Attaches a tiny text file (`input.txt`)
• Runs Python code inside the Pyodide sandbox:
    – reads the file
    – prints its contents and length
    – fetches example.com (allow_net=True)
"""


from langchain_sandbox import PyodideSandboxTool
from agent.configs.chat_models_cfg import LlamaCPPChatConfig, OllamaChatConfig
from langgraph.prebuilt import create_react_agent

# 1. create the sandbox tool -----------------------------------------------
# with open("customers-100000.csv", "rb") as f:
#     # Attach a file to the sandbox
#     # (this is optional, you can run code without any files)
#     files = f.read()
sales_data = """
2024-01-15,Laptop,Electronics,2,1299.99,North
2024-01-16,Chair,Furniture,1,249.50,South
2024-01-16,T-shirt,Clothing,5,29.99,East
2024-01-17,Laptop,Electronics,1,1299.99,West
2024-01-18,Phone,Electronics,3,799.99,North
2024-01-19,Desk,Furniture,2,399.99,South
2024-01-20,Jeans,Clothing,4,79.99,East
2024-01-21,Tablet,Electronics,2,499.99,West
2024-01-22,Sofa,Furniture,1,899.99,North
2024-01-23,Shoes,Clothing,3,129.99,South"""

sb_tool = PyodideSandboxTool(
    files={"/home/pyodide/sales.csv": str.encode(sales_data)}, allow_net=True
)

print("✅  Tool created:", sb_tool)

# 2. code to run inside the sandbox -----------------------------------------
# Test the LLamaCPPChat class

chat_model = OllamaChatConfig().instantiate_model()

agent = create_react_agent(
    model=chat_model,
    tools=[sb_tool],
    prompt="Use the tool to analyse the data within it.",
)

for message in agent.stream(
    {
        "messages": "Give me a summary of the data"
    },
    stream_mode="values",
):
    message["messages"][-1].pretty_print()
