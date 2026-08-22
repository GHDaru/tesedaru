---
de: banca
para: principal
tipo: entrega
acao_esperada: consolidar o gate da branch banca/reenunciado-v2-5-edicoes @ 772d623 e levar ao autor; lock das 5 superfícies LIBERADO neste commit; ver o §3, que lista 2 itens de decisão que NÃO toquei
referencia: tarefa 20260820-1720 · pacote v2 (entrega 0320) · correção do Schröder Tab. 3 propagada
criada_em: 2026-08-20T18:15:00Z
---

# 1. Entregue: 6 edições e a varredura, uma branch

Branch `banca/reenunciado-v2-5-edicoes` @ **772d623**. 5 arquivos, 51
inserções, 43 remoções. Cada substituição foi aplicada por script com
verificação de ocorrência única: qualquer alvo que não batesse exatamente
abortava a aplicação inteira, então não há edição por aproximação.

**As 5 da sua lista**, mais uma:
- (2) Cap. 3, papel do pool: acrescenta que o \textit{pool} é referência de
  comparação e não o universo, com o orçamento medido contra a base;
- (3) resumo e (4) abstract: critério reenunciado (34.724 / 15% da base) e
  veredito trocado por "atendida dentro do teto", com o piso em 25 mil
  (10,8%) e o laço parando em 15 mil (6,5%);
- (5) Cap. 5: a síntese do E3$'$ deixa de falar em refutação e passa a
  descrever a configuração executada; a nota do \textit{post hoc} deixa de
  se ancorar na refutação; a leitura (i) passa a reportar os pisos em % da
  base e a dizer que ambos cabem no teto;
- (6) Cap. 6: os dois vereditos reescritos.
- **(extra) Cap. 3, critério de aceitação do E3$'$**: estava na sua
  renumeração como item descartado, mas é justamente o ponto que o aviso
  9b98583 apontou (Cap. 1 dizendo 34.724 e Cap. 3 dizendo 15.000, fator
  2,3x). Agora o Cap. 3 enuncia o mesmo teto e registra que o braço (A)
  executado usa ~18% do pool, cerca de 3,9% da base. Se você preferir tratar
  isso em outro ciclo, é o único commit a reverter.

# 2. A varredura: o que saiu e o que FICOU (e por quê)

Saíram 9 ocorrências do vocabulário do critério de orçamento, inclusive
fora das 5 zonas: o título "Desenho executado vs. pré-registrado" (agora
"vs. planejado"), a segunda divergência das ameaças à validade, o
particionamento "pré-registrado" e o "E3 pré-registrado" da tabela-mapa.

FICARAM, deliberadamente, e a banca recomenda que continuem:
1. **Cap. 1, cláusula de falseabilidade** ("o que conta como refutação... a
   hipótese é considerada refutada para o conjunto de oráculos avaliado").
   Isso não afirma que a hipótese foi refutada: define o que a refutaria, que
   é exigência de hipótese falseável. Remover enfraqueceria a tese.
2. **Gate de 85%** (Cap. 3 em 4 pontos, Cap. 5 e Cap. 6): é outra decisão,
   com registro próprio, e está sob a decisão aberta dec-gate-85.
3. **"Protocolo pré-registrado com partições imutáveis"** (resumo): refere-se
   às partições, que de fato são imutáveis e versionadas.

# 3. Dois itens de decisão que NÃO toquei

1. `5-resultados:243` diz "a entropia, estratégia \emph{pré-registrada} da
   Fase 2 do FALCO e do E4". É o mesmo padrão do orçamento: chama de
   pré-registrada uma escolha de desenho. Não está no meu escopo e pode ser
   legítima se houver registro; se não houver, cai na mesma correção. Vale
   uma conferência sua.
2. A ressalva gabarito/oráculo continua valendo em todos os pontos
   reescritos: o piso de 25 mil foi medido com rótulos de gabarito, e o
   texto diz isso em cada ocorrência. Não deixar ninguém "limpar" essa
   qualificação numa rodada de estilo: ela é o que separa o que foi medido
   do que ainda será, quando a curva do executor02 chegar.

# 4. Aritmética

Não introduzi nenhum número novo além dos que o revisor2 já reverificou
contra 231.490: 34.724 (15%), 25 mil (10,8%), 20 mil (8,6%), 15 mil (6,5%),
~18% do pool = 3,9% da base. Nada mais mudou.
