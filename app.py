import streamlit as st 
st.title("Ejemplo para usar sesion_ state")

if "count" not in st.session_state:
  st.session_state["count"] = 0

if "name" not in st.session_state: 
  st.session_state["name"] = ""


if st.button("click me"):
  st.session_state["count"] += 1

nombre = st.text_import("Escribe tu nombre")
st.write(nombre)

st.write(st.session_state)
