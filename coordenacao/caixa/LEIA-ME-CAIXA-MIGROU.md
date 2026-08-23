# ⚠️ Esta caixa (na main) está CONGELADA — a caixa viva migrou para a branch `mensageria`

**Desde 2026-08-24 (PROTOCOLO v1.8).**

A `coordenacao/caixa/` **viva** agora mora na branch **`mensageria`** (descendente
da main, mão única do principal). A `main` = só a tese.

- **Para LER a caixa:** `git fetch origin mensageria` e leia `coordenacao/caixa/`
  em `origin/mensageria`.
- **NÃO escreva mensagens novas aqui (main).** Escreva na `mensageria`.
- Os arquivos históricos abaixo ficam **preservados** para rastreabilidade (nada
  foi apagado — decisão I4).

O hook `estado-da-sessao.py` já lê a caixa de `origin/mensageria`. Detalhes no
`PROTOCOLO.md` §9 (v1.8).
