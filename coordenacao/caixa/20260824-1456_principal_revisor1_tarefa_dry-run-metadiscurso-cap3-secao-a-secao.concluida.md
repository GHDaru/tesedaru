---
de: principal
para: revisor1
tipo: tarefa
referencia: 3-metodo/texto.tex (main @7974563) · regra nova em docs/criterio-humanizacao.md (seção final) · scripts/checa-metadiscurso.py
acao_esperada: dry run de LEITURA, seção a seção, do Cap.3 inteiro; LAUDO apenas (nenhuma edição de .tex); recibo de 1 linha
prazo: auditoria do autor em curso no Cap.3
---

# Dry run do Cap.3: metadiscurso encenado e registro acadêmico (LEITURA, não regex)

Encomenda do autor. Contexto: na auditoria de hoje nasceu uma regra nova,
registrada em `docs/criterio-humanizacao.md` (seção "Metadiscurso: sóbrio
sim, encenado não") com verificador `scripts/checa-metadiscurso.py`. O
verificador é regex e só pega frases fixas. O autor quer um **dry run lido**:
você lê o capítulo inteiro, seção a seção, como leitor humano, procurando o
que o regex não alcança.

## O que procurar (por ordem de prioridade)

1. **Metadiscurso encenado em formulação nova** (o alvo principal): drama de
   falta/necessidade, apelo ao leitor, palco/suspense, em frases que não
   estão na lista do verificador. Leia a regra antes; o teste operacional
   dela decide o veredito.
2. **Registro não acadêmico**: coloquialismos, tom de marketing, metáforas de
   palco fora de figura/legenda.
3. **Jargão sem definição na 1ª ocorrência** (regra do autor: define ou não
   coloca), inclusive jargão de engenharia de software em texto para leitor
   de ML.
4. **Âncoras a experimentos/pilares na prosa** (regra do autor de hoje: a
   prosa refere a substância; identificadores E*/pilar-N só onde a função é
   localizar: tabela de rastreabilidade, nota da tabela, §3.10).

## Como entregar

- LAUDO em arquivo na sua branch (nenhuma edição no .tex — o principal
  gateia com o autor): para cada achado, `linha | citação exata | qual regra
  fere | reescrita sugerida`. Achados ordenados por seção (3.1 a 3.10).
- Se um padrão novo merecer entrar no verificador regex, proponha o padrão
  no fim do laudo.
- Vale declarar seções limpas ("3.x: nada encontrado") — o autor quer o
  capítulo todo coberto, não só os achados.
- Recibo de 1 linha na caixa (`de:revisor1 para:principal`,
  `branch@sha:caminho`).

Restrições: congelamento vige (números intocáveis); zero travessões nas
sugestões; sugestões devem passar no próprio checa-metadiscurso.py.
