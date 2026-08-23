---
de: revisor2
para: principal
tipo: entrega
acao_esperada: LEVAR AO AUTOR os dois quadros abaixo, para ele escolher o regime vendo tabela final. Não editei nenhum .tex, como a tarefa pediu. O LaTeX das duas tabelas no regime canônico vai pronto no §5, para colar SE ele escolher canônico
referencia: tarefa 20260820-2020 (item 1) · artefatos e3prime_{D,E35,E30,E25,E20,E}_s{7,42,123}.json e legacy_s42_bs16_eval20k/ em activelearning@origin/main
criada_em: 2026-08-20T20:50
---

Entregue o item 1. O item 2 (cruzada da divisão da banca) fica para quando a branch
dividida aparecer — ela ainda não está na main.

# 1. A diferença entre os dois regimes, em uma frase

O mesmo experimento foi avaliado em dois conjuntos de teste de tamanhos muito
diferentes: **20.092 instâncias** no regime antigo e **177.490** no canônico (a
população reservada inteira). O campo `eval_n` está gravado em cada arquivo, então não há
ambiguidade sobre qual é qual. Avaliar na população inteira derruba o Macro F1 de todos
os braços, porque entram as classes de cauda que o recorte de 20 mil quase não continha —
mas derruba **também a régua**, e é por isso que o veredito não se move na direção óbvia.

# 2. Quadro I — a tabela dos braços (`tab:e3p`)

| braço | rótulos | regime antigo (`eval_n`=20.092, 1 semente) | regime canônico (`eval_n`=177.490, 3 sementes) |
|---|---|---|---|
| A (*pipeline* real, oráculo) | 8.937 | acc 0,6585 · F1 0,2424 | **não medido** |
| B (mesmos itens, gabarito) | 8.937 | acc 0,7023 · F1 0,2092 | **não medido** |
| C (aleatório, gabarito) | 8.937 | acc 0,7316 · F1 0,1888 | **não medido** |
| D (régua: *pool* inteiro) | 50.000 | acc 0,8831 · F1 0,4509 | acc 0,8675±0,0021 · F1 0,3684±0,0091 |

**O buraco, declarado:** A, B e C **não têm número canônico**. Estão bloqueados esperando
o `annotation_cache_nemotron.jsonl` como dataset do Kaggle. Como a decomposição inteira do
Cap. 5 (ruído do oráculo = A−B; valor da seleção = B−C) vive nesses três braços, **no
regime canônico hoje não se pode afirmar nem que a hipótese foi atendida nem que foi
refutada na configuração executada**: falta o numerador. Qualquer veredito canônico
enunciado agora seria parcial, e é preciso dizer isso no texto.

# 3. Quadro II — a varredura de orçamento (`tab:e3p-sweep`)

Critério = $0{,}95 \times$ régua. No canônico: **F1 ≥ 0,3500** e **acc ≥ 0,8241**.
No antigo: F1 ≥ 0,4284 e acc ≥ 0,8389.

| braço | rótulos | % base | % *pool* | ANTIGO acc | ANTIGO F1 | CANÔNICO acc (±dp) | CANÔNICO F1 (±dp) |
|---|---|---|---|---|---|---|---|
| E | 15.000 | 6,48% | 30% | 0,8314 ❌ | 0,3801 ❌ | 0,6966 ±0,0061 ❌ | 0,2016 ±0,0094 ❌ |
| E20 | 20.000 | 8,64% | 40% | 0,8592 ✅ | 0,4181 ❌ | 0,7748 ±0,0068 ❌ | 0,2533 ±0,0118 ❌ |
| **E25** | **25.000** | **10,80%** | **50%** | **0,8729 ✅** | **0,4335 ✅** | **0,8281 ±0,0046 ✅** | **0,3061 ±0,0074 ❌** |
| E30 | 30.000 | 12,96% | 60% | 0,8774 ✅ | 0,4562 ✅ | 0,8439 ±0,0042 ✅ | 0,3233 ±0,0006 ❌ |
| **E35** | **35.000** | **15,12%** | **70%** | **0,8860 ✅** | **0,4627 ✅** | **0,8610 ±0,0040 ✅** | **0,3520 ±0,0121 ✅ (por +0,0021)** |
| D (régua) | 50.000 | 21,60% | 100% | 0,8831 | 0,4509 | 0,8675 ±0,0021 | 0,3684 ±0,0091 |

## O que muda, em uma linha

**O piso da métrica da hipótese (Macro F1) sai de 25.000 e vai para 35.000 rótulos** — de
**10,80%** da base, folgado dentro do teto de 15%, para **15,12%**, que são **276 rótulos
fora** do teto de 34.724. Em acurácia o piso sai de 20 mil e vai para 25 mil, e continua
dentro do teto.

# 4. O E35 cruza no limiar — e não cruza em todas as sementes

Cada semente tem a sua própria régua, porque D também varia. Conferindo semente a semente:

| semente | D (F1) | critério | E35 (F1) | Macro F1 | acurácia |
|---|---|---|---|---|---|
| 7 | 0,3771 | 0,3582 | 0,3440 | ❌ **não cruza** (−0,0142) | ✅ (E35, E30, E25 cruzam) |
| 42 | 0,3691 | 0,3506 | 0,3660 | ✅ (+0,0154) | ✅ (E35, E30) |
| 123 | 0,3590 | 0,3410 | 0,3461 | ✅ (+0,0051) | ✅ (E35, E30, E25) |

Na média cruza por **+0,0021**, contra um desvio próprio de **±0,0121** — isto é, a folga
é seis vezes menor que a dispersão entre sementes. **Nenhuma redação deve descrever isso
como "o E35 cumpre o critério" sem a qualificação "em 2 das 3 sementes, no limiar".**

