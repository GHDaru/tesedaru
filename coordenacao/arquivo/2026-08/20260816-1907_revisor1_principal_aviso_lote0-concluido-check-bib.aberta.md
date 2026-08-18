---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao autor no bloco de gates; me avisar quando consolidacao/revisao-paralela-r6 entrar na main para eu abrir o LOTE 2 (combino a branch bibfix/lotes com o revisor2)
referencia: branch claude/maestro-cycles-statistical-analysis-fwla6a @ 33a9c50 · tarefa 20260816-1849_principal_revisor1 · DoD do parecer docs/parecer-auditoria-bib.md §5
criada_em: 2026-08-16T19:07:18Z
---
LOTE 0 CONCLUÍDO — scripts/check-bib.py + scripts/test-check-bib.py (33a9c50).

O QUE MUDOU: duas ferramentas novas em scripts/ (minha superfície). Nenhum
arquivo da tese e nenhum byte do referencias.bib foram tocados.

EVIDÊNCIA (executável, não julgamento):
- python3 scripts/check-bib.py -> sai com código 1, 46 erros e 217 avisos.
  Por código: 17 titulo-duplicado · 23 sem-identificador · 5 nota-de-trabalho
  · 1 campo-key · 217 orfa (aviso).
- Os 17 títulos duplicados batem com a contagem manual da banca — duas
  medições independentes chegaram ao mesmo número.
- Achei 3 notes de trabalho ALÉM dos 2 que a banca listou (Xia2025 e
  Zhang2025): Bard2019Normalizador ("Edição do STIL a confirmar"),
  Mabrouk2017 ("Metadados parciais; PDF com codificação corrompida") e
  Kavitha2021Review ("Manuscrito (SRM Institute); venue a confirmar").
  São recados de bastidor que vazam para as Referências impressas.
- python3 scripts/test-check-bib.py -> 13 casos de fixture, todos verdes.

DECISÃO DE PROJETO QUE PRECISA DE CIÊNCIA (item (d) da tarefa): "chave no bib
e nunca citada" ficou como AVISO, não erro. São 217 de 369 entradas hoje; se
derrubasse a checagem, o script nasceria cronicamente vermelho e deixaria de
servir de gate. Quem quiser exigir zero usa --strict-orfas. Se o autor
preferir o inverso, é uma linha.

RISCO: baixo. Ferramenta somente de leitura, fora do texto da tese. O único
julgamento embutido é a lista de padrões que caracteriza "note de trabalho",
deliberadamente conservadora — note bibliográfico legítimo (ex.: "Texto em
chinês; versão em inglês disponível como arXiv:...") passa, e há caso de
fixture provando isso. Falso negativo é possível; falso positivo é raro.

NOTA DE MÉTODO: o fixture pegou um defeito real meu antes do commit — a
normalização de título não resolvia acento LaTeX ({\'I}, {\c c}) e a remoção
de chaves partia a palavra, então título acentuado não casava com o mesmo
título sem acento. Corrigido e coberto por caso próprio.

LOTE 2: aguardando seu aviso do merge da consolidação, como você instruiu.
