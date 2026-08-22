---
de: principal
para: banca
tipo: tarefa
acao_esperada: UMA passada coerente (substitui a 0930, que sozinha pioraria o texto): (1) trocar as 12 marcas PROVISORIO pelos valores da varredura homogênea confirmada; (2) reescrever as DUAS afirmações que mudaram, em TODAS as superfícies; (3) refazer resumo/abstract removendo a limitação de "semente única" JUNTO com o conserto da afirmação (b). Branch única, cruzada do revisor2, gate do autor. NÃO tocar defesa/artigo (autor adiou).
referencia: cruzada do revisor2 20260822-0638 (números confirmados, activelearning@4e33c9a) e 0930 (o risco de executar a antiga sozinha) · 12 marcas PROVISORIO · dec-piso-f1 resolvida pelos dados
criada_em: 2026-08-22T10:30:00Z
---

A varredura homogênea (regeração dos 25 braços) foi CONFIRMADA por cruzada
independente do revisor2 nos 27 braços. Consequências, todas numa passada:

# 1. Troca das 12 marcas PROVISORIO (valores confirmados)
Critério subiu (D subiu): acurácia 0,839→**0,843**; Macro F1 0,428→**0,436**.
Valores novos por braço estão no aviso 0638 (tabela tab:e3p-sweep) — use-os
verbatim. Cap.6 l.56: A 0,711→**0,705**. Confira cada marca contra a tabela
do 0638; o revisor2 tem os 27 artefatos.

# 2. Duas afirmações que MUDARAM (reescrever, não remendar)
(a) **Piso e teto**: some "35 mil, fração acima do teto" e o argumento "o teto
   não acomoda o melhor braço". AGORA: o critério de F1 cruza em **30 mil
   (E30), dentro do teto de 34.724, pelas DUAS leituras** (média 0,455 e as
   três sementes, menor 0,4443). A bifurcação média×3-sementes DEIXA DE
   EXISTIR — não a mencione. Piso de acurácia continua **20 mil, 3/3**.
   Isto MELHORA a tese: o piso robusto agora cabe no teto.
(b) **E35 vs régua**: a afirmação "supera nas TRÊS sementes, McNemar p<10⁻⁷"
   caiu. Verdade nova: supera **na média das três** (0,889×0,887 acc;
   0,463×0,459 F1); por semente é **2 de 3** — a semente 7 INVERTE em Macro F1
   (−0,0050, IC excluindo zero) e empata em acurácia (p=0,67); p<10⁻⁷ só na
   semente 42. Escreva como afirmação de MÉDIA, com a ressalva de que não é
   unânime. Não esconda a inversão da semente 7.

# 3. As CINCO superfícies da afirmação (b) — nenhuma pode sobrar
Cap.5 (leitura iii), Cap.6 (2×), resumo, abstract. [defesa é a 6ª mas o autor
adiou — NÃO tocar.] O resumo/abstract são espelhos PT/EN: conserte os dois.

# 4. resumo/abstract: os dois consertos JUNTOS
Remover "semente única / single seed" (hoje falso: são 3) E corrigir a
afirmação (b) na mesma passada — tirar a ressalva mantendo a alegação antiga
produziria um resumo PIOR (revisor2, 0930).

# 5. Um item a conferir com quem rodou (não bloqueia)
Resumo diz "classificador leve treinado com 250 mil rótulos"; o maior ponto
medido é 200.000. Provável referência à base crua (250.221), não ao treino.
Uma palavra resolve — confirme antes de fixar.
