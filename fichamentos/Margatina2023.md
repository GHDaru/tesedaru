---
id: Margatina2023
title: "Active Learning Principles for In-Context Learning with Large Language Models"
authors: ["Margatina, Katerina", "Schick, Timo", "Aletras, Nikolaos", "Dwivedi-Yu, Jane"]
year: 2023
venue: "Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 5011--5034"
doi: "10.18653/v1/2023.findings-emnlp.334"
pdf: referencias-pdf/Margatina2023.pdf

paper_type: avaliacao
pillars: [P3, geral]
status: fichado

proposes: []
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza,
               selecao-por-diversidade, selecao-por-similaridade, k-means,
               few-shot, aprendizado-em-contexto, selecao-de-demonstracoes]
datasets: [crossfit]
metrics: [acuracia, macro-f1, perplexidade]
tasks: [classificacao-de-texto]
models: [gpt-2, gpt-j, gpt-neox, opt, sentence-bert]

extends: []
compares_with: []   # o artigo compara-se a Liu et al. 2022 (KATE) e Gonen et al. 2022 (SPELL); nenhuma das duas está no nosso bib, então não declaro aresta pendurada
contradicts: []
builds_on: [Settles2009, Lewis1994]

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Sustenta a frase do Cap. 2 que estende a seleção ativa para além das
           instâncias, até os exemplos que compõem o prompt de anotação: é o
           trabalho que formula explicitamente a escolha de demonstrações como
           problema de aprendizado ativo baseado em pool."
  - type: ameaca
    target: DRI-SL
    note: "Achado incômodo e útil: amostragem por incerteza, forte no aprendizado
           ativo supervisionado, tem o PIOR desempenho no aprendizado em contexto
           (§4, p. 5014). Vale como limite declarado de escopo — a incerteza que
           o FALCO usa opera sobre classificador treinado no laço, não sobre
           demonstrações de prompt."
  - type: fundamenta
    target: LCE
    note: "A §5.5 (p. 5017) mostra que o RANKING dos métodos muda conforme a
           métrica (F1 × acurácia) — apoio externo direto à prática da tese de
           reportar acurácia e Macro F1 lado a lado e de não fechar veredito
           por uma métrica só."
---

# Active Learning Principles for In-Context Learning with Large Language Models

## Resumo (com as minhas palavras)
Os autores tratam a escolha das demonstrações do prompt — os exemplos rotulados
que acompanham a pergunta no aprendizado em contexto — como um problema de
aprendizado ativo baseado em pool, executado em UMA única iteração, já que o
modelo não é retreinado a cada rodada. Comparam quatro famílias de seleção
(aleatória, diversidade, incerteza e similaridade) em 15 modelos das famílias
GPT e OPT, de 125 milhões a 30 bilhões de parâmetros, sobre 15 tarefas de
classificação e 9 de múltipla escolha. O resultado principal contraria a
intuição herdada do aprendizado ativo clássico: escolher demonstrações
semanticamente SIMILARES ao exemplo de teste vence tudo, inclusive a seleção
aleatória, enquanto a amostragem por incerteza — a mais forte no cenário
supervisionado — fica em último. Um achado metodológico fecha o trabalho: o
ranking dos métodos muda conforme a métrica escolhida.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A seleção de demonstrações para aprendizado em contexto é formulável como aprendizado ativo baseado em pool de UMA iteração — sem atualização do modelo no laço | §2.1, p. 5012; Fig. 2, p. 5013 | Cap. 2: é a fonte que sustenta estender a seleção ativa até os exemplos do prompt |
| C2 | Demonstrações semanticamente similares ao exemplo de teste superam todos os demais métodos por margem larga, em todas as famílias e tamanhos de modelo | Resumo, p. 5011; §4, p. 5014; Conclusão, p. 5019 | Cap. 2: mostra que a seleção importa mais que o tamanho do modelo em classificação |
| C3 | Amostragem por incerteza, das mais fortes no aprendizado ativo supervisionado, tem o PIOR desempenho no aprendizado em contexto | §4, p. 5014; §5.5, p. 5017; Conclusão, p. 5019 | Cap. 2/6: limite declarado — o que vale no laço com classificador treinado não se transfere para o prompt |
| C4 | O ranking dos métodos DEPENDE da métrica: com F1 vence a similaridade, seguida da diversidade; com acurácia a diversidade passa à frente, seguida de similaridade e aleatória | §5.5 e Fig. 8, p. 5017 (a figura aparece na p. 5018) | Cap. 3/5: apoio externo a reportar acurácia e Macro F1 lado a lado; ecoa o caso E3′ (braço melhor em Macro F1 e pior em acurácia) |
| C5 | A diversidade é consistentemente a segunda melhor, o que os autores leem como sinal de que diversidade é característica de boas demonstrações | §4, p. 5014 | Cap. 2: sustenta o valor de cobertura/diversidade também fora do laço clássico |
| C6 | A seleção por similaridade tem um custo estrutural: cada exemplo de teste recebe um prompt diferente, porque os k vizinhos mudam — ao contrário das outras, em que os rótulos adquiridos servem a qualquer consulta | §2.2, p. 5014 | Cap. 3: argumento de custo operacional; no nosso cenário de lote isso multiplicaria chamadas |
| C7 | Trocar os rótulos verdadeiros das demonstrações por rótulos aleatórios degrada significativamente a similaridade, o melhor método | §5.2, referida na p. 5017 | Cap. 5: reforça que a QUALIDADE do rótulo do oráculo importa, não só quais itens entram |

