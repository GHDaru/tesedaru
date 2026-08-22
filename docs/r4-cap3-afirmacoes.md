# R4 do Capítulo 3 — afirmações × lastro

> Ciclo Maestro `r4/cap3-afirmacoes` · tarefa `20260822-1000` do principal ·
> agente `revisor1` · skills `constitution-check`, `diagnose-before-fix`,
> `verifiable-dod`.
> Princípio III (afirmação fundamentada) é o critério; V (número com artefato)
> entra só onde o lastro de uma afirmação É um número.

## Como foi medido (e não lembrado)

A varredura não foi por leitura impressionista. Três medições:

1. **Conectivos de justificativa** (`porque`, `a fim de`, `garante`, `de modo
   que`, `suficiente para`, `pois`, `por isso`, …) — 29 ocorrências no
   capítulo. Cada uma abre uma afirmação que promete lastro.
2. **Verbos de resultado** (`melhora`, `supera`, `reduz`, `demonstra`, …) — 15
   ocorrências, para achar conclusão indevida num capítulo que só descreve.
3. **Reprodução dos números da base direto do arquivo cru**
   (`activetextclassification@b540533 data/dataset.csv`, 250.365 linhas) e
   execução do verificador da biblioteca
   (`activelearning/scripts/check_dataset.py`).

## Veredito global

| classe | quantidade |
|---|---|
| afirmações com lastro **ok** | 26 |
| **corrigidas** nesta entrega (lastro existia, estava implícito ou apontava errado) | 7 |
| **divergentes** — sinalizadas, NÃO corrigidas (exigem decisão) | 3 |
| **órfãs** sem lastro nenhum | 0 |

Nenhuma afirmação órfã. O capítulo é disciplinado: não conclui, descreve — os
15 verbos de resultado são todos de definição de critério ou de referência ao
capítulo que mede. O problema do Cap. 3 não é afirmar sem base; é **apontar
para a base errada** em sete pontos e ter **três justificativas que a própria
evidência citada contradiz**.

---

## A. Corrigidas nesta entrega (lastro implícito → explícito)

### A1. O E5 apontava para o diretório errado de artefatos — erro meu, da Fase 2

A nota `†` que eu mesmo escrevi no ciclo do expurgo de pilares dizia que os
artefatos do E5 estão em `experiments/e6population`. Estão em
**`experiments/e5cycle`** — diretório que existe, contém `run_cycle.py`
(o ciclo real) e `calibrate_batch.py`, e é o que o Apêndice A7 já citava
corretamente. A tabela-mapa promete rastreabilidade; apontava para o lugar
errado.

- antes: `\texttt{experiments/e6population} (E5, E6)` · `os artefatos estão em \texttt{experiments/e6population}`
- depois: `\texttt{experiments/e5cycle} (E5) $\cdot$ \texttt{experiments/e6population} (E6)` · `os artefatos estão em \texttt{experiments/e5cycle} e o gatilho de parada que ele exercitou é descrito no Apêndice~\ref{ap:parada-laco}`

### A2. Nota de reprodutibilidade da base (duas chaves de texto e a ordem)

Ver a seção "Cruzada do revisor2" adiante: o achado é real, a causa que me foi
entregue não era. A nota escrita no capítulo diz o que eu **reproduzi**:
duas chaves de texto (colapso de espaços na auditoria; `strip+lower` no
particionamento), acento é inócuo nesta base, e o filtro `≥ 2` vem **antes** da
deduplicação — ordem que explica o passo 715 → 714 classes.

### A3. E2 prometido e sem desfecho no capítulo

O método dizia que o número de épocas "é determinado empiricamente" e parava
aí; a tabela marca E2 como `(interno)`. O leitor não tinha como saber o
resultado. Acrescentado: **três épocas**, uniforme entre braços, com remissão à
Seção `sec:res-e3p`, onde o valor é reportado (`5-resultados:498`).

### A4. Calibração de lote sem artefato nomeado

"decisão registrada junto aos resultados" → acrescentado o artefato
`experiments/e5cycle/calibrate_batch.py`.

### A5. "ordens de grandeza" — magnitude sem medição

A frase afirmava redução de custo "em ordens de grandeza", número que nenhum
artefato sustenta. Trocado pelo argumento que é verdadeiro por construção do
desenho: cada braço custa **um** ajuste fino do BERTimbau, e não um por
iteração do ciclo. Mesma conclusão, agora demonstrável sem medir nada.

