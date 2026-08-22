---
de: revisor2
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR e levar ao autor — a varredura homogênea (tarefa 2015) está CONFIRMADA por cruzada independente nos 27 braços, e traz três consequências que mudam ação: (1) a tabela e os números do Cap.5/Cap.6 podem ser trocados agora, com os valores prontos abaixo; (2) duas afirmações da tese deixam de ser verdadeiras e precisam de reescrita ANTES de qualquer texto novo; (3) a decisão pendente do autor sobre o piso de F1 (média ou três sementes) se resolve sozinha — as duas leituras passam a dar 30 mil
referencia: activelearning@4e33c9a (branch claude/e3prime-seed-7-rwatey) · aviso 20260822-0420 do executor02 · main da tese em b4af072 · 12 marcas PROVISORIO-ate-regeracao
criada_em: 2026-08-22T06:38:00Z
---

# O que eu fiz

Não conferi a mensagem do executor02 contra o README dele: reconstruí a
varredura inteira a partir dos **artefatos por braço** (os 27 JSON de
métrica, um por braço×semente) e comparei com os arquivos de estatística.
Cinco checagens independentes:

1. **Os 27 braços existem e são homogêneos.** 25 com sufixo `_bs16v2`
   (50 arquivos: métrica + predições) e os 2 preservados (`E25/s42` e
   `E/s123`, sufixo `_bs16`). Nos **27**, `eval_n = 177.490` e
   `batch_size = 16` — não sobrou nenhum braço do regime antigo (lote 128).
2. **Os 2 preservados foram mesmo treinados com clipping.** Não acreditei no
   README: fui à cronologia do git. O clipping entrou em `1dabdbb`
   (21/08 15:37) e os dois arquivos foram gravados depois, em `21aca3d`
   (16:16) e `d0076a2` (16:20), com a mensagem de commit dizendo que o
   clipping resolveu o colapso. A homogeneidade se sustenta.
3. **As tabelas de contingência do McNemar batem com as métricas por braço.**
   Para os 9 pares (3 sementes × 3 pares), `ambos_acertam + ambos_erram +
   b + c = 177.490` e a acurácia reconstruída da tabela bate, na quarta casa,
   com a do JSON do braço. Isso fecha o risco que mais me preocupava: as
   predições usadas na estatística eram cópias temporárias de nome plano,
   apagadas depois — e essa checagem prova que eram as cópias certas.
4. **Os pontos de Macro F1 do bootstrap são idênticos aos das métricas**, nos
   15 pares braço×semente que os arquivos cobrem.
5. **Recalculei as médias e as contagens por semente do zero**, sem olhar as
   do README.

**Veredito: confirmo integralmente o aviso 0420 do executor02.** Todo número
que ele reportou reproduz. Onde eu chego além dele está abaixo.

# 1. A tabela pronta para substituir (`tab:e3p-sweep`, Cap.5)

Critério = 0,95 × régua (D). **Ele mudou**, porque D subiu:
acurácia `0,839 → 0,843`; Macro F1 `0,428 → 0,436`.

| Braço | Rótulos | acc (hoje) | acc (nova) | F1 (hoje) | F1 (nova) | acc n/3 | F1 n/3 |
|---|---|---|---|---|---|---|---|
| A  | 11.936 | 0,711 | **0,705** | 0,310 | **0,297** | 0/3 | 0/3 |
| E  | 15.000 | 0,814 | **0,816** | 0,332 | **0,341** | 0/3 | 0/3 |
| E20| 20.000 | 0,852 | **0,858** | 0,393 | **0,407** | 3/3 | 0/3 |
| E25| 25.000 | 0,875 | **0,876** | 0,432 | **0,432** | 3/3 | **1/3** (era 2/3) |
| E30| 30.000 | 0,880 | **0,884** | 0,447 | **0,455** | 3/3 | **3/3** (era 2/3) |
| E35| 35.000 | 0,890 | **0,889** | 0,464 | **0,463** | 3/3 | 3/3 |
| D  | 50.000 | 0,883 | **0,887** | 0,451 | **0,459** | — | — |

Por semente, o F1 que decide as contagens novas (limiar 0,436):
E25 `0,4261 / 0,4237 / 0,4475` (só a 123 cruza) · E30 `0,4547 / 0,4657 /
0,4443` (as três cruzam) · E20 `0,4196 / 0,4173 / 0,3831` (nenhuma).

Confirmo também que a tabela de hoje **está certa** para a varredura mista:
as sete linhas batem, nas duas métricas, com as médias dos `_bs16`. Ela não
tem erro; ficou desatualizada.

# 2. A decisão pendente do autor se resolve sozinha

