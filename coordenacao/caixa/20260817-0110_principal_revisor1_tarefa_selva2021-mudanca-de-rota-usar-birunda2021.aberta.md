---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: SUBSTITUI a rota da tarefa 20260817-0045 (que você já claimou): NÃO reconstruir Selva2021 — a obra real JÁ EXISTE no repositório como Birunda2021 (fichada, com PDF); remover Selva2021 e repontuar a citação
referencia: tarefa 20260817-0045 (em-andamento) · referencias.bib @Birunda2021 · fichamentos/Birunda2021.md · referencias-pdf/Birunda2021.pdf · 2-fundam:683
criada_em: 2026-08-17T01:10:00Z
---

PARE antes de reconstruir a entrada: o principal descobriu que a obra real
("A Review on Word Embedding Techniques for Text Classification", Selva
Birunda & Kanniga Devi, ICIDCA 2020/Springer, pp. 267-281) **já está
cadastrada como `Birunda2021`** — @incollection correta, fichamento feito e
PDF arquivado. É exatamente o cenário do seu invariante ("verificar se a
obra corrigida já está sob outra chave") — desta vez pego ANTES do commit.

Rota correta (mesma do caso Naseem):

1. REMOVER a entrada `Selva2021` (fabricação de metadados, órfã após o
   passo 2).
2. REPONTUAR 2-fundam:683: `\cite{Selva2021, Goldberg2017}` →
   `\cite{Birunda2021, Goldberg2017}` (troca de chave, sem tocar a frase —
   dentro da sua alçada, como no Naseem).
3. Na entrada `Birunda2021`: acrescentar o DOI, conferido na fonte:
   10.1007/978-981-15-9651-3_23 (Crossref/Springer). O fichamento tem
   `doi: ""` — preencher lá também (uma linha; fichamento é superfície de
   revisores).
4. DoD: check-bib sem a pendência Selva2021 (devem restar só Wu2022 e
   Ahmed2023); zero órfã nova; a citada some, a fichada assume.

Bônus de contexto: o volume inteiro do livro já passou pela triagem uma vez
(`_TRIAGEM_volume_ICIDCA2020_capitulo_Birunda_ja_arquivado.pdf`) — quem
triou extraiu o capítulo e arquivou. O autor ia subir o livro de novo; o
principal avisou que não precisa.
