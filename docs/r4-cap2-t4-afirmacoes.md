# R4 do tema t4 do Capítulo 2 — afirmações e números sem âncora

**Escopo**: `2-fundam/texto.tex`, seção 2.4 ("Classificação de texto curto") —
linhas 674-769 na `main` de 2026-08-17T12:30Z (eram 627-721 quando o
levantamento foi feito). Cada ponto abaixo dá o trecho citado além do número,
porque a faixa desliza a cada merge; ver a nota de recuperação no fim.
**Rodada**: R4 — princípio III (afirmação fundamentada) com o princípio V
(nenhum número sem artefato rastreável) no mesmo passe, porque este bloco é o
primeiro do capítulo que faz afirmações numéricas sobre **os nossos próprios
dados**.
**Executado por**: revisor1 · **Data**: 2026-08-17
**Base**: a prosa da `main`, com as citações conferidas contra o `.tex` da
branch `bibfix/lotes` — várias chaves já foram repontadas lá, e diagnosticar
contra a `main` sozinha já me fez errar duas vezes.
**Natureza**: levantamento. Nenhuma frase reescrita.

## Placar

O bloco é bem citado: praticamente toda afirmação carrega fonte, e as
repontuações do bib-fix acertaram o alvo (o caso do pré-processamento, abaixo,
é exemplar). São **seis** pontos, e a boa notícia é que **os dois numéricos
sobre os nossos dados estão CERTOS** — só não dizem onde se verificam.

| # | Linha | Tipo | Situação |
|---|---|---|---|
| 1 | 671 | número sobre dado nosso | **verificado, exato**; falta declarar o artefato |
| 2 | 684-686 | afirmação sobre dado nosso | **verificada, 97,93%**; falta declarar o artefato |
| 3 | 656-657 | número atribuído a fonte qualitativa | atribuição imprecisa — **segunda ocorrência do padrão** |
| 4 | 707 | citação que talvez contradiga a afirmação | verificar |
| 5 | 710-711 | custo afirmado sem fonte nem número | órfã |
| 6 | 661-662 | repontuação do bib-fix | **acertou** — registro positivo |

---

## 1. "os textos têm 4 a 50 caracteres" (hoje L707; era L671) — CERTO, e agora tem prova

> "No domínio específico — cupons fiscais de varejo — os textos têm 4 a 50
> caracteres, caixa alta e abreviações agressivas"

Sem citação e sem remissão a artefato. Rodei a checagem sobre
`activelearning/data/dataset.csv`, coluna `nm_item`, 250.221 descrições:

```
comprimento em caracteres: min = 4   max = 50   média = 31,2   mediana = 32
p1 = 15 · p5 = 20 · p50 = 32 · p95 = 40 · p99 = 45 · p100 = 50
```

**Os extremos batem exatamente**: mínimo 4, máximo 50. A afirmação está certa.

O que falta é o princípio V: o número não diz onde se verifica. Conserto barato
— remeter a `data/DICIONARIO.md`, que já existe e registra a coluna e o md5 do
arquivo, ou acrescentar a frase de que os extremos vêm do conjunto completo.

Sugestão de conteúdo, porque a faixa bruta esconde a distribuição: o intervalo
**20 a 40 caracteres concentra 90%** das descrições. Dizer "4 a 50" é correto e
dá a impressão de dispersão maior do que a real.

## 2. "quase todo termo ocorre uma única vez por descrição" (hoje L721; era L684-686) — CERTO

> "em texto curto a frequência de termos satura (quase todo termo ocorre uma
> única vez por descrição), o que explica a vantagem empírica da variante
> binária sobre TF e TF--IDF"

Atribuído a `Daru2024Dissertacao`, então tem fonte. Mas é afirmação empírica
sobre o nosso conjunto e dá para medir:

```
descrições com ALGUM termo repetido: 5.180 de 250.221  =  2,07%
tokens por descrição: média 5,49 · mediana 5
```

**97,93% das descrições não repetem nenhum termo.** A afirmação se sustenta com
folga, e o número é mais forte que o "quase todo" do texto. Vale trocar o
qualificador vago por ele — é o tipo de troca que o princípio V premia:
substituir uma impressão por uma medida.

## 3. "tipicamente até 200 caracteres" (hoje L692; era L656-657) — segunda ocorrência do padrão

> "o texto \emph{curto} especializa a tarefa para sequências de comprimento
> limitado — tipicamente até 200 caracteres `\cite{Song2014, Alsmadi2019}`"

As duas fontes têm fichamento, e os dois fichamentos dizem, na seção "Números
que posso citar":

- `Song2014`: *"(Survey de 2014; usar caracterização qualitativa.)"*
- `Alsmadi2019`: *"(Revisão qualitativa; 89 referências.)"*

Um limiar numérico está atribuído a duas obras que os nossos próprios registros
de leitura declaram qualitativas. **É exatamente o caso A1 da R4 do t2**, onde
o `Settles2012` sustentava "dez vezes a duração do áudio" contra o próprio
fichamento que diz "não usar como fonte de números".

Duas ocorrências do mesmo padrão em dois blocos deixam de ser acidente. Vale a
checagem executável que propus no relatório da R4 do t2: cruzar fichamentos que
se declaram qualitativos com números citados ao lado das suas chaves.

**Conserto**: localizar o limiar em uma das obras e registrar a página no
fichamento; ou trocar por fonte que o meça; ou tirar o número e manter
"sequências de comprimento limitado", que é o que as duas fontes sustentam.

