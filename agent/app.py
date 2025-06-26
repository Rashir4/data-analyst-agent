import streamlit as st, pandas as pd
from agent.configs import AppSettings

cfg_path = "run_agent.yaml"  # could also be user text-box
config = AppSettings.load_from_yaml(cfg_path)

st.set_page_config(page_title=config.page_title, layout="wide")


def stream_args(question: str):
    """
    Return (*args, **kwargs) for agent.stream depending on graph type.
    - LangGraph  DataAnalysisGraph  →  stream({"messages":[...]}, stream_mode="values")
    - LangChain  (plain)            →  stream("question")
    """
    if config.graph.type == "DataAnalysisGraph":
        args = ({"messages": [{"role": "user", "content": question}]},)
        kwargs = {"stream_mode": "values"}
    else:
        args = (question,)
        kwargs = {}
    return args, kwargs


uploaded = st.file_uploader("Upload CSV", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())

    # build once per upload
    if "agent" not in st.session_state:
        agent = config.graph.instantiate_model(
            llm=config.chat_model.instantiate_model(), df=df
        )
        st.session_state.agent = agent

    question = st.chat_input("Ask a question")
    if question:
        with st.spinner("Thinking…"):
            args, kwargs = stream_args(question)
            for message in st.session_state.agent.stream(*args, **kwargs):
                response = message["messages"][-1]
                with st.chat_message("assistant"):
                    st.markdown(response.content)
