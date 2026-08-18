---
de: banca
para: principal
tipo: tarefa
acao_esperada: incluir a edição aprovada pelo autor no ciclo do t1 (revisor2, que vai humanizar a mesma zona) ou aplicar direto — a frase-alvo está em 2-fundam/texto.tex:109-113; gate em bloco como de costume
referencia: aprovação do autor em conversa com a banca, 2026-08-17 ("Aprovo a sugestão, manda ao principal") · leitura do autor na seção de métricas · princípio VII (sem código de experimento no Cap. 2)
criada_em: 2026-08-17T04:27:48Z
---
Durante a leitura do autor, ele questionou a justificativa da dispensa das
métricas alternativas (acurácia balanceada, MCC, Kappa) — a frase atual afirma
a conclusão sem mostrar a razão mais forte. A banca propôs o reforço abaixo e
o autor APROVOU textualmente.

FRASE ATUAL (2-fundam:109-113):
"...esta tese as dispensa porque o par Macro F1 + acurácia global já separa os
dois fenômenos de interesse (desempenho nas caudas \textit{versus} desempenho
agregado)."

FRASE APROVADA (substituir o trecho final):
"...esta tese as dispensa porque o par Macro F1 + acurácia global já separa os
dois fenômenos de interesse (desempenho nas caudas \textit{versus} desempenho
agregado) — separação que é operacional, não estética: nos experimentos desta
tese as duas métricas chegam a divergir em sinal, e uma métrica única
mascararia precisamente esse contraste (Capítulo~\ref{ch:resultados-falco})."

RACIONAL (para o commit/gate): a razão profunda da dispensa é que os fenômenos
centrais da tese têm sinais OPOSTOS nas duas métricas (E3': seleção piora
acurácia e melhora Macro F1; E6: viés interno subestima acurácia e superestima
Macro F1) — métrica única mascararia os dois achados. A redação aprovada evita
códigos de experimento no Cap. 2 (princípio VII) e remete ao capítulo de
resultados. Sustentação numérica já na main: mcnemar_s42/bootstrap_f1_s42.
