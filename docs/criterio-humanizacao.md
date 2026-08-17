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
