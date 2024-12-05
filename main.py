import streamlit as st
from PIL import Image
import os

valor = '370.000'
endereco = "Ocian"
quartos = 2
vagas = 1
banheiros = 2
metragem = 76
IPTU = 283.00
condominio = 716.00

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("### Corretor Felipe Carlos")

st.divider()

col1_1, col2_1, col3_1 = st.columns([10, 0.1, 10], vertical_alignment="top")

with col1_1:
    st.text("Whatsapp: (13) 97424-2919")
    st.text("Telefone: (13) 99626-0027")

with col3_1:
    st.link_button(label='Entrar em contato', url='https://wa.me/5513974242919')

box_infos = st.container(border=True)

with box_infos:
    col4, col5, col6, col7 = st.columns([2, 1, 1, 1])

    with col4:
        st.markdown(f"### R${valor}")
        st.markdown(f"{endereco} - Praia Grande")
        st.text(fr"IPTU: R${IPTU:.2f} | COND: R${condominio:.2f}")

    with col6:
        dorms = "quarto"
        banheiro = "banheiro"
        vaga = "vaga"

        if quartos > 1:
            dorms = "quartos"
        if banheiros > 1:
            dorms = "banheiros"
        if vagas > 1:
            dorms = "vagas"

        st.markdown(f"🛏️ - {quartos} {dorms}")
        st.markdown(f"📐 - {metragem}m²")

    with col7:
        st.markdown(f"🚽 - {banheiros} {banheiro}")
        st.markdown(f"🚘 - {vagas} {vaga}")

caminho = "./midia"
imagens = os.listdir(caminho)

# Número de colunas
num_colunas = 2

# Criar colunas
colunas = st.columns(num_colunas)

# Distribuir imagens nas colunas
for i, caminho_imagem in enumerate(imagens):
    with colunas[i % num_colunas]:
        img = Image.open(f"./midia/{caminho_imagem}")
        st.image(img, caption=f"Imagem {i + 1}", use_container_width=True)
