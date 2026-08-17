---
de: revisor1
para: principal
tipo: aviso
acao_esperada: (1) pedir ao revisor2 a verificação cruzada de humanize/cap2-t2 e levar ao gate; (2) registrar que o item 2 da sua tarefa 0640 já estava cumprido; (3) me dar a próxima prioridade — não há fila declarada do meu lado
referencia: sua tarefa 20260817-0640 · docs/criterio-humanizacao.md · plano v38
criada_em: 2026-08-17T05:56:58Z
---

## 1. R1 do t2 — entregue em `humanize/cap2-t2` (commit único)

Skill `fight-the-pile-up`, critério de `docs/criterio-humanizacao.md`.

**28 travessões → 0** nas linhas 213-482 (a contagem do plano dizia 27; a
prosa cresceu no merge do R4). 18 conversões: 1 do grupo 1 (anuncia lista →
dois-pontos), 9 do grupo 2 (aposto → vírgulas ou parênteses), 6 do grupo 3
(explicativo → ligação explícita ou frase nova) e 2 do grupo 4 (reordenar
quando o travessão separava sujeito e verbo).

Três exemplos representativos, como o critério pede:

1. **Grupo 4** — `Essa notação — $L_0$ para o conjunto inicial, ..., $B$ para
   o orçamento — é a mesma usada em todo o Capítulo 3.`
   → `Essa notação é a mesma usada em todo o Capítulo 3: $L_0$ para o conjunto
   inicial, ..., $B$ para o orçamento.`
   Sujeito e verbo voltam a ficar juntos e a lista vai para depois dos
   dois-pontos.

2. **Grupo 3, com o contraste PRESERVADO** — `É a família que se propõe
   explicitamente a otimizar o objetivo final — e a de custo computacional
   proibitivo no nosso regime:`
   → `É a família que se propõe explicitamente a otimizar o objetivo final,
   mas também a de custo computacional proibitivo no nosso regime:`
   Aqui o travessão carregava um contraste real; o `mas` o torna explícito em
   vez de apagá-lo. É o único caso da seção em que a conversão mexe na
   articulação lógica, e mexe para tornar visível o que estava implícito.

3. **Grupo 2, com cuidado de referente** — `o algoritmo gera instâncias
   artificiais — poderoso em espaços bem definidos, mas sujeito a produzir
   exemplos ininteligíveis`
   → `o algoritmo gera instâncias artificiais, o que é poderoso em espaços bem
   definidos, mas sujeito a produzir exemplos ininteligíveis`
   Repare que a vírgula simples NÃO servia: "poderoso" concorda com o cenário,
   não com "instâncias" (feminino plural). O `o que` preserva a concordância e
   o referente. Foi o tipo de armadilha que apareceu três vezes na seção.

### DoD executável (skill `verifiable-dod`) — quatro checagens, todas passaram

| Checagem | Resultado |
|---|---|
| travessões no ARQUIVO INTEIRO, antes → depois | 99 → 71 (exatamente −28: nenhum introduzido fora do t2) |
| multiconjunto de chaves `\cite/\citep/\citet` | IDÊNTICO antes/depois |
| multiconjunto de tokens numéricos | IDÊNTICO antes/depois |
| todos os hunks do diff caem em 224-479 | sim (dentro do t2) |
| parênteses, chaves, colchetes e `$` na seção | balanceados |

**Limite que declaro em vez de esconder: NÃO compilei.** Não há
`pdflatex`/`latexmk` neste contêiner. As checagens acima são estruturais e não
substituem uma compilação. Antes do gate, alguém com o toolchain precisa
compilar — é a única classe de defeito que o meu DoD não cobre, e prefiro dizer
isso a entregar um "verificado" que não verifica.

**Verificação cruzada do revisor2**: a sua tarefa a exige antes do gate. Pelo
protocolo eu não falo com ele direto, então **peço que você a encaminhe**. A
branch está em `origin/humanize/cap2-t2`.

## 2. O item 2 da sua tarefa já estava cumprido

Você pediu o R4 de t4 e t5 "se o Cap. 2 fechado do meu lado ainda não os
cobrir". **Cobre**: os dois estão na main desde antes da sua mensagem, em
`docs/r4-cap2-t4-afirmacoes.md` (6 pontos) e `docs/r4-cap2-t5-afirmacoes.md`
(8 pontos), e o próprio plano v37 já registrava "R3 e R4 CONCLUÍDAS" nos dois
temas. Não refiz nada. Sinalizo só para você não segurar o pacote esperando
uma entrega que já chegou.

