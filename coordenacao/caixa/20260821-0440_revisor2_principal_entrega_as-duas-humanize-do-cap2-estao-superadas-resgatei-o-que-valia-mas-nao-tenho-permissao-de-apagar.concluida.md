---
de: revisor2
para: principal
tipo: entrega
acao_esperada: LEVAR AO AUTOR — ele mandou avaliar e apagar as duas branches `humanize/cap2-*` se não fossem mais úteis. Avaliei (estão superadas), resgatei o que valia (já na main, 5218ccd), mas o DELETE volta 403: a credencial desta sessão cria e atualiza refs, não apaga. Precisa da mão dele — comando pronto abaixo
referencia: ordem do autor 2026-08-21 · merge do harness 904c7ca (que é o que tornou isto urgente) · resgate 5218ccd
criada_em: 2026-08-21T04:40
---

# O veredito: as duas estão superadas

| branch | ponta | o que continha | situação hoje |
|---|---|---|---|
| `humanize/cap2-t2` | `2438c68` (17/08) | 1 linha: "é o espírito de Shannon" → "no espírito de" | **a main removeu o trecho inteiro** — a oração apositiva não existe mais (`2-fundam:389` termina em `\citep{Settles2012}.`) |
| `humanize/cap2-t3` | `dc7247e` (17/08) | travessão → dois-pontos em `2-fundam` + correção do QA | **o conserto do `.tex` já está na main** (linha 708, com os dois-pontos), chegou por outro caminho |

A main andou **272 e 294 commits** desde a base de cada uma. Nenhuma das duas
aplica: ambas conflitam em `2-fundam/texto.tex`.

# O que eu resgatei antes, e por que não podia ser perdido

A `cap2-t3` carregava uma coisa que a main **não tinha**: a correção de um erro
meu no relatório de QA do ciclo 009 — e eu fui o executor daquele ciclo.

A main dizia (errado): critério 1 "22 → **1**" travessões, e uma seção
"Pendência declarada" afirmando que o remanescente era `humano--LLM`, "grafia
de termo, mantido de propósito".

Medi na main de hoje e as duas afirmações caem:
- `humano--LLM` usa **hífen duplo** `--`, que não é o caractere `—` que a
  contagem mede (2 ocorrências, nenhuma conta);
- o único `—` de `2-fundam/texto.tex` está na **linha 113**, na seção de
  métricas — **fora da faixa do t3**, que é a §2.3 ("Modelos de linguagem como
  oráculos de rotulagem"). Na faixa do t3, a contagem hoje é **zero**.

Quem pegou o erro foi o **revisor1**, na verificação cruzada. A branch tinha a
correção; a main não. Apagar sem resgatar deixaria de pé um relatório de QA que
afirma o que a medição desmente. Resgatado em **`5218ccd`** (só o `qa-report.md`;
não toquei no `.tex`, que já estava certo).

# O que eu NÃO consegui fazer, e por quê

`git push origin --delete` volta **HTTP 403**, de forma consistente: 10
tentativas com backoff (0/2/4/8/16 s) nas duas branches, todas 403. Não é
transitório — pushes normais para a `main` funcionaram minutos antes e continuam
funcionando, e o proxy não reporta falha (`recentRelayFailures: []`). A leitura
do remoto funciona. **Minha inferência:** a credencial desta sessão pode criar e
atualizar refs, mas não apagar. Não há ferramenta de apagar branch no servidor
MCP do GitHub (só `create_branch`).

**Comando para o autor rodar**, com os SHAs registrados para restauração:

```
git push origin --delete humanize/cap2-t2   # ponta 2438c68c2b5bd3af95d167c956338da2eaf548a7
git push origin --delete humanize/cap2-t3   # ponta dc7247ea7a27e48e2baa02b72e07cd5fba5961f5
```

Se depois quiser qualquer uma de volta: `git branch humanize/cap2-t2 2438c68`.

# O que fica travado até lá

Enquanto essas duas branches existirem, o guarda mantém **`2-fundam/texto.tex`
bloqueado para todos os agentes** — reconferido agora: `exit=2`. É a regra do
autor funcionando, mas hoje ela protege contra um conflito que não existe mais,
porque o conteúdo das duas já está superado.

Duas saídas, e a escolha é do autor:
1. **Ele apaga as duas** (comando acima) — o Cap. 2 destrava sozinho, sem mexer
   em nada do harness. É a saída limpa.
2. **Ele autoriza estreitar a regra 3 do guarda** para ignorar branch cujo diff
   já esteja integralmente na main. Não fiz por conta própria: mudar a semântica
   de uma regra dele sem ordem seria decidir no lugar dele.

Recomendo a 1: é uma linha, é reversível pelo SHA, e não mexe em código que
governa o trabalho de todos.
