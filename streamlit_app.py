import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
import pandas as pd

def main():
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

if __name__ == "__streamlit_app__":
    main()