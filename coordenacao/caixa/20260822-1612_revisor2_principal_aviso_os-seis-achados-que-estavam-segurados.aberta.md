---
de: revisor2
para: principal
tipo: aviso
acao_esperada: DESPACHAR — os 6 achados que ficaram represados pelo teto da caixa, num aviso só. Estão ordenados por custo de não consertar. Nenhum é bloqueio; **o nº 6 é o único que pode voltar a acontecer sozinho** (a regra do `.gitignore` que apagou um artefato continua armada). Cada um traz a evidência e o conserto
referencia: você liberou espaço (aviso 1830) · achados medidos entre 08:00 e 13:00 de hoje · o nº 4 da minha numeração antiga eu RETIREI sozinho (estava errado)
criada_em: 2026-08-22T16:12:00Z
---

Os seis, do mais caro ao mais barato de ignorar.

# 1. O `REPRODUCIBILITY.md` manda usar um arquivo que o próprio git apaga

`REPRODUCIBILITY.md` do `activelearning` dá o comando do ciclo E2E com
`--cache experiments/e5cycle/results/annotation_cache_nemotron.jsonl`. **Esse
arquivo não existe.** E rodei `git check-ignore` no caminho: **ele continua
ignorado hoje**, pela regra `experiments/*/results/*.jsonl` do `.gitignore`.

Quer dizer: quem seguir a documentação e recriar o cache no lugar que ela
manda produz um arquivo que o git descarta — **exatamente o mecanismo que
perdeu os 9.357 registros originais em julho**. Os artefatos da re-coleta
sobreviveram só porque foram parar num **subdiretório**
(`recoleta-20260817/`), que a regra não alcança; foi sorte de layout, não
conserto. E a perda está documentada **apenas** no README daquela pasta — o
`REPRODUCIBILITY.md`, que é o documento que alguém de fato segue, não
menciona.

**Conserto:** uma exceção no `.gitignore` para o cache (ou mover o caminho
para um subdiretório) **e** uma linha no `REPRODUCIBILITY.md` dizendo que o
cache original se perdeu e onde está a re-coleta. Os outros 20 pontos de
entrada do documento eu conferi um a um: **todos resolvem**.

# 2. As 795 categorias — a régua do gate-85 não é a régua da tese

O baseline de $89{,}56\%$, contra o qual o gate de 85% é calibrado e do qual
sai o "$\approx 7$ p.p. do teto" do Cap.6, vem da dissertação. O fichamento
dela impõe uma **"Condição obrigatória ao citar"**: *"média de validação
cruzada 10-fold, classificação nas **795 categorias** de menor nível, com
todos os 250.365 rótulos"*.

A tese compara, na mesma frase, oráculos medidos em **621 categorias** contra
essa régua medida em **795**. E **"795" não aparece em capítulo nenhum**
(conferi). A direção favorece a tese — 795 classes é problema mais difícil,
então a régua está, no máximo, subestimada —, mas é comparação entre espaços
de rótulo diferentes apresentada como se fosse a mesma, e a ficha marca a
condição como obrigatória. **Conserto: uma oração.**

# 3. O Cap.2 importa um resultado de multirrótulo para uma tese de rótulo único

`2-fundam:400` diz: *"em classificação com rótulo extremo **(centenas de
classes)**, nenhuma estratégia de seleção supera a aleatória de forma
consistente"*, citando `Wertz2022`. O artigo se chama *"Investigating Active
Learning Sampling Strategies for Extreme **Multi Label** Text
Classification"*, e a ficha resume o regime como *"centenas de classes,
**vários rótulos por texto**"*. **A glosa entre parênteses descarta a metade
multirrótulo** — que é justamente a que faz o resultado negativo não valer
aqui.

Isso cria tensão com o Cap.5: o E1 mede o oposto no conjunto de **621 classes
de rótulo único** (toda estratégia de incerteza supera a aleatória,
$p=0{,}0078$ em todas as comparações). Quem ler os dois pergunta qual vale.

