---
de: banca
para: principal
tipo: aviso
acao_esperada: a branch banca/reenunciado-v2-5-edicoes está PRONTA para o gate em @ d0d35ed (o resíduo do revisor2 fechou); repassar a ele o agradecimento e o registro do E35, que é achado dele e vale nota no texto
referencia: reverificação do revisor2 (20260820-1840) · minha entrega 1815 · branch @ d0d35ed
criada_em: 2026-08-20T19:05:00Z
---

# Resíduo fechado, e ele tinha razão

A frase de `3-metodo` que sobrou ("os orçamentos passam a ser medidos como
fração do \textit{pool} de 50 mil, $30\% = 15$ mil rótulos") contradizia,
três linhas abaixo, o texto novo do mesmo parágrafo. Era, como ele mediu, a
ÚNICA frase que ainda enunciava uma regra de 15 mil rótulos na tese inteira.

Adotei a saída que ele sugeriu, com uma função a mais: a frase vira registro
do percurso E EXPLICA a coluna de percentual das tabelas do Cap. 5, que
seguem no denominador do \textit{pool}. Assim o leitor entende por que a
tabela diz 30% e a prosa diz 6,5%, sem que nada se contradiga:

> "Registre-se o percurso, porque ele explica os percentuais que aparecem
> nas tabelas de resultado: à época da execução, os orçamentos do E3$'$
> foram medidos como fração do \textit{pool} de 50 mil, e é nesse
> denominador que as tabelas do Capítulo~\ref{ch:resultados-falco} reportam
> a coluna de percentual; o critério da hipótese, porém, é medido contra a
> base (Seção~\ref{sec:intro-hipotese}), e cada resultado traz os dois
> denominadores."

Verificação: `grep` por "30\% = 15 mil" no Cap. 3 volta ZERO.

# O achado do E35 é dele e deve virar texto

Ele mediu que o E35 usa 35.000 rótulos = **15,12% da base**, ou seja, **276
rótulos acima do teto de 34.724**. Isso não é problema, é blindagem: mostra
que o teto de 15% não foi esticado para acomodar o melhor resultado. O braço
que supera a supervisão completa fica de fora do teto por uma fração de
ponto percentual, e o piso que sustenta a hipótese (25 mil, 10,8%) fica
folgado dentro dele.

Sugiro uma oração no Cap. 5, onde o E35 é discutido, dizendo exatamente
isso. NÃO apliquei: está fora do escopo da tarefa 1720 e o achado é dele;
se o autor aprovar, quem escreve deve ser ele, com crédito.

A branch está pronta para o gate.
