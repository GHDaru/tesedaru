# Parecer simulado R5 — orientador e banca (pós-fechamento do programa experimental)

Data: 19/07/2026. Estado avaliado: **programa experimental completo**. Desde o
R4 (18/07, média 85,7) fecharam-se: reescrita do Cap. 2, ablação DRI-SL-C,
campanha de 8 sementes do E6 (inferencial), E3′ com varredura de orçamento
(hipótese central respondida), auditoria dos experimentos legados, DOI da base
integrado, biblioteca validada como pip-instalável, e o catálogo executável de
experimentos na interface. Complementa e substitui o parecer v2 (R4).

## 1. Avaliação R5 (academic-paper-reviewer, modo re-review final)

| Dimensão (peso) | R3 | R4 | **R5** | Movimento R4→R5 |
|---|---|---|---|---|
| Originalidade (20%) | 82 | 84 | **86** | E3′ com varredura de orçamento + "menos é mais" no transformer (E35 > régua) fecham um achado próprio e memorável; DRI-SL-C e viés de autoavaliação consolidados |
| Rigor metodológico (25%) | 86 | 87 | **90** | hipótese central agora TESTADA e respondida com pré-registro honrado; E6 inferencial (8 sementes, Wilcoxon); auditoria de proveniência dupla verificada por cruzamento automático |
| Suficiência de evidência (25%) | 84 | 86 | **89** | programa completo: nenhum pilar em aberto; o E3′ que faltava foi executado e a varredura mediu os pisos de orçamento |
| Coerência argumentativa (15%) | 85 | 84 | **88** | Cap. 2 reestruturado (5 seções, 2 níveis); a narrativa fecha em "refutada em 30%, sustentada em 50%, causa identificada" — arco completo |
| Apresentação (15%) | 85 | 88 | **89** | booktabs, tabela de lacunas, resumo respondendo (Minto); tese 84 pp. compila limpa (0 erros/0 refs) |
| **Média ponderada** | 84,5 | 85,7 | **88,4** |

**Decisão: APROVAÇÃO com revisões menores (defensável).** Nenhum bloqueante
científico permanece — o que era o bloqueante do R4 (bloco H / BERTimbau na
GPU) foi resolvido pela execução do E3′ em CPU com desenho enxuto. Os itens
abertos são operacionais/editoriais, listados em §4.

## 2. Na voz do orientador

Gilsiley, o trabalho mudou de patamar desde ontem, e por um motivo específico:
**a hipótese central deixou de ser uma promessa.** No R4 eu dizia "a tese
termina formalmente aberta até o E3"; agora ela termina com um número testado.
E o número é o melhor tipo de resultado — não o "deu certo" ingênuo, mas o
"deu certo sob condições que eu medi e sei explicar". A sequência
refutada-em-30% → sustentada-em-50% → causa-identificada (a parada, não o
oráculo) → 70% supera a régua completa é exatamente a maturidade de pesquisa
que a banca de doutorado procura. Três recomendações:

**a) Mova o "menos é mais" para o resumo e para a defesa oral.** O achado de
que 35 mil rótulos ativamente selecionados superam os 50 mil completos, tanto
no leve (E6) quanto no forte (E3′), é o resultado mais contraintuitivo e mais
citável da tese. Ele merece uma frase no resumo (já está) e um slide próprio
na defesa.

**b) A varredura de orçamento é a resposta à pergunta "e daí?".** Quando a
banca perguntar qual a recomendação prática, a resposta é uma linha: "rotule
metade do pool com seleção por incerteza e pare — mais que isso desperdiça, e
rotular tudo piora". Isso é um resultado de engenharia, não só de ciência.

**c) Escreva a proveniência dupla no Cap. 3.** É o único ponto onde a banca
pode se confundir: quais números vêm do repositório legado
(activetextclassification) e quais da biblioteca nova (activelearning). O
Cap. 4 já diz, mas uma frase no Cap. 3 blinda a questão (ação editorial em §4).

## 3. Na voz da banca (arguições prováveis e onde a tese responde)

**Metodologia**: "O senhor refutou a hipótese e depois a sustentou mudando o
orçamento — isso não é mover a trave?" → *Resposta: não. O critério (≥95% da
supervisão, ≤30%) foi pré-registrado e a refutação em 30% está reportada como
refutação. A varredura NÃO altera o critério; ela mede em que orçamento o
critério passaria a valer, o que é uma pergunta de desenho distinta e
declarada. O piso de 50% é um resultado, não um critério reescrito.*

**AL / escala**: "A saturação de 8.000 do E6 é robusta?" → *RESPONDIDA: 8
sementes, 9,1k±0,6k; entropia vence o aleatório em 8/8 (Wilcoxon p=0,0078).*

**Estatística**: "O E3′ é semente única." → *Verdade, e declarado. As
comparações são amparadas pelos IC de Wilson na população (n=20k) e pelo
pareamento na mesma amostra; a varredura mostra a tendência monotônica que
uma semente isolada não explicaria por acaso. Extensão natural: repetir os
braços-fronteira (E20/E25) com sementes.*

**Aplicações**: "Como isso vira produto?" → *O FALCO rodou ponta a ponta a
custo zero de oráculo (E5), a interface reproduz/reprisa cada experimento, e
a biblioteca é pip-instalável — o caminho da pesquisa ao uso está demonstrado,
não prometido.*

## 4. Pendências para a versão de depósito (não-científicas)

| Item | Tipo | Responsável | Esforço |
|---|---|---|---|
| Frase de proveniência dupla no Cap. 3 | editorial | eu, sob seu OK | 10 min |
| Licença explícita da base no Kaggle (CC BY 4.0 recomendada) | decisão | autor | 5 min |
| Rotação das 5 chaves de API | segurança | autor | 15 min |
| Autoria/ordem dos 5 artigos | decisão | autor + orientador | conversa |
| Proofreading final PT + revisão de inglês dos artigos | editorial | autor/ferramenta | — |
| Figura de arquitetura do A4 (obrigatória p/ ESWA) | editorial | eu | 30 min |
| Porte do runner P2 para a biblioteca nova (opcional; artefato legado já verificado) | engenharia | eu | 1–2 h |
| DOI Zenodo do código (fecha artefatos do A1/A5) | operacional | autor + eu | 30 min |

## 5. Veredito

A tese está **cientificamente completa e defensável**. A média R5 (88,4)
coloca-a na faixa de aprovação confortável, e o salto desde o R4 (+2,7) vem
inteiramente do fechamento do programa experimental — não de retórica. O
diferencial competitivo permanece o mesmo, agora consumado: nenhum número sem
artefato rastreável, e agora com a interface que torna essa rastreabilidade
clicável. Recomendo agendar a pré-defesa com o orientador assim que os itens
editoriais de §4 (todos ≤30 min) estiverem fechados.
