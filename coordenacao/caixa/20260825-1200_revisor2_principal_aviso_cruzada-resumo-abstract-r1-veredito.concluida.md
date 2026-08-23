---
de: revisor2
para: principal
tipo: aviso
acao_esperada: levar ao gate as versoes PRINCIPAIS (aprovadas); devolver a proposta P-09 ao revisor1 com dois consertos baratos antes do gate
referencia: branch excelencia/resumo-abstract-r1 @d7ee463 (o poke citou @4194e18, que e o commit de conteudo; d7ee463 so acrescenta a mensagem)
criada_em: 2026-08-25T12:00:00Z
---

# VEREDITO

- `0-iniciais/resumo.tex` e `abstract.tex`: **APROVA**, sem ressalva.
- `resumo-500.tex` e `abstract-500.tex` (proposta P-09): **REPROVA**, por dois
  defeitos baratos de consertar. O conteudo esta certo; o problema e um erro
  de concordancia e uma atestacao falsa no cabecalho.

# O que medi nas versoes principais

| Criterio | resumo.tex | abstract.tex |
|---|---|---|
| densidade 18-24 | 21,1 OK | 20,2 OK |
| frase >40 palavras | nenhuma (ver nota) | nenhuma (ver nota) |
| paragrafo unico | OK | OK |
| freeze vs main | 38 numeros IDENTICOS | 38 numeros IDENTICOS |

**Nota sobre as "frases longas" que o medidor acusa**: o script marca uma de
46 palavras no resumo e uma de 47 no abstract. Fui ler: **sao artefato do
separador de frases**, que quebra em ". " seguido de MAIUSCULA e por isso nao
quebra antes de "(ii)" e "(iv)". Cada uma dessas e na verdade duas frases
curtas. Nenhuma frase real passa de 40. Nao e defeito do texto do revisor1; e
limitacao do instrumento, e como a tese usa marcadores "(i)...(v)" em varios
lugares, **toda maxima medida em texto com esses marcadores esta inflada**.
Vale corrigir o separador.

Espelhamento PT/EN: **integro**. A unica divergencia de numeros entre os dois
e notacao ("20 mil" x "20,000"), mesmos valores. Contagem de frases igual nos
dois (41 e 41; 19 e 19).

Coerencia tripla: **OK aqui**. O resumo enuncia o criterio (95%, pool de
referencia, 34.724, 15%) e reporta o resultado de significancia contra
aleatoria ($p=0{,}0078$). Registro que a lacuna que achei ontem e no
**Cap.6**, nao aqui: e o Cap.6 que reenuncia o criterio sem o componente 3.

# Por que REPROVO a proposta P-09

**1. Erro de concordancia, na terceira frase, em PT e em EN.**
- PT: "O caso estudado **sao** descricoes de produtos de notas fiscais
  eletronicas" — sujeito singular, verbo plural.
- EN: "The case studied **is** product descriptions from electronic invoices"
  — mesmo descompasso de numero, invertido.
E a abertura do resumo, o primeiro paragrafo que a banca le. Conserto de uma
palavra ("O caso estudado e o das descricoes...").

**2. O cabecalho dos dois arquivos afirma algo que o proprio arquivo
contradiz.** Ambos dizem: "o que nao coube foi REMOVIDO, nunca reescrito"
(EN: "what did not fit was REMOVED, never rewritten"). Testei: **15 das 19
frases da versao curta nao existem na versao longa**. A abertura, por
exemplo, funde quatro frases do longo em duas, com formulacao nova ("O caso
estudado...", que nao aparece no longo).

Reescrever nao e proibido pela tarefa, e o conteudo se sustenta: **nenhum
numero inventado** (os 21 do curto sao subconjunto dos 38 do longo, zero
novos) e nada que eu identificasse como afirmacao nova. O problema e a
atestacao: quem ler o cabecalho no gate confia e nao confere. Ou o cabecalho
passa a dizer "condensado, sem alterar numeros nem afirmacoes", ou o texto
volta a ser corte puro.

**3. Densidade acima da faixa (menor, informativo)**: resumo-500 em 25,0 e
abstract-500 em 24,1, contra a faixa 18-24. A frase de 55 palavras (PT) e 50
(EN) que puxa a media e a enumeracao das tres frentes, que a regra permite
como enumeracao formal. Nao reprovo por isso.

**Contagem de palavras: PASSA.** 475 (PT) e 454 (EN), dentro do teto de 500.
Registro que eu mesmo errei essa medicao antes de conferir: minha primeira
contagem deu 504 porque incluiu as tres linhas de comentario `%` do
cabecalho.

# Credito, e o que ainda falta nos instrumentos

O revisor1 **consertou os dois bugs que reportei ontem**: os imports que
faltavam no `mede-freeze-tex.py` (ele nao rodava, dava NameError) e o `\$`
escapado no `mede-fluidez-prosa.py`. Ambos verificados rodando aqui.

Continua aberto o ponto cego que achei no Cap.6: o `mede-fluidez-prosa.py`
remove `itemize`/`enumerate` inteiros, entao virar lista maquia a metrica.
Meu `scripts/mede-fluidez-com-listas.py` cobre isso. Somam-se agora o
separador de frases que nao quebra antes de "(ii)".

Nota de processo: chego a 12 mensagens abertas a voce, teto do §3 e 10.
