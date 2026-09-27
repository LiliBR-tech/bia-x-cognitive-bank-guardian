# BIA-X — Base de Conhecimento

**Banking Intelligence Assistant — Explainable Experience**

> **Projeto:** BIA-X — Cognitive Bank Guardian
>
> 
> **Laboratório:** Bank Cognitive Immune Lab
>
> 
> **Etapa:** 2 — Base de Conhecimento
>
> 
> **Versão:** V1 — DIO Lab

---

## 1. Objetivo

A base de conhecimento do BIA-X fornece as informações utilizadas pelo agente para contextualizar as conversas e formular respostas.

O objetivo não é criar uma grande quantidade de dados, mas disponibilizar informações suficientes para testar os principais comportamentos definidos na documentação do agente:

* resposta baseada em informação disponível;
* utilização de contexto;
* identificação de informação ausente;
* tratamento de ambiguidades;
* solicitação de esclarecimento;
* recuperação da conversa;
* reconhecimento de informações inexistentes;
* prevenção de respostas inventadas.

A base utiliza exclusivamente dados simulados.

---

## 2. Princípio da Base de Conhecimento

O BIA-X não deve tratar a base de conhecimento como uma fonte para preencher lacunas por suposição.

A relação esperada é:

```text
Base de conhecimento
        ↓
Informação disponível
        ↓
Contexto
        ↓
LLM
        ↓
Resposta fundamentada
```

Quando uma informação necessária não estiver disponível:

```text
Informação ausente
        ↓
BIA-X reconhece a limitação
        ↓
Solicita esclarecimento
ou
informa que não possui dados suficientes
```

O princípio central é:

> **Ausência de informação não deve ser transformada em informação inventada.**

---

## 3. Estrutura da Base

A V1 utilizará uma estrutura simples, inspirada nos dados disponibilizados como referência pelo desafio e adaptada ao caso de uso do BIA-X.

```text
data/
├── transactions.csv
├── service_history.csv
├── customer_profile.json
└── financial_products.json
```

Os arquivos podem ser ampliados conforme os testes do agente evoluírem.

---

## 4. `transactions.csv`

### Finalidade

Representar movimentações financeiras simuladas de uma pessoa cliente.

### Informações previstas

```text
id
data
descricao
categoria
tipo
valor
estabelecimento
status
```

### Exemplo conceitual

```csv
id,data,descricao,categoria,tipo,valor,estabelecimento,status
T001,2026-09-01,Supermercado,alimentacao,debito,245.80,Mercado Central,concluida
T002,2026-09-02,Combustivel,transporte,debito,180.00,Posto Avenida,concluida
T003,2026-09-03,Streaming,entretenimento,debito,39.90,StreamPlay,concluida
```

### Utilização pelo BIA-X

Esses dados podem ser utilizados para consultas como:

> "Quanto gastei com alimentação?"

ou:

> "Qual foi minha última compra no supermercado?"

O agente deve responder somente com base nos registros disponíveis.

---

## 5. `service_history.csv`

### Finalidade

Representar interações anteriores simuladas.

Esse arquivo permite testar situações nas quais uma nova mensagem depende parcialmente do contexto de uma conversa anterior.

### Informações previstas

```text
id_atendimento
data
categoria
mensagem_usuario
resposta
status
```

### Exemplo conceitual

```csv
id_atendimento,data,categoria,mensagem_usuario,resposta,status
A001,2026-09-01,cartao,"Meu cartão foi recusado","Atendimento registrado para análise do cartão",encerrado
A002,2026-09-05,transacao,"Não reconheço uma compra","Transação encaminhada para análise",encerrado
```

### Utilização pelo BIA-X

O histórico poderá fornecer contexto adicional para perguntas como:

> "E aquele problema do cartão?"

Nesse caso, o agente deve verificar se existe contexto suficiente no histórico antes de assumir qual problema está sendo mencionado.

---

## 6. `customer_profile.json`

### Finalidade

Representar informações gerais e simuladas do perfil utilizado pelo agente.

O arquivo não representa dados reais de uma pessoa.

### Informações previstas

```json
{
  "cliente_id": "C001",
  "perfil": {
    "faixa_etaria": "30-39",
    "relacionamento": "cliente_simulado",
    "preferencias": [
      "atendimento digital",
      "respostas objetivas"
    ]
  },
  "contexto": {
    "produtos_utilizados": [
      "conta_corrente",
      "cartao"
    ]
  }
}
```

### Utilização

O perfil pode ser usado para contextualizar a interação, sem permitir que o agente utilize informações pessoais inexistentes ou faça inferências indevidas.

O perfil não deve ser utilizado para determinar decisões financeiras em nome da pessoa usuária.

---

## 7. `financial_products.json`

### Finalidade

Representar produtos e serviços financeiros fictícios disponíveis no ambiente de demonstração.

### Informações previstas

```json
{
  "produtos": [
    {
      "id": "P001",
      "nome": "Conta Digital Exemplo",
      "categoria": "conta",
      "descricao": "Conta digital para movimentações financeiras simuladas.",
      "status": "disponivel"
    },
    {
      "id": "P002",
      "nome": "Cartão Exemplo",
      "categoria": "cartao",
      "descricao": "Cartão de crédito utilizado no ambiente simulado.",
      "status": "disponivel"
    }
  ]
}
```

