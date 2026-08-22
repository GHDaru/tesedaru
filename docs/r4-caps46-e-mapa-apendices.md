# R4 dos Caps. 4 e 6 + R1/R4 e mapa de rodadas dos apêndices

> Tarefa `20260823-1045` · `revisor1` · **modo auditoria: não editei nada.**
> Mesmo método das R4 dos Caps. 3 e 5.

## Antes de tudo: três achados meus estão MORTOS, e é bom que estejam

As três divergências que mandei ao autor na R4 do Cap. 3 **foram todas
corrigidas** e eu as retiro da fila. Verifiquei no texto de hoje:

1. **Racional do gate** — era *"85% fica um desvio acima de 89,56%"* (invertido
   e com "um desvio" sem artefato). Hoje lê-se
   $0{,}95 \times 89{,}56\% = 85{,}1\%$: o limiar passou a ser derivado, não
   estipulado. **Fechada.**
2. **Fase 2 em entropia contra o veredito do E1** — hoje o texto declara que a
   varredura dá estimativas pontuais superiores para margem/confiança, que **o
   desenho nunca as testou entre si**, que a comparação medida é cada uma
   contra a aleatória, e que a troca fica como extensão imediata. É mais
   honesto do que eu pedi. **Fechada.**
3. **Fator 22 na tolerância de parada** — Cap. 3 e Apêndice A7 agora **dizem a
   mesma coisa**: a tolerância é deliberadamente ~20× menor que o limite
   amostral $1/\sqrt{n_V}=0{,}0224$, para que a parada exija ausência total de
   ganho. O espelho fecha nos dois lados. **Fechada.**

---

## Cap. 4 — R4

**Zero conectivos causais sem lastro. Zero afirmações órfãs.** O capítulo faz
algo que merece registro: **declara o próprio viés** — "os valores do AG aqui
reportados herdam o protocolo original (aptidão e relato na mesma partição),
inflacionado por construção". Isso torna a comparação DRI-SL × AG
*conservadora*, e o capítulo diz isso.

Três achados, todos leves:

**C4-1 [BAIXO]** — *"O ganho evolutivo sobre a 1ª geração (coluna Δ) confirma
que o AG explora estrutura real, não flutuação."* O Δ mostra ganho; separar
"estrutura" de "deriva de busca" pediria um nulo (busca aleatória de mesmo
orçamento). Ou se abranda o verbo, ou se declara que o nulo não foi corrido.

**C4-2 [BAIXO]** — *"sempre no sentido esperado, **pois** o protocolo com
deduplicação é ligeiramente mais difícil."* O sentido está medido; a razão está
afirmada. Uma linha de argumento (a deduplicação remove quase-duplicatas que
inflavam a concordância treino/teste) resolve.

**C4-3 [BAIXO, espelho]** — a síntese diz *"o envelope evolutivo confirma
espaço explorável de dezenas de pontos percentuais"* **sem** o qualificador "no
regime pequeno" — que o item (i) da mesma síntese carrega e que o **Cap. 6
carrega** ("no regime pequeno, que é o regime do *cold start*"). Alinhar o
Cap. 4 ao Cap. 6, não o contrário.

---

## Cap. 6 — R4

**Zero conectivos causais sem lastro.** Mas dois achados de peso, e um deles é
espelho de defeito já aberto no Cap. 5.

**C6-1 [ALTO]** — *"O Macro F1 zero-shot ($\approx 0{,}79$) supera o do
baseline supervisionado leve ($0{,}70$)"*, com a leitura de que *"o LLM é
melhor nas classes raras"*.

As duas medidas **não vêm da mesma amostra**. O 0,79 é medido na **S-strat**,
que é balanceada por construção (3 por classe); o 0,70 é o Macro F1 do PVBin
com supervisão completa, medido no conjunto de teste. Macro F1 é média por
classe: numa amostra balanceada, cada classe rara tem 3 instâncias de suporte;
no teste natural, tem quase nenhuma. **A conclusão extraída — "melhor nas
classes raras" — é exatamente a que mais depende dessa diferença de suporte.**

E o Cap. 6 é a versão **pior** do problema: o Cap. 5 ao menos escreve "na
S-strat"; o Cap. 6 dá o 0,79 **sem qualquer qualificador de amostra**. Quem lê
só a conclusão não tem como saber.

A medição de composição que entreguei hoje é o lastro quantitativo da objeção:
mudar o balanceamento da amostra muda a massa de classes raras em ~3×.

**C6-2 [ALTO, espelho do Cap. 5]** — o gate. O Cap. 6 escreve *"sem oráculo
$\ge 85\%$…"* e, na mesma frase, *"a configuração derivada do FALCO é
deepseek-v4-flash (Inicial) + deepseek-v4-pro (Avançado)"*. É o **mesmo
defeito** do achado 2 da R4 do Cap. 5: o papel é atribuído por um critério cuja
restrição não foi satisfeita, sem declarar a divergência. **Consertar só o
Cap. 5 deixa o defeito de pé na conclusão.**

### Um presente para a banca: a redação certa já existe

O achado **1 (ALTO) da R4 do Cap. 5** — a conclusão do pilar afirmada com
gabarito e atribuída ao FALCO — **já está escrita corretamente no Cap. 6**:

> "(achado *post hoc*, executado com rótulos de **gabarito**, não do oráculo da
> hipótese)"

A banca não precisa inventar formulação: basta levar essa ao Cap. 5. É o
espelho funcionando a favor, para variar.

---

## Apêndices — R1 (medido)

Densidade de travessão por mil palavras. A **régua** são os capítulos que já
passaram por R1:

