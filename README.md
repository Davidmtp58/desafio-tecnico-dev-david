# Finlytics, Assistente Financeiro Pessoal

`Em desenvolvimento` · MVP previsto para 31/05/2026

---

## 1. Visão Geral e a Dor

A maioria das pessoas olha o extrato bancário e não consegue responder uma pergunta simples: *"pra onde foi meu dinheiro?"*. O Finlytics resolve isso transformando o extrato bruto em uma visão clara, com saldo do mês, total por categoria e top 3 de gastos, sem precisar de planilha, sem digitar transação a transação.

**Para quem é:** O Finlytics é pensado para pessoas físicas que querem entender seus gastos sem o trabalho de manter planilha. O público inclui tanto quem nunca conseguiu criar o hábito de acompanhar finanças, quanto quem tentou planilhas no Excel e desistiu por achar manual e cansativo demais.

**Por que isso importa:** O mercado de gestão financeira pessoal é maduro e prova que existe demanda real, mas a maioria dos apps consolidados exige cadastro completo, integração bancária e, muitas vezes, assinatura paga. O Finlytics ataca um público que esses produtos não alcançam: pessoas que querem entender seus gastos de forma prática, gratuita e sem fricção. A proposta vai além de listar gastos, é mostrar onde o dinheiro está indo para que o usuário tenha mais consciência na hora de fazer escolhas financeiras.

---

## 2. Arquitetura e Decisões Técnicas

Cada escolha técnica deste projeto foi feita com foco em três critérios: **velocidade de entrega no MVP**, **clareza do pipeline** e **caminho natural para evoluir com IA**. A tabela abaixo resume o que está implementado e o que está planejado para os próximos passos.

| Camada | Escolha | Status | Por que escolhi? |
|---|---|---|---|
| **Linguagem** | Python | ✅ Implementado | Ecossistema maduro para análise de dados e IA, com base sólida do meu aprendizado prévio em BI e bootcamp de GenAI. Mesma linguagem do CSV ao Gemini, sem trocar stack. |
| **Manipulação de dados** | pandas | ✅ Implementado | Resolve em uma linha operações que em Python puro exigiriam laços manuais, como filtrar transações, agrupar por categoria, somar valores e converter datas. Integra naturalmente com numpy, matplotlib, Streamlit e APIs de IA, permitindo construir o pipeline inteiro do extrato ao insight sem trocar de ferramenta. |
| **Persistência** | CSV | ✅ Implementado | Entrada direta do extrato bancário, sem fricção de cadastro ou integração bancária. SQLite no roadmap para suporte a histórico multi-mês. |
| **Interface** | Streamlit | 🟡 Planejado | Mantém a stack 100% em Python, sem fricção de aprender HTML/CSS/JS no escopo do MVP. Padrão do mercado de dados para protótipos e dashboards. |
| **IA** | Gemini | 🟡 Planejado | API de LLM escolhida por custo baixo por requisição em comparação às alternativas (OpenAI, Claude). Função no projeto: categorizar transações que não foram classificadas pela regra de palavras-chave, e gerar resumo opinativo dos gastos do mês. Arquitetura prevista é um **pipeline híbrido** (regra, cache, LLM como fallback) para minimizar chamadas pagas à API. |

---

## 3. Demonstração

*Em construção. Aguardando implementação da interface (Streamlit) para gerar demo visual.*

---

## 4. Destaque de Engenharia, The Hard Part

*Em construção. Será desenvolvido junto com a implementação do pipeline híbrido de categorização (regra, cache, LLM).*

---

## 5. Insights e Valor de Negócio

**Para o produto (usuário):**
O Finlytics entrega ao usuário um diagnóstico claro do próprio dinheiro em poucos segundos: onde está concentrado o maior volume de gastos, qual o saldo real do mês e quais hábitos pesam mais no orçamento. Essa visibilidade gera autocrítica, abre espaço para revisão de hábitos de consumo e, no médio prazo, cria condições para poupar e investir. O valor está em transformar dado bruto em decisão financeira consciente.

**Para o negócio:**
O mercado de finanças pessoais mostra que existe disposição a pagar por ferramentas robustas: plataformas premium do segmento cobram a partir de R$ 100/mês para acompanhar gastos e investimentos. O Finlytics nasce gratuito, mas projeta um modelo freemium claro: o controle de gastos via CSV permanece sem custo, enquanto recursos avançados ficam em uma camada paga. A versão paga pode incluir integração via Open Finance (entrada automatizada de transações sem upload manual), IA mais sofisticada com recomendações personalizadas, módulo de investimentos (acompanhamento de ações e simulador de aporte mensal) e relatórios analíticos mais profundos. O foco inicial é pessoa física, mas o mesmo modelo pode escalar para cooperativas de crédito ou bancos digitais como solução white-label de educação financeira para os correntistas.

**Para dados / IA:**
Cada usuário que processa um extrato no Finlytics gera, na prática, uma linha de um dataset rico em comportamento financeiro. À medida que o produto evolui e passa a coletar informações adicionais (como profissão, idade e localização durante o cadastro), o conjunto de dados anonimizados abre frentes analíticas valiosas: estimativa de **custo de vida por região e profissão**, **análise comportamental por faixa etária** (como o consumo muda dos 20 aos 60 anos), **mapeamento de padrões de consumo** por faixa de renda, e construção de **modelos preditivos** para hipóteses como "padrões de gasto conseguem prever risco de inadimplência?". Esses derivados têm valor direto para o setor financeiro (cooperativas, fintechs, bancos) e para pesquisas socioeconômicas, e podem se transformar em produtos B2B independentes a partir da mesma base.

---

## 6. Instruções de Instalação e Uso

### Pré-requisitos
- Python 3.12 ou superior
- Git

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/Davidmtp58/finlytics.git
cd finlytics

# 2. Crie e ative o ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1     # Windows (PowerShell)
# source venv/bin/activate       # Linux / macOS

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o script de análise
python relatorio_financeiro.py
```

### O que esperar

O script processa o arquivo `extrato_exemplo.csv` (incluído no repositório) e imprime no terminal:
- Tabela com transações categorizadas
- Total gasto por categoria
- Top 3 categorias de maior gasto no mês

*Versão com interface visual (Streamlit) prevista no roadmap.*
---

## 7. Roadmap

O Finlytics está sendo construído em fases. Abaixo, o que está na fila para evoluir do MVP para um produto completo.

**Curto prazo (consolidação do MVP):**
- Suporte a PDF de extrato bancário (hoje apenas CSV)
- Entrada manual de transações (criar, editar e corrigir categoria)
- Implementação da interface visual em Streamlit
- Pipeline híbrido de categorização com IA (regra, cache, LLM via Gemini)

**Médio prazo (evolução do produto):**
- Integração com Open Finance via Belvo ou Pluggy (entrada automática de transações)
- Objetivos e caixinhas de economia (definir metas e acompanhar progresso)
- Persistência em SQLite para histórico multi-mês

**Longo prazo (visão de produto completo):**
- Chat em linguagem natural com os próprios dados ("quanto gastei em mercado em abril?")
- Módulo de investimentos (acompanhamento de ações e simulador de aporte mensal)
- Ativação do modelo freemium com recursos avançados em camada paga

---

*Última atualização: 17/05/2026*