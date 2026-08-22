---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma — ciência; publicado direto (ADR 0010, site dispensa gate)
criada_em: 2026-08-22T00:53:00Z
referencia: ciclo 013 · specs/013-resultados-ux-cards-e-sumario/ · commit 9daad49
---
Pedido direto do autor logo após o ciclo 012 (link do notebook Kaggle):
"Chame especialista de uxui ao menos três para melhorar a entrega visual e
a usabilidade." Convoquei 3 pareceres independentes de novo (tabelas/design
de informação, visual/tipografia, usabilidade/interação) — mesmo ritual do
ciclo 011.

Dois dos três convergiram: a seção "Experimentos executados" nunca deveria
ter sido uma tabela — 7 experimentos com células de 2 a 400 caracteres na
mesma linha forçam rolagem horizontal, e foi exatamente essa rolagem que
escondeu a coluna de notebook Kaggle publicada no ciclo anterior, sem
nenhum aviso visual de que havia mais conteúdo.

Publicado:
- "Experimentos executados" virou grid de cards (mesmo padrão de
  "Entregas" já na página) — zero rolagem horizontal, em qualquer tela.
- O selo do notebook (verde "✓ notebook" quando existe, cinza "sem
  notebook" quando não) fica sempre visível no topo do card, nunca mais
  escondido — e ganhou `aria-label` com o id do experimento, para leitor de
  tela.
- Os dois pilares sem achado (P1, P2) deixaram de competir em peso visual
  com os pilares que têm achado real (P3, P4) — viraram uma linha
  tracejada compacta em vez de um card cheio vazio.
- A página ganhou um sumário no topo com as contagens reais (Achados,
  Entregas, Experimentos), útil já que ela deve crescer.

Testado (Playwright): claro/escuro, mobile 390px (zero rolagem horizontal
em qualquer lugar da página — era exatamente o defeito relatado), 8
páginas, 0 erros de console reais. Os 3 pareceres e a decisão consolidada
estão em `specs/013-resultados-ux-cards-e-sumario/ux-design.md`.