## Números que posso citar
- 15 modelos avaliados, de **125 milhões a 30 bilhões** de parâmetros: 8 da
  família GPT e 7 da OPT (§3, p. 5014; Limitações, p. 5019).
- **15 tarefas de classificação e 9 de múltipla escolha**, do benchmark
  CrossFit (§3, p. 5014) — as "24 tarefas" do resumo.
- **k = 16 demonstrações** por prompt, salvo indicação em contrário (§3, p. 5014).
- Seleção por diversidade: agrupamento k-médias sobre embeddings do
  Sentence-BERT, escolhendo **um ponto por grupo**, com número de grupos igual
  a k (§2.2, p. 5013).
- Seleção por incerteza: usa **perplexidade** do prompt como escore, porque um
  modelo sem camada de classificação ajustada não permite entropia máxima nem
  menor confiança (§2.2, p. 5013).

## Citações diretas (com página)
> "uncertainty sampling, despite its success in conventional supervised
> learning AL scenarios, performs poorly in in-context learning" (Resumo, p. 5011)

> "This disparity highlights the potential for misconceptions or obscured
> findings, underscoring the need for caution when evaluating and comparing
> different methods" (§5.5, p. 5017)

## Crítica / limitações (minha leitura)
- **Uma iteração só, por construção.** Os autores são explícitos: como o modelo
  não é atualizado, múltiplas iterações não fariam sentido no desenho deles
  (Limitações, p. 5019). Ou seja, o trabalho NÃO é sobre o laço iterativo que a
  tese executa — é sobre a montagem do prompt. Citar como vizinho, não como
  concorrente do DRI-SL.
- **Só inglês** e só o CrossFit (Limitações, p. 5019). Nada garante o
  comportamento em português, muito menos em texto curto de varejo com cauda
  longa de 714 classes.
- **Sem custo em dinheiro ou tokens.** A comparação é por desempenho; o preço
  de recuperar vizinhos por exemplo de teste (C6) aparece como limitação
  qualitativa, não como conta.
- O oráculo ali é humano e o rótulo é dado; não há o problema, central na
  tese, de o próprio anotador errar de forma estruturada.

## Ideias que gera para a tese
- O C4 é o achado mais aproveitável: um trabalho externo, publicado em venue
  forte, mostrando que a escolha da métrica inverte o pódio. Serve de apoio
  independente à decisão da tese de reportar acurácia e Macro F1 juntos e de
  descrever o veredito cláusula a cláusula, em vez de eleger um número único.
- O contraste C2 × C3 sugere uma leitura para o Cap. 6: incerteza é boa para
  decidir O QUE ROTULAR, e ruim para decidir O QUE MOSTRAR ao modelo — são
  perguntas diferentes, e confundi-las é o erro que este artigo documenta.
