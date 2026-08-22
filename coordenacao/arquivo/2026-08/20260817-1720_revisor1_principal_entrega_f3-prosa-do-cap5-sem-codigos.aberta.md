---
de: revisor1
para: principal
tipo: entrega
acao_esperada: gate da F3 — branch refatora/resultados-f3 @9d4a751 (inclui o conserto 4609830 do revisor2, dele, íntegro). Pedir a cruzada do revisor2 sobre TODOS os arquivos do diff (é 1: o texto do Cap.5)
referencia: tarefas 1240/1400 · claim 1705 · gate F1+F2 6db220a · aviso 1710 do revisor2
criada_em: 2026-08-17T17:20:00Z
---

## F3 entregue: a prosa do Cap. 5 fica com ZERO código de experimento (era 28)

Padrão aplicado — o do próprio autor (`a7e8b91` no Cap. 2 e o veredito
`e72ebca` nos títulos): **remover o código mantendo a frase**; onde a remissão
agrega, o código vira `Seção~\ref{}`. Três exemplos representativos:

| Antes | Depois |
|---|---|
| "é a hipótese testada **no E4**." | "é a hipótese testada **na Seção~\ref{sec:res-e4}**." |
| "(i) o **E4 torna-se obrigatório**, executado…" | "(i) a **avaliação de robustez ao ruído torna-se obrigatória**, executada…" |
| "o braço **E35** (35 mil rótulos ativamente selecionados) supera a régua" | "o braço **de 35 mil rótulos ativamente selecionados** supera a régua (a linha da tabela segue identificável pela contagem)" |

## Decisões de escopo, declaradas

1. **Legendas e células de tabela (13 ocorrências) FICAM** — são a fatia de
   migração para a tabela-mapa, que entrego separada para o gate julgar
   isolado. As 2 legendas da F3 entraram pelo conserto do revisor2 (o
   travessão), que está na base da branch.
2. **Notação RQ1–RQ4 intocada** — decisão do autor pendente, registrada.
3. **Um caso limite**: `E3` (revalidação com BERTimbau) NÃO virou
   `\ref{sec:res-e3p}` — E3 (planejado) ≠ E3′ (executado); apontei para o
   desenho (`sec:metodo-falco-baselines`), que é o que a frase promete.

## DoD (executável, sobre TODOS os arquivos do `git diff --name-only` = 1)

```
labels: multiconjunto IDÊNTICO (22/22)
refs:   nenhum perdido; +12 ganhos (códigos → remissões): res-e0 1→4,
        res-e4 2→5, res-e1 2→4, res-e6 1→3, res-e0p 1→2, metodo-falco-baselines 2→3
códigos por contexto: prosa 28→0 · título 0 · legenda/célula 13 (declarado) ·
        label/ref 49 · artefato 4 (+1: experiments/e0 substituiu "do E0")
check-travessao-titulo: exit 0 (a branch nasce do conserto 4609830)
check-bib: exit 0 (336 entradas)
```

Régua §7: **nenhuma das 4 regras acionada** — as frases novas são descritivas;
nenhum número, IC ou conclusão foi tocado (fight-the-pile-up: des-densificar
sem mudar conteúdo técnico).

Lock de `5-resultados-falco/texto.tex` LIBERADO neste push. Próximas na fila,
aguardando este gate: **F4** (prosa do Cap. 3, inclui os 4 títulos com código) e
**F5** (Cap. 6); a fatia de migração das legendas/células fecha a conta das 105.

## Resultado (principal)
Entrega processada e integrada; arquivada na limpeza.
