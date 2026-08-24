# Parecer da banca — painel de 3 especialistas sobre a introdução metodológica do Capítulo 3

**Data**: 2026-08-24 · **Encomenda do autor**: "uma introdução metodológica que
leve o leitor à compreensão do que foi feito", avaliada por um especialista em
escrita acadêmica e mais dois de interesse (storytelling científico e leitor
metodológico de banca), em loop até a excelência.

**Método**: três pareceristas simulados leram o capítulo (`3-metodo/texto.tex`,
919 linhas, main @575e0ca) de forma independente e com lentes distintas; a
banca mediu cada achado verificável contra o texto antes de aceitá-lo; a
proposta resultante passou por verificação em contexto limpo (teste cego de
compreensão com 10 itens + caça a vícios de estilo), foi reprovada na primeira
rodada, corrigida e reaprovada. Divulgação: os três assentos são instâncias do
mesmo modelo com papéis separados; a convergência entre eles corrobora, mas
não constitui três julgamentos estatisticamente independentes.

## 1. Diagnóstico consolidado (o que os três assentos concordam)

O capítulo NÃO é o problema: as transições entre seções são genuinamente
narrativas ("Definido o material...", "Com dados, classificadores e métricas
estabelecidos...", "Resolvido o início do laço...") e a espinha "ordem em que
o custo aparece" é real e estruturante. Os problemas concentram-se na
ABERTURA:

1. **[MAIOR, 3/3 assentos] A mesma visão geral é contada três vezes** em 75
   linhas: parágrafo de abertura (l.4-26), legenda da figura (l.31-36) e
   "visão de conjunto" (l.59-78). A terceira ainda interrompe a Seção 3.1 no
   meio, entre a formalização *pool-based* e o parágrafo de proveniência, com
   a transição falsa "Antes do detalhamento, vale a visão de conjunto" (o
   detalhamento já começou).
2. **[MAIOR, assento leitor; o achado central para a encomenda] O elementar
   está ausente**: no teste cego de 8 perguntas sobre as linhas 1-142, um
   leitor de outra área quantitativa NÃO consegue responder o que se
   classifica, em que língua, com que dados nem com que métrica primária
   (Macro F1 só aparece na l.400; tarefa e base, na l.155-169). A introdução
   explica a LÓGICA da investigação sem dizer O QUE ela faz.
3. **[MAIOR, 3/3] DRI-SL circula fechada** da l.17 até a expansão na l.520,
   violando o princípio I da constituição na sigla mais idiossincrática da
   tese. (Medido: a expansão consta da lista de siglas, idêntica à do §3.6.)
4. **[MAIOR, 2/3] Promessa desmentida pela própria tabela**: a abertura
   promete "quatro pilares, cada qual associado a um experimento identificado
   e reprodutível", mas quatro linhas da Tabela 3.1 têm "---" na coluna Id, a
   relação pilar-experimento é um-para-muitos e a coluna Pilar tem um quinto
   valor ("apoio ao framework", E1/E2) nunca anunciado. (Medido: confirmado.)
5. **[MAIOR, assento escrita] Datação dupla do pré-registro ambígua**
   (l.80-88): "material datado de maio de 2022, na versão de maio de 2023"
   deixa indefinido qual é "esse marco" de que depende o princípio VI.
6. **[MAIOR, assento escrita/storytelling] Parágrafo de abertura monolítico**
   (23 linhas, cinco movimentos, abridor morto "Este capítulo descreve...").
7. Menores convergentes: "arquitetura hexagonal com domínio isolado" na
   abertura é jargão prematuro (a explicação real está na l.892); a ressalva
   E3/extensão (l.96-98) é críptica antes de o leitor saber que houve um
   desenho maior; LLM circula dentro da sigla FALCO antes de ser aberta; a
   remissão à figura é burocrática; os pilares 2 e 3 nunca se numeram nas
   suas seções (o placar se perde); tiques "vale a visão de conjunto" (l.59)
   e "Vale mapear o caminho" (l.442); aposição ambígua "integra as peças,
   partida a frio, ..." (l.75-77); a Seção 3.4 (Métricas) é a única sem frase
   de transição narrativa.

## 2. A proposta (o artefato)

`3-metodo/esquemas-propostos/proposta-introducao-cap3.tex` — substitui as
linhas 4-26 e 40-45 da abertura atual e o parágrafo 59-78 da Seção 3.1
(instruções de recorte nos comentários do próprio arquivo). Desenho:

- **Parágrafo 1**: problema (Cap. 1) + a tarefa concreta (classificar
  descrições curtas de produtos de varejo em português, exemplo real
  `CERV BRAHMA LT 350ML`, centenas de categorias, base de ~250 mil) + a régua
  (Macro F1 na curva de aprendizado; LCE como resumo) + a tensão que organiza
  o capítulo: o custo não chega de uma vez (sem rótulo algum → cada rótulo
  tem preço → tudo sob o mesmo orçamento).
- **Parágrafo 2**: terreno comum (com \ref's) + os quatro pilares na ordem do
  custo, cada um com sua pergunta e remissão, DRI-SL e FALCO abertos na
  primeira ocorrência, LLM aberta ANTES de FALCO + mapa para os capítulos de
  resultados (pilares 1-2 → Cap. 4; pilares 3-4 → Cap. 5).
- **Parágrafo 3**: remissão ATIVA à figura ("cada seta se lê como uma
  dependência"), que permanece onde está com a legenda atual.
- **Parágrafo 4 (fecho)**: validade + reprodutibilidade + contrato de
  rastreabilidade com remissão; "arquitetura hexagonal" sai da abertura.
- **Ajuste acoplado na Seção 3.1**: o parágrafo de visão de conjunto é
  reduzido ao que só ele contém (duas visões dos dados; divisão dos
  classificadores por custo, com BERTimbau glosado) e a cauda que re-lista as
  seções é cortada; a Seção 3.1 recupera o fio formalização → proveniência →
  tabela.

**Verificação executável**: compila com 0 erros e 0 overfull nas medidas
reais (corpo 12, textwidth 16 cm; wrapper com \ref simuladas); todos os 13
rótulos de \ref/\label existem na tese; zero travessões; "cerca de 250 mil" é
arredondamento fiel do espelho (250.365 original / 250.221 corrigida, §3.2).

**Loop de excelência**: verificador independente em contexto limpo aplicou
teste cego de compreensão (10 itens) + revisão de estilo → REPROVADO na 1ª
rodada (item h não respondível: faltava o mapa para os capítulos de
resultados; uma frase de 55 palavras exigia releitura; contrato de
rastreabilidade semiórfão) → 3 correções aplicadas → re-submetido →
**APROVADO na 2ª rodada**: 10/10 itens do teste respondíveis pela prosa
isolada, zero travessões, zero sigla invertida, nenhuma frase que exija
releitura, nenhum vício novo introduzido pelos ajustes.

## 3. Sugestões secundárias (fora da proposta, para decisão do principal/autor)

S1. **Tabela 3.1**: alinhar a coluna Pilar aos quatro nomes da prosa; marcar
    E1/E2 como experimentos de apoio (não pilar) em nota; ou dar Id às quatro
    linhas "---" do pilar do conjunto inicial, ou explicar na nota por que
    essas execuções são recuperáveis por outro caminho. A promessa "cada qual
    associado a um experimento identificado" saiu da nova abertura, o que já
    desarma a contradição.
S2. **Pré-registro (l.80-88)**: nomear UM marco em frase própria ("O marco do
    pré-registro é X; a primeira versão data de maio de 2022, e ambas são
    preservadas com a tese").
S3. **Ressalva E3/extensão (l.96-98)**: adiar para a Seção 3.8.2 ou completar
    com meia frase de contexto ("houve um desenho maior; a divergência é
    declarada na Seção X").
S4. **Numerar os pilares 2 e 3** nas aberturas das Seções 3.6 e 3.7 (uma
    palavra cada) e manter o protagonista custo nas transições: 3.7 →
    "Resolvido o custo de começar, aparece o custo de continuar"; 3.8 → "o
    que o custo total compra".
S5. **Seção 3.4 (Métricas)**: frase de ponte no padrão das vizinhas ("Falta a
    última peça do terreno comum: a régua...").
S6. **Tiques**: cortar "vale a visão de conjunto" (resolvido pela proposta) e
    "Vale mapear o caminho" (l.442).
S7. **Legenda da fig:metodo-sequencia**: com a nova abertura, a legenda pode
    encolher para o que só ela faz ("cada seta indica o que precisa estar
    resolvido antes do passo seguinte"), removendo a re-narração dos pilares.
S8. **Política de itálico** para estrangeirismos (framework em redondo vs
    \textit{pool-based}): declarar e uniformizar.

## 4. Limites deste parecer

A banca não editou o Capítulo 3: a proposta e as sugestões sobem ao principal
para gate com o autor (PROTOCOLO §2-bis). Os três assentos e o verificador
são instâncias do mesmo modelo (corroboração, não independência estatística).
Nenhum número novo foi introduzido; o único número da proposta ("cerca de 250
mil") espelha o §3.2 e deve acompanhar qualquer mudança futura da base.
