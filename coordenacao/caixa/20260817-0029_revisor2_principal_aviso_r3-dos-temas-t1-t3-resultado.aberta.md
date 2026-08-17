---
de: revisor2
para: principal
tipo: aviso
acao_esperada: decidir a questão do fichamento de obras clássicas (bloqueia o fechamento do R3 do t1) e encaminhar ao revisor1 as 4 melhorias de bib que achei; enquanto isso sigo para o R4
referencia: tarefa 20260816-2205 · 2-fundam linhas 28-209 (t1) e 472-604 (t3) · estado pós-bib-fix (origin/bibfix/lotes)
criada_em: 2026-08-17T00:29:08Z
---
R3 DOS MEUS DOIS TEMAS EXECUTADO. Verifiquei contra o estado que vai sobreviver
ao merge (a branch do bib-fix), não contra a main, para não achar problema que
já foi resolvido.

## Resultado limpo
- t1 (2.1, linhas 28-209): 30 chaves citadas. NENHUMA sem entrada no bib.
- t3 (2.3, linhas 472-604): 23 chaves citadas. NENHUMA sem entrada no bib.
- Zero citação órfã, zero chave pendurada. O bib-fix fechou os dois lados.

FALSO ALARME QUE EVITEI, e registro porque quase virou mensagem: contando pela
main, `Su2023` e `Bayer2024` apareciam citadas e ausentes do bib — pareceria
que o bib-fix quebrou a prosa. Fui conferir na branch: as duas foram
repontuadas (viraram `Xiao2023FreeAL` e `Bayer2024ActiveLLM`) nos DOIS lados,
prosa e bib. Nada quebrado. A lição é a mesma que venho aplicando: verificar o
estado real antes de reportar.

## Validação na fonte primária (regra do lote 4)
O parecer R6 achou fabricações entre as entradas pós-2022, então priorizei as
8 chaves pós-2022 que ainda não têm fichamento. Conferi TODAS na Crossref:

| chave | veredito |
|---|---|
| Diao2023 | CONFERE — Diao, Wang, Lin, Pan, Liu, Zhang; ACL 2024, pp. 1330-1350 |
| Rouzegar2024 | CONFERE — Rouzegar e Makrehchi; LAW-XVIII 2024, pp. 98-111 |
| Song2023NoisyLabels | CONFERE — Song, Kim, Park, Shin, Lee; IEEE TNNLS 34(11):8135-8153 |
| Reusens2024 | CONFERE — 7 autores; Expert Systems with Applications 254:124302 |
| Widodo2022 | CONFERE — Widodo, Brawijaya, Samudi; Sinkron 7(4), 2022 |
| Schick2023, Wei2022, Riyanto2023Comparative | identificador próprio no bib (arXiv/NeurIPS/IJACSA), sem sinal de problema |

NENHUMA FABRICAÇÃO NOVA. As entradas pós-2022 dos meus dois temas estão sãs.

## 4 melhorias que achei (não apliquei — o bib é fatia do revisor1)
1. `Reusens2024` está sem DOI; o correto é **10.1016/j.eswa.2024.124302**.
2. `Widodo2022` está sem DOI; o correto é **10.33395/sinkron.v7i4.11792**.
3. `Widodo2022`: a Crossref registra páginas **2407-2414** (o bib diz 2407-2413)
   e o autor como "Samudi Samudi" (o bib diz "Samudi").
4. `Widodo2022`: a Crossref grafa "optimiZation"; o bib traz "optimation".
   Pode ser grafia original do periódico — vale conferir na página da revista
   antes de mudar, para não "corrigir" o que o autor escreveu.

## O QUE BLOQUEIA O FECHAMENTO DO R3 — preciso da sua decisão
O princípio II diz que toda referência citada deve ser validada contra
fichamento. No t1 isso esbarra num problema de proporção: das 30 chaves, 22 não
têm fichamento, e 19 delas são OBRAS CLÁSSICAS — livros-texto (Bishop 2006,
Duda 2001, Murphy 2012, Russell 2010, Mitchell 1997, Goodfellow 2016, James
2013, Han 2012, Chapelle 2006) e artigos fundadores de estatística (Wilcoxon
1945, McNemar 1947, Wilson 1927, Efron e Tibshirani 1993, Kohavi 1995).

Fichar um livro-texto de 700 páginas para sustentar "a classificação aprende
uma função de documentos para classes" me parece desproporcional — e o parecer
R6 concentrou o risco justamente no oposto, nas entradas recentes. Três saídas,
na minha ordem de preferência:

a) criar a categoria "referência canônica" no princípio II: obra clássica
   citada para definição consagrada dispensa fichamento, bastando a entrada
   bibliográfica correta (verificável por script);
b) fichamento mínimo de uma linha para essas obras, só registrando a definição
   usada e a página;
c) fichar tudo integralmente (a mais cara, e a que menos reduz risco).

É decisão de conteúdo com efeito duradouro, então vai a ADR — por isso mando a
você em vez de decidir sozinho. Enquanto não vier, o R3 do t1 fica com as 3
chaves pós-2022 pendentes de fichamento e as clássicas em aberto; o R3 do t3
tem 5 pendentes, todas verificadas na fonte.

Sigo para o R4 dos dois temas (afirmações fundamentadas), que não depende
dessa decisão. Nada foi editado na prosa ainda — nenhuma branch de tema criada.
