---
de: banca
para: principal
tipo: aviso
acao_esperada: status pedido pelo autor. Itens acionaveis para voce: (1) a branch `banca/lote-cap5-varredura` @33cc87c ja tem as 3 decisoes do autor + R3-3 aplicados; (2) para EU fechar o lote faltam duas entregas que estao com outros: o valor homogeneo do braco E (sua tarefa 0830 ao revisor2) e a medicao de composicao por classe (revisor1, seu 0700); (3) decida se o R5-3 (p=0,58, bloqueado no executor02) segura o lote ou fecha em passada propria — recomendo passada propria, para nao atrasar o Cap.5.
referencia: pedido de status do autor · tarefa 0330 · seus 0730/0800 · revisor2 0600 (R3/R5) e tarefa 0830 · revisor1 0640/seu 0700 · branch @33cc87c
criada_em: 2026-08-23T10:15:00Z
---

# Status 6 da banca

**Papel**: confirmado pelo titulo da sessao (ADR 0011): "Revisao critica para
banca". Consultei a sessao; nao respondi de memoria.

**O que JA esta na branch** (`banca/lote-cap5-varredura` @33cc87c, base
`celulas-invalidos-e-metade` @11770fc que vem junto no merge):

- os 16 itens do lote anterior (@6f25d32): 9 dos meus R2/R6 + 5 dos 8 da R4
  do revisor1 + 2 reparos do revisor2 das cruzadas;
- as 3 decisoes do autor (seu 0800): "dp" glosado como "desvio-padrao, dp"
  na primeira legenda que o usa; "interna/teste interno" unificado em
  "autoavaliacao" nas 7 ocorrencias do Cap.5 (os outros sentidos de
  "interna", como "divisao interna" e "controle interno", ficaram);
  reabertura LLM/LCE mantida como aplicada;
- do R3/R5 do revisor2 (0600): o R3-3 aplicado — a frase do colapso deixou
  de atribuir o fenomeno a uma literatura nao fichada e virou observacao
  deste experimento, na redacao que ele propos; o R5-2 ja estava resolvido
  na base da branch (celulas 0,7%/0,2%).

check-bib e check-travessao verdes na branch.

**O que ainda espera, e com quem esta**:

1. **Braco E homogeneo (R5-1, o grave)** — com o revisor2 (sua tarefa 0830).
   Quando o valor confirmado chegar, aplico: a celula da tab:e3p, o derivado
   da l.565 (92,0% vira 92,7% se ficar 0,8223) e a legenda, que hoje promete
   "media±desvio-padrao de tres sementes" — prometo ajusta-la ao que o valor
   final de fato for (tres sementes homogeneas se a s123 rodar, ou lacuna
   declarada, principio VI). Nao mexo antes do numero.
2. **Composicao por classe da amostra ativa (R4#7)** — com o revisor1 (seu
   0700). Fecha os dois "porque" do E6 com numero em vez de suposicao.
3. **R5-3 (p=0,58)** — bloqueado no executor02 (chave). Recomendo NAO
   segurar o lote por ele: fecha em passada propria quando a calibracao
   rodar.
4. Fora da minha superficie, so registro: R3-1/R3-2 (fichas Yuan/Kholodna,
   dos revisores) e o achado estrutural dos artefatos `_bs16v2` fora da
   main do `activelearning` (decisao sua/autor).

**Previsao**: com o braco E e a medicao em maos, fecho o lote em MENOS de um
ciclo (as edicoes ja estao desenhadas) e sinalizo na hora a cruzada final do
revisor2 sobre a branch inteira; depois, seu gate ao autor.

**Caixa**: atualizada — 0330 em-andamento com dois registros de andamento;
ativas minhas: 2345, 2359, 0500, 0640 e esta (5 de 10; arquivo as duas
primeiras no proximo ciclo de higiene, ja consolidadas pelos merges).
