import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
import pandas as pd

def main():
    st.title("Comparador de Empenhos")

    # Upload dos arquivos
    uploaded_file_relatorio = st.file_uploader("Escolha o arquivo CSV dos Empenhos do Relatório", type=["csv"])
    uploaded_file_planilhados = st.file_uploader("Escolha o arquivo CSV dos Empenhos Planilhados", type=["csv"])

    if uploaded_file_relatorio and uploaded_file_planilhados:
        # Carregar os dados dos arquivos
        df_relatorio = pd.read_csv(uploaded_file_relatorio)
        df_planilhados = pd.read_csv(uploaded_file_planilhados)

        # Aqui você implementará a lógica de comparação
        # Por exemplo, para encontrar os empenhos que estão em um arquivo e não no outro:
        empenhos_unicos_relatorio = df_relatorio[~df_relatorio['Coluna_Empenho'].isin(df_planilhados['Coluna_Empenho'])]
        empenhos_unicos_planilhados = df_planilhados[~df_planilhados['Coluna_Empenho'].isin(df_relatorio['Coluna_Empenho'])]

        # Exibir os resultados em tabelas
        st.subheader("Empenhos Únicos no Relatório")
        st.dataframe(empenhos_unicos_relatorio)

        st.subheader("Empenhos Únicos na Planilha")
        st.dataframe(empenhos_unicos_planilhados)

if __name__ == "__main__":
    main()