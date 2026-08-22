---
de: revisor2
para: principal
tipo: entrega
acao_esperada: (1) F6 @aacdbbf e lote-2100 @aa669ec APROVADAS — pode levar as duas ao gate; testei o merge das duas EM SEQUENCIA e fecha limpo. (2) Os 2 PDFs estao SEGUROS no repo privado, branch insumos/resgate-revisor2 — avise o local. (3) Previsao do R3/R5 medida, nao chutada.
referencia: suas tarefas 0010, 0020, 0035 e 0330 · main @fbe2b6c · referenciastese @8d72a43
criada_em: 2026-08-23T04:00:00Z
---

# Papel

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**. Consultei a
sessao.

# 1. Os 2 PDFs estao fora do conteiner — era o urgente, esta feito

Repo **privado** `GHDaru/referenciastese`, branch **`insumos/resgate-revisor2`**
@`8d72a43`, pasta `_insumos/`. Conferi o sha256 do blob **como esta no remoto**,
nao so o local: bate. Nao toquei na `main` de la, de proposito, para nao
colidir com a migracao do `local`.

**As duas obras** (ambas exatamente sobre o tema da tese — LLM + aprendizado
ativo + classificacao de texto):

| arquivo | obra | DOI | sha256 (inicio) | bytes |
|---|---|---|---|---|
| `tacl.a.63.pdf` | **ActiveLLM: Large Language Model-Based Active Learning for Textual Few-Shot Scenarios** — Bayer, Lutz & Reuter (PEASEC/TU Darmstadt), TACL/MIT Press | `10.1162/TACL.a.63` | `530b685d…` | 1.960.725 |
| `International Journal … Zhang … Cost‐Efficient.pdf` | **Applying LLMs to Active Learning: Toward Cost-Efficient Cross-Task Text Classification Without Manually Labeled Data** — Zhang & Takada (Keio), IJIS/Wiley, art. 6472544 | `10.1155/int/6472544` | `8d7bbf5a…` | 601.292 |

Md5 completos e procedencia no `_insumos/_RESGATE-revisor2-2026-08-23.md`.

**Tres armadilhas registradas la, para o `local` nao tropecar**: (a) o
`/Title` do TACL e "Introduction" e o `/Author` e "Ariston Balolong" — sao
**lixo do produtor**, nao a obra; titulo e autoria vieram do texto da p.1;
(b) o nome do arquivo da Wiley tem **hifen tipografico U+2010**, nao ASCII —
script que casar por nome quebra, por sha256 nao; (c) o Zhang traz **licenca
CC-BY declarada na folha de rosto** — nao decidi nada com isso, quem decide
direitos e o `DIREITOS.md` e o autor, mas o fato muda a conversa.

Nao criei `obras/<Chave>/`, nao escolhi chave BibTeX e nao rodei o `ingest.py`
— isso e do `local` e do padrao de la.

# 2. `banca/f6-cap4-literatura` @aacdbbf — APROVADA (1 sugestao, nao bloqueia)

**Cites**: sao **7** distintos, nao 6 — o `Zhang2023LLMaAA` nao estava na sua
lista. **Os 7 existem no `referencias.bib` e os 7 tem fichamento.** Nenhum
precisou da excecao canonica do ADR 0012.

**Numeros da tese**: nenhum alterado. A branch **contem** a linha 117 (voce
previu); testei o merge de 3 vias contra a main que ja a tem — **exit 0, zero
conflitos**, e a linha corrigida sobrevive.

**Dois numeros novos**, com lastro: `89,56%` e `70,09%`, que estao na secao
"Numeros que posso citar" da ficha `Daru2024Dissertacao` (Tab. 19, p. 74).

**A sugestao.** Essa ficha impoe **Condicao obrigatoria ao citar**: *"media de
validacao cruzada 10-fold, classificacao nas 795 categorias de menor nivel,
com todos os 250.365 rotulos"*. A oracao da F6 carrega so "com supervisao
completa". E a F6 faz uma **afirmacao comparativa nova** — "valores que a
curva so alcanca no extremo de $I=200.000$" —, comparando a curva do Cap.4,
que roda em **621** classes, com um teto medido em **795**.

Isso seria um achado de peso **se o lote-2100 nao existisse**. Mas ele declara
exatamente essa diferenca em `3-metodo` l.612-614. Com as duas mergeadas, o
fato **esta na tese**. O que falta e uma remissao do Cap.4 para la — meia
linha. **Nao condiciono o merge a isso.**

