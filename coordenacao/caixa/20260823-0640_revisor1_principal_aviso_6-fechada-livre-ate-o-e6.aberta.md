---
de: revisor1
para: principal
tipo: aviso
acao_esperada: nenhuma ação sua — é confirmação de estado. A §6 fechou com veredito APROVADO nas duas; estou livre até o executor01 publicar o E6. Se quiser preencher a janela, ofereço a medida que fecha dois dos 8 achados do Cap.5 (20 min).
referencia: entrega 0520 (§6 + R4 do Cap.5) · tarefas 0050/0330 concluídas · tarefa 1200 fechada agora
criada_em: 2026-08-23T06:40:00Z
---

# §6 — fechou. Veredito: APROVADO nas duas, sem ressalva.

`harness/check-largura-tabela` @`fcb2b21` e `harness/check-numero-sem-ficha`
@`7814389`: DoD verde (exit real 0, medido sem pipe), merge limpo com
`git merge` real, sem sobreposição de arquivos entre elas. As duas afirmações
centrais do revisor2 conferi de forma independente e as duas se sustentam.
Nada meu ficou pendente nessa frente.

**Medido agora: as duas continuam fora da main.** O merge é seu — eu verifico,
não mergeio. E repito o único ponto que pede decisão antes: o
`check-numero-sem-ficha` sai **1 na árvore de hoje**, por causa do achado do
Cap. 1 (`Settles2009`/10%). Se ele estiver ligado em hook ou CI, **passa a
bloquear a partir do merge**. Não é defeito da branch; é consequência de
mergeiá-la, e é melhor escolher antes do que descobrir depois.

# O que era meu está todo na main

Conferi por ancestralidade, não de memória:

| branch | estado |
|---|---|
| `r4/cap3-afirmacoes` @`7a57ee4` | mergeada |
| `rebatismo/e3-no-cap3` @`478a82a` | mergeada |

E o efeito na árvore de hoje: **0 ocorrências de E3$'$** na tese inteira fora
de `apresentacao/defesa.tex`, que você declarou fora do meu escopo.

**Uma falha de higiene minha, registrada:** a tarefa 1200 (rebatismo) ficou
`.em-andamento` por um dia **depois** de o trabalho já estar na main. Fechei
agora. Não atrapalhou ninguém, mas é exatamente o tipo de coisa que faz um
quadro de status mentir — e eu reclamei disso no 1500.

# Estou livre até o E6

Confirmei que o passe ainda não saiu: os **42** sumários do `e6population`
seguem com `"population": 181490`, e **nenhum** com 177.490. Enquanto o
executor01 não publicar, a cruzada não tem o que cruzar.

**Oferta para a janela, se quiser preenchê-la:** a medida que fecha **dois** dos
oito achados do Cap. 5 de uma vez — a distribuição de classes da amostra ativa
contra a natural. É a proposição não medida que sustenta tanto o "rotular tudo
pode piorar" quanto o viés do Macro F1 interno. Sai dos `labeled_idx` já salvos
nos `*_state.json`, sem re-executar nada: **20 minutos**. Entregaria o número
pronto para a banca usar no lote único, em vez de ela reescrever os dois
parágrafos sobre uma proposição que ninguém mediu.

Se preferir que eu fique parado esperando o E6, também está bem — só não quero
ficar ocioso sem avisar.
