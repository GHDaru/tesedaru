# Fixtures do ciclo 011 (integração do check-bib)

Reproduzem os critérios 1-5 do DoD sem tocar no acervo real.

- `bib-com-3-defeitos.bib` — `key = {residuo}` em entrada de UMA linha (o falso
  negativo que motivou o ciclo), `note = {ver tabela, key = valor}` (o falso
  positivo que NÃO deve disparar), par de títulos duplicados com um lado sem
  DOI, e uma órfã. Esperado: 2 erros + 1 aviso, exit 1.
- `bib-so-orfa.bib` — apenas uma órfã. Esperado: 1 aviso, **exit 0**.

Para rodar, monte um diretório com `referencias.bib`, `fichamentos/`,
`2-fundam/texto.tex` citando as chaves e `scripts/` com os dois módulos; o
procedimento está no `specs/011-integra-check-bib/qa-report.md`.
