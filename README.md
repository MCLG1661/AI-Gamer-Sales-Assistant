## 🎮 AI Gamer Sales Assistant

*Assistente Consultivo de Vendas com IA Generativa e Prompt Engineering*

![Generative AI](https://img.shields.io/badge/Generative%20AI-Sales%20Assistant-8A2BE2)
![Prompt Engineering](https://img.shields.io/badge/AI-Prompt%20Engineering-412991)
![Sales](https://img.shields.io/badge/Sales-Consultative%20Selling-2E8B57)
![Strategy](https://img.shields.io/badge/Strategy-Upsell%20%26%20Cross--sell-orange)
![GitHub](https://img.shields.io/badge/GitHub-Documentation-181717?logo=github)
![Status](https://img.shields.io/badge/Status-Protótipo-blue)

O **AI Gamer Sales Assistant** é um protótipo de assistente consultivo desenvolvido
com **IA Generativa e Prompt Engineering** para apoiar vendedores na condução de
atendimentos comerciais no segmento gamer e de tecnologia.

A solução foi estruturada para transformar uma necessidade inicial do cliente em
um processo de:

**Diagnóstico → Qualificação → Oferta → Upsell → Cross-sell → Fechamento**

O projeto explora como prompts estruturados podem apoiar decisões comerciais,
padronizar abordagens e gerar mensagens adaptadas ao contexto do cliente.

> O projeto atual é um protótipo baseado em Prompt Engineering. Não há integração
> automatizada com catálogo, CRM, e-commerce ou API de IA nesta versão.

---

## 🎯 Objetivo

Estruturar um assistente capaz de apoiar uma abordagem de **venda consultiva**,
indo além da simples recomendação de produtos.

O assistente busca :

- Compreender a necessidade do cliente
- Identificar o contexto da compra
- Qualificar a oportunidade
- Adaptar a argumentação
- Identificar oportunidades de upsell
- Identificar oportunidades de cross-sell
- Estruturar argumentos de valor
- Gerar mensagens para canais digitais

---

## 💡 Problema

Em atendimentos comerciais, uma abordagem baseada apenas em :

> “Qual produto você procura?”

pode limitar a capacidade do vendedor de compreender o contexto real da compra.

Uma abordagem consultiva busca entender também :

- Quem utilizará o produto
- Quem toma a decisão
- Qual problema precisa ser resolvido
- Qual orçamento está disponível
- Qual nível de desempenho é esperado
- Qual é a urgência da compra

O projeto utiliza IA Generativa para estruturar esse processo de análise.

---

## 🧠 Estratégia do Assistente

A lógica conceitual segue:

```text
Necessidade do Cliente
        ↓
Leitura do Contexto
        ↓
Qualificação
        ↓
Diagnóstico da Oportunidade
        ↓
Estratégia Comercial
        ↓
Oferta Principal
      ↙     ↘
  Upsell   Cross-sell
      ↘     ↙
Argumentação de Valor
        ↓
Fechamento
        ↓
Mensagem Personalizada
```

---

## 🏗️ Arquitetura Visual

A arquitetura representa o fluxo conceitual utilizado pelo assistente para
transformar informações do cliente em uma estratégia de abordagem comercial.



> ⚠️ A arquitetura representa o funcionamento conceitual do protótipo baseado
> em prompts. Integrações com catálogo, CRM e APIs fazem parte de possíveis
> evoluções do projeto.

---

## 🔄 Evolução do Projeto

Uma característica importante do projeto é a evolução iterativa do prompt.

🔹 Versão 1 — Assistente de Vendas

A primeira versão concentrou-se em :

- Identificação da necessidade
- Perguntas de qualificação
- Sugestão de produtos
- Oferta principal
- Cross-sell
- Ancoragem básica

🔥 Versão 2 — Assistente Consultivo

A segunda versão adicionou novas dimensões de análise :

- Motivação da compra
- Identificação do decisor
- Nível de urgência
- Sensibilidade a preço
- Risco de perda
- Perfil racional, emocional ou híbrido
- Upsell
- Cross-sell contextual
- Estratégia de ancoragem
- Gatilho de fechamento
- Mensagem personalizada

Essa evolução demonstra um processo de **refinamento iterativo de prompts**
orientado ao contexto de negócio.

---

## 🧩 Estrutura da Análise

O prompt principal foi dividido em dez etapas.

A. Leitura do Cliente

Identifica :

- Necessidade
- Motivação
- Possível decisor

B. Diagnóstico da Oportunidade

Analisa :

- High Ticket / Misto / Low Ticket
- Urgência
- Sensibilidade a preço
- Risco de perda

C. Perfil do Cliente

Classificação proposta :

- Racional
- Emocional
- Híbrido

D. Qualificação

Gera até cinco perguntas relacionadas a :

- Orçamento
- Jogos ou utilização
- Desempenho
- Mobilidade
- Urgência

E. Oferta Principal

Estrutura :

- Produto recomendado
- Justificativa
- Argumento de valor
- Forma de apresentação

F. Upsell

Avalia se existe uma oportunidade coerente de upgrade.

G. Cross-sell

Identifica produtos complementares relacionados a :

- Performance
- Conforto
- Estética

H. Ancoragem

Utiliza uma das abordagens :

**Bom → Ótimo → Premium**

ou

**Custo-benefício → Performance**

I. Fechamento

Estrutura uma frase utilizando elementos de :

- Urgência leve
- Escassez
- Segurança

J. Mensagem Final

Produz uma mensagem adaptada para :

- WhatsApp
- Instagram
- Atendimento digital

---

## 🧠 Prompt Engineering

O projeto utiliza algumas estratégias de estruturação de prompts :

### Role Definition

Define explicitamente o papel do modelo como assistente especializado em vendas
no segmento gamer.

### Context

Fornece informações sobre :

- Segmento
- Categorias
- Produtos High Ticket
- Produtos Low Ticket

### Structured Output

A resposta segue uma estrutura previamente determinada.

### Behavioral Constraints

O prompt determina comportamentos como :

- Não ser insistente
- Não forçar High Ticket
- Priorizar clareza
- Adaptar a linguagem
- Justificar recomendações

### Conditional Rules

Algumas situações ativam estratégias específicas.

Exemplos:

```text
Desempenho ruim
      ↓
Upgrade / RAM

Jogos competitivos
      ↓
Periféricos

Estudo + mobilidade
      ↓
Notebook

Setup
      ↓
Periféricos / decoração
```

---

## 🛠️ Tecnologias e Conceitos

**Generative AI** - Geração e análise das respostas 

**Prompt Engineering** - Estruturação do comportamento

**Consultative Selling** - Metodologia comercial

**Upselling** - Identificação de upgrades

**Cross-selling** - Produtos complementares

**Customer Profiling** - Estruturação do contexto

**Markdown** - Documentação

**Git/GitHub** - Versionamento

---

## 🧪 Exemplo de Uso

### Entrada

```text
Meu filho precisa de um notebook para estudar.

Eu vou comprar, mas ele também gostaria de usar o computador para jogar.
```

### Análise esperada

```text
Oportunidade: Mista / tendência High Ticket
Decisor: responsável pela compra
Necessidade principal: estudos
Necessidade secundária: jogos
Estratégia: equilibrar produtividade, desempenho e investimento
```

O assistente pode então estruturar perguntas adicionais antes de recomendar
uma configuração ou categoria de produto.

---

## ⚠️ Limitações

O protótipo não possui atualmente :

- Catálogo real de produtos
- Consulta de estoque
- Preços atualizados
- Integração com CRM
- Integração com WhatsApp
- Integração com Instagram
- API de LLM
- Métricas reais de conversão

Por isso, recomendações produzidas pelo modelo devem ser interpretadas como
**apoio ao processo comercial**, e não como dados operacionais do negócio.

---

## 📂 Estrutura do Projeto

```text
AI-Gamer-Sales-Assistant/
│
├── prompts/
│   ├── prompt-v1.md
│   └── prompt-v2.md
│
├── exemplos/
│   ├── exemplo-notebook.md
│   └── exemplo-setup.md
│
├── images/
│   └── architecture.png
│
└── README.md
```

---

## 📈 Aplicações

O conceito pode ser adaptado para :

- Lojas de informática
- E-commerce
- Atendimento por WhatsApp
- Social Selling
- Treinamento comercial
- Assistência ao vendedor
- Operações de Inside Sales

---

## 🚀 Roadmap

### Versão atual

**Prompt Engineering + Assistente Consultivo**

### Próximas evoluções

- Catálogo estruturado de produtos
- RAG para consulta ao catálogo
- API de LLM
- Interface web
- Integração com CRM
- Integração com WhatsApp
- Histórico de atendimentos
- Guardrails comerciais
- Métricas de conversão
- Dashboard
- Avaliação das respostas do assistente

Uma evolução mais avançada poderia assumir :

```text
Cliente
   ↓
Interface Conversacional
   ↓
LLM
   ↓
RAG / Catálogo
   ↓
Sales Tools
   ↓
CRM / E-commerce
   ↓
Resposta
```

---

## 💡 Competências Demonstradas

- Prompt Engineering
- Generative AI
- Vendas Consultivas
- Estratégia Comercial
- Customer Profiling
- Upselling
- Cross-selling
- Estruturação de processos
- Documentação técnica
- Git/GitHub

---

## 🤝 Como Contribuir

Contribuições são bem-vindas especialmente nas áreas de :

- Prompt Engineering
- Sales AI
- RAG
- Avaliação de prompts
- Automação comercial
- UX conversacional

1. Faça um Fork
2. Crie uma branch
3. Implemente e documente sua melhoria
4. Faça o commit
5. Envie a branch
6. Abra um Pull Request

---

## 👨‍💻 Autor

**Marcus Guedes**

Marketing | Data Science | Inteligência Artificial | Gestão de Projetos

GitHub: MCLG1661  

LinkedIn: Marcus Guedes

---

🎮 **IA Generativa aplicada à venda consultiva: entender antes de recomendar.**
