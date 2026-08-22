---
de: principal
para: banca
tipo: tarefa
acao_esperada: DECISÃO ESTRUTURAL DO AUTOR — reenunciar o critério da hipótese contra a BASE DEDUPLICADA, com teto de 15%, e resolver a proveniência do critério; entregar como pacote de prosa com antes/depois para o gate do autor
referencia: decisão do autor 2026-08-18 · medição do principal (tabela de saturação) · dec-politica-parada (curva completa) · 1-intro:88-100 · 3-metodo:190-201
criada_em: 2026-08-18T01:45:00Z
---

# Reenunciar a hipótese: denominador é a base, teto é 15%

Decisão do autor, em três partes. Esta é a mudança de maior alcance
conceitual do dia — mexe no que a tese AFIRMA, não em como afirma.

## (1) O denominador muda: pool 50k → base deduplicada (231.490)

O autor: *"devemos declarar a tese referenciando os 200 mil e não os 50 mil,
que foi escolha deliberada e não justificada"*. Hoje o critério diz "30% dos
exemplos do pool" (1-intro:96) — e o pool de 50 mil é justificado por
**viabilidade computacional** (3-metodo:195), não por mérito metodológico.
Medir a economia contra um denominador escolhido por conveniência é
exatamente o que a arguição ataca.

## (2) O teto passa a ser 15% DA BASE — e a proveniência importa

O autor declarou: *"este foi quando nasceu minha hipótese anos atrás. Se
conseguimos mais, ótimo."*

Números que você precisa ter na mão (medidos por mim):
- 15% da base = **34.724 rótulos** = 69% do pool;
- o orçamento executado (30% do pool) = 15.000 = **6,5% da base**;
- ou seja: **a execução foi mais restritiva que o critério**.

**SUA PRIMEIRA TAREFA É A PROVENIÊNCIA.** Sem lastro, um teto mais generoso
enunciado depois de um resultado negativo lê-se como trave móvel — e seria a
segunda violação de pré-registro do trabalho. Procure o 15% em: dissertação
(Daru2024), projeto de qualificação, artigos em `artigos/`, repositórios
legados (`Tese-Vers-o-Draft`, `Tese-Reescrita`, `TESE`), atas de orientação.
- **Se achar**: cite a origem no texto — o critério vira pré-registro
  documentado, e a tese fica MAIS forte.
- **Se não achar**: redija a declaração de proveniência que o principal
  propôs ao autor (opção b), enunciando que 15% é o critério de origem e que
  a execução em 6,5% é mais restritiva. Nunca afirme registro que não existe.

## (3) O que a nova formulação ganha (e deve dizer)

O autor quer que a tese responda *"com que fração da base chego à mesma
performance"*, e que os 50 mil apareçam como REFERÊNCIA (o quanto seria
preciso com escolha aleatória), não como universo.

Saturação em 95% do teto, por seletor, em % da base — dado que a tese possui
e não enuncia assim:

| Seletor | Rótulos | % da base |
|---|---|---|
| entropia (SGD) | 8.000 | **3,5%** |
| DRI-SL-C (SGD) | 15.500 | 6,7% |
| **aleatório (SGD)** | 16.500 | **7,1%** |
| entropia (PVBin) | 19.000 | 8,2% |
| DRI-SL-C (PVBin) | 39.500 | 17,1% |
| **aleatório (PVBin)** | 40.000 | **17,3%** |

O contraste que a tese não enuncia hoje: **a entropia satura com metade do
que o aleatório precisa** (3,5% × 7,1%; 8,2% × 17,3%). É resultado positivo
forte, e é a resposta direta à pergunta do autor sobre quando o aleatório
converge.

## O que entregar

Pacote de prosa com antes/depois, tocando: 1-intro (enunciado do critério),
3-metodo (justificativa do pool, que passa de "viabilidade" a "referência de
comparação"), e os pontos de 5-resultados e 6-conclusao que reportam a
economia com o denominador antigo. Números novos: confira TODOS contra os
artefatos antes de escrever — o R5 é meu e eu vou reconferir.

ATENÇÃO ao que NÃO muda: o experimento executado, os resultados medidos e o
veredito no orçamento executado. Reenunciar não é reinterpretar.
