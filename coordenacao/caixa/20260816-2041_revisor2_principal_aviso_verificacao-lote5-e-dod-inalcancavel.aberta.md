---
de: revisor2
para: principal
tipo: aviso
acao_esperada: ajustar o DoD do lote 5 (hoje inalcançável como está escrito) e decidir sobre a única relação pendurada que sobrou; aceito a divisão proposta pelo revisor1
referencia: tarefa 20260816-2032 (lote 5) · claim do revisor1 20260816-2033 · branch bibfix/lotes @ 216461b
criada_em: 2026-08-16T20:41:35Z
---
DIVISÃO DO LOTE 5: aceito a proposta do revisor1. Ele fica com o arquivo de
referências (tem o lock); eu fico com a verificação cruzada do que ele fizer,
que é o §6 do protocolo — quem executa não verifica. Não toquei no bib.

PRIMEIRA PASSADA DE VERIFICAÇÃO (já feita, sobre o estado atual da branch):
varri TODAS as relações entre fichamentos e o arquivo de referências, não só
as da minha rodada. Sobrou UMA pendurada em todo o repositório:

  fichamentos/Bayer2024ActiveLLM.md aponta para a chave "Yuan2020ALPS", que
  não existe. A obra existe e está no arquivo sob outra chave: "Yuan2020"
  (Yuan, Lin e Boyd-Graber, EMNLP 2020 — é o artigo que introduz o ALPS).
  O mesmo fichamento declara um PDF que não está no repositório.

IMPORTANTE: isso NÃO é regressão do bib-fix. Conferi contra a main: a chave
"Yuan2020ALPS" nunca existiu lá. É dívida antiga, do lote dos fichamentos
legados que reportei em 20260816-1809. Não corrigi porque o arquivo não é da
minha rodada e não me foi atribuído — mas o conserto é de uma linha, e faço
assim que você mandar.

PROBLEMA NO DoD DO LOTE 5 (é o que precisa da sua decisão): o critério diz
"os dois checadores em exit 0". O checador de fichamentos NUNCA vai dar exit 0
hoje, porque os 140 fichamentos legados acumulam 342 entidades fora do
vocabulário controlado — dívida antiga, anterior a todo este ciclo. Do jeito
que está escrito, o lote 5 não tem como fechar.

Sugestão: escrever o DoD como "o checador passa nas chaves tocadas pelo lote e
não introduz nenhuma relação pendurada nova" — que é verificável, é o que
importa para este lote, e não exige limpar uma dívida de meses. A dívida de
vocabulário segue como item separado, para o autor decidir se entra no plano.
