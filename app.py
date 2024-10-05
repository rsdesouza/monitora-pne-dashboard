import streamlit as st
import plotly.express as px
from st_files_connection import FilesConnection

def main():
    # Configurar o layout da página
    st.set_page_config(layout="wide")

    st.title("Acompanhamento de estratégias")

    # Conectar ao GCS e ler o arquivo CSV
    conn = st.connection('gcs', type=FilesConnection)

    # Especificar o caminho do arquivo no bucket do GCS
    df = conn.read("monitora_pne_15_streamlit/estrategias.csv", input_format="csv", ttl=600, sep=";", decimal=",")

    # Filtrar os dados para a estratégia 'cadastro de professores'
    consulta = df.loc[df['nomeEstrategia'] == 'cadastro de professores']
    consulta.set_index('index', inplace=True)

    # Selecionar colunas relevantes
    selected_columns = consulta[['mes', 'valor', 'nomeEstrategia']]

    st.markdown("Abaixo os gráficos de acompanhamento das estratégias aplicadas aos indicadores da meta 15 do PNE.")

    # Descrição do indicador 15A
    multi = '''**INDICADOR 15A** - Proporção de docências da educação infantil com professores cuja formação superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi)

    # Criar o gráfico
    fig = px.line(selected_columns, x='mes', y='valor', color='nomeEstrategia', title='Estrategia 2')
    st.plotly_chart(fig)

    # Exibir os gráficos em colunas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.plotly_chart(fig)
    with col2:
        st.plotly_chart(fig)
    with col3:
        st.plotly_chart(fig)

    # Outros indicadores
    st.markdown('''**INDICADOR 15B** - Proporção de docências dos anos iniciais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.''')

    st.markdown('''**INDICADOR 15C** - Proporção de docências dos anos finais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.''')

    st.markdown('''**INDICADOR 15D** - Proporção de docências do ensino médio com professores cuja formação superior está adequada à área de conhecimento que lecionam.''')

if __name__ == "__main__":
    main()
