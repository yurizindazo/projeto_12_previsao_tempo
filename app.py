import streamlit as st
from dados import previsao_temperatura

####Cidades
cidades = {
    "Santana de Parnaiba" : [-23.440663378456815, -46.919530686514285],
    "Madrid" : [40.41521683750571, -3.7015093061523094],
    "Barcelona" : [41.385584784900274, 2.1673115474380067],
    "Paris" : [48.85953036741794, 2.346294424022486],
    "Manchester" : [53.48235956251265, -2.244405537895169]
    }

st.sidebar.title("Previsão do tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude, longitude = cidades[cidade]

st.title(f"Previsão do tempo em {cidade} para os proximos 7 dias")
st.markdown("------")

dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data", f'{int(d['dia'])}/{int(d['mes'])}')
        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}º")
        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"
            elif d['temperatura_media'] < 18:
                temp = "cool.png"
            elif d['temperatura_media'] < 25:
                temp = "comfort.png"
            else:
                temp = "warn.png"

                st.image(temp, width=40)