### Utilização

O BIA-X poderá responder perguntas relacionadas aos produtos que estejam efetivamente descritos na base.

Caso a pessoa pergunte sobre um produto inexistente:

> "O produto XYZ possui qual taxa?"

o agente não deverá criar uma taxa ou característica que não esteja presente nos dados.

---

## 8. Contexto e Informação Ausente

Uma característica importante da base do BIA-X é permitir a diferenciação entre:

### Informação existente

A base contém os dados necessários.

```text
Pergunta
   ↓
Dado encontrado
   ↓
Resposta
```

### Informação parcialmente disponível

A base contém parte do contexto.

```text
Pergunta
   ↓
Contexto parcial
   ↓
Identificação da informação ausente
   ↓
Esclarecimento
```

### Informação inexistente

A base não contém os dados necessários.

```text
Pergunta
   ↓
Nenhum dado relevante encontrado
   ↓
Informar limitação
```

Essa distinção será utilizada posteriormente nos prompts e nos testes.

---

## 9. Dados para Testar Ambiguidade

Além dos dados bancários simulados, a base será organizada de forma a permitir testes de compreensão progressiva.

Exemplo:

```text
Mensagem:
"Quero ver meu negócio."
```

Essa mensagem não deve ser automaticamente associada a uma única informação.

O agente deve buscar reduzir a ambiguidade.

Uma resposta possível seria:

> "Posso ajudar. Você quer consultar uma transação, um produto financeiro ou outra informação da sua conta?"

O objetivo desse teste não é demonstrar que a IA "adivinhou" a intenção, mas que conseguiu conduzir a conversa com segurança.

---

## 10. Dados para Conversation Recovery

O histórico de atendimento será utilizado para testar a recuperação de conversas.

Exemplo:

```text
Usuário:
"Quero saber sobre aquele problema."

BIA-X:
"Posso verificar. Você está se referindo ao problema relacionado ao cartão ou à transação mencionada anteriormente?"
```

Após a resposta:

```text
Usuário:
"O cartão."

BIA-X:
[utiliza o contexto correspondente]
```

Esse comportamento será utilizado como um dos diferenciais experimentais do BIA-X.

---

## 11. Dados Mockados e Segurança

Todos os dados utilizados nesta versão são fictícios.

Não serão utilizados:

* números reais de contas;
* cartões reais;
* documentos pessoais;
* dados bancários reais;
* credenciais;
* informações financeiras privadas.

A utilização de dados simulados também segue a orientação do desafio de utilizar os dados mockados fornecidos como ponto de partida e adaptá-los ao caso de uso.

---

## 12. Relação entre Base e LLM

A LLM não será tratada como fonte independente de fatos bancários.

O fluxo esperado é:

```text
Dados
  ↓
Seleção do contexto relevante
  ↓
Contexto fornecido ao agente
  ↓
System Prompt + contexto
  ↓
LLM
  ↓
Resposta
```

O modelo deve respeitar as limitações estabelecidas pelo contexto disponível.

Quando não houver informação suficiente, a resposta esperada é reconhecer essa ausência em vez de completar a informação com conhecimento não fornecido pela base.

---

## 13. Casos de Uso da Base

A base será preparada para suportar pelo menos os seguintes cenários:

| Cenário                          | Fonte principal             |
| -------------------------------- | --------------------------- |
| Consulta de transação            | `transactions.csv`          |
| Consulta de gastos               | `transactions.csv`          |
| Contexto de atendimento anterior | `service_history.csv`       |
| Contexto geral do cliente        | `customer_profile.json`     |
| Consulta de produto              | `financial_products.json`   |
| Informação ausente               | combinação das fontes       |
| Ambiguidade                      | contexto + histórico        |
| Conversation Recovery            | histórico + nova mensagem   |

---

## 14. Relação com a Avaliação

A base de conhecimento será utilizada posteriormente para avaliar três dimensões principais do desafio:

### Assertividade

A resposta corresponde à informação solicitada?

### Segurança

O agente evita inventar informações que não estão disponíveis?

### Coerência

A resposta é compatível com o contexto fornecido?

Esses critérios serão complementados pelos testes experimentais do BIA-X:

* Conversation Recovery;
* Minimum Useful Response;
* tratamento de ambiguidade.

---

## 15. Limitações da Base

A base da V1 é deliberadamente pequena.

Ela não pretende representar a complexidade de uma instituição financeira real.

Sua finalidade é fornecer um ambiente controlado para demonstrar:

```text
dados
  ↓
contexto
  ↓
LLM
  ↓
resposta
```

e permitir testar como o agente se comporta quando:

* possui informação;
* possui informação parcial;
* não possui informação.

---

## 16. Evolução da Base

Futuras versões poderão incorporar novos conjuntos de dados para ampliar os testes do Cognitive Bank Guardian.

Possíveis extensões:

```text
Eventos
Anomalias
Alertas
Evidências
Relacionamentos entre eventos
Contexto investigativo
```

Esses elementos permanecem fora do escopo da V1 do DIO.

---

## 17. Princípio da Base de Conhecimento

A base de conhecimento do BIA-X não existe apenas para fornecer respostas.

Ela também existe para definir **os limites do que o agente pode afirmar**.

> **O que está na base pode ser utilizado como evidência contextual.
> O que não está na base não deve ser inventado para completar uma resposta.**
