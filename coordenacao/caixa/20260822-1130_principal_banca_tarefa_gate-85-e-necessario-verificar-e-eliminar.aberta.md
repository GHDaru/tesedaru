---
de: principal
para: banca
tipo: tarefa
acao_esperada: (decisão do autor: "verifique se é necessário e já elimine") avaliar se a discussão do gate de 85% ainda é necessária na tese e, se não for, ELIMINAR — com antes/depois. Se for necessária, corrigir a incoerência apontada no parecer. Branch, cruzada do revisor2, gate do autor.
referencia: dec-gate-85 · pareceres R3/R4/R6 · pode estar em 3-metodo, 5-resultados e 6-conclusao
criada_em: 2026-08-22T11:30:00Z
---

O gate de 85% dizia: escolher o oráculo que passa de 85% de acurácia. Nenhum
oráculo atingiu; a justificativa ficou incoerente (diz "um desvio acima" de
89,56% quando na verdade está 4,6 p.p. ABAIXO) e a configuração final foi
derivada sem oráculo cruzar o limiar e sem declarar violação do pré-registro.

O autor decidiu: **verifique se ainda é necessário e, se não, elimine.**
Avalie:
1. O gate ainda cumpre alguma função no argumento, ou virou artefato de um
   critério que os fatos não sustentaram? Com a nova geração de oráculos
   (GLM/DeepSeek) e o eixo do veredito já reescrito, ele pode ter ficado
   órfão.
2. Se for eliminável: remova a menção nas 3 superfícies (3-metodo, 5, 6)
   substituindo pela lógica que de fato governou a escolha de oráculo (razão
   acurácia/custo, fases de custo crescente) — sem deixar buraco lógico.
3. Se NÃO for eliminável: conserte a incoerência numérica e declare
   honestamente que nenhum oráculo cruzou o limiar.
Recomende a saída; o autor decide no gate. Cruzada do revisor2.
