---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: unificar a tipografia dentro do fecho do Cap. 6 (só os traços; nenhuma palavra muda) e avisar o principal ao terminar; a branch fica em gate junto com humanize/cap5 e cap6
referencia: sua conclusão 20260816-1953 · decisão do autor 2026-08-16 · docs/criterio-humanizacao.md
criada_em: 2026-08-16T20:32:39Z
---
DECISÃO DO AUTOR sobre o único ponto que você deixou em aberto: **pode
unificar a tipografia do fecho do Cap. 6**.

Limite exato: apenas a forma dos traços (--- e -- usados como travessão viram
—, mantendo -- para intervalos numéricos). NENHUMA palavra do fecho muda: a
tríade ("começar bem, perguntar bem, pagar bem") e o aforismo final ficam
como estão, por decisão do autor já registrada; a reavaliação deles fica em
aberto para a leitura final (R7).

Também da conta C: a sua correção de relação (Settles2010 -> Settles2009 no
fichamento Farquhar2021Bias) NÃO vai para a main sozinha — a branch
fix/relacao-settles-farquhar sai de bibfix/lotes e arrastaria todo o bib-fix,
que a banca reprovou por cobertura. Incorpore esse commit à própria
bibfix/lotes; ele entra na main junto com o bib-fix corrigido.

## Resultado (revisor2, 2026-08-16)

AS DUAS PARTES JÁ ESTAVAM FEITAS. Verifiquei em vez de refazer, e não inventei
commit para "mostrar serviço".

1. TIPOGRAFIA DO FECHO — já unificada na branch humanize/cap6 (@92dd951), que
   está no seu bloco de gates. Evidência: na seção Conclusão do capítulo há
   exatamente um travessão (—) e um "--", que é o intervalo numérico 78--83%,
   justamente o caso que a sua instrução manda preservar. Os 5 hífens simples
   restantes são legítimos: um rótulo interno, a sigla DRI-SL, as palavras
   "pré-registrado" e "tornando-se" e o código de experimento E0-P. Não há
   nenhum "---" no arquivo e nenhum hífen solto fazendo papel de travessão.
   Os dois "---" que ainda existem na main (linhas 63 e 199) são exatamente os
   que essa branch já converteu — um virou travessão, o outro virou dois-pontos
   durante a humanização. Ou seja: nada a commitar; o ponto se resolve quando
   humanize/cap6 passar no gate.

2. COMMIT DO SETTLES — já incorporado à bibfix/lotes por outro caminho: o
   merge 216461b (fix/referencias-penduradas-lote2) já contém a repontuação
   Settles2010 -> Settles2009. Confirmei no arquivo e rodando o checador: os 11
   fichamentos da rodada passam, exit 0. A branch fix/relacao-settles-farquhar
   ficou redundante — pode apagar.
