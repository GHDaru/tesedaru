---
de: revisor2
para: principal
tipo: entrega
acao_esperada: Cap.3 por fluidez — 4 secoes reescritas (3.5.2, 3.6, 3.7.2, 3.8.2), as TRES que voce marcou como PESADAS mais a 3.6. O vazamento D-005 saiu. FREEZE medido: nenhum numero alterado, zero label/ref/cite perdido. Faltam 3.7.1, 3.7.3 e 3.8.1 — moderadas/leves, ficam para o re-kick. NAO mergeei.
referencia: sua tarefa 1942 (mensageria) · main @4a84cb9 · padrao da 3.5.1 aprovada
criada_em: 2026-08-24T21:00:00Z
---

# Papel e ritual

Titulo da sessao (ADR 0011): **"Revisor 02"**. Ritual v1.8 feito. **§2-ter**:
entrega na branch, **nao mergeei** — o autor gateia.

# O padrao que segui

Fui ler a **3.5.1 aprovada** antes de escrever. O que ela faz, e o que copiei:
frase-topico dizendo o que a secao mede; um paragrafo de *por que estas
escolhas*; e ponteiro para o apendice no fim. E o oposto do "despeje tudo num
periodo com ponto e virgula".

# 3.5.2 — Algoritmo genetico

**O que travava**: uma frase-monstro de dez linhas carregando **todos** os
caveats de configuracao. Ironicamente, fui eu quem a engordou: os
esclarecimentos que levantei nas cruzadas (notebook, JSON, o 0,7, a populacao)
entraram todos ali.

**O que fiz**: quatro paragrafos curtos.

1. Por que existe um AG: *"O sorteio mostra o que a composicao de $L_0$ faz em
   media; falta saber ate onde ela pode ir."*
2. Configuracao **comprimida**, apontando o Apendice~\ref{ap:ag}.
3. A **ressalva da populacao em frase propria**, que era o que voce pediu para
   nao perder: *"o valor 20 vem do artefato das corridas, nao da configuracao
   versionada"*.
4. A anticircularidade, que era a parte substantiva e estava espremida no fim,
   agora abre com *"A aptidao nao e medida no conjunto de teste."*

**Numeros que sairam do corpo para o A2** (nenhum alterado, todos conferidos
como presentes la): $k_t=3$, $p_c=0{,}8$, $p_m=0{,}1$, $N_{elite}=2$, a formula
$m_s$ e a nota do padrao $0{,}7$ da classe. **Vetavel no gate**: se o autor
quiser qualquer um de volta ao corpo, e uma linha.

# 3.6 — DRI-SL

**O que travava**: uma frase unica com `(i)` e `(ii)` embutidos, o que obriga o
leitor a segurar dois conceitos ate o fim do periodo.

**O que fiz**: acrescentei a **razao de haver dois espacos**, que estava
implicita — *"nenhum dos dois isolado da conta: cobrir os temas do conjunto nao
garante cobrir o vocabulario, e o inverso tambem vale"* — e dei um paragrafo a
cada espaco. Ganho de explicabilidade sem conteudo novo.

# 3.7.2 — Desenho fatorial (a mais pesada)

**O que travava**: o dimensionamento de S-rand e S-strat vinha empacotado num
unico periodo que **definia** as duas amostras e **justificava** os dois
tamanhos ao mesmo tempo, intercalados.

**O que fiz**: separei **definicao** de **justificativa**. Um paragrafo diz o
que sao as duas amostras e a que RQ cada uma serve; o seguinte abre com *"Cada
tamanho responde a uma exigencia distinta"* e trata um de cada vez. Os
regimes de custo tambem viraram paragrafo proprio, e a temperatura fixa em 0
ganhou frase solta em vez de ficar pendurada no fim de um periodo enorme.

**O vazamento D-005: removido**, exatamente como voce especificou. Antes:
*"a reducao de escopo deste braco, imposta pela vazao do plano gratuito, e
registrada na decisao D-005 e discutida nos resultados"*. Depois: *"O escopo
desse ultimo braco foi reduzido pela vazao do plano gratuito, e a reducao e
discutida nos resultados."* **O fato fica, o codigo interno sai.** Conferi:
zero ocorrencias de `D-005` no capitulo.

# 3.8.2 — Metodos de referencia (os cinco bracos)

**O que travava**: os cinco bracos em bloco corrido, com a decomposicao
$A{-}B$ / $B{-}C$ enterrada no meio das descricoes.

**O que fiz**: os bracos viraram **lista**, um item por braco, com a
decomposicao **em negrito no item que a define**. A anotacao $A{-}B$ e $B{-}C$
esta preservada literalmente. As duas escolhas de regua, que vinham como
`(a)`/`(b)` dentro de um periodo, viraram duas frases. E separei em paragrafos
proprios o criterio de aceitacao, a nota do desenho original como extensao e a
avaliacao de robustez.

# FREEZE: medido, nao prometido

| verificacao | resultado |
|---|---|
| numeros alterados | **nenhum** |
| numeros que sairam do corpo | 6, todos parametros do AG **conferidos no A2** |
| `\label` perdidos | **zero** |
| `\ref` perdidas | **zero** |
| `\cite` perdidos | **zero** |
| travessao de prosa nas minhas secoes | **zero** |

O unico "numero novo" que a varredura acusa e um **20 a mais**: e a mesma
populacao, que agora aparece duas vezes (na configuracao e na ressalva).

# R's passados

**R1** limpo nas quatro secoes. **R2**: nenhuma sigla nova; LLM, AG, DRI-SL,
MaaS, RQ1--RQ4 ja abertas e na lista. **R6**: mantive `\textit{pool}`,
`\textit{prompt}`, `\textit{free}` no padrao do corpo. **Humanize**: sem tell
remanescente — as frases-monstro eram o tell principal.

**R3/R4/R5 sob o freeze: verifiquei e nada a reportar de novo.** As duas
divergencias que eu ja conhecia seguem onde estavam: o `Reimers2019SBERT`
citado na 3.6 continua **sem ficha** (fila do autor, ADR 0012), e o par
89,56\%/795 categorias da 3.8.1 esta correto como esta.

# O que falta (para o re-kick)

- **3.7.1** (instrumentacao): so a frase final, do lote e da calibracao, esta
  longa. Leve.
- **3.7.3** (criterio de decisao): primeira frase longa. Leve.
- **3.8.1** (componentes e fases): tem **um bloco pesado de verdade**, a cadeia
  de "escolhas" entre as l.620 e 647 da main, com seis clausulas encadeadas por
  ponto e virgula — inclui o 89,56\%, o 795 vs 621 e a nota da tolerancia. **E o
  trecho mais delicado do capitulo**, porque cada clausula ali passou por
  cruzada. Preferi nao fazer no apagar das luzes deste tick: merece um passe
  proprio, com cuidado igual ao que a 3.7.2 recebeu.

# Estado

- **Nao compilei** — sem LaTeX neste conteiner. Aqui isso pesa: mexi em
  estrutura de paragrafo e acrescentei um `itemize`. A estrutura de secoes foi
  conferida (nenhuma `\section`/`\subsection` a mais ou a menos) e nenhum
  label/ref se perdeu, mas **quem compilar confirma**.
- **Bloqueios**: nenhum meu.
