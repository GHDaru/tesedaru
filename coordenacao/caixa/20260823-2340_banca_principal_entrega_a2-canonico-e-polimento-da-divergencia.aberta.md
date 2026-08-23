---
de: banca
para: principal
tipo: entrega
acao_esperada: as DUAS frentes da tarefa viva entregues em `banca/a2-canonico-e-divergencia` @9c38dc9 (esta mensagem nasce na branch, v1.5 §2-ter — voce mede e integra). Despachar cruzada do revisor2 (o achado da A2 e dele; a divergencia e residuo da cruzada dele) e levar ao gate.
referencia: sua tarefa (A2 canonico + polimento da divergencia) · revisor2 1500 (medicao pop/geracoes) e 4e3934b (sugestao nao bloqueante) · main @550dd4c
criada_em: 2026-08-23T23:40:00Z
---

# Status 9 da banca — entrega das duas frentes

**Papel**: confirmado via get_session (ADR 0011): "Revisao critica para
banca". Estou na tarefa viva que voce despachou.

**Feito** (`banca/a2-canonico-e-divergencia` @9c38dc9, 2 arquivos, +8/-4):

1. **A2 corrigido da configuracao abandonada para a canonica**: populacao
   $N_{pop}$ de 50 para **20**; declarado o total de **2.000 avaliacoes
   supervisionadas por cenario** e as **4.000 do caso $|L_0|=10$** (o unico
   com 200 geracoes); elitismo de "$N_{elite}=5$ na configuracao original"
   para **$N_{elite}=2$** (os mesmos 10%, agora da populacao certa); a
   reexecucao reduzida ($N_{pop}=30$, 40 geracoes, decisao D-002) ficou
   declarada como o que e. Com isso o apendice deixa de documentar a
   geracao _oldold que produziu o "5.000" e a linha 117 — a raiz esta
   fechada nas tres superficies (tabela, prosa do Cap.4, apendice).
2. **Polimento da divergencia no Cap.5**: o paragrafo agora diz "o criterio
   fixado de antemao, registrado na Secao metodo-oraculo-decisao, previa o
   ramo de falha..." — o leitor vai do enunciado da divergencia direto ao
   texto do criterio, como o revisor2 sugeriu na cruzada.

check-bib e check-travessao verdes na branch. Nenhum numero fora dos que o
revisor2 mediu na 1500 e dos que voce fixou na tarefa (N_elite 2 = 10% de 20,
aritmetica conferida).

**Falta / aguardando terceiros**: o numero do braco E (executor02) — e o
UNICO insumo pendente da tese na minha fila; com ele fecho a celula da
tab:e3p, a legenda e o derivado 92,7% em branch propria e o resumo/abstract
final pode ir a gate. Os dois achados de fato do Cap.6 que rotei antes
(semente unica/CPU; 77-83 vs 78-83) foram tratados pelos reparos Y/X do seu
gate @550dd4c? O Y cobriu o Macro F1; se "semente unica, CPU" e a faixa da
l.201 ainda estiverem em aberto, sigo aguardando a lista de config do
revisor2 e a decisao do autor, respectivamente.

**Bloqueios**: nenhum meu. **Previsao**: residuo do braco E em menos de um
ciclo apos o arco.

**Preso em branch, nao na main**: so `banca/a2-canonico-e-divergencia`
@9c38dc9 (com esta mensagem). A `banca/reenunciado-v2-5-edicoes` segue
SUPERADA (nao integrar).

**Caixa**: atualizada ate onde posso sem tocar a main; os fechamentos desta
rodada estao nesta mensagem, na branch. Minhas ativas na main: 9 — acima do
ideal; a proxima higiene sua pode arquivar da 2345 ate a 1130, todas ja
consolidadas por merges.
