---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: busca acadêmica com verificação na fonte primária; devolver ao principal lista de obras candidatas com evidência — NÃO editar prosa nem bib sem nova ordem
referencia: branch fix/cap2-prosa-619-648 @ 43f6fae · 2-fundam/texto.tex ~linhas 618 e 648 · decisão do autor 2026-08-16
criada_em: 2026-08-16T21:10:00Z
prazo: 2026-08-18T12:00:00Z
---

# Busca acadêmica: fontes reais para a frase da seleção multinível (Cap. 2)

Contexto: Wu2022 e Ahmed2023 são fabricadas. O principal já reescreveu a
prosa em rascunho (branch acima) citando Diao2023 e Zhang2023LLMaAA. O autor
pediu uma busca acadêmica para achar outras obras que SUSTENTEM a afirmação
ou CONTRIBUAM com ela, antes do gate.

## O que a frase precisa sustentar

1. **Seleção ativa de prompts/demonstrações**: escolher ativamente os
   exemplos que compõem o prompt de anotação (in-context learning).
   Verificar se Diao2023 (Active Prompting with Chain-of-Thought) realmente
   cobre isso e buscar 1–2 obras adicionais (ex.: seleção de demonstrações
   para ICL, anotação com LLM).
2. **Seleção do próprio oráculo**: escolher QUAL LLM/configuração anota
   (model selection/routing para anotação, comitês de anotadores LLM,
   comparação de anotadores). Se existir literatura real, ela reforça; se
   não existir nada sólido, reportar "sem fonte" — a frase já está escrita
   como passo da tese (E0/E0-P) e sobrevive sem citação.
3. **Ahmed2022 cobre as 4 características do texto curto?** (escassez de
   contexto, esparsidade, ruído/informalidade, ambiguidade — linha ~648).
   Confirmar no PDF/fonte que o survey sustenta as quatro; se alguma não
   estiver lá, dizer qual.

## Método (lição do lote 4 — obrigatório)

- Verificar SEMPRE na fonte primária: ACL Anthology, arXiv API, Crossref,
  página do venue. NUNCA aceitar título/autores de memória ou de parecer.
- Para cada candidata: chave sugerida, título, autores, venue, ano,
  DOI/arXiv, 1 frase do que ela sustenta, e o trecho/segmento que comprova.
- Obra só entra no bib se vier com mini-fichamento (constituição: toda
  referência validada contra fichamento).

## Entrega

Aviso ao principal com a lista (pode ser vazia em 2 — honestidade acima de
cobertura). O principal consolida, ajusta a prosa se preciso e leva ao gate
do autor com antes/depois. Prioridade: depois da sua verificação cruzada do
lote 5, antes de qualquer coisa nova.
