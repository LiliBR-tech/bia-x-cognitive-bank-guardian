# BIA-X — Arquitetura

## 1. Objetivo

Este documento descreve a arquitetura do **BIA-X — Cognitive Bank Guardian**, um assistente virtual desenvolvido para um ambiente bancário simulado.

A arquitetura foi definida a partir dos requisitos estabelecidos na documentação do agente, da base de conhecimento e da estratégia de prompts.

O objetivo é manter uma estrutura simples o suficiente para um protótipo funcional, mas organizada para permitir evolução posterior.

---

## 2. Visão geral

O BIA-X é organizado em camadas responsáveis por:

1. interação com o usuário;
2. processamento da solicitação;
3. aplicação das regras do agente;
4. acesso ao contexto disponível;
5. geração da resposta;
6. avaliação do comportamento.

Fluxo conceitual:

```text
                    ┌─────────────────────┐
                    │       Usuário       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Interface BIA-X   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Agente BIA-X      │
                    │                     │
                    │ Intenção + Contexto │
                    │ Regras + Segurança  │
                    └──────┬───────┬──────┘
                           │       │
              ┌────────────┘       └────────────┐
              ▼                                 ▼
   ┌─────────────────────┐          ┌─────────────────────┐
   │  Base de Conhecimento│          │  Prompt de Sistema  │
   │                     │          │                     │
   │ CSV / JSON          │          │ Comportamento       │
   │ Dados simulados     │          │ Limites             │
   └──────────┬──────────┘          │ Segurança           │
              │                     └──────────┬──────────┘
              └──────────────┬────────────────┘
                             ▼
                    ┌─────────────────────┐
                    │        LLM          │
                    │                     │
                    │ Geração da resposta │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Resposta ao usuário │
                    └─────────────────────┘
```

---

## 3. Componentes

### 3.1 Interface

A interface representa o ponto de interação entre o usuário e o BIA-X.

Responsabilidades:

* receber mensagens;
* apresentar respostas;
* manter a experiência conversacional;
* disponibilizar o contexto necessário para a interação.

A tecnologia específica da interface será definida durante a implementação.

A arquitetura não depende obrigatoriamente de uma tecnologia específica.

---

### 3.2 Agente BIA-X

O agente representa a camada responsável pela aplicação das regras comportamentais definidas para o projeto.

Responsabilidades:

* interpretar a solicitação;
* considerar o contexto da conversa;
* aplicar as regras do prompt;
* utilizar informações disponíveis;
* identificar necessidade de esclarecimento;
* evitar respostas sem suporte;
* conduzir a recuperação da conversa.

O agente funciona como a camada intermediária entre a interface, o contexto disponível e o modelo de linguagem.

---

### 3.3 Base de conhecimento

A base de conhecimento contém os dados utilizados pelo protótipo para fornecer contexto ao agente.

A estrutura inicialmente definida é:

```text
data/
├── transactions.csv
├── service_history.csv
├── customer_profile.json
└── financial_products.json
```

Os arquivos representam um ambiente bancário **simulado**.

A base não representa dados reais de clientes ou operações bancárias.

---

### 3.4 Prompt de sistema

O prompt de sistema estabelece as regras de comportamento do BIA-X.

Ele define:

* objetivo;
* contexto;
* tom;
* limites;
* comportamento diante de ambiguidades;
* tratamento de informações ausentes;
* segurança;
* prevenção de respostas inventadas;
* recuperação da conversa.

O prompt funciona como uma camada de orientação do modelo, não como substituto da base de conhecimento.

---

### 3.5 Modelo de linguagem

O LLM é responsável pela interpretação e geração das respostas em linguagem natural.

A arquitetura deve permitir que o modelo seja substituído sem exigir uma alteração completa da estrutura do projeto.

A escolha do modelo e da forma de execução será definida na etapa de implementação.

O uso de um modelo específico não constitui requisito arquitetural permanente do BIA-X.

---

## 4. Fluxo de uma interação

Uma interação típica seguirá conceitualmente estas etapas:

```text
1. Usuário envia uma mensagem
             ↓
2. Interface recebe a mensagem
             ↓
3. BIA-X analisa intenção e contexto
             ↓
4. Sistema consulta informações disponíveis
             ↓
5. Regras do agente são aplicadas
             ↓
6. Contexto + instruções são enviados ao LLM
             ↓
7. LLM gera uma resposta
             ↓
8. Resposta é apresentada ao usuário
```

Esse fluxo poderá ser refinado durante a implementação.

---

## 5. Fluxo de compreensão progressiva

Uma característica importante da arquitetura é permitir que a conversa avance mesmo quando a primeira mensagem não contém todas as informações necessárias.

```text
                 ┌─────────────────┐
                 │ Mensagem        │
                 │ do usuário      │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │ Interpretar     │
                 │ contexto        │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │ Informação      │
                 │ suficiente?     │
                 └──────┬─────┬────┘
                       SIM    NÃO
                        │       │
                        ▼       ▼
                    Responder  Existe
                              compreensão
                              parcial?
                              │
                         ┌────┴────┐
                        SIM       NÃO
                         │         │
                         ▼         ▼
                    Esclarecer   Solicitar
                                 contexto
                         │         │
                         └────┬────┘
                              ▼
                       Nova informação
                              │
                              ▼
                     Atualização do
                         contexto
                              │
                              ▼
                         Resposta
```

