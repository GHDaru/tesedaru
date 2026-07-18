# Parecer simulado v2 — orientador e banca + avaliação R4 pela skill

Data: 18/07/2026. Estado avaliado: v0 completa + E6/DRI-SL-C incorporados,
passe de estilo (booktabs, nomenclatura, impessoalidade), apêndice A7,
levantamento de literatura integrado. Complementa o parecer de 17/07 e as
revisões R1–R3.

## 1. Avaliação R4 (academic-paper-reviewer, modo re-review + apresentação)

| Dimensão (peso) | R3 | R4 | Movimento |
|---|---|---|---|
| Originalidade (20%) | 82 | 84 | E6 (viés de autoavaliação com controle) e DRI-SL-C são contribuições novas e legítimas |
| Rigor metodológico (25%) | 86 | 87 | justificativas de dimensionamento completas; E6 declarado como descritivo (semente única) — honesto |
| Suficiência de evidência (25%) | 84 | 86 | 8 braços do E6 + ciclo real com parada; AlleNoise/NoiseBench ancoram o E4 |
| Coerência argumentativa (15%) | 85 | 84 | ↓ leve: o Cap. 5 acumulou seções (E0→E0-P→E1→E4→E6→gate) e o Cap. 2 não prepara E6 — a reestruturação planejada resolve |
| Apresentação (15%) | 85 | 88 | booktabs unificado, nomenclatura, figura citada, tabelas como veículo primário |
| **Média ponderada** | 84,5 | **85,7** |

**Decisão: MINOR REVISION (mantida)** — os bloqueantes continuam sendo
externos ao texto (bloco H). Apontamento novo da R4: a **fragmentação
estrutural do Cap. 2** (70 blocos/4 níveis) é agora o maior déficit de
apresentação; o plano de reestruturação em `plano-reestruturacao-cap2.md`
responde exatamente a isso e tem o endosso desta revisão.

## 2. Na voz do orientador

Gilsiley, três coisas.

**a) Sobre a sua inquietação com a numeração: ela está certa, e chegou na
hora certa.** O Cap. 2 é o único pedaço da tese escrito ANTES de existir o
programa experimental — e se nota: ele cataloga em vez de argumentar. Um
capítulo de fundamentação maduro não é uma enciclopédia com numeração; é um
argumento em cinco movimentos que termina com o leitor pensando "claro que o
Cap. 3 tem que existir". O plano de reestruturação propõe exatamente isso:
cada seção com pergunta e mensagem declaradas, dois níveis no máximo, corte
de 25%. Minha única condição: **não perca as fórmulas de incerteza** (o
leitor do Cap. 5 precisa delas) e **não corte a tabela de lacunas** — ela é o
gatilho do seu Cap. 3.

**b) O E6 valorizou a tese, mas cuidado com o escopo do Cap. 5.** Você agora
tem seis seções experimentais num capítulo só. Depois da reestruturação do
Cap. 2, considere (não é obrigatório) mover E6 para um capítulo curto próprio
ou para junto dos apêndices operacionais — a banca lê o Cap. 5 como "o
capítulo do oráculo", e o E6 é sobre seleção e medição. Decisão sua; registre
o racional em qualquer caso.

**c) O "menos é mais" precisa de uma frase de cautela.** O achado (treinar
com 15k ativos supera 50k completos) vale para SGD com perda logística e
métrica macro, semente única. Está corretamente declarado como descritivo —
mantenha assim e resista à tentação de generalizar no resumo. Se o resultado
sobreviver a 8 sementes (barato: oráculo perfeito), aí sim sobe de status.

## 3. Na voz da banca (arguições novas)

**Metodologia**: "O E6 usa semente única e o senhor reporta 'saturação em
8.000'. Qual a sensibilidade desse número ao sorteio inicial?" *(Resposta
honesta: não medida; o custo de repetir com 8 sementes é ~1 dia de CPU e é a
primeira extensão natural — está declarado como descritivo.)*

**AL**: "A DRI-SL-C com alocação mínima de 1 por classe prevista, com 621
classes e lote 500, força ~500 grupos distintos por lote — não é isso um
estratificador disfarçado? O ganho vem da 'novidade lexical' ou só do
balanceamento?" *(RESPONDIDA em 18/07 — ablação executada (braço drisl-cs,
2 classificadores × 100 lotes): a banca tinha razão. A versão SEM novidade
lexical supera a DRI-SL-C completa nos dois classificadores (SGD: teto
0,555/sat. 10k vs 0,491/15,5k; PVBin: sat. 18k vs 39,5k) — o ganho vem
integralmente do agrupamento por predição; a novidade lexical é
contraproducente no regime contínuo, embora essencial no cold start (P2).
Incorporado como achado (iv) do E6 no Cap. 5, com a contribuição (ii) do
Cap. 6 reformulada em conformidade.)*

**Aplicações**: "O senhor mostra que rotular tudo piora o macro do SGD. Numa
empresa que JÁ rotulou tudo, o que fazer?" *(Resposta que a tese suporta:
reponderar/subamostrar o treino — a amostra ativa é um curriculum de
balanceamento; ou usar classificador com normalização por classe, como o
PVBin, imune por construção.)*

## 4. Auditoria: todos os achados estão na tese? (pedido do autor)

| Achado | Na tese? | Onde |
|---|---|---|
| Sensibilidade de L0 (6,4 p.p.) + replay ≤0,7 p.p. | ✔ | Cap. 4 |
| Envelope AG + circularidade −6,3 p.p. | ✔ | Cap. 4 |
| DRI-SL vence AG no cold start | ✔ | Cap. 4 |
| E0 RQ1–RQ4 completos + gate | ✔ | Cap. 5 |
| Ruído do gabarito ≤ +0,7 p.p. | ✔ | Caps. 3 e 5 |
| E0-P faca de dois gumes | ✔ | Cap. 5 |
| E1 rankings + ablação de lote | ✔ | Cap. 5 |
| E4 retenção 87/74/54% + nuance NoiseBench | ✔ | Cap. 5 |
| Braço free + achado de serving (p<0,001) | ✔ | Cap. 5 + resumo |
| E6: seletores em escala, menos-é-mais, viés interna×externa, DRI-SL-C | ✔ | Cap. 5 §E6 + Cap. 6 (18/07) |
| Parada por estagnação nos ciclos real (4,7k/6k de 15k) e simulado | ✔ | Apêndice A7 (atualizado 18/07) |
| Ciclo de vida: liberação + drift em 3 camadas | ✔ | Apêndice A7 |
| Calibração de lote b20×b50 (NIM) | repo | decisão: instrumento operacional; citada por remissão nos artefatos |
| BERTimbau smoke CPU (86,3% em 900 docs) | repo | correto ficar fora: números da tese virão do E2/E3 na GPU (bloco H) |
| Vazão/cota como achado operacional (D-005/D-006) | ✔ | Cap. 5 RQ2 + decisões |

**Veredito: nenhum achado científico fora do texto**; os dois itens "repo"
são instrumentação operacional, com registro rastreável e menção por
remissão — decisão defensável.
