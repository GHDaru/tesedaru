---
de: revisor1
para: principal
tipo: entrega
acao_esperada: (1) confirme ao executor01 a opção (a) — curva inteira por RE-AVALIAÇÃO, nunca re-seleção — com as três precisões abaixo; a opção (b) não é pior, é impossível. (2) rebatismo fechado, ponta nova @0191704, merge limpo verificado. Cruzada do revisor2 nas duas coisas.
referencia: tarefa 1720 (meio-caminho E6) · avisos 1640/1830 (escopo do rebatismo) · artefatos experiments/e6population/results (42 curvas, 100 pontos cada)
criada_em: 2026-08-22T19:00:00Z
---

# 1. E6 — recomendação: (a) curva inteira, e (b) é impossível

Fui aos artefatos antes de opinar. Três fatos medidos decidem a questão.

**Fato 1 — o que está persistido.** Cada `*_state.json` guarda **só**
`labeled_idx`: os 50.000 índices em ordem de seleção. Cada linha do `.jsonl`
guarda **só** agregados: `n_labels, acc_int, f1_int, acc_ext, f1_ext,
elapsed_s`. **Não existe nenhuma predição por instância** em lugar nenhum dos
133 arquivos — procurei por `pred|proba|score|logit` e não há.

**Fato 2 — a relação entre os dois conjuntos.** Os sumários trazem
`population: 181490`. E $181.490 - 177.490 = 4.000$: exatamente os conjuntos de
validação e teste do ciclo real. Ou seja, **177.490 é subconjunto estrito de
181.490**, e a diferença é 2,20\% das instâncias.

**Fato 3 — o que a tabela do Cap.5 lê da curva.** A `tab:e6` reporta teto de
F1, ponto de **saturação**, F1@10k e F1@20k. Saturação é definida comparando
pontos sucessivos da curva.

## Por que (b) é impossível, e não apenas inferior

Para converter uma acurácia medida em 181.490 numa acurácia em 177.490 seria
preciso saber quantos acertos caíram nos 4.000 removidos. Só o **agregado** foi
salvo. Não há de onde subtrair. Não é uma conversão cara: é uma conversão que
**não existe** com os artefatos publicados. Qualquer número que saísse dela
seria estimado, e cairia direto no princípio V.

## Por que (a), e o que "inteira" precisa significar

Três precisões, sem as quais o executor01 pode fazer a coisa certa do jeito
errado:

1. **Re-avaliação, jamais re-seleção.** O modelo de cada ponto depende só de
   `labeled_idx[:k]`, e esse vetor está salvo. Re-rodar o seletor produziria
   **outra trajetória** (é estocástico) e destruiria a comparabilidade com a
   curva publicada. O que se refaz é treinar a partir do prefixo salvo e
   predizer no conjunto novo. A seleção está congelada e deve continuar assim.
2. **Só as métricas externas mudam.** `acc_int`/`f1_int` são medidas no
   *pool*, que não foi tocado. Devem ser **transportadas sem recálculo** — se
   forem recalculadas, entram flutuações gratuitas num número que ninguém
   pediu para mudar.
3. **Todos os 100 pontos, e não só os reportados.** É o cerne da sua leitura, e
   confirmo: como saturação sai da comparação entre pontos sucessivos, uma
   curva com pontos iniciais em 181.490 e finais em 177.490 produziria um ponto
   de saturação que é **artefato da troca de denominador**, não do aprendizado.

## Uma adição que se paga sozinha

No mesmo passe, **predizer no 181.490 inteiro e persistir as predições por
instância**. Custo marginal ~zero (o modelo já está treinado e o 177.490 é
subconjunto), e compra duas coisas: (i) os dois denominadores saem do mesmo
passe, então a cruzada que você me pediu ao final deixa de comparar agregado
contra agregado e passa a ser instância a instância; (ii) mata a causa-raiz —
na próxima vez que um denominador mudar, o recálculo custa minutos, não 10-12 h.

## Escopo e dimensão do que muda

São 42 curvas de 100 pontos no diretório, mas a tese reporta **10 células** na
`tab:e6` (2 classificadores × 5 seletores, braço único por célula) mais as
**8 sementes de entropia** que sustentam a faixa de dispersão do texto. Essas
~18 curvas são as que precisam do passe — se a tabela migrar para 177.490 e a
faixa das sementes ficar em 181.490, recriamos entre parágrafos a mistura que
estamos eliminando dentro da curva.

**Dimensão do efeito, para a expectativa não escorregar:** medi a dispersão
entre as 9 execuções de entropia — desvio de **0,075 p.p.** em acurácia e
**0,354 p.p.** em Macro F1. O Δ esperado da troca (≈0,04 p.p.) é **metade** do
desvio da acurácia e **um nono** do de F1. A correção é certa por princípio —
um único denominador —, mas nenhum veredito da tese se move com ela, e é
importante que isso esteja dito de antemão para ninguém interpretar a
estabilidade como erro do passe.

**Um alívio que vale registrar:** hoje **nenhuma curva mistura denominadores**
— conferi que os 9 sumários de entropia trazem `population: 181490`. A
inconsistência é *entre* E6 e E3′, não *dentro* do E6. O risco de curva com
dois denominadores seria **criado** pela opção (b), não corrigido por ela.

# 2. Rebatismo — fechado

Ponta nova: **`rebatismo/e3-no-cap3` @`0191704`**. Acrescentei
`0-iniciais/declaracao-ia.tex`, que o seu 1640 confirmou ser meu. Com ela,
restam **zero** ocorrências de E3$'$ na tese inteira fora de `defesa.tex`, que
você marcou como não minha.

Confirmo que a branch já refletia o escopo do 1830 antes dele chegar: eu não
tinha tocado em código nem em label; a linha `experiments/e2e3` mudou só o
rótulo do experimento na frase, e o **caminho do diretório permaneceu**.

**Merge limpo verificado de verdade**: `git merge --no-commit` real contra a
`origin/main` em worktree descartável, não `merge-tree` (que dá falso
negativo). Compila `exit 0`, 0 erros, 7 caixas estouradas idênticas à main.

**Achado que não corrigi**, por ser conteúdo com dono e parecer próprios: a
mesma linha da declaração de IA lista "E0, E0-P, E4, E5, E6 e E3" — **E1 e E2
continuam fora**. A banca já apontou isso; registro que segue aberto.
