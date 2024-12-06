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
    df1 = pd.read_csv(uploaded_file_1, sep=';', encoding='latin1')
    df2 = pd.read_csv(uploaded_file_2, sep=',', encoding='utf-8')
    # Criando uma nova coluna 'ano' extraindo o ano da coluna 'empenho'
    df2['ANO'] = df2['EMPENHO'].str.extract(r'(\d{4})$')

    # Criando uma nova coluna 'empenho' com apenas o número
    df2['EMPENHO'] = df2['EMPENHO'].str.split('/').str[0]

    # Criando um novo DataFrame com as colunas desejadas
    empenhos_planilhados = df2[['EMPENHO', 'ANO', 'PLANILHA']]
    #empenhos_relatorio = df1[['Empenho', 'Vínculo', 'Emissão,', 'Empenhado' 'Credor']]

    df1 = df1['Empenho', 'Emissão', 'Credor'].astype(str)
    empenhos_relatorio = df1#['Empenho']

    st.data_editor(empenhos_relatorio)
    st.data_editor(empenhos_planilhados)




else:
    st.info("☝️ Atenção: Para que a comparação seja realizada, é preciso que você faça o upload dos dois arquivos CSV indicados na barra lateral. Ao enviar, o sistema irá processar os dados e apresentar os resultados de forma clara e organizada.")