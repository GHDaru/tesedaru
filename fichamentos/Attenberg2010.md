---
id: Attenberg2010
title: "Why Label when you can Search? Alternatives to Active Learning for Applying Human Resources to Build Classification Models Under Extreme Class Imbalance"
authors: ["Attenberg, Josh", "Provost, Foster"]
year: 2010
venue: "KDD 2010, pp. 423-432"
doi: "10.1145/1835804.1835859"
pdf: referencias-pdf/Attenberg2010.pdf
paper_type: metodo
pillars: [p1-selecao]
status: fichado
proposes: [aprendizado-guiado, busca-por-exemplos, estrategia-hibrida-busca-rotulagem]
uses_methods: [aprendizado-ativo, amostragem-por-incerteza, pool-based]
datasets: [safe-adult, safe-guns, open-directory-project]
metrics: [acuracia]
tasks: [classificacao-binaria, classificacao-de-texto]
falco_relation:
  - type: ameaca
    target: amostragem-por-incerteza
    note: "Mostra empiricamente o limite da família por incerteza sob desbalanceamento
           extremo: quando a classe rara é rara o bastante, o problema dominante deixa
           de ser achar a instância informativa e passa a ser ACHAR a instância da
           classe minoritária. Sustenta as duas passagens do Cap. 2 sobre a seleção
           por incerteza se concentrar na fronteira das majoritárias."
  - type: complementa
    target: FALCO
    note: "A saída deles é humana (buscar em vez de rotular). A do FALCO é outra —
           oráculo LLM barato o bastante para cobrir mais do pool —, mas o
           diagnóstico é o mesmo: sob cauda longa, cobertura vale mais que
           refinamento de fronteira."
---

# Why Label when you can Search? (Attenberg & Provost, KDD 2010)

## Resumo
Sob desbalanceamento extremo, rotular o que o modelo acha informativo é a
estratégia errada: não há exemplos positivos suficientes para o modelo saber o
que é informativo. Os autores comparam **rotular** (aprendizado ativo) com
**buscar** (aprendizado guiado: a pessoa procura ativamente exemplos de cada
classe, com um buscador) e mostram que, sob assimetria severa, até a busca
mais simples domina claramente a seleção ativa. Como nem sempre buscar é
barato, avaliam o trade-off de custo relativo entre buscar e rotular e propõem
uma **estratégia híbrida** que combina as duas — melhor que qualquer uma pura
quando a escolha não é óbvia. O domínio é publicidade segura: identificar
páginas com conteúdo que anunciantes não querem ao lado do seu anúncio.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | "o problema dominante nesses domínios é simplesmente **encontrar exemplos da classe minoritária**, não encontrar exemplos 'informativos' ou próximos da fronteira de classificação" | §1, p. 2 | 2.1 e 2.4 — é o lastro exato das duas citações da tese |
| C2 | Sob assimetria extrema, o aprendizado guiado "domina completamente" as estratégias ativas para aplicar esforço humano | Abstract, p. 1; Fig. 2 | 2.1 — limite da família por incerteza |
| C3 | A estratégia **híbrida** (busca + rotulagem ativa) supera as duas puras quando o custo relativo torna a escolha ambígua | Abstract, p. 1; §5 | Cap. 6 — desenho possível de trabalho futuro |
| C4 | Em publicidade segura, a taxa base da classe minoritária vai de 1/10⁴ a 1/10⁷ ou menos; com filtros, "geralmente abaixo de 1/10²" | §2, p. 2 | limite de escopo: é MUITO mais extremo que a cauda da tese |

## Números que posso citar
- Assimetria dos conjuntos: **Safe-Adult ≈ 20:1**; **Safe-Guns ≈ 150:1**
  (§4, p. 5); os outros três vêm de um rastreamento de ≈ **4.000.000 de URLs**
  do Open Directory Project.
- Taxa base da minoria no domínio real: **1/10⁴ a 1/10⁷** (§2, p. 2).

## Citações diretas (com página)
> "This result shows that the dominant problem in these domains is simply
> finding minority-class examples, not finding otherwise 'informative' examples
> or examples near the classification boundary." (p. 2)

## VERIFICAÇÃO DAS DUAS PASSAGENS DA TESE — as duas BATEM
Medido contra a fonte, porque citação de limitação é onde a banca cutuca:
1. Cap. 2, família por incerteza: "pode negligenciar classes raras ao
   concentrar-se na fronteira das majoritárias" — **bate** com C1/C2.
2. Cap. 2, condições do domínio: "o desbalanceamento interage com a seleção por
   incerteza, que tende a concentrar-se nas fronteiras das classes
   majoritárias" — **bate** com C1.
Nada a corrigir. Registro explicitamente porque o silêncio sobre o que está
certo faz parecer que só há erro no capítulo.

## O que esta obra NÃO sustenta
1. **Não é multiclasse.** É binária (classe minoritária × resto). As 714
   classes da tese não estão no regime analisado.
2. **Não fala de LLM nem de oráculo automático.** O "recurso humano" é humano:
   pessoas rotulando ou pesquisando.
3. **A assimetria é ordens de grandeza maior** que a da tese (1/10⁴ a 1/10⁷).
   Usar a obra para dizer "o mesmo vale aqui" seria exagero; ela sustenta o
   MECANISMO (incerteza ignora o raro), não a magnitude.
4. **Não mede texto curto.** São páginas web, não títulos de produto.

## Ideias que gera para a tese
1. **Cobertura × refinamento.** O achado central (achar o raro vale mais que
   refinar a fronteira) é o argumento mais forte a favor do desenho do FALCO:
   um oráculo barato cobre mais pool, e cobertura é o que a cauda precisa.
   Vale dizer isso explicitamente no Cap. 6.
2. **A híbrida tem paralelo direto** na progressão de fases: barato para
   cobrir, caro para decidir. C3 é o antecedente empírico disso.
