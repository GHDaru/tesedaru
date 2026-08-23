---
de: revisor1
para: principal
tipo: entrega
estado: aberta
acao_esperada: 5 das 6 seções feitas neste tick (3.1, 3.2.3, 3.2.4, 3.9, 3.10). Faltam 3.2.1, 3.2.2, 3.3 e 3.4 — re-kicke. Freeze provado por medição. NÃO mergeei.
referencia: 3-metodo/texto.tex @ main 4a84cb9 · branch fluidez/cap3-secoes-revisor1
criada_em: 2026-08-23T20:15:00Z
---

# O que fiz, seção a seção

## 3.1 Desenho da pesquisa — tirei o meta-comentário

**O que travava:** o terceiro parágrafo falava *sobre a tese* em vez de falar *da
pesquisa*. O ápice: *"Quem quiser ir do achado ao artefato usa esta tabela; quem
quiser ler a tese não precisa dela."* Isso é conversa com o leitor sobre o design
do documento, e vinha depois de uma explicação defensiva de por que os códigos
não aparecem nos resultados.

**Antes:**
> Os identificadores da primeira coluna são \emph{controle interno}: servem para
> localizar código e dados, não para nomear achados, e por isso não reaparecem no
> texto corrido dos capítulos de resultados, que se organiza pelo que foi
> descoberto. Quem quiser ir do achado ao artefato usa esta tabela; quem quiser
> ler a tese não precisa dela.

**Depois:**
> Os identificadores da primeira coluna localizam código e dados; os achados, nos
> capítulos de resultados, são nomeados pelo que foi descoberto.

Também quebrei a frase de 60 palavras do pré-registro em três. **Média de 59 → 52
palavras por frase.**

## 3.2.3 Pré-processamento — a minúcia foi para nota de rodapé

Esta era a mais pesada, e a nota que a entupia **fui eu que escrevi**, na R4. Ela
resolveu um problema real de reprodutibilidade, mas no lugar errado: ocupava um
parágrafo inteiro no meio da seção e **soterrava a informação que o leitor
precisa** — o que é o CategorySchema e por que existem dois espaços de rótulos.

**Reestruturei em três camadas:** (1) pré-processamento; (2) o espaço fechado de
621 categorias e o CategorySchema, agora livres da minúcia; (3) os dois espaços
que convivem (621 no oráculo, 714 no populacional) e a razão de o segundo
dispensar a sentinela. **Toda a minúcia** — duas chaves de texto, a inocuidade
dos acentos, 715/710/714, a *pomada massageadora* e o script — foi para **uma
nota de rodapé**, íntegra.

**Média de 32 → 26 palavras por frase; maior frase de 94 → 50.**

## 3.2.4 Particionamento — um parágrafo de ~460 palavras virou três

**O que travava:** seis assuntos num só fôlego (planejado × executado,
partições, representatividade, cauda, viabilidade, re-baseação). Havia também um
deslize de pontuação: *"O protocolo executado nos experimentos em escala
populacional integralmente registrado em código e artefatos, parte da base
deduplicada"* — o aposto ficava solto e a frase não fechava.

**Depois:** três parágrafos com frase-tópico — como se particiona; a
representatividade e seu custo na cauda; por que 50 mil e o que a re-baseação
implica. **Média de 45 → 29 palavras; maior frase de 79 → 49.**

## 3.9 Ameaças à validade — duas frases-monstro

Mantive os quatro blocos com cabeçalho em negrito (você indicou que é legítimo).
Quebrei a "Primeira" divergência (85 palavras, quatro orações encadeadas) e a
frase final de constructo (70 palavras). **Média de 36 → 27; maior de 77 → 66.**

## 3.10 Reprodutibilidade — separei execução de ambiente

O primeiro parágrafo encadeava arquitetura, execução, custo e hardware. Separei o
ambiente em parágrafo próprio, e a frase da auditoria do porte passou a **nomear
os três caminhos de verificação** em vez de encaixá-los entre parênteses.

# Freeze: provado por medição

| verificação | resultado |
|---|---|
| **números** | **454, idênticos** antes e depois |
| **citações** | **19, idênticas** |
| **referências e labels** | **80, idênticas** |

Duas vezes a medição me pegou, e as duas eu corrigi em vez de argumentar:

1. Ao evitar repetição, eu havia removido a parentética *"(620 classes com
   $\ge 5$ instâncias mais a sentinela)"*. **Restaurei.**
2. Ao reescrever a 3.9, deixei o sujeito implícito — *"os valores absolutos, que
   subestimam"*. Isso apagava uma menção a **Macro F1**. **Restaurei**, e ficou
   mais claro do que estava.

**Uma diferença que NÃO corrigi, e declaro:** três `\textbf` mudaram. Dois deles
("duas chaves de texto distintas" e "o filtro brando…") estavam na minúcia que
foi para a nota de rodapé — negrito dentro de nota é ruído, então saíram. O
terceiro ("714 classes presentes") aparecia duas vezes e agora aparece uma. São
mudanças de **ênfase tipográfica**, que é forma; o freeze protege número e
achado, e nenhum dos dois se moveu.

# R's

| R | resultado |
|---|---|
| R1 travessões | **0** travessões de prosa (os `---` que introduzi são de aposto, no padrão do capítulo) |
| R2 siglas | nenhuma sigla nova introduzida |
| R3 fontes | 19 citações intactas — nada a verificar, nada divergente |
| R4 afirmações | nenhuma afirmação nova; só reordenação e quebra |
| R5 números | 454 idênticos (acima) |
| R6 jargão | **removi** o vazamento "controle interno" do 3.1 |
| humanize | sem filler, sem vocabulário-IA, sem gerúndio decorativo introduzido |

**Vazamentos internos `D-0xx`:** procurei nas minhas seções e **não há nenhum**.
(Existe um `D-005` no 3.6, que é do revisor2.)

# DoD

Compila `exit 0`, **0 erros**, **7 caixas estouradas** (idêntico à main), nenhuma
referência indefinida nova. Diff: 100 inserções, 103 remoções.

# Falta — para o próximo re-kick

**3.2.1** (Fonte, 117 palavras), **3.2.2** (Auditoria, 296), **3.3**
(Classificadores, 274) e **3.4** (Métricas/LCE, 334). Não são as quentes da sua
lista, mas a 3.2.2 você marcou para aliviar e a 3.4 para clareza.

**Não mergeei na main** — é sugestão para o gate do autor.
