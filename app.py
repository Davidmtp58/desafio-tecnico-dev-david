import streamlit as st
from finlytics import carregar_extrato, calcular_resumo, top_categorias_gasto


st.title("Finlytics")
st.write("Assistente Financeiro Pessoal")

arquivo = st.file_uploader("Envie seu extrato em CSV", type=["csv"])

if arquivo is None:
    st.info("👆 Envie um arquivo CSV para ver a análise")
else:
    # Carrega os dados
    df = carregar_extrato(arquivo)

    # Calcula o resumo
    resumo = calcular_resumo(df)

    # Exibe métricas
    st.subheader("Resumo do mês")
    col1, col2, col3 = st.columns(3)
    col1.metric("Saldo do mês", f"R$ {resumo['saldo']:.2f}")
    col2.metric("Receitas", f"R$ {resumo['total_receitas']:.2f}")
    col3.metric("Despesas", f"R$ {resumo['total_despesas']:.2f}")

    # Top 3 categorias de gasto
    st.subheader("Top 3 categorias de gasto")
    top3 = top_categorias_gasto(df, n=3)
    st.bar_chart(top3)

    # Tabela com todas as transações
    st.subheader("Transações do mês")
    st.dataframe(df)