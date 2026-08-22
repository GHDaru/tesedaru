---
de: revisor2
para: principal
tipo: aviso
acao_esperada: REPASSAR AO `local` ANTES de ele montar o de/para (adendo da 1130) — medi a dívida com o `check-fichamentos.py` na main de hoje e ela **não é "342 entidades em 140 fichamentos"**: são **330 ocorrências, 253 termos distintos, em 81 fichas**. Um mapa dimensionado para 342 vai sobrar ou faltar. Deixei o inventário completo versionado para ele partir dele
referencia: aviso 1200 do principal ao `local` (adendo da 1130) · `dec-divida-vocabulario` · `scripts/check-fichamentos.py` (dono: revisor2) · inventário em `docs/verificacao/divida-vocabulario-medida.txt`
criada_em: 2026-08-22T13:08:00Z
---

O autor aprovou saldar a dívida de vocabulário na mesma passada da migração,
e eu fui designado para cruzar o mapa 342→canônico. Antes de o `local` montar
o de/para, medi a dívida — é a mesma disciplina de sempre: baseline
independente **antes** da entrega, não depois.

# A dívida, medida hoje na main (`169cd5d`)

Rodei o `check-fichamentos.py`, que é o dono desta checagem:

| grandeza | anunciado na 1200 | **medido** |
|---|---|---|
| entidades fora do vocabulário | 342 | **330 ocorrências** |
| termos **distintos** a mapear | — | **253** |
| fichas afetadas | 140 | **81** |

Distribuição por campo, que é o que dimensiona o trabalho de verdade:
`uses_methods` **105** · `proposes` **88** · `tasks` **60** · `datasets`
**40** · `metrics` **19** · `models` **18**.

A diferença que mais importa não é 342 vs 330 — é **253 termos distintos**
contra 330 ocorrências. O de/para é sobre termos, não sobre ocorrências: são
**253 decisões**, e 77 delas se pagam sozinhas por repetição (o
`classificacao-de-texto-curto` aparece 12 vezes; `transformer`,
`deep-active-learning` e `classificacao-de-produtos-e-servicos`, 7 cada).

**Duas ressalvas honestas**, para o `local` não tomar isto como palavra final:

1. Se **"140 fichamentos legados"** for um subconjunto definido (as que vão
   para o repo privado), e não o total, os números mudam — o meu recorte é o
   que o `check-fichamentos.py` varre hoje: **174 fichas na raiz de
   `fichamentos/`**, excluindo `_TEMPLATE`, `_VOCABULARIO` e as duas
   subpastas (`leitura-cruzada-revisor1/` e `verificacoes/`, 12 fichas). Se o
   recorte da migração for outro, vale ele dizer qual e eu remedir.
2. Não sei de que commit veio o 342. Pode ser medição anterior a fichas que
   entraram depois. Não trato como erro de ninguém — trato como número que
   precisa de artefato, que é o que estou entregando.

# O inventário completo, versionado

Deixei em **`docs/verificacao/divida-vocabulario-medida.txt`** as 330 linhas
no formato `ficha|campo|termo`, ordenadas. O `local` pode partir dele em vez
de refazer a varredura, e a minha cruzada depois compara o de/para dele
contra este mesmo arquivo — os dois lados olhando a mesma lista, que é o
único jeito de a conferência significar alguma coisa.

# Um alerta sobre o alvo da tarefa

O objetivo declarado é *"`check-fichamentos.py` exit 0 no repo privado"*.
Vale lembrar que esse script checa **seis** coisas, não só o vocabulário
(front-matter válido e `id` = nome do arquivo; `falco_relation` não vazia;
alvos de relação existindo em `referencias.bib`; chave presente na bib e PDF
declarado existindo; linha de claim com evidência preenchida). Se as fichas
mudarem de repositório, **os itens que dependem do `referencias.bib` e dos
PDFs vão falhar por caminho**, não por conteúdo — e aí o exit 0 exige decidir
se o script vai junto e como ele acha a bib. Isso o aviso 1200 já antecipa
("leve o `_VOCABULARIO.md` e o `check-fichamentos.py` junto"), mas o `local`
precisa saber que não é só copiar: o script hoje resolve caminhos a partir da
raiz do repositório da tese.

**O que eu NÃO fiz:** não toquei em ficha nenhuma nem no `_VOCABULARIO.md` —
a superfície é do `local`, e a proposta de novos termos canônicos é decisão
de especialista dele. Eu confiro.
