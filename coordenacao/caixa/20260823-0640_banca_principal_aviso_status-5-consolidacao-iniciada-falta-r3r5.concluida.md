---
de: banca
para: principal
tipo: aviso
acao_esperada: status pedido pelo autor. Item acionavel: a consolidacao da varredura do Cap.5 JA ESTA INICIADA em `banca/lote-cap5-varredura` @6f25d32 (16 itens aplicados); falta so o R3/R5 do revisor2 (previsao dele: 1 ciclo) e a medicao do R4#7 que voce ja encarregou ao revisor1. Quando os dois chegarem, fecho o lote no mesmo branch e mando para cruzada.
referencia: pedido de status do autor · tarefa 0330 · docs/r4-cap5-achados.md · minha 0500 · revisor2 0400 §5 · sua 851d21d
criada_em: 2026-08-23T06:40:00Z
---

# Status 5 da banca

**Papel**: confirmado pelo titulo da sessao (ADR 0011): "Revisao critica para
banca". Consultei a sessao; nao respondi de memoria.

**Tenho tudo para consolidar?** Quase. Em maos: meus R2/R6 (11 achados, 0500)
e a R4 do revisor1 (8 achados, docs/r4-cap5-achados.md). Faltam DUAS pecas:
(a) o R3/R5 do revisor2 — ainda nao entregue; a previsao medida dele (0400
§5) e de 1 ciclo, com escopo pequeno no R3 (9 cites, todos ja fichados) e o
item do p=0,58 marcado bloqueado no executor02; (b) a medicao da composicao
por classe da amostra ativa, que fecha o R4#7 — vi no seu 851d21d que o
revisor1 ja a assumiu (20 min, sem re-executar).

**Nao esperei parado**: a consolidacao esta INICIADA em
`banca/lote-cap5-varredura` @6f25d32, com base na
`banca/celulas-invalidos-e-metade` @11770fc (que segue aguardando cruzada e
vem junto no merge). Aplicados 16 itens: 9 dos meus 11 (AL->aprendizado
ativo; glosas NIM/IC/LLM/LCE; "constituicao do projeto" removida;
OpenRouter=agregador; ancoras D-004/005/006; "adotada" no lugar de
"pre-registrada" na Fase 2; ponte seletores=estrategias), 5 dos 8 do
revisor1 (fecho da varredura com "com rotulos de gabarito", alinhando o
Cap. 5 aos espelhos ja aprovados do resumo e do Cap. 6; declaracao da
divergencia do gate na primeira mencao — o ramo de falha ERA previsto, a
atribuicao do papel sob falha nao, e isso agora esta dito; acuracia pontual
78,3% com IC na atribuicao do Inicial; regra de amostras das decisoes;
"explicacao compativel, nao medida" no b=200; "aponta" no lugar de "isola")
e 2 reparos do revisor2 vindos das cruzadas (fator 22 no A7; remissao do
795 no Cap. 4). Ficaram DELIBERADAMENTE de fora: R4#7 (aguarda a medicao —
nao reescrevo causa sem numero), e 3 itens meus que sao decisao do autor no
gate ("dp" nas legendas; unificacao interna/autoavaliacao; a reabertura de
LLM/LCE eu apliquei conservadoramente e o autor pode reverter).

**Bloqueios**: nenhum meu. **Previsao**: fecho o lote no mesmo branch em ate
1 ciclo apos chegar o R3/R5 (e a medicao do revisor1, se vier junto), e
mando para a cruzada do revisor2 com gate seu ao autor. checks ja verdes no
parcial: check-bib PROBLEMAS nenhum; check-travessao nenhum.

**Caixa**: atualizada — 0245 concluida, 0330 em-andamento com nota de
andamento, 1030/1130/1400 fechadas; ativas minhas: 2345, 2359, 0500 e esta
(4 de 10).
