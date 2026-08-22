---
de: revisor2
para: principal
tipo: entrega
acao_esperada: LEVAR AO AUTOR — tarefa 1700 respondida com evidência de código. **(2) A resposta é (a): o framework executou entropia mesmo**, e a divergência é mais branda do que parece, porque o E1 **não testa margem contra entropia** — elege por estimativa pontual. **(3) São DUAS constantes diferentes**, e a boa notícia é que a comparação favorece a tese. Proposta de redação nos dois casos
referencia: tarefa 1700 · R4 do revisor1 (itens 2 e 3) · `activelearning@origin/main:src/activelearning/application/run_falco.py` · `experiments/e1e4/results/analysis.json` · 5-resultados:281-290 · Apêndice A7
criada_em: 2026-08-22T16:08:00Z
---

Fui ao código do ciclo real, que é onde a pergunta se resolve.

# (2) Fase 2 usa entropia — e usa mesmo. A saída é a **(a)**

**O que o framework executou, medido no código.** Em
`src/activelearning/application/run_falco.py`, o laço da Fase 2 (l.153-163)
chama, a cada lote:

```
chosen_local = select_top_k(entropy_scores(probs), k)
```

e a Fase 3 (l.172) chama o mesmo. O import na l.24 é `entropy_scores`, e não
há nenhuma outra estratégia importada no arquivo. O docstring já anunciava:
*"Fase 2 (incerteza + oráculo Inicial): lotes por **entropia preditiva**"*.
**Não é (b): o Cap.3 não está com a palavra errada — o método usou entropia
de fato.**

**Mas a divergência é mais fraca do que a R4 sugere, e isto muda a redação
necessária.** Fui ao artefato do E1
(`experiments/e1e4/results/analysis.json`) ver **quais testes existem**. Cada
estratégia tem exatamente dois: `wilcoxon_vs_random_lce_p` e
`wilcoxon_vs_random_final_macro_f1_p`. **Não há teste algum de margem contra
entropia.** O E1 testa cada estratégia **contra a aleatória** — e nessa
comparação a entropia vence, com o mesmo $p=0{,}0078$ das demais.

Então "o E1 elege menor margem/menor confiança" é leitura de **estimativa
pontual**, não eleição medida:

| estratégia | LCE | Macro F1 final |
|---|---|---|
| menor margem | $0{,}528 \pm 0{,}013$ | $0{,}418 \pm 0{,}013$ |
| menor confiança | $0{,}518 \pm 0{,}010$ | $\mathbf{0{,}421 \pm 0{,}009}$ |
| **entropia** | $0{,}493 \pm 0{,}006$ | $0{,}398 \pm 0{,}008$ |

A distância é grande frente à dispersão (3 a 5 desvios), então um Wilcoxon
pareado provavelmente daria significativo — **mas ele não foi rodado**, e a
tese não pode afirmar o que não mediu.

**(c) não se sustenta:** as duas medem a mesma coisa (ranking do pool a cada
lote), então não é ranking global × por lote.

**Proposta de redação.** Trocar a alegação de lastro por uma declaração de
escolha com ressalva medida: *"A Fase 2 seleciona por entropia. A varredura
do E1 (Seção~\ref{sec:res-e1}) mostra que, com o classificador leve, menor
margem e menor confiança apresentam estimativas pontuais superiores à
entropia, sem que o desenho tenha testado essas estratégias entre si — a
comparação medida ali é de cada uma contra a aleatória, e a entropia a supera
com a mesma significância. A troca da estratégia da Fase 2 fica como extensão
imediata."* Isso conserta o único problema real — o Cap.3 dizer que a escolha
é *justificada* pela varredura, quando a varredura não testou essa
comparação.

# (3) São duas constantes diferentes, e a comparação **favorece** a tese

**De onde vem cada número, medido:**

- **$\varepsilon = 10^{-3}$** é `stagnation_eps`, parâmetro do
  `run_falco.py` (l.76, valor padrão `1e-3`). O uso é a l.161:
  `if val_f1 > best_val + stagnation_eps: best_val, stagnant = val_f1, 0`.
  Ou seja: **quanto de melhora em Macro F1 de validação conta como progresso
  e zera o contador de estagnação**. É uma **tolerância de convergência**.
- **$1/\sqrt{n_V} = 0{,}0224$** (com $n_V = 2.000$) é a **escala de ruído
  amostral** da medição na validação. É um **piso de significância**, não
  uma tolerância.

**Não são a mesma constante com valores incompatíveis: são grandezas
distintas que o texto encosta uma na outra.** O A7 usa a segunda para
justificar a primeira, e é aí que nasce o fator 22.

**E o fator 22 diz algo relevante, na direção certa.** Como $10^{-3}$ está
**22 vezes abaixo** do ruído, o critério é **permissivo**: quase qualquer
flutuação para cima zera o contador, o que **adia** a parada. Se a tolerância
fosse do tamanho do ruído (0,0224), o laço teria parado **antes**.

Isso é bom para a tese: a configuração executada parou em 11.936 rótulos
**apesar de** um critério frouxo. A parada precoce, que é o diagnóstico
central do Cap.5, **não é artefato de tolerância apertada** — pelo
contrário, sobreviveu à tolerância mais generosa possível.

**Proposta de redação.** Separar as duas no texto e usar a comparação como
argumento, não como justificativa: *"A tolerância de estagnação é
$\varepsilon = 10^{-3}$ em Macro F1 de validação (parâmetro
`stagnation_eps`). Ela não deriva do limite amostral $1/\sqrt{n_V} =
0{,}0224$: é deliberadamente **duas ordens de grandeza menor**, de modo que a
parada só ocorre após $p$ iterações sem qualquer ganho, e não por o ganho ser
pequeno demais para se distinguir do ruído. A parada observada no ciclo real,
portanto, não é efeito de uma tolerância estrita."*

Se o autor preferir alinhar a tolerância ao ruído, isso **muda o
comportamento do laço** e exigiria reexecução — não é troca de redação. Por
isso recomendo a separação, e não o alinhamento.

**O que eu NÃO fiz:** não editei texto, como a tarefa pediu. E não rodei o
Wilcoxon margem×entropia que falta — se o autor quiser transformar a
estimativa pontual em eleição medida, isso é experimento novo (os artefatos
por semente existem; é barato), e eu não abro experimento por conta própria.
