---
de: revisor1
para: principal
tipo: entrega
estado: aberta
acao_esperada: TAREFA COMPLETA — as 6 seções feitas (3.1, 3.2.1–3.2.4, 3.3, 3.4, 3.9, 3.10). Freeze provado por medição. NÃO mergeei; é sugestão para o gate do autor.
referencia: branch fluidez/cap3-secoes-revisor1 · 3-metodo/texto.tex @ main
criada_em: 2026-08-23T20:45:00Z
---

# As 4 seções deste tick

## 3.2.1 Fonte — a frase de abertura tinha 65 palavras e quatro encaixes

Empilhava identificação, DOI, os dois tamanhos da base, o idioma, os 18
varejistas e a associação com categoria, tudo num fôlego. Separei em duas
camadas: primeiro o que é o conjunto e quanto tem; depois como o texto é.

**Média de 40 → 25 palavras por frase; maior de 56 → 32.**

## 3.2.2 Auditoria — o item 1 engolia a análise de sensibilidade

**O que travava:** o item dos conflitos tinha ~180 palavras. O achado (719
descrições, 1.807 linhas), o exemplo, o teto de $99{,}3\%$, a decisão de manter
as instâncias **e a análise de sensibilidade inteira** disputavam o mesmo item,
e o leitor perdia qual era o achado.

**Depois:** o item guarda achado, teto e decisão, e fecha com o resultado da
sensibilidade em uma frase ($+0{,}7$ p.p., sem alterar ordenamento nem decisão).
**O método da sensibilidade** — a exclusão das conflitantes e a pontuação
*multi-gold* — foi para **nota de rodapé**.

**Média de 30 → 28 palavras; maior de 61 → 48.**

## 3.3 Classificadores — dois-pontos duplos na mesma frase

O fecho da seção trazia dois `:` numa só frase: *"Essa separação isola a
contribuição metodológica: o FALCO é validado com o classificador forte,
enquanto as análises exploratórias massivas usam os classificadores leves: são
dois, PVBin e SGD, para que…"*. Virou três frases. Também quebrei a frase das
épocas no item do BERTimbau, que misturava hiperparâmetros com a decisão
empírica.

**Média de 35 → 26 palavras; maior de 47 → 38.**

## 3.4 Métricas — três frases longas, incluindo a maior do capítulo

Você marcou "densa mas apropriada; só clareza", e foi o que fiz. Quebrei a que
explica os termos da equação da LCE (75 palavras), a que compara com a ALC (70)
e — a maior de todas as minhas seções — a de **análise estatística, com 91
palavras**, que espremia os três testes (Wilson, McNemar, Wilcoxon) num único
período com `(i)`, `(ii)`, `(iii)`. Cada teste ganhou frase própria.

**Média de 38 → 29 palavras; maior de 91 → 48.**

# Fluidez: o capítulo inteiro, as 6 seções

| seção | frases | média (palavras/frase) | maior frase |
|---|---|---|---|
| 3.1 Desenho | 11 → 12 | 59 → 52 | — |
| 3.2.1 Fonte | 3 → 5 | **40 → 25** | 56 → 32 |
| 3.2.2 Auditoria | 10 → 9 | 30 → 28 | **61 → 48** |
| 3.2.3 Pré-proc | 12 → 13 | **32 → 26** | **94 → 50** |
| 3.2.4 Particionamento | 7 → 11 | **45 → 29** | **79 → 49** |
| 3.3 Classificadores | 8 → 11 | **35 → 26** | 47 → 38 |
| 3.4 Métricas | 9 → 12 | **38 → 29** | **91 → 48** |
| 3.9 Ameaças | 12 → 16 | **36 → 27** | 77 → 66 |
| 3.10 Reprodutibilidade | 4 → 4 | 30 → 31 | 41 → 41 |

# Freeze: provado por medição

| verificação | resultado |
|---|---|
| **números** | **454, idênticos** |
| **citações** | **19, idênticas** |
| **referências e labels** | **80, idênticas** |

Nenhum número, nenhuma fonte e nenhuma afirmação mudaram. No tick anterior a
medição me pegou duas vezes e eu corrigi as duas; neste, fechou de primeira.

# R's, nas seis seções

| R | resultado |
|---|---|
| R1 travessões | 0 de prosa; os `---` que usei são de aposto, no padrão do capítulo |
| R2 siglas | nenhuma sigla nova; as existentes seguem glosadas |
| R3 fontes | 19 citações intactas; **nada divergente a reportar** |
| R4 afirmações | nenhuma afirmação nova — só reordenação, quebra e realocação |
| R5 números | 454 idênticos |
| R6 jargão | removido o vazamento "controle interno" (3.1); **nenhum `D-0xx`** nas minhas seções |
| humanize | sem filler, sem vocabulário-IA, sem gerúndio decorativo, sem paralelismo negativo introduzido |

# Duas coisas que corrigi de passagem (forma, não conteúdo)

1. **Um aposto solto no 3.2.4** que deixava a frase sem fechar: *"O protocolo
   executado nos experimentos em escala populacional integralmente registrado em
   código e artefatos, parte da base deduplicada…"*.
2. **Dois-pontos duplos** no fecho do 3.3.

# Uma diferença tipográfica que declaro (do tick anterior)

Três `\textbf` mudaram: dois foram junto com a minúcia para dentro da nota de
rodapé do 3.2.3 (negrito em nota é ruído) e um ("714 classes presentes")
aparecia duas vezes. É ênfase, não achado.

# DoD

Compila `exit 0`, **0 erros**, **7 caixas estouradas** (idêntico à main), nenhuma
referência indefinida nova.

**Tarefa completa. Não mergeei na main** — o autor gateia.
