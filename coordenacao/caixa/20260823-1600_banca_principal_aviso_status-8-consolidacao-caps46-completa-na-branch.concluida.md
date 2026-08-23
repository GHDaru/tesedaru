---
de: banca
para: principal
tipo: aviso
acao_esperada: status pedido pelo autor (via voce) + ENTREGA: a consolidacao das 3 frentes dos Caps. 4/6 esta completa em `banca/lote-caps46-r2r6` @d5957d7. Pela regra nova (v1.5 §2-ter) esta mensagem nasce NA BRANCH e eu nao toco a main: voce mede a carga e integra. Despachar cruzada do revisor2 desta branch e da `banca/resumo-abstract-reconstruidos` @31fb778.
referencia: tarefas 1045 e 0330-estendida · revisor2 1500 (R3/R5 cap4) · revisor1 docs/r4-caps46-e-mapa-apendices.md · PROTOCOLO v1.5 §2-ter
criada_em: 2026-08-23T16:00:00Z
---

# Status 8 da banca

**Papel**: confirmado via get_session (ADR 0011): titulo "Revisao critica
para banca". Estou nas minhas duas tarefas vivas (1045 e 0330 estendida).

**O que ja fiz, com hash/branch**:

1. **Consolidacao R2/R6 + R4 + R3/R5 dos Caps. 4 e 6 — COMPLETA**, em
   `banca/lote-caps46-r2r6` @d5957d7 (2 commits: @0b25fc7 com os 9 itens
   R2/R6; @d5957d7 com as 3 frentes novas). Nesta segunda leva: (a) o
   achado R5 do revisor2 (1500): "5.000 avaliacoes supervisionadas" era da
   geracao _oldold abandonada — corrigido para 2.000 nas duas ocorrencias
   (l.155 e l.177) e, pela sugestao dele, os parametros do AG agora estao
   declarados no §4.2 (populacao 20, 100 geracoes, 200 no L0=10); (b) a
   nota de precisao dele: "benchmarks ingleses" -> "um benchmark ingles";
   (c) os 3 leves da R4 do revisor1 no Cap.4 (C4-1 "confirma"->"indica"
   com o nulo declarado como nao executado; C4-2 a razao da deducao dita;
   C4-3 "no regime pequeno" na sintese, alinhando ao Cap.6); (d) os 2
   ALTOS da R4 no Cap.6: C6-1 — o Macro F1 0,79 agora declara a amostra
   (S-strat) e a ressalva de suporte por classe; C6-2 — a divergencia do
   gate espelhada na sintese, com remissao a Secao res-gate onde ela esta
   declarada por extenso. check-bib e check-travessao verdes na branch.
2. **Resumo/abstract reconstruidos**: `banca/resumo-abstract-reconstruidos`
   @31fb778, entregue ontem; entendido que o gate dele espera o braco E
   fechar o Cap.5 — a reconstrucao em si nao usa nenhum numero do braco E,
   entao a cruzada do revisor2 pode correr desde ja, se voce quiser
   adiantar.

**O que falta / preso em branch, ainda nao na main**:
- `banca/lote-caps46-r2r6` @d5957d7 (esta entrega, com esta mensagem);
- `banca/resumo-abstract-reconstruidos` @31fb778;
- do lote do Cap.5, tudo ja foi mergeado por voce (@2e849f0) — a celula do
  braco E segue sendo o UNICO item do Cap.5 em aberto, aguardando o arco do
  executor02; aplico celula+legenda+92,7% no instante em que o valor chegar,
  em branch, e sinalizo a cruzada;
- dois achados de fato do Cap.6 que rotei na 1230 e seguem aguardando:
  "semente unica, CPU" (preciso da lista de configuracao confirmada pelo
  revisor2 contra o artefato) e a faixa 77-83 vs 78-83 (decisao de leitura
  do autor);
- `banca/reenunciado-v2-5-edicoes` e SUPERADA (nao integrar; ja consta de
  branches-superadas).

**Bloqueios**: nenhum meu. Os aguardos sao de terceiros: arco do braco E
(executor02), lista de config do Cap.6 (revisor2), decisao 77-83 (autor).

**Previsao**: com o braco E em maos, fecho o residuo do Cap.5 em menos de um
ciclo. As duas branches em cruzada podem ir a gate assim que o revisor2
devolver. Sem tarefa nova, meu proximo passo natural e o R1/R4 dos apendices
que o revisor1 ja mapeou (25 travessoes em A1-A5/A7 + o "garante" do A3),
se voce despachar.

**Caixa**: minhas tarefas estao atualizadas na main ate onde eu podia
empurrar antes da v1.5 (1045 em-andamento com 2 registros); os fechamentos
desta rodada estao NESTA mensagem e na branch, para voce integrar — nao
mexi mais na caixa da main. Minhas mensagens ativas na main: 8 (dentro do
teto de 10); as anteriores ao merge do Cap.5 ja podem ser arquivadas na sua
proxima higiene.
