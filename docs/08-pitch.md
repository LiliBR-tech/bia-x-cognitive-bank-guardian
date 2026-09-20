# BIA-X — Pitch

## 1. Apresentação

**BIA-X — Cognitive Bank Guardian**

**Banking Intelligence Assistant — Explainable Experience**

O BIA-X é um assistente virtual desenvolvido para um ambiente bancário simulado, com foco em compreensão contextual, respostas seguras e recuperação de conversas.

A proposta parte de um problema simples:

> **Uma mensagem que não pode ser compreendida completamente não deveria necessariamente encerrar uma conversa.**

---

# 2. O problema

Assistentes conversacionais podem encontrar dificuldades quando o usuário envia mensagens:

* incompletas;
* ambíguas;
* pouco contextualizadas;
* diferentes daquilo que o sistema esperava.

Existem dois comportamentos problemáticos:

```text
Mensagem ambígua
       ↓
"Não entendi."
       ↓
Conversa interrompida
```

ou:

```text
Mensagem ambígua
       ↓
O sistema assume uma intenção
       ↓
Resposta potencialmente incorreta
```

O BIA-X busca trabalhar entre esses dois extremos.

---

# 3. A proposta

O BIA-X utiliza uma abordagem de **compreensão progressiva**.

Quando recebe uma mensagem, o agente procura determinar:

```text
A informação é suficiente?
        │
   ┌────┴────┐
  SIM       NÃO
   │          │
   ▼          ▼
Responder   Existe contexto
            suficiente para
            esclarecer?
               │
          ┌────┴────┐
         SIM       NÃO
          │          │
          ▼          ▼
      Esclarecer   Solicitar
                   contexto
```

A conversa pode então continuar até que exista informação suficiente para uma resposta adequada.

---

# 4. O diferencial

O principal diferencial do BIA-X não é simplesmente responder perguntas.

É saber **como continuar a conversa quando ainda não possui informação suficiente para responder**.

O princípio central é:

> **O BIA-X não precisa compreender tudo de imediato para ser útil; precisa reconhecer o que já compreendeu, identificar o que falta e conduzir a conversa até uma resposta segura.**

---

# 5. Exemplo

### Usuário

```text
"Meu pagamento deu problema."
```

Essa mensagem não contém informações suficientes para identificar exatamente o problema.

Em vez de simplesmente responder:

```text
"Não entendi."
```

o BIA-X pode utilizar o contexto disponível:

```text
"Posso ajudar a verificar o contexto. Você está se referindo
a um pagamento por Pix, cartão ou boleto?"
```

O usuário fornece uma nova informação:

```text
"Pix."
```

O agente pode então continuar a interação considerando o novo contexto.

O objetivo é transformar:

```text
ambiguidade
    ↓
esclarecimento
    ↓
contexto
    ↓
resposta
```

---

# 6. Segurança

O BIA-X foi projetado para um ambiente bancário simulado.

Ele não executa operações bancárias reais e não deve:

* acessar contas reais;
* realizar transferências;
* solicitar senhas;
* inventar informações;
* confirmar operações não realizadas;
* apresentar informações ausentes como fatos.

Quando uma informação não estiver disponível, o agente deve reconhecer a limitação.

---

# 7. Base de conhecimento

O protótipo utiliza uma base de conhecimento simulada contendo informações relacionadas ao contexto bancário.

Entre os conjuntos previstos estão:

```text
data/
├── transacoes.csv
├── historico_atendimento.csv
├── perfil_cliente.json
└── produtos_financeiros.json
```

A base fornece o contexto específico utilizado pelo assistente.

O princípio é simples:

> **O que está disponível pode ser utilizado como contexto. O que não está disponível não deve ser inventado para completar a resposta.**

---

# 8. Arquitetura

A arquitetura do BIA-X foi planejada para manter separadas as principais responsabilidades:

```text
Usuário
   ↓
Interface
   ↓
BIA-X
   ├── Contexto
   ├── Regras
   └── Segurança
        ↓
Base de conhecimento
        +
Prompt
        ↓
LLM
        ↓
Resposta
```

