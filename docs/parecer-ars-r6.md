# Parecer R6 — academic-paper-reviewer (modo re-review, painel de 5 assentos)

Data: 2026-08-16 · Skill: `academic-paper-reviewer` v1.11.1 (instalada no repo,
`skills-lock.json`) · Âncora: R5 de 19/07 (média 88,4, "aprovação com revisões
menores").

**Proveniência do painel** (exigência da skill): 5 assentos executados em
contextos separados e cegos entre si (Iron Rule #2), somente-leitura, todos na
mesma família de modelo (Claude, sessão única de orquestração) — a separação de
papéis NÃO é alegação de processos de erro independentes; achados corroborados
entre assentos indicam robustez de leitura, não replicação independente.
Nenhum arquivo da tese foi editado pelo painel.

Configuração (Fase 0): Journal-Fit (banca PPGMNE, concentração Programação
Matemática) · R1 Metodologia (desenho experimental/estatística) · R2 Domínio
(AL + anotação com LLM) · R3 Perspectiva (ML de produção/MLOps/governança) ·
Devil's Advocate (fixo).

## 1. Notas consolidadas

| Dimensão (peso) | R4 | R5 | **R6** | Por assento (JF/Met/Dom/Persp) |
|---|---|---|---|---|
| Originalidade (20%) | 84 | 86 | **86,5** | 86 / 85 / 84 / 91 |
| Rigor metodológico (25%) | 87 | 90 | **85,8** | 90 / 87 / 80 / 86 |
| Suficiência de evidência (25%) | 86 | 89 | **83,3** | 89 / 84 / 81 / 79 |
| Coerência argumentativa (15%) | 84 | 88 | **87,3** | 88 / 88 / 88 / 85 |
| Apresentação (15%) | 88 | 89 | **87,8** | 89 / 90 / 83 / 89 |
| **Média ponderada** | 85,7 | 88,4 | **85,8** | — |

A queda R5→R6 **não reflete regressão do texto** (que quase não mudou): reflete
profundidade maior de verificação — este ciclo auditou bibliografia contra
fontes primárias, refez aritmética de tabelas e estressou a camada de síntese
com um Devil's Advocate dedicado. Três dos quatro assentos disseram isso
explicitamente.

## 2. Adjudicação dos CRITICALs (Iron Rule #4 — visível, um a um)

| # | Origem | Achado | Adjudicação | Consequência |
|---|---|---|---|---|
| DA-C1 | Devil's Advocate | "Sustentada a ~50%" verifica outra hipótese: a varredura usa rótulos **de gabarito**, não do oráculo, sem os controles da cláusula de superioridade; a pré-registrada pedia "rotulados pelo oráculo" | **VALIDADO** (âncoras conferidas: `1-intro:95-96` vs `5-resultados:550-552`). A camada experimental já demarca o post hoc; o excesso está no resumo e Cap. 6 | Bloqueia Accept. Remédio mínimo: reescrever resumo/conclusão ("sustentável com rótulos perfeitos, sem controle de baseline, semente única"); remédio forte: braço a 25k com oráculo |
| DA-C2 | Devil's Advocate | Cláusula "superando aleatória e incerteza com significância" silenciosamente abandonada no regime "sustentado"; no único ponto com controle, aleatória vence em acurácia | **VALIDADO** | Bloqueia Accept. Declarar a cláusula como não testada no regime post hoc (ou adicionar braços) |
| DA-C3 | Devil's Advocate | "Menos é mais no transformer" com E35 dentro do IC de Wilson da régua D, semente única, sem teste — e virou política categórica na conclusão | **VALIDADO** — corroborado sem combinação prévia pelo assento de Metodologia (MAJOR-4/5) | Bloqueia Accept. McNemar + bootstrap sobre predições persistidas; moderar verbos onde o IC cruzar zero |
| Dom-C1 | Domínio | Metadados bibliográficos fabricados: `Su2023` = título do FreeAL com autores inventados (reais: Xiao et al.); `Margatina2023` com obra/autores não localizáveis; ActiveLLM em triplicata com autores errados em 2 de 3 chaves | **VALIDADO** (linhas do bib conferidas). 4 de ~12 entradas recentes inspecionadas com metadados errados | Bloqueia Accept e o depósito. Auditoria TOTAL do `referencias.bib` contra fontes primárias (a constituição do projeto já exige validação contra fichamento) |
| Persp-C1 | Perspectiva | Base no Kaggle com "License = Unknown" (TODO do artigo A5 confirma); tese apresenta a base como contribuição sem licença nem parágrafo de proveniência/LGPD | **VALIDADO** | Bloqueia o depósito. Definir CC BY 4.0 (pendência R5), declarar no Cap. 3 com parágrafo de proveniência e ausência de dados pessoais |

## 3. Consenso entre assentos (achados corroborados por ≥2 assentos, sem combinação prévia)

1. **"Quatro resultados principais" enumera cinco** (resumo e abstract) — JF-M1; também na auditoria de escrita da sessão.
2. **População reservada: ≈140 mil (Cap. 5/E6) × 177.490 (Cap. 3)** — Met-MAJOR-2 + Persp-m2; a aritmética só fecha com 177.490.
3. **Racional do gate defeituoso**: "85% fica um desvio ACIMA do baseline (89,56%)" — DA-m1 + Met-MINOR-2.
4. **E2 prometido e nunca reportado** (fundamenta as 3 épocas do E3′) — Met-MAJOR-3 + DA-m6; e **E5 fantasma** (citado 3×, ausente do programa e do Cap. 5) — DA-m2 + Met-MINOR-7.
5. **Apêndice A7 recomenda a política de parada que o E3′ refutou** — Persp-M2 + DA (explicação alternativa 5).
6. **Pendências R5 abertas um ciclo depois**: licença Kaggle, DOI Zenodo/URL do código, autoria dos artigos, figura do A4 — JF-M2 + Persp-C1/M1. **Proveniência dupla: RESOLVIDA** (confirmada por JF e Met em `3-metodo:552-564`).
7. **Alegações empíricas sem citação** ("raramente tratada na literatura", "o colapso descrito na literatura") — Dom-M5; já apontadas na auditoria de escrita.
8. **Declaração de IA ainda "RASCUNHO"**, sem nomear ferramenta, com E1/E2 fora das listas — JF-m1 + Persp-m1.

Divergência registrada: Perspectiva deu Originalidade 91 (instrumentação de
custo adotável pela indústria) enquanto Domínio deu 84 (vizinhos FreeAL/LLMaAA
não confrontados) — as duas leituras são compatíveis: a originalidade forte é
metrológica, não conceitual.

## 4. Decisão editorial

**MAJOR REVISION — circunscrita: nenhum experimento novo de coleta é exigido.**

Rebaixamento em relação ao R5 (minor) por três razões que nenhum ciclo anterior
havia capturado: (i) metadados bibliográficos fabricados são incompatíveis com
revisões menores em tese de doutorado; (ii) a camada de síntese
(resumo/conclusão) afirma mais do que os dados sustentam em três pontos
validados pelo DA; (iii) licença da base indefinida bloqueia a contribuição
"conjunto de dados público". O núcleo experimental permanece forte, honesto e
acima do padrão da área — os cinco assentos convergem nisso — e TODAS as
correções são de texto, bibliografia ou análises sobre artefatos já
persistidos.

## 5. Roadmap de revisão (consolidado, deduplicado, por prioridade)

### Bloco A — Bloqueantes de mérito (antes de qualquer nova rodada)
1. Auditoria total do `referencias.bib` contra fontes primárias; corrigir
   FreeAL (Xiao et al. 2023), ActiveLLM (Markus Bayer/Christian Reuter),
   resolver `Margatina2023`; unificar chaves duplicadas (ActiveLLM 3×,
   Zhang2025 2×, zhang2022 2×, Devlin/Alsmadi/Song 2×). [Dom-C1, Dom-M2]
2. Reescrever a síntese do veredito no resumo, abstract e Cap. 6: demarcar
   "sustentável com rótulos de gabarito, sem controles, semente única";
   eliminar "não é infirmada" e "rotular tudo é contraproducente" como
   categóricas; fechar o veredito cláusula a cláusula (95%/30%; oráculo;
   superioridade). [DA-C1, DA-C2, JF-m2/m3]
3. Análises baratas sobre predições persistidas: McNemar A–B, B–C, E35–D +
   IC bootstrap das diferenças de Macro F1; moderar "supera"/"degradam"
   conforme o resultado. [DA-C3, Met-MAJOR-4/5]
4. Licença CC BY 4.0 no Kaggle + parágrafo de proveniência/LGPD no Cap. 3.
   [Persp-C1]

### Bloco B — Consistência numérica e programa
5. Reconciliar linha I=100 das duas tabelas do AG contra artefato. [Met-MAJOR-1]
6. Corrigir população reservada do E6 (177.490) ou declarar o filtro. [Met-MAJOR-2]
7. Reportar E2 (ou declarar "3 épocas por convenção"); definir ou remover E5;
   atualizar a tabela do programa (E0-P, E5, E6, E3′). [Met-MAJOR-3, DA-m2, Met-MINOR-7]
8. Corrigir o racional do gate (85% × 89,56%) e a frase "8 sementes é o
   mínimo para p<0,05" (n=6 já permite). [Met-MINOR-1/2]

### Bloco C — Posicionamento de literatura (dias, não meses)
9. FreeAL e LLMaAA na Tabela de lacunas + parágrafo de confronto. [Dom-M1]
10. Viés de autoavaliação: citar Farquhar/Gal/Rainforth 2021 e Kossen 2021;
    reivindicar a quantificação, não o fenômeno. [Dom-M3]
11. DRI-SL frente a TypiClust/coreset/PATRON. [Dom-M4]
12. Citar as 6 alegações sem fonte (lista em Dom-M5). [também G1.4 do scorecard]

### Bloco D — Operacional/prática
13. URL + DOI Zenodo do código no A4 e Cap. 3; licença do código. [Persp-M1]
14. Atualizar A7 com a política de parada corrigida pós-E3′. [Persp-M2]
15. Latência/vazão na tabela de custo + decomposição em tokens por rótulo
    (dados já instrumentados). [Persp-M3/M4]
16. Subseção curta de ética (viés do oráculo como viés de dado; papel humano
    remanescente). [Persp-M5]

### Bloco E — Forma e depósito
17. "Quatro"→"Cinco resultados" (ou fundir iv+v) no resumo e abstract. [JF-M1]
18. Finalizar declaração de IA (tirar RASCUNHO, nomear ferramenta, incluir
    E1/E2). [JF-m1, Persp-m1]
19. Parágrafo de ancoragem ao PPGMNE na Introdução (AL como alocação de
    recursos sob orçamento). [JF-(a)]
20. Resumo de ~800→~500 palavras; siglas PSI/RS/US expandidas e na lista;
    figura de arquitetura do A4; limpar resíduos do template PPGInf;
    autoria dos artigos derivados declarada. [JF-m4/m5, Persp-m3/m4, JF-M2]

### Integração com o ciclo de humanização (ADR 0001)
Os itens 2 e 17 tocam os mesmos arquivos do ciclo humanize-02 (resumo/abstract)
— executar juntos para não editar a mesma superfície duas vezes. Os itens do
Bloco C alimentam fichamentos novos (skill `fichamento`) antes de citar.

## 6. Nota final

O que este painel acrescentou aos R1–R5: os pareceres anteriores avaliaram o
que a tese FAZ; este auditou o que a tese CITA e o que a tese AFIRMA SOBRE O
QUE MEDIU. O veredito dos cinco assentos sobre a camada experimental é unânime
e positivo — "incomumente honesta" (DA). O trabalho desta revisão é fazer a
camada de síntese e a bibliografia descerem ao mesmo nível de rigor. Feito o
roadmap (estimativa: dias de trabalho de texto + auditoria de bib, zero
experimentos novos), a trajetória natural do próximo re-review é retomar e
superar os 88,4 do R5 — com fundações que uma banca hostil não derruba.
