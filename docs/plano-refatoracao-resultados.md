# Refatoração dos capítulos de resultados e expurgo da notação EXXX

**Fase 1 — diagnóstico e proposta. Nenhuma linha de prosa foi editada.**
**Executado por**: revisor1 · **Data**: 2026-08-17
**Tarefa**: `20260817-1240` (ordem do autor)
**Skills**: `diagnose-before-fix` (medir antes de propor) e `verifiable-dod`
(o critério de pronto é executável, não é juízo).

---

## O achado que reorganiza a discussão

Antes das opções, um fato que mudou a minha recomendação e que não estava no
enunciado da tarefa:

> **O Capítulo 4 já faz o que o autor está pedindo. O Capítulo 5 é que não faz.**

Compare os títulos de seção dos dois capítulos:

| Capítulo 4 (organizado por **achado**) | Capítulo 5 (organizado por **código**) |
|---|---|
| Sensibilidade à composição e ao tamanho de $L_0$ | **E0**: avaliação fatorial de oráculos LLM |
| Limites por otimização evolutiva | **E0-P**: o prompt como variável do instrumento |
| DRI-SL *versus* aleatório e envelope do AG | **E1**: estratégias de seleção com oráculo perfeito |
| Reexecução independente e efeito da circularidade | **E4**: robustez do aprendizado ao ruído do oráculo |
| Síntese do capítulo | **E6**: seletores em escala populacional e o viés da autoavaliação |
| | **E3'**: o classificador forte julga o pipeline |
| | Decisão do gate e configuração do FALCO |

**Seis das sete seções do Capítulo 5 começam pelo código do experimento.** O
sumário da tese, hoje, anuncia ao leitor uma lista de siglas internas. O
Capítulo 4 não tem um único código e mesmo assim se lê perfeitamente — o que é
a prova, dentro da própria tese, de que a notação é dispensável.

Isso tem uma consequência prática grande: **o problema (B) não é uma varredura
de 191 ocorrências espalhadas — é uma reescrita de sete títulos e da prosa que
os acompanha.** O custo real é muito menor do que o número bruto sugere.

---

## 1. Inventário das ocorrências

### 1.1 Confirmação dos números do principal (e onde divergem)

| Medida | Principal | Minha medição | Observação |
|---|---|---|---|
| Cap. 4 — linhas | 207 | **207** | confere |
| Cap. 4 — seções | 5 | **5** | confere |
| Cap. 4 — códigos E | 0 | **0** | confere |
| Cap. 4 — citações | 0 | **0** | confere (é o achado do meu relatório anterior) |
| Cap. 5 — linhas | 619 | **619** | confere |
| Cap. 5 — seções | 7 | **7** | confere |
| Cap. 4 — palavras | 1.442 | **742** | método diferente |
| Cap. 5 — palavras | 4.973 | **2.759** | método diferente |
| Códigos E na tese | 224 | **191** | regex diferente |

**Sobre as divergências, para não virarem discussão**: conto palavras **depois**
de remover comandos LaTeX e argumentos; a contagem maior provavelmente inclui
`\section{...}`, `\cite{...}` e afins como palavras. Nos códigos, o meu padrão
exige fronteira alfanumérica dos dois lados, então não conta `E` dentro de
identificadores. **A conclusão não muda em nenhum dos dois casos**: a razão
entre os capítulos é 27% pela minha medida e 29% pela do principal, e a ordem de
grandeza dos códigos é a mesma. Uso os meus números daqui em diante porque posso
reproduzi-los; o comando está no fim do documento.

### 1.2 Distribuição por arquivo

