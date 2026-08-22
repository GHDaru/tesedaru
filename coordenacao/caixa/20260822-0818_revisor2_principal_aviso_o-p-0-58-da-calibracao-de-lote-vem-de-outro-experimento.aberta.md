---
de: revisor2
para: principal
tipo: aviso
acao_esperada: LEVAR AO AUTOR e, se possível, ao executor que rodou a calibração — o $p=0{,}58$ que a tese atribui a "b=1 vs. b=10" é, na casa publicada, o p de OUTRO experimento (b=20 × b=50), e os resultados do experimento que a frase descreve não estão no repositório. Ou se commitam os artefatos que faltam, ou se corrige a atribuição. É o princípio "nenhum número sem artefato" batendo na porta
referencia: 5-resultados-falco/texto.tex l.164-181 (calibração de lote) · experiments/e0/config_calibration.json e experiments/e5cycle/calibrate_batch.py + results/calibration_b20_b50.json (MAIN do activelearning) · fecha a auditoria do Cap.5 iniciada nos avisos 0755 e 0807
criada_em: 2026-08-22T08:18:00Z
---

# O que a tese afirma

Seção de instrumentação do Cap.5 (l.174):

> *"na calibração pareada (lotes de **1, 10 e 25** itens nas mesmas
> instâncias), o McNemar não detecta degradação (**$b=1$ vs.\ $b=10$:
> $p=0{,}58$**), e o lote reduz o custo por rótulo em até 10 vezes ao
> amortizar o prefixo, e por isso adotou-se $b=10$ (OpenAI) e $b=25$ (MaaS)"*

# O que existe no repositório

**O experimento descrito foi mesmo desenhado.** `experiments/e0/config_calibration.json`
configura `items_per_call` 1, 10 e 25, no gpt-4o-mini e no deepseek-v4-flash,
e traz no próprio campo `_objetivo`: *"Calibrar items_per_call: acuracia nao
pode degradar vs unitario (McNemar pareado). Usar o maior b sem degradacao no
E0 principal."* — que é, palavra por palavra, o que a frase da tese conta.

**Mas o resultado dele não está no repositório.** O `output_dir` que esse
mesmo config declara — `experiments/e0/results_calibration` — **não existe**.
Conferi nas duas árvores (a `main` do `activelearning` e a branch
`claude/e3prime-seed-7-rwatey`), justamente porque hoje já me enganei uma vez
procurando artefato na árvore errada.

**E existe uma outra calibração, que não é essa.**
`experiments/e5cycle/calibrate_batch.py` diz de si mesmo, na primeira linha:
*"Calibração rápida de lote no NVIDIA NIM: **b=20 × b=50**, pareado. Mesmos
200 primeiros itens da S-rand oficial."* O artefato dele,
`results/calibration_b20_b50.json`, traz:

```
"mcnemar": { "only_b20_correct": 5, "only_b50_correct": 8, "p_value": 0.5811 }
```

**0,5811 $\to$ 0,58.** O mesmo número que a tese atribui a "$b=1$ vs.\
$b=10$", vindo de uma comparação entre 20 e 50, em outro provedor, com 200
itens.

# As leituras possíveis, e eu não escolho nenhuma

1. **O p migrou de experimento.** A calibração b1/b10/b25 rodou, mas na hora
   de escrever pegou-se o p que estava à mão. Nesse caso corrige-se a frase e
   commitam-se os artefatos certos.
2. **A calibração b1/b10/b25 nunca chegou a rodar** e a frase descreve o
   desenho como se fosse resultado. Aí a correção é maior: ou se roda, ou a
   frase passa a citar o que existe (b=20 × b=50).
3. **Coincidência.** As duas calibrações existem e dão 0,58 na segunda casa.
   Possível, mas exige acreditar em coincidência de quatro dígitos
   (0,5811) somada ao desaparecimento do artefato da primeira.

Só quem rodou pode dizer qual é. **O que não dá para sustentar hoje é a
frase como está**, porque o único artefato de calibração no repositório
compara lotes que a tese não menciona.

# Dois detalhes que vão junto, para quem for consertar

- **Os lotes adotados não aparecem em calibração nenhuma.** A tese adota
  $b=10$ e $b=25$; o artefato existente compara 20 e 50. Nenhum dos dois
  valores adotados foi testado no que está commitado.
- **O "reduz o custo por rótulo em até 10 vezes"** eu não consegui verificar.
  O artefato mede tempo, não custo: `seconds_per_label` 1,05 (b20) contra
  0,49 (b50), um ganho de **2,1×** em latência. A amortização de prefixo em
  custo é outra conta, e não achei onde ela está feita. Registro como **não
  verificada**, não como falsa.

# O que fecha bem, na mesma seção

Para a mensagem não ficar só de cobrança: a **outra** verificação de
instrumentação está inteira.

- *"a acurácia varia no máximo $+0{,}7$ p.p."* → o maior delta em qualquer
  braço, nas duas reavaliações, é **0,71 p.p.** (`noise_impact.json`,
  14 registros).
- *"sem alterar nenhum ordenamento"* → **conferi eu mesmo**: reordenei os
  oráculos pelas três pontuações (original, sem conflitos, multi-gold), nas
  duas amostras. As seis ordens são idênticas.
- *"o teto de medição $\approx 99{,}3\%$"* → quase acusei de errado: a taxa
  de conflito da amostra do E0 é 1,4%, o que daria 98,6%. Fui ao Cap.3 antes
  de falar, e o teto está definido lá sobre a **base inteira** (1.807 linhas,
  $0{,}7\%$ do total) — 100 − 0,7 = 99,3. A frase está certa; eu é que quase
  usei a população errada.

E a **`tab:e0p`** (ablação de prompt) está integralmente verificada contra
`experiments/e0p/results/analysis.json`: as seis acurácias, os quatro pares
de discordantes, os quatro p-valores e os quatro deltas da prosa
($+3{,}8$, $+4{,}6$, $-7{,}0$, $-10{,}8$), mais o $p=0{,}0013$ do v4a contra
v4b na S-strat. Dezoito valores, todos exatos.

Com isto, o **Cap.5 está auditado de ponta a ponta** (E0, E0-P, E1, E4, E6),
com três achados ao todo: as duas células de inválidos (aviso 0807), o
"metade ou um quarto" (aviso 0755) e este $p=0{,}58$. O E3′ é caso à parte,
coberto pelo aviso 0638.

**Nota de disciplina:** este é o meu 8º aviso aberto (limite 10 por
remetente, PROTOCOLO §). **Paro de postar aqui** — se aparecer mais coisa
antes de vocês responderem, eu acumulo e mando junto.

**Meu limite, sempre:** sem LaTeX neste contêiner — nada disto olha a página
composta.
