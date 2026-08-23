---
de: revisor1
para: principal
tipo: aviso
acao_esperada: pegar dc4f4b7 no commit unico; decidir sobre 737a42d (condicional); e levar ao autor os 2 achados que NAO sao fluidez
referencia: branch fluidez/cap3-r1-melhorias-finais @ dc4f4b7 (+ 737a42d condicional)
criada_em: 2026-08-23T21:30:00Z
---

Identidade confirmada pelo titulo da sessao (ADR 0011): **Revisor 01**.
Ritual v1.8 feito com o refspec explicito da `mensageria`.

Resposta: **(a)**, tenho melhorias. Branch sai de `origin/main@dd4e21c`, entao
aplica direto no seu commit unico.

## dc4f4b7 — 5 melhorias, todas nas MINHAS partes

Nenhuma duplica suas 4 quebras pendentes. Nenhuma toca as enumeracoes que voce
julgou legitimas.

| # | onde | antes | depois |
|---|---|---|---|
| A | abertura | "quatro pilares" **78 pal.** | 5 frases |
| B | abertura | "Todos os experimentos" 48 pal. | 2 frases |
| C | 3.2 | "quatro decisoes encadeadas" 47 pal. | 2 frases |
| E | 3.9 | "Tres mitigacoes sao adotadas" **68 pal.** | 4 frases |
| F | 3.9 | "Segunda: o orcamento" 46 pal. | 2 frases |

A **A** e a frase mais longa do capitulo inteiro. Exemplo:

> ANTES: "A investigacao esta organizada em quatro pilares empiricos, cada qual
> associado a um experimento identificado e reproduzivel: o impacto da
> composicao do conjunto inicial de rotulagem L0; a construcao de um L0
> informativo sem acesso a rotulos, via o algoritmo DRI-SL; a viabilidade, o
> custo e o perfil de erro de modelos de linguagem de grande porte (LLMs) como
> oraculos de rotulagem; e a avaliacao integrada do FALCO contra metodos de
> referencia sob o mesmo orcamento de rotulagem."

> DEPOIS: "...cada qual associado a um experimento identificado e reproduzivel.
> O primeiro mede o impacto da composicao do conjunto inicial de rotulagem L0.
> O segundo trata da construcao de um L0 informativo sem acesso a rotulos, pelo
> algoritmo DRI-SL. O terceiro examina a viabilidade, o custo e o perfil de erro
> de modelos de linguagem de grande porte (LLMs) como oraculos de rotulagem. O
> quarto avalia o FALCO de forma integrada, contra metodos de referencia e sob o
> mesmo orcamento de rotulagem."

Medido: media **27,5 -> 26,0** pal./frase; frases >40 pal. **31 -> 26**.
**Freeze EXIT 0** contra `origin/main`: 264 numeros, 23 citacoes, 55 refs, 26
labels IDENTICOS. Zero travessao novo, zero caminho interno.
pdflatex+bibtex: 0 erro, 0 citacao indefinida, 0 referencia indefinida.

## 737a42d — CONDICIONAL, commit separado, descartavel

3.10 "Os resultados originais..." (69 pal.). Voce disse que a "proveniencia
validada pelo autor" nao deve ser forcada. Ha **duas** frases de proveniencia:
a de 62 pal. no 3.1 (exame de qualificacao) e esta, de 69, no 3.10. Nao sei qual
o autor validou. **Se for esta, descarte o commit** — o dc4f4b7 fica de pe
sozinho. Nao decidi por voce porque a informacao que decide e sua.

## Dois achados que NAO sao fluidez (esses sim, para o autor)

**1. A auto-contencao entrou, mas a rastreabilidade saiu junto.** A main removeu
os caminhos (0 restantes, so o identificador de modelo — correto). Mas a nota da
tabela agora diz apenas: *"Os artefatos de todos os experimentos acompanham o
repositorio de codigo da tese"*. **Nao ha referencia bibliografica que diga QUAL
repositorio.** Nenhuma entrada de software foi citada (`DaruActiveLearning`:
0 ocorrencias na main; 0 na bib). O leitor nao consegue resolver o ponteiro.
Isso e afirmacao orfa (principio III) e enfraquece o principio V (nenhum numero
sem artefato rastreavel). O autor pediu *"apenas citacao bibliografica **se
necessario**"* — este e exatamente o caso necessario. As duas entradas `@misc`
prontas (`DaruActiveLearning`, `DaruActiveTextClassification`, com URL) estao em
`fluidez/cap3-secoes-revisor1@a254da7`, que o gate nao levou. Recomendo levar so
elas.

**2. O 3.5.1 nunca recebeu passada de fluidez de ninguem.** Pelos gates: voce
pegou 3.2.4/3.8.x, o revisor2 pegou 3.5.2, 3.6, 3.7.1-3.7.3, 3.8.2. O **3.5.1
(Sensibilidade a amostragem aleatoria)** ficou de fora: **40,2 pal./frase, frase
maxima 78** — empatada com a pior do capitulo, e a unica razao de o maximo do
Cap.3 continuar em 78 depois das minhas quebras. Nao e minha superficie e nao
toquei. Vale uma tarefa.

## Nota de processo

Os dois instrumentos (`mede-fluidez-prosa.py`, `mede-freeze-tex.py`) tambem nao
entraram no gate; reinstalei-os em dc4f4b7. E **corrigi um defeito meu**: o
`mede-freeze-tex.py` que eu commitei subiu sem a linha de `import` e quebrava ao
ser chamado. Sem ele o DoD de freeze nao e executavel (principio IX). Estava
errado no que entreguei; esta certo agora.

## Nao verificado por mim

Principio VI: a cruzada continua pendente. O numero e meu; o julgamento de que
ficou melhor nao pode ser meu.
