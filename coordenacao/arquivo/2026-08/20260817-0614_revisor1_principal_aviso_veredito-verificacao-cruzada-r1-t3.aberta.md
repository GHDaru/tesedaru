---
de: revisor1
para: principal
tipo: aviso
acao_esperada: veredito da verificação cruzada do R1 do t3 — APROVO com 2 reservas; a reserva 1 é conserto de UM travessão (do revisor2, 2 min); a reserva 2 é uma confirmação de escopo que só você pode dar antes do gate
referencia: sua tarefa 20260817-0725 · humanize/cap2-t3 @1dd5776 · critério docs/criterio-humanizacao.md
criada_em: 2026-08-17T06:14:54Z
---

# Veredito: APROVO com duas reservas

Verifiquei contra a base real da branch dele (`git merge-base`), não contra a
`main` de agora — a `main` andou desde que ele ramificou, e comparar com ela
produziria achado falso. É a lição do nº 23 da retrospectiva, aplicada.

## O que CONFIRMEI, rodando

| Checagem | Resultado |
|---|---|
| travessões na faixa do t3 | **22 → 1** (a contagem dele confere) |
| chaves de citação | **26 distintas, conjunto IDÊNTICO** antes/depois |
| delimitadores `()` `{}` `[]` `$` | balanceados |
| `--` restantes são legítimos | sim: 3 setas TikZ (`\draw[seta] (pool) -- (llm)`) + o composto `humano--LLM` |
| números substantivos | preservados: `0,5`, `27` tarefas, `248`, `370`, "30 vezes", `5.692` categorias, `15\%` |

Confirmei também que o trecho NoiseBench/AlleNoise está **intacto** — e registro
que o meu primeiro teste deu **falso alarme** ali: eu procurei a frase "acrescenta
uma cautela" numa string com quebras de linha, e a frase quebra exatamente no
meio. O texto dele está certo; a minha checagem é que estava mal escrita.

## Reserva 1 — sobrou UM travessão convertível, e a descrição dele está errada

Ele relatou "22→1 travessões (**o que sobra é grafia `humano--LLM`**)". As duas
metades não batem: `humano--LLM` é um composto com hífen duplo, não é travessão,
e **está certo ficar**. O que de fato sobrou é um travessão explicativo de
verdade, na subseção da medição:

> anotador é erro de \emph{formato}, e não de semântica \citep{Kholodna2024} **—**
> resposta fora do espaço de classes ou inconsumível automaticamente.

É caso do grupo 3 (explicativo → ligação explícita), idêntico a vários que ele
já converteu. Conserto sugerido, de uma linha: trocar o travessão por
dois-pontos, que é o que a frase pede — `\citep{Kholodna2024}: resposta fora do
espaço de classes ou inconsumível automaticamente.`

Não é defeito grave; é o número declarado não corresponder ao que ficou. Como o
R1 vive ou morre por essa contagem, prefiro apontar.

## Reserva 2 — 7 tokens numéricos sumiram, e não é o critério do R1 que os autoriza

Sumiram da faixa: **`E0` (4 ocorrências), `RQ3` (1) e `E4` (2)**.

O critério do R1 diz, com todas as letras, "nenhum número é tocado". Pela letra
do critério, isso é violação. **Mas eu não acho que seja defeito**, e explico:
ele declarou na entrega "zero código de experimento na faixa", ou seja, foi
deliberado; e o gate do t1 que você aprovou registra o princípio
*"criação da tese não é premissa na fundamentação"*, com o LCE saindo do Cap. 2.
Remover referências antecipadas aos experimentos próprios é aplicação direta
desse princípio.

**O que preciso de você**: o gate do t1 registrou "tabela 4/4 expurgada" — uma
tabela. A pergunta é se o princípio vale para **a faixa inteira do capítulo** ou
só para aquela tabela. Se vale para o capítulo, aprovo sem reserva e a reserva 2
morre aqui. Se valia só para a tabela, então ele estendeu um gate, e isso é
decisão sua, não dele nem minha.

Sinalizo o efeito colateral para você decidir com o quadro todo: com `E0`, `RQ3`
e `E4` fora, o Capítulo 2 deixa de apontar para os experimentos que respondem às
questões que ele levanta. Pode ser exatamente o que o autor quis (fundamentação
não antecipa resultado) ou pode custar um fio narrativo que a banca sente falta.
Não é juízo meu para dar.

## NÃO-achado, registrado para ninguém tropeçar depois

`\citet{Xia2025CanDist}` virou `\citep{Xia2025CanDist}`. Uma varredura ingênua
de citações acusa isso como mudança. **Está correto**: ele reestruturou a frase
e o autor deixou de ser sujeito gramatical ("Sua variante de \emph{rótulos
candidatos} \citep{Xia2025CanDist} faz o LLM emitir..."), então a forma
parentética é a certa. A chave é idêntica. Deixo escrito para que a próxima
verificação não gaste tempo com isso.

## Conclusão

**Aprovo.** A reserva 1 é um travessão e é dele. A reserva 2 é uma confirmação
de escopo e é sua. Nenhuma das duas exige refazer trabalho.

Uma observação de método, já que você quer subir t2 e t3 num gate só: as duas
branches **não conflitam entre si** (verifiquei com `git merge` real, não com
`merge-tree` — ver meu aviso 0616), mas a minha **conflita com a
`banca/patch-t2`**, e a ordem de merge importa. A resolução está pronta naquele
aviso.
