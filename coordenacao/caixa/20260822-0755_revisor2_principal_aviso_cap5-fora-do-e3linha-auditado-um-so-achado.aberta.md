---
de: revisor2
para: principal
tipo: aviso
acao_esperada: REGISTRAR (não urgente) e juntar ao bloco de gate — auditei o Cap.5 fora do E3′ contra os artefatos: 86 valores conferidos, 86 batem. Um único achado, de prosa: a frase "metade ou um quarto do que a seleção aleatória exige" não tem apoio na própria tabela que ela cita — é metade nos dois casos. Correção pronta abaixo, de uma palavra
referencia: 5-resultados-falco/texto.tex tab:e1 (l.258), tab:e4 (l.312), tab:e6 (l.419) · experiments/e1e4/results/analysis.json e experiments/e6population/results/ na MAIN do activelearning · este aviso JUNTA quatro frentes limpas num só, por causa do limite de 10 mensagens abertas do PROTOCOLO
criada_em: 2026-08-22T07:55:00Z
---

Segui rastreando enquanto os ciclos vinham vazios. Esta é a auditoria do
Cap.5 **fora** do E3′ — que é a parte do capítulo que a regeração de hoje
**não** toca, e que portanto pode ser lida como estável.

# O achado, e é só um

Seção do E6, logo abaixo da Tabela~\ref{tab:e6}:

> *"a entropia domina em escala: satura a 95\% do teto com 8.000 rótulos no
> SGD (19.000 no PVBin), **metade ou um quarto** do que a seleção aleatória
> exige"*

**É metade nos dois casos, e não um quarto em nenhum.** Da própria tabela:

| classificador | entropia | aleatório | razão |
|---|---|---|---|
| SGD   | 8.000  | 16.500 | **2,06×** |
| PVBin | 19.000 | 40.000 | **2,11×** |

Procurei um par que justificasse "um quarto" e não existe: contra o DRI-SL
(41.500 no SGD) a razão é 5,2×, não 4×. A correção é trocar *"metade ou um
quarto"* por *"cerca de metade nos dois classificadores"* — e o número fica
até mais bonito, porque 2,06 e 2,11 são praticamente o mesmo fator em dois
classificadores diferentes, o que é um resultado mais forte do que um
intervalo vago.

Não é erro de conta nem de dado: a tabela está certa, é a frase que
generaliza além dela.

# O que conferi, e bate: 86 valores

**`tab:e1` (E1, estratégias com oráculo perfeito)** — 20 valores contra
`experiments/e1e4/results/analysis.json`. Média e desvio das 8 sementes, nas
5 estratégias, em LCE e F1 final: todos exatos (ex.: menor margem
$0{,}528 \pm 0{,}013$ ← 0,528 / 0,0127; aleatória $0{,}444 \pm 0{,}011$ ←
0,4439 / 0,011). Mais: a ablação de lote (0,492 / 0,493 / 0,481 para
$b=50/100/200$) bate; o *"recupera 78\% do Macro F1 do teto"* dá 78,1%
(0,4214 sobre o teto 0,5398); e o *"menor $p$ atingível é 0,0078"* está
certo — com $n=8$, Wilcoxon bicaudal não desce de $2/2^8 = 0{,}0078125$.

**`tab:e4` (E4, robustez ao ruído)** — 20 valores. Os três níveis de ruído,
duas estratégias, F1 final e retenção: exatos (ex.: $\varepsilon=0{,}4$
entropia $0{,}215 \pm 0{,}010$ e retenção 54,1% ← 0,215 / 0,0098 / 0,5407).

**`tab:e6` (E6, escala populacional)** — 40 valores. Oito braços × quatro
colunas contra `experiments/e6population/results/analysis.json`: exatos.

Os dois braços de *"Estratif. por predição"* **não estão** no `analysis.json`
— então não me contentei com o resumo: **recalculei os quatro valores de cada
um a partir da curva bruta** (`popcurve_<clf>_drisl-cs.jsonl`, 100 pontos),
aplicando a definição que a própria legenda dá (teto = máximo da curva;
saturação = menor $|L|$ que atinge 95% do teto). Deu 0,5551 / 10.000 /
0,5329 / 0,5427 no SGD e 0,5276 / 18.000 / 0,4442 / 0,4984 no PVBin —
exatamente as oito células publicadas.

**A afirmação mais forte do E6 também bate, e na vírgula:** *"no SGD, o Macro
F1 atinge $0{,}59$ com $\approx 15$ mil rótulos e cai para $0{,}44$ quando o
pool inteiro é rotulado"*. Na curva, o pico é **0,5907 em $|L|=15.500$** e o
último ponto, com 50.000 rótulos, é **0,4400**. "Rotular tudo pode piorar"
está sustentado com precisão.

# Uma diferença de arredondamento, não é erro

Na linha PVBin/entropia, F1@20k é 0,5085 no artefato e $0{,}509$ na tese.
Arredondamento meio-para-cima, correto. Anoto só para quem for reconferir
com script não tropeçar: o Python arredonda 0,5085 para 0,508.

# O que isto delimita

Junto com o meu 0744, o quadro dos capítulos de resultado fica assim: **o
Cap.5 fora do E3′ está verificado contra artefato e tem um ajuste de uma
palavra**; o E3′ é o que a regeração de hoje muda (aviso 0638); e o Cap.4
tem a divergência entre duas tabelas (aviso 0744) mais o resto limpo.

**Meu limite, sempre:** sem LaTeX neste contêiner — nada disto olha a página
composta. Não editei capítulo nenhum.
