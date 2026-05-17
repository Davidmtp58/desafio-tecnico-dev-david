# Finlytics — Assistente Financeiro Pessoal

`Em desenvolvimento` · MVP previsto para 31/05/2026

---

## 1. Visão Geral e a Dor

A maioria das pessoas olha o extrato bancário e não consegue responder uma pergunta simples: *"pra onde foi meu dinheiro?"*. O Finlytics resolve isso transformando o extrato bruto em uma visão clara: saldo do mês, total por categoria e top 3 de gastos — sem precisar de planilha, sem digitar transação a transação.

**Para quem é:**
O Finlytics é pensado para pessoas físicas que querem entender seus gastos sem o trabalho de manter planilha. O público inclui tanto quem nunca conseguiu criar o hábito de acompanhar finanças, quanto quem tentou planilhas no Excel e desistiu por achar manual e cansativo demais.

**Por que isso importa:**
O mercado de gestão financeira pessoal é maduro e prova que existe demanda real — mas a maioria dos apps consolidados exige cadastro completo, integração bancária e, muitas vezes, assinatura paga. O Finlytics ataca um público que esses produtos não alcançam: pessoas que querem entender seus gastos de forma prática, gratuita e sem fricção. A proposta vai além de listar gastos — é mostrar onde o dinheiro está indo para que o usuário tenha mais consciência na hora de fazer escolhas financeiras.

---

## 2. Arquitetura e Decisões Técnicas

Cada escolha técnica deste projeto foi feita com foco em três critérios: **velocidade de entrega no MVP**, **clareza do pipeline** e **caminho natural para evoluir com IA**. A tabela abaixo resume o que está implementado e o que está planejado para os próximos passos.

| Camada | Escolha | Status | Por que escolhi? |
|---|---|---|---|
| **Linguagem** | Python | ✅ Implementado | Ecossistema maduro para análise de dados e IA, com base sólida do meu aprendizado prévio em BI e bootcamp de GenAI. Mesma linguagem do CSV ao Gemini, sem trocar stack. |
| **Manipulação de dados** | pandas | ✅ Implementado | Resolve em uma linha operações que em Python puro exigiriam laços manuais — filtrar transações, agrupar por categoria, somar valores, converter datas. Integra naturalmente com numpy, matplotlib, Streamlit e APIs de IA, permitindo construir o pipeline inteiro do extrato ao insight sem trocar de ferramenta. |
| **Persistência** | CSV | ✅ Implementado | Entrada direta do extrato bancário, sem fricção de cadastro ou integração bancária. SQLite no roadmap para suporte a histórico multi-mês. |
| **Interface** | Streamlit | 🟡 Planejado | Mantém a stack 100% em Python, sem fricção de aprender HTML/CSS/JS no escopo do MVP. Padrão do mercado de dados para protótipos e dashboards. |
| **IA** | Gemini | 🟡 Planejado | API de LLM escolhida por custo baixo por requisição em comparação às alternativas (OpenAI, Claude). Função no projeto: categorizar transações que não foram classificadas pela regra de palavras-chave, e gerar resumo opinativo dos gastos do mês. Arquitetura prevista é um **pipeline híbrido** (regra → cache → LLM como fallback) para minimizar chamadas pagas à API. |

---

## 3. Demonstração

🚧 *Em construção. Aguardando implementação da interface (Streamlit) para gerar demo visual.*

---

## 4. Destaque de Engenharia — The Hard Part

🚧 *Em construção. Será desenvolvido junto com a implementação do pipeline híbrido de categorização (regra → cache → LLM).*

---

## 5. Insights e Valor de Negócio

🚧 *Em construção.*

---

## 6. Instruções de Instalação e Uso

🚧 *Em construção. Documentação completa será adicionada quando o app estiver funcional.*

---

## 7. Roadmap

🚧 *Em construção.*

---

*Última atualização: 16/05/2026*