import streamlit as st
import plotly.express as px
import pandas as pd
from st_files_connection import FilesConnection

def main():
    # Configurar o layout da página
    st.set_page_config(layout="wide")

    # Conectar ao Google Cloud Storage (GCS) e ler o arquivo CSV
    conn = st.connection('gcs', type=FilesConnection)

    # Especificar o caminho do arquivo no bucket do GCS
    df = conn.read("monitora_pne_15_streamlit/estrategias.csv", input_format="csv", ttl=600, sep=";", decimal=",")

    # Ordenar os meses corretamente
    df['mes'] = pd.Categorical(
        df['mes'],
        categories=["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
        ordered=True
    )
    df = df.sort_values(by=["ano", "mes"])  # Ordenar por ano e mês

    # Criar uma função para exibir gráficos por indicador
    def exibir_graficos(indicador, descricao):
        st.markdown(descricao)

        # Filtrar os dados pelo indicador
        dados_indicador = df[df["indicador"] == indicador]
        estrategias = dados_indicador["nomeEstrategia"].unique()

        # Dividir os gráficos em colunas para visualização
        col1, col2 = st.columns(2)

        for i, estrategia in enumerate(estrategias):
            dados_estrategia = dados_indicador[dados_indicador["nomeEstrategia"] == estrategia]

            # Criar gráfico para a estratégia
            grafico = px.line(
                dados_estrategia,
                x="mes",
                y="valor",
                title=f"Estratégia: {estrategia}",
                markers=True,
                labels={"mes": "Mês", "valor": "Valor"},
                color="ano"
            )
            grafico.update_xaxes(categoryorder="array", categoryarray=["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"])

            # Exibir os gráficos em colunas alternadas
            if i % 2 == 0:
                with col1:
                    st.plotly_chart(grafico, use_container_width=True)
            else:
                with col2:
                    st.plotly_chart(grafico, use_container_width=True)

    # Indicadores e suas descrições
    indicadores = {
        "indicador1": "**INDICADOR 15A** - Proporção de docências da educação infantil com professores cuja formação superior está adequada à área de conhecimento que lecionam.",
        "indicador2": "**INDICADOR 15B** - Proporção de docências dos anos iniciais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.",
        "indicador3": "**INDICADOR 15C** - Proporção de docências dos anos finais do ensino fundamental com professores cuja formação superior está adequada à área de conhecimento que lecionam.",
        "indicador4": "**INDICADOR 15D** - Proporção de docências do ensino médio com professores cuja formação superior está adequada à área de conhecimento que lecionam."
    }

    # Exibir gráficos para cada indicador
    for indicador, descricao in indicadores.items():
        exibir_graficos(indicador, descricao)

if __name__ == "__main__":
    main()
