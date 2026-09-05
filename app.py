import urllib.parse
import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="L&V Cosméticos", page_icon="💄", layout="centered"
)

# Estilização visual (Estilo App Mobile)
st.markdown(
    """
    <style>
    .stApp { background-color: #f8f9fa; }
    .produto-card {
        background-color: #ffffff;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 16px;
        border: 1px solid #eaeaea;
    }
    .produto-titulo { font-size: 16px; font-weight: bold; color: #333333; margin-bottom: 4px; }
    .produto-detalhe { font-size: 13px; color: #666666; margin-bottom: 2px; }
    .produto-preco { font-size: 16px; font-weight: bold; color: #d63384; margin-bottom: 12px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Configurações básicas
numero_whatsapp = "5531999999999"  # Coloque seu número com DDD
chave_pix = (
    "sua-chave-pix-aqui@email.com"  # Coloque sua Chave PIX (CPF, CNPJ, E-mail, Celular)
)

# 1. SISTEMA DE LOGIN SIMPLES
if "logged_in" not in st.session_state:
  st.session_state.logged_in = False

if not st.session_state.logged_in:
  st.markdown(
      "<h2 style='text-align: center; color: #d63384;'>💄 L&V Cosméticos - Entrar</h2>",
      unsafe_allow_html=True,
  )
  with st.form("login_form"):
    nome_usuario = st.text_input("Seu Nome:")
    telefone_usuario = st.text_input("Seu Telefone/WhatsApp:")
    submitted = st.form_submit_button("Acessar Aplicativo")

    if submitted:
      if nome_usuario and telefone_usuario:
        st.session_state.logged_in = True
        st.session_state.user_name = nome_usuario
        st.session_state.user_phone = telefone_usuario
        st.rerun()
      else:
        st.warning("Por favor, preencha seu nome e telefone para continuar.")
  st.stop()  # Para a execução aqui até o usuário fazer o login

# --- APLICATIVO PRINCIPAL APÓS O LOGIN ---
st.markdown(
    f"<h3 style='text-align: center; color: #d63384;'>Olá, {st.session_state.user_name}! ✨</h3>",
    unsafe_allow_html=True,
)

# Abas de navegação do App
aba1, aba2, aba3, aba4 = st.tabs(
    ["🛍️ Catálogo", "🔍 Buscar por Código", "📖 Revistas Online", "💳 Pagamento PIX"]
)

# Base de produtos simulada (Pode ser substituída por uma planilha Excel)
produtos = [
    {
        "codigo": "NAT01",
        "nome": "Perfume Kaiak",
        "marca": "Natura",
        "preco": "R$ 120,00",
        "imagem": "https://images.unsplash.com/photo-1523293182086-7651a899d37f?w=300",
    },
    {
        "codigo": "BOT02",
        "nome": "Perfume Egeo",
        "marca": "Boticário",
        "preco": "R$ 130,00",
        "imagem": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=300",
    },
    {
        "codigo": "AVO03",
        "nome": "Batom Matte Avon",
        "marca": "Avon",
        "preco": "R$ 30,00",
        "imagem": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=300",
    },
]

# --- ABA 1: CATÁLOGO GERAL ---
with aba1:
  st.subheader("Catálogo de Produtos")
  marca_selecionada = st.selectbox(
      "Filtrar por Marca:", ["Todas", "Natura", "Boticário", "Avon"]
  )

  produtos_filtrados = (
      [p for p in produtos if p["marca"] == marca_selecionada]
      if marca_selecionada != "Todas"
      else produtos
  )

  for prod in produtos_filtrados:
    mensagem = f"Olá! Sou {st.session_state.user_name}. Gostaria de comprar o produto: {prod['nome']} (Cód: {prod['codigo']}) por {prod['preco']}."
    link_whatsapp = (
        f"https://wa.me/{numero_whatsapp}?text="
        + urllib.parse.quote(mensagem)
    )

    st.markdown(
        f"""
        <div class="produto-card">
            <img src="{prod['imagem']}" style="width: 100%; height: 160px; object-fit: cover; border-radius: 10px; margin-bottom: 8px;">
            <div class="produto-titulo">{prod['nome']} (Cód: {prod['codigo']})</div>
            <div class="produto-detalhe"><b>Marca:</b> {prod['marca']}</div>
            <div class="produto-preco">{prod['preco']}</div>
            <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
                <button style='background-color: #25D366; color: white; padding: 10px; border: none; border-radius: 8px; width: 100%; font-weight: bold;'>💬 Pedir no WhatsApp</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- ABA 2: BUSCA POR NOME OU CÓDIGO (Ideal para planilhas) ---
with aba2:
  st.subheader("Busca rápida na Revista")
  st.write(
      "Digite o nome ou o código do produto que você viu na revista impressa ou"
      " digital:"
  )

  termo_busca = st.text_input("Digite o nome ou código (ex: NAT01 ou Kaiak):")

  if termo_busca:
    resultado = [
        p
        for p in produtos
        if termo_busca.lower() in p["nome"].lower()
        or termo_busca.lower() in p["codigo"].lower()
    ]
    if resultado:
      for prod in resultado:
        st.success(
            f"Encontrado: **{prod['nome']}** (Cód: {prod['codigo']}) - Marca:"
            f" {prod['marca']} - Preço: **{prod['preco']}**"
        )
    else:
      st.warning(
          "Produto não encontrado com esse termo. Tente anotar o código exato"
          " da revista!"
      )

# --- ABA 3: LINKS DAS REVISTAS ONLINE ---
with aba3:
  st.subheader("📖 Revistas Digitais das Marcas")
  st.write(
      "Folheie a revista oficial, escolha seus produtos, anote o **código** e"
      " faça a busca na aba ao lado!"
  )

  st.markdown(
      "👉 [Acessar Revista Digital Natura](https://www.natura.com.br)"
  )
  st.markdown("👉 [Acessar Revista Digital Boticário](https://www.boticario.com.br)")
  st.markdown("👉 [Acessar Revista Digital Avon](https://www.avon.com.br)")

# --- ABA 4: PAGAMENTO VIA PIX ---
with aba4:
  st.subheader("💳 Pagamento via PIX")
  st.write("Realize o pagamento e envie o comprovante pelo WhatsApp.")
  st.info(f"**Chave PIX:** `{chave_pix}`")
  st.write(
      "Após realizar a transferência, clique no botão abaixo para enviar o"
      " comprovante direto para o nosso atendimento:"
  )

  msg_pix = f"Olá, aqui está o meu comprovante de pagamento via PIX. Meu nome é {st.session_state.user_name}."
  link_pix_wpp = (
      f"https://wa.me/{numero_whatsapp}?text=" + urllib.parse.quote(msg_pix)
  )

  st.markdown(
      f"""
      <a href="{link_pix_wpp}" target="_blank" style="text-decoration: none;">
          <button style='background-color: #0088cc; color: white; padding: 12px; border: none; border-radius: 8px; width: 100%; font-weight: bold;'>📤 Enviar Comprovante no WhatsApp</button>
      </a>
      """,
      unsafe_allow_html=True,
  )
