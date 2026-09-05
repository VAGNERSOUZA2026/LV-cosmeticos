import urllib.parse
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Catálogo de Cosméticos", page_icon="💄", layout="wide"
)

st.title("🛍️ Catálogo de Cosméticos - Natura, Boticário e Avon")
st.write("Encontre os melhores produtos de beleza em um só lugar!")

# SEU NÚMERO DO WHATSAPP (Coloque seu código do país + DDD + número, sem espaços ou símbolos)
# Exemplo para Belo Horizonte/MG: "5531988887777"
numero_whatsapp = "5531999999999"

# Menu lateral para escolher a marca
st.sidebar.header("Filtros")
marca_selecionada = st.sidebar.selectbox(
    "Escolha a Marca:", ["Todas", "Natura", "Boticário", "Avon"]
)

# Simulando uma base de dados de produtos
produtos = [
    {
        "nome": "Perfume Kaiak",
        "marca": "Natura",
        "preco": "R$ 120,00",
        "tipo": "Perfumaria",
    },
    {
        "nome": "Hidratante Tododia",
        "marca": "Natura",
        "preco": "R$ 55,00",
        "tipo": "Corpo",
    },
    {
        "nome": "Perfume Egeo",
        "marca": "Boticário",
        "preco": "R$ 130,00",
        "tipo": "Perfumaria",
    },
    {
        "nome": "Creme Lily",
        "marca": "Boticário",
        "preco": "R$ 95,00",
        "tipo": "Corpo",
    },
    {
        "nome": "Batom Matte Avon",
        "marca": "Avon",
        "preco": "R$ 30,00",
        "tipo": "Maquiagem",
    },
    {
        "nome": "Máscara de Cílios Super Shock",
        "marca": "Avon",
        "preco": "R$ 40,00",
        "tipo": "Maquiagem",
    },
]

# Filtrando os produtos conforme a escolha do usuário
if marca_selecionada != "Todas":
  produtos_filtrados = [
      p for p in produtos if p["marca"] == marca_selecionada
  ]
else:
  produtos_filtrados = produtos

# Exibindo os produtos em colunas na tela
col1, col2 = st.columns(2)

for i, prod in enumerate(produtos_filtrados):
  # Alterna entre as colunas para organizar o layout
  with col1 if i % 2 == 0 else col2:
    st.subheader(prod["nome"])
    st.write(f"**Marca:** {prod['marca']}")
    st.write(f"**Categoria:** {prod['tipo']}")
    st.write(f"**Preço:** {prod['preco']}")

    # Mensagem que vai chegar para você no WhatsApp
    mensagem = (
        f"Olá! Gostaria de comprar o produto: {prod['nome']} ({prod['marca']})"
        f" por {prod['preco']}."
    )

    # Codifica a mensagem para o formato de URL
    mensagem_codificada = urllib.parse.quote(mensagem)

    # Cria o link do WhatsApp
    link_whatsapp = (
        f"https://wa.me/{numero_whatsapp}?text={mensagem_codificada}"
    )

    # Botão estilizado do WhatsApp
    st.markdown(
        f"""
        <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
            <button style='
                background-color: #25D366; 
                color: white; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 5px; 
                cursor: pointer; 
                font-weight: bold;
                width: 100%;'>
                💬 Pedir no WhatsApp
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
