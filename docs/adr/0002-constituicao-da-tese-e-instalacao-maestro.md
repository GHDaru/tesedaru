# ADR 0002 — Constituição de conteúdo da tese e instalação do método Maestro

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú (instrução em conversa)

## Contexto

O autor determinou que o trabalho na tese siga sua metodologia Maestro
(GHDaru/maestro), com rastreabilidade de decisão. O Maestro possui constituição
própria (`principles.md`, v1.3.0, 8 princípios de PROCESSO), mas não princípios de
CONTEÚDO acadêmico. O gatilho concreto: a sigla FALCO aparece no §1.4 da introdução
sem nunca ser expandida no corpo do texto, e a varredura subsequente encontrou
DRI-SL com duas expansões divergentes (lista × Cap. 3) e seis siglas usadas no
corpo sem constar da lista (PLN, SGD, MaaS, NIM, CSV, JSON).

## Decisão

1. Instalamos o toolkit Maestro no repositório da tese (74 arquivos: agentes,
   skills, scripts, templates, governança) via `install-maestro.sh`.
2. Adotamos a Constituição da Tese (`docs/governance/constituicao-tese.md`,
   v1.0.0) com quatro princípios ratificados, ditados pelo autor: I. siglas
   abertas na 1ª ocorrência e presentes na lista; II. referências validadas
   contra fichamento; III. afirmações fundamentadas, referenciadas ou provadas;
   IV. decisões registradas em ADR.
3. Seis princípios adicionais (V–X) ficam PROPOSTOS no mesmo documento,
   aguardando gate do autor.
4. A correção imediata do gatilho (abertura de FALCO, DRI-SL, LLM, BERT, TF no
   Cap. 1 e saneamento da lista de siglas) entra no mesmo ciclo.

## Alternativas consideradas

- **Só corrigir o FALCO, sem constituição**: resolveria o sintoma — descartada: o
  autor pediu o princípio, não o curativo, e a varredura provou que o problema é
  sistêmico (7 siglas em situação irregular).
- **Adotar apenas a constituição do Maestro**: já instalada — insuficiente: ela
  governa processo de engenharia, não regras de conteúdo acadêmico (siglas,
  fichamento, fundamentação).
- **Não instalar o toolkit completo (seguir só com ADR + índice)**: mais leve —
  descartada: o autor pediu a instalação explicitamente.

## Consequências

- (+) Regra objetiva e verificável por script para siglas, referências e afirmações.
- (+) Toolkit completo disponível (agentes, constitution-check, verifiable-dod).
- (−) 74 arquivos de método passam a viver no repositório da tese (ruído no diff
  inicial; mitigado por serem de leitura, não de compilação).
- (−) O princípio II cria dívida imediata: validar as citações existentes contra os
  142 fichamentos é um ciclo futuro de trabalho não trivial.

## Registro

Branch `governanca/constituicao`: instalação Maestro, `constituicao-tese.md`
v1.0.0, este ADR, linha em `decisoes.jsonl`, correções de siglas no Cap. 1 e em
`0-iniciais/acronimos.tex`.
