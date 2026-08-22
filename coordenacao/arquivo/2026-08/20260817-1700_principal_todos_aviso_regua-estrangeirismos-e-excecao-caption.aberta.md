---
de: principal
para: todos
tipo: aviso
acao_esperada: adotar as duas regras aprovadas pelo autor (docs/criterio-humanizacao.md): régua de estrangeirismos e exceção do travessão em \caption
referencia: proposta do revisor1 · achado do revisor2 (DoD inalcançável) · aprovação do autor 2026-08-17
criada_em: 2026-08-17T17:00:00Z
---
1. ESTRANGEIRISMOS: termo corrente na área fica em itálico sem glosa
   (tweets, embeddings, bag-of-words, cold start, prompt); glosa-se só o
   que a banca pode estranhar (stopwords, stemming, missed cluster effect)
   ou o que tem palavra portuguesa (survey → revisão). Siglas de método
   sempre expandidas na 1ª ocorrência.
2. EXCEÇÃO DO \caption: a proibição do travessão Unicode vale para títulos
   de capítulo/seção/subseção, NÃO para legendas — LoF/LoT não maiusculizam
   e os builds com legendas assim saem verdes. O check-travessao-titulo.py
   trata legenda como AVISO; nenhum DoD de fatia trava por isso.
   revisor1: ajuste o script à regra (é seu) e some a fixture do caso.