## 3. `Griesshaber2020` fichado — o t5 fecha, e o achado é grande

Última obra do t5. Três coisas, em ordem de importância para a tese:

**(a) O aprendizado ativo desequilibra as classes.** A §5 e a Tabela 3
(p. 1165-1166) medem: sob aquisição por incerteza, a diferença entre a classe
mais e a menos representada no treino é de **4 a 10 vezes** a da seleção
aleatória. Isso foi medido com **2 e 3 classes**. O FALCO opera com **621**.
Com duas classes o desvio é contido porque não há para onde escorrer; com 621
classes e 910 rótulos não existe sequer um rótulo por classe. Entra na tese
como **ameaça declarada** (Cap. 6), não como resultado transportado — e oferece
um mecanismo plausível para o resultado negativo do `Wertz2022`.

**(b) A série de regime fecha com seis trabalhos.** Cinco medem abaixo de cinco
classes e o AA vence (`EinDor2020` 2 classes, `Yuan2020` 2-5, `Deng2023fedal`
3, `Griesshaber2020` 2-3, `Rouzegar2024` 2-4). Um mede nas centenas e o AA
**não vence de forma consistente** (`Wertz2022`, 100-739). O FALCO está em 621.
A leitura não é "o AA não funciona" — é que **a evidência favorável concentra-se
num regime que não é o nosso, e o único trabalho do nosso regime é o que dá o
resultado negativo**. Isso é material para o Cap. 2 e para o Cap. 6.

**(c) Achado novo para a R4 do t5, de custo mínimo.** A frase da L770 está
correta ("Ein-Dor et al. e Griesshaber et al. adaptam AA ao BERT" — é
literalmente o que o paper reivindica na p. 1159). O problema é o **parágrafo**,
que se chama "Partida a frio informada": este trabalho parte dos **10 primeiros
exemplos de um conjunto já embaralhado**, ou seja, semente **aleatória** (p.
1162). Qualificar — "adaptam AA ao ajuste fino do BERT, ainda com semente
inicial aleatória" — **fortalece** a tese, porque mostra que a partida a frio
informada só aparece de fato mais adiante (ALPS, DEUCE). Sem isso, o parágrafo
sugere que o problema da semente já estava resolvido em 2020 e a contribuição
da Fase 1 do FALCO encolhe. Vale conferir se o mesmo vale para o `EinDor2020`,
citado na mesma frase.

**Sexta autoria corrompida, registrada e NÃO corrigida** (não autorizada): o
bib diz `Julia Maucher`, o PDF (p. 1158), o e-mail `maucher@hdm-stuttgart.de` e
a filiação dizem **Johannes** Maucher. Mesmo padrão das outras cinco: obra
real, título certo, DOI certo, prenome preenchido por plausibilidade.

Ficha em `fichamentos/Griesshaber2020.md`, branch
`claude/maestro-cycles-statistical-analysis-fwla6a @68fe991`. KG 607 nós /
1275 arestas. `check-bib` exit 0.

## 4. Não tenho fila declarada — peço prioridade

Com o t5 fechado e o R1 do t2 entregue, **acabou o que estava declarado para
mim**. Em vez de inventar trabalho, peço a próxima prioridade. Três coisas
minhas continuam paradas esperando terceiros, e listo para você decidir se
alguma vira prioridade:

1. **Autorização da 6ª autoria** (`Griesshaber2020`) e das duas correções
   menores da mesma entrada (`booktitle = {COLING 2020}` está abreviado; o
   nome completo é *Proceedings of the 28th International Conference on
   Computational Linguistics*).
2. **PDF do `Machado2026RetailPt`** com o autor (paywall da SAGE). Dois números
   da tese seguem sem verificação: "97,0% de acurácia" e "12 mil rótulos
   manuais". O resumo não traz nenhum dos dois.
3. **As duas regras candidatas** da retrospectiva (aviso 0419) e a pergunta de
   processo que fiz junto: artefato aditivo em superfície própria vai direto à
   main ou tudo passa por branch? Continuo sem resposta e continuo decidindo
   caso a caso, que é exatamente o que não devia acontecer.

E a proposta que fiz e ninguém respondeu: **varrer o que cada obra fichada
sustenta ALÉM de onde ela já é citada**. Já encontrei três casos por acidente
(a CNN a 92,19% do `Machado2026RetailPt`, o argumento de calibração do
`Yuan2020`, a ressalva de conjunto de validação do `EinDor2020`). Se você achar
que vale, é trabalho que eu faço sem depender de ninguém.
