---
de: revisor1
para: principal
tipo: aviso
acao_esperada: APROVO a entrega do revisor2; mas levar ao autor o achado bloqueante de CONTEÚDO (3ª parte do critério do §1.3), que precede a entrega e é decisão dele
referencia: cruzada de claude/tesedaru-activelearning-maestro-bf56y7 @1786296, 6-conclusao/texto.tex
criada_em: 2026-08-23T22:55:00Z
---

Identidade: **Revisor 01** (ADR 0011). Cruzei o SHA que você passou; ele resolve.
Medi tudo de novo com meus instrumentos, sem aceitar os números do revisor2.

# VEREDITO: **APROVA** a entrega — com um achado bloqueante de conteúdo que NÃO é dele

## Régua máxima: cumprida, e confirmada por medição independente

| | main | entrega do revisor2 |
|---|---|---|
| densidade | 53,9 p/f | **19,3 p/f** (faixa 18–24) |
| frase mais longa | 255 | **40** |
| frases >40 palavras | 21 | **0** |

O revisor2 relatou 53,8 → 18,9 e máx 40. Minha medição dá 53,9 → 19,3 e máx 40.
A diferença é de variante de medidor, não de fato: **a alegação central, zero
frases acima de 40 palavras, confere exatamente**.

**Freeze**: 63 números, 4 `\ref`, 7 `\label`, 14 `\emph`, 17 `\textbf`
IDÊNTICOS. Única diferença: `+1 \cite{DaruActiveLearning}` — é a rota
bibliográfica autorizada, a chave existe na bib da main e na branch dele, e está
citada em lugar correto (nomeando a biblioteca como entrega).

**Forma**: zero travessão em prosa (antes e depois), zero caminho interno, zero
marcador de IA, e nada subiu em relação à main.

**Aritmética dos denominadores** (conferi porque é o que a banca refaz):

    34.724 / 231.490 = 15,00%   texto: 15,0%
    20.000 / 231.490 =  8,64%   texto: 8,6%
    11.936 / 231.490 =  5,16%   texto: 5,2%
    30.000 / 231.490 = 12,96%   texto: 13,0%

Os quatro fecham. **Coerência tripla: sem contradição.**

**Arco narrativo**: o §6 final reenuncia o critério nas palavras do §1.3
(*"pede $\ge 95\%$ da acurácia da supervisão completa do \textit{pool} de
referência, que é a métrica do pré-registro, com no máximo 34.724 rótulos, ou
$15\%$ da população deduplicada"*) e responde com veredito de duas metades.
Passa no teste do leitor de banca.

# ACHADO BLOQUEANTE (conteúdo, não forma — precede esta entrega)

O critério do §1.3 tem **três** conjunções, não duas:

1. no máximo 34.724 rótulos ($15\%$ da população deduplicada);
2. pelo menos $95\%$ da acurácia da supervisão completa do \textit{pool};
3. **"superando com significância estatística a seleção aleatória e a seleção
   por incerteza sob o mesmo orçamento"**.

O Cap.6 declara *"O critério é atingível dentro do teto"* atendendo **1 e 2**.
A conjunção **3 não aparece no capítulo**: `superando`, `aleatória` e
`significância estatística` dão **zero ocorrência** ligadas ao veredito (a única
"significativa comprovada" é sobre os papéis de oráculo, v4-pro vs.\ flash).

E há tensão com a evidência do próprio Cap.5, que afirma textualmente:

> **"A seleção ativa compra Macro F1 e cobertura, não acurácia."**

Ou seja: na métrica que o critério elege (acurácia, por ser a do pré-registro),
o braço ativo **não** demonstra superioridade significativa sobre o sorteio.
Declarar "o critério é atingível" sem tratar a conjunção 3 é o ponto exato em
que a banca vai perguntar *"e a terceira parte do seu próprio critério?"*.

**Não corrigi nada** (FREEZE do capítulo de conclusão, e a decisão é de
conteúdo). Três saídas possíveis, todas do autor: (a) reportar a conjunção 3
explicitamente com o resultado que houver, ainda que negativo; (b) declarar a
divergência pré-registrado × executado onde o veredito é dado, como o
princípio VI já obriga em outros pontos; ou (c) emendar o critério por ADR, se
a intenção original era outra. Não é falha do revisor2: ele recebeu o texto
assim e cumpriu a régua de forma que lhe foi pedida.

# Resumo

Forma: **APROVADA**, régua máxima cumprida e verificada de forma independente.
Conteúdo: **um item para o autor**, anterior a esta entrega.
