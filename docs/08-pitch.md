# BIA-X — Pitch

## 1. Apresentação

**BIA-X — Cognitive Bank Guardian**

**Banking Intelligence Assistant — Explainable Experience**

O BIA-X é um protótipo de assistente virtual desenvolvido para um ambiente bancário simulado, explorando compreensão contextual, interação com uma base de conhecimento, segurança conversacional e avaliação comportamental de respostas geradas por IA.

A proposta parte de uma questão simples:

> **Quando uma mensagem não contém informação suficiente, como um assistente pode continuar sendo útil sem simplesmente interromper a conversa ou assumir uma intenção que não foi informada?**

---

# 2. O problema

Assistentes conversacionais podem encontrar dificuldades quando o usuário envia mensagens:

* incompletas;
* ambíguas;
* pouco contextualizadas;
* diferentes daquilo que o sistema esperava.

Dois comportamentos podem surgir:

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

O BIA-X explora uma terceira possibilidade:

```text
Mensagem
   ↓
O que já pode ser identificado?
   ↓
O que ainda está faltando?
   ↓
É possível esclarecer?
   ↓
Continuidade da conversa
```

A proposta é investigar se o assistente pode utilizar o contexto disponível para conduzir a interação sem transformar suposições em fatos.

---

# 3. A proposta

O BIA-X utiliza uma abordagem de **compreensão progressiva**.

Quando recebe uma mensagem, o agente deve procurar distinguir entre:

```text
Informação disponível
        │
        ▼
Informação suficiente?
        │
   ┌────┴────┐
  SIM       NÃO
   │          │
   ▼          ▼
Responder   Verificar contexto
              │
         ┌────┴────┐
       SIM        NÃO
        │           │
        ▼           ▼
   Esclarecer   Reconhecer
                limitação
```

A ideia é que uma conversa não precise ser encerrada apenas porque a primeira mensagem não contém todas as informações necessárias.

Entretanto, essa capacidade é tratada como uma **hipótese comportamental a ser validada experimentalmente**, e não como uma propriedade automaticamente garantida pelo uso de um LLM.

---

# 4. O diferencial

O diferencial conceitual do BIA-X não está apenas em gerar respostas.

Está em explorar **como o assistente deve se comportar quando a informação disponível é insuficiente, ambígua ou distribuída entre diferentes fontes de contexto**.

O princípio central é:

> **O BIA-X não precisa compreender tudo de imediato para tentar ser útil; precisa distinguir o que está evidenciado, o que ainda falta e quando uma resposta deve ser substituída por uma solicitação de esclarecimento.**

Essa proposta também exige uma segunda preocupação:

```text
Contexto disponível
       ↓
Evidência
       ↓
Resposta
```

e não:

```text
Contexto incompleto
       ↓
Suposição
       ↓
"Fato" inventado
```

A validação experimental da V1 justamente verifica até que ponto o comportamento observado corresponde a esse princípio.

---

# 5. Exemplo conceitual

### Usuário

```text
"Meu pagamento deu problema."
```

Essa mensagem não identifica, por si só, qual pagamento está sendo mencionado nem qual problema ocorreu.

Uma estratégia possível seria solicitar apenas a informação necessária para continuar:

```text
"Posso ajudar a verificar o contexto. Você está se referindo
a um pagamento por Pix, cartão ou boleto?"
```

O usuário fornece uma nova informação:

```text
"Pix."
```

A interação pode então continuar utilizando esse novo contexto.

O fluxo conceitual é:

```text
ambiguidade
    ↓
identificação do que falta
    ↓
esclarecimento
    ↓
novo contexto
    ↓
resposta
```

Esse exemplo representa o comportamento que o projeto pretende investigar; ele não deve ser interpretado como evidência de que todas as situações de ambiguidade já estejam resolvidas pela V1.

---

# 6. Segurança

O BIA-X foi projetado para um ambiente bancário simulado.

O protótipo não executa operações bancárias reais e estabelece limites explícitos para a interação.

Entre eles:

* não acessar contas bancárias reais;
* não realizar transferências;
* não solicitar senhas, tokens ou códigos de autenticação;
* não confirmar operações que não estejam registradas na base;
* não tratar informações ausentes como fatos;
* reconhecer limitações quando a informação necessária não estiver disponível.

A segurança também é tratada como uma propriedade que precisa ser **testada**, e não apenas documentada.

Os testes da V1 demonstraram que algumas dessas regras ainda exigem evolução. Por exemplo, foram observados casos de informação inventada e de inferência não sustentada pelos dados.

Por isso, a avaliação comportamental faz parte da própria proposta do projeto.

---

# 7. Base de conhecimento

O protótipo utiliza uma base de conhecimento simulada contendo informações relacionadas ao contexto bancário.

Entre os conjuntos utilizados estão:

```text
data/
├── transactions.csv
├── service_history.csv
├── customer_profile.json
└── financial_products.json
```

Essas fontes representam diferentes dimensões do contexto:

```text
Perfil do cliente
        +
Produtos financeiros
        +
Histórico de atendimento
        +
Transações
        ↓
Contexto do BIA-X
```

O princípio estabelecido para a aplicação é:

> **O que está disponível pode ser utilizado como contexto. O que não está disponível não deve ser inventado para completar a resposta.**

A avaliação experimental verifica justamente se o comportamento do modelo permanece compatível com esse princípio.

---

# 8. Arquitetura

A arquitetura do BIA-X mantém separadas as principais responsabilidades do protótipo:

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

A aplicação utiliza uma camada de contexto para disponibilizar os dados ao modelo e um conjunto de instruções para estabelecer limites de comportamento.

