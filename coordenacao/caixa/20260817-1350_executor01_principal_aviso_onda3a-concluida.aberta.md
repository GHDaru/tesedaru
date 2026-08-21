---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma — registro de fechamento; sigo para a Onda 4 (E1/E4)
referencia: activelearning notebooks/auditoria/efeito-do-prompt.ipynb
criada_em: 2026-08-17T13:50:00Z
---
**Onda 3a concluída** (E0 + E0-P). O E0-P também reproduz 100%: 6 de 6
acurácias e 6 de 6 pares de McNemar idênticos ao `analysis.json` publicado,
recomputados do dado bruto sem gastar nada.

Os dois oráculos do Cap. 5 (E0 e E0-P) estão agora auditados ponta a ponta.
Resumo do que ficou: E0 confirma **zero divergência** de pipeline (o achado
do `b=43,c=16` segue firme, sem novidade); E0-P confirma o capítulo inteiro,
sem ressalva.

**Próximo**: Onda 4 (E1/E4) — o `sweeps.jsonl` das 104 células não está
versionado (achado do lote 2), então aqui não há reanálise grátis possível
como no E0: seria reexecução completa. Vou avaliar o custo antes de rodar.
