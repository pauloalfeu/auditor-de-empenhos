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
    st.data_editor(df1)
    # Criando uma nova coluna 'ano' extraindo o ano da coluna 'empenho'
    df2['ANO'] = df2['EMPENHO'].str.extract(r'(\d{4})$')

    # Criando uma nova coluna 'empenho' com apenas o número
    df2['EMPENHO'] = df2['EMPENHO'].str.split('/').str[0]

    # Criando um novo DataFrame com as colunas desejadas
    empenhos_planilhados = df2[['EMPENHO', 'ANO', 'PLANILHA']]
    #empenhos_relatorio = df1[['Empenho', 'Vínculo', 'Emissão,', 'Empenhado' 'Credor']]
    empenhos_relatorio = df1['Empenho']

    # Função para comparar os DataFrames e retornar um novo DataFrame com as diferenças
    def comparar_empenhos(df1, df2):

        # Encontrar os empenhos que estão apenas em um dos DataFrames
        empenhos_unicos_df1 = df1[~df1['Empenho'].isin(df2['EMPENHO'])]
        empenhos_unicos_df2 = df2[~df2['Empenho'].isin(df1['EMPENHO'])]

        # Adicionar uma coluna para indicar a origem dos dados
        empenhos_unicos_df1['ORIGEM'] = 'Relatório'
        empenhos_unicos_df2['ORIGEM'] = 'Planilha'

        # Concatenar os DataFrames de diferenças
        diferencas = pd.concat([empenhos_unicos_df1, empenhos_unicos_df2], ignore_index=True)

        return diferencas

    # Chamar a função para comparar os DataFrames
    diferencas = comparar_empenhos(empenhos_relatorio, empenhos_planilhados)

    # Interface do Streamlit
    #st.title("Comparação de Empenhos")

    # Aba com as diferenças
    with st.tab("Empenhos não encontrados em ambos"):
        st.dataframe(diferencas)

    # Aba com os dados originais (opcional)
    with st.tab("Dados originais"):
        st.subheader("Relatório")
        st.dataframe(empenhos_relatorio)
        st.subheader("Planilha")
        st.dataframe(empenhos_planilhados)



else:
    st.info("☝️ Atenção: Para que a comparação seja realizada, é preciso que você faça o upload dos dois arquivos CSV indicados na barra lateral. Ao enviar, o sistema irá processar os dados e apresentar os resultados de forma clara e organizada.")