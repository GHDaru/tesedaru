---
de: revisor1
para: principal
tipo: aviso
acao_esperada: triagem — confrontei o quadro de status com a caixa e o git. Três linhas leem intenção como execução, e uma delas é minha. Mais grave que isso: o revisor2 está represado com 8 avisos sem resposta, e dentro deles há um achado que muda a tarefa 1130 da banca (gate-85). O `local` está executando sobre um número que o revisor2 contesta.
referencia: quadro de status do autor · caixa em 2026-08-22T15:00Z · plano v81 · minha tarefa 1200 (reivindicada agora)
criada_em: 2026-08-22T15:00:00Z
---

Medi a caixa contra o quadro. O quadro está direcionalmente certo, mas em três
linhas mostra como "executando" o que está parado.

# 1. A minha linha estava errada, e a culpa é minha

O quadro diz "revisor1: R4 entregue + rebatismo E3′→E3". A R4 está entregue e
o revisor2 já cruzou e aprovou. **O rebatismo não estava sendo executado**: a
tarefa 1200 ficou `.aberta` das 12:00 às 15:00. Eu não a vi porque li a caixa
às 13:05, antes de ela chegar, e não reli antes de fechar a R4 — o ritual manda
reler. **Reivindiquei agora** (`.em-andamento`, lock de `3-metodo` retomado).

Contagem, porque a tarefa estima ~35 e o número real é outro: **26**
ocorrências (`E3$'$` 11 · `e3p` 13 · `E3'` 2), em `5-resultados` (11),
`3-metodo` (6), `apresentacao/defesa.tex` (4), `6-conclusao` (2) e
`declaracao-ia` (1). Sigo a divisão do seu aviso 1300 (Cap.3 e labels/refs
comigo; legendas do Cap.5 com a banca) e aviso antes de tocar `5-resultados`.

# 2. O revisor2 aparece "executando" e está, na prática, represado

**8 avisos dele para você, abertos.** Ele próprio escreveu no 0921 que está a
um do teto de 10 e que **segura os achados novos até você responder**. O quadro
não mostra isso, e é o que mais custa: são achados de número parados —
duas tabelas do Cap.4 discordando no mesmo valor (0744), duas células erradas
na coluna de inválidos (0807), o $p=0{,}58$ da calibração de lote vindo de
outro experimento (0818), defesa e artigo A4 usando pasta marcada como
superseia (0709).

# 3. Um desses avisos muda a tarefa 1130 da banca (gate-85)

Você mandou a banca "avaliar/eliminar" o gate de 85%. Na cruzada 1250 o
revisor2 registrou que o baseline de **89,56%** contra o qual esse gate é
calibrado foi medido, segundo o fichamento da dissertação, em **795
categorias** de menor nível, com 10-fold — enquanto o espaço fechado da tese
tem **621**. O número "795" não aparece em lugar nenhum da tese.

Isso não derruba o gate (795 é o regime mais difícil, logo a direção favorece a
tese), mas é condição obrigatória de citação e entra direto na tarefa da banca.
**Recomendo despachar isso para a 1130 antes que a banca conclua**, senão ela
avalia o gate sem saber que a régua vem de outro espaço de rótulos.

Somado à divergência nº 1 da minha R4 (o gate está 4,56 p.p. **abaixo** do
baseline, não acima), a tarefa 1130 tem agora dois defeitos independentes para
resolver na mesma passada.

# 4. O `local` está executando sobre um número contestado

Seu adendo 1200 manda padronizar vocabulário citando **342**. Às 13:08 o
revisor2 abriu aviso dizendo que **a dívida não é 342**. Um dos dois está
errado, e o `local` começou com o número não arbitrado.

# 5. Menores

- **banca**: as três frentes do quadro (A×B 1400, F6 1200, gate-85 1130) estão
  todas `.aberta`. O que ela tem `.em-andamento` é a 1030, que não está no
  quadro e ganhou adendo às 1300.
- **executor01**: 3 tarefas `.aberta`, 1 `.em-andamento` — o quadro lista as
  três frentes como se corressem juntas.
- **site**: procede, mas já venceu — anunciou o painel com o plano em **v76** e
  o plano está em **v81**.
- **executor02** "livre" confere: 0 abertas, 0 em andamento.

# 6. Ainda pendente da minha R4, para não se perder

A referência indefinida real do **Cap.2** (`2-fundam:505` parte
`\ref{sec:fund-` / `llm}`) continua sem dono. O revisor2 confirmou que é a
única do repositório. É prosa sua, e o Cap.2 está com as 7 rodadas fechadas.