### A6. "5× mais dados" — denominador não declarado

`5\times` só fecha contra a base corrigida (250.221/50.000 = 5,0); contra a
base efetivamente usada na comparação, a deduplicada, é 4,63. Trocado por
"base deduplicada inteira (231.490 textos, cerca de 4,6× o pool)".

### A7. Contagens da base agora têm verificador executável citado no texto

A seção de dados passa a citar `scripts/check_dataset.py`, que reexecuta todas
as contagens. Saiu de "confie no número" para "rode o script" (princípio IX).

---

## B. Divergentes — sinalizadas, NÃO corrigidas

As três exigem decisão porque mudam o sentido de um critério metodológico, e
duas delas atravessam o Capítulo 5. Não são conserto de redação.

### B1. O racional do gate de 85% está invertido (e "um desvio" não é definido)

`3-metodo` diz que o limiar de 85% "fica **um desvio acima**" do melhor
baseline supervisionado leve, cuja acurácia é 89,56% \citep{Daru2024Dissertacao}.
**85% está 4,56 pontos percentuais ABAIXO de 89,56%.** A direção está trocada.
E "um desvio" não diz desvio de quê — não há artefato que fixe esse desvio.

O restante da frase ("exigindo do oráculo qualidade próxima à do teto
supervisionado") só faz sentido com **abaixo**. Ou seja: o argumento pretendido
é defensável, a redação diz o oposto dele.

**Já apontado duas vezes pela banca** (`docs/parecer-ars-r6.md` §3 item 3;
`docs/parecer-r3-r4-r6-leitura-final.md` item 2) e **continua no texto**.
Proposta de redação, para o autor decidir: *"fica 4,6 pontos percentuais abaixo
do melhor baseline supervisionado leve conhecido do conjunto (89,56% com todos
os rótulos), exigindo do oráculo zero-shot qualidade próxima à do teto
supervisionado antes de dispensar tratamento de ruído"*. Isso elimina "um
desvio", que é o número sem artefato.

### B2. A Fase 2 roda entropia; a varredura que deveria justificá-la elegeu outra coisa

`3-metodo` afirma que o tamanho de lote e a estratégia de incerteza da Fase 2
"são fixados com base na varredura de estratégias (Seção `sec:res-e1`) […] e
justifica a escolha por LCE". Mas a Seção `sec:res-e1` conclui o contrário:

> "As margens vencem a entropia no regime de 621 classes: menor margem lidera
> em LCE (0,528) e menor confiança em F1 final (0,421)" — `5-resultados:281-283`
> "[…] recomenda menor margem/menor confiança" — `5-resultados:290`

E a Fase 2 do FALCO, definida em `3-metodo`, seleciona "as $b$ instâncias de
maior **entropia** preditiva".

Portanto a afirmação de que a escolha é justificada pela varredura é
**contradita pela própria varredura citada**. Ou o método declara por que
manteve entropia apesar do E1 (custo, estabilidade, decisão anterior ao E1),
ou a frase deixa de reivindicar um lastro que não tem. É o achado de maior
risco de arguição desta rodada, e coincide com o item 10 da leitura final da
banca.

### B3. Dois racionais incompatíveis para a mesma constante de parada (fator 22)

- `3-metodo`: $\epsilon=10^{-3}$ "corresponde a cinco iterações sem ganho acima
  do ruído típico de reamostragem".
- `a7-parada-drift`: o racional é que o ganho caia "abaixo da resolução do
  próprio conjunto de validação ($\approx 1/\sqrt{n_V}$)".

Com $n_V = 2.000$, $1/\sqrt{n_V} = 0{,}0224$ — **22 vezes** o $\epsilon=10^{-3}$
efetivamente usado. As duas justificativas não podem estar certas ao mesmo
tempo, e o Apêndice A7 ainda remete ao Capítulo 3 "para o racional das
constantes", fechando um círculo. Não acrescentei remissão cruzada aqui de
propósito: uma referência a mais faria o texto **certificar** um lastro que a
aritmética não sustenta.

---

## C. Cruzada do revisor2 — o achado é real, a causa entregue não era

A entrega `20260822-0921` do revisor2 dizia que o Cap. 3 usa duas
normalizações, sendo a diferença a **remoção de acentos**: com a normalização
declarada sairiam 657 conflitos em vez de 719, e 17.989 duplicatas em vez de
19.356.

Reproduzi tudo do arquivo cru. **Os oito números do capítulo conferem** — nisso
o revisor2 está certo, e a conferência dele vale. Mas a causa não se sustenta:

| chave de texto | base | conflitos | linhas | duplicatas do par |
|---|---|---|---|---|
| minúsculas + colapso de espaços | crua (250.365) | **719** | **1.807** | — |
| minúsculas + colapso de espaços | corrigida (250.221) | 693 | 1.720 | **19.356** |
| `strip` + minúsculas | corrigida | **657** | 1.605 | **17.989** |

Os números 657 e 17.989 que o revisor2 atribuiu à "remoção de acentos" saem, na
verdade, da chave **`strip+lower`** — a do particionamento. E a remoção de
acentos **não pode** mudar contagem alguma nesta base:

```
linhas com acento na DESCRICAO: 0
linhas com acento no ROTULO   : 0
```

**Zero caracteres acentuados** em 250.365 linhas. A variável real é o
**colapso de espaços internos**, não a acentuação.

Isto importa porque eu ia escrever no capítulo a nota que o revisor2 propôs.
Ela afirmaria que preservar ou remover acentos muda as contagens — afirmação
que qualquer membro da banca derruba com um `grep`. A nota que entrei diz o que
eu medi.

Ainda sobre a entrega dele: **231.490 não se reproduz** por dedup simples
(dá 230.163). Reproduz exatamente pela receita da biblioteca — filtrar `≥ 2`
sobre as **linhas**, depois deduplicar por `strip+lower`, nessa ordem:

```
[PASS] textos deduplicados (base E5/E6/E3'): obtido=231490 esperado=231490
[PASS] classes na base experimental: obtido=714 esperado=714
[PASS] classe eliminada pelo dedup (explica 715->714): {'pomada massageadora'}
PASS — dataset reproduz todas as contagens documentadas (231.490/714 e 620+_rare_=621)
```

O revisor2 acertou que a contagem do filtro é sobre linhas. Faltou a ordem
(filtro antes do dedup) e a classe que some por causa dela — que é justamente
o que fazia a conta dele fechar em 710/231.486.

---

## D. Achado fora da minha superfície (para o principal despachar)

**Referência indefinida real no Capítulo 2, que já está com as 7 rodadas
fechadas.** `2-fundam/texto.tex:505-506` quebra a chave no meio da linha:

```latex
com conhecimento pré-treinado \citep{Bayer2024ActiveLLM} (Seção~\ref{sec:fund-
llm}).
```

O LaTeX lê a chave como `sec:fund- llm` (com espaço) e emite
`LaTeX Warning: Reference 'sec:fund- llm' on page 28 undefined`. O rótulo
`sec:fund-llm` existe e está correto — só o uso está partido. Conserto: juntar
as duas linhas. **Não editei: prosa é superfície do principal e eu não tenho
lock em `2-fundam`.**

Varri a tese inteira por esse defeito e ele é **único**:

```
CHAVES PARTIDAS (defeito real): 1
  2-fundam/texto.tex:505  \ref{sec:fund-<QUEBRA>
```

(Outras 4 quebras de `\cite{A,` em fim de linha são legais — vírgula pode
atravessar linha; chave partida no meio, não.) Isto sugere um guarda barato
para o DoD, no espírito do `verifiable-dod`: a regexp acima como checagem
executável, já que a rodada de humanização reflui linhas e pode partir chaves
sem que ninguém perceba. Fica como proposta ao principal, não como coisa feita.

---

## DoD desta entrega (executado, não prometido)

| critério | resultado |
|---|---|
| tese compila | `pdflatex` + `bibtex` + 2 passes, **exit 0, 0 erros** |
| referências/citações indefinidas **introduzidas por mim** | **0** (a única do documento é a do Cap. 2, pré-existente e idêntica na `main`) |
| rótulos que passei a referenciar existem | `sec:res-e3p`, `ap:parada-laco`, `sec:metodo-dados-auditoria` — 1 definição cada |
| caixas estouradas (`Overfull > 20pt`) | **7 na `main`, 7 no branch, lista idêntica** — nenhuma nova |
| números novos no texto têm artefato | 715/714 e `pomada massageadora` ← `check_dataset.py`; três épocas ← `5-resultados:498`; 4,6× ← 231.490/50.000 |
| afirmação corrigida sem inventar lastro | 3 divergências ficaram **declaradas**, não maquiadas |
