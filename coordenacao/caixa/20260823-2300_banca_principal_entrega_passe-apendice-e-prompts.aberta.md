---
de: banca
para: principal
tipo: tarefa
acao_esperada: somar o Apêndice E ao bloco de integração pendente (B, A, C, D) — as cinco entregas vão juntas, com a compilação completa (DoD IX)
referencia: a5-prompts/texto.tex + esq-prompt-anatomia.tex · branch banca/esquemas-tikz-metodo · ordem do autor (2026-08-23)
criada_em: 2026-08-23T23:00:00Z
---
Conclusão do passe no Apêndice E (claim 2240; ordem do autor). Ele já
recebeu as páginas renderizadas.

1. **a5-prompts/texto.tex**: FREEZE do instrumento respeitado — o texto do
   prompt v3 intocado palavra por palavra (única intervenção: \sloppy
   tipográfico no quote, comentado, porque as abreviações X=y inquebráveis
   estouravam a linha). Autocontenção: saíram "medido no E0", "(somente
   RQ4)", "decisão D-004" e o título "Variantes do E0-P" (→ "Variantes do
   prompt"), preservando a substância de cada um. "88–95%" verificado
   contra o Cap. 5 (l.106). Modos de instrumentação em lista.
2. **Figura NOVA**: esq-prompt-anatomia.tex (nascida em corpo 12) — a
   chamada em lote: contêiner tracejado (prefixo estático cacheável +
   itens numerados) → oráculo → vetor indexado, com a nota do cache.
   Inserida como fig:ap-prompts-anatomia.
3. Loop (3 renders): quote estourando (\sloppy), figura 1cm larga demais
   (comprimida), expanded_description pendurado no fim de linha (frase
   reordenada), contêiner apertado. 0 erros / 0 overfull nas medidas
   reais.

Fila de integração em bloco: B (2100) + A (2130) + C (2200) + D (2230) +
E (esta) + correções 12pt. Critério: compilação completa. Restam A6
(tabelas) e A7 (parada/drift) na série.
