import streamlit as st
import pandas as pd

st.set_page_config(page_title="Comparador de Empenhos", page_icon="")

st.sidebar.title("Upload de Arquivos")

    # Upload do primeiro CSV
uploaded_file_1 = st.sidebar.file_uploader("Empenhos do Relatório", type=["csv"])
if uploaded_file_1 is not None:
    df1 = pd.read_csv(uploaded_file_1)
    st.write("## Empenhos do Relatório")
    st.dataframe(df1)

    # Upload do segundo CSV
uploaded_file_2 = st.sidebar.file_uploader("Empenhos Planilhados", type=["csv"])
if uploaded_file_2 is not None:
    df2 = pd.read_csv(uploaded_file_2)
    st.write("## Empenhos Planilhados")
    st.dataframe(df2)