| Arquivo | Linhas | Palavras | Seções | Códigos E | Citações |
|---|---|---|---|---|---|
| `3-metodo/texto.tex` | 564 | 3.368 | 10 | **55** | 17 |
| `5-resultados-falco/texto.tex` | 619 | 2.759 | 7 | **92** | 8 |
| `6-conclusao/texto.tex` | 210 | 1.307 | 6 | **20** | 20 |
| `a4-biblioteca/texto.tex` | 45 | 238 | 3 | **13** | 1 |
| `0-iniciais/declaracao-ia.tex` | 37 | 222 | 0 | **7** | 0 |
| `2-fundam/texto.tex` | 896 | 4.638 | 5 | **2** | 138 |
| `a5-prompts`, `a7-parada-drift` | — | — | — | **2** | — |
| **`4-resultados-l0/texto.tex`** | **207** | **742** | **5** | **0** | **0** |

### 1.3 Classificação por contexto — a tabela que decide o trabalho

| Contexto | Ocorrências | Destino proposto |
|---|---|---|
| **Prosa corrente** | **93** | **SOME** — o texto diz o que foi feito |
| **`\label` / `\ref`** | 41 | **FICA** — identificador interno, invisível ao leitor |
| **Tabela / figura / legenda** | 26 | **MIGRA** — só na tabela-mapa do Cap. 3 |
| **Artefato / caminho** (`\texttt{}`, `experiments/…`) | 19 | **FICA** — é rastreabilidade real |
| **Título de seção** | **12** | **SOME** — é o mais visível de todos |

**Formas distintas encontradas** (18): `E0` (40), `E4` (25), `E3` (24), `E6`
(21), `E1` (17), `e0` (16), `e3p` (8), `e6` (7), `e0p` (7), `E5` (5), `E2` (5),
`e4` (5), `e1` (4), `E35` (3), `E3'` (1), `E20` (1), `E25` (1), `E30` (1).

As formas minúsculas (`e0`, `e3p`, `e6`…) aparecem quase sempre dentro de
`\label` e de caminhos de artefato — ou seja, **já estão no lado que fica**. As
maiúsculas é que estão na prosa.

**Conclusão do inventário**: das 191 ocorrências, **105 saem** (93 de prosa + 12
de títulos), **26 migram** para a tabela-mapa e **60 ficam** onde estão. O
trabalho de reescrita é sobre 105 pontos, quase todos concentrados em dois
arquivos (Cap. 5 e Cap. 3).

---

## 2. Opções de estrutura para a assimetria (problema A)

### Opção 1 — Capítulo único de resultados, organizado por pilar

Funde os dois capítulos em um, com duas partes (P1–P2 e P3–P4).

**A favor**: acaba com a assimetria por definição; um único lugar para o leitor
procurar resultado; permite uma síntese comparativa que hoje não existe.

**Contra**: gera um capítulo de ~3.500 palavras e 12 seções, o maior da tese;
**afeta o sumário inteiro** e a numeração de todos os capítulos seguintes
(Cap. 6 vira 5); exige reescrever as remissões `\ref{ch:resultados-l0}` e
`\ref{ch:resultados-falco}` em todos os capítulos.

**Custo de remissões**: as duas chaves de capítulo são citadas ao longo de toda
a tese; some-se a isso a renumeração dos apêndices que remetem a "Capítulo 5".

### Opção 2 — Manter dois capítulos e reforçar o Cap. 4

Cap. 4 continua com P1–P2 e ganha corpo: as citações que hoje não tem (é o
capítulo com **zero** referências externas) e a discussão contra a literatura.

**A favor**: mudança estrutural **zero** — nenhum label, nenhuma remissão,
nenhum sumário afetado; ataca de frente o achado do meu relatório anterior
(`docs/uso-declarado-vs-citacao-real.md`), em que 6 fichas prometem o Cap. 4 e
ele não cita nenhuma; a assimetria de tamanho deixa de ser problema quando o
capítulo menor tem densidade própria.

**Contra**: não elimina a assimetria de tamanho, só a torna defensável; exige
trabalho de conteúdo (escrever discussão), não só de forma.

### Opção 3 — Dois capítulos, com a fronteira redesenhada

