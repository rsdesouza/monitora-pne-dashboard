import streamlit as st
import plotly.express as px
from st_files_connection import FilesConnection

def main():
    # Configurar o layout da página
    st.set_page_config(layout="wide")

    # Conectar ao Google Cloud Storage (GCS) e ler o arquivo CSV
    conn = st.connection('gcs', type=FilesConnection)

    # Especificar o caminho do arquivo no bucket do GCS
    df = conn.read("monitora_pne_15_streamlit/estrategias.csv", input_format="csv", ttl=600, sep=";", decimal=",")

    # Converter valores e meses para garantir ordenação correta
    df["mes"] = pd.Categorical(
        df["mes"],
        categories=["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
        ordered=True
    )
    df = df.sort_values(["indicador", "mes"])

    # Calcular o total por indicador e o percentual acumulado por mês
    df["total_por_indicador"] = df.groupby("indicador")["valor"].transform("sum")
    df["percentual"] = (df["valor"] / df["total_por_indicador"]) * 100

    # Agrupar os dados por indicador
    grouped = df.groupby("indicador")

    # Gerar gráficos dinamicamente para cada indicador
    for indicador, data in grouped:
        # Cabeçalho para cada indicador
        st.markdown(f"### **Indicador {indicador.upper()}**")
        st.markdown(f"Proporção de docências com professores cuja formação superior está adequada para o {indicador}.")

        # Dividir os gráficos em colunas
        col1, col2 = st.columns(2)

        # Obter estratégias únicas dentro do indicador
        estrategias = data["nomeEstrategia"].unique()

        # Gráfico percentual acumulado
        grafico_percentual = px.line(
            data,
            x="mes",
            y="percentual",
            color="nomeEstrategia",
            title=f"Percentual de Progresso - Indicador {indicador}",
            markers=True
        )
        with st.expander(f"Gráfico Percentual do {indicador}", expanded=True):
            st.plotly_chart(grafico_percentual, use_container_width=True)

        # Gerar gráficos para cada estratégia
        for i, estrategia in enumerate(estrategias):
            estrategia_data = data[data["nomeEstrategia"] == estrategia]
            grafico = px.line(
                estrategia_data,
                x="mes",
                y="valor",
                title=f"{estrategia}",
                markers=True
            )

            # Mostrar os gráficos em colunas alternadas
            if i % 2 == 0:
                with col1:
                    st.plotly_chart(grafico, use_container_width=True)
            else:
                with col2:
                    st.plotly_chart(grafico, use_container_width=True)

if __name__ == "__main__":
    main()
