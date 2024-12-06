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
    df1 = pd.read_csv(uploaded_file_1, sep=',', encoding='latin1')
    df2 = pd.read_csv(uploaded_file_2, sep=',', encoding='latin1')

    # Criando uma nova coluna 'ano' extraindo o ano da coluna 'empenho'
    df2['ano'] = df2['empenho'].str.extract(r'(\d{4})$')

    # Criando uma nova coluna 'empenho' com apenas o número
    df2['empenho'] = df2['empenho'].str.split('/').str[0]

    # Criando um novo DataFrame com as colunas desejadas
    empenhos_planilhados = df2[['empenho', 'ano']]

    # Convertendo as colunas 'empenho' e 'ano' para o tipo numérico (opcional)
    empenhos_planilhados['empenho'] = pd.to_numeric(empenhos_planilhados['empenho'])
    empenhos_planilhados['ano'] = pd.to_numeric(empenhos_planilhados['ano'])

    st.data_editor(empenhos_planilhados)




else:
    st.info("☝️ Atenção: Para que a comparação seja realizada, é preciso que você faça o upload dos dois arquivos CSV indicados na barra lateral. Ao enviar, o sistema irá processar os dados e apresentar os resultados de forma clara e organizada.")