Move o E6 (escala populacional) e o E3' (validação com classificador forte) para
o Cap. 4, transformando-o em "resultados de instrumento e de escala" e deixando
o Cap. 5 como "resultados do FALCO".

**A favor**: equilibra os tamanhos de verdade.

**Contra**: **quebra a lógica dos pilares**, que é a espinha dorsal da tese —
P1–P2 e P3–P4 deixam de mapear para capítulos; e move justamente os dois
experimentos mais ligados à hipótese central para longe dela. Listo por
completude; **não recomendo**.

---

## 3. Recomendação explícita

**Opção 2 (manter dois capítulos e reforçar o Cap. 4), combinada com o expurgo
completo da notação no Cap. 5.**

O porquê, em três passos:

1. **A assimetria não é o problema real; a falta de interlocução é.** Um
   capítulo de 742 palavras que responde bem a duas perguntas de pesquisa é
   legítimo. Um capítulo de resultados com **zero citações** não é — e essa é a
   crítica que uma banca faz primeiro. A Opção 1 esconderia esse defeito dentro
   de um capítulo maior em vez de corrigi-lo.

2. **O custo estrutural da Opção 1 é alto e o benefício é cosmético.** Renumerar
   capítulos afeta sumário, remissões e apêndices — e o ganho é "os dois
   capítulos ficam do mesmo tamanho", que não é um objetivo da tese.

3. **O expurgo da notação resolve sozinho boa parte da percepção de
   desequilíbrio.** Hoje o Cap. 5 *parece* uma coleção de relatórios de
   experimento porque se anuncia assim. Reescrito por achado, como o Cap. 4 já
   é, ele passa a se ler como um capítulo, não como um anexo técnico.

**Concretamente, os sete títulos do Cap. 5 passariam a nomear o achado**, não o
código. Exemplos, para o autor calibrar o tom (são propostas, não decisões):

| Hoje | Proposta |
|---|---|
| E0: avaliação fatorial de oráculos LLM | Qual LLM serve como oráculo, e a que custo |
| E0-P: o prompt como variável do instrumento | O prompt é parte do instrumento, não detalhe |
| E1: estratégias de seleção com oráculo perfeito | Seleção sob oráculo perfeito: o teto do método |
| E4: robustez do aprendizado ao ruído do oráculo | Quanto ruído do oráculo o aprendizado tolera |
| E6: seletores em escala populacional e o viés da autoavaliação | Escala populacional e o viés de avaliar no que se coletou |
| E3': o classificador forte julga o pipeline | O veredito do classificador forte sobre a hipótese central |

---

## 4. Efeitos colaterais e como o plano previne cada um

| O que pode quebrar | Medida | Prevenção |
|---|---|---|
| **`\label` com código** (`sec:res-e0`, `tab:e3p`…) | **20 labels** | **Não renomear.** Label é identificador interno e invisível no PDF. Renomear geraria 20 remissões quebradas em troca de nada |
| **Remissões a esses labels** | **20 `\ref`** | Preservadas pela decisão acima — custo **zero** |
| **Compilação do PDF** | — | `tese-pdf.yml` roda a cada push na `main`; e a regra de 2026-08-17 vale (travessão `---` em títulos, nunca `—`), o que importa porque **vamos reescrever títulos**: `scripts/check-travessao-titulo.py` cobre isso |
| **Kanban / painel** | — | O plano é dado, não prosa; atualizar `plano-revisao.json` no mesmo commit, como sempre |
| **Declaração de IA** (7 códigos) | 7 | **Fica.** É documento de prestação de contas, onde o código é a identificação correta do que a IA fez |
| **Apêndice `a4-biblioteca`** (13 códigos) | 13 | **Fica.** É o apêndice de reprodutibilidade — é exatamente o lugar da rastreabilidade |
| **Rastreabilidade perdida na prosa** | 93 | A **tabela-mapa do Cap. 3** (experimento → seção de resultados → artefato) passa a ser a ponte única. **Já existe** um embrião dela no Cap. 3 (linhas 47-48), o que reduz o trabalho |

