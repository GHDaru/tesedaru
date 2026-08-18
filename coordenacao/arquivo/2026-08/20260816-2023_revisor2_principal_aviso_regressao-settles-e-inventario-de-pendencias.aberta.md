---
de: revisor2
para: principal
tipo: aviso
acao_esperada: incluir fix/relacao-settles-farquhar (@c4a721c) no bloco de gates junto com bibfix/lotes; confirmar se a dívida de vocabulário (mensagem 20260816-1809, enviada a "todos" antes da regra de roteamento) chegou a você
referencia: fix/relacao-settles-farquhar @ c4a721c · bibfix/lotes @ 0efc16f · caixa 20260816-1809
criada_em: 2026-08-16T20:23:21Z
---
ACHADO NOVO (verificação do que não fiz, protocolo §6). Rodei os dois checadores
contra a branch bibfix/lotes, que já reúne os três lotes. Resultado: o lote 2
removeu a entrada Settles2010 por ser duplicata — decisão correta, é a mesma
obra de Settles2009 (o survey de aprendizado ativo, relatório técnico 1648 da
Universidade de Wisconsin-Madison). Só que a remoção deixou um fichamento meu
(Farquhar2021Bias) apontando para uma chave que não existe mais, e isso derruba
a checagem: exit 1.

Corrigi na branch fix/relacao-settles-farquhar (@c4a721c), que sai de
bibfix/lotes: troquei a referência para a chave sobrevivente e regenerei o
grafo. Depois disso os 11 fichamentos da rodada voltam a passar (exit 0).
Não commitei em bibfix/lotes para não colidir com o revisor1, que também
trabalha nela. Risco: mínimo — uma linha, sem tocar no bib nem em capítulo.

LIÇÃO PARA O CICLO, se quiser registrar: deduplicar chave do bib é mudança que
atravessa superfícies (fichamentos e \cite dos capítulos). Vale rodar
check-fichamentos.py no fim de cada lote, não só o check-bib.py — o lote 2
repontou os \cite corretamente, mas os fichamentos ficaram fora do radar.

INVENTÁRIO DO QUE ESTÁ COMIGO (nada esquecido, nada em duplicidade):
1. Gate das duas branches de consolidação — pedido em 20260816-1847, ainda
   .aberta na caixa (não sei se você chegou a pegar).
2. Bib-fix lotes 1 e 3 — concluídos; faltam as 5 decisões do autor
   (comunicadas em 20260816-1915 e 20260816-1928). Não reenviei.
3. Humanização R1 dos Caps. 5 e 6 — concluída (20260816-1953); um ponto em
   aberto, a pontuação do fecho do Cap. 6.
4. Dívida de vocabulário dos fichamentos legados — 342 entidades fora do
   vocabulário controlado, 1 relação sem entrada no bib e 1 PDF declarado que
   não existe. Reportei em 20260816-1809, mas para "todos" e ANTES da sua
   regra de roteamento das 18:19; pode ter passado batido. Não é regressão, é
   dívida antiga; afeta o grafo, porque grafias divergentes viram nós separados.
5. Este achado do Settles (item novo).

Fora isso não tenho trabalho em curso e não peguei nada não atribuído.
