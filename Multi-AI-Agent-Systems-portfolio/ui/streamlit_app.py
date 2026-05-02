import os
import requests
import streamlit as st

API_BASE = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Multi AI Agent Systems", layout="wide")
st.title("Multi AI Agent Systems")
st.caption("Portfolio-grade multi-agent AI platform for family operations.")

message = st.text_area(
    "What do you want your agents to do?",
    value="Plan my week, create grocery reminders, track bills, and prepare a travel checklist.",
    height=120,
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Run synchronously", type="primary"):
        res = requests.post(f"{API_BASE}/agents/run", json={"message": message}, timeout=120)
        res.raise_for_status()
        result = res.json()

        st.subheader("Final Answer")
        st.write(result["answer"])

        st.subheader("Selected Agents")
        st.write(", ".join(result["selected_agents"]))

        st.subheader("Agent Actions")
        for agent_result in result["agent_results"]:
            with st.expander(agent_result["agent_name"]):
                st.write(agent_result["summary"])
                for action in agent_result["actions"]:
                    st.success(action)

with col2:
    if st.button("Queue background job"):
        res = requests.post(f"{API_BASE}/jobs/agent-run", json={"message": message}, timeout=30)
        res.raise_for_status()
        st.json(res.json())

st.divider()
tabs = st.tabs(["Tasks", "Expenses", "Memory"])

with tabs[0]:
    st.dataframe(requests.get(f"{API_BASE}/tasks", timeout=30).json(), use_container_width=True)
with tabs[1]:
    st.dataframe(requests.get(f"{API_BASE}/expenses", timeout=30).json(), use_container_width=True)
with tabs[2]:
    st.dataframe(requests.get(f"{API_BASE}/memory", timeout=30).json(), use_container_width=True)
