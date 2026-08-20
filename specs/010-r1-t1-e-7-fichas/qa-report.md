# QA — ciclo 010: R1 do t1 + as 7 pendências reais

**Tarefa:** 20260817-0740 (ordem direta do autor: "quero terminar o t1")
**Executor:** revisor2 · **Branch:** `humanize/cap2-t1`
**Skills:** `fight-the-pile-up` (R1) · `fichamento` (as 4 fichas)

## Parte 1 — R1 (humanização) do t1

Medido **por seção** (`\section{Aprendizado supervisionado…}` até
`\section{Aprendizado ativo}`), não por faixa de linhas. Essa mudança de método
é consequência direta do falso positivo que cometi na verificação do t2: janela
de linha fixa quebra quando o texto muda de tamanho.

| # | Critério | Antes | Depois |
|---|---|---|---|
| 1 | travessões `—` na seção | **9** | **0** |
| 2 | multiconjunto de chaves de citação | 25 | **25, idêntico** (`diff` vazio) |
| 3 | todos os números da seção | — | **idênticos** (`diff` vazio) |
| 4 | travessão em `\section`/`\subsection`/`\caption` (aviso 0815) | — | **nenhum** |

As 9 conversões foram todas de aposto encaixado entre pares de travessão:
estratificação sob desbalanceamento, cobertura errática do intervalo de Wald,
regime do teste de McNemar, suposição de normalidade do Wilcoxon e funcionais
sem distribuição conhecida no bootstrap.

**Nenhum número foi tocado** — inclusive os do parágrafo das sementes, que o
autor acabou de aprovar no lote R4 (seis como mínimo, oito por margem, pisos
$p=0{,}031$ e $p=0{,}0078$). Aquele trecho passou intacto: humanizei em volta
dele, não dentro.

## Parte 2 — as 7 pendências

Baixei os PDFs de fonte aberta para `a_sanear/` (1,8 MB no total) e li cada um
antes de fichar. Nenhuma ficha foi escrita a partir de resumo de terceiros.

| Chave | Situação | Resultado |
|---|---|---|
| `Grandini2020` | aberta (arXiv 2008.05756, 17 pp.) | **fichada** |
| `Nti2021` | aberta (MECS, 11 pp.) | **fichada** |
| `Widodo2022` | aberta (Sinkron, 8 pp.) | **fichada** |
| `Riyanto2023Comparative` | aberta (IJACSA, 9 pp.) | **fichada** |
| `Reusens2024` | fechada (Elsevier) | link para o autor: DOI 10.1016/j.eswa.2024.124302 |
| `Prechelt2012` | fechada (Springer) | link para o autor: DOI 10.1007/978-3-642-35289-8_5 |
| `Barros2014` | não localizada | segue `nao-encontrada`; **não inserir** o DOI da homônima |

Efeito medido no verificador: o aviso A1 (citada, sem ficha, não canônica) caiu
de **35 para 31** — exatamente as quatro fichadas. As quatro passam
`check-fichamentos.py` com `PROBLEMAS: nenhum`.

### As quatro citações sustentam o que a tese diz que sustentam?

Essa era a pergunta que importava, e a resposta é **sim nas quatro** — verificado
contra o texto da fonte, com seção e página em cada claim:

- **Nti2021** confirma literalmente "k tipicamente 5 ou 10", e as palavras da
  própria fonte (*"are believed to"*, *"there is no formal rule"*) **reforçam** o
  hedge da tese.
- **Grandini2020** descreve as três alternativas que a tese cita e dispensa
  (acurácia balanceada p. 4; Matthews e Kappa p. 9).
- **Widodo2022** usa a estratificação exatamente como remédio declarado para
  desbalanceamento (Resumo, p. 1) — o uso que a tese faz.
- **Riyanto2023Comparative** é a mais alinhada: conclui que o F1 é a métrica que
  importa sob desbalanceamento, em texto multiclasse.

## Achados registrados nas fichas

1. **`Widodo2022`: o PDF do periódico tem o volume ERRADO no cabeçalho** —
   "Volume 6, Number 4" contra o DOI `…v7i4…` e o registro da Crossref (volume
   7). Erro do periódico, não da tese. Registrado para que ninguém "corrija" o
   `.bib` para 6 acreditando seguir a fonte.
2. **`Nti2021`: a conclusão própria da obra aponta k = 7**, não 5 nem 10. Não
   contradiz a tese (que cita a convenção), mas oferece um argumento melhor caso
   o texto precise defender o $k$ desta tese.
3. **`Grandini2020` é um *white paper* corporativo**, não artigo revisado por
   pares. Não compromete o uso (descrição de métricas consagradas), mas a banca
   pode perguntar.
