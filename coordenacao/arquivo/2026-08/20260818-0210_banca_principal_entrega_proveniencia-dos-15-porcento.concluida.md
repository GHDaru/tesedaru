---
de: banca
para: principal
tipo: entrega
acao_esperada: (1) levar ao autor o resultado da busca de proveniência — o lastro EXISTE, mas é da LITERATURA, não de pré-registro próprio, e isso muda a redação; (2) enfileirar a correção da ficha Schroder2022Uncertainty (o claim C3 diz "~15%" e a fonte diz 14%); (3) ATENÇÃO à colisão de denominador do §3, que pode inviabilizar o número 15 como enunciado
referencia: tarefa 20260817-0145 (re-enunciar hipótese), item "SUA PRIMEIRA TAREFA É A PROVENIÊNCIA" · redirecionamento do autor à banca, 2026-08-18 ("utilizei números de artigos e do settles para me ancorar")
criada_em: 2026-08-18T02:10:00Z
---

# 1. Onde NÃO está (busca esgotada, resultado negativo declarado)

- **Dissertação de mestrado** (PDF integral, 91 pp.): a única ocorrência de
  15% é a partição canônica 70/15/15 de treino/validação/teste. Nada sobre
  orçamento de rotulagem.
- **Repositório e histórico do git** (`git log -S` em 1-intro e 3-metodo):
  nenhuma versão anterior da tese enunciou 15% como critério.
- **artigos/ e docs/**: os 15% que aparecem são pesos de rubrica de parecer,
  sem relação.

Conclusão parcial: **não há pré-registro próprio dos 15%**. Escrever que o
critério estava pré-registrado seria afirmar registro inexistente.

# 2. Onde ESTÁ: a âncora é da literatura, e é boa (conferida na FONTE)

O autor está certo: os números vêm de artigos e do Settles.

**(a) Settles (2009), §2, Fig. 2(c)** — a ilustração canônica do campo:
> "it avoids requesting labels for redundant or irrelevant instances, and
> achieves accuracy = 0.9 with a mere 30 labeled instances. That is a 67%
> reduction in error compared to 'passive' supervised learning (i.e., random
> sampling), **and less than 10% of the data was labeled**."

**(b) Schröder, Müller, Niekler e Potthast (2022), §4/Tab. 3** — a âncora
moderna, era transformer, que é a faixa em que o 15% cai:
> "all models are close to or even sur-pass the state of the art, **using
> only between 0.4% and 14% of the data**."

**CORREÇÃO DE FICHA (enfileirar, não é minha superfície):** o fichamento
`Schroder2022Uncertainty.md`, claim C3, registra "entre 0,4% e ~15%". A
fonte diz **14%**. É o mesmo padrão do caso Yuan/ALPS de ontem: a ficha
arredondou e a prosa herdaria o arredondamento. Se a tese citar 15% como
sendo de Schröder, a banca abre a página 2197 e lê 14%.

# 3. RECOMENDAÇÃO DE REDAÇÃO (e uma colisão que precisa de decisão)

Com esse lastro, o enunciado honesto e mais forte NÃO é "critério
pré-registrado de 15%", e sim **critério ancorado na literatura**:

> proposta: "O teto de rotulagem adotado como critério, 15% da base, situa-se
> na faixa que a literatura de aprendizado ativo reporta como suficiente
> para alcançar o desempenho da supervisão passiva: menos de 10% dos dados
> na ilustração canônica de \citet{Settles2009} e entre 0,4% e 14% dos dados
> nos benchmarks com transformers de \citet{Schroder2022Uncertainty}. A
> execução desta tese foi mais restritiva que o próprio critério: 15.000
> rótulos, ou 6,5% da base."

Isso converte o ponto fraco (teto enunciado depois) em ponto forte (teto
ancorado e execução conservadora), sem afirmar registro que não existe.

**COLISÃO QUE PRECISA DE DECISÃO DO AUTOR:** o número 15% JÁ é usado na tese
com OUTRO denominador. No resumo: "recuperando 78% do Macro F1 do teto
supervisionado com 15% dos rótulos"; e em `5-resultados:246` ("o orçamento
de 3.000, 15% do...") e `:277` ("com 15% do orçamento de rótulos"). Esses
15% são do POOL/orçamento, não da base. Se o critério da hipótese passar a
ser "15% da base" (34.724 rótulos), a tese terá dois "15%" com significados
distintos, no mesmo documento, a poucas páginas de distância. Saídas:
  (a) manter 15% como critério e reescrever as três ocorrências antigas com
      o denominador explícito em cada uma;
  (b) enunciar o critério em VALOR ABSOLUTO ("34.724 rótulos, 15% da base"),
      o que remove a ambiguidade na primeira leitura;
  (c) escolher outro teto redondo que não colida.
Recomendo (b): o valor absoluto é imune a confusão de denominador e a
percentagem fica como glosa.

Não redigi o pacote de antes/depois ainda: as três saídas acima produzem
textos diferentes, e a escolha é do autor. Com a decisão dele, entrego o
pacote completo (1-intro, 3-metodo, 5-resultados, 6-conclusao) no mesmo
ciclo.
