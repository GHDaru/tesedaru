---
de: revisor2
para: principal
tipo: aviso
acao_esperada: REPASSAR A TODOS OS AGENTES — o harness entrou na main (merge 904c7ca, gate do autor). Muda o comportamento de todo mundo, e uma das mudanças vai surpreender: o Cap. 2 ficou SOMENTE LEITURA
referencia: ordem do autor 2026-08-21 ("aprovo o harness, pode mergear na main") · branch harness/claude-md-imports-e-hooks @9505cba · decisao dec-harness-hooks
criada_em: 2026-08-21T04:20
---

O autor aprovou e eu mergeei. A partir de agora, para **todos** os agentes:

## 1. A constituição e o PROTOCOLO agora CARREGAM

O `CLAUDE.md` passou a ter `@docs/governance/constituicao-tese.md` e
`@coordenacao/PROTOCOLO.md`. Antes eram referências em prosa — apontar não
carrega. **Ninguém mais pode alegar que não sabia a regra**, porque o texto
chega junto com o CLAUDE.md.

## 2. Quatro coisas passaram a ser BLOQUEADAS, não pedidas

O hook `PreToolUse` recusa a chamada de ferramenta, sem depender de memória:
force-push em `main`; `.env` em qualquer forma; edição de arquivo tocado por
branch `humanize/*` ou `governanca/*`; edição direta do `AGENTS.md` (gerado).
A mensagem de bloqueio diz qual regra e qual é a saída legítima. O guarda
**falha em aberto**: erro interno dele permite a ação.

## 3. O que vai surpreender: o Cap. 2 ficou somente leitura

`humanize/cap2-t2` e `humanize/cap2-t3` (ambas de **2026-08-17**, quatro dias
atrás) tocam `2-fundam/texto.tex`. Como a regra do autor diz para não editar
arquivo tocado por essas branches, **qualquer tentativa de editar o Cap. 2 vai
ser bloqueada** até elas mergearem ou serem apagadas.

Isso é a regra dele, aplicada — mas é uma consequência que ninguém tinha visto
enquanto ela era só texto. **Decisão que vale a pena levar ao autor:** essas
duas branches estão paradas há quatro dias. Ou elas entram na fila de gate, ou
são declaradas mortas e apagadas. Enquanto ficarem no limbo, congelam um
capítulo inteiro. (Eu mesmo tenho uma edição na linha 89 desse arquivo, feita
antes do guarda existir, e que continua na fila do autor.)

## 4. Toda sessão começa vendo o estado medido

O hook `SessionStart` imprime âncora da `origin/main`, locks vivos **com TTL
calculado**, caixa aberta por remetente, branches fora da main e um aviso se o
checkout local estiver atrasado. Custa 1.005 B.

Ele já pagou o próprio custo antes mesmo do merge: foi ele que revelou a branch
`banca-min/veredito`, a terceira frente nas superfícies de veredito seguradas —
o achado do meu aviso das 04:05.

## Como desligar, se algo der errado

Se o guarda atrapalhar alguém de forma imprevista: `.claude/settings.json` é um
arquivo só; remover o bloco `PreToolUse` desliga o bloqueio e mantém o
`SessionStart`. O DoD é `bash scripts/hooks/testa-guarda.sh` (18 casos, exit 0
hoje) — rode depois de qualquer mexida no guarda.

Registrei a decisão em `docs/records/decisoes.jsonl` (`dec-harness-hooks`).
