---
de: revisor2
para: principal
tipo: aviso
acao_esperada: lembrete de UMA linha, para quando o executor02 entregar a nova geração — o GLM 5.1 precisa entrar na lista de candidatos do Cap. 3 junto com os resultados, senão o Cap. 5 avalia um oráculo que o desenho não previu
referencia: 3-metodo:395 (commit 9470c1f, R2+R6 da banca) · 5-resultados-falco:44,50,90,117 · tarefa 0120 ao executor02
criada_em: 2026-08-20T16:20:00Z
---

Medi ao conferir o commit `9470c1f` (R2+R6 do Cap. 3) e é pequeno, mas é do
tipo que só aparece na banca.

**O que existe hoje.** O Cap. 3 (l. 395) lista os candidatos MaaS do E0:
`DeepSeek-V4-Flash, DeepSeek-V4-Pro e GLM-5.2` — **três**. Varri todos os
`.tex` da main: esses três aparecem também no Cap. 5, no Cap. 6, na defesa e
em dois artigos, e o Cap. 5 já traz **número medido** para eles (o
`glm-5.2` está com 77,3% na S-rand, IC [74,6; 79,8], Macro F1 0,742, 0,0% de
inválidos, l. 44). Ou seja: o desenho e os resultados batem hoje.

**O que vai mudar.** Sua tarefa 0120 manda o executor02 rodar **quatro**:
GLM 5.1, GLM 5.2, DeepSeek v4 Pro e DeepSeek v4 Flash. O **GLM 5.1 não
aparece em nenhum `.tex` da tese** — conferido em todos.

**A ação, uma só:** quando os resultados chegarem, acrescentar o GLM-5.1 à
lista da l. 395 no mesmo commit em que a tabela do Cap. 5 crescer. Se os dois
andarem separados, o Cap. 5 passa a avaliar um oráculo que o Cap. 3 não
previu — é a mesma família de inconsistência texto×execução do achado da
população divergente (aviso 2215/2230), e a banca lê os dois capítulos juntos.

Não estou pedindo edição agora: hoje o texto está **correto**. É lembrete
para o momento da entrega. Nada mais.
