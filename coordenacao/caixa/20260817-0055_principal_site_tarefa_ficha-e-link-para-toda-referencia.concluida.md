---
de: principal
para: site
tipo: tarefa
acao_esperada: na página Referências, garantir que TODA entrada tenha (1) ficha de detalhes funcional e (2) link clicável — sem exceção; publicar sem gate e avisar com a URL
referencia: pedido do autor 2026-08-17 · página Referências · docs/records/referencias.json · tarefa 20260816-2110
criada_em: 2026-08-17T00:55:00Z
---

Pedido do autor ao revisar a página Referências: "importante a ficha e todos
deveriam ter" + "colocar também o link no site". Dois requisitos, valem para
TODAS as entradas do bib, não só as fichadas:

## 1. Ficha para toda referência

O botão "ver detalhes" deve funcionar em 100% das linhas:
- **Obra fichada**: como hoje — o fichamento renderizado.
- **Obra SEM fichamento**: ficha básica gerada dos metadados do próprio bib
  (título completo, autores por extenso, veículo/venue, ano, volume/páginas,
  DOI/arXiv/URL, onde é citada na tese com todas as ocorrências) + selo
  claro "ainda não fichada" — para o autor nunca clicar num botão morto.

## 2. Link para toda referência

Hierarquia atual (DOI > arXiv > URL) continua; a novidade é o fallback:
- Entrada SEM nenhum identificador → gerar **link de busca pronto**
  (Google Scholar com título entre aspas + primeiro autor, e/ou busca
  Crossref), rotulado como "buscar ↗" para não se passar por link direto.
  Racional do autor: ele quer clicar e ter a busca pronta para fazer a parte
  que os agentes não alcançam (baixar PDF, confirmar em base fechada).
- O campo de link é dado computado no `compute-referencias.py` (build), não
  montado no cliente.

Cuidado de honestidade visual: distinguir os três estados no mesmo padrão de
badges do site — link direto (DOI/arXiv/URL) · buscar (fallback) · fichada/
não fichada. Nada de link quebrado ou botão inerte em nenhuma linha.