Esse fluxo representa a ideia de **Conversation Recovery** definida na documentação do agente.

---

## 6. Tratamento da informação

A arquitetura deverá preservar a distinção entre diferentes estados de informação.

### Informação disponível

Pode ser utilizada como contexto para a resposta.

### Informação parcialmente disponível

Pode justificar uma pergunta de esclarecimento.

### Informação ausente

Não deve ser criada pelo modelo.

### Informação ambígua

Deve ser esclarecida antes de uma resposta conclusiva.

Conceitualmente:

```text
                 Informação
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Disponível   Ambígua      Ausente
          │           │           │
          ▼           ▼           ▼
      Responder   Esclarecer   Informar
                               limitação
```

---

## 7. Fronteira entre dados e LLM

A arquitetura deve manter uma separação conceitual entre:

```text
Dados simulados
      │
      ▼
Contexto fornecido
      │
      ▼
Prompt + regras
      │
      ▼
LLM
      │
      ▼
Resposta
```

O modelo de linguagem não deve ser tratado como uma fonte ilimitada de informações bancárias.

A base de conhecimento fornece o contexto específico do ambiente simulado, enquanto o prompt define como o agente deve utilizar esse contexto.

---

## 8. Segurança arquitetural

A segurança do protótipo será baseada principalmente em limites de escopo, controle de contexto e regras de comportamento.

O BIA-X deverá:

* utilizar dados simulados;
* evitar operações bancárias reais;
* não solicitar credenciais;
* não afirmar que executou uma operação que não foi realizada;
* não inventar informações ausentes;
* reconhecer limitações;
* evitar extrapolar o contexto disponível.

A arquitetura não pressupõe acesso a sistemas bancários reais.

---

## 9. Separação entre aplicação e conhecimento

Os dados devem permanecer separados da lógica da aplicação.

Estrutura:

```text
data/
    dados simulados

src/
    lógica da aplicação
```

Essa separação permite alterar ou ampliar a base de conhecimento sem necessariamente modificar toda a aplicação.

Também facilita testes utilizando diferentes conjuntos de dados simulados.

---

## 10. Estrutura técnica inicial

A implementação inicial poderá evoluir para a seguinte organização:

```text
bia-x-cognitive-bank-guardian/
│
├── README.md
│
├── assets/
│
├── data/
│   ├── transactions.csv
│   ├── service_history.csv
│   ├── customer_profile.json
│   └── financial_products.json
│
├── docs/
│   ├── 01-agent-documentation.md
│   ├── 02-knowledge-base.md
│   ├── 03-prompts.md
│   └── 04-architecture.md
│
├── examples/
│
├── src/
│   └── app.py
│
└── tests/
```

Essa é uma estrutura inicial e poderá ser refinada durante a implementação.

---

## 11. O que não faz parte da arquitetura V1

Para manter o projeto proporcional ao objetivo do desafio, a primeira versão não depende de:

* integração com banco real;
* banco vetorial;
* arquitetura RAG sofisticada;
* múltiplos agentes;
* fine-tuning;
* modelos próprios;
* pipelines de Machine Learning;
* XGBoost;
* SHAP;
* automações bancárias reais.

Essas tecnologias podem ser consideradas em evoluções futuras caso exista uma necessidade técnica que justifique sua utilização.

---

## 12. Arquitetura e evolução do projeto

A arquitetura foi planejada para permitir evolução incremental.

### V1 — Assistente conversacional

```text
Interface
    ↓
BIA-X
    ↓
Base simulada + Prompt
    ↓
LLM
    ↓
Resposta
```

### Evolução futura

O projeto poderá incorporar camadas adicionais para:

* avaliação automatizada;
* observabilidade;
* classificação de intenção;
* recuperação de contexto;
* análise de evidências;
* mecanismos adicionais de segurança;
* métricas de comportamento conversacional.

Essas extensões não são necessárias para o funcionamento básico do protótipo.

---

## 13. Relação com o Cognitive Bank Guardian

O **Cognitive Bank Guardian** representa o conceito mais amplo de análise cognitiva e contextual associado à evolução do projeto.

No V1, ele não será implementado como uma segunda aplicação independente.

A separação conceitual é:

```text
BIA-X
│
├── produto/assistente do desafio
│
└── experiência conversacional
        │
        ▼
Cognitive Bank Guardian
        │
        └── conceito de evolução/laboratório
```

Dessa forma, o projeto evita ampliar artificialmente o escopo da primeira versão.

---

## 14. Princípio arquitetural

A arquitetura do BIA-X segue uma premissa simples:

> **A complexidade deve existir quando resolver um problema real do projeto, não apenas porque uma tecnologia está disponível.**

O objetivo da V1 é demonstrar um assistente funcional, contextual, seguro e capaz de lidar com situações em que a compreensão inicial da mensagem é incompleta.

A arquitetura deverá acompanhar esse objetivo, mantendo separação entre interface, agente, conhecimento, modelo e avaliação.
