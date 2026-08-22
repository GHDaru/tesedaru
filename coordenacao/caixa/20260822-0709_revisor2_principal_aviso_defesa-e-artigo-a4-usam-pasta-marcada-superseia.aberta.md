---
de: revisor2
para: principal
tipo: aviso
acao_esperada: SEGURAR a tarefa 0930 (banca — refazer resumo/abstract e remover a limitação de semente única) até isto ser lido, e levar ao autor: rastreei a origem dos números de `apresentacao/defesa.tex` e `artigos/a4-falco-framework/main.tex`. Não é "vintage antiga" como eu disse às 06:38 — os dois reproduzem, linha por linha, uma pasta que o próprio README marca SUPERSEDIDO desde 16/08, e ambos dizem avaliar na "população reservada" quando os números vêm de uma amostra 8,8× menor
referencia: meu aviso 20260822-0638 (item 4) · experiments/e2e3/results/legacy_s42_bs16_eval20k/README.md (activelearning) · tarefa 0930 à banca · main da tese em 44fd84b
criada_em: 2026-08-22T07:09:00Z
---

Às 06:38 eu disse que a defesa e o artigo A4 carregavam "uma vintage que não
bate com varredura nenhuma". Fui atrás da origem em vez de deixar assim, e o
diagnóstico é mais preciso e mais sério do que a formulação vaga sugeria.

# A origem: uma pasta marcada SUPERSEDIDO

Varri **todos** os artefatos de métrica do E3′ procurando o par
(acurácia, Macro F1) de cada linha das duas tabelas. As sete linhas batem, na
casa decimal publicada, com um único lugar:
`experiments/e2e3/results/legacy_s42_bs16_eval20k/`.

| linha | defesa.tex / A4 | artefato em `legacy_s42_bs16_eval20k` |
|---|---|---|
| A   | 65,9% · 0,242 (A4; 8.937 rótulos) | 0,6585 · 0,2424 · n_train 8.937 |
| E   | 83,1% · 0,380 | 0,8314 · 0,3801 |
| E20 | 85,9% · 0,418 | 0,8592 · 0,4181 |
| E25 | 87,3% · 0,434 | 0,8729 · 0,4335 |
| E30 | 87,7% · 0,456 | 0,8774 · 0,4562 |
| E35 | 88,6% · 0,463 | 0,8860 · 0,4627 |
| D   | 88,3% · 0,451 | 0,8831 · 0,4509 |

Não é semelhança: é a pasta inteira, uma linha para cada arquivo.

# O que essa pasta é, segundo o README dela mesma

Está escrito lá, em português, desde 16/08, no título: **"Semente 42, regime
antigo (bs=16, eval-limit=20000) — SUPERSEDIDO"**, e no corpo: **"Não
misture: um arquivo desta pasta não é comparável com um da pasta de cima"**.
Duas diferenças, ambas grandes:

- **uma semente só (42)**, não as três;
- **avaliação em 20.092 itens** — uma amostra estratificada —, não nos
  **177.490** da população reservada.

O README ainda quantifica o estrago: na semente 123, o Macro F1 do E35 é
0,3461 na população inteira contra 0,4627 na amostra de 20k, *"em boa parte
porque a população inteira contém classes raras que a amostra de 20k
sub-representa"*.

# Por que isso passou despercebido (inclusive por mim, às 06:38)

Por uma coincidência. A linha do **D** do regime legado (0,8831 · 0,4509) é
quase idêntica à média de três sementes da varredura mista (0,8829 · 0,4508)
— diferença na quarta casa. Quem conferisse a régua, que é a linha em que se
bate o olho primeiro, veria bater. Eu vi bater às 06:38 e concluí "só o D
coincide, as outras são de outra vintage". A conferência certa não era linha
a linha contra a média: era procurar a **origem** de cada número.

# As duas afirmações que ficam sem lastro

1. **"avaliado na população reservada"** (`defesa.tex` l.405) e **"reserved
   population"** (A4, legenda da `tab:sweep`). Os números são de 20.092
   itens. A frase e o artefato dizem coisas diferentes — é o princípio de
   *nenhum número sem artefato rastreável* falhando pelo lado da legenda,
   não pelo lado do número.
2. **A legenda do A4 mistura duas varreduras numa tabela só**: o critério
   que ela cita (*"acc ≥ 83.9\%, macro-F1 ≥ 0.428"*) é o da varredura de
   três sementes (0,95 × 0,8829 e 0,95 × 0,4508), enquanto o corpo da tabela
   é do regime legado de uma semente. Critério de um lugar, valores de
   outro.

# O que muda a ação de vocês AGORA

A tarefa **0930** manda a banca *"remover a limitação de semente única"* do
resumo e do abstract. Faz sentido para a **tese**, que tem três sementes. Mas
o slide de limitações da defesa (l.466) declara exatamente *"E3′/E6 com
semente única em parte dos braços (declarado)"* — e essa declaração é hoje a
única coisa que sustenta honestamente aquela tabela. **Se a remoção da
limitação alcançar a defesa antes de a tabela ser trocada, o slide passa a
alegar rigor de três sementes exibindo números de uma.** É o pior dos dois
mundos, e vem de uma tarefa bem-intencionada.

Duas ressalvas do meu lado, para não inflar o achado: (a) o "em parte dos
braços" da l.466 subestima — a tabela inteira é de uma semente, não parte
dela; (b) eu **não** estou dizendo que a defesa está errada de propósito:
ela foi montada quando aquela pasta era o dado que existia, e o próprio
autor mandou refazer a semente 42 no regime canônico em 16/08.

# O que eu NÃO fiz

Não toquei em nenhum dos dois arquivos: a defesa é do autor e o A4 não é
minha superfície. Também **não** tenho os valores corretos para o A4 — a
tabela dele tem coluna de `% pool` e recorte próprio, e quem a refizer
precisa decidir se troca para os 27 braços homogêneos (números no meu aviso
0638) ou para a varredura mista. Essa é decisão de quem escreve, não minha.

**Meu limite, sempre:** sem LaTeX neste contêiner — não olhei nenhuma das
duas páginas compostas, só o fonte e os artefatos.
