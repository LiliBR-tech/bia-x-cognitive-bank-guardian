# BIA-X — Cognitive Bank Guardian

**Banking Intelligence Assistant — Explainable Experience**

> **Laboratório:** Bank Cognitive Immune Lab
>
> 
> **Conceito:** Cognitive Bank Guardian
>
> 
> **Versão:** V1 — DIO Lab
>
> 
> **Status:** Em desenvolvimento

---

## 1. Visão Geral

O **BIA-X (Banking Intelligence Assistant — Explainable Experience)** é um protótipo de assistente virtual baseado em Inteligência Artificial Generativa para o contexto bancário.

Seu objetivo é auxiliar uma pessoa usuária na compreensão e resolução de necessidades relacionadas a informações financeiras disponíveis em uma base de conhecimento controlada.

O diferencial do BIA-X está na forma como trata situações nas quais a mensagem inicial não contém informação suficiente para determinar completamente a intenção da pessoa usuária.

Em vez de simplesmente abandonar a interação ou assumir uma intenção sem evidências suficientes, o BIA-X busca:

1. identificar o que já pode ser compreendido;
2. utilizar o contexto disponível;
3. identificar informações ausentes;
4. solicitar o menor esclarecimento necessário;
5. continuar a conversa com o novo contexto;
6. responder de forma coerente com as informações disponíveis.

O projeto utiliza dados mockados e não realiza operações bancárias reais.

---

## 2. Problema

Assistentes conversacionais podem receber mensagens curtas, incompletas ou ambíguas.

Uma mensagem como:

> "Quero ver meu negócio."

não necessariamente fornece contexto suficiente para determinar qual informação a pessoa deseja consultar.

Diante desse tipo de situação, existem dois comportamentos problemáticos:

* interromper a conversa imediatamente com uma resposta genérica de incompreensão;
* assumir uma intenção que não foi suficientemente indicada pela mensagem.

O BIA-X explora uma terceira abordagem: **compreensão progressiva**.

A ideia é utilizar aquilo que já pode ser compreendido, identificar a informação necessária para reduzir a ambiguidade e conduzir a conversa até uma resposta mais adequada.

---

## 3. Objetivo

O objetivo do BIA-X é demonstrar como um assistente virtual pode utilizar Inteligência Artificial Generativa, contexto conversacional e uma base de conhecimento para auxiliar uma pessoa usuária de forma:

* clara;
* contextual;
* segura;
* coerente;
* transparente quanto às suas limitações.

O agente não precisa assumir certeza quando a informação disponível não permite uma conclusão segura.

Seu comportamento deve priorizar a utilização das informações disponíveis e o esclarecimento das informações ausentes.

---

## 4. Caso de Uso

### Assistente conversacional para apoio em consultas bancárias simuladas

O BIA-X será utilizado em um cenário bancário simulado no qual a pessoa usuária pode consultar informações presentes na base de conhecimento.

Entre os possíveis tipos de interação estão:

* consulta de transações;
* compreensão de gastos;
* consulta de informações sobre produtos financeiros disponíveis na base;
* recuperação de contexto de atendimentos anteriores;
* esclarecimento de informações;
* consultas que não possuem dados suficientes;
* perguntas fora do escopo do agente.

A aplicação não acessa contas bancárias reais e não executa operações financeiras.

---

## 5. Público-alvo

O protótipo é direcionado a pessoas que utilizam serviços bancários e precisam consultar ou compreender informações financeiras disponíveis em um ambiente conversacional.

O foco do projeto não é substituir profissionais financeiros nem executar decisões financeiras em nome da pessoa usuária.

O foco é demonstrar uma experiência conversacional capaz de utilizar contexto e informação disponível para auxiliar a pessoa na próxima etapa da interação.

---

## 6. Persona do Agente

### BIA-X

A BIA-X possui uma personalidade:

* clara;
* objetiva;
* contextual;
* investigativa;
* transparente;
* não presunçosa.

O agente deve evitar demonstrar uma certeza que não esteja sustentada pelas informações disponíveis.

