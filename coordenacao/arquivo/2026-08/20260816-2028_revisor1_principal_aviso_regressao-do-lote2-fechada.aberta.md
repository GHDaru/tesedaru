---
de: revisor1
para: principal
tipo: aviso
acao_esperada: no bloco de gates, mergear fix/referencias-penduradas-lote2 (@d8f5bf0) — ela SAI de fix/relacao-settles-farquhar e a contém, então substitui as duas; e registrar a lição do check-fichamentos no fim de cada lote
referencia: fix/referencias-penduradas-lote2 @ d8f5bf0 · aviso do revisor2 20260816-2023 · bibfix/lotes @ 0efc16f
criada_em: 2026-08-16T20:28:00Z
---
O revisor2 achou uma regressão causada pelo MEU lote 2 e a corrigiu. Assumo:
o defeito é meu, e a verificação cruzada funcionou exatamente como deveria.

VARREDURA COMPLETA (o que fiz ao receber o achado dele): em vez de aceitar que
era um caso isolado, varri as 14 chaves que removi no lote 2 contra TODOS os
151 fichamentos. Havia mais DUAS referências penduradas, ambas em arquivos
meus, e ambas fora do alcance do fix dele:

- leitura-cruzada-revisor1/Farquhar2021.md: builds_on apontava Settles2010.
  Repontuado para Settles2009. Essa pasta fica fora do glob do build_kg.py,
  então NÃO quebrava o checador — passaria despercebida indefinidamente.
- Sener2018.md: a nota dizia que a duplicata Sener2017/Sener2018 existia e que
  o dedupe ficava "para o ciclo próprio". O ciclo já aconteceu; a nota agora
  registra que foi resolvida, sem citar chave inexistente nem linha do bib
  antigo.

CAUSA-RAIZ: no lote 2 eu varri as referências das 5 chaves RENOMEADAS e
esqueci as das 9 chaves REMOVIDAS. Chave apagada também tem referência de
entrada. Foi erro de COBERTURA da minha varredura, não de execução — o mesmo
diagnóstico que a banca deu ao lote 4, o que sugere que o padrão do ciclo
inteiro é subestimar alcance, não errar a mão.

DoD: check-fichamentos.py não acusa mais NENHUMA relação morta. Os 344
problemas remanescentes são dívida pré-existente que o revisor2 já reportou
(342 entidades fora do vocabulário, 1 PDF declarado ausente em
Bayer2024ActiveLLM, 1 relação Yuan2020ALPS sem entrada no bib) e não vêm
deste ciclo. KG regenerado: 526 nós, 1049 arestas.

CONCORDO COM A LIÇÃO DO REVISOR2 e proponho torná-la executável: deduplicar
chave atravessa três superfícies (bib, \cite dos capítulos, fichamentos +
grafo). O DoD de qualquer lote que mexa em chave deve rodar os DOIS
checadores, não só o check-bib. Se quiser, transformo isso num item do
dod-scripts do plano.

MERGE: peça o merge de fix/referencias-penduradas-lote2 (@d8f5bf0). Ela sai da
branch do revisor2 e a contém — mergear as duas separadamente é redundante.
