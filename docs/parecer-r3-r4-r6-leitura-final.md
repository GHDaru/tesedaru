# Parecer da banca — R3, R4 e R6 consolidados: guia para a leitura final

Data: 2026-08-16 · Agente: banca · Método: três auditorias independentes,
read-only, em contextos separados, cada uma com âncora `arquivo:linha` medida
por `grep -n` (nenhuma estimativa). R3 = referências × fichamento (princípio II);
R4 = afirmações fundamentadas (princípio III); R6 = terminologia em camadas
(princípio VII). Nenhum arquivo da tese foi editado.

## Veredito de conjunto

O padrão de falha dominante **não é afirmação sem fonte** — a tese cita de forma
densa e declara divergências. É **inconsistência entre dois pontos do próprio
texto**: 16 dos 23 achados de risco alto do R4 são contradições internas, e o R6
mostra o mesmo fenômeno na terminologia. A consequência prática é boa notícia e
má notícia ao mesmo tempo: **um arguidor não precisa de literatura externa para
atacar — basta ler dois capítulos seguidos**; mas quase tudo se corrige por
edição de texto e conferência de tabela, sem experimento novo.

Placar bruto: R4 achou 101 itens (23 alta, 30 média, ~48 baixa), concentrados
no Cap. 5 (57% dos de risco alto). R6 achou 19 vazamentos de jargão, 16
problemas de sigla e 15 símbolos não declarados. R3 achou 92 citações sem
fichamento e 97 fichamentos órfãos.

## Os 12 itens que eu levaria à defesa

Ordenados por risco de arguição, não por esforço.

| # | Item | Onde | Por que é o topo |
|---|---|---|---|
| 1 | **A tese afirma as duas coisas opostas sobre ruído estruturado**, usando as mesmas duas citações | `2-fundam:585-587` × `5-resultados:143-144` e `6-conclusao:86-93` | O Cap. 2 diz que ruído dependente de classe degrada acentuadamente; o Cap. 5 diz que é o regime benigno — e é sobre esta segunda leitura que repousam três achados (E4, braço A×B, discussão). Uma pergunta derruba a cadeia |
| 2 | **O gate de 85% não fecha nem na aritmética nem na lógica** | `3-metodo:432-436` e `5-resultados:605-607` | A justificativa diz que 85% "fica um desvio acima" de 89,56% (está 4,6 p.p. abaixo); e quando nenhum oráculo atinge o limiar, a configuração do FALCO é derivada assim mesmo, sem declarar a violação do pré-registro |
| 3 | **A política de parada tem dois racionais incompatíveis** (fator ~20) | `a7:20-22` (≈0,022) × `3-metodo:428-431` (ε=10⁻³) | É a causa-raiz que a tese atribui ao resultado negativo. Se a política era arbitrária, "parou cedo demais" deixa de ser diagnóstico e vira desculpa |
| 4 | **E5 é declarado executado e nunca reportado**; a tabela do programa lista E0–E4 e a tese roda sete experimentos | `3-metodo:38-56`, `1-intro:161`, `6-conclusao:210`, `declaracao-ia:27` | Achado simultâneo do R4 (A17) e do R6 (item 1). A tabela promete um programa e os resultados entregam outro — é das primeiras coisas que a banca confere |
| 5 | **A comparação-vitrine "LLM zero-shot supera o supervisionado" mistura conjuntos de avaliação** | `5-resultados:68-71` e `6-conclusao:33-35` | 0,78–0,80 é medido na S-strat (3 por classe); 0,70 é medido no teste T. Macro F1 em amostra balanceada não é comparável ao de T. Aparece como achado de destaque em dois capítulos |
| 6 | **O resultado central do P2 não declara partição nem dispersão** | `4-resultados:127-133`, Tab. `tab:drisl-vs-ag`; mecanismo em `:49-52` | É a contribuição algorítmica própria (DRI-SL vence o envelope do AG). A tabela não diz onde o DRI-SL foi avaliado, e a curva de cobertura que sustenta o mecanismo não existe |
| 7 | **Cinco números que se contradizem dentro da tese** | 140 mil × 177.490 (`5-resultados:365` × `3-metodo:156`); viés 17,1 × 14 p.p. (`5-resultados:396` × `:459`); cache 88–95% × tabela com 91%; E35 "supera" × "empata (p=0,10)"; "96%" × 95,4% | Correções de minutos, mas cada uma é uma trinca no princípio VIII — e a banca costuma checar justamente o número que o candidato repetiu na apresentação |
| 8 | **"Revisão sistemática" prometida e desmentida; tabela de lacunas sem critério** | `1-intro:159` e `2-fundam:25` × `2-fundam:743-744`; `tab:lacunas` (`:804-827`) | O texto chama de sistemática e depois confessa que é narrativa focada. E a tabela que legitima a lacuna distribui 45 marcas ✓/✗/∼ sem definir nenhuma coluna |
| 9 | **Duas interpretações do E3′ excedem o que um braço de semente única sustenta** | `5-resultados:528-531` e `:505-512` | "Nenhum oráculo sustentaria o critério" é refutado pelos próprios dados (A supera B em Macro F1); "erro estruturado como regularizador" é causalidade de braço único. O veredito negativo está bem defendido — a interpretação dele é que está sobre-alegada |
| 10 | **O método promete o que a execução não cumpre, em dois pontos** | `5-resultados:288-290` × `3-metodo:412-414`; `5-resultados:219-222` × `a5-prompts:44-46` | O E1 elege menor margem/menor confiança e todo o resto roda entropia, sem justificar. E o ganho do E0-P é anunciado "sem nenhum rótulo adicional" quando as regras vieram de análise de erro contra o gabarito |
| 11 | **O Cap. 2 usa códigos de experimento antes de existirem** (7 pontos) e a declaração de IA os usa na página pré-textual | `2-fundam:159,199-202,469,597,621`; `declaracao-ia:27` | Violação direta do princípio VII: o capítulo teórico fica ancorado em nomes que só nascem no Cap. 3 |
| 12 | **Colisões de símbolo não resolvidas** | `b` (lote × discordantes de McNemar, na mesma seção); `B` (orçamento × braço); `S` (regra × amostra); `p` (paciência × p-valor); `ε` com duas grafias | `simbolos.tex` declara 7 símbolos; o texto usa ~25. Em tese de métodos numéricos, notação ambígua é arguição garantida |

