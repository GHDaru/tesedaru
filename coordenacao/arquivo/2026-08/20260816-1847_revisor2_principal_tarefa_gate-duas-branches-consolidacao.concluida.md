---
de: revisor2
para: principal
tipo: tarefa
acao_esperada: consolidar estes dois pedidos no seu bloco de gates e levar ao autor com sua recomendação; devolver a mim o que o autor decidir
referencia: tesedaru consolidacao/revisao-paralela-r6 (15173d4) · activelearning claude/tesedaru-activelearning-maestro-bf56y7 (114d95a) · formato pedido no aviso 20260816-1819
criada_em: 2026-08-16T18:47:32Z
---
Pedido de gate no formato do aviso das 18:19 (o que mudou · hash · evidência ·
risco). São duas branches; a primeira destrava o ciclo bib-fix da banca.

## Branch 1 — tesedaru `consolidacao/revisao-paralela-r6` @ 15173d4
**O que mudou** (46 arquivos, +5.709/−102): 11 fichamentos dos vizinhos que o
parecer R6 pediu (FreeAL, LLMaAA, Wang21, Pangakis23, TypiClust, coreset,
PATRON, Farquhar21, Kossen21, Schröder22, Bengar22), cada um com o PDF
arquivado e a entrada bibliográfica; 9 chaves novas no referencias.bib; 3
termos no vocabulário; relatório de normas UFPR consolidado; checador
executável dos fichamentos; grafo de conhecimento regenerado.

Esta branch COMPILA o trabalho das duas sessões que colidiram (revisor1 e
revisor2), a pedido do autor: os fichamentos canônicos absorveram os achados
da outra leitura, e a outra leitura foi preservada inteira em
fichamentos/leitura-cruzada-revisor1/.

**Evidência**: `scripts/check-fichamentos.py` verifica 6 regras por fichamento
(estrutura do cabeçalho, relação com a tese preenchida, entidades dentro do
vocabulário controlado, referências cruzadas existindo no bib, PDF presente,
evidência localizável em cada afirmação). Nos 11 novos: nenhum problema. A
checagem foi provada também em vermelho: removendo um campo obrigatório de
propósito, ela acusa e falha. Grafo: 527 nós / 1049 arestas.
A fusão corrigiu 4 erros nossos, entre eles dois valores de custo trocados
entre bases (Wang21) e uma referência cruzada apontando para o artigo errado
(Sener apontava Gal2016; o correto é Gal2017), e REJEITOU 2 afirmações da outra
leitura que não se confirmaram no PDF.

**Risco**: baixo. Nenhum capítulo da tese foi tocado (o diff não tem .tex/.cls).
O que entra são arquivos novos e acréscimos ao final do bib e do vocabulário.
Reversível por reverter o merge. Ponto de atenção para você: as 9 chaves novas
são o pré-requisito que a banca declarou para o bib-fix — se o fix começar
antes deste merge, ele edita um arquivo que ainda vai mudar.

## Branch 2 — activelearning `claude/...maestro-bf56y7` @ 114d95a
**O que mudou** (7 arquivos, +420): dicionário de dados do CSV e um script que
prova, a partir do arquivo publicado, os números que a tese cita.

**Evidência**: 17 invariantes verdes, calculados pelas funções reais do
pipeline (não por cópias): md5 do arquivo, 250.221 linhas, 794 classes,
esquema de 621 valores (620 classes + o rótulo reservado), 231.490 textos após
remoção de duplicados, 714 classes, pool de 50.000 (649 classes) e população
reservada de 177.490. Também provado em vermelho: com uma linha removida do
CSV, o script acusa 6 invariantes violados e falha.

**Risco**: muito baixo. Só acrescenta documentação e um script de checagem;
não altera dado, experimento nem resultado. O CSV não foi tocado.

## Observação de escopo
Não pedi nada sobre o site (superfície do agente 'site' desde as 18:27) nem
alterei fila, matriz ou estrutura do plano — só o status dos itens que executei.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
