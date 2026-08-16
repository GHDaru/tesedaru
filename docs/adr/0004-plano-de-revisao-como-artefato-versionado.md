# ADR 0004 — Plano de revisão como JSON versionado + painel republicável

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú (instrução em conversa)

## Contexto

O autor quer paralelizar o trabalho em várias sessões e, em qualquer uma delas,
saber o próximo passo: um plano por capítulo das rodadas de revisão, cobrindo
também os artefatos não textuais (experimentos, publicações, artigos, defesa),
consultado antes de cada rodada.

## Decisão

1. A fonte de verdade do plano é `docs/records/plano-revisao.json` (versionado;
   campo `versao` incrementa a cada mudança; campo `proximo` diz o passo seguinte).
2. O painel visual é um Artifact que RENDERIZA esse JSON; como o sandbox de
   artifacts bloqueia rede externa, o JSON é embutido na publicação:
   `scripts/render-plano-revisao.py` injeta o JSON no template
   `docs/records/plano-artefato-template.html` e o HTML é republicado na URL fixa
   registrada em `docs/records/plano-artefato-url.txt`.
3. Ritual por sessão: ler `proximo` → executar o ciclo (branch, antes/depois,
   gate, ADR) → atualizar o JSON (+push) → republicar o painel na mesma URL.
4. Sete rodadas por capítulo (R1 humanização … R7 leitura final), mapeadas aos
   princípios da Constituição da Tese v1.1.0.

## Alternativas consideradas

- **Painel lendo o GitHub ao vivo**: dispensaria republicação — inviável: o CSP
  dos artifacts bloqueia qualquer host externo e o roster de capacidades desta
  conta (downloads, mcp) não fornece fetch genérico.
- **Só o task list da sessão**: morre com a sessão — descartada: o requisito é
  exatamente sobreviver a sessões e paralelizar.
- **Planilha externa**: fora do git, sem trilha de decisão — descartada.

## Consequências

- (+) Qualquer sessão sabe o próximo passo lendo um arquivo do repositório.
- (+) O histórico do plano fica no git (diffs de status são auditáveis).
- (−) O painel só reflete o JSON após republicação — um passo manual por ciclo.
- (−) Duas fontes visuais (JSON e painel) podem divergir entre a atualização e a
  republicação; o JSON prevalece.

## Registro

`docs/records/plano-revisao.json` v1; template + script; URL do artefato em
`docs/records/plano-artefato-url.txt`; este ADR; linha no `decisoes.jsonl`.
