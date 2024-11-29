import streamlit as st
import pandas as pd
import plotly.express as px
from st_files_connection import FilesConnection

# Configurar o layout da página
st.set_page_config(layout="wide")

# Conectar ao Google Cloud Storage (GCS) e ler o arquivo CSV
conn = st.connection('gcs', type=FilesConnection)
df = conn.read("monitora_pne_15_streamlit/estrategias.csv", input_format="csv", ttl=600, sep=";", decimal=",")

# Ordenar os meses corretamente
df['mes'] = pd.Categorical(
    df['mes'],
    categories=["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
    ordered=True
)
df = df.sort_values(by=['ano', 'mes'])  # Ordenar por ano e mês

# Lista de indicadores e textos explicativos
indicadores = {
    "indicador1": "**INDICADOR 15A** - Proporção de docências da educação infantil com professores cuja formação superior está adequada à área de conhecimento que lecionam.",
    "indicador2": "**INDICADOR 15B** - Proporção de docências dos anos iniciais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.",
    "indicador3": "**INDICADOR 15C** - Proporção de docências dos anos finais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.",
    "indicador4": "**INDICADOR 15D** - Proporção de docências do ensino médio com professores cuja formação superior está adequada à área de conhecimento que lecionam.",
}

# Função para exibir gráficos por indicador
def exibir_graficos_por_indicador(indicador, descricao):
    st.markdown(descricao)

    # Filtrar dados pelo indicador
    data = df[df['indicador'] == indicador]
    estrategias = data['nomeEstrategia'].unique()

    # Dividir os gráficos em colunas
    col1, col2 = st.columns(2)

    for i, estrategia in enumerate(estrategias):
        estrategia_data = data[data['nomeEstrategia'] == estrategia]

        # Gerar gráfico para a estratégia
        grafico = px.line(
            estrategia_data,
            x="mes",
            y="valor",
            color="nomeEstrategia",
            title=estrategia,
            markers=True,
            labels={"mes": "Mês", "valor": "Valor"}
        )
        grafico.update_xaxes(categoryorder="array", categoryarray=["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"])

        # Exibir gráfico nas colunas alternadas
        if i % 2 == 0:
            with col1:
                st.plotly_chart(grafico, use_container_width=True)
        else:
            with col2:
                st.plotly_chart(grafico, use_container_width=True)

# Gerar gráficos para cada indicador
for indicador, descricao in indicadores.items():
    exibir_graficos_por_indicador(indicador, descricao)