### Princípio comportamental

> **Se houver informação suficiente, responda.
> Se houver informação parcial, aproveite o que já pode ser compreendido e esclareça o necessário.
> Se não houver informação suficiente, informe a limitação.**

---

## 7. Tom de Voz

O BIA-X utiliza um tom:

**profissional, claro, humano e objetivo.**

A comunicação deve evitar:

* excesso de jargão técnico;
* respostas desnecessariamente longas;
* falsa certeza;
* afirmações sem suporte na base de conhecimento;
* respostas genéricas que encerrem a conversa sem orientar a pessoa usuária.

Quando precisar solicitar esclarecimento, o agente deve explicar de forma simples o que precisa saber para continuar.

---

## 8. Comportamento Esperado

O comportamento do BIA-X pode ser representado pelo seguinte fluxo:

```text
Mensagem da pessoa usuária
          |
          v
Identificação da intenção
          |
          v
Existe informação suficiente?
      /           \
    SIM            NÃO
     |              |
     v              v
  Responder    Existe compreensão parcial?
                  /          \
                SIM           NÃO
                 |             |
                 v             v
       Identificar ausência   Solicitar
       de informação          contexto
                 |
                 v
       Pergunta de esclarecimento
                 |
                 v
          Novo contexto
                 |
                 v
              Resposta
```

O objetivo desse fluxo não é criar um sistema complexo de classificação, mas estabelecer um comportamento verificável para o agente.

---

## 9. Compreensão Progressiva

A compreensão progressiva é o principal diferencial experimental do BIA-X.

O agente deve distinguir entre:

### Compreensão suficiente

Quando a mensagem contém informações suficientes para responder utilizando a base de conhecimento.

### Compreensão parcial

Quando existe uma intenção provável ou um contexto útil, mas ainda falta uma informação específica.

Nesse caso, o agente deve procurar uma pergunta de esclarecimento que reduza a ambiguidade.

### Ausência de informação

Quando a base de conhecimento não possui dados suficientes para responder.

Nesse caso, o agente deve declarar a limitação em vez de criar uma resposta.

---

## 10. Minimum Useful Response

Como parte do laboratório, o BIA-X adota o conceito de **Minimum Useful Response**.

Uma resposta de esclarecimento não deve ser apenas:

> "Não entendi."

Sempre que possível, ela deve utilizar o contexto disponível para indicar como a conversa pode prosseguir.

Exemplo:

> "Posso ajudar. Quando você diz 'meu negócio', você quer consultar uma transação, um produto financeiro ou outra informação da sua conta?"

O objetivo é transformar uma situação de incompreensão em uma oportunidade de recuperação da conversa.

---

## 11. Conversation Recovery

O BIA-X também será avaliado quanto à sua capacidade de recuperar uma conversa quando a primeira mensagem não for suficientemente clara.

O conceito de **Conversation Recovery** representa a capacidade de:

1. reconhecer a ambiguidade;
2. evitar uma suposição indevida;
3. solicitar informação relevante;
4. incorporar o novo contexto;
5. continuar a interação.

Essa característica pertence ao **LAB BIA-X** e representa uma extensão experimental dos requisitos básicos do desafio.

---

## 12. Arquitetura

A arquitetura inicial será deliberadamente simples:

```text
┌──────────────────────┐
│        USUÁRIO       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│        BIA-X         │
│                      │
│ Intenção             │
│ Contexto             │
│ Ambiguidade          │
│ Guardrails           │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ BASE DE CONHECIMENTO │
│                      │
│ Dados mockados       │
│ Transações           │
│ Histórico            │
│ Perfil / produtos    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│         LLM          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ RESPOSTA             │
│ ou                   │
│ ESCLARECIMENTO       │
└──────────────────────┘
```

A implementação poderá utilizar uma interface simples e uma LLM via API ou modelo local. O desafio oficialmente permite essas alternativas e sugere ferramentas como Streamlit, Gradio, Ollama e diferentes provedores de LLM.

---

## 13. Base de Conhecimento