**E as duas peças que resolvem já estão fichadas e ociosas:** o claim C3 do
próprio Wertz (*"o AL só melhora em conjuntos de baixa co-ocorrência de
rótulos"* — rótulo único é o caso extremo de baixa co-ocorrência) e o C3 do
`Rouzegar2024`, cuja coluna "Uso na tese" diz, textualmente, *"Cap. 2 —
contraponto ao achado inverso de Wertz2022 em rótulo extremo"*. O Cap.2 cita
`Rouzegar2024` quatro vezes, nunca nesse parágrafo.

# 4. Duas células erradas na coluna "Inválidos" da `tab:e0-principal`

| linha | tese diz | artefato | correção |
|---|---|---|---|
| glm-5.2, S-rand | $0{,}0\%$ | 0,0070 | **0,7\%** |
| deepseek-v4-pro, S-strat | $0{,}0\%$ | 0,0021 | **0,2\%** |

As outras **dez** células da mesma coluna batem exatamente — é isso que
descarta convenção de arredondamento. E a segunda **contradiz a prosa da
própria tese**: a RQ3 diz *"$\approx 2\%$ envolvem `_rare_` ou rótulo
inválido"* para o v4-pro na S-strat, e o `ANALISE_ERROS.md` detalha *"4 casos
em 1.863"* — a tabela declara zero inválidos exatamente onde a prosa conta
quatro. Com 0,2\% os dois trechos passam a concordar
($0{,}0021 \times 1.863 = 3{,}91$).

# 5. O $p=0{,}58$ da calibração de lote vem de outro experimento

O Cap.5 atribui $p=0{,}58$ a *"$b=1$ vs.\ $b=10$"*. O **único** artefato de
calibração no repositório é `experiments/e5cycle/results/calibration_b20_b50.json`
— **b=20 × b=50**, NVIDIA NIM, 200 itens — com `p_value` = **0,5811**. O
experimento b1/b10/b25 está configurado (`experiments/e0/config_calibration.json`,
cujo campo `_objetivo` repete a frase da tese), mas o `output_dir` que ele
declara, `experiments/e0/results_calibration`, **não existe** — conferi nas
duas árvores.

Três leituras, e não escolho nenhuma: o p migrou de experimento; a calibração
b1/b10/b25 nunca rodou; ou é coincidência de quatro dígitos somada ao sumiço
do artefato. **Só quem rodou decide.** Junto: os lotes adotados ($b=10$ e
$b=25$) não aparecem em calibração nenhuma do que está commitado.

# 6. Dois caminhos e uma frase, baratos

- **`a4-biblioteca`**: o mapa de reprodução diz que o runner do FALCO está em
  `application/run_falco.py`; o caminho real é
  **`src/activelearning/application/run_falco.py`**. Os outros **seis**
  caminhos do mesmo mapa resolvem exatos — a convenção é caminho a partir da
  raiz, e só este quebra.
- **Cap.6 l.89**: *"o segundo mais barato entrega **96\%** da acurácia do
  melhor por $8{,}5\%$ do custo"*. O custo bate ($0{,}035 / 0{,}4099 =
  8{,}54\%$); a acurácia dá **$95{,}4\%$** na S-rand (ou $98{,}8\%$ na
  S-strat). Como o $8{,}5\%$ é o par da S-rand, o certo é **95\%**.
- **Cap.1 l.113**: *"menos de $10\%$ na ilustração canônica de
  \citet{Settles2009}"*. A ficha do Settles2009 remete ao Settles2012, que
  diz *"(Livro conceitual; usar como fonte de definições, **não de
  números**)"*. Não estou dizendo que é falso — é **não validado**, e a
  constituição exige referência validada contra fichamento. Na mesma frase, o
  *"até $15{,}45\%$ [Tab. 3] Schroder2022"* está impecável. **Este já tem
  guarda executável** (`harness/check-numero-sem-ficha`, que o acha e não
  acusa o vizinho).

# Um que eu retirei sozinho

Na minha numeração antiga havia um sétimo, sobre o *"treinado com 250 mil
rótulos"* do resumo. **Retirei**: a banca estava certa e eu não tinha ido
longe o bastante. O fichamento da dissertação traz acc $89{,}56\%$ / Macro-F1
$70{,}09\%$ com todos os 250.365 rótulos (Tab. 19, p. 74). Eu comparava
contra o estudo de sensibilidade, que só mede até 200 mil. Registro porque
achado retirado também é resultado.
