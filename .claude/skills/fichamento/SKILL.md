---
name: fichamento
description: Fichar um artigo científico no padrão KG-ready da tese (markdown + front-matter YAML). Use quando o usuário pedir para fichar/resumir/anotar um paper, ou quando houver PDFs novos em a_sanear/.
---

# Fichamento KG-ready

## Fluxo
1. **Entrada**: PDF em `a_sanear/` (ou indicado pelo usuário).
2. **Identidade**: localizar/criar a entrada em `referencias.bib`. A chave BibTeX é o
   ID universal (nó do grafo, nome do PDF, nome do fichamento).
3. **Renomear e arquivar o original**: mover o PDF para
   `referencias-pdf/{ChaveBibtex}.pdf` (minúsculas não; manter a chave exata).
   O original SEMPRE fica versionado na tese.
4. **Fichar**: copiar `fichamentos/_TEMPLATE.md` para `fichamentos/{ChaveBibtex}.md`
   e preencher LENDO O PDF (nunca de memória):
   - front-matter completo (entidades/relações do `fichamentos/_VOCABULARIO.md`
     — só nomes canônicos; se faltar termo, adicionar ao vocabulário no mesmo commit);
   - resumo em palavras próprias (5-8 linhas);
   - claims com evidência localizável (seção/tabela/página) e uso previsto na tese;
   - números citáveis com condições exatas;
   - crítica/limitações e relação com FALCO/DRI-SL/LCE (`falco_relation`).
5. **Sanear**: remover o PDF de `a_sanear/` (já movido). Commit único por artigo:
   `Fichamento: {ChaveBibtex}` incluindo PDF + fichamento + bib + vocabulário.

## Regras
- Um fichamento por arquivo; um commit por fichamento.
- Claim sem evidência localizável não entra na tabela.
- `falco_relation` é obrigatório: se o paper não toca a tese, ele não precisava
  ser fichado — justifique ao usuário antes de pular.
- Campos que exigem versão final do paper (números, páginas) ficam marcados
  `(preencher c/ PDF final)` — nunca inventados.
