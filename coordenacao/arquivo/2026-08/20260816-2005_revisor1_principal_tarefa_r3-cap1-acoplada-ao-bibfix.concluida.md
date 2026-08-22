---
de: revisor1
para: principal
tipo: tarefa
acao_esperada: decidir (com o autor) se a R3 do Cap. 1 vira ciclo-piloto acoplado ao bib-fix; e encaminhar à banca as 2 correções que já apliquei em bibfix/lotes @ 0efc16f para o lote 4
referencia: docs/mapa-duplicatas-bib.md · bibfix/lotes @ 0efc16f · plano cap1.R3 · decisão pendente dec-fila
criada_em: 2026-08-16T20:05:00Z
---
DECISÃO DO AUTOR (transmitida por ele nesta sessão): "vamos acertar as
referências primeiro". Proposta concreta abaixo.

1. R3 DO CAP. 1 ACOPLADA AO BIB-FIX, COMO PILOTO

Fazer a R3 do Cap. 1 ANTES do bib-fix significa editar as mesmas linhas duas
vezes — é exatamente o desperdício que o autor já apontou na decisão pendente
`dec-fila` (humanizar antes de mexer nas citações = editar a mesma superfície
duas vezes). O caminho econômico é o inverso: R3 do Cap. 1 acoplada ao ciclo
do bib-fix, num único movimento.

O Cap. 1 é o piloto natural: tem só 8 citações distintas, contra 132 do
Cap. 2. Se o formato funcionar nele, replica-se no Cap. 2 com escala 16x maior
e risco já conhecido.

Estado das 8 citações do Cap. 1 após o lote 2 (que já executei):
- 4 pós-2022 (prioridade da R3): Bayer2024ActiveLLM, Zhang2025,
  zhang-etal-2022-survey e Daru2024Dissertacao. As três primeiras foram
  corrigidas nos lotes 1-3; falta validar Daru2024Dissertacao, que é a
  dissertação do próprio autor e segue sem DOI nem URL.
- 4 pré-2022: validadas agora, ver item 2.

2. VALIDAÇÃO DAS 4 PRÉ-2022 (feita a pedido do autor) — 2 CORREÇÕES APLICADAS

Conferi cada uma no registro Crossref e na página do venue, não no parecer.
Commit 0efc16f em bibfix/lotes:

- Alsmadi2019: ERRO REAL. O bib trazia "Alsmadi, Izzat"; Crossref e a página
  da Emerald registram "Issa Alsmadi". Corrigido. Demais metadados conferem
  (IJWIS 15(2):155-182, 2019).
- Devlin2019: metadados corretos, mas sem identificador. Acrescentei o DOI
  10.18653/v1/N19-1423 (NAACL-HLT 2019, pp. 4171-4186).
- Souza2020BERTimbau: confirmado integralmente; o DOI já entrara no lote 3.
- Song2014: metadados confirmados (5 autores, Journal of Multimedia 9(5),
  2014). RESSALVA: o DOI está registrado no Crossref mas NÃO resolve para o
  artigo — cai num índice do dblp, porque a Academy Publisher deixou de
  existir. Não alterei: decidir se acrescenta URL alternativa é editorial.

Como isso topicamente pertence ao lote 3 (identificadores), sinalizo para a
banca cobrir no lote 4 e para o revisor2 não refazer.

3. CORREÇÃO DE UMA OBSERVAÇÃO MINHA ANTERIOR (denominador dos 30%)

Eu havia levantado que o Cap. 1 enuncia "30% do pool" enquanto o Cap. 3
pré-registra "B = 30% de |U0|", e sugerido que faltava declarar a divergência
(princípio VI). RECHECADO NO TEXTO DE HOJE: a divergência JÁ está declarada,
em dois pontos do Cap. 3 — na Seção de particionamento ("essa re-baseação do
denominador é declarada e suas consequências são discutidas nas limitações") e
na Validade ("os percentuais reportados no Cap. 5 referem-se sempre ao
denominador de 50 mil, e a primeira menção de cada resultado o explicita").
O espelho Cap. 1 x Cap. 3 está COERENTE: ambos no denominador do pool de 50
mil. Retiro o apontamento; não há ação pendente aí.

Fica de pé apenas uma verificação futura, que é da R5 do Cap. 5 e não minha:
o Cap. 3 promete que "a primeira menção de cada resultado explicita o
denominador" — isso é uma promessa checável por script quando a R5 do Cap. 5
abrir.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
