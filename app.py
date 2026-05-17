import streamlit as st

st.title("Finlytics")
st.write("Olá! Esse é meu primeiro app Streamlit.")

nome = st.text_input("Qual é o seu nome?")
st.write(f"Bem-vindo(a), {nome}!")