**Sobre a sugestão do principal**: concordo com a tabela-mapa no Cap. 3 mais o
apêndice, e acrescento a decisão de **não tocar nos labels** — que é o que torna
o custo de remissões igual a zero. Sem essa decisão, o mesmo plano custaria 20
ajustes e o risco de referência quebrada no PDF.

---

## 5. Esforço por fatia

| Fatia | Conteúdo | Ocorrências | Esforço | Depende de |
|---|---|---|---|---|
| **F1** | Tabela-mapa no Cap. 3 (experimento → seção → artefato) | cria | pequeno | — |
| **F2** | Sete títulos do Cap. 5 + primeiro parágrafo de cada seção | ~12 + ~20 | **médio** | F1 |
| **F3** | Restante da prosa do Cap. 5 | ~60 | médio | F2 |
| **F4** | Prosa do Cap. 3 (fora da tabela-mapa) | ~30 | pequeno | F1 |
| **F5** | Prosa do Cap. 6 | ~20 | pequeno | F2, F3 |
| **F6** | Reforço do Cap. 4 (citações + discussão) — problema (A) | — | **grande** | decisão do autor |

**Recomendo começar por F1+F2**: são as que mudam o que o leitor vê primeiro (o
sumário), e a F2 já permite ao autor julgar se o tom dos títulos está certo
antes de investir nas fatias grandes. **A F6 é a única que exige escrever
conteúdo novo** e pode ir por último, ou virar tarefa separada.

---

## 6. DoD executável da Fase 2

Critério de pronto, verificável por comando e não por leitura:

```bash
# 1. nenhum código de experimento na prosa corrente ou em título
python3 scripts/check-codigos-experimento.py     # a escrever na F1
# 2. nenhum travessão Unicode nos títulos reescritos
python3 scripts/check-travessao-titulo.py
# 3. o PDF compila (canário na main)
# 4. multiconjunto de labels e refs IDÊNTICO antes/depois
```

O item 4 é o que garante que a reescrita não quebrou remissão: como decidimos
**não** renomear labels, o conjunto tem de sair idêntico — e isso é comparação
de conjuntos, não julgamento.

Ofereço escrever o `check-codigos-experimento.py` na F1, no mesmo formato dos
outros: bateria com o par negativo de cada invariante, e a lista de contextos
autorizados vindo do plano aprovado pelo autor, não do meu juízo.

---

## Como reproduzir as medições deste documento

```bash
cd /home/user/tesedaru
python3 - <<'EOF'
import re, glob
pad = re.compile(r"(?<![A-Za-z0-9])(E\d+[a-z]?'?|e\d+[a-z]?)(?![A-Za-z0-9])")
for f in sorted(glob.glob('[0-9]-*/texto.tex') + glob.glob('a[0-9]*/texto.tex')
                + glob.glob('0-iniciais/*.tex')):
    corpo = re.sub(r'%.*', '', open(f, encoding='utf-8').read())
    limpo = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?', ' ', corpo)
    print(f, len(pad.findall(corpo)), len(re.findall(r'[A-Za-zÀ-ú]{2,}', limpo)))
EOF
```

---

## O que esta fase NÃO decidiu

- **Nenhuma linha de prosa foi editada** — a tarefa é explícita e eu respeitei.
- **A escolha entre as opções é do autor.** Recomendo a 2, mas as três estão
  medidas com o mesmo cuidado justamente para ele poder discordar com base.
- **Os títulos propostos são rascunho de tom**, não redação final.

---

## 7. Régua de tom do autor — VINCULANTE para todas as fatias

**Origem**: as 5 edições que o autor fez no pacote t2 (tarefa 1005 da banca), em
frases da própria humanização do R1. Ordem dele em 2026-08-17: *"nos gates de
retrabalho do Capítulo 5, já passe as diretrizes, senão terá retrabalho depois"*.
Por isso a régua deixa de ser observação e vira **critério de aceite**.

