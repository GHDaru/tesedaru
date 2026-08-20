---
de: revisor2
para: principal
tipo: aviso
acao_esperada: antes de despachar o pacote do t1 para mim, decidir sobre as 2 lacunas abaixo — a segunda precisa da palavra do autor, e é o achado GRAVE nº 1 do meu R4, que fica a 10 linhas de uma das edições aprovadas
referencia: pacote da banca 20260817-0455 (5 edições aprovadas) · meu R4 em 20260817-0038 · 2-fundam/texto.tex
criada_em: 2026-08-17T06:15:00Z
---

# Li o pacote do t1. Aplico quando você despachar — mas há 2 lacunas

O pacote está bom e as edições são claramente melhorias. Duas coisas, porém, é
melhor resolver ANTES de eu encostar no arquivo, senão a mesma zona é editada
duas vezes.

## Lacuna 1 — o expurgo de códigos de experimento está incompleto

A edição nº 4 declara o critério (item 3 do R6: código de experimento não fica
no Cap. 2) e corrige três pontos: l.159, l.199 e l.200. **Mas a tabela tem
quatro linhas**, e as duas restantes continuam com código:

| Linha | Célula "Uso na tese" | Situação |
|---|---|---|
| 199 | `toda acurácia de oráculo (E0)` | corrigida pelo pacote |
| 200 | `pareamentos do E0/E0-P` | corrigida pelo pacote |
| **201** | `E1/E4 (8 sementes)` | **NÃO está no pacote** |
| **202** | `diferença de LCE (E3)` | **NÃO está no pacote** |

Aplicar o pacote como está deixa a tabela **metade expurgada**, o que é pior
que não expurgar: fica parecendo critério aplicado por descuido. Como o pacote
já diz que "as demais ocorrências seguem a mesma receita nos ciclos t3/t4 sem
aprovação item a item", entendo que 201 e 202 se enquadram nessa autorização —
mas elas estão DENTRO da mesma tabela das duas já aprovadas, não em outro tema.
**Confirma que posso aplicar a mesma receita nas quatro linhas?** Se sim,
proponho: l.201 → `duas estratégias sob as mesmas sementes
(Cap.~\ref{ch:resultados-falco})`; l.202 → `diferença de LCE
(Cap.~\ref{ch:resultados-falco})`.

## Lacuna 2 — o "portanto" das oito sementes fica a 10 linhas da edição nº 5

Esta é a mais importante, e é o **achado GRAVE nº 1 do meu R4** (aviso 0038),
ainda sem decisão do autor.

A edição nº 5 mexe nas linhas 163--170 (McNemar/Dietterich). Dez linhas abaixo,
na **linha 180**, está intacta a frase que eu havia sinalizado:

> "...com menos de seis sementes a significância a 5\% é inalcançável por
> construção, **o que fundamenta o mínimo de oito sementes** adotado no
> Capítulo~\ref{ch:metodo}."

A aritmética anterior está certa — com 5 sementes o menor p bicaudal é 0,0625 e
com 6 é 0,03125. O problema é o "portanto": **o argumento apresentado justifica
SEIS, não oito.** O salto não tem premissa no texto. É primo do item
R5-imediato já registrado para o Cap. 3, onde a frase equivalente foi
corrigida — a inferência sobreviveu aqui, em forma mais sutil.

Se eu aplicar as 5 edições e deixar a linha 180 como está, entrego uma seção
"revisada" contendo justamente o tipo de salto lógico que uma banca puxa, a
poucas linhas de onde acabei de mexer.

**Pergunta ao autor, curta:** por que oito e não seis? Basta ele dizer, e o
remédio é uma linha:
- se a razão é margem: *"...fundamenta o mínimo de seis; esta tese adota oito
  por margem"*;
- se a razão é outra (potência, número de braços, custo), escrevê-la.

## O que proponho

Um lote só: as 5 edições aprovadas + as 2 linhas restantes da tabela + a
correção da linha 180 conforme a resposta do autor. Uma passagem, um lock, um
gate — em vez de três idas ao mesmo parágrafo.

Se o autor não quiser decidir agora, aplico as 5 aprovadas e deixo a linha 180
explicitamente registrada como pendência no gate — mas registrada, não
esquecida.

Aguardo o despacho. Nada começa sem ele.
