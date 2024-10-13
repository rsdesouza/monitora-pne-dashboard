import streamlit as st
import plotly.express as px
from st_files_connection import FilesConnection

def main():
    # Configurar o layout da página
    st.set_page_config(layout="wide")

    st.title("Acompanhamento de Estratégias - Meta 15 do PNE")

    # Conectar ao Google Cloud Storage (GCS) e ler o arquivo CSV
    conn = st.connection('gcs', type=FilesConnection)

    # Especificar o caminho do arquivo no bucket do GCS
    df = conn.read("monitora_pne_15_streamlit/estrategias.csv", input_format="csv", ttl=600, sep=";", decimal=",")

    # Exibir os gráficos e indicadores
    st.markdown("## Gráficos de acompanhamento das estratégias aplicadas aos indicadores da meta 15 do PNE.")

    # Gráfico para Indicador 15A
    multi_15A = '''**INDICADOR 15A** - Proporção de docências da educação infantil com professores cuja formação superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi_15A)

    # Consulta e gráficos do Indicador 15A
    consulta_plano_estrategico = df[df['nomeEstrategia'] == 'Plano estrategico conjunto para diagnosticos e formacao']
    consulta_financiamento_estudantil = df[df['nomeEstrategia'] == 'Consolidar financiamento estudantil']

    grafico_plano_estrategico = px.line(consulta_plano_estrategico, x='mes', y='valor', color='nomeEstrategia', title='Plano estratégico conjunto para diagnósticos e formação')
    grafico_financiamento_estudantil = px.line(consulta_financiamento_estudantil, x='mes', y='valor', color='nomeEstrategia', title='Consolidar financiamento estudantil')

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_plano_estrategico)
    with col2:
        st.plotly_chart(grafico_financiamento_estudantil)

    # Gráfico para Indicador 15B
    multi_15B = '''**INDICADOR 15B** - Proporção de docências dos anos iniciais do ensino fundamental com professores cuja formação
    superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi_15B)

    # Consulta e gráficos do Indicador 15B
    consulta_iniciacao_docencia = df[df['nomeEstrategia'] == 'Ampliar programa de iniciacao a docencia']
    consulta_plataforma_digital = df[df['nomeEstrategia'] == 'Expandir plataforma digital de matriculas']

    grafico_iniciacao_docencia = px.line(consulta_iniciacao_docencia, x='mes', y='valor', color='nomeEstrategia', title='Ampliar programa de iniciação à docência')
    grafico_plataforma_digital = px.line(consulta_plataforma_digital, x='mes', y='valor', color='nomeEstrategia', title='Expandir plataforma digital de matrículas')

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_iniciacao_docencia)
    with col2:
        st.plotly_chart(grafico_plataforma_digital)

    # Gráfico para Indicador 15C
    multi_15C = '''**INDICADOR 15C** - Proporção de docências dos anos finais do ensino fundamental com professores cuja formação
    superior está adequada à área de conhecimento que lecionam.'''
    st.markdown(multi_15C)

    # Consulta e gráficos do Indicador 15C
    consulta_formacao_especiais = df[df['nomeEstrategia'] == 'Programas de formacao para areas especiais']
    consulta_reforma_curricular = df[df['nomeEstrategia'] == 'Reforma curricular dos cursos de licenciatura']

    grafico_formacao_especiais = px.line(consulta_formacao_especiais, x='mes', y='valor', color='nomeEstrategia', title='Programas de formação para áreas especiais')
    grafico_reforma_curricular = px.line(consulta_reforma_curricular, x='mes', y='valor', color='nomeEstrategia', title='Reforma curricular dos cursos de licenciatura')

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_formacao_especiais)
    with col2:
        st.plotly_chart(grafico_reforma_curricular)

    # Gráfico para Indicador 15D
    multi_15D = '''**INDICADOR 15D** - Proporção de docências do ensino médio com professores cuja formação superior está adequada
    à área de conhecimento que lecionam.'''
    st.markdown(multi_15D)

    # Consulta e gráficos do Indicador 15D
    consulta_praticas_ensino = df[df['nomeEstrategia'] == 'valorizar as praticas de ensino e os estagios']
    consulta_cursos_programas_especiais = df[df['nomeEstrategia'] == 'Implementar cursos e programas especiais para formacao de docentes']

    grafico_praticas_ensino = px.line(consulta_praticas_ensino, x='mes', y='valor', color='nomeEstrategia', title='Valorizar as práticas de ensino e os estágios')
    grafico_cursos_programas_especiais = px.line(consulta_cursos_programas_especiais, x='mes', y='valor', color='nomeEstrategia', title='Implementar cursos e programas especiais para formação de docentes')

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(grafico_praticas_ensino)
    with col2:
        st.plotly_chart(grafico_cursos_programas_especiais)

if __name__ == "__main__":
    main()
