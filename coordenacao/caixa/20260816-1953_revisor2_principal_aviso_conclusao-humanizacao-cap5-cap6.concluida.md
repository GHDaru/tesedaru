---
de: revisor2
para: principal
tipo: aviso
acao_esperada: consolidar no bloco de gates e levar ao autor; decidir com ele o único ponto em aberto (pontuação do fecho do Cap. 6)
referencia: branches humanize/cap5 @ dea35da e humanize/cap6 @ 92dd951 · docs/criterio-humanizacao.md · tarefa 20260816-1938
criada_em: 2026-08-16T19:53:27Z
---
HUMANIZAÇÃO R1 DOS CAPS. 5 E 6 CONCLUÍDA. Uma branch por capítulo, commits por
lote temático. Nada foi para a main: toda a prosa está em branch, conforme a
regra do autor.

NÚMEROS
- Cap. 5: 64 travessões de prosa -> 0. Restam 6 no arquivo, todos preservações
  previstas pelo critério: 2 separadores de rótulo em legendas e 4 células de
  tabela que usam o travessão como marcador de "sem valor".
- Cap. 6: 40 -> 6, também todos previstos: 4 rótulos dos pilares (P1 — ... a
  P4 — ...) e 2 travessões de contraste ("não o ruído — e sim o critério").
- Conversões por grupo: G1 (anuncia lista) 3 · G2 (aposto) 19 · G3
  (explicativo) 24 · G4 (sujeito separado do verbo) 5.
- Fórmulas telegráficas do Cap. 5: "Três leituras." e "Dois achados." ganharam
  verbo; as outras quatro aberturas enumerativas já eram frases completas.

DOD EXECUTÁVEL (princípio IX). Em vez de afirmar que não mexi em conteúdo,
provei: o conjunto de números e o de comandos de citação de cada capítulo têm
hash md5 IDÊNTICO ao da main.

TRÊS EXEMPLOS REPRESENTATIVOS
1. G4, Cap. 5 (E6): a definição da DRI-SL-C ocupava um aposto de cinco linhas
   entre travessões, separando a lista de seletores do resto da frase; virou
   frase própria logo após a lista.
2. G3, Cap. 5 (E6): "...não é utilizável como estimativa de implantação — a
   justificativa empírica direta para o conjunto de validação" virou
   "...implantação: é a justificativa empírica direta para...".
3. G2, Cap. 6 (fecho): "A hipótese quantitativa central — >=95% ... via
   oráculo LLM — foi submetida" virou a mesma frase com parênteses.

PONTO EM ABERTO PARA O AUTOR. O fecho do Cap. 6 (tríade + aforismo) é decisão
dele e NÃO foi reescrito. Nele apliquei só pontuação: o travessão que anunciava
a tríade virou dois-pontos e dois apostos viraram parênteses, sem alterar uma
palavra nem a ordem delas. Se preferir o fecho intocado até na pontuação,
basta reverter esse trecho do commit 92dd951.

DOIS ACHADOS DE CONTEÚDO QUE NÃO CORRIGI (R1 é forma; ambos já constam do
plano como R5-IMEDIATO, registro por terem passado sob os meus olhos):
- Cap. 5, seção do E6: "população reservada (~140 mil instâncias)". O valor
  medido é 177.490 — provei isso no ciclo de dados do activelearning, com
  invariante executável.
- Cap. 5, desenho do E1: "8 sementes é o mínimo que permite p<0,05 no
  Wilcoxon" é falso; com 6 pares o Wilcoxon já atinge p=0,031.

Locks dos dois capítulos liberados neste mesmo commit.
