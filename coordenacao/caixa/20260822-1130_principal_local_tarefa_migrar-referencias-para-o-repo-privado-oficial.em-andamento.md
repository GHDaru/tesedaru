---
de: principal
para: local
tipo: tarefa
acao_esperada: migrar TODAS as referências (PDFs + fichamentos + grafo + bibliometria) para o repositório privado oficial GHDaru/referenciastese (hoje vazio), organizado por padrão de especialista em administração de referências; criar CLAUDE.md e AGENTS.md; e devolver ao principal o que atualizar no repositório da tese. É trabalho longo do seu lado (você tem a máquina do autor e credencial).
referencia: decisão do autor 2026-08-22 · repo https://github.com/GHDaru/referenciastese.git (privado, vazio) · referencias-pdf/ (170 arquivos) + a_sanear/ + fichamentos/ + docs/records/referencias.json
criada_em: 2026-08-22T11:30:00Z
---

O autor criou o repositório PRIVADO e OFICIAL das referências:
`https://github.com/GHDaru/referenciastese.git` (vazio). Ele é privado porque
guarda obras sob direito autoral; quem precisar pede autorização de leitura ao
autor. Passa a ser a fonte canônica das referências da tese.

# O que mover para lá
1. **`referencias/`** — todos os PDFs de `referencias-pdf/` (170 arquivos) já
   renomeados pelo padrão ChaveBibtex.pdf; e o que estiver em `a_sanear/` que
   já foi fichado (os `_TRIAGEM_*` são descartes — decida com o padrão do
   especialista se entram como "descartados/" ou saem).
2. **`fichamentos/`** — os fichamentos hoje em `fichamentos/` do repo da tese.
3. **`grafo/`** — a estrutura de grafos de relações entre obras (o KG que já
   alimenta as relações citadas × fichadas).
4. **`bibliometria/`** — contagens, cobertura (fichadas/citadas/órfãs),
   autoria (≥5 autores), DOIs, mapa de citação por capítulo.

# Padrão de especialista em administração de referências (aplique)
- Chave BibTeX como identidade única (arquivo, ficha e nó do grafo usam a
  MESMA chave). PDF = `<Chave>.pdf`; ficha = `<Chave>.md`.
- Um `referencias.bib` mestre no repo privado, espelhado/derivado do que a
  tese usa — a tese continua com o .bib dela, mas o privado é a fonte.
- Invariantes verificáveis (traga como script, no espírito dos guards da
  tese): toda chave tem PDF OU justificativa (livro/pré-2010 dispensa, ADR
  0012); toda ficha aponta para um PDF ou entrada verificável; sem DOI
  repetido; sem chave órfã sem relação no grafo.
- Bibliometria reprodutível: um script gera as contagens a partir do .bib +
  fichas + grafo, não à mão.

# Arquivos para IA no repo privado
- **CLAUDE.md** e **AGENTS.md**: descrevem a estrutura (referencias/,
  fichamentos/, grafo/, bibliometria/), a regra da chave única, como adicionar
  uma obra (PDF → ficha → nó no grafo → entrada no .bib → rodar a
  bibliometria), e a regra de privacidade (não vazar conteúdo de obra em
  mensagem/commit público). Curtos e operacionais.
- README do repo privado: o que é, por que é privado, como pedir acesso.

# O que devolver ao principal (para eu atualizar a tese)
- Confirmação de que os PDFs saíram do repo público da tese (ou o que fica e
  por quê) — o repo da tese é PÚBLICO, então PDFs sob copyright não devem
  ficar nele.
- A lista do que remover de `referencias-pdf/` e `a_sanear/` do repo da tese
  após a migração, para eu limpar com gate do autor.
- Como a tese passa a referenciar o repo privado (o README já ganhou a nota;
  confirme o texto ou sugira melhor).

Segurança: repo privado, mas trate como se pudesse vazar — nenhuma chave/token
em commit; a privacidade é do CONTEÚDO das obras, não desculpa para relaxar.
Se quiser, o autor pode dedicar uma sessão "especialista de referências" para
manter o repo daqui pra frente; sinalize se achar necessário.
