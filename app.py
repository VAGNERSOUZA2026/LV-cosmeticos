import streamlit as st

# Configuração da página
st.set_page_config(page_title="Catálogo de Cosméticos", page_icon="💄", layout="wide")

st.title("🛍️ Catálogo de Cosméticos - Natura, Boticário e Avon")
st.write("Encontre os melhores produtos de beleza em um só lugar!")

# Menu lateral para escolher a marca
st.sidebar.header("Filtros")
marca_selecionada = st.sidebar.selectbox(
    "Escolha a Marca:",
    ["Todas", "Natura", "Boticário", "Avon"]
)

# Simulando uma base de dados de produtos
produtos = [
    {"nome": "Perfume Kaiak", "marca": "Natura", "preco": "R$ 120,00", "tipo": "Perfumaria"},
    {"nome": "Hidratante Tododia", "marca": "Natura", "preco": "R$ 55,00", "tipo": "Corpo"},
    {"nome": "Perfume Egeo", "marca": "Boticário", "preco": "R$ 130,00", "tipo": "Perfumaria"},
    {"nome": "Creme Lily", "marca": "Boticário", "preco": "R$ 95,00", "tipo": "Corpo"},
    {"nome": "Batom Matte Avon", "marca": "Avon", "preco": "R$ 30,00", "tipo": "Maquiagem"},
    {"nome": "Máscara de Cílios Super Shock", "marca": "Avon", "preco": "R$ 40,00", "tipo": "Maquiagem"},
]

# Filtrando os produtos conforme a escolha do usuário
if marca_selecionada != "Todas":
    produtos_filtrados = [p for p in produtos if p["marca"] == marca_selecionada]
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
        st.button(f"Comprar {prod['nome']}", key=f"btn_{i}")
        st.markdown("---")