A base de conhecimento será composta por dados simulados relacionados ao cenário bancário.

O repositório oficial fornece como referência dados de:

* transações;
* histórico de atendimento;
* perfil do cliente;
* produtos financeiros.

O desafio permite adaptar ou expandir esses dados conforme o caso de uso.

Para o BIA-X, esses dados serão utilizados para criar contexto suficiente para testar tanto respostas diretas quanto situações de informação incompleta.

Não serão utilizados dados bancários reais.

---

## 14. Segurança e Anti-alucinação

O BIA-X deverá seguir as seguintes regras:

1. Não inventar informações.
2. Não apresentar uma suposição como fato.
3. Não preencher informações ausentes por inferência não sustentada.
4. Utilizar a base de conhecimento como fonte contextual.
5. Informar quando não houver dados suficientes.
6. Solicitar esclarecimento quando necessário.
7. Não executar operações financeiras reais.
8. Utilizar dados simulados durante o protótipo.
9. Não expor informações que não sejam necessárias para a resposta.
10. Manter claras as limitações do agente.

A segurança e o controle de alucinações fazem parte explicitamente da documentação exigida pelo desafio.

---

## 15. Limitações

O BIA-X é um protótipo educacional.

Portanto:

* não acessa contas bancárias reais;
* não executa transferências;
* não autoriza transações;
* não bloqueia ou desbloqueia produtos;
* não substitui atendimento bancário;
* não substitui aconselhamento financeiro profissional;
* não deve ser utilizado para tomar decisões financeiras reais;
* suas respostas dependem das informações disponíveis na base de conhecimento e das capacidades da LLM utilizada.

---

## 16. Diferencial do BIA-X

O diferencial experimental do BIA-X é a **gestão da incerteza conversacional**.

O projeto não considera que uma conversa possui apenas dois estados:

```text
ENTENDEU
ou
NÃO ENTENDEU
```

O BIA-X trabalha com pelo menos três estados:

```text
ENTENDIMENTO SUFICIENTE
        ↓
      RESPONDER

ENTENDIMENTO PARCIAL
        ↓
   ESCLARECER

INFORMAÇÃO INSUFICIENTE
        ↓
   DECLARAR LIMITE
```

Essa abordagem será testada experimentalmente por meio de cenários de avaliação.

---

## 17. Princípio Central

> **O BIA-X não precisa compreender tudo de imediato para ser útil; precisa reconhecer o que já compreendeu, identificar o que falta e conduzir a conversa até uma resposta segura.**

---

## 18. Relação com o Cognitive Bank Guardian

O **Cognitive Bank Guardian** representa o conceito cognitivo que orienta a evolução do laboratório.

Nesta primeira versão, o BIA-X concentra-se na experiência conversacional.

Uma evolução futura poderá explorar capacidades internas de análise orientada por evidências, investigação, explicabilidade e correlação de eventos.

Essas capacidades não fazem parte do escopo necessário para a primeira versão funcional deste Lab.

---

## 19. Escopo da V1

### Incluído

* assistente conversacional;
* base de conhecimento simulada;
* integração com LLM;
* contexto;
* tratamento de ambiguidade;
* esclarecimento;
* respostas fundamentadas na informação disponível;
* proteção contra respostas inventadas;
* testes estruturados;
* avaliação de qualidade.

### Fora do escopo

* dados bancários reais;
* execução de transações;
* sistemas bancários reais;
* multiagentes;
* fine-tuning;
* infraestrutura bancária;
* investigação automatizada de fraude;
* análise operacional de segurança;
* arquitetura avançada de RAG.

---

## 20. Evolução planejada

O conceito **Cognitive Bank Guardian** poderá futuramente incorporar uma camada interna de análise orientada por evidências, separada da experiência conversacional do cliente.

Essa evolução poderá explorar:

```text
Evidence
   ↓
Context
   ↓
Reasoning
   ↓
Investigation
```

Entretanto, essa camada permanece fora do escopo da V1 para preservar a simplicidade, funcionalidade e clareza exigidas pelo desafio.
