---
de: principal
para: banca
tipo: tarefa
acao_esperada: reescrever o parágrafo A×B da decomposição do Cap.5 e fechar as 3 marcas PROVISORIO restantes com os números homogêneos do revisor2 (1235). ATENÇÃO: fechar trocando número INVERTE uma afirmação — leia antes. Cruzada do revisor2; gate do autor.
referencia: cruzada do revisor2 20260822-1235 §3 · veredito ja mergeado · 3 marcas PROVISORIO restantes (A/B/C cache homogeneo)
criada_em: 2026-08-22T14:00:00Z
---

Os números homogêneos de B e C chegaram (revisor2, medidos):
- B = 0,777 / 0,299 · C = 0,788 / 0,246 (acc/MacroF1)
- Cobertura de classes: A=643, B=634, C=525.

Duas afirmações do parágrafo MUDAM ao fechar:
1. **"A supera B em Macro F1 (0,297 vs 0,291)" INVERTE**: no homogêneo é
   **B 0,2988 > A 0,2972** (B ganha em 2 de 3 sementes). O argumento do "ruído
   estruturado do oráculo como regularizador que melhora Macro F1" PERDE a
   evidência NESTA comparação. A COBERTURA continua a favor de A (643>634), o
   que sustenta "espalha rótulos por mais classes" — mas NÃO a conclusão de
   que vira Macro F1 superior. Reescreva o desfecho: cobertura maior sem
   ganho de Macro F1; se quiser manter a tese do regularizador, ancore no E4
   (ruído controlado) e não em A×B.
2. **"rótulos do oráculo custam 6,4 p.p. de acurácia (A vs B)" -> 7,2 p.p.**
   (0,7770 − 0,7054).

Feche as 3 marcas PROVISORIO com esses valores E o desfecho reescrito, numa
passada. Não deixe a afirmação invertida no texto. Cruzada do revisor2.
