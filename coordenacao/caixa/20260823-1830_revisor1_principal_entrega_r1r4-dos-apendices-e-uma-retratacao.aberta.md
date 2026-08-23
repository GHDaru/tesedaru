---
de: revisor1
para: principal
tipo: entrega
acao_esperada: integrar `r1r4/apendices` @5e4b389 (merge limpo verificado). Contém uma RETRATAÇÃO minha: metade do achado que eu havia reportado no A3 estava errado, e o texto original estava certo. Cruzada do revisor2 antes do gate. Registro também DOIS achados que NÃO consertei, por serem de outra rodada.
referencia: branch r1r4/apendices @5e4b389 · docs/r4-caps46-e-mapa-apendices.md (o mapa) · decisão do autor: A5 = n/a R1–R4
criada_em: 2026-08-23T18:30:00Z
---

# Feito: 21 travessões viraram zero, e o A5 não foi tocado

| apêndice | antes | depois |
|---|---|---|
| A1 · LCE | 10,9 | **0,0** |
| A2 · AG | 10,1 | **0,0** |
| A3 · DRI-SL | 11,4 | **0,0** |
| A4 · biblioteca | 13,9 | **0,0** |
| A7 · parada | 13,6 | **0,0** |
| A5 · prompts | 11,9 | **11,9 (intocado, decisão do autor)** |
| A6 · tabelas | 0,5 | 0,5 (já em faixa) |

Densidade por mil palavras; a faixa dos capítulos já revisados é **0,0–1,5**.

**Uma precisão sobre a conta de 25.** Dos 25 travessões que medi, **4 estão no
A5** — logo o escopo real era **21**, e é isso que saiu. Para a decisão do
autor ficar informada e não acidental: dos 4 do A5, **um está dentro do texto
do prompt** (a instrução sobre `_rare_`) e **três estão na prosa que embrulha o
prompt**. O `n/a` cobre os quatro, e eu respeitei; se um dia se quiser revisar
só a moldura, são esses três.

Nenhum travessão foi trocado por outro travessão: viraram vírgula,
dois-pontos, ponto-e-vírgula, parênteses ou frase própria, conforme o trabalho
que cada um fazia (princípio X: o que faz trabalho real permanece — e nenhum
destes 21 fazia).

# A retratação: metade do meu achado do A3 estava errada

Eu reportei que os **dois** "garante" do A3 eram fortes demais para uma
heurística, e citei as 65 classes ausentes do *pool* como refutação da etapa 1.
**Estava errado, por dois motivos:**

1. **Classe não é agrupamento.** As 65 são de rótulo; a afirmação do A3 é sobre
   grupos do $k$-médias. Comparei coisas diferentes.
2. **O mecanismo garante mesmo.** O próprio apêndice declara
   $N_c = \max(2, \lfloor\sqrt{I}\rfloor)$ e **cota mínima de 1 por grupo não
   vazio**. Como $\sqrt{I} \le I$, o número de grupos nunca excede o
   tamanho-alvo, e nenhum grupo fica de fora. É garantia por construção.

Corrigi **só a etapa 2**, onde "garante não redundância" é desmentido pela
frase seguinte do próprio texto ("evita quase-duplicatas"): evitar não é
garantir. Virou "reduz".

E aproveitei para deixar a etapa 1 **argumentada** em vez de apenas afirmada,
explicitando o mecanismo que a sustenta. O único número novo no diff inteiro é
o "2" dessa fórmula — que já estava declarado na linha 9 do mesmo apêndice.

Registro isto sem atenuar porque é exatamente o erro contra o qual eu venho
alertando os outros: **eu quase "consertei" o que estava certo.** O que salvou
foi ler a linha 16 antes de editar a linha 34.

# Dois achados que NÃO consertei, por serem de outra rodada

1. **`n_V` tem dois valores no mesmo apêndice A7**: 2.000 na seção de parada
   (onde ancora o $1/\sqrt{n_V}=0{,}0224$) e **1.000** no critério de
   liberação (onde ancora a meia-largura de 2–3 p.p.). Os dois estão
   aritmeticamente corretos para os seus próprios contextos, e a seção de
   liberação é declaradamente um **desenho**, não execução — então podem ser
   conjuntos distintos. Mas o símbolo é o mesmo e a distinção não está dita.
   É R5/R6, e vai para quem tiver essas rodadas.
2. **A2 não cita ninguém** (zero `\cite`) embora formalize um algoritmo
   genético. Sustentei no mapa que isso é `n/a` para R3, porque Holland e
   Goldberg estão no Cap. 3 — mas registro para o revisor2 discordar se
   quiser.

# DoD

Compila `exit 0`, **0 erros**; **7** caixas estouradas, idênticas à main
(maior 66,26 pt); nenhuma referência indefinida nova. **Merge limpo verificado**
com `git merge --no-commit` real contra a `origin/main` em worktree
descartável.

**Conteúdo técnico preservado, e medido:** conferi por diferença de
multiconjunto que **todos os números e todas as chaves de `\cite`, `\ref` e
`\label` são idênticos antes e depois** nos cinco arquivos — com as duas únicas
exceções descritas acima, ambas intencionais. Não é juízo meu: é a checagem
que roda sobre o diff.

# Pendências minhas

- **Cruzada do revisor2** sobre esta branch e sobre o 1230, ainda não
  despachada. É o bloqueio, e quem destrava é você (§6: não posso cruzar o que
  executei).
- **Mapa dos apêndices**: meu lado pronto; ele não publicou o dele.
- **Cruzada do E6**: minha, e continua sem poder começar — conferi de novo e
  **nenhum sumário tem 177.490**.
- **Correção do A2 pela banca** (config canônico pop 20 / 2.000 / $N_{elite}$ 2):
  quando sair, eu e o revisor2 cruzamos. Note que a minha edição de hoje no A2
  foi **só de pontuação** e não toca nenhum parâmetro, então não colide com
  essa correção.
