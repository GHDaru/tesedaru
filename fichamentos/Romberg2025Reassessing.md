---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Romberg2025Reassessing
title: "Reassessing Active Learning Adoption in Contemporary NLP: A Community Survey"
authors: ["Romberg, Julia", "Schröder, Christopher", "Gonsior, Julius", "Tomanek, Katrin", "Olsson, Fredrik"]
year: 2026
venue: "Proceedings of EACL 2026 (Long Papers), p. 2621-2647 (preprint arXiv:2503.09701)"
doi: "10.18653/v1/2026.eacl-long.120"
pdf: referencias-pdf/Romberg2025Reassessing.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: avaliacao
pillars: [P1, P4]
status: fichado

# ===== ENTIDADES =====
proposes: []
uses_methods: [aprendizado-ativo, pesquisa-de-comunidade]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: []

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Lewis1994]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: motiva
    target: FALCO
    note: "Sustenta a afirmação de 2-fundam:785-789 sobre as barreiras práticas
           à adoção do aprendizado ativo — e sustenta com números, não só
           qualitativamente. As três barreiras que a tese lista (complexidade de
           implantação, incerteza sobre redução de custo, ferramental) são
           exatamente as três do resumo do artigo. A leitura que a tese
           acrescenta ('a viabilidade operacional, não a acurácia, é o
           obstáculo') é inferência nossa, mas os números a sustentam na
           proporção de cerca de 2 para 1 — ver claim C3."
  - type: fundamenta
    target: LCE
    note: "Dá base externa para a tese instrumentar CUSTO como dimensão de
           primeira classe: a segunda barreira mais citada é justamente a
           incerteza sobre a redução real de custo, e o artigo mostra que ela
           persiste há mais de quinze anos sem ser resolvida pela literatura."
---

# Reassessing Active Learning Adoption in Contemporary NLP: A Community Survey

## Resumo (5-8 linhas, com as MINHAS palavras)
Pesquisa de comunidade com 144 participantes da área de PLN sobre o uso
**prático** — não experimental — do aprendizado ativo, deliberadamente
construída para comparar com a pesquisa equivalente de Tomanek e Olsson de
2009. A pergunta de fundo é incômoda: a literatura acumulou ganhos
consideráveis, sobretudo depois dos LLMs, mas isso chegou a quem anota dados no
mundo real? A resposta é que a anotação segue sendo gargalo, o aprendizado
ativo segue sendo considerado relevante, e **as mesmas três barreiras de quinze
anos atrás continuam de pé**: complexidade de montagem, incerteza sobre a
redução de custo e ferramental. O artigo propõe estratégias de mitigação para
cada uma.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Três desafios persistem, os mesmos de quinze anos atrás: complexidade de montagem, incerteza sobre redução de custo e ferramental | Resumo, p. 1 ("three key challenges yet persist—setup complexity, uncertain cost reduction, and tooling") e §1 | 2-fundam:785-789 — é a frase que esta ficha valida |
| C2 | Em 2009 apenas 20% dos praticantes haviam implementado AA, e as barreiras eram ceticismo sobre a efetividade prática e o custo de construir interfaces de anotação | §1, p. 1-2 (citando Olsson 2009) | Cap. 2 e Cap. 6: mostra que a barreira é estrutural, não conjuntural |
| C3 | Entre quem NÃO usa AA, as barreiras operacionais dominam as de desempenho: custo de implantação 37% e falta ou desconhecimento de ferramenta 32%, contra 14% que duvidam da efetividade e 12% que apontam dificuldade de estimar o ganho a priori | §3, p. 5 (bloco II.5) | **É o número que sustenta a leitura da tese**: operacional ≈ 69 pontos contra ≈ 26 de desempenho |
| C4 | A rejeição de fato é quase nula: 54% de quem nunca usou consideraria usar, 38% está apenas incerto por falta de conhecimento, e apenas UM participante recusaria explicitamente | §3, p. 5 (bloco II.8) | Cap. 6: o problema não é convencer, é viabilizar |
| C5 | Projetos recentes com AA foram considerados bem-sucedidos em 91% dos casos e efetivos em 67%, contra 57% de sucesso nos projetos sem AA | §3.4 | Cap. 6: evidência de que a barreira é de adoção, não de resultado |

## Números que posso citar
Condições: pesquisa de comunidade, **144 participantes**, maioria da academia,
área de linguística computacional; questionário com desvio condicional (perguntas
puladas conforme elegibilidade); comparação explícita com a pesquisa de Tomanek
e Olsson (2009).

- **Barreiras entre quem não usa AA** (§3, bloco II.5): custo de implantação
  **37%** · ausência ou desconhecimento de ferramenta adequada **32%** ·
  viés de amostragem **18%** · dúvida sobre a efetividade em si **14%** ·
  dificuldade de estimar a efetividade a priori **12%** · inadequação ao
  requisito do projeto **9%**.
- **Disposição futura** (§3, II.7-II.8): **54%** de quem não usou consideraria
  usar; **38%** incerto por falta de conhecimento; **1** participante recusaria
  explicitamente; **4** condicionariam às circunstâncias.
- **Sucesso percebido** (§3.4): projetos recentes com AA — **91%** bem-sucedidos,
  **67%** efetivos; projetos sem AA — **57%**.
- **Linha de base histórica** (§1): em 2009, **20%** dos praticantes haviam
  implementado AA.

## Citações diretas (com página)
> "Consistent with a community survey from over 15 years ago, three key
> challenges yet persist—setup complexity, uncertain cost reduction, and
> tooling—for which we propose alleviation strategies." (Resumo, p. 1)

> "key barriers to AL adoption from over a decade ago still persist, demanding
> greater emphasis on reducing the complexity of setup, ensuring cost
> reduction, and improving annotation tools." (§1, p. 2)

## Crítica / limitações (minha leitura)
- **Autosseleção**: quem responde a uma pesquisa sobre aprendizado ativo tende
  a ser quem já se interessa por aprendizado ativo. Os 144 não são amostra
  aleatória da área, e o próprio artigo se declara descritivo. Citar como
  retrato de uma comunidade interessada, não como estimativa populacional.
- **Maioria acadêmica**, o que provavelmente subestima as barreiras de
  indústria — justamente onde o custo de anotação morde mais.
- **Percepção, não medição**: "sucesso" e "efetividade" são auto-relatados. O
  91% do C5 é percepção de sucesso, não desempenho medido. Não misturar com
  números de F1 em nenhuma tabela da tese.
- Os dois coautores da pesquisa de 2009 (Tomanek e Olsson) assinam esta. Isso
  dá continuidade metodológica e, ao mesmo tempo, é fonte de expectativa —
  vale notar que a conclusão confirma a pesquisa anterior deles.

## Onde a tese o usa, e o que confere
A frase de `2-fundam:785-789` diz:

> "A pesquisa de comunidade de \citet{Romberg2025Reassessing} acrescenta o
> alerta prático: complexidade de implantação, incerteza sobre a redução real
> de custo e ferramental inadequado seguem sendo as barreiras à adoção — a
> viabilidade operacional, não a acurácia, é o obstáculo apontado."

**As três barreiras conferem termo a termo** com o resumo do artigo, e o
"seguem sendo" conferе com "yet persist" e com a comparação explícita com 2009.

**A oração final é inferência da tese, não do artigo** — o artigo não escreve
"viabilidade operacional, não acurácia". Mas os números do C3 a sustentam: as
barreiras operacionais somam cerca de 69 pontos percentuais (37 de implantação
mais 32 de ferramental) contra cerca de 26 das relacionadas a desempenho (14 de
dúvida sobre efetividade mais 12 de dificuldade de estimá-la). É uma inferência
bem apoiada, e ficaria ainda melhor com o número no corpo do texto em vez do
adjetivo.

## Ideias que gera para a tese
- **Trocar o qualitativo pelo quantitativo no Cap. 2**: em vez de afirmar que a
  viabilidade operacional é o obstáculo, dar os 37% e os 32% contra os 14%. O
  argumento passa de leitura a medida, que é o que o princípio V premia.
- **Enquadramento do Cap. 6**: o C4 mostra que a resistência de fato é quase
  nula — um único participante em 144 recusaria usar. Ou seja, o FALCO não
  precisa convencer ninguém de que aprendizado ativo vale a pena; precisa
  remover as três barreiras. Isso reposiciona a contribuição da tese de
  "provar que funciona" para "tornar praticável", que é uma tese mais honesta
  e mais defensável.
- **Fechar o argumento de custo**: a segunda barreira mais citada é a incerteza
  sobre a redução real de custo, e é exatamente o que a instrumentação de custo
  do FALCO ataca. Vale citar aqui, e não só na revisão, quando o Cap. 3
  justificar por que o custo é medido em vez de estimado.
