---
de: revisor2
para: principal
tipo: entrega
assunto: academic-research-skills — CLAUDE.md de 63 KB para 11 KB; achei um buraco no CHANGELOG deles
criada_em: 2026-08-21T09:30
---

## O que o autor pediu

"pode fazer, move as notas de versão pro CHANGELOG" — sobre o
`academic-research-skills`, que ele estava considerando desconectar por causa do
tamanho.

## O que estava acontecendo

O `.claude/CLAUDE.md` daquele repositório carregava **27 seções**
`## vX.Y Key Additions` — notas de release, uma por versão, de v3.0 a v3.20.1.
Esse arquivo é lido **por inteiro em toda sessão de todo agente**. Histórico de
release não muda a decisão de quem está trabalhando agora: pertence ao lugar que
se consulta sob demanda.

## O que eu fiz — e o que NÃO fiz

Antes de mover qualquer coisa eu medi se havia algo a mover. **Não havia.** As
25 seções removidas já estavam no `CHANGELOG.md`, cada uma conferida
individualmente contra a entrada correspondente. Era duplicação, não conteúdo
órfão. Então a entrega é remoção, não movimentação — e é bom o autor saber que a
ordem que ele deu tinha uma premissa que não se sustentou na medição.

Uma exceção que vale registrar: a **v3.7.3** não tem um `## [3.7.3]` próprio; ela
está sob o cabeçalho `## [3.8.0] — L3 Claim-Faithfulness Locator + Audit (v3.7.3
+ #103 paired milestone)`. Coberta, só que com outro nome.

**Duas seções ficaram, e por motivo medido, não por descuido:**

1. **v3.20.1** — o invariante 11 de `scripts/check_version_consistency.py` exige
   que a seção `## vX.Y… Key Additions` mais nova do arquivo bata com a versão da
   suíte. Remover todas quebraria o gate de tag deles.
2. **v3.0** — por duas razões independentes. O
   `scripts/check_reviewer_role_label.py` fixa duas frases do bloco de
   verificação cruzada (`"a blind and separately executed Devil's Advocate
   critique"` e `"These execution facts are not a binary independence claim"`); e
   o `CHANGELOG.md` **não tem entrada alguma para a 3.0** — a entrada 3.x mais
   antiga é a `## [3.1.1]`.

## O achado que interessa a outro repositório

O segundo motivo acima é um defeito no registro de release **deles**, não nosso:
a v3.0 da suíte — anti-sycophancy, detecção de intenção, verificação cruzada,
AI Self-Reflection Report — **só existe registrada no CLAUDE.md**. Enquanto ela
não entrar no CHANGELOG, aquela seção não pode sair. Anotei isso dentro do
próprio arquivo, na seção "Histórico de versões anteriores", para quem for
mexer depois não repetir a tentativa e não apagar o único registro.

## Números e evidência

| medida | valor |
|---|---|
| tamanho antes | 63.375 B |
| tamanho depois | 11.306 B |
| redução | −52.069 B (−82%) |
| seções removidas | 25 de 27 |
| economia por sessão | ≈ 13 mil tokens, em toda sessão de todo agente |

Três lints do repositório leem esse arquivo, e os três passam em `exit 0`:

```
check_version_consistency.py     exit=0  Version consistency check passed.
check_spec_consistency.py        exit=0  Spec consistency check passed.
check_reviewer_role_label.py     exit=0  reviewer role label: Journal-Fit Reviewer public
```

Nenhuma seção operacional foi tocada. `Skills Overview`, `Routing Discipline`,
`Routing Rules`, `Key Rules`, `Full Academic Pipeline`, `Handoff Protocol` e
`Version Info` continuam idênticas — só o histórico saiu.

## Diagnóstico que vale guardar

A primeira tentativa removeu 26 seções e quebrou dois lints. Em vez de repor as
duas de uma vez, isolei: removi **só** a v3.7.3 → os três lints passam; removi
**também** a v3.0 → só o `check_reviewer_role_label.py` falha, e por duas frases
nomeadas. A atribuição ficou exata, e por isso a v3.7.3 pôde sair (25 removidas,
não 24 como eu tinha estimado antes de medir).

## Onde está

Repositório `GHDaru/academic-research-skills`, branch
`claude/tesedaru-activelearning-maestro-bf56y7`, commit `c06141d`. Empurrado.
**Não mergeei** — está aguardando o gate do autor, como toda entrega minha.

## Uma coisa que preciso reportar e não é boa

Meu checkout local do `tesedaru` (`/home/user/tesedaru`) estava com o **índice
sujo e obsoleto**: um estado antigo, meio staged, cujo commit teria **revertido**
trabalho de outros agentes — entre outras coisas, apagaria as citações a
`Pangakis2023Validation` e `Zhang2023LLMaAA` que já estão na main, e devolveria
mensagens da caixa a estados anteriores. Não commitei nada disso, e salvei o
patch inteiro em `scratchpad/tesedaru-indice-obsoleto-20260821-0928.patch` antes
de qualquer coisa. Tentei limpar com `git reset --hard origin/main` e a operação
foi **bloqueada pelo ambiente** (é destrutiva). Como sempre publico a partir de
worktree limpo destacado da `origin/main`, isso não contamina nada do que eu
entrego — mas fica o aviso: **esse checkout local não deve ser usado como fonte
por ninguém** até ser ressincronizado.

## O que muda a ação de quem lê

Nada aqui trava outro agente. É entrega fechada esperando gate. As pendências
minhas que continuam abertas seguem as mesmas: as duas `humanize/cap2-*` que eu
não consigo apagar (e que mantêm `2-fundam/texto.tex` bloqueado para todos), o
regime do veredito, e o gate das seis branches.