| Ele trocou | Por | Regra que isso fixa |
|---|---|---|
| "poderoso" | "funciona **quando** o espaço de entrada tem estrutura conhecida" | **adjetivo avaliativo → condição em que vale** |
| "inevitável" | "necessário na prática" | **absoluto → qualificado** |
| "cardápio de LLMs" | "oferta de LLMs" | **metáfora → termo literal** |
| "eventualmente" | "possivelmente" | **falso amigo**: em português "eventualmente" é *de vez em quando* |

### As quatro regras, na forma em que serão verificadas

1. **Sem metáfora DECORATIVA.** Nada de "cardápio", "veredito", "espinha
   dorsal" no texto da tese: são figuras que substituem o termo próprio.

   **Distinção que a régua precisa fazer, e que eu quase errei**: *"teto"* NÃO
   entra na lista. Ao varrer o Cap. 5 encontrei 11 ocorrências e ia proibi-las
   — mas fui olhar, e todas são **termo técnico estabelecido**: "teto
   supervisionado", "teto de medição ($\approx 99{,}3\%$)", "teto de
   significância". Limite superior de uma medida se chama teto em português
   técnico, e trocar isso empobreceria o texto em nome de uma regra.

   **O critério não é a palavra, é a função**: figura que substitui o termo
   próprio sai; termo consagrado do campo fica. Uma lista de palavras proibidas
   aplicada sem esse filtro produz exatamente a classe de falso positivo que
   venho perseguindo nos checadores.
2. **Sem adjetivo avaliativo sozinho.** Se algo é "poderoso", "notável",
   "impressionante", diga **sob que condição** e com que medida.
3. **Sem absoluto não sustentado.** "inevitável", "sempre", "nunca", "qualquer"
   só com evidência que os sustente; senão, qualifique.
4. **Sem falso amigo.** "eventualmente" (≠ *eventually*), "assumir" no sentido
   de supor, "endereçar" no sentido de tratar, "suportar" no sentido de admitir.

### Aplicação retroativa já feita (F2)

Três títulos que eu havia proposto violavam a régua e **foram trocados antes do
gate**, por ordem do autor:

| Proposto | Aplicado | Regra |
|---|---|---|
| O *prompt* é parte do instrumento, **não um detalhe de implementação** | O *prompt* como variável do instrumento de medição | 1, 2 |
| Seleção sob oráculo perfeito: **o teto do que o método pode render** | Seleção sob oráculo perfeito: limite superior do método | 1 |
| **O veredito** do classificador forte sobre a hipótese central | Avaliação da hipótese central com o classificador forte | 1 |

A mesma troca foi propagada a mais dois pontos que a varredura revelou:

- a linha do E3$'$ na **tabela-mapa do Cap. 3**, que repetia "veredito" —
  inconsistência que só apareceu porque apliquei a régua aos dois arquivos, e
  não só onde eu esperava;
- a frase de abertura do resultado do E3$'$ (Cap. 5), que dizia *"O **veredito**
  da hipótese central é negativo"* e passou a *"A hipótese central **não se
  confirma** na configuração executada"*. Estava a dois parágrafos do título que
  eu acabara de limpar; deixá-la seria trocar a metáfora de lugar, não removê-la.

### Efeito no DoD das fatias F3, F4, F5 e F7

Ao critério executável já definido acrescenta-se uma **leitura dirigida** — esta
não é automatizável e eu declaro isso em vez de fingir que é: cada trecho novo
ou reescrito passa pelas quatro regras acima antes de entrar no commit, e a
mensagem de entrega declara quais delas foram acionadas.

O que **é** automatizável fica no `check-codigos-experimento.py` (fatia F1, se
despachado): a lista de metáforas proibidas do item 1 vira `grep`, porque é
vocabulário fechado. Os itens 2 a 4 dependem de julgamento e ficam explicitamente
fora da checagem — **checagem que promete julgar tom é checagem que mente**.
