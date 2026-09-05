import urllib.parse
import streamlit as st

# Exemplo de número de WhatsApp (substitua pelo seu DDD e número, sem espaços ou símbolos)
numero_whatsapp = "5531989684010"

# Exibindo os produtos
for i, prod in enumerate(produtos_filtrados):
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

    # Codifica a mensagem para o formato de URL (substitui espaços por %20, etc.)
    mensagem_codificada = urllib.parse.quote(mensagem)

    # Cria o link do WhatsApp
    link_whatsapp = (
        f"https://wa.me/{numero_whatsapp}?text={mensagem_codificada}"
    )

    # Botão estilizado em HTML/Markdown abrindo em nova aba
    st.markdown(
        f"""
        <a href="{link_whatsapp}" target="_blank">
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
