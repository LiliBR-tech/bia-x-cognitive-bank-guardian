```python
import json
import os
from pathlib import Path

import pandas as pd
import requests
import streamlit as st


# ============================================================
# BIA-X — Cognitive Bank Guardian
# Banking Intelligence Assistant — Explainable Experience
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "gpt-oss"
)


# ============================================================
# Page configuration
# ============================================================

st.set_page_config(
    page_title="BIA-X",
    page_icon="B",
    layout="centered"
)


# ============================================================
# Knowledge Base
# ============================================================

@st.cache_data
def load_transactions():
    path = DATA_DIR / "transacoes.csv"

    if not path.exists():
        return pd.DataFrame()

    return pd.read_csv(path)


@st.cache_data
def load_service_history():
    path = DATA_DIR / "historico_atendimento.csv"

    if not path.exists():
        return pd.DataFrame()

    return pd.read_csv(path)


@st.cache_data
def load_customer_profile():
    path = DATA_DIR / "perfil_cliente.json"

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


@st.cache_data
def load_financial_products():
    path = DATA_DIR / "produtos_financeiros.json"

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# ============================================================
# Load knowledge base
# ============================================================

transactions = load_transactions()
service_history = load_service_history()
customer_profile = load_customer_profile()
financial_products = load_financial_products()


# ============================================================
# Knowledge context
# ============================================================

def build_context():
    context = {
        "perfil_cliente": customer_profile,
        "produtos_financeiros": financial_products,
        "historico_atendimento": service_history.to_dict(
            orient="records"
        ),
        "transacoes": transactions.to_dict(
            orient="records"
        )
    }

    return json.dumps(
        context,
        ensure_ascii=False,
        indent=2
    )


# ============================================================
# BIA-X system prompt
# ============================================================

SYSTEM_PROMPT = """
Você é o BIA-X — Banking Intelligence Assistant.

Você atua em um ambiente bancário exclusivamente simulado.

Seu objetivo é oferecer respostas úteis, contextuais, seguras e coerentes
com as informações disponíveis na base de conhecimento.

PRINCÍPIOS:

1. Utilize somente as informações disponíveis no contexto fornecido.

2. Nunca invente transações, valores, produtos, limites, dados pessoais,
   operações ou informações bancárias.

3. Se houver informação suficiente para responder, responda diretamente.

4. Se houver compreensão parcial da solicitação, utilize o contexto já
   disponível e faça uma pergunta objetiva para obter somente a informação
   necessária.

5. Evite responder simplesmente "não entendi" quando houver algum contexto
   útil disponível.

6. Se uma solicitação for ambígua, não escolha arbitrariamente uma
   interpretação. Explique brevemente a ambiguidade e solicite o dado mínimo
   necessário.

7. Se a informação solicitada não existir na base de conhecimento, informe
   claramente essa limitação.

8. Uma hipótese não deve ser apresentada como fato.

9. Uma informação não encontrada não deve ser apresentada como confirmada.

10. O ambiente é simulado. Não execute operações bancárias reais.

11. Nunca solicite senhas, tokens, códigos de autenticação ou credenciais.

12. Mantenha linguagem profissional, natural e objetiva.

13. Priorize a continuidade da conversa.

14. Quando não for possível responder com segurança, pergunte em vez de
    especular.

15. Diferencie claramente informação encontrada na base de conhecimento de
    qualquer interpretação necessária para responder.

PRINCÍPIO CENTRAL:

O BIA-X não precisa compreender tudo imediatamente para ser útil.

Ele deve reconhecer:
- o que já compreendeu;
- o que ainda falta;
- quando pode responder;
- quando precisa esclarecer;
- quando precisa reconhecer uma limitação.

Sempre priorize uma resposta útil sem ultrapassar os limites da evidência
disponível.
"""


# ============================================================
# Ollama
# ============================================================

def ask_ollama(user_message, conversation_history):
    context = build_context()

    messages = []

    messages.append({
        "role": "system",
        "content": SYSTEM_PROMPT
    })

    messages.append({
        "role": "system",
        "content": (
            "BASE DE CONHECIMENTO SIMULADA:\n\n"
            + context
        )
    })

    for message in conversation_history:
        messages.append(message)

    messages.append({
        "role": "user",
        "content": user_message
    })

    prompt = ""

    for message in messages:
        prompt += (
            f"{message['role'].upper()}:\n"
            f"{message['content']}\n\n"
        )

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return result.get(
        "response",
        "Não foi possível obter uma resposta do modelo."
    )


# ============================================================
# Session state
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# Interface
# ============================================================

st.title("BIA-X")

st.caption(
    "Banking Intelligence Assistant — Explainable Experience"
)

st.write(
    "Assistente bancário experimental para interação contextual "
    "em ambiente simulado."
)


with st.expander("Sobre o ambiente"):
    st.write(
        "O BIA-X utiliza dados sintéticos para demonstrar "
        "compreensão contextual, recuperação de conversa e "
        "respostas condicionadas às informações disponíveis."
    )

    st.write(
        "Nenhuma operação bancária real é executada."
    )


# ============================================================
# Conversation
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# User input
# ============================================================

user_message = st.chat_input(
    "Digite sua mensagem..."
)


if user_message:

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.markdown(user_message)

    try:

        with st.chat_message("assistant"):

            with st.spinner("Analisando contexto..."):

                response = ask_ollama(
                    user_message,
                    st.session_state.messages[:-1]
                )

            st.markdown(response)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    except requests.exceptions.ConnectionError:

        error_message = (
            "Não foi possível conectar ao serviço Ollama. "
            "Verifique se o Ollama está em execução e se o endpoint "
            f"está disponível em `{OLLAMA_URL}`."
        )

        with st.chat_message("assistant"):
            st.error(error_message)

    except requests.exceptions.Timeout:

        error_message = (
            "O modelo demorou mais do que o tempo limite configurado "
            "para responder."
        )

        with st.chat_message("assistant"):
            st.error(error_message)

    except requests.exceptions.HTTPError as error:

        error_message = (
            "O serviço do modelo retornou um erro HTTP: "
            f"{error}"
        )

        with st.chat_message("assistant"):
            st.error(error_message)

    except Exception as error:

        error_message = (
            "Ocorreu um erro durante o processamento da solicitação: "
            f"{error}"
        )

        with st.chat_message("assistant"):
            st.error(error_message)


# ============================================================
# Development information
# ============================================================

with st.sidebar:

    st.header("BIA-X")

    st.write(
        "Protótipo V1 — ambiente bancário simulado."
    )

    st.divider()

    st.subheader("Knowledge Base")

    st.write(
        f"Transações: {len(transactions)}"
    )

    st.write(
        f"Atendimentos: {len(service_history)}"
    )

    st.write(
        f"Produtos: {len(financial_products.get('produtos', []))}"
    )

    st.divider()

    st.caption(
        f"Modelo configurado: {OLLAMA_MODEL}"
    )
```
