---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: corrigir a entrada Selva2021 na branch bibfix/lotes (com lock) para os metadados REAIS abaixo, verificando na fonte antes de aplicar; chave permanece Selva2021 (sem repontuar prosa)
referencia: busca do principal 2026-08-17 · 2-fundam:683 · padrão Naseem2021 (fabricação de metadados sobre obra real)
criada_em: 2026-08-17T00:45:00Z
---

Sexta fabricação de metadados do ciclo, mesmo padrão do Naseem2021: a obra
EXISTE, o registro estava inventado. A entrada alegava "Review on word
embedding techniques and its applications", IJERT 10(01), autores "Selva,
Jeba Princy and Titus, T Shiny" — autores e veículo não conferem.

A obra real (encontrada pelo principal, VERIFIQUE na fonte antes de aplicar):

- **Título**: A Review on Word Embedding Techniques for Text Classification
- **Autores**: Selva Birunda, S. e Kanniga Devi, R.
- **Onde**: capítulo em "Innovative Data Communication Technologies and
  Application" (eds. Raj, Iliyasu, Bestak, Baig), Springer Singapore,
  Lecture Notes on Data Engineering and Communications Technologies v. 59,
  pp. 267-281, 2021
- **DOI**: 10.1007/978-981-15-9651-3_23
- **Tipo correto**: @incollection (era @article)

A alegação da linha 683 (embeddings estáticos vs contextuais) é exatamente
o escopo do capítulo — a frase fica de pé, só o registro muda. Confira no
Crossref pelo DOI e na página do Springer; o autor vai baixar o PDF e subir
em a_sanear/ para fichamento (aviso à parte quando chegar).

Com isso o check-bib deve cair para 2 pendências (Wu2022 e Ahmed2023,
aguardando o merge da prosa que já tem aprovação prévia do autor).

## Resultado (revisor1, 2026-08-17T01:00Z)
SUPERADA pela tarefa 20260817-0110, que mudou a rota antes do resultado final:
em vez de reconstruir Selva2021, a obra real ja existia como Birunda2021. O
que ficou desta tarefa foi a verificacao na fonte (Crossref/Springer), que
confirmou os metadados que voce levantou e alimentou a rota correta.
