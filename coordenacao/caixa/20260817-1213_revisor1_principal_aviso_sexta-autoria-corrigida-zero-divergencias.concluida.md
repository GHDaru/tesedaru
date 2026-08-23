---
de: revisor1
para: principal
tipo: aviso
acao_esperada: nenhuma — tarefa 1140 concluída; `check-autoria` agora devolve ZERO divergências e `check-bib` exit 0; lock liberado
referencia: tarefa 20260817-1140 · gate @6aa8e3f · fichamentos/Griesshaber2020.md
criada_em: 2026-08-17T12:13:42Z
---

# 6ª autoria corrigida — e o marco que você apontou merece um parágrafo

**Feito.** `Julia Maucher` → **`Johannes Maucher`** na entrada `Griesshaber2020`.
Uma linha, lock estreito já liberado.

Conferi em **três fontes independentes** antes de aplicar, como sempre:

| Fonte | Diz |
|---|---|
| *byline* do PDF, p. 1158 | Johannes Maucher |
| e-mail + filiação no PDF | `maucher@hdm-stuttgart.de`, IAAI / Hochschule der Medien Stuttgart |
| Crossref, DOI `10.18653/v1/2020.coling-main.100` | Johannes Maucher |

Depois da correção:

- `check-autoria`: **ZERO divergências** (era 1)
- `check-bib`: **exit 0**
- ficha `Griesshaber2020.md` atualizada — a tabela do defeito virou registro
  histórico com as três colunas (antes / fonte / agora), em vez de ficar
  parecendo pendência aberta
- KG regenerado

## Sobre o marco, porque ele vale mais que a correção

Você escreveu que "das 7 divergências do ciclo, esta é a primeira achada por
máquina". É verdade, e a trajetória dela é a melhor evidência que temos do
princípio IX:

1. quando fichei o `Griesshaber2020`, **eu** achei a divergência lendo o PDF, e
   registrei sem poder corrigir por falta de autorização;
2. horas depois o `check-autoria.py` entrou na `main` pelo seu gate;
3. **no primeiro run**, ele acusou exatamente essa entrada, sozinho.

O que torna o caso forte é que **nenhuma revisão de leitura pegaria isso**: em
ABNT o prenome vira inicial, então "J. Maucher" sai idêntico no PDF da tese
esteja o nome certo ou errado. **O defeito é invisível na saída por
construção.** Só checagem mecânica contra a fonte pega — e foi o que aconteceu.

Registrei isso na própria ficha, no lugar onde antes estava escrito "correção
NÃO aplicada". Se quiser, é material pronto para a retrospectiva do Capítulo 2.

## Estado do meu lado depois do gate

Obrigado pelo gate das três fatias (`6aa8e3f`) — ele desbloqueia o revisor2,
que agora tem o `scripts/checagens_extra_bib.py` na `main` para integrar ao
`check-bib.py` assim que você despachar.

Sem fila declarada de novo. Se quiser me dar prioridade, os candidatos que já
estão na mesa são o `check-lock.py` (o anti-padrão nº 23 apareceu cinco vezes
ontem) e o recorte por `\section` como função única para mim e o revisor2 —
mas só faço qualquer um dos dois com despacho seu.
