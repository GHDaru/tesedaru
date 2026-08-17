---
de: principal
para: site
tipo: aviso
acao_esperada: incorporar à tarefa 20260817-0055 (ficha e link para toda referência): cada referência deve trazer também o link da sua página no Semantic Scholar
referencia: tarefa 20260817-0055 · pedido do autor 2026-08-17 ("o link do fichamento que é do semantic scholar")
criada_em: 2026-08-17T01:10:00Z
---
Esclarecimento do autor sobre a tarefa 0055: a "ficha" que ele quer para
toda referência inclui o **link da página da obra no Semantic Scholar**
(ex.: semanticscholar.org/paper/<id>) — ele usa essa página como ficha
externa de conferência. Implementação sugerida no compute-referencias.py
(build, nunca no cliente): resolver via API pública do Semantic Scholar por
DOI (api.semanticscholar.org/graph/v1/paper/DOI:<doi>) ou arXiv; sem
identificador, cair para o link de busca do S2 por título. Exibir dentro da
ficha de detalhes como "Ficha S2 ↗", ao lado do link direto — sem
substituir o DOI. Se a API limitar taxa no deploy, cachear os IDs
resolvidos em docs/records/ (recomputar só entradas novas).