| capítulo (pós-R1) | densidade | | apêndice (sem R1) | densidade |
|---|---|---|---|---|
| 1-intro | 0,0 | | a1-lce | **10,9** |
| 6-conclusao | 0,0 | | a2-ag | **10,1** |
| 2-fundam | 0,1 | | a3-drisl | **11,4** |
| 3-metodo | 0,7 | | a4-biblioteca | **13,9** |
| 5-resultados | 0,8 | | a5-prompts | **11,9** |
| 4-resultados-l0 | 1,5 | | a6-tabelas | 0,5 |
| | | | a7-parada-drift | **13,6** |

**Faixa dos capítulos: 0,0–1,5. Apêndices: 10,1–13,9.** Sete a quatorze vezes
acima — o principal está certo, nenhum passou por R1.

**A boa notícia é o tamanho:** os apêndices são curtos, e isso são **25
travessões no total** em A1–A5 e A7. R1 dos apêndices é trabalho de horas, não
de dias. O **A6 já está na faixa** (0,5) e não precisa de R1 — é tabela, não
prosa.

## Apêndices — R4

**A3-1 [MÉDIO]** — *"A etapa 1 **garante** representatividade… A etapa 2
**garante** não redundância."* O DRI-SL é uma **heurística**; "garantir" é
afirmação de propriedade demonstrada. E a primeira nem se sustenta como
garantia: a alocação proporcional **não impede** que um agrupamento cuja
proporção fique abaixo de $1/I$ receba zero amostras — o que o próprio Cap. 3
reconhece ao declarar 65 classes ausentes do *pool*. Trocar "garante" por
"promove"/"busca" custa uma palavra e elimina a única afirmação forte demais
dos apêndices.

**A7** — depois do conserto da tolerância, está **limpo** e é hoje o apêndice
mais bem argumentado. Sem achado.

**A1, A2, A4** — sem afirmação forte; nada a reportar em R4.

**A5, A6** — R4 **não se aplica**: ver o mapa.

---

## O mapa de rodadas por apêndice (proposta a convergir com o revisor2)

A chave é que os apêndices **não são todos a mesma coisa**. Medindo o que cada
um contém, saem três famílias, e a família decide as rodadas:

### Família 1 — prosa argumentativa (A1, A3, A4, A7)
Texto que afirma. **Todas as rodadas se aplicam**, como em capítulo.

### Família 2 — formalização (A2)
Pseudocódigo e operadores. R1/R2/R6 sim; **R3 n/a** (não cita, e não deve — a
literatura do AG está no Cap. 3); **R5 como espelho**: os parâmetros
($N_{pop}$, gerações, $p_c$, $p_m$) têm de bater com o Cap. 3.

### Família 3 — DADO, não prosa (A5, A6)
Aqui está a parte da proposta que eu defendo com mais convicção:

- **A5 (prompts): R1, R2, R3, R4 são `n/a`, e não por preguiça.** O corpo do
  A5 é o **texto literal do prompt que produziu os resultados**. Humanizar um
  travessão, abrir uma sigla ou suavizar um "sempre" ali **falsifica o
  instrumento**: o apêndice deixaria de reproduzir o que foi executado. A regra
  para o A5 é a oposta da R1 — **fidelidade byte a byte ao artefato**. O que se
  revisa é só a prosa que embrulha o prompt.
- **A6 (tabelas): R1, R2, R3, R4 são `n/a`; R5 é crítico.** São 2.144 palavras
  que são quase todas números dentro de uma `longtable`. Rodar humanização ou
  siglas ali é esforço jogado fora; o que importa é cada número bater com o
  artefato. E note que a densidade já está em 0,5 — não há o que humanizar.

### Tabela-resumo

| Apêndice | conteúdo | R1 | R2 | R3 | R4 | R5 | R6 | R7 |
|---|---|---|---|---|---|---|---|---|
| A1 · LCE | prosa + 1 equação | **sim** (10,9) | sim | sim | sim | n/a¹ | sim | sim |
| A2 · AG | formalização | **sim** (10,1) | sim | **n/a**² | leve | espelho³ | sim | sim |
| A3 · DRI-SL | prosa | **sim** (11,4) | sim | sim | **sim**⁴ | espelho⁵ | sim | sim |
| A4 · biblioteca | prosa | **sim** (13,9) | sim | leve | leve | n/a | sim | sim |
| A5 · prompts | **dado verbatim** | **n/a**⁶ | **n/a**⁶ | **n/a** | **n/a**⁶ | n/a | n/a | sim |
| A6 · tabelas | **números** | **n/a**⁷ | n/a | n/a | n/a | **crítico** | sim⁸ | sim |
| A7 · parada | prosa | **sim** (13,6) | sim | leve⁹ | sim | **sim**¹⁰ | sim | sim |

¹ não reporta número de resultado · ² a literatura do AG está no Cap. 3 ·
³ parâmetros têm de bater com o Cap. 3 · ⁴ os dois "garante" (A3-1) ·
⁵ os 7,7% de duplicatas têm de bater com o Cap. 3 · ⁶ **fidelidade ao artefato
sobrepõe-se**: editar o prompt falsifica o instrumento · ⁷ já em 0,5, é tabela ·
⁸ formato/casas decimais · ⁹ faz afirmação estatística sem citar; vale conferir
se precisa de fonte · ¹⁰ 910/1.000, 6.009, 4.742, 32–40%

**Para o revisor2 convergir**: o ponto em que espero divergência é o A5. Se ele
propuser R1/R2 lá, a discussão é boa e o autor arbitra — mas o meu argumento é
que o A5 não é texto da tese, é **anexo de instrumento**, e a regra de anexo de
instrumento é reproduzir, não melhorar.
