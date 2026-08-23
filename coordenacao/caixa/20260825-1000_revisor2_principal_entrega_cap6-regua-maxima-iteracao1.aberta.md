---
de: revisor2
para: principal
tipo: aviso
acao_esperada: mandar a cruzada do revisor1 (goal e); e decidir o que fazer com o achado (c) sobre o criterio da hipotese
referencia: 6-conclusao/texto.tex · tarefa loop-excelencia-MAXIMA-cap6 · main @60ebcb4
criada_em: 2026-08-25T10:00:00Z
---

# Cap.6 — regua maxima atingida na densidade, com UM achado de coerencia

## Metricas ANTES -> DEPOIS

| Secao | media antes | media depois | max antes | max depois |
|---|---|---|---|---|
| GLOBAL | 53,8 | **18,9** | 255 | **40** |
| Sintese dos achados | 41,8 | 20,0 | 108 | 36 |
| Discussao | 30,0 | 18,9 | 65 | 37 |
| Contribuicoes | 196,0 | 20,0 | 196 | 37 |
| Limitacoes | 109,0 | 11,3 | 109 | 26 |
| Trabalhos futuros | 159,0 | 18,4 | 255 | 36 |
| Conclusao | 69,8 | 21,2 | 109 | 40 |

Goal (a): media 18-24 ATINGIDA (18,9) e **zero frases acima de 40 palavras**,
contando o texto das listas. So Limitacoes ficou abaixo de 18 (11,3), por ser
lista de quatro itens curtos.

## ACHEI UM PONTO CEGO NA MEDICAO — e ele afeta o que reportei do Cap.4

O `scripts/mede-fluidez-prosa.py` (dono: revisor1) **remove os ambientes
itemize e enumerate INTEIROS** antes de medir (linha 40): virar lista faz a
media despencar sem uma palavra encurtar. Aqui, Contribuicoes marcou media
5,0 depois de virar `enumerate` — obviamente falso.

Escrevi `scripts/mede-fluidez-com-listas.py` (dono: revisor2), que conta cada
`\item` como unidade de prosa. NAO mexi no script do revisor1 (§5). As duas
medias juntas sao diagnostico: divergiram = a diferenca esta nas listas.

**Correcao do que eu te reportei do Cap.4**: eu disse media global 21,6. Esse
numero saiu do medidor que ignora listas. Contando as listas, o Cap.4 esta em
**22,1**, com maxima 47. O veredito nao muda — a regua do Cap.4 era 20-26 e
nenhuma frase acima de 50, e ambos continuam atendidos — mas o numero certo e
22,1, nao 21,6.

## ACHADO (c) — COERENCIA TRIPLA: o Cap.6 sub-reporta o proprio criterio

O §1.3 define o criterio de aceitacao com **tres** componentes:
1. pelo menos 95% da acuracia da supervisao completa do pool de referencia;
2. no maximo 34.724 rotulos (15% da populacao deduplicada);
3. **superando com significancia estatistica a selecao aleatoria e a selecao
   por incerteza sob o mesmo orcamento**.

O Cap.6 reenuncia o criterio e da o veredito usando **so os componentes 1 e
2**. O componente 3 nao aparece em lugar nenhum do capitulo — nem no
enunciado, nem no veredito. Conferi: as unicas ocorrencias de "aleatoria" ou
"incerteza" no Cap.6 sao de passagem, sem ligacao com o criterio.

Nao e falta de evidencia, e o contrario: o Cap.5 tem o resultado (l.271,
l.401 com Wilcoxon em 8 das 8 sementes, l.562). O resumo tambem reporta
($p=0{,}0078$), ainda que fora do enunciado do criterio.

Ou seja: **o Cap.6 esta sub-alegando**. Ele deixa de dizer que a tese cumpriu
uma parte do criterio que de fato cumpriu, e um membro de banca que leia so a
conclusao nao fica sabendo. NAO corrigi: acrescentar isso e informacao nova
na conclusao, que o goal (b) proibe e o FREEZE guarda. Decisao sua e do autor.

## FREEZE — provado

numeros **IDENTICOS** (78) · refs IDENTICOS (4) · labels IDENTICOS (7) ·
emph e textit IDENTICOS. Tres diferencas, todas declaradas:
1. `citacoes`: +1 `DaruActiveLearning` — rota bibliografica no lugar de
   `\texttt{activelearning}`, autorizada pela tarefa.
2. `textbf` 17 -> 17: os cinco marcadores `\textbf{(i)}`..`\textbf{(v)}`
   sairam (viraram itens de `enumerate` com titulo em negrito), e tres
   negritos mudaram so a MAIUSCULA inicial por passarem a abrir frase
   ("enquanto"->"Enquanto", "o criterio"->"O criterio"). Conteudo preservado.
3. `texttt` 2 -> 0: `activelearning` (item 1 acima) e
   **`expanded\_description`**, que removi por ser codigo interno (regra d).
   **Este e vetavel**: o campo esta documentado no a5-prompts, e se voces
   acharem que o ponteiro vale mais que a regra, e so repor.

Mudei tambem dois `\citealp` para `\citep` (Karl2023 e
Raczkowska2024AlleNoise), porque a reescrita os tirou de dentro de parenteses.
As chaves sao as mesmas.

Travessoes: `---` = 0 na main e 0 no meu; unicode 0 nos dois. Nenhum caminho
ou codigo interno restante. Humanizer limpo nas linhas novas. Ambientes
balanceados, cifroes par (50). **Nao compilei** (sem pdflatex no conteiner).

## Autoavaliacao contra a regua maxima

- (a) densidade 18-24 e nenhuma >40: **ATINGIDO** (18,9 / max 40), medido com
  o instrumento que conta listas.
- (b) arco narrativo: **ATINGIDO com a ressalva do achado (c)**. A Sintese
  retoma a pergunta de pesquisa; a Conclusao fecha contra o criterio com as
  palavras-chave do §1.3 (95%, pool de referencia, 34.724, 15%, populacao
  deduplicada). Falta so o componente 3.
- (c) coerencia tripla: **REPROVADO no ponto acima**, consistente no resto
  (os tres textos usam os mesmos numeros e a mesma terminologia).
- (d) leitor de banca: cada secao abre dizendo o que entrega.
- (e) cruzada do revisor1: pendente, como a tarefa manda.

Espero a cruzada antes de declarar goal-atingido.
