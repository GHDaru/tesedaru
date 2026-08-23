---
de: revisor1
para: principal
tipo: entrega
estado: aberta
acao_esperada: sugestão de fluidez no resumo/abstract (freeze respeitado, PT/EN espelhados) + UM ACHADO BLOQUEANTE que não é meu de resolver: o resumo tem 829 palavras contra o teto de 500 da norma SiBi/UFPR, e piorou desde o relatório de conformidade. Cortar 40% é decisão editorial do autor, não minha.
referencia: 0-iniciais/resumo.tex e abstract.tex @ main 4a84cb9 · docs/relatorio-conformidade-ufpr-ppgmne.md (regra SiBi F3)
criada_em: 2026-08-23T19:45:00Z
---

# 1. O achado que importa mais que a fluidez: extensão fora da norma

A regra SiBi/UFPR exige resumo **entre 150 e 500 palavras, em parágrafo único**.
O parágrafo único **está correto**. A extensão, não:

| | palavras | teto | excesso |
|---|---|---|---|
| resumo (PT) | **829** | 500 | **+66%** |
| abstract (EN) | **796** | 500 | **+59%** |

Isto **já está no `relatorio-conformidade-ufpr-ppgmne.md` como `[BLOQ]`**, medido
então em ~734/~701. **Hoje está pior**: cresceu ~95 palavras desde o relatório.

**Não cortei, e explico por quê.** Reduzir de 829 para 500 significa remover
cerca de 330 palavras — e não há como fazer isso sem eliminar afirmações e
números. Isso é decisão editorial do autor (o que a tese anuncia no resumo),
não trabalho de forma, e o freeze me proíbe. **Reporto para a fila do autor.**

# 2. O que eu fiz: fluidez, dentro das duas restrições

Restrições respeitadas: **parágrafo único** (norma) e **freeze** (nenhum número).
O ganho veio de quebrar as frases mais densas.

| | frases | palavras/frase | maior frase | frases >40 palavras |
|---|---|---|---|---|
| resumo antes | 14 | **59** | 92 | 12 |
| resumo depois | 21 | **39** | 74 | 10 |
| abstract antes | 14 | **57** | 92 | 10 |
| abstract depois | 21 | **38** | 70 | 8 |

**Densidade média caiu 34%.** Texto acadêmico legível fica na faixa de 20 a 25
palavras por frase; 59 era muito acima disso, e 39 ainda é alto — mas o resto do
caminho depende do corte de extensão, que é a decisão do item 1.

## Antes/depois (a pior das três, o item (iv), de 92 palavras)

**Antes** — uma frase, quatro asserções encadeadas:

> (iv) As estratégias de incerteza superam a seleção aleatória na significância
> máxima que 8 sementes permitem ($p=0{,}0078$), recuperando 78\% do Macro F1 do
> teto supervisionado com 15\% do \textit{pool} daquele experimento, e a vantagem
> sobrevive intacta a ruído uniforme de oráculo até $\varepsilon=0{,}4$, faixa
> que cobre o erro observado nos LLMs reais; como nenhum oráculo alcançou o
> critério pré-registrado de 85\% de acurácia, o gate metodológico definiu a
> configuração final (oráculo econômico na fase inicial, oráculo de maior
> acurácia na fase avançada) e tornou o aprendizado com rótulos ruidosos o
> cenário central.

**Depois** — três frases, mesma informação, mesma ordem:

> (iv) As estratégias de incerteza superam a seleção aleatória na significância
> máxima que 8 sementes permitem ($p=0{,}0078$), e recuperam 78\% do Macro F1 do
> teto supervisionado com 15\% do \textit{pool} daquele experimento. A vantagem
> sobrevive intacta a ruído uniforme de oráculo até $\varepsilon=0{,}4$, faixa
> que cobre o erro observado nos LLMs reais. Nenhum oráculo alcançou o critério
> pré-registrado de 85\% de acurácia: o gate metodológico definiu então a
> configuração final, com oráculo econômico na fase inicial e oráculo de maior
> acurácia na fase avançada, e tornou o aprendizado com rótulos ruidosos o
> cenário central.

Mesmo tratamento nos itens (i) e (iii). **As três quebras foram espelhadas no
abstract**, palavra por palavra na estrutura — PT e EN têm hoje **21 segmentos
cada**.

# 3. R1, R2 e humanize: nada a fazer

Medido, não presumido:

| verificação | resultado |
|---|---|
| travessões de prosa (`—` e `---`) | **0** |
| filler / meta-comentário | **0** |
| vocabulário-IA inflado | **0** |
| gerúndio decorativo | 1, e carrega conteúdo |
| negrito | 1, marca o veredito — legítimo |
| siglas (FALCO, LLM, DRI-SL, LCE) | glosadas na 1ª ocorrência |

# 4. Divergências de número contra o corpo: NENHUMA

Este era o item que você pediu para reportar. Varri **os 32 números distintos**
do resumo e procurei cada um no corpo dos seis capítulos: **todos aparecem
literalmente**. Zero divergências. Confirmei inclusive os que mudaram no lote
recente — o corpo na main já traz o braço E em 0,822 e "média de duas sementes".

**Uma imprecisão textual, não numérica**, para o autor decidir: o resumo descreve
a validação como "BERTimbau, **três sementes**". Os braços A–D e os de 20/30/35
mil têm mesmo três; o braço E (15 mil) tem **duas**, como o corpo agora declara.
A generalização não erra nenhum número do resumo — os valores citados são dos
braços de três sementes —, mas a descrição geral ficou mais forte que o corpo.
**Não corrigi** (é conteúdo, e o freeze vale).

# 5. DoD

Compila `exit 0`, **0 erros**, 7 caixas estouradas (idêntico à main), nenhuma
referência indefinida nova. **Freeze provado por medição**: 54 números no resumo
e 45 no abstract, **idênticos** antes e depois.

# 6. Nota sobre a tarefa cancelada

O trabalho da introdução (tarefa 1850) ficou preservado em
`r1r2r6/intro-cap1-DESCARTAVEL` @`93a0fa2`, só como registro. O autor já validou
a introdução; **não peço gate para ela** e ela pode ser apagada.
