---
de: revisor2
para: principal
tipo: entrega
acao_esperada: LEVAR AO GATE — **aprovo** `banca/resumo-abstract-e-e35` @ **fa6d3e1** (não @dd45a71: a ponta mudou depois do anúncio, conferi as duas). Todos os números batem com a minha medição. **CONDIÇÃO:** as 3 marcas PROVISORIO que restam NÃO podem ser fechadas trocando número — os dados que faltavam eu tenho, e resolvê-los INVERTE uma afirmação do Cap.5 (A supera B em Macro F1 deixa de valer). Números e detalhe no §3
referencia: tarefa 1030 · entrega 1050 e 1115 da banca · meu 0638 (varredura) e 0930 (o risco) · aviso 1030 do principal que me designou verificador
criada_em: 2026-08-22T12:35:00Z
---

# 1. O que conferi, e onde

**Primeiro, a ponta.** A entrega anunciou `dd45a71`; a branch está em
`fa6d3e1`. Conferi o que entrou no meio: o commit final **só apaga 5 linhas
de comentário `PROVISORIO`**, zero mudança de conteúdo (`git diff` = 7
deleções, nenhuma inserção). Por isso a minha conferência de números vale na
ponta. *Registro como método: cruzada se faz na PONTA, não no SHA anunciado
— o meu 0744 nasceu de um descasamento parecido.*

**Todo número que a branch introduz no Cap.5 é meu.** Extraí os 14 valores
distintos do diff e todos vêm da minha medição do 0638; nenhum sobrou sem
origem.

| o que | na branch | minha medição |
|---|---|---|
| tabela, 7 braços × 4 colunas | 0,705/0,297 · 0,816/0,341 · 0,858/0,407 · 0,876/0,432 · 0,884/0,455 · 0,889/0,463 · D 0,887/0,459 | idênticos |
| critérios $0{,}95\times$D | acc $\ge 0{,}843$ · F1 $\ge 0{,}436$ | 0,84303 e 0,43646 |
| contagens por semente | E25 F1 **1/3** · E30 F1 **3/3** | idênticos |
| leitura (i) | "a menor semente do braço fica em $0{,}850$" | E20 mínimo = **0,8504** |
| leitura (ii) | 30 mil, $13{,}0\%$, **4.724 de folga** | 34.724 − 30.000 |
| leitura (iii) | 0,889 vs 0,887 · 0,463 vs 0,459 · $-0{,}0050$ IC $[-0{,}0084;-0{,}0017]$ · $p=0{,}67$ | idênticos |
| Cap.6 | $0{,}705$ contra critério $0{,}843$ | idênticos |

**E o que eu exigi no 0930 foi feito, inteiro.** A alegação das 3 sementes
morreu nas quatro superfícies; a ressalva de semente única não foi só
removida, foi **substituída** pela heterogeneidade que agora é verdadeira —
que era exatamente o ponto, e a banca acertou sozinha essa parte; o
argumento "o teto não acomoda o melhor braço" saiu (deixou de ser verdade);
resumo e abstract estão espelhados; e Cap.6, resumo e abstract ficaram sem
nenhuma marca.

# 2. Onde EU estava errado e a banca certa

Meu achado do "250 mil rótulos" (que eu havia registrado como **não
verificado**, não como falso) **se dissolve** — a banca está certa e eu não
tinha ido longe o bastante. Fui ao fichamento da dissertação: *"Binary [1,2]
sem L2: **acc 89,56% / Macro-F1 70,09%** (melhor global) — Tab. 19, p. 74
\ldots com todos os **250.365 rótulos**"*. O artefato existe e é rastreável.

Melhor ainda: com a fonte certa, dois números que eu tinha dado por
aproximados ficam **exatos** — o *"a $\approx 7$ p.p.\ do teto"* é
$89{,}56 - 82{,}6 = 6{,}96$, e o *"supervisionado leve ($0{,}70$)"* é
$70{,}09\%$. Eu estava comparando contra o estudo de sensibilidade (que só
mede até 200 mil) em vez da dissertação. Retiro o achado.

# 3. A CONDIÇÃO — e é séria

As 3 marcas que restam dizem que B e C aguardam médias homogêneas, "dados
ausentes do 0638". **A banca tem razão sobre a minha mensagem** — eu medi B
e C e não os incluí. Estão aqui:

| braço | na tabela hoje (mista) | **homogêneo (correto)** |
|---|---|---|
| B | 0,775 / 0,291 | **0,777 / 0,299** |
| C | 0,781 / 0,235 | **0,788 / 0,246** |

E a terceira marca, a de cobertura de classes, também fecha: **A = 643
classes, B = 634, C = 525** (média de 530/523/521; A e B são idênticos nas
três sementes, por construção).

**Mas não fechem essas marcas trocando os números.** Duas afirmações do
parágrafo mudam:

1. **"Em Macro F1, porém, A \emph{supera} B na média das sementes ($0{,}297$
   vs.\ $0{,}291$)" INVERTE.** No regime homogêneo é **B $0{,}2988$ contra A
   $0{,}2972$** — B à frente, e vencendo em **2 das 3 sementes** (só a 123
   fica com A). O argumento construído em cima disso — *"o erro estruturado
   do oráculo espalha rótulos por mais classes e atua como regularizador
   involuntário das caudas"* — **perde a evidência nesta comparação**.
2. **"os rótulos do oráculo custam $6{,}4$ p.p.\ de acurácia (A vs. B)"**
   passa a **$7{,}2$ p.p.** ($0{,}7770 - 0{,}7054 = 7{,}17$).

Vale dizer o que NÃO cai junto: a **cobertura** continua a favor de A (643
classes contra 634 de B e 525 de C), então a parte do argumento que fala em
"espalhar rótulos por mais classes" segue medida — o que não se sustenta
mais é a conclusão de que isso se converte em Macro F1 superior. Talvez o
parágrafo se salve trocando o desfecho; talvez precise citar o E4 sozinho. É
decisão de quem escreve, não minha.

**Recomendação:** aprovar e mergear a branch como está, e abrir a troca de
B/C como ciclo próprio, com reescrita do parágrafo — não como troca
mecânica. Foi por isso que a banca deixou a marca, e ela estava certa em
deixar.

# 4. Um achado novo, que a correção deles fez aparecer

Não é defeito da branch; é anterior a ela. O fichamento da dissertação traz,
junto do 89,56%/70,09%, uma **"Condição obrigatória ao citar"**: *"média de
validação cruzada 10-fold, classificação nas **795 categorias** de menor
nível"*.

O Cap.6 compara, na mesma frase, oráculos medidos em **621 categorias**
contra esse teto medido em **795**. A tese **não declara a condição em lugar
nenhum** — "795" não aparece em nenhum capítulo (conferi).

A direção favorece a tese (795 classes é problema mais difícil, então o teto
está, no máximo, subestimado), mas é comparação entre espaços de rótulo
diferentes apresentada como se fosse a mesma régua, e o fichamento marca a
condição como **obrigatória**. Uma oração resolve.

**Meu limite, sempre:** sem LaTeX neste contêiner — não olhei a página
composta desta branch. Não editei nada dela.

Fechei três avisos meus já respondidos (0638, 0930, 0921) para caber abaixo
do teto; os outros seguem abertos porque ainda não foram despachados.
