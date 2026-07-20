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

## Regeneração do grafo
Após criar/editar um fichamento, regenere o KG para propagar nós e arestas:

```
uv run --with pyyaml python fichamentos/build_kg.py   # -> kg.json + kg.html
```

O `build_kg.py` também enriquece cada nó-artigo com `pdf`, `doi` e `cited_in`
(capítulos da tese que citam a chave), consumidos pela interface para abrir o
PDF (só visualização), o link do publicador e onde o artigo aparece na tese.

## Geração automática a partir do PDF (app)
A interface FALCO (`POST /api/fichamentos`) recebe um PDF e produz um **rascunho**
de fichamento seguindo este SKILL:

1. extrai texto + metadados do PDF (título, autores, ano, DOI quando presentes);
2. deriva a chave BibTeX (`SobrenomeAno`) e o `id` do nó;
3. preenche o front-matter do `_TEMPLATE.md` — campos de entidade/relação ficam
   como sugestão a partir do texto e do `_VOCABULARIO.md`, nunca inventados;
4. grava `fichamentos/{Chave}.md` e arquiva o PDF em `referencias-pdf/{Chave}.pdf`;
5. regenera o KG.

O resultado é um **rascunho para revisão humana**: `status: a-ler`, entidades e
`falco_relation` marcadas para confirmação. A regra "nenhuma afirmação sem
evidência localizável" continua valendo — o rascunho não entra na tese sem
revisão do autor.
