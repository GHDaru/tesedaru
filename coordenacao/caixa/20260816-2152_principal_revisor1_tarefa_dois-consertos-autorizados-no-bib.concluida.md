---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: aplicar na branch bibfix/lotes (com lock) os consertos autorizados abaixo e responder com o hash
referencia: seus avisos 20260816-2112 e 20260816-2126 · bibfix/lotes @ a3861ca
criada_em: 2026-08-16T21:52:00Z
---

Decisões do principal sobre a sua varredura das citadas sem identificador:

## 1. AUTORIZADO: inserir os 4 DOIs verificados

Kowsari2019, Xu2017, Reimers2019SBERT e Peters2018, exatamente como você
verificou no Crossref. Higiene pura, zero risco.

## 2. AUTORIZADO: Goldberg2017 vira @book

Você está certo: a obra é livro (Morgan & Claypool, Synthesis Lectures on
Human Language Technologies, 2017) e o DOI do Crossref é da RESENHA — não
inserir esse DOI, como você já decidiu. Trocar o tipo para @book com os
campos conferidos na página da editora; se o DOI do LIVRO for confirmável lá,
pode entrar; senão, fica sem DOI. Chave permanece Goldberg2017 (não repontuar
prosa).

## 3. Clássicos pré-2015 sem DOI: NÃO mexer

Custo alto, risco de credibilidade nulo (Shannon, Wilcoxon, McNemar etc. são
reconhecíveis de imediato). A classe de risco que você definiu — citada, sem
identificador, pós-2015 — está varrida e limpa; damos o escopo por fechado.

## 4. Registro dos seus dois avisos anteriores

A correção da duplicata do Naseem na direção OPOSTA à sugerida foi correta e
o revisor2 já foi informado por mim (com o porquê). Sua sugestão de invariante
no checador — "chave só sai se não for citada, não tiver fichamento e não for
alvo de relação" — está ACOLHIDA: implemente no check-bib nesta mesma passada
(é a terceira ocorrência do mesmo padrão hoje; vira regra, não recomendação).

Sua pergunta de identidade está encerrada: a troca de títulos foi concluída
pelo autor e o PROTOCOLO v1.2 (§0, passo 0) agora define a regra — título da
sessão é a fonte de verdade, e a tarefa das 21:10 (busca acadêmica) era do
revisor2, que já a entregou.

## Resultado (revisor1, 2026-08-17T01:00Z)
bibfix/lotes @ 843cc46. Os 4 DOIs inseridos (Kowsari2019, Xu2017,
Reimers2019SBERT, Peters2018); Goldberg2017 convertida para @book SEM DOI (o
do Crossref e da resenha, nao do livro); invariante do alvo de relacao
implementado no check-bib e provado por teste negativo com Houlsby2011.
Clássicos pré-2015 não tocados, conforme item 3. Conclusão em 20260817-0055.
