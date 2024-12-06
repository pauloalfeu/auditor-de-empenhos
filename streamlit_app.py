import streamlit as st
import pandas as pd

st.set_page_config(page_title="Comparador de Empenhos", page_icon="")
st.markdown("### 📑 COMPARADOR DE EMPENHOS")

st.sidebar.title("Upload dos Arquivos")

    # Upload do primeiro CSV
uploaded_file_1 = st.sidebar.file_uploader("Carregue abaixo o arquivo referente ao **relatório de 'empenhos emitios'** gerados pelos seu sistema:", type=["csv"])

    # Upload do segundo CSV
uploaded_file_2 = st.sidebar.file_uploader("Carregue abaixo o arquivo referente aos **empenhos planilhados**:", type=["csv"])

if (uploaded_file_1 is not None) and (uploaded_file_2 is not None):
    df1 = pd.read_csv(uploaded_file_1)
    st.write("## Empenhos do Relatório")
    st.dataframe(df1)
else:
    st.info("☝️ Atenção: Para que a comparação seja realizada, é preciso que você faça o upload dos dois arquivos CSV indicados na barra lateral. Ao enviar, o sistema irá processar os dados e apresentar os resultados de forma clara e organizada.")