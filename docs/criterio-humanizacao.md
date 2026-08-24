# Critério de humanização (R1) — aprovado pelo autor em 2026-08-16

Referência viva: o lote 1 do Cap. 2 (merge na main) é o exemplar aprovado.
Aplique o MESMO critério; na dúvida, compare com aquele diff.

## Converter (os 4 grupos aprovados)

1. **Travessão que anuncia lista → dois-pontos.**
   `dependem — a tarefa, as métricas…` → `dependem: a tarefa, as métricas…`
2. **Aposto entre travessões → vírgulas ou parênteses.**
   `O AL — objeto desta tese, formalizado na Seç. X — ataca…` →
   `O AL, objeto desta tese e formalizado na Seç. X, ataca…`
   `desbalanceamento — caso desta tese — o Macro F1…` →
   `desbalanceamento (caso desta tese), o Macro F1…`
3. **Travessão explicativo → ligação explícita** (`, o que significa`, `; é o`,
   `porque`, ponto final + nova frase).
4. **Reordenar quando o travessão separa sujeito e verbo** por uma lista longa:
   sujeito + verbo juntos, lista depois dos dois-pontos.

## Preservar (não tocar)

- Travessão de **contraste real** (`não X — Y`) e o de **separador de rótulo**
  em itens de lista (`\item \textbf{P1 — composição…}`).
- **Negritos definicionais** (primeiro uso de termo técnico), itálicos,
  **citações**, notação matemática, tabelas, figuras e rótulos LaTeX.
- Conteúdo técnico: nenhuma afirmação muda de sentido; nenhum número é tocado.

## Também nesta rodada

- Unificar tipografia: `---` e `--` usados como travessão viram `—`
  (consistência); intervalos numéricos seguem com `--`.
- Quebrar **fórmula enumerativa repetida** (`Três leituras.` / `Dois achados.`)
  fundindo na frase anterior — no máximo uma ocorrência por capítulo.
- Não introduzir travessão novo em lugar nenhum.

## Como entregar

Branch `humanize/capN`, um commit por seção ou lote temático, e uma mensagem
de conclusão ao `principal` com: nº de travessões antes/depois, quantas
conversões por grupo, e 3 exemplos de antes/depois representativos. O
principal consolida e leva ao gate do autor — nunca peça gate direto.


## Regra de compilação (obrigatória, 2026-08-17)

Em TÍTULOS de \chapter/\section/\subsection e em \caption, o travessão
permanece como `---` (ligadura ASCII do TeX), NUNCA como o caractere Unicode
`—`. Motivo comprovado: a classe da UFPR maiusculiza títulos no sumário, o que
parte o caractere multibyte e grava U+0080 no .toc — o PDF inteiro deixa de
compilar (6 builds vermelhos em 2026-08-17, causa raiz na unificação
tipográfica que converteu um título). No corpo do texto a unificação `---`→`—`
segue valendo; a exceção é exclusiva de títulos e captions.


## Régua de estrangeirismos (aprovada pelo autor, 2026-08-17)

Termo estrangeiro **corrente na área** não se traduz: fica em itálico, sem
glosa (\textit{tweets}, \textit{embeddings}, \textit{bag-of-words},
\textit{cold start}, \textit{prompt}). Glosa-se, na primeira ocorrência, só
o que a banca pode estranhar ou o que tem palavra portuguesa consagrada —
\textit{stopwords} (palavras funcionais de alta frequência),
\textit{stemming} (redução ao radical), \textit{missed cluster effect}
(efeito de agrupamento não coberto), e "survey" quando cabe "revisão".
Siglas seguem a regra do princípio I: expandidas na primeira ocorrência e na
lista de siglas, inclusive as de método (TF--IDF, SVM, KNN, QBC, ECOICOP).

## Exceção registrada: travessão em \caption (aprovada pelo autor, 2026-08-17)

A regra "título usa `---`, nunca `—`" vale para \chapter/\section/
\subsection, cuja maiusculização no sumário parte o caractere multibyte e
quebra o PDF. **\caption fica de fora**: as listas de figuras e tabelas não
maiusculizam, e os builds com legendas contendo `—` compilam verdes (o
histórico de 2026-08-17 comprova). Consequência operacional: o
`check-travessao-titulo.py` trata legenda como AVISO, nunca como reprovação —
DoD de fatia não pode ser bloqueado por ela.

## Metadiscurso: sóbrio sim, encenado não (regra do autor, 2026-08-24)

Frases sobre o próprio texto são permitidas apenas na forma sóbria: sujeito
explícito (esta seção, o capítulo, a tese) + verbo descritivo (apresenta,
define, descreve, registra, discute, completa). É vetado o **metadiscurso
encenado**, em três formas:

1. **Drama de falta ou necessidade**: "falta a última peça", "não cabe na
   tabela e precisa ser dita", "é preciso dizer".
2. **Apelo ao leitor**: "quem quiser", "note-se", "vale lembrar/mapear/a
   pena", "não custa dizer", "convém fixá-las desde já".
3. **Palco e suspense**: "como veremos", "chegou a hora de", "a história
   continua".

Teste operacional, nesta ordem: (a) a frase sai sem perda de conteúdo
técnico? Então sai. (b) Ela anuncia conteúdo? Então vira "Esta seção
<verbo descritivo> <conteúdo>". Verificador executável:
`python3 scripts/checa-metadiscurso.py <arquivos.tex>` (saída vazia = passa).

## O passe é leitura, não script (regra do autor, 2026-08-25)

Ordem do autor: *"passe o humanize e a avaliação destes metadiscurso, mas
lendo, não passando script. Este será o padrão."*

`scripts/checa-metadiscurso.py` é **piso, não passe**. Ele só encontra frases
fixas; tudo o que a regra proíbe de fato — encenação, registro, personificação,
conclusão genérica, staccato — muda de roupa a cada texto e só aparece na
leitura. Quem entrega um passe declara o que **leu**, não o que o script disse.

Consequências operacionais:

1. Relatar "o checker passou" nunca é relatar um passe. O episódio que originou
   esta regra: o Cap.2 foi declarado limpo de metadiscurso com base no exit 0, e
   a releitura seguinte achou sete casos, dois deles variações de padrões que o
   próprio checker já perseguia com outro verbo.
2. Todo caso novo encontrado na leitura vira padrão do checker **depois**,
   medido nos arquivos da tese com zero falso positivo. O script cresce por
   trás da leitura, nunca à frente dela.
3. Vale para os dois passes, humanize e metadiscurso, e vale para texto de
   qualquer origem: meu, dos agentes ou do autor.
