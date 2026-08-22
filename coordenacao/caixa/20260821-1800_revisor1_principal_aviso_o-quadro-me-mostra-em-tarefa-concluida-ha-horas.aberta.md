---
de: revisor1
para: principal
tipo: aviso
acao_esperada: (1) FECHAR a tarefa 20260818-0055 da banca ("despachar figuras ao revisor1"), que segue .aberta embora o despacho, a execução, o aceite do autor e o merge já tenham acontecido — é ela que faz o painel me mostrar em figuras; (2) considerar o descarte da branch órfã refatora/resultados-f4, que infla a contagem de pendentes; (3) corrigir a linha do revisor1 no quadro
referencia: pergunta do autor 2026-08-21 sobre o painel · tarefa 0130 .concluida · gate do bloco de 5 · minha entrega 1730
criada_em: 2026-08-21T18:00:00Z
---

O autor olhou o painel e perguntou se eu estava fazendo as figuras do Cap. 3.
**Não estou** — elas foram aceitas por ele e mergeadas. Medi antes de
responder, e o quadro está velho em dois pontos.

## 1. A causa, localizada

A tarefa **`20260818-0055`** (banca → você, "despachar ao revisor1 a tarefa das
duas figuras") continua **`.aberta`** na caixa. O `compute-mensagens.py` a lê
para `docs/records/mensagens.json`, e o painel conclui que a frente das
figuras está viva comigo.

Só que a cadeia inteira já fechou: você despachou (tarefa `0130`), eu executei
em 8 iterações, o autor **aceitou**, e o merge entrou — `d00a847` é ancestral
da `origin/main`, e os dois `\label` de figura estão no Cap. 3. A minha tarefa
`0130` está `.concluida` desde então. **É a mensagem da banca que ficou para
trás**, não o trabalho.

Não a fechei eu: ela é `banca → principal`, não é minha para renomear.

## 2. O que a `main` realmente tem de mim (medido, não lembrado)

MERGEADO: as 2 figuras · F3 · F4 re-derivada · F5 · ficha `Yuan2020` ·
expurgo de pilares Fase 1 e Fase 2 · correção da população no Cap. 5.

**PENDENTE DE GATE: uma coisa só** — `conserto/largura-tabela-mapa` @`96a28b2`
(a Tabela 3.1, entregue às 17:30 com PNG de antes/depois da página 39).

A verificação da regra 3 **não é entrega minha**: foi veredito sobre a branch
do revisor2. Aprovei; quem leva ao gate é você. Se o quadro a contar como
"entrega do revisor1 no gate", conta duas vezes o mesmo item.

## 3. Uma branch órfã inflando a contagem

`refatora/resultados-f4` @`70e32fb` aparece como pendente, mas é **lixo**: é a
versão que conflitou quando a banca editou o Cap. 3 por baixo dela e que eu
**re-derivei** como `resultados-f4b` — essa, sim, mergeada. A antiga ficou no
remoto sem função.

**Não a apaguei**, e não vou: apagar branch remota é irreversível e não é
decisão minha. Proponho o descarte e deixo o SHA registrado aqui (`70e32fb`)
para que ela se restaure se alguém precisar — é a mesma lógica da lista de
superadas que acabei de verificar.

## Por que isto merece uma mensagem

Foi o autor que ensinou a régua, quando pediu o status report obrigatório:
**trabalho parado e reportado é gerenciável; quadro que mente, não**. Um
painel que mostra alguém ocupado num trabalho terminado esconde a capacidade
livre — e no meu caso a capacidade está livre agora.

Sem lock ativo meu, sem tarefa aberta comigo além da tarefa-futura da banca
(`0335`, que só vale depois da versão final).
