import streamlit as st
import pandas as pd

st.set_page_config(page_title="Comparador de Empenhos", page_icon="")
st.markdown("### 📑 COMPARADOR DE EMPENHOS")

st.sidebar.title("Upload dos Arquivos")

    # Upload do primeiro CSV
uploaded_file_1 = st.sidebar.file_uploader("Carregue abaixo o arquivo referente ao **relatório de 'empenhos emitios'** gerados pelos seu sistema:")

    # Upload do segundo CSV
uploaded_file_2 = st.sidebar.file_uploader("Carregue abaixo o arquivo referente aos **empenhos planilhados**:")

st.sidebar.warning("""Para haver processamento correto, a planilha inserida deve conter uma coluna chamada **'EMPENHO'** no topo e logo abaixo todos os números de empenhos que se deseja verificar. 

Para isso, basta colar os números dos empenhos que serão buscados em uma planilha em branco (ideal para pesquisar por empenhos de mais de uma planilha""")

if (uploaded_file_1 is not None) and (uploaded_file_2 is not None):
    df1 = pd.read_csv(uploaded_file_1, sep=';', encoding='latin1')
    df1 = pd.DataFrame(df1)
    df2 = pd.read_csv(uploaded_file_2, sep=',', encoding='utf-8')
    df2 = pd.DataFrame(df2)
    # Criando uma nova coluna 'ano' extraindo o ano da coluna 'empenho'
    df2['ANO'] = df2['EMPENHO'].str.extract(r'(\d{4})$')

    # Criando uma nova coluna 'empenho' com apenas o número
    df2['EMPENHO'] = df2['EMPENHO'].str.split('/').str[0]

    # Criando um novo DataFrame com as colunas desejadas
    empenhos_planilhados = df2[['EMPENHO', 'ANO', 'PLANILHA']]
    #empenhos_relatorio = df1[['Empenho', 'Vínculo', 'Emissão,', 'Empenhado' 'Credor']]

    df1['Empenho'] = df1['Empenho'].astype(str)
    empenhos_relatorio = df1#['Empenho']


    # Encontrar os empenhos únicos em cada DataFrame
    empenhos_unicos_planilhados = set(empenhos_planilhados['EMPENHO']) - set(empenhos_relatorio['Empenho'])
    empenhos_unicos_relatorio = set(empenhos_relatorio['Empenho']) - set(empenhos_planilhados['EMPENHO'])

    # Criar DataFrames com os empenhos únicos
    df_unicos_relatorio = empenhos_relatorio[empenhos_relatorio['Empenho'].isin(empenhos_unicos_relatorio)]
    df_unicos_planilhados = empenhos_planilhados[empenhos_planilhados['EMPENHO'].isin(empenhos_unicos_planilhados)]

    # Concatenar os DataFrames de diferenças
    diferencas = pd.concat([df_unicos_relatorio, df_unicos_planilhados], ignore_index=True)
    diferencas.dropna(subset=['Empenho'], inplace=True)


    # Exibir o DataFrame com as diferenças
    diferencas.drop(columns=['Espécie', 'Dotação', 'Vínculo', 'Estornado', 'Revertido', 'Líquido', 'EMPENHO', 'ANO', 'PLANILHA' ], inplace=True)
    # Removendo a coluna sem nome (índice 1)
    diferencas = diferencas.dropna(axis=1, how='all')
    st.data_editor(diferencas)


else:
    st.info("☝️ Atenção: Para que a comparação seja realizada, é preciso que você faça o upload dos dois arquivos CSV indicados na barra lateral. Ao enviar, o sistema irá processar os dados e apresentar os resultados de forma clara e organizada.")