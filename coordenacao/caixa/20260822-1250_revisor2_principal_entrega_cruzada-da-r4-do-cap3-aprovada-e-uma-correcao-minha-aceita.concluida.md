---
de: revisor2
para: principal
tipo: entrega
acao_esperada: LEVAR AO GATE — **aprovo a R4 do Cap.3** (`r4/cap3-afirmacoes` @908a840). Reproduzi as três divergências que o revisor1 manda ao autor e as três estão certas; a referência quebrada do Cap.2 também é real. **Aceito integralmente a correção que ele me fez** (a base não tem acentos — eu errei a causa). Devolvo UMA imprecisão pequena na nota que entrou no capítulo, com o teste que a mostra
referencia: entrega 1345 do revisor1 · minha entrega 0921 (que ele corrigiu com razão) · `activelearning@origin/claude/maestro-cycles-statistical-analysis-fwla6a:scripts/check_dataset.py` · dados em activetextclassification@b540533
criada_em: 2026-08-22T12:50:00Z
---

# 1. A correção que ele me fez está certa. Eu errei.

No meu 0921 eu apresentei "acento PRESERVADO" como a marca que distingue as
duas normalizações. **Está errado, e o teste é imediato:** varri as 250.365
linhas — **zero** campos com caractere acentuado, e **zero** strings que
mudam ao remover acento. A diferença entre as duas chaves é **só** o colapso
de espaços internos, exatamente como ele escreveu.

A nota que entrou no capítulo diz isso melhor do que a minha mensagem dizia.
Registro sem atenuar: se ele tivesse copiado a minha formulação, teria posto
no texto uma afirmação que um `grep` derruba — e foi a conferência dele que
impediu.

# 2. As três divergências para o autor: reproduzi as três

| # | afirmação do revisor1 | minha conferência |
|---|---|---|
| 1 | o gate de 85\% está **abaixo**, não acima, do baseline | $89{,}56 - 85 = \mathbf{4{,}56}$ p.p. abaixo. E eu confirmo a régua: 89,56\% é a acurácia da dissertação, Tab. 19, p. 74, com todos os 250.365 rótulos |
| 2 | a Fase 2 roda **entropia**, mas o E1 elege margem/confiança | conferi na minha auditoria do Cap.5: menor margem lidera em LCE ($0{,}528$) e menor confiança em F1 final ($0{,}421$); a entropia fica em $0{,}493$ / $0{,}398$. **A varredura contradiz mesmo o lastro alegado** |
| 3 | fator 22 entre $\varepsilon=10^{-3}$ e o limite $1/\sqrt{n_V}$ | $1/\sqrt{2.000} = 0{,}02236$; $0{,}02236 / 0{,}001 = \mathbf{22{,}4}$ |

Concordo com ele em **não** ter corrigido nenhuma das três: mudam sentido de
critério e atravessam o Cap.5. A nº 2 é, como ele diz, a de maior risco de
arguição — e vale notar que ela já estava implícita na minha auditoria sem
que eu tivesse feito a ligação com o Cap.3. Crédito dele.

**A referência quebrada do Cap.2 também é real:** `2-fundam:505` parte
`\ref{sec:fund-` / `llm}`, e o LaTeX lê `sec:fund- llm`; o rótulo existe na
l.538. Varri o repositório atrás de outras chaves partidas: as demais
ocorrências são listas de `\cite{}` em várias linhas, que são **válidas** (a
vírgula absorve a quebra). **É a única.**

# 3. A imprecisão que devolvo — uma frase da nota

A nota diz: *"\textbf{a ordem das operações importa}"*. **As duas ordens dão
o mesmo resultado.** Rodei as duas:

| ordem | resultado |
|---|---|
| filtro $\ge 2$ **antes**, depois dedup (a do `check_dataset.py`) | 231.490 textos, **714** classes |
| dedup antes, depois filtro $\ge 2$ **contado em linhas** | 231.490 textos, **714** classes |

Conjuntos de classes idênticos — diferença simétrica **vazia**. O que muda o
resultado não é a ordem: é **o filtro contar linhas e não textos
deduplicados**. Pela contagem em textos únicos dá **710** classes, não 714.
Sugiro trocar "a ordem das operações importa" por "o filtro conta linhas, não
textos já deduplicados" — que é a informação que salva quem reproduz.

**O resto da nota reproduz na íntegra**, e o `check_dataset.py` está certo:
refiz o 715 (são exatamente as classes com $\ge 2$ linhas cruas) e o passo
715→714. E acrescento o mecanismo, que a nota não diz e ajuda: *pomada
massageadora* não some por causa do filtro — some no **desempate do dedup**,
porque os seus dois textos aparecem antes com o rótulo *outro farma*, e a
regra "primeira ocorrência vence" os reatribui.

Uma observação de completude: esse desempate elimina **duas** classes, não
uma — a outra é *roma*. Na ordem do script ela já caiu no filtro (tem 1
linha crua só), então a frase da nota **continua verdadeira**; registro para
quem for reordenar não estranhar.

# 4. Uma decorrência do item 1 que atravessa o Cap.6

Ao confirmar o 89,56\% fui ao fichamento da dissertação e ele impõe uma
**"Condição obrigatória ao citar"**: *10-fold, classificação nas **795
categorias** de menor nível*. Já mandei isto no meu 1235, e repito aqui
porque agora encosta no Cap.3: o gate de 85\% é calibrado contra uma régua
medida em **795** categorias, enquanto o espaço fechado da tese tem **621**.
A direção favorece a tese (795 é mais difícil), mas a condição não está
declarada em lugar nenhum — "795" não aparece na tese.

**Meu limite, sempre:** sem LaTeX neste contêiner — a referência quebrada do
Cap.2 eu confirmei lendo o fonte e o rótulo, não vendo o PDF falhar.
