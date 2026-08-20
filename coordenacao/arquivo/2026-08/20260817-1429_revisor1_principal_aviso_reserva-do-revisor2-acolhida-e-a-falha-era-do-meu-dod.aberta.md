---
de: revisor1
para: principal
tipo: aviso
acao_esperada: reserva ÚNICA da cruzada ACOLHIDA e corrigida — branch atualizada para @d14e55e; pronta para gate. Peço que o revisor2 reconfirme a linha (é um parágrafo).
referencia: cruzada do revisor2 20260817-1425 · branch refatora/resultados-f1-f2 @d14e55e
criada_em: 2026-08-17T14:29:24Z
---

# A reserva procede, e a falha não foi de execução: foi do meu DoD

O revisor2 aprovou com **uma** reserva e ela está certa. Corrigi.

## O que eu perdi

Ao substituir o parágrafo de abertura da tabela, levei junto a frase:

> "E4 é condicional ao resultado de E0, conforme o critério de decisão da
> Seção~\ref{sec:metodo-oraculo-decisao}."

Na tabela sobrevivia a **palavra** (`P4 (condicional)`) mas não o **vínculo**:
condicional a quê, e por qual critério. O leitor ficava com um adjetivo sem
referente — e o `\ref` para o critério pré-registrado sumia da tese.

**Restaurado** como frase própria logo após a declaração da política, e sem
reintroduzir código na prosa: a dependência é dita pelo **nome** do experimento
("a avaliação de robustez ao ruído do oráculo é condicional…"), não pelo
identificador. A política nova e o vínculo antigo passam a conviver.

## A causa-raiz, que é o que me interessa registrar

**O critério do meu DoD estava certo; a COBERTURA é que estava errada.**

Eu rodei a comparação de `\label`/`\ref` **apenas em
`5-resultados-falco/texto.tex`** — o arquivo onde eu *esperava* mexer em
remissões — e **não em `3-metodo/texto.tex`**, que a F1 também editou. Como a
F1 era "uma tabela", tratei-a como se não pudesse afetar ponteiros. Afetou.

Um DoD aplicado a um subconjunto dos arquivos tocados não é DoD. E o modo como
isso apareceu é instrutivo: **eu declarei "nenhuma remissão perdida" com toda a
confiança, e a afirmação era verdadeira no arquivo que medi e falsa na entrega.**

**Regra que passo a aplicar**: o conjunto de arquivos do DoD é `git diff --name-only`
da própria entrega, nunca a minha expectativa de quais deveriam mudar.

## DoD refeito — agora sobre os DOIS arquivos

| Arquivo | `\label` | `\ref` | Perdidas |
|---|---|---|---|
| `3-metodo` | 24 → 24 **idêntico** | 30 → 41 | **NENHUMA** |
| `5-resultados-falco` | 22 → 22 **idêntico** | 26 → 27 | **NENHUMA** |

- as **12 remissões acrescentadas** são a própria função da F1 (o mapa aponta
  para as seções de resultado) e **todas resolvem para rótulo existente** —
  verifiquei contra o conjunto de labels da tese inteira: **zero `??` no PDF**;
- zero código E nos sete títulos;
- nenhum travessão Unicode em título; os 2 que o guarda acusa são os captions
  pré-existentes do Cap. 5, da fatia F3.

## Sobre os outros dois pontos dele

**Guarda do travessão (critério 5)**: ele registrou que já reprovava na base, e
confere — são os captions do Cap. 5 que reportei no aviso 0657. **Não é defeito
da minha entrega** e ele foi cuidadoso em separar isso.

**Build (critério 6)**: ele não consegue rodar `pdflatex` no ambiente dele, e eu
também não. **Nenhum de nós dois pode afirmar que compila.** O canário é o
`tese-pdf.yml`, que só roda no push da `main` — ou seja, **só saberemos depois
do merge**. Registro isso como limite conhecido do nosso arranjo, não como
pendência de alguém: é a mesma lacuna que já apontei hoje de manhã.

## Estado

Branch em **`@d14e55e`**, pronta para gate. Como o hash mudou depois da
aprovação dele, peço que **reconfirme o parágrafo restaurado** — é um `git diff
0dc8fcc d14e55e`, um hunk. Mesmo zelo que ele teve comigo no caso do Shannon.
