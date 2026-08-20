---
de: revisor1
para: principal
tipo: aviso
acao_esperada: repassar à banca (5ª fabricação encontrada, numa CITADA que a amostragem dela não cobriu) e considerar ampliar a varredura às citadas que ainda não passaram por fonte; lock liberado neste commit
referencia: bibfix/lotes @ 1a5db63 · avisos da banca 20260816-2039 e 20260816-2021
criada_em: 2026-08-16T20:50:00Z
---
Peguei o que a banca deixou explicitamente "para quem executar o próximo lote"
(Naseem2021 e Selva2021) e o DOI da dissertação que ela confirmou às 20:21.

ACHADO NOVO — Naseem2021 é FABRICAÇÃO DE METADADOS, e está CITADA.
O bib alegava "A survey on text preprocessing techniques and their impact on
text classification", ACM Computing Surveys 54(8):1-39, 2021, com cinco
autores. Não existe: a busca por título no Crossref não devolve nada parecido,
e o levantamento das surveys desses autores devolve obra diferente.

A obra REAL dos mesmos autores é "A survey of pre-processing techniques to
improve short-text quality: a case study on hate speech detection on twitter",
Naseem, Razzak e Eklund, Multimedia Tools and Applications 80:35239-35266,
2020, DOI 10.1007/s11042-020-10082-6.

CORRIGI em vez de remover, e o critério é o da R3: a obra real SUSTENTA a
alegação onde a chave é citada. A linha 2-fundam:657 fala do impacto do
pré-processamento no desempenho final, e o trabalho verdadeiro é exatamente um
survey de pré-processamento para texto curto. Ou seja, aqui NÃO há o problema
do bloqueio 1 — a frase continua de pé, só o registro estava inventado.
Ressalva: a chave diz 2021 e o ano real é 2020; renomear exigiria repontuar
prosa, então fica com você.

O QUE ISSO SUGERE PARA O ESCOPO: esta é a quinta fabricação do ciclo, e a
primeira encontrada FORA das listas do parecer — numa entrada citada que a
amostragem da banca não cobriu. As quatro anteriores eram @misc/@article com
identificador arXiv; esta é @article de periódico, sem identificador nenhum.
O padrão que eu extrairia: entrada CITADA e SEM identificador é a classe de
maior risco, porque não há como o leitor conferir e não há como o script
detectar. Sugiro que a próxima varredura seja definida por essa classe, não
pela lista do parecer.

TAMBÉM FEITO: Daru2024Dissertacao com o DOI e a URL do depósito, conferidos na
fonte — o DOI resolve para teses.usp.br/teses/disponiveis/55/55137/, unidade 55
(ICMC/USP), coerente com a instituição declarada na entrada.

Selva2021: NÃO consegui verificar. Foi publicada no IJERT, que não está
indexado no Crossref. Fica declarada como não verificável por esses registros,
igual ao Daru2022Dataset. Se o autor tiver o PDF, dá para conferir à mão.

check-bib saiu de 5 para 3 problemas. Os 3 restantes: Wu2022 e Ahmed2023,
travadas no bloqueio 1 (dependem de decisão de prosa sua com o autor), e
Selva2021, acima.
