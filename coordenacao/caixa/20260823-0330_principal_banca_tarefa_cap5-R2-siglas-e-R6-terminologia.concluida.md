---
de: principal
para: banca
tipo: tarefa
acao_esperada: varredura R2 (siglas) + R6 (terminologia) do Cap.5 (5-resultados-falco). MODO: audite e produza a lista de achados ao principal; VOCÊ tambem consolida e APLICA o lote das 3 frentes (suas + R3/R5 do revisor2 + R4 do revisor1) numa branch unica, para nao termos varias maos no mesmo arquivo. Cruzada do revisor2. Prioridade DEPOIS de fechar F6 e lote-2100 (que ja estao em cruzada).
referencia: varredura R2-R6 dos caps de resultado (decisao do autor) · Cap.5 ja com R1 feito e R5 em andamento · criterio-humanizacao.md (regua de siglas/terminologia)
criada_em: 2026-08-23T03:30:00Z
---

R2 (siglas): toda sigla na 1a ocorrencia do Cap.5 com extenso; consistencia
de RS/US/AL/MaaS/IC etc.; nada de sigla nova sem glosa. R6 (terminologia):
termos-chave usados de forma consistente (oraculo, seletor, regua, braco,
pool, populacao reservada, gate); sem sinonimos soltos que confundam.
Entregue os achados; depois eu te libero para consolidar o lote com os do
revisor2 (R3/R5) e revisor1 (R4) numa branch so. Nenhum numero muda em R2/R6.

## Andamento (banca, 2026-08-23, apos a liberacao do principal)

Auditoria R2/R6 entregue (minha 0500, 11 achados). Consolidacao INICIADA em
`banca/lote-cap5-varredura` @6f25d32 (base: banca/celulas-invalidos-e-metade,
para conter as celulas ja em cruzada): aplicados 9 dos meus 11 + 5 dos 8 da
R4 do revisor1 + 2 reparos do revisor2 vindos das cruzadas (fator 22 no A7;
remissao 795 no Cap.4). Pendentes para fechar: (a) R3/R5 do revisor2 (ainda
nao entregue; previsao dele: 1 ciclo); (b) R4#7 do revisor1, que exige medir
a composicao por classe da amostra ativa (labeled_idx nos *_state.json do
E6) antes de reescrever os dois "porque"; (c) 3 itens meus de decisao do
autor (reabertura LLM/LCE ja aplicada conservadoramente; "dp" nas legendas e
unificacao interna/autoavaliacao ficam para o gate). Fecho o lote no mesmo
branch quando o R3/R5 chegar.

## Andamento 2 (banca, 2026-08-23, apos R3/R5 e decisoes do autor)

Branch `banca/lote-cap5-varredura` avancou para @33cc87c: aplicadas as 3
decisoes do autor (dp glosado na 1a legenda; "interna/teste interno" ->
"autoavaliacao" em todo o Cap.5; reabertura LLM/LCE mantida) e o R3-3 do
revisor2 (frase do colapso reformulada como observacao deste experimento).
R5-2 ja estava resolvido na base da branch (celulas 0,7%/0,2%). Aguardam
para fechar: valor homogeneo do braco E (tarefa 0830 ao revisor2) + a frase
da l.565 (92,0%->92,7% se 0,8223); medicao de composicao por classe do
revisor1 (R4#7); R5-3 (p=0,58) segue bloqueado no executor02 e pode fechar
em passada propria se o autor preferir nao segurar o lote. R3-1/R3-2
(fichas) e o achado estrutural (_bs16v2 fora da main do activelearning) nao
sao superficie da banca.
