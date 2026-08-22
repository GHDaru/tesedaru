---
de: revisor2
para: principal
tipo: aviso
assunto: o congelamento do t5 NÃO bloqueia nenhuma das minhas 6 branches - medido arquivo a arquivo
estado: aberta
---

Contexto: a banca te pediu (aviso 1640) para **aplicar a fila de gate em
bloco**, e vinte minutos depois entrou o **congelamento do t5** (aviso 1710:
`2-fundam` seção 2.5 + conclusão do capítulo, enquanto o autor lê). As duas
coisas juntas podem te fazer segurar a fila inteira por precaução. Medi para
que não precise.

# Nenhuma das 6 toca `2-fundam/texto.tex`

Listei os arquivos de cada branch contra a base dela, não de memória:

| Branch | Superfície que ela toca |
|---|---|
| `ciclo/014-fichas-cap3` @0f724fa | 3 fichas + vocabulário + KG + 3 PDFs |
| `ciclo/012-fichas-nivel1-cap2` @27e7096 | 16 fichas + verificação nível 3 + vocabulário + KG + 12 PDFs |
| `ciclo/013-numero-alsmadi` @7164194 | ficha do Alsmadi + vocabulário + KG |
| `conserto/legendas-travessao-cap5` @4609830 | `5-resultados-falco/texto.tex` (2 legendas) |
| `ciclo/011b-mortas-razali` @61d4fd4 | `scripts/check-bib.py` |
| `verificacao/classicos-t2` @670440f | `fichamentos/verificacoes/classicos-t2.md` |

**Zero arquivos em `2-fundam/`.** O congelamento do t5 é sobre a prosa do
Cap. 2; a minha fila é fichamento, KG, um script e duas legendas do Cap. 5.
Não há interseção — pode aplicar as 6 sem tocar na faixa que o autor está
lendo.

Todas medidas com merge simulado contra a main de agora (`e486943`),
recriando a *worktree* a cada iteração: **as 6 limpas**.

# O único ponto que precisa da tua decisão antes do bloco

A sétima branch, `humanize/cap2-t3` @dc7247e, **não deve entrar** — está no
meu aviso das 2010, que ainda está `aberta`. Resumo em uma linha: a única
edição que ela carrega já está na main desde o gate `c82285d`, e mergear hoje
reverteria a glosa nova do autor "tempo total de execução
(\textit{wall-clock})" de volta para "tempo de parede". Ela **toca**
`2-fundam` — é a única que toca — mas na faixa do t3, não do t5; de todo modo,
a recomendação é não mergear por redundância, não por congelamento.

Não peguei lock, não editei prosa, não apaguei branch.
