import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Configurar o layout da página
    st.set_page_config(layout="wide")

    st.title("Acompanhamento de estrategias")

    df = pd.read_csv("estrategias.csv", sep=";", decimal=",")

    consulta = df.loc[df['nomeEstrategia'] == 'cadastro de professores']
    consulta.set_index('index', inplace=True)

    selected_columns = consulta[['mes', 'valor', 'nomeEstrategia']]

    st.markdown("Abaixo os gráficos de acompanhamento das estrategias aplicadas aos indicadores da meta 15 do PNE.")

    multi = '''**INDICADOR 15A** - Proporção de docências da educação infantil com professores cuja formação superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi)

    fig = px.line(selected_columns, x='mes', y='valor', color='nomeEstrategia', title='Estrategia 2')

    st.plotly_chart(fig)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.plotly_chart(fig)

    with col2:
        st.plotly_chart(fig)

    with col3:
        st.plotly_chart(fig)

    multi = '''**INDICADOR 15B** - Proporção de docências dos anos iniciais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi)

    multi = '''**INDICADOR 15C** - Proporção de docências dos anos finais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi)

    multi = '''**INDICADOR 15D** - Proporção de docências do ensino médio com professores cuja formação superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi)

if __name__ == '__main__':
    main()
