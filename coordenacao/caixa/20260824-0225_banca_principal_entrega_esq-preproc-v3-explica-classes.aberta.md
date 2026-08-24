---
de: banca
para: principal
tipo: tarefa
acao_esperada: gatear com o autor a v3 da figura do pré-processamento (adendo 0143); no gate, checar o espelho figura×prosa dos números do §3.2; a banca NÃO tocou no Cap. 3
referencia: adendo 0143 da tarefa 0138 · esq-preproc-espacos-rotulos.tex (v3) · branch banca/esquemas-tikz-metodo
criada_em: 2026-08-24T02:25:00Z
---
Entrega do adendo 0143: `esq-preproc-espacos-rotulos.tex` refeita como a
EXPLICAÇÃO DAS CLASSES. A figura agora responde, olhando para ela, "por que
621 num experimento e 714 no outro?": duas vias a partir da base corrigida
(linhas cruas com filtro de >=5 -> CategorySchema fechado de 621; filtro
brando de >=2 -> deduplicação -> visão populacional de 714), a "pomada
massageadora" apontada no vão entre as vias, a seta anotada "715 - 1 = 714"
e uma nota-resposta ao pé com as duas convenções de contagem (chave de
texto e o que se conta).

EXCEÇÃO CONTROLADA cumprida: só os números já impressos no §3.2 (250.221,
>=5, 621, 620, >=2, 715, 710, 231.490, 714); nada recomputado. O cabeçalho
do `.tex` documenta a exceção e o dever de espelho: qualquer edição futura
desses números na prosa deve refletir na figura (checagem manual no gate).

Loop de excelência: 4 iterações compiladas nas medidas reais (corpo 12,
textwidth 16 cm); defeitos achados no render e corrigidos (rewraps
intra-palavra "li-nhas"/"tex-tos", colisão da nota da pomada com o
CategorySchema, hífen manual). Final: 0 erros, 0 overfull, prévia
regenerada (`preview-esq-preproc-espacos-rotulos.png`).

LEGENDA PROPOSTA (substitui a da mensagem 0210 para esta figura):
"O pré-processamento e os dois espaços de rótulos, com o caminho das
contagens: da mesma base corrigida e normalizada (250.221 linhas), o filtro
de cinco ou mais instâncias sobre as linhas cruas produz o
\textit{CategorySchema} fechado de 621 categorias (620 frequentes mais a
sentinela), que governa os oráculos; o filtro brando de duas ou mais
instâncias (715 classes em linhas; 710 em textos únicos), seguido da
deduplicação, produz a visão populacional de 231.490 textos únicos com 714
classes presentes. As contagens diferem porque mudam o espaço (fechado com
sentinela ou aberto na cauda) e as convenções de contagem (a chave de texto
e o que se conta: linhas ou textos únicos)."

INSERÇÃO PROPOSTA: inalterada (fim da Seção sec:metodo-dados-preproc).
A figura 1 da 0138 (esq-sequencia-metodologia) segue como entregue na 0210.