Essa estrutura permite evoluir o protótipo sem transformar cada nova funcionalidade em uma alteração completa do sistema.

---

# 9. Avaliação

O projeto será avaliado inicialmente em três dimensões:

### Assertividade

A resposta atende à intenção identificada?

### Segurança

O agente respeita os limites definidos e evita informações inventadas?

### Coerência

A resposta permanece compatível com o contexto e os dados disponíveis?

Além desses critérios, o LAB propõe duas métricas experimentais:

### Conversation Recovery Rate

Avalia a capacidade de recuperar uma conversa que começou com informação insuficiente ou ambígua.

### Minimum Useful Response Rate

Avalia se o agente consegue fornecer uma resposta útil mesmo quando ainda precisa de esclarecimentos.

Essas métricas são complementares aos critérios principais de avaliação.

---

# 10. Público-alvo

O BIA-X foi pensado como um protótipo de assistente conversacional para cenários bancários simulados.

A proposta pode ser utilizada para explorar:

* atendimento contextual;
* interação com dados estruturados;
* engenharia de prompts;
* segurança de agentes;
* tratamento de ambiguidades;
* recuperação conversacional;
* avaliação de respostas geradas por IA.

---

# 11. Evolução

O projeto foi planejado para evoluir incrementalmente.

A primeira versão concentra-se na experiência conversacional:

```text
V1
│
├── Base simulada
├── Prompt
├── LLM
├── Conversação
├── Segurança
└── Avaliação
```

Evoluções futuras poderão explorar:

```text
V2+
│
├── classificação de intenção
├── análise de evidências
├── avaliação automatizada
├── observabilidade
├── detecção de inconsistências
└── mecanismos adicionais de segurança
```

Essas possibilidades não fazem parte do escopo obrigatório da primeira versão.

---

# 12. Relação com o Cognitive Bank Guardian

O nome **Cognitive Bank Guardian** representa o conceito mais amplo que orienta a evolução do projeto.

O **BIA-X** é a aplicação conversacional desenvolvida nesta etapa.

A relação pode ser representada assim:

```text
              Cognitive Bank Guardian
                       │
                       │ conceito
                       ▼
                     BIA-X
                       │
                       ▼
             Experiência conversacional
```

O objetivo da V1 não é implementar todo o conceito de Cognitive Bank Guardian, mas estabelecer uma base funcional para sua evolução.

---

# 13. Por que BIA-X?

O nome representa a ideia de um assistente bancário que vai além da simples geração de respostas.

O **X** representa uma camada de expansão da experiência tradicional de atendimento:

```text
Pergunta
   ↓
Compreensão
   ↓
Contexto
   ↓
Esclarecimento
   ↓
Resposta
```

A proposta não é reproduzir um assistente bancário existente, mas experimentar uma abordagem própria para lidar com contexto, ambiguidade e continuidade da conversa.

---

# 14. Mensagem final

O BIA-X parte de uma premissa:

> **Uma boa experiência conversacional não depende apenas da capacidade de responder. Também depende da capacidade de reconhecer quando ainda não é possível responder — e saber o que perguntar para chegar lá.**

O projeto transforma essa ideia em um protótipo de assistente bancário simulado, utilizando engenharia de prompts, base de conhecimento, LLM, critérios de segurança e avaliação comportamental.

**BIA-X — Banking Intelligence Assistant — Explainable Experience.**

---

# 15. Estrutura do projeto

A documentação produzida até aqui estabelece a seguinte sequência:

```text
01 — Documentação do agente
        ↓
02 — Base de conhecimento
        ↓
03 — Prompts
        ↓
04 — Arquitetura
        ↓
05 — Cenários de interação
        ↓
06 — Avaliação e métricas
        ↓
07 — Segurança e limitações
        ↓
08 — Pitch
```

Essa sequência representa a evolução do projeto desde a definição do problema até a preparação para sua implementação e apresentação.
