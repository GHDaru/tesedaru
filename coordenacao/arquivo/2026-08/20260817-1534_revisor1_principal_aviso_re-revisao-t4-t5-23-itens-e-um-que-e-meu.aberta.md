---
de: revisor1
para: principal
tipo: aviso
acao_esperada: aplicar os 23 itens de docs/re-revisao-registro-t4-t5.md na ordem sugerida; ATENÇÃO aos itens 13-14, que são defeito visível no PDF; e 4 itens exigem conferência contra ficha antes de tocar
referencia: tarefa 20260817-1420 (ordem do autor via banca, checklist de 9 itens) · docs/re-revisao-registro-t4-t5.md
criada_em: 2026-08-17T15:34:33Z
---

# Re-revisão de registro de t4 e t5: 23 itens, nenhuma linha editada

Levantamento em `docs/re-revisao-registro-t4-t5.md`, no formato que você pediu
(antes/depois proposto, sem editar prosa).

| Item do checklist | t4 | t5 | Total |
|---|---|---|---|
| (a) palavra inflada | 3 | 1 | 4 |
| (b) metáfora | 2 | 3 | 5 |
| (d) nome em prosa sem `\citet` | 0 | **2** | **2** |
| (f) estrangeiro / sigla | 6 | 4 | 10 |
| (g) algoritmo sem atribuição | 1 | 1 | 2 |
| (c), (e), (h), (i) | 0 | 0 | 0 |

## Os dois que eu aplicaria primeiro, e não são de estilo

**Itens 13 e 14**: `"Ein-Dor et al. \cite{EinDor2020}"` e `"Griesshaber et al.
\cite{Griesshaber2020}"`. Com `\cite`, o PDF imprime *"Ein-Dor et al. (EIN-DOR
et al., 2020)"* — **o nome sai duas vezes e o sobrenome não vira link**. Com
`\citet`, o pacote gera o nome ligado.

É **defeito de saída**, não preferência de registro. Custa dois caracteres cada.

## Quatro itens que NÃO devem ser aplicados sem conferência contra ficha

Os itens 12, 17, 20 e 22 inserem ou reatribuem chave de citação: a atribuição do
SBERT, o termo real que o `Yuan2020` usa para a "surpresa" do modelo, e a fonte
que nomeia o "efeito de cluster perdido". **Marquei-os como bloqueados por
conferência** — é a mesma disciplina do princípio II, e o único subconjunto em
que a edição de registro esbarra em conteúdo.

## Uma decisão de régua que é do autor, não minha

No item (f), **não listei todo estrangeirismo**. "\textit{tweets}",
"\textit{embeddings}" e "\textit{bag-of-words}" já são correntes na área e a
tese os usa em itálico, que é a convenção. Listei os que um leitor de banca pode
legitimamente não conhecer e as siglas nunca expandidas (TF--IDF, SVM, KNN,
SBERT, ECOICOP).

**Glosar tudo é tão ruidoso quanto não glosar nada.** Se ele quiser a régua mais
estrita, é só ampliar a lista — mas quis que a escolha fosse consciente e dele,
não um efeito colateral do meu critério.

## E um item (c) que é MEU, fora da minha faixa

O checklist do autor lista **"autoridade decorativa — 'no espírito de X'"**. Isso
descreve exatamente uma frase que **eu escrevi hoje**, no t2:

> "…\citep{Settles2012}, **no espírito de** \citet{Shannon1948}: buscar
> ativamente a informação que mais reduz a incerteza."

A história vale registrar: o texto tinha "— no espírito de"; no R1 eu troquei
por "**é o** espírito de"; o revisor2 apontou, com razão, que isso **atribuía** a
Shannon uma posição que ele não tomou; eu restaurei o "no espírito de" e tratei
como resolvido.

**O autor diz que nenhuma das duas serve.** A citação deve estar onde o conceito
é tecnicamente exato — e Shannon (1948) é teoria da comunicação, não seleção de
instâncias. **Dois revisores gastaram uma rodada discutindo qual preposição usar,
quando a pergunta era se a citação devia estar ali.**

Sugestão: remover a evocação, ou citar Shannon onde a entropia é de fato usada
(a equação da amostragem por incerteza). Não é da minha faixa nesta tarefa e não
toquei — registro porque é meu e porque mostra que este checklist pega o que dois
revisores deixaram passar duas vezes.

## Estado

Tarefa 1420 concluída. A parte do **t3 é do revisor2**, quando ele liberar.
Sigo aguardando o gate da F1+F2 e **não inicio F3/F4/F5/F7**.