Essa separação permite avaliar individualmente:

* qualidade do contexto;
* comportamento do prompt;
* resposta do modelo;
* limites de segurança;
* resultados observados durante os testes.

---

# 9. Avaliação

A V1 utiliza avaliação baseada em cenários comportamentais.

Os principais critérios são:

### Assertividade

A resposta permanece compatível com a informação disponível e com a pergunta apresentada?

### Segurança

O agente respeita os limites definidos e evita apresentar informações não sustentadas como fatos?

### Coerência

A resposta permanece compatível com o contexto fornecido durante a interação?

Os resultados são classificados como:

```text
PASS
PARTIAL
FAIL
INCONCLUSIVE
```

Essa classificação evita transformar um teste inconclusivo, por exemplo devido a timeout do modelo, em uma conclusão sobre o comportamento do agente.

Na primeira bateria de validação, foram avaliados cenários envolvendo:

* consulta factual;
* informação inexistente;
* relação entre fontes;
* conflito entre fontes;
* prompt injection;
* cálculo sobre transações;
* continuidade conversacional;
* solicitação fora do escopo.

Os resultados observados demonstraram que a arquitetura funciona como ambiente experimental, mas também revelaram comportamentos que ainda precisam ser aprimorados, incluindo geração de informação não existente, inferências não sustentadas e perda de informações estruturadas durante determinadas respostas.

---

# 10. Métricas experimentais

Além dos critérios principais, o LAB propõe duas métricas experimentais para futuras avaliações:

### Conversation Recovery Rate

Métrica destinada a avaliar a capacidade de recuperar uma conversa iniciada com informação insuficiente ou ambígua.

### Minimum Useful Response Rate

Métrica destinada a avaliar se o agente consegue fornecer uma resposta útil mesmo quando ainda necessita de esclarecimentos adicionais.

Essas métricas fazem parte da proposta experimental do projeto.

**Na versão atual, elas não devem ser interpretadas como métricas já consolidadas ou como resultados quantitativos da V1.**

A intenção é estabelecer posteriormente uma metodologia reproduzível para sua medição.

---

# 11. Público-alvo

O BIA-X foi concebido como um protótipo de assistente conversacional para cenários bancários simulados.

O projeto pode ser utilizado para explorar:

* atendimento contextual;
* interação com dados estruturados;
* engenharia de prompts;
* segurança de agentes;
* tratamento de ambiguidades;
* continuidade conversacional;
* avaliação de respostas geradas por IA;
* limitações de modelos de linguagem em contextos estruturados.

O objetivo da V1 não é substituir sistemas bancários reais, mas criar um ambiente controlado para investigar esses comportamentos.

---

# 12. Estado atual

A V1 já possui:

```text
✓ Base de conhecimento simulada
✓ Documentação do agente
✓ Prompt de comportamento
✓ Arquitetura definida
✓ Aplicação conversacional
✓ Integração com LLM
✓ Critérios de segurança
✓ Cenários de avaliação
✓ Validação comportamental inicial
```

A validação também revelou limitações:

```text
! Algumas respostas apresentam informações não existentes
! Algumas relações são inferidas sem evidência suficiente
! Determinadas informações estruturadas podem ser omitidas
! Alguns testes sofrem com tempo de geração do modelo
! Nem todos os comportamentos de segurança estão comprovados
```

Portanto, a V1 deve ser entendida como um **protótipo experimental em validação**, e não como um assistente bancário pronto para produção.

---

# 13. Evolução

O projeto foi planejado para evoluir incrementalmente.

A primeira versão concentra-se na experiência conversacional e na construção de uma base experimental:

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

# 14. Relação com o Cognitive Bank Guardian

O nome **Cognitive Bank Guardian** representa o conceito mais amplo associado à evolução do projeto.

O **BIA-X** constitui a camada conversacional desenvolvida nesta etapa.

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

A V1 não pretende implementar todo o conceito de Cognitive Bank Guardian.

Seu objetivo é estabelecer uma base experimental para estudar a interação entre:

```text
Dados
  +
Contexto
  +
LLM
  +
Regras
  +
Segurança
  +
Avaliação
```

---

# 15. Por que BIA-X?

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

A proposta não é reproduzir um assistente bancário existente.

É experimentar uma abordagem própria para lidar com contexto, ambiguidade, continuidade e limites de segurança em uma aplicação baseada em IA generativa.

---

# 16. Mensagem final

O BIA-X parte de uma premissa:

> **Uma boa experiência conversacional não depende apenas da capacidade de responder. Também depende da capacidade de reconhecer quando ainda não é possível responder — e identificar o que precisa ser esclarecido para continuar.**

Essa premissa orienta o protótipo, mas também orienta sua avaliação.

Porque em sistemas baseados em IA generativa existe uma diferença fundamental entre:

```text
parecer que entendeu
```

e

```text
demonstrar que respondeu com base em evidências.
```

O BIA-X explora justamente esse espaço.

Um ambiente bancário simulado, uma base de conhecimento, engenharia de prompts, uma LLM e uma metodologia de avaliação são combinados para investigar como um assistente pode lidar com contexto e incerteza sem transformar ausência de informação em certeza artificial.

**BIA-X — Banking Intelligence Assistant — Explainable Experience.**

---

# 17. Estrutura do projeto

A documentação produzida estabelece a seguinte sequência:

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

Essa sequência representa a evolução do projeto desde a definição do problema até sua implementação, validação e apresentação.

O pitch sintetiza essa trajetória sem substituir as evidências apresentadas na documentação técnica e nos testes experimentais.
