import streamlit as st 
st.title("Ejemplo para usar sesion_ state")

if "count" not in st.session_state:
  st.session_state["count"] = 0


if st.button("click me"):
  st.session_state["count"] += 1
