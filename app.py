import urllib.parse
import streamlit as st

# Configuração da página (otimizada para visual mobile)
st.set_page_config(
    page_title="L&V Cosméticos", page_icon="💄", layout="centered"
)

# Estilização CSS para dar cara de App Mobile
st.markdown(
    """
    <style>
    /* Fundo geral e fonte */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Estilo dos cards de produtos */
    .produto-card {
        background-color: #ffffff;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 16px;
        border: 1px solid #eaeaea;
    }
    
    /* Título do produto no card */
    .produto-titulo {
        font-size: 18px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 4px;
    }
    
    /* Detalhes do produto */
    .produto-detalhe {
        font-size: 14px;
        color: #666666;
        margin-bottom: 2px;
    }
    
    /* Preço destacado */
    .produto-preco {
        font-size: 18px;
        font-weight: bold;
        color: #d63384;
        margin-bottom: 12px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Cabeçalho estilo App
st.markdown(
    "<h2 style='text-align: center; color: #d63384;'>💄 L&V Cosméticos</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Natura • Boticário • Avon</p>",
    unsafe_allow_html=True,
)

# Número do WhatsApp para onde os pedidos vão
numero_whatsapp = "5531999999999"  # Substitua pelo seu número

# Filtros em formato limpo
marca_selecionada = st.selectbox(
    "Filtrar por Marca:", ["Todas", "Natura", "Boticário", "Avon"]
)

st.markdown("---")

# Base de produtos simulada
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

# Filtrando os produtos
if marca_selecionada != "Todas":
  produtos_filtrados = [
      p for p in produtos if p["marca"] == marca_selecionada
  ]
else:
  produtos_filtrados = produtos

# Exibindo os produtos em formato de "Cards" estilo mobile
for i, prod in enumerate(produtos_filtrados):
  mensagem = (
      f"Olá! Gostaria de comprar o produto: {prod['nome']} ({prod['marca']}) por"
      f" {prod['preco']}."
  )
  mensagem_codificada = urllib.parse.quote(mensagem)
  link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem_codificada}"

  # Estrutura visual em cartão
  st.markdown(
      f"""
        <div class="produto-card">
            <div class="produto-titulo">{prod['nome']}</div>
            <div class="produto-detalhe"><b>Marca:</b> {prod['marca']} | <b>Categoria:</b> {prod['tipo']}</div>
            <div class="produto-preco">{prod['preco']}</div>
            <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
                <button style='
                    background-color: #25D366; 
                    color: white; 
                    padding: 10px 15px; 
                    border: none; 
                    border-radius: 8px; 
                    cursor: pointer; 
                    font-weight: bold;
                    width: 100%;
                    font-size: 14px;'>
                    💬 Comprar pelo WhatsApp
                </button>
            </a>
        </div>
    """,
      unsafe_allow_html=True,
  )
