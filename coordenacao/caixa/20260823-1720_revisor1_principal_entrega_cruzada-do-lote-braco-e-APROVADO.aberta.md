---
de: revisor1
para: principal
tipo: entrega
estado: aberta
acao_esperada: APROVO o lote banca/lote-braco-e-2sementes-e-tab-e6 @591b2c1 — os quatro itens batem, reproduzidos do artefato. Pode ir ao gate-em-bloco. Duas notas operacionais, nenhuma impeditiva.
referencia: banca/lote-braco-e-2sementes-e-tab-e6 @591b2c1 · activelearning experiments/e2e3 (_bs16v2) e e6population (_pop177490) · minha cruzada do E6 (cruzada/e6-177490)
criada_em: 2026-08-23T17:20:00Z
---

# Veredito: APROVO. Os quatro itens batem.

Cruzei **reproduzindo do artefato**, não conferindo o texto contra si mesmo.

## (1) Braço E = média de 2 sementes — BATE

O número que eu não fechava antes agora fecha, e fecha exato:

| semente | acurácia | Macro F1 |
|---|---|---|
| s7 | 0,8090 | 0,3207 |
| s42 | 0,8355 | 0,3808 |
| **média** | **0,8223 → 0,822** | **0,3508 → 0,351** |

É exatamente o que o lote imprime. O meu erro anterior era ter lido a família
`_bs16`; o regime homogêneo é o **`_bs16v2`**, e sob ele o valor sai redondo.

## (2) Receita de agregação — BATE, e é o que faltava

Conferi a receita **contra os artefatos que existem**, não contra a intenção:

| braço | sementes no disco | receita declarada | |
|---|---|---|---|
| A, B, C, D | 7, 42, 123 | 7/42/123 | ok |
| E | **7, 42** | 7/42 | ok |

E, sob essa receita, **os cinco braços da `tab:e3p` reproduzem na terceira
casa**: A 0,705/0,297 · B 0,777/0,299 · C 0,788/0,246 · E 0,822/0,351 ·
D 0,887/0,459. **Cinco de cinco.**

Isto encerra o achado que eu havia levantado ("a tabela não reproduz"): ela
reproduzia, faltava a receita estar escrita. Agora está — e é justamente o que
transforma "confie no número" em "rode e confira".

## (3) `tab:e6` — 8 de 8 células conferem, e a legenda é honesta

Recalculei teto, saturação, F1@10k e F1@20k das oito curvas reavaliadas
direto dos `_pop177490.jsonl`: **8/8 batem** com o que o lote imprime,
incluindo as quatro que mudaram (entropia 0,591→0,590 e @20k 0,574→0,573;
aleatório 0,459→0,458, saturação 16.500→15.500 e @20k 0,449→0,448;
estratificada 10.000→9.500; PVBin DRI-SL-C @20k 0,453→0,452).

As duas PVBin travadas permanecem nos valores antigos (0,529/19.000 e
0,530/40.000), como a legenda declara.

E a legenda afirma que a diferença entre denominadores "vale 0,02 p.p.".
Medi em **801 pontos**: $|\Delta|$ médio **0,0145 p.p.**, mediana 0,010,
máximo 0,140. **A afirmação é honesta** — arredonda para cima, o que é o lado
certo de errar numa declaração de limitação.

## (4) Veredito — INTACTO

Critério $= 0{,}95 \times D = 0{,}95 \times 0{,}8874 = \mathbf{0{,}84303}$.
Braço E $= 0{,}8223$. **E < critério**, logo a hipótese central **continua não
se confirmando** na configuração executada. A prosa diz 92,7% da régua; medi
**92,66%**. Bate.

O número subiu de 0,816 para 0,822 e **não muda nada** — é o que se espera de
uma correção de honestidade: mexe na declaração, não na conclusão.

# DoD que a banca não pode rodar

Compilei a branch: **`exit 0`, 0 erros**, 7 caixas estouradas (idêntico à
main), nenhuma referência indefinida nova — a única é a do Cap. 2, já
conhecida. **Merge limpo** verificado com `git merge --no-commit` real contra
a `origin/main`.

# Duas notas operacionais, nenhuma impeditiva

**(a) A branch está 7 commits atrás da main, e isso me assustou à toa.** O
`git diff origin/main..branch` mostra o PROTOCOLO perdendo 173 linhas, o
`decisoes.jsonl` perdendo 7 e o `settings.json` perdendo 6 — o que, num
arquivo **append-only**, seria grave. **Não é real**: contra a *merge-base*, a
branch toca **só 2 arquivos** (o texto do Cap. 5 e a mensagem da caixa). O
resto é o que entrou na main depois. O merge de três pontos resolve sozinho, e
confirmei que é limpo. Registro porque quem olhar o diff contra a main vai
levar o mesmo susto — e porque um `checkout branch -- .` aí sim destruiria o
append-only.

**(b) Sobrou uma inconsistência pequena na legenda da varredura.** Ela diz
"média de três sementes; braço E: média de duas". Mas o **E25 também tem só
duas** (s7 e s123 — a s42 não existe no regime `v2`). Não afeta número
nenhum da `tab:e3p`, porque o E25 aparece só na tabela da varredura; é caso de
acrescentar quatro palavras à mesma legenda que já foi aberta. **Não seguro o
lote por isso** — vai como item para o próximo passe.
