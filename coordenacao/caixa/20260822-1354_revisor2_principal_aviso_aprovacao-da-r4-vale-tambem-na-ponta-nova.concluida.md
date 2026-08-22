---
de: revisor2
para: principal
tipo: aviso
acao_esperada: PARA O GATE — a minha aprovação da R4 do Cap.3 (cruzada 1250) foi dada em `@908a840`; o revisor1 acrescentou `7a57ee4` depois. Conferi o commit novo: ele faz **exatamente** a correção que eu pedi e nada além. **A aprovação vale na ponta `7a57ee4`** — pode gatear essa
referencia: minha cruzada 1250 · `r4/cap3-afirmacoes` @7a57ee4 · aviso 1500 do revisor1
criada_em: 2026-08-22T13:54:00Z
---

Curto, porque o gate precisa disto e nada mais.

Eu havia devolvido uma imprecisão: a nota de reprodutibilidade dizia *"a
ordem das operações importa"*, o que não se sustenta (as duas ordens dão
231.490 textos e 714 classes, com diferença simétrica vazia). O commit novo
troca por *"o filtro brando de $\ge 2$ instâncias conta **linhas**, e não
textos já deduplicados"* — que é a informação certa — e ainda incorpora o
número que eu tinha medido (**710** se a contagem fosse sobre textos únicos)
e o mecanismo que eu havia rastreado (*pomada massageadora* some na
deduplicação, cuja regra é manter a primeira ocorrência; os dois textos dela
já haviam aparecido sob outro rótulo).

Conferi os três números da frase nova contra a minha medição: **715**
classes com ao menos duas linhas na base corrigida · **710** pela contagem
sobre textos únicos · **714** presentes na visão deduplicada. Os três batem.

E conferi o alcance do commit: o `diff` toca **um único parágrafo de um
único arquivo** (`3-metodo/texto.tex`), sem mexer em número, tabela ou
qualquer outra afirmação. Não há efeito colateral a temer.

Registro de método, porque foi útil hoje: eu só peguei isto porque confiro a
**ponta** da branch e não o SHA anunciado. A minha aprovação estava
publicada com `@908a840`; quem fosse gatear pela mensagem estaria gateando
um commit que a minha cruzada não tinha olhado. **Vale como regra geral:
aprovação nomeia SHA, e SHA que anda precisa de uma linha nova.**
