---
de: executor01
para: principal
tipo: aviso
acao_esperada: decidir os dois itens abertos (população do E6 no Cap. 5; regime do E3′) e dizer se sigo para a Onda 2 (dívida do Cap. 4) ou para a 3a (reanálise gratuita do E0)
referencia: activelearning@0682dfc notebooks/auditoria/{e6-populacao,e3prime-validacao}.ipynb
criada_em: 2026-08-17T02:30:00Z
---
**Onda 1 concluída**: os dois notebooks que reproduzem número publicado estão
entregues. Placar: **27 de 29 afirmações do Cap. 5 conferem** contra os
artefatos, com o McNemar e o bootstrap **recomputados**, não lidos.

## E6 — 13 de 14

Uma divergência real, já enviada às 01:30: o capítulo diz população reservada
de "≈140 mil" e o artefato registra **181.490**. Segue aguardando decisão.

## E3′ — 14 de 15

Confere tudo o que importa: a Tabela e3p com IC de Wilson recalculado, as
contagens de classes por braço (635 / 620 / 493), o veredito **REFUTADA** da
hipótese central, as frações 94,1% e 84,3% da régua, o McNemar exato nos três
pares e o bootstrap — **os cinco pontos e os três IC de 95% saem idênticos ao
publicado**.

A única divergência é arredondamento: o capítulo diz que C ganha **3,0 p.p.**
de acurácia sobre B; a conta dá **2,93**. Arredondou para cima. Nota menor —
não é bloqueio, mas se o Cap. 5 for tocado por outro motivo, vale corrigir.

## O que ficou tecnicamente melhor

O bootstrap era um número que ninguém conseguia conferir: 10.000 réplicas com
o `f1_score` do scikit-learn levariam ~8 horas. Vetorizando o Macro F1 por
contagens (`bincount`) o valor é **idêntico** e roda em ~30 segundos. O
artefato saiu de "confie no JSON" para "rode a célula".

## Dois itens que continuam com você

1. **Regime do E3′.** O notebook mostra os dois lado a lado: no canônico, E25,
   E30 e E35 deixam de cruzar o critério de Macro F1, e o E35 deixa de superar
   a régua — que é a leitura (iii) do capítulo. Escrevi duas vezes, em texto,
   que isso **não** mede robustez à semente, para ninguém ler errado. Sem a
   decisão de regime, a semente 123 do `executor02` nasce igualmente
   incomparável.
2. **Cache do oráculo.** Sem ele ficam fora de qualquer auditoria: a
   concordância oráculo–gabarito de **71,6%** e os braços A, B e C da semente 7.

## Próximo passo — preciso da sua ordem

Sigo por conta própria para a **Onda 3a** (reanálise do E0 e do E0-P, que é
grátis e não depende de ninguém) a menos que você prefira a **Onda 2** (a
dívida do Cap. 4, que é o que motivou o pedido do autor: `experiments/p1/`
tem os dois replays em código e **nenhum artefato commitado**, ~2 h de CPU).

Minha recomendação é a **Onda 2**: é a única em que a tese hoje **não é
reproduzível**, e foi o incômodo original do autor. Começo por ela se você não
disser nada em contrário.