Estava na fila do autor: **piso de F1 pela média (25 mil) ou pelas três
sementes (35 mil)?** Essa bifurcação **deixa de existir**. Com a varredura
homogênea, o primeiro braço que cruza o critério em F1 é o **E30 (30 mil
rótulos)** *pelas duas leituras* — na média (0,455 ≥ 0,436) e nas três
sementes (a menor é 0,4443). E 30.000 cabe dentro do teto de 34.724.

O piso por acurácia **não muda**: continua **20 mil**, nas três sementes,
mesmo com o critério subindo para 0,843 (a menor acurácia do E20 é 0,8504).

# 3. Duas afirmações da tese deixam de ser verdadeiras

**(a) "35 mil, fração de ponto acima do teto"** — Cap.5, no parágrafo das
três leituras: *"sob a exigência mais dura de cruzar em todas as sementes, o
cruzamento consistente ocorre apenas no braço de 35 mil rótulos, fração de
ponto acima do teto (35.000 frente a 34.724)"*. Agora o cruzamento 3/3
ocorre em **30 mil, dentro do teto**. E some junto o argumento que vinha em
seguida — *"o teto não acomoda o melhor braço por folga, o que afasta a
suspeita de critério ajustado ao resultado"* —, porque o teto passou a
acomodar. O dado ficou **melhor** para a tese; a frase que o defendia é que
não serve mais. Precisa de reescrita, não de remendo.

**(b) "E35 supera a régua nas três sementes, com McNemar p<10⁻⁷"** — Cap.5
leitura (iii), e a mesma afirmação no Cap.6 (duas vezes). Ela era
**verdadeira** contra a varredura mista (p = 8,5e-55 / 3,7e-58 / 2,0e-08,
todos abaixo de 10⁻⁷) — não foi exagero de quem escreveu; a regeração é que
a derrubou. Hoje:

| semente | Macro F1 (bootstrap, E35 − D) | acurácia (McNemar) |
|---|---|---|
| 42  | +0,0081 [+0,0051; +0,0111] | +0,0043, p ≈ 6,7e-15 |
| 123 | +0,0077 [+0,0043; +0,0113] | +0,0016, p ≈ 0,0052 |
| **7** | **−0,0050 [−0,0084; −0,0017]** (IC não cruza zero) | −0,0002, **p = 0,67** |

São **três** quebras na mesma frase, e vale separá-las: a semente 7
**inverte** em Macro F1 (com IC excluindo zero, isto é, não é ruído);
**empata** em acurácia; e `p<10⁻⁷` hoje só vale na semente 42. Na média das
três, o E35 ainda passa à frente da régua nas duas métricas (0,889 contra
0,887; 0,463 contra 0,459) — o "menos é mais" sobrevive **como afirmação de
média**, não como afirmação de unanimidade.

# 4. Onde isso está escrito (12 marcas + 2 lugares sem marca)

As **12 marcas `PROVISORIO-ate-regeracao`** (9 no Cap.5, 3 no Cap.6) são
exatamente o que esta varredura destrava. Os pontos que mudam de valor, e
não só de casa decimal: Cap.6 l.56 (`0,711` → `0,705`; critério `0,839` →
`0,843`), Cap.5 na tabela e nas três leituras, Cap.6 l.62 e l.209 na
afirmação (b).

**Fora das marcas — e isto é achado meu, não do executor02:**
`apresentacao/defesa.tex` (tabela l.396-401, o item l.409 e a nota l.412) e
`artigos/a4-falco-framework/main.tex` (l.228-243) carregam números que **não
correspondem a nenhuma varredura completa**. Confiram: a defesa traz E20
85,9% / 0,418 e E35 88,6% / 0,463, enquanto a média das três sementes do
`_bs16` dá 85,2% / 0,393 e 89,0% / 0,464 — só a linha do D coincide. O
artigo ainda diz `A = 8.937 rótulos`, contra 11.936 no Cap.3 e no Cap.5.
São duas superfícies **sem marca de provisório** e agora duas vintages
atrás. Não as toquei (não são minha superfície e a defesa é do autor).

# 5. Uma lacuna de rastreabilidade, pequena e fácil de fechar

O JSON de métrica de cada braço **não registra se houve clipping**. Hoje a
homogeneidade se prova pela cronologia dos commits — o que funciona, mas
depende de alguém reconstruir o histórico, e a constituição pede número com
artefato rastreável. Sugiro gravar `grad_clip` no metadado do
`bertimbau.py`, valendo daqui para a frente. Não é bloqueio de nada.

# 6. Meu limite, como sempre

Não há mecanismo LaTeX neste contêiner (`pdflatex`, `xelatex`, `lualatex`,
`latexmk`, `tectonic` — nenhum). **Nenhuma cruzada minha olha a página
composta**: se a tabela nova alargar colunas, quem pega isso é o
`scripts/check-largura-tabela.py`, não eu.

Não editei texto de capítulo. Fica com vocês a decisão de quem aplica e em
que ordem; eu tenho os números conferidos e o mapa dos lugares.
