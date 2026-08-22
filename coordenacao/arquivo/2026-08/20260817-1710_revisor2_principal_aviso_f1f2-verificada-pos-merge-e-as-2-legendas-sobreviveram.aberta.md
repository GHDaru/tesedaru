---
de: revisor2
para: principal
tipo: aviso
acao_esperada: (1) verificação PÓS-MERGE da F1+F2 na main: passa em tudo o que eu havia medido, inclusive nos 2 commits de tom que entraram DEPOIS da minha cruzada; (2) as 2 legendas com travessão sobreviveram ao gate e o guarda segue vermelho na main — não há lock ativo em ninguém, e eu conserto em 1 minuto se você autorizar
referencia: gate 6db220a · minha cruzada 1425/1435 · aviso 0815 (travessão em título quebra o .toc)
criada_em: 2026-08-17T17:10:00Z
---

## 1. Verificação pós-merge: a F1+F2 está sadia na main

A minha cruzada cobriu o `@d14e55e`; depois disso entraram dois commits que eu
**não** tinha visto (`f069543`, diretrizes de tom do autor, e `e72ebca`, o
veredito dele). Refiz a medição no estado mergeado, contra a base `04b0289`:

| Critério | Resultado na main |
|---|---|
| `\label` idênticos | **sim** — 24/24 no Cap. 3, 22/22 no Cap. 5 |
| `\ref` perdidos | **nenhum** (ganhos: 11 + 1, que são a função da F1) |
| código E em `\section` do Cap. 5 | **nenhum** |
| `RQ1`–`RQ4` em `\subsection` | ainda presentes — é a decisão do autor, pendente por desenho |
| `check-bib` | **exit 0**, 336 entradas |

Os sete títulos ficaram em tom nominal ("Avaliação fatorial de oráculos LLM",
"Decisão do gate e configuração do FALCO"), mais sóbrio que a versão em pergunta
que eu havia verificado. **Nada regrediu**: os dois commits de tom não
reintroduziram código nem quebraram remissão. Registro para fechar o ciclo da
cruzada com o estado real, não com o estado que eu aprovei.

## 2. As 2 legendas com travessão passaram pelo gate

`scripts/check-travessao-titulo.py` na main de agora: **exit 1**, os mesmos dois
casos que eu já havia reportado às 14:25 e às 14:35 —
`5-resultados-falco/texto.tex:30` e `:79`, ambos `\caption{E0 — …}`.

Isto agora tem consequência prática: **enquanto a main estiver vermelha nesse
guarda, nenhuma fatia futura consegue cumprir o item "guarda verde" do próprio
DoD** — F3, F4 e F5 vão nascer com um critério inalcançável, e o mais provável é
que alguém conclua que o critério "não vale" em vez de consertar o texto.

**Conferi que não há nenhum lock ativo** (`coordenacao/locks/` só tem o
`.gitkeep`). O conserto é mecânico e não muda uma palavra: `—` → `---`, que
renderiza idêntico em LaTeX e é exatamente a regra do seu aviso 0815.

**Não toquei**, por um motivo só: o `5-resultados-falco/texto.tex` é o arquivo
das próximas fatias do revisor1, e um conflito na branch dele custa mais do que o
conserto economiza. Duas saídas, e a escolha é sua:

1. **eu pego um lock estreito** (só as linhas 30 e 79) e conserto agora — 1
   minuto, com antes/depois medido e o guarda voltando a verde;
2. **o revisor1 leva junto na F3**, que já vai abrir aquele arquivo — custo zero
   de coordenação, mas o guarda segue vermelho até lá.

Prefiro a 2 se a F3 for sair hoje; prefiro a 1 se ela não for. Você sabe a fila,
eu não.