4. **`Riyanto2023Comparative`: ressalva de escala** — 4 classes com razão de
   17:1, contra os 621 rótulos da tese. A conclusão qualitativa transfere; os
   números, não.

## Pendências que NÃO são desta rodada

- `BERT` sem expansão no diagrama TikZ da figura do ActiveLLM (faixa do t3):
  é critério do **R2 (siglas)**, registrado e não corrigido.
- Título e página do `Widodo2022` no `.bib`: superfície do **revisor1**.

## Adendo (2026-08-17T12:06Z) — a main mexeu na minha faixa e o número mudou

O commit `e778bda` da main aplicou as edições 1 e 2 da leitura do autor dentro
da §2.1, **depois** desta medição. Refiz tudo por seção sobre a main
`2d174ea`; abaixo o que é medido, não julgado:

| Medida | main `2d174ea` | branch `e122b4d` | **merge simulado** |
|---|---|---|---|
| travessões `—` na §2.1 | **10** | **0** | **1** |
| chaves de citação na §2.1 | 32 | 32 | **32** |
| `git merge --no-commit` | — | — | **exit 0**, sem conflito |

Leituras que interessam ao gate:

1. **O merge é limpo e as duas edições do autor sobrevivem literais** — conferi
   "divergir em sinal", "deixa de ser generalização para ser memorização" e
   "deduplica por texto normalizado" no texto mesclado, e reli os dois
   parágrafos inteiros: nenhuma frase duplicada ou truncada.
2. **O travessão que resta é do autor, não regressão da branch.** Ele nasceu em
   `e778bda` ("desempenho agregado) — separação que é operacional…"). A main
   foi de 9 para 10 travessões na seção; a branch zera os 9 antigos e não
   toca no novo. Portanto o DoD deste ciclo passa de `0` para `1`, e a causa
   é texto novo aprovado pelo autor.
3. **Não afeta o build.** O travessão está em corpo de texto, não em
   `\section`/`\subsection`/`\caption` — o aviso 0815 segue respeitado (medido:
   nenhum travessão em título ou legenda no merge).

Não converti a frase: é prosa recém-aprovada do autor e não é minha para
mexer. Se o gate quiser zerar, a conversão é de uma linha, mas **tem de ser
vírgula, não dois-pontos** — a frase do autor já usa dois-pontos oito palavras
depois ("não estética: nos experimentos"), e um segundo travaria a leitura.

## Adendo 2 (2026-08-17T15:00Z) — o pacote de inferência do autor substituiu 8 das 9 conversões

O commit `03d88d5` aplicou na §2.1.4 o pacote de inferência da banca aprovado
pelo autor: 4 parágrafos novos com as fórmulas de Wilson, McNemar, Wilcoxon e
bootstrap em display. **Aquela era a região onde viviam 8 das minhas 9
conversões de travessão.** Trouxe a main para dentro desta branch e resolvi os
2 conflitos **em favor da main** — texto do autor prevalece sobre humanização
minha, sem discussão.

O que sobra desta entrega no `.tex`, medido:

| Medida | main `03d88d5` | **esta branch, resolvida** |
|---|---|---|
| travessões `—` na §2.1 | 3 | **1** (o do autor, do `e778bda`) |
| chaves de citação na §2.1 | 32 | **32, idêntico** |
| rótulos `eq:wilson/mcnemar/wilcoxon/bootstrap` | 4 | **4, intactos** |
| `\begin{table}` / `\end{table}` | 4 / 4 | **4 / 4** |
| linhas que esta branch ainda muda no `.tex` | — | **2** |

Ou seja: **a contribuição desta branch ao texto encolheu para UMA conversão** —
o par de travessões da frase da validação cruzada estratificada virou vírgulas.
As outras oito foram absorvidas por texto melhor que o meu, escrito pela banca e
aprovado pelo autor. Registro sem rodeio: o R1 do t1, na parte de prosa da
inferência, **foi superado e não precisa mais de gate**.

O que ainda justifica esta branch é o resto do ciclo, que o pacote não toca:
as 4 fichas lidas na fonte (`Grandini2020`, `Nti2021`, `Widodo2022`,
`Riyanto2023Comparative`), os 4 PDFs em `a_sanear/`, a verificação das 7
pendências em `fichamentos/verificacoes/pendencias-t1.md` e este relatório.

**Alerta de método, para mim mesmo:** eu só descobri que o pacote havia sido
aplicado porque fui medir outra coisa. Ele entrou às 13:53, dois minutos antes
do meu próprio aviso das 13:55, e os meus check-ins seguintes comparavam a main
contra **o meu último commit** — janela que esconde tudo o que entrou entre o
meu último fetch e o meu push. Passo a ancorar a janela no último commit que eu
**verifiquei**, não no que eu escrevi.
