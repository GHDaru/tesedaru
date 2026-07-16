# tesedaru — Tese de Doutorado (reescrita)

**Aprendizado Ativo com Modelos de Linguagem para Textos Curtos em Português (FALCO)**
Gilsiley Henrique Darú — PPGMNE/UFPR — Orientador: Prof. Dr. Gustavo Valentim Loch

Repositório **limpo** da reescrita final da tese. Template: classe `ppginf.cls`
(Maziero/UFPR), adaptada com os dados do PPGMNE. Compilação: `pdflatex + bibtex`.

- Plano de reescrita capítulo a capítulo: [docs/plano-reescrita](docs/parecer-fase-menos-1.md) (§5)
- Código e experimentos: [GHDaru/activelearning](https://github.com/GHDaru/activelearning)
- **Regra de ouro:** nenhum número entra aqui sem artefato rastreável no `activelearning`.

| Diretório | Conteúdo | Fonte no draft legado |
|---|---|---|
| `1-intro/` | Introdução | `nova_introducao.tex` (~80% reaproveitado) |
| `2-fundam/` | Fundamentação + revisão | `capitulo_02_fundamentos/` (ML condensado) |
| `3-metodo/` | Metodologia | reescrita ~60% (DRI unificado, IPR cortado) |
| `4-resultados-l0/` | P1 sensibilidade L0 + AG, P2 DRI-SL | dados reais legados |
| `5-resultados-falco/` | P3 oráculo (E0), P4 FALCO vs RS/US (E3) | experimentos novos |
| `6-conclusao/` | Discussão + conclusão | reescrita ~70% |
| `a1..a6-*/` | Apêndices (LCE, AG, DRI-SL, biblioteca, prompts, tabelas) | — |