## 4. `Xu2017` sustenta "benefício limitado"? (hoje L743; era L707)

> "arquiteturas profundas convolucionais e recorrentes capturam padrões locais
> e sequenciais `\cite{Goodfellow2016, Xu2017}`, com benefício limitado em
> textos muito curtos"

A primeira metade é sustentada. A segunda é o problema: `Xu2017` é
*"Self-Taught Convolutional Neural Networks for **Short Text** Clustering"* —
um trabalho que **demonstra rede convolucional funcionando em texto curto**.
Usá-lo para dizer que o benefício é limitado nesse regime é, no mínimo,
citá-lo contra a sua própria tese.

Não afirmo que a frase esteja errada — afirmo que a citação não a sustenta e
pode contradizê-la. `Xu2017` está na minha lista de obras que mereceriam
fichamento próprio (relatório da R3 do t4); com a ficha feita, dá para decidir
com evidência localizável em vez de por título.

**Conserto**: fichar `Xu2017` e então (a) manter a citação só para a primeira
metade, ou (b) achar fonte que meça o benefício limitado, ou (c) reformular.

## 5. "ao custo de treinamento e inferência substancialmente maiores" (hoje L747; era L710-711)

Sem fonte e sem número. É consenso, mas consenso não é fundamentação — e neste
caso a tese **tem** o dado: ela opera com um par de classificadores justamente
por causa dessa diferença de custo, e o Capítulo 3 a mede.

**Conserto**: remeter ao Capítulo 3 ou dar a ordem de grandeza. Resolve pelo
princípio III na modalidade "provada com dados/artefatos", sem precisar de
citação externa.

## 6. Registro positivo: a repontuação do pré-processamento acertou

> "sua escolha e ordem afetam o desempenho final `\cite{Naseem2021HateSpeech,
> Aliero2023}`"

Na `main` esta linha ainda cita `Naseem2021`, chave morta. Na `bibfix/lotes` já
aponta para `Naseem2021HateSpeech`, que é *"A survey of pre-processing
techniques to improve short-text quality"* — ou seja, a repontuação não foi
mecânica: caiu na obra que efetivamente trata do assunto da frase.

Registro porque numa auditoria vale dizer o que está certo, e porque isso
significa que **o gate do bib-fix melhora este bloco sem trabalho adicional**.

O mesmo vale para `Selva2021` → `Birunda2021` na frase sobre polissemia
(L694 da `main`, L688 da branch).

---

## Como reproduzir as duas medições

Do repositório `activelearning`, sobre `data/dataset.csv`:

```python
import csv, collections, statistics
comp, rep, tot = [], 0, 0
with open('data/dataset.csv', encoding='utf-8') as f:
    r = csv.reader(f); next(r)
    for linha in r:
        d = linha[0].strip()
        if not d: continue
        tot += 1; comp.append(len(d))
        if any(v > 1 for v in collections.Counter(d.split()).values()): rep += 1
print(min(comp), max(comp), statistics.mean(comp), rep / tot)
# 4 50 31.2 0.0207
```

O `scripts/check_dataset.py` daquele repositório já roda doze checagens do
mesmo tipo; estas duas cabem lá como décima terceira e décima quarta, e aí a
frase do Capítulo 2 passa a ter checagem executável em vez de leitura humana.
Proponho ao dono daquele arquivo — sou eu — fazê-lo quando o gate liberar.


---

## Nota de recuperação — este relatório esteve PERDIDO por nove horas

**O que aconteceu**: escrevi este documento às 03:52 de 2026-08-17, no commit
`3401cf5`, e anunciei a entrega ao principal no aviso `20260817-0353`. O commit
nunca chegou à `main`: um **force-push meu**, ao reconstruir a branch de
trabalho a partir da `main`, desanexou-o. Ele ficou como *dangling commit* —
existindo no repositório, alcançável por nenhuma referência.

**Como apareceu**: só quando o principal me redespachou o R4 do t4 (12:15) e eu
fui conferir antes de refazer. O plano dizia "R4 CONCLUÍDA … 6 pontos em
`docs/r4-cap2-t4-afirmacoes.md`" — **apontando para um arquivo que nunca
existiu em commit nenhum**. Recuperado com `git show 3401cf5:<arquivo>`.

**Por que isto importa mais do que o arquivo em si**: durante nove horas o plano
afirmou uma entrega cujo artefato não resolvia. É exatamente a falha que o
princípio V existe para impedir — a diferença é que aqui o número sem artefato
era um *status*, não uma medida. Um artefato citado e inalcançável é
indistinguível de um artefato inexistente para quem lê o plano.

**Antídoto, e é executável**: o `plano-revisao.json` cita caminhos de arquivo em
várias notas. Uma checagem que resolva cada caminho citado no plano contra o
disco (e falhe se não resolver) fecha esta classe inteira, e custa dez linhas.
Fica oferecido ao principal; a mesma ideia serve para os `qa-report.md` dos
ciclos.

**Segunda lição, a das linhas**: as referências deste relatório eram todas por
número de linha, e em nove horas o texto deslizou ~36 linhas. Atualizei-as e
passei a dar também o trecho citado. É a mesma conclusão a que o revisor2 e eu
chegamos hoje por caminhos independentes — ele quase reprovou uma entrega
correta comparando janelas fixas, eu quase perdi um achado procurando frase com
quebra de linha. **Medir e apontar por seção e por trecho, nunca por faixa de
linhas.**
