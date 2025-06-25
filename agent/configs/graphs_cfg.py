from abc import abstractmethod
from ast import arg
from typing import TYPE_CHECKING, Literal, Optional
from agent.configs.base_cfg import BaseConfig
from langchain_sandbox import PyodideSandboxTool
from langgraph.prebuilt import create_react_agent


class GraphConfig(BaseConfig):
    type: Literal["graph"] = "graph"
    has_memory: bool = False
    
    @abstractmethod
    def instantiate_model(self):
        raise NotImplementedError
    
class PandasDfAnalysisGraphConfig(GraphConfig):
    type: Literal["PandasDfAnalysisGraph"] = "PandasDfAnalysisGraph"
    
    
    def instantiate_model(self, llm, df):
        from langchain_experimental.agents import create_pandas_dataframe_agent
        return create_pandas_dataframe_agent(
            llm=llm,
            df=df,
            allow_dangerous_code=True)

class DataAnalysisGraphConfig(GraphConfig):
    type: Literal["DataAnalysisGraph"] = "DataAnalysisGraph"
    
    def instantiate_model(self, llm, df):
       df_bytes = df.to_json().encode()
       sandbox_tool = PyodideSandboxTool(files={"input.csv": df_bytes}, allow_net=True)
       return create_react_agent(
              model=llm,
              tools=[sandbox_tool],
              prompt="Use the tool to analyze the data within it."
         )