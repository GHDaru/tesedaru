---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: humanizar (rodada R1) os Capítulos 5 e 6 conforme docs/criterio-humanizacao.md, entregar em branch e mandar conclusão ao principal
referencia: docs/criterio-humanizacao.md · exemplar aprovado: merge 7e90069 (lote 1 do Cap. 2) · plano cap5.R1 e cap6.R1
criada_em: 2026-08-16T19:38:13Z
---
O autor aprovou o critério de humanização e delegou a rodada R1 aos revisores.
A superfície de prosa destes dois capítulos passa a ser sua enquanto durar a
tarefa (lock por arquivo; o principal não edita em paralelo).

SEUS CAPÍTULOS
- Capítulo 5 (5-resultados-falco/texto.tex): 64 travessões + 6 frases telegráficas ("Três leituras.")
- Capítulo 6 (6-conclusao/texto.tex): 35 travessões + mistura de --- e — ; o FECHO (tríade + aforismo) é DECISÃO DO AUTOR: mantido, NÃO reescrever

CRITÉRIO: docs/criterio-humanizacao.md — os 4 grupos de conversão, o que
preservar e como entregar. Leia antes de começar; ele é o contrato. O exemplar
aprovado pelo autor está no merge 7e90069 (Cap. 2): compare seu trabalho com
aquele diff sempre que tiver dúvida.

REGRAS
- Lock por arquivo antes de editar (coordenacao/locks/<cap>--texto.tex.md).
- NÃO toque nos Capítulos 1 e 2: estão com o bib-fix (28 das 37 citações
  afetadas vivem no Cap. 2) — colisão garantida.
- Trabalhe em lotes por seção; um commit por lote, mensagem descritiva.
- Ao terminar: libere o lock, publique a branch e mande CONCLUSÃO ao
  principal (nunca ao autor) com travessões antes/depois, conversões por
  grupo e 3 exemplos representativos. Eu consolido e levo ao gate do autor.
- Se o bib-fix ainda estiver ocupando você, faça esta tarefa depois — ela não
  é bloqueante; avise o principal a ordem que escolheu.
