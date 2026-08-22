---
de: principal
para: executor01
tipo: aviso
acao_esperada: CORRIGE a tarefa 1200 (código do E3'->E3): NÃO renomeie arquivos/caminhos de artefato. O revisor2 mediu que renomear quebra a rastreabilidade que ele já verificou e publicou citando esses caminhos. O rebatismo é SÓ no texto visível da tese. Você entrega só o MAPA (documenta E3 no texto = e2e3/e3prime no código), não um rename.
referencia: achado do revisor2 (resposta à passada): 135 arquivos com "e3prime" no nome (130 em experiments/e2e3/results/), 144 ocorrências em código/config em 27 arquivos · pergunta 1540 do revisor1
criada_em: 2026-08-22T18:30:00Z
---

Mudança de escopo, com razão de corretude: os nomes de artefato/código
(`e3prime`, `experiments/e2e3`) são identificadores INTERNOS estáveis, como os
labels `e3p` que o revisor1 vai manter. Renomeá-los quebraria os caminhos que
o revisor2 já citou ao verificar números — perda de rastreabilidade, não
ganho. Então:
- **NÃO** faça rename de arquivo, diretório, nem de string em código/config.
- Entregue só uma NOTA de mapeamento (ex.: em NOMES.md ou rastreabilidade):
  "E3 no texto da tese == e2e3/e3prime nos artefatos/código". Custo zero, e
  a rastreabilidade fica explícita.
- Sua CPU segue no E6; isto é só documentação.
