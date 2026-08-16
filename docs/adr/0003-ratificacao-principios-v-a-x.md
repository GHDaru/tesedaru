# ADR 0003 — Ratificação dos princípios V–X da Constituição da Tese

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú ("Pode mergear e ratifico os princípios V a X.")

## Contexto

O ADR 0002 adotou a Constituição da Tese v1.0.0 com os princípios I–IV ratificados
(ditados pelo autor) e seis princípios adicionais (V–X) em estado PROPOSTO,
sugeridos pelo agente a partir de lições concretas do próprio trabalho: veredito
desatualizado no resumo (VIII), jargão E3′ na introdução (VII), varredura post-hoc
do P4 (VI), prática "nenhum número sem artefato" (V), DoD verificável do Maestro
(IX) e a humanização calibrada do ADR 0001 (X).

## Decisão

Ratificamos os princípios V–X sem alteração de texto. A Constituição da Tese passa
a v1.1.0 com dez princípios ratificados: V. nenhum número sem artefato rastreável;
VI. divergência pré-registrado × executado declarada onde ocorre; VII. terminologia
em camadas; VIII. consistência espelhada resumo/abstract/corpo; IX. DoD de texto
verificável; X. estilo humano calibrado.

## Alternativas consideradas

- **Ratificar um subconjunto**: o autor podia aparar — não o fez; ratificou os seis.
- **Manter como propostos por mais um ciclo**: postergaria a vigência — descartada
  pela decisão explícita do autor.
- **Não ter princípios além dos ditados**: deixaria as lições recorrentes sem regra —
  descartada.

## Consequências

- (+) As seis lições viram regra verificável para todos os ciclos futuros.
- (+) O princípio IX habilita automação (scripts de checagem de siglas, números e
  compilação como gate de merge).
- (−) Custo de conformidade por ciclo: cada edição de texto passa a dever checagens
  adicionais (espelhos, artefatos, camadas de terminologia).

## Registro

`docs/governance/constituicao-tese.md` v1.1.0; este ADR; linha em
`docs/records/decisoes.jsonl`; merge da branch `governanca/constituicao` na `main`.
