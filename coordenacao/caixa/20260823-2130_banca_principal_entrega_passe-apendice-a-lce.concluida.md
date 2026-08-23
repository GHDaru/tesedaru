---
de: banca
para: principal
tipo: tarefa
acao_esperada: integrar na main, EM BLOCO, as três peças pendentes desta branch — Apêndice B (entrega 2100), Apêndice A (esta) e as correções 12pt dos dois esquemas — validando com a compilação completa (DoD IX)
referencia: a1-lce/texto.tex + esq-lce.tex · branch banca/esquemas-tikz-metodo · ordem do autor (2026-08-23)
criada_em: 2026-08-23T21:30:00Z
---
Conclusão do passe no Apêndice A (claim 2110; ordem do autor: "faça o mesmo
para o apêndice A"). Ele já recebeu as 2 páginas renderizadas.

O que mudou em a1-lce/texto.tex (forma e didática; conteúdo técnico
intacto — equação, propriedades e relação com a ALC dizem o mesmo):
1. Título com o estrangeirismo em itálico (via texorpdfstring).
2. A Definição abre dizendo para que a LCE serve (escalar único para
   comparar e ordenar estratégias) antes do "Seja uma execução...".
3. "MESMO classificador" (caixa alta) → \emph{mesmo}.
4. As 4 propriedades saíram do parágrafo "(i)...(iv)" para lista nomeada
   (Imagem; Invariância de escala — com a justificativa de uma linha;
   Comparabilidade entre tetos; Dependência do intervalo).
5. Autocontenção: o símbolo T (notação do Cap. 3) saiu da Definição.
6. Legenda da figura sem a fórmula repetida (virou prosa; remove
   redundância e um overfull).
7. esq-lce: caixa da fórmula 66mm (o mbox mede ~64,7mm em corpo 12 — o
   overfull interno acusou o valor exato).

MEDIDA IMPORTANTE para suas integrações: o textwidth real do ppginf é
16cm (a4, 2+2cm + lombada 1cm) — meus invólucros de prévia agora usam
isso. Apêndices A e B compilam aqui com 0 erros e 0 overfull em corpo 12.
A compilação completa da tese continua sendo o seu teste de integração.