# 5. Uma diferença de qualidade, independente do veredito

Vale registrar para a decisão não se reduzir a "qual regime dá a resposta que eu prefiro":

- O regime **antigo tem uma semente só** (s42). O intervalo `[87,9; 88,8]` que hoje aparece
  no Cap. 5 é um intervalo de Wilson — incerteza de amostragem **dentro de uma execução** —,
  não dispersão entre sementes. Ele não diz nada sobre reprodutibilidade.
- O regime **canônico tem três sementes**, com desvio real medido entre elas, e avalia na
  população que a tese declara.

Ou seja: o regime canônico é metodologicamente superior por razões que nada têm a ver com
o resultado — e é justamente por isso que trocar de regime **não** pode ser lido como
escolher o número mais conveniente. É o argumento que protege o autor na defesa, e é
verdadeiro nos dois sentidos: o canônico é melhor **e** dá o resultado mais duro.

# 6. As duas tabelas em LaTeX, prontas para colar SE o autor escolher canônico

Não apliquei — a tarefa pediu quadro, não edição, e `5-resultados-falco/texto.tex` está
em disputa entre a branch da banca e a do revisor1.

```latex
% tab:e3p — braços, regime canônico (eval 177.490, média±dp de 3 sementes)
\begin{tabular}{l l r r r}
\toprule
\textbf{Braço} & \textbf{Fonte} & \textbf{Rótulos} & \textbf{Acurácia} & \textbf{Macro F1} \\
\midrule
A & \textit{pipeline} real, oráculo & 8.937 & \multicolumn{2}{c}{\emph{sem medição canônica}} \\
B & mesmos itens, gabarito         & 8.937 & \multicolumn{2}{c}{\emph{sem medição canônica}} \\
C & aleatório, gabarito            & 8.937 & \multicolumn{2}{c}{\emph{sem medição canônica}} \\
D & \emph{pool} inteiro (régua)    & 50.000 & $0{,}8675 \pm 0{,}0021$ & $0{,}3684 \pm 0{,}0091$ \\
\bottomrule
\end{tabular}

% tab:e3p-sweep — varredura, regime canônico
\begin{tabular}{l r r r r r cc}
\toprule
\textbf{Braço} & \textbf{Rótulos} & \textbf{\% base} & \textbf{\% \textit{pool}} &
\textbf{Acurácia} & \textbf{Macro F1} & \textbf{Critério} \\
\midrule
E    & 15.000 & 6,5\%  & 30\%  & $0{,}6966 \pm 0{,}0061$ & $0{,}2016 \pm 0{,}0094$ & acc~\xmark~F1~\xmark \\
E20  & 20.000 & 8,6\%  & 40\%  & $0{,}7748 \pm 0{,}0068$ & $0{,}2533 \pm 0{,}0118$ & acc~\xmark~F1~\xmark \\
E25  & 25.000 & 10,8\% & 50\%  & $0{,}8281 \pm 0{,}0046$ & $0{,}3061 \pm 0{,}0074$ & acc~\cmark~F1~\xmark \\
E30  & 30.000 & 13,0\% & 60\%  & $0{,}8439 \pm 0{,}0042$ & $0{,}3233 \pm 0{,}0006$ & acc~\cmark~F1~\xmark \\
E35  & 35.000 & 15,1\% & 70\%  & $0{,}8610 \pm 0{,}0040$ & $0{,}3520 \pm 0{,}0121$ & acc~\cmark~F1~\cmark$^{\dagger}$ \\
\midrule
D    & 50.000 & 21,6\% & 100\% & $0{,}8675 \pm 0{,}0021$ & $0{,}3684 \pm 0{,}0091$ & --- \\
\bottomrule
\end{tabular}
% Critério: 0,95 x régua (D) = acurácia >= 0,8241 e Macro F1 >= 0,3500, na média das 3 sementes.
% dagger: o E35 cruza o critério de Macro F1 em 2 das 3 sementes, e na média por 0,0021 —
% folga menor que o desvio entre sementes (+-0,0121). Fica no limiar.
```

# 7. Como fica o Cap. 5 em cada escolha (para o autor decidir de olhos abertos)

- **Regime antigo (como está hoje).** O piso da métrica é 25 mil (10,8% da base), dentro do
  teto; a hipótese é atendida com folga; o E35 supera a supervisão completa. Custo: uma
  semente só, avaliação em 20.092 quando a tese declara população de 177.490, e a banca
  pode perguntar por que o denominador da avaliação não é o declarado.
- **Regime canônico.** O piso da métrica é 35 mil (15,12%), 276 rótulos fora do teto, e
  cruza em 2 de 3 sementes. A hipótese, na métrica que a define, **não é atendida dentro
  do teto** — e a decomposição do Cap. 5 fica sem A, B e C até o cache destravar. Custo:
  o veredito endurece. Ganho: três sementes, dispersão real, denominador coerente com o
  resto da tese, e nenhuma pergunta sobre régua conveniente.

Não recomendo qual escolher: é decisão do autor sobre o que a tese reporta. Recomendo
apenas que a escolha seja **declarada no texto**, com o regime nomeado e o `eval_n` dito,
em vez de silenciosa — é a diferença entre uma decisão metodológica e uma trave móvel.

Evidência: 18 arquivos `e3prime_{D,E35,E30,E25,E20,E}_s{7,42,123}.json` (todos com
`eval_n` = 177490) e 9 em `legacy_s42_bs16_eval20k/` (`n_eval` = 20092), em
`activelearning@origin/main`. Médias, desvios e critérios recalculados por mim a partir
desses arquivos; conferem com o registro do plano (`plano-revisao.json`, id
`e3p-seed42-canonico`) linha a linha.
