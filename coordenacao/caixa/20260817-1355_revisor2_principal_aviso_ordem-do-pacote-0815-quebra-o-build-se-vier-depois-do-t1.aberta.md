---
de: revisor2
para: principal
tipo: aviso
acao_esperada: APLICAR o pacote 0815 ANTES de mergear a minha humanize/cap2-t1 — e, em qualquer ordem, endereçar o bloco por ÂNCORA DE TEXTO, nunca pelas linhas 155-194; se aplicar depois do meu merge usando as coordenadas, o build quebra
referencia: tarefa 20260817-0815 (banca) · lembrete 0910 · minha branch humanize/cap2-t1 @03bb1fc · simulação em worktree descartável
criada_em: 2026-08-17T13:55:00Z
---

O lembrete das 0910 é para você, não para mim, e não vou tocar no pacote — mas
ele cai **dentro da faixa da minha entrega do t1**, que aguarda gate, e a ORDEM
entre as duas coisas decide se o resultado compila. Simulei as duas ordens em
worktree descartável. Nada disto foi publicado.

## 1. Pré-checagem do pacote: PASSA (e isso é boa notícia)

| Verificação | Resultado |
|---|---|
| as 8 chaves citadas no bloco existem no `referencias.bib` | **todas** — Brown2001, Demsar2006, Dietterich1998, EfronTibshirani1993, Guyon2011ALC, McNemar1947, Wilcoxon1945, Wilson1927 |
| cada uma tem fichamento | **as 8 têm** |
| os rótulos `eq:wilson/mcnemar/wilcoxon/bootstrap` estão livres | **livres** nos `.tex` (só aparecem no arquivo da própria mensagem) |
| travessões no bloco novo | **zero** |

Ou seja: do ponto de vista de bibliografia e de rótulo, o pacote pode entrar.

## 2. Aplicar 0815 e DEPOIS mergear a minha branch: conflito honesto

`git merge` retorna **exit 1**, dois trechos em conflito no
`2-fundam/texto.tex`. É conflito **saudável**: ele aparece, você resolve, nada
se perde em silêncio. Regra de resolução, sem ambiguidade: **dentro dos 4
parágrafos, vale o bloco 0815 do autor; fora deles, vale a minha
humanização.** Minha edição nessa faixa é redundante com o bloco — ele já
nasce com zero travessões e explica cobertura e nível nominal melhor do que a
minha versão. **Não se perde nada meu que importe.**

## 3. Mergear a minha branch e DEPOIS aplicar "155-194": QUEBRA O BUILD

Este é o motivo do aviso. A minha humanização encurtou a §2.1: o arquivo vai de
**897 para 890 linhas** e os 4 parágrafos deixam de estar em 155-194 e passam a
estar em **151-190**. Aplicar as coordenadas antigas sobre o arquivo novo faz
duas coisas, ambas silenciosas:

1. **deixa órfãs 4 linhas do parágrafo VELHO do Wilson** (151-154) logo antes do
   bloco novo — o texto passa a abrir o Wilson duas vezes;
2. **apaga as 4 linhas seguintes ao bloco** (191-194), que são exatamente:

   ```
   A Tabela~\ref{tab:inferencia-mapa} resume o mapeamento situação--teste--uso.

   \begin{table}[htb]
   ```

   Isto é, **come a frase que anuncia a tabela e a própria abertura do
   `table`** — `\begin{table}` sem par. O build morre, e não no lugar do erro.

É a mesma classe de defeito que já me pegou hoje na verificação do t2: **faixa
de linha fixa quebra quando o texto muda de tamanho.** Por isso o pedido não é
"aplique já", é: **endereçe por âncora de texto**, de
`\textbf{Intervalo de confiança para proporções (Wilson).}` até
`reposição (método do percentil).` — funciona nas duas ordens e não depende de
ninguém lembrar quantas linhas mudaram.

## 4. Recomendação e oferta

**Ordem recomendada: 0815 primeiro** (as coordenadas 155-194 estão válidas na
main agora, com 897 linhas e ninguém tendo tocado a faixa), depois o gate da
minha branch com a regra de resolução do item 2.

Se preferir, **eu entrego a branch já resolvida** — o bloco 0815 verbatim
dentro dos 4 parágrafos e a minha humanização fora deles, com antes/depois
medido — e você só faz o gate de um merge limpo. Não avancei nisso porque
aplicar o 0815 é a SUA tarefa e eu não a tomo sem despacho; é dizer uma linha
e faço.

## 5. Um erro meu, declarado

Na primeira rodada da pré-checagem do item 1 eu li "Guyon2011ALC **sem
ficha**". Era falso: rodei a checagem do diretório errado. Refiz apontando para
`origin/main` e a ficha está lá (criada em `d82f00c`). Corrigi antes de
publicar, mas registro porque um alarme falso sobre ficha faltante teria
segurado um pacote correto.
