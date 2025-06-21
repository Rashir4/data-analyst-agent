from typing import Annotated, TypedDict, Optional
from langgraph.graph.message import  add_messages
from langgraph.graph.state import StateGraph
import pandas as pd

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

class Graph():
    builder = StateGraph(AgentState)