## Guia de leitura, capítulo a capítulo

O que conferir enquanto lê — cada item já tem a linha.

**Resumo e abstract.** Seis termos internos aparecem antes de existirem (LCE sem
expansão, "gate", "envelope", "gabarito", "braço", `|L_0|`). Conferir se o
veredito reescrito no lote 1 está com a demarcação de gabarito em todos os
pontos (a banca confirmou que sim).

**Declaração de uso de IA.** É o **primeiro** texto da tese a citar códigos de
experimento (E0, E0-P, E4, E5, E6, E3′) — nenhum definido até ali, e E5 nunca.
Ainda traz o marcador "RASCUNHO".

**Cap. 1 — Introdução.** Auto-suficiente (define FALCO, DRI-SL, LCE, P1–P4,
oráculo, L0). Dois pontos: "programa experimental E0–E4" (`:161`) não cobre o
que foi executado; e "revisão sistemática" (`:159`) contradiz o Cap. 2.

**Cap. 2 — Fundamentação.** O capítulo menos auto-suficiente. Além dos códigos
de experimento vazados, é onde estão as duas alegações de lacuna sem citação
(`:479`, `:603`), a contradição sobre ruído estruturado (`:585`) e a tabela de
lacunas sem critérios. Também é o capítulo com 85 das 92 citações sem fichamento.

**Cap. 3 — Método.** Define quase tudo bem. Falhas: E3′ usado em `:137` e
explicado em `:464`; "régua" em `:171` antes de `:451`; "gate" nunca definido
formalmente; RS/US nunca expandidas; AG nunca introduzida; e a aritmética do
limiar de 85% (`:432-436`).

**Cap. 4 — Resultados L0.** Auto-suficiente. O ponto sensível é o resultado
central do P2 (partição e dispersão não declaradas) e a curva de cobertura
ausente.

**Cap. 5 — Resultados FALCO.** Onde se concentra 57% do risco. Além dos itens 1,
5, 7 e 9 acima: a convenção E20–E35 nunca é enunciada e colide com o braço E na
mesma tabela; `b` tem dois sentidos na mesma seção.

**Cap. 6 — Conclusão.** Remove uma ressalva que o Cap. 5 tinha imposto
(`:91-93` × `5-resultados:347-353`); cita E5; usa "AL" onde o Cap. 2 fixou "AA";
usa "Fase Inicial", nome que não existe na máquina de fases.

**Apêndices.** A7 tem o racional incompatível da parada (item 3) e usa NIM e PSI
sem expansão. A1 e A3 estão com 0% de cobertura de fichamento.

## O que NÃO é bloqueio (registro honesto)

- **Os ~48 itens de risco baixo do R4** são retórica — alvo da humanização (R1),
  não da R4.
- **As 92 citações sem fichamento**: fichar todas seria semanas e a banca não
  cobra isso. As que carregam peso argumentativo são poucas — `Rouzegar2024`
  (5 citações, o trabalho mais próximo do FALCO, e o fichamento existente é de
  outra obra do mesmo autor), `Frenay2014` e `Song2023NoisyLabels` (sustentam a
  moldura de ruído nos capítulos de resultado — e são justamente as citações do
  item 1) e a tríade `Wilson1927`/`McNemar1947`/`Wilcoxon1945`.
- **Os 97 fichamentos órfãos** são o inverso de um problema: incluem
  `Vaswani2017`, `Sener2018`, `Hacohen2022TypiClust`, `Yu2023Patron`,
  `Zhang2023LLMaAA`, `Wang2021GPT3Labeling`, `Farquhar2021Bias`,
  `Kossen2021ActiveTesting`, `Pangakis2023Validation` — exatamente as obras que
  o parecer R6 (assento de Domínio) apontou como ausentes do posicionamento.
  **Já estão lidas e fichadas; falta citá-las.** É o trabalho mais barato de
  alto impacto disponível.

## Nota sobre o que este parecer não cobre

R3 mediu cobertura de fichamento, não qualidade do fichamento. R4 mediu
fundamentação, não correção factual dos números (isso é R5). R6 mediu ordem de
introdução de termos, não clareza da prosa (isso é R1/R7). E nenhuma das três
leu o PDF compilado — todas as âncoras são da fonte `.tex` no estado atual.
