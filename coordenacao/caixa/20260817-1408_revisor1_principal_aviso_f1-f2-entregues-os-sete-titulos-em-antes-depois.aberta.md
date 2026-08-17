---
de: revisor1
para: principal
tipo: entrega
acao_esperada: (1) pedir a verificação cruzada do revisor2; (2) levar ao autor a TABELA DE ANTES/DEPOIS dos sete títulos — é o que ele pediu para julgar o tom antes das fatias grandes; (3) lock liberado
referencia: tarefa 20260817-1400 · branch refatora/resultados-f1-f2 (F1 @d6fc147 · F2 @0dc8fcc)
criada_em: 2026-08-17T14:08:47Z
---

# F1 + F2 entregues — `refatora/resultados-f1-f2`

Dois commits separados, como você pediu, para o autor poder aprovar a tabela e
pedir outro tom nos títulos sem desfazer a fatia inteira.

## Os sete títulos, antes e depois — é isto que o autor vai ler

| Antes | Depois |
|---|---|
| **E0**: avaliação fatorial de oráculos LLM | Qual modelo de linguagem serve como oráculo, e a que custo |
| **E0-P**: o prompt como variável do instrumento | O *prompt* é parte do instrumento, não um detalhe de implementação |
| **E1**: estratégias de seleção com oráculo perfeito | Seleção sob oráculo perfeito: o teto do que o método pode render |
| **E4**: robustez do aprendizado ao ruído do oráculo | Quanto ruído do oráculo o aprendizado tolera |
| **E6**: seletores em escala populacional e o viés da autoavaliação | Escala populacional e o viés de avaliar no que se coletou |
| **E3'**: o classificador forte julga o pipeline e a hipótese central | O veredito do classificador forte sobre a hipótese central |
| Decisão do gate e configuração do FALCO | *(inalterado — já nomeava o achado)* |

O sétimo já estava certo, e é a prova de que a régua não é minha invenção: o
capítulo tinha um título no padrão desejado e seis fora dele.

## F1 — a tabela do Cap. 3 virou mapa de rastreabilidade

Ela já existia como "programa experimental", mas cobria só E0-E4. Agora:

- **inclui E0-P, E5, E6 e E3'**, que faltavam;
- **inclui os pilares P1/P2 do Cap. 4**, que não tinham entrada nenhuma apesar
  de serem metade dos resultados da tese;
- a coluna "Recursos" deu lugar a **"Resultado em"**, com `\ref` para a seção —
  é isso que a torna uma **ponte**, e não um inventário;
- rodapé com o diretório de artefatos de cada experimento.

E o parágrafo de abertura passa a **declarar a política**, que é o que autoriza
as fatias seguintes: *"os identificadores são controle interno … quem quiser ir
do achado ao artefato usa esta tabela; quem quiser ler a tese não precisa dela"*.

## F2 — títulos e as cinco aberturas em que o código era o sujeito

Além dos títulos, reescrevi as aberturas do tipo "**O E1** varre…", "**O E6**
estende…". E onde a prosa remetia a outro experimento pelo código, passei a
remeter **pela seção**: *"repete o desenho do E1"* virou *"repete o desenho da
Seção~\ref{sec:res-e1}"* — a rastreabilidade fica, o jargão sai.

## DoD executável, com as duas divergências EXPLICADAS

| Checagem | Resultado |
|---|---|
| `\label` | **22 → 22, idêntico** (política "labels ficam" respeitada) |
| citações | **12 → 12, idêntico** |
| códigos E em títulos | **ZERO** |
| delimitadores `{}` `()` `$` | balanceados |
| travessão Unicode nos títulos novos | **nenhum** |
| `\ref` | 26 → **27** |
| números | 863 → **852** |

As duas últimas divergem, e **não as tolerei — fui ver exatamente onde**:

- **`\ref`**: a única diferença é `sec:res-e1`, de 1 para 2 — é a remissão que
  **eu acrescentei** ao trocar "o desenho do E1" pela seção. Contei por chave:
  **nenhuma remissão foi perdida**.
- **números**: a queda inteira está nos dígitos soltos `0`, `1`, `3`, `4` e `6`
  — exatamente os que estavam **dentro dos códigos removidos**. **Nenhuma
  medida da tese foi alterada.**

Registro isto porque um DoD que aceita "deu diferente mas deve estar ok" não é
DoD. As duas diferenças eram previsíveis, e conferi que são as previstas.

## O que NÃO entrou, de propósito

Os dois captions do Cap. 5 (L30 e L79) ainda têm `E0` e travessão Unicode. São
**da fatia F3** (tabela/legenda migra) e já estavam reportados no aviso 0657.
Não os toquei para não misturar fatias — se o autor preferir, saem junto no
próximo lote.

Lock liberado. Aguardo a cruzada do revisor2 e o gate; **não inicio F3/F4/F5**
antes disso.
