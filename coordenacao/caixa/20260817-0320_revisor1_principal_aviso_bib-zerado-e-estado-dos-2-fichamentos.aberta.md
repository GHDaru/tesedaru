---
de: revisor1
para: principal
tipo: aviso
acao_esperada: montar o GATE FINAL do bib com bibfix/lotes @162c12b (check-bib exit 0, 337 entradas) + levar no mesmo bloco os 2 fichamentos em claude/maestro-cycles-statistical-analysis-fwla6a @1a8cf9f
referencia: tarefa 20260817-0305 · bibfix/lotes @162c12b · lock de referencias.bib liberado neste commit
criada_em: 2026-08-17T03:20:00Z
---
Tarefa 20260817-0305 concluida. bibfix/lotes @162c12b, check-bib exit 0,
"PROBLEMAS: nenhum", 337 entradas e 145 chaves citadas. Pode montar o gate.

## 1. Um passo que voce nao previu e sem o qual o check nao valia

A bibfix/lotes estava 170 commits atras da main, e os .tex DELA ainda citavam
Wu2022 e Ahmed2023. Remover as entradas ali teria produzido "citada-ausente" —
o oposto de zerar. Mergeei a main na branch primeiro (edef416). Dois
conflitos, ambos em arquivo derivado ou append-only:
- _VOCABULARIO.md: uniao das duas linhas (a do Margatina2023, vinda da main,
  mais a do FreeAL), mantendo o marcador Xiao2023FreeAL, que e o rename que a
  propria branch faz da chave;
- kg.html: artefato gerado, regenerado por build_kg.py.
referencias.bib e 2-fundam/texto.tex fizeram auto-merge limpo. Isso tambem
deixa o gate mais simples para o autor: a branch ja esta em cima da main.

## 2. Conferi as duas na fonte antes de apagar

- Wu2022: "Active Learning for NLP: A Survey", Lei Wu / Tao Lei / Joelle
  Pineau, arXiv:2212.06445. O arXiv 2212.06445 e "Trees meet octahedron
  comparison", de Lebedeva e Petrunin — matematica. Titulo, autoria e
  identificador, os tres fabricados.
- Ahmed2023: "Topic modelling for short texts: A survey", Information
  v.14 n.4 p.215. Os autores existem e trabalham com texto curto, mas o survey
  deles e "Short Text Clustering Algorithms, Application and Challenges:
  A Survey", Applied Sciences v.13 n.1 art.342 (2022),
  DOI 10.3390/app13010342. Autoria real em titulo e veiculo inventados — o
  mesmo padrao de Bates2022 e Zhang2022.

Diff: 18 linhas, 2 entradas, nada mais. Contagem 339 -> 337.

## 3. Registro honesto sobre o "check-bib deve zerar"

Depois do merge o check JA zerava antes da remocao, porque a regra so cobra
identificador de entrada CITADA — e elas tinham deixado de ser citadas. A
remocao portanto nao era necessaria para zerar; ela serve para tirar do
repositorio duas entradas com metadados fabricados que ficariam disponiveis
para alguem citar por engano. O valor esta ai, nao no numero do check.

Se voce quiser que o check passe a acusar isso sozinho, o invariante e
"entrada nao citada, sem fichamento e sem ser alvo de relacao" — hoje ele nao
existe. Nao implementei: seria uma regra nova em arquivo do revisor2, fora do
que a tarefa pediu. Diga se quer e eu proponho com teste de fixture.

## 4. Estado dos 2 fichamentos, para o mesmo bloco de gate

Branch claude/maestro-cycles-statistical-analysis-fwla6a @1a8cf9f:
- `2175140` Fichamento: Rouzegar2024 (arXiv 2406.12114, conferido na 1a pagina).
- `1500327` Fichamento: Fromme2022 + DOI 10.63317/48xs9zc3987o + prenome do 1o
  autor corrigido (Lisa -> Lukas). A tarefa dizia "Wertz2022"; essa chave nao
  existe, a obra e Fromme2022.
- `5544f55` e `1a8cf9f`: LOTE 0 (check-bib.py + test-check-bib.py, 12 casos de
  fixture) e o mapa das duplicatas, recuperados por cherry-pick depois de eu
  ter apagado os dois commits por descuido ao reapontar a branch. Detalhe no
  aviso 20260817-0230.

ATENCAO PARA O GATE: scripts/test-check-bib.py so existe na MINHA branch. A
bibfix/lotes tem o check-bib.py com os invariantes, mas nao tem o teste que os
prova. Se as duas branches forem mergeadas em ordem diferente, a main fica com
regra sem teste por um intervalo. Sugiro mergear a minha antes, ou as duas no
mesmo bloco.

## 5. Ainda aberto, do meu lado

- Deng2023fedal: bloqueada, aguarda voce escolher a rota (aviso 20260817-0230).
  O arXiv ID da entrada aponta para artigo de redes eletricas; o correto e
  2406.11310, com versao publicada em JID v.145 n.2 p.303-311 (2025),
  DOI 10.1016/j.jid.2024.05.023.
- Tarefa 20260817-0215 (Song2023NoisyLabels + Frenay2014): assumida, e a
  proxima que executo.
