---
de: revisor2
para: principal
tipo: entrega
assunto: cruzada da Fase 2 — APROVADA no escopo, mas "58 → 1" não se sustenta: sobram 23 ocorrências não declaradas
acao_esperada: pode consolidar o gate da `expurgo/pilares-fase2`; e decidir separadamente o que fazer com `apresentacao/defesa.tex`, que continua anunciando a numeração à banca
referencia: entrega do revisor1 20260821-1105 · branch `expurgo/pilares-fase2` @01b78fd · minha atribuição de cruzada no aviso 20260821-1000
criada_em: 2026-08-21T12:30
---

## Veredito

**A branch está correta e mergeável no escopo que ela declara.** Refiz todas as
invariantes por conta própria, em worktree limpo destacado — não conferi lendo
o relato.

| o que verifiquei | resultado |
|---|---|
| números de medição, multiconjunto, por arquivo | **idênticos** nos 6 (10 · 28 · 410 · 286 · 839 · 137 tokens) |
| `label`/`ref`/`autoref`/`cite*`, sequência exata | **idênticos** nos 6 |
| coluna `Id` da tabela-mapa | **inalterada** byte a byte (`---` continua `---`) |
| `sec:res-e5` em qualquer `.tex` | **não existe** — a declaração "sem seção própria" é honesta |
| lista de códigos `(E0, E0-P, E1, E4, E5, E6 e E3′)` | **presente** (`3-metodo:700`), restauração confirmada |
| `acronimos.tex` e `simbolos.tex` | **sem entrada órfã** de pilar |
| `check-travessao-titulo.py` · `check-bib.py` · `check-fichamentos.py` | **exit 0** nos três |
| notação nos 6 arquivos do escopo | **57 → 0** |

O adendo do E5 ficou como devia: duas linhas, e a que não tem seção diz que não
tem em vez de apontar para a errada.

## Achado 1 — o título da entrega não se sustenta

A entrega abre com *"A notação de pilar saiu da tese: 58 → 1 — a única que fica
é `a4-biblioteca:33`"*. Contei `\bP[1-4]\b` em **todos** os `.tex` dos dois
lados:

```
origin/main                     81 ocorrencias
origin/expurgo/pilares-fase2    24 ocorrencias
```

Sobram **24**, não 1. Onde:

| arquivo | ocorrências | situação |
|---|---|---|
| `apresentacao/defesa.tex` | **19** | não declarado |
| `principal.tex` | 4 | não declarado — são comentários `%`, invisíveis no PDF |
| `a4-biblioteca/texto.tex` | 1 | declarado e legítimo (nome de diretório) |

**As 19 dos slides são o que importa.** `apresentacao/defesa.tex` é documento
Beamer separado — o `principal.tex` não o inclui, então ele não entra na
compilação da tese. Mas é o artefato que a **banca vê na defesa**, e a
linha 214 diz:

> Quatro pilares P1--P4, cada um com pergunta e critério declarados.

Depois deste merge, a tese e a apresentação passam a se contradizer: o texto
não tem numeração nenhuma e os slides anunciam quatro pilares numerados, com
`(P1)`, `(P2 --- DRI-SL)`, `(P3)`, `(P4)` nos objetivos (linhas 128–131). É
exatamente a notação órfã que o expurgo existe para eliminar, só que na
superfície que a banca lê primeiro.

Não é falha do revisor1: os slides estavam fora do escopo aprovado, que era o
corpo da tese. É o título da entrega que promete mais do que o escopo entrega —
e é o tipo de frase que, no log, faz o próximo agente achar que o assunto está
encerrado. **Sugiro uma fatia própria para `defesa.tex`**, com o mesmo critério
de nomes curtos. Os 4 comentários do `principal.tex` são documentação velha:
custam uma linha cada e podem ir junto ou ficar.

## Achado 2 — paralelismo quebrado na conclusão (opcional, não bloqueia)

Os quatro fechos do Cap. 6 eram rótulo + frase. Três viraram frase declarativa
inteira ("A composição do conjunto inicial importa…", "É possível capturar esse
espaço sem nenhum rótulo.", "Oráculos LLM são viáveis…"). O quarto virou
rótulo com dois-pontos:

> **O framework integrado: respondido, com veredito refinado e diagnóstico.**

Lê bem e resolve o problema do sujeito que faltava, mas quebra o paralelismo
dos outros três. Uma alternativa na mesma forma dos demais: *"O framework
integrado responde à hipótese, com veredito refinado e diagnóstico."* Redação
é do revisor1; registro como observação, não como pendência.

## Um erro meu, no mesmo espírito do que o revisor1 registrou

Minha primeira checagem de números acusou divergência em `3-metodo`. Era do meu
instrumento: a regex engolia a pontuação final, então `E5, E6` dava o token
`"5,"` e `E5` dava `"5"` — diferença de vírgula lida como número alterado.
Troquei por `\d+(?:[.,]\d+)*` e a igualdade apareceu. Registro porque foi o
mesmo padrão que ele descreveu hoje: o medidor acusa, e antes de acusar o outro
convém conferir o medidor.

## Resumo para o gate

Pode consolidar. O que peço que **não** entre no gate como resolvido é a
notação nos slides — isso continua aberto e merece fatia própria.
