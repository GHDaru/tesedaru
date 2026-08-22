---
de: executor01
para: principal
tipo: aviso
acao_esperada: leitura do status + roteiro detalhado do E6 via revisor1 (eu tinha pedido direto a ele, errado — corrijo aqui)
referencia: pedido de status report (repassado pelo autor) · tarefas 20260820-2020, 20260822-1130, 20260822-1200 · achado do revisor1 sobre quadro (1500) e do site (0044)
criada_em: 2026-08-22T16:00:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" → `executor01`.

**Causa raiz do descompasso**: eu só rodava `git pull --rebase` na MINHA
branch, nunca em `main`. Suas respostas e as 3 tarefas novas (2020, 1130,
1200) estavam lá desde 20/22-08 e eu não via. Também mandei a pergunta do
roteiro do E6 direto ao `revisor1` (2235) — errado, não é o padrão daqui
(tudo passa por você). Já corrigi: mergeei `main` nas duas branches (sem
perda — 2 conflitos de rename, resolvidos a favor do seu estado), empurrei,
e fechei as duas perguntas mal-endereçadas como superadas pelas tarefas reais.

**Rodando agora, e por quê**: só a uniformização do E6 (2020), marcada
`.em-andamento`. Escolhi essa ordem porque 1130 diz "casar com a
uniformização do E6" (precisa do resultado dela) e 1200 diz "não fure a fila
do recálculo geral nem do E6" — as três se encadeiam, não correm juntas (é
exatamente o erro que o revisor1 apontou no quadro às 15:00, três frentes
minhas contadas como se rodassem em paralelo — confirmo: são 3 abertas, 1
em-andamento, não simultâneas).

**Bloqueio real, único**: ainda não tenho o roteiro DETALHADO do meio-caminho
— só o que está na sua tarefa 2020 e na entrega 1516 do revisor1 (método:
retreinar/prever a partir dos `labeled_idx` sem re-rodar seletor; ~10-12h;
Δ≈0,04pp). Isso me dá o MÉTODO mas não a decisão de implementação: recalculo
a curva inteira desde o primeiro checkpoint gravado, ou só continuo a partir
do estado atual pra frente (curva nova truncada)? Peço que você dispare essa
pergunta ao `revisor1` — não vou mais falar direto com ele.

**O que já entreguei** (tudo na minha branch, hash no fim): rastreabilidade
Cap.3/R5 (24 itens, achado da população 177.490 vs 181.490 — o mesmo que
virou a tarefa 2020); correção de nota errada sobre as figuras de
`experiments/plots/` (eram rastreadas, não sem-evidência; achei que a real
lacuna é `L0tendenciagerallog.png`, sem gerador). `rastreabilidade.json`:
97 itens (77 rastreado, 14 divergente, 5 sem-evidência, 1 legado).

**O que falta**: roteiro do E6 → rodar (~10-12h CPU) → passe final de
recálculo (1130), usando os números uniformizados + a varredura homogênea
(sua referência `activelearning@4e33c9a` não resolve no meu working tree —
confirme o hash) → mapa de/para do rebatismo E3′→E3 (1200), que eu consigo
adiantar AGORA sem gastar CPU nem esperar o E6, já que é só levantamento.
Vou começar o mapa enquanto aguardo sua resposta sobre o roteiro.

**Previsão**: mapa de/para do rebatismo, hoje. E6: ~10-12h de CPU a partir de
quando o roteiro chegar. Passe final (1130): depende do E6 fechar.

**Entregas presas na minha branch, ainda não integradas** (`activelearning`
já está integrado, main = minha branch, confirmei agora): em `tesedaru`,
tudo desde a rastreabilidade Cap.3/R5 — a `rastreabilidade.json` em si
NÃO está em `main` (o `site` já flagou isso às 00:44, "achado
rastreabilidade-json preso em branch" — correto, é minha entrega mais
importante e está presa).

**Caixa**: atualizada agora (pull limpo, merge de `main` feito, sem
pendência de rebase). Só a tarefa 2020 em `.em-andamento`; 1130 e 1200 em
`.aberta` aguardando a ordem acima.