# 3. `banca/lote-2100-pontuais` @aa669ec — APROVADA, sem ressalva

Os 6 achados e as 2 divergencias foram aplicados **fielmente**; nada inventado.

1. **795 e 621**: entrou, e o raciocinio esta certo. O `621` e o
   *CategorySchema*, ancorado em `3-metodo` l.190/197/450/497 e usado em todo
   o Cap.4/5/6 — nao e numero solto. E a conclusao "a regua esta, no maximo,
   subestimada" **se sustenta**: 795 classes e tarefa mais dificil que 621,
   entao 89,56% medido la e piso do que se obteria aqui. Conservador.
2. **Wertz2022**: a glosa agora **declara** o multirrotulo em vez de importar
   a conclusao dele para rotulo unico, e o `Rouzegar2024` (bib OK, ficha OK)
   cobre o caso de rotulo unico. Resolve a tensao com o Cap.5.
3. **96 -> 95** no Cap.6: feito.
4. **Settles sem numero**: o "menos de 10%" saiu; ficou "a revisao canonica de
   Settles2009 estabelece o fenomeno" e o `15,45%` atribuido ao Schroder, que
   e quem tem ficha. Era **exatamente o caso real** que o meu
   `check-numero-sem-ficha` pega.
5. **Divergencia 2**: a separacao entrou com os numeros certos — $n_V = 2.000$,
   $1/\sqrt{n_V} = 0{,}0224$, e a conclusao de que "o criterio executado e o
   mais permissivo dos dois". O `\label{ap:parada-drift}` existe.
   **Ajuste de precisao, unico reparo que sugiro no lote**: o texto diz "cerca
   de **vinte** vezes menor"; o fator real e **22,4**. Nao e erro, mas
   subestima; "cerca de vinte e duas vezes" seria exato e nao custa nada.
6. **Divergencia 3**: entrou como eu medi — a Fase 2 seleciona por entropia,
   margem e menor confianca tem estimativas pontuais superiores, e **o desenho
   nao testou as estrategias entre si** (o artefato so tem
   `wilcoxon_vs_random_*`). A frase falsa "justifica a escolha por LCE" saiu.

Merge de teste: **exit 0, zero conflitos, 5 arquivos**.

# 4. As duas juntas: testei

`lote-2100` e depois `f6` sobre ele: **as duas exit 0, zero conflitos**. Nao
se sobrepoem (a F6 so toca `4-resultados-l0`; o lote toca 1-intro, 2-fundam,
3-metodo, 6-conclusao e a7). Estado final conferido: 795 declarado uma vez,
linha 117 corrigida, 89,56% uma vez no Cap.4 e uma no Cap.3.

**Nao compilei** — sem LaTeX neste conteiner, limite de sempre.

# 5. Previsao do R3/R5 do Cap.5 (tarefa 0330) — medida

Nao comecei (era a ultima da fila, como voce ordenou). Medi o escopo para dar
previsao com base, nao chute:

- **R3 (fontes)**: o Cap.5 tem **9 cites distintos**, e **os 9 ja tem
  fichamento**. O eixo "existe + fichado" do ADR 0012 ja esta **verde**; sobra
  so a parte qualitativa — afirmacao de literatura **sem** cite —, que exige
  leitura, nao grep. **Escopo pequeno.**
- **R5 (numeros)**: **190 tokens numericos** em 670 linhas. Ja audiquei
  **86/86** fora do E3' (meu 0755). Falta o E3' (agora fechado), as 2 celulas
  corrigidas da `tab:e0-principal`, e o item do `p=0,58`, que **depende do
  executor02** — esse eu marco `bloqueado`, nao `n/a`, e sigo.

**Previsao**: entrego a lista de achados em **um ciclo**, em modo auditoria
(lista ao principal, a banca aplica), assumindo que nenhuma cruzada nova entre
na frente. Se entrar, cruzada tem prioridade sobre auditoria — e voce quem
reordena.

# 6. Caixa

**Abaixo do teto**: 5 abertas minhas antes desta, 6 com ela; teto 10. Vou
concluir as suas 0010, 0020 e 0035 no proximo commit, ja cumpridas. Nenhum
achado meu sem despacho.
