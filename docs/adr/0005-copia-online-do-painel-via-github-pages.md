# ADR 0005 — Cópia online sempre atual do painel via GitHub Pages

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú (pergunta "como visualizar de forma atualizada / posso gerar cópia online?")

## Contexto

O Artifact do Claude embute o JSON no momento da publicação (o sandbox bloqueia
rede externa), então ele só reflete o plano após uma republicação manual. O autor
quer uma visualização sempre atual, acessível de qualquer lugar, e perguntou
sobre Google Drive.

## Decisão

Adotamos GitHub Pages do próprio tesedaru como cópia online canônica: o workflow
`.github/workflows/painel.yml` re-renderiza o painel a partir de
`docs/records/plano-revisao.json` a cada push na main e publica em
https://ghdaru.github.io/tesedaru/ — a página está sempre igual ao JSON da main,
sem passo manual. Requer uma habilitação única pelo autor (Settings → Pages →
Source: GitHub Actions), o mesmo gesto já feito no repositório activelearning.

## Alternativas consideradas

- **Google Drive**: exige autorizar o conector no claude.ai e re-enviar o arquivo
  a cada mudança (sincronização manual) — descartada como canônica; possível como
  espelho se o autor quiser.
- **Só o Artifact do Claude**: fica defasado entre republicações — mantido como
  espelho, não como fonte.
- **Painel lendo raw.githubusercontent ao vivo**: bloqueado pelo CSP dos artifacts.

## Consequências

- (+) Uma URL pública sempre igual à main; push = painel atualizado.
- (+) Zero dependência de sessão do Claude para atualizar a visualização.
- (−) O repositório tesedaru é público: o plano (títulos de pendências) fica
  visível; nada sensível deve entrar no JSON.
- (−) Habilitação única do Pages pelo autor ainda pendente.

## Registro

`.github/workflows/painel.yml`; ritual atualizado no plano v2; este ADR; linha no
`decisoes.jsonl`.
