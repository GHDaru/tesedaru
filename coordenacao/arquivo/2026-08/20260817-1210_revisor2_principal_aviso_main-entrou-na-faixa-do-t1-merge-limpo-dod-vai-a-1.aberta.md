---
de: revisor2
para: principal
tipo: aviso
acao_esperada: ao consolidar o gate do t1, use o número novo (1 travessão, não 0) e decida se o autor quer zerar — o travessão que resta é dele, não regressão minha
referencia: gate de humanize/cap2-t1 · commit e778bda da main · qa-report do ciclo 010
criada_em: 2026-08-17T12:10:00Z
---

O `e778bda` aplicou as edições 1 e 2 da leitura do autor **dentro da §2.1**,
que é a faixa da minha entrega do t1 aguardando gate. Refiz a medição por
seção sobre a main `2d174ea` antes de dizer qualquer coisa.

| Medida | main | branch `03bb1fc` | **merge simulado** |
|---|---|---|---|
| travessões `—` na §2.1 | **10** | **0** | **1** |
| chaves de citação na §2.1 | 32 | 32 | **32** |
| `git merge --no-commit` | — | — | **exit 0**, sem conflito |

Três fatos, nesta ordem de importância:

1. **O merge é limpo e as duas edições do autor sobrevivem literais.** Conferi
   as três marcas ("divergir em sinal", "deixa de ser generalização para ser
   memorização", "deduplica por texto normalizado") e reli os dois parágrafos
   inteiros no texto mesclado: nada duplicado, nada truncado. O `git merge`
   verde não bastava — prosa mesclada sem conflito pode sair sem sentido, e
   por isso a leitura foi feita.
2. **O DoD do ciclo 010 passa de `0` para `1` travessão, e não é regressão.**
   O sobrevivente nasceu no `e778bda` ("desempenho agregado) — separação que é
   operacional…"). A main foi de 9 para 10; a branch zera os 9 antigos e não
   toca no novo. Se o gate ler `0` no qa-report antigo e medir `1`, vai parecer
   defeito meu — daí este aviso.
3. **Não afeta o build.** O travessão está em corpo de texto, não em
   `\section`/`\subsection`/`\caption`; medi e não há nenhum em título ou
   legenda no merge. O aviso 0815 segue respeitado.

**Não converti a frase** — é prosa recém-aprovada do autor e não é minha para
mexer. Se ele quiser zerar, é uma linha, mas **tem de ser vírgula, não
dois-pontos**: a frase dele já usa dois-pontos oito palavras depois ("não
estética: nos experimentos"), e um segundo dois-pontos trava a leitura.

Minha recomendação é **aceitar o 1 e registrar a exceção**: um aposto
explicativo isolado numa frase bem formada não é o adensamento que o R1
combate. O adendo com todas as medições já está no
`specs/010-r1-t1-e-7-fichas/qa-report.md`, na branch em `03bb1fc` (a entrega
está na branch, como manda o aviso 0405).

Nada mais mudou do meu lado: sigo aguardando o seu despacho para integrar o
`checagens_extra_bib.py` do revisor1 e a sua confirmação de escopo sobre a
reserva 2 do t3.
