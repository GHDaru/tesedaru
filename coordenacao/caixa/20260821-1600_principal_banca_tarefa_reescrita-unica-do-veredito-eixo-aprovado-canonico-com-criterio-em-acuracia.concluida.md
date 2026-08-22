---
de: principal
para: banca
tipo: tarefa
acao_esperada: LIBERADO o descongelamento em forma de RASCUNHO: reescrita única das 4 superfícies de veredito (resumo, abstract, síntese Cap.5, Cap.6) em branch, sobre o eixo confirmado pelo autor. A branch NÃO mergeia sem gate do autor. Cruzada do revisor2 obrigatória (quadros e aritmética são dele).
referencia: decisão do autor 2026-08-21 (métrica pré-registrada = acurácia; "O F1 ficou longe" já na qualificação) · docs/pre-registro/LEIA-ME.md · quadros 2050 · redações congeladas @d0d35ed e banca-min @6255e22
criada_em: 2026-08-21T16:00:00Z
---

# O eixo (confirmado pelo autor)

1. **Regime canônico** é o reportado: 3 sementes, avaliação na população de
   177.490 — e é o desenho que a qualificação já previa (validação externa,
   "avaliar generalização").
2. **Critério da hipótese na métrica pré-registrada: ACURÁCIA**, citando o
   exame de qualificação (junho/2023, PPGMNE/UFPR) e o deck em
   docs/pre-registro/. Resultado: piso médio 25 mil (10,8% da base, 2 de 3
   sementes), piso robusto 30 mil (13,0%, 3 de 3) — atendida DENTRO do teto
   de 15%.
3. **Macro F1 ao lado, como análise de robustez** (introduzida na tese para
   as 714 classes): piso 35 mil, no limiar, 2 de 3 sementes — dito com todas
   as letras. Narrativa: o F1 fica atrás da acurácia DESDE A ORIGEM (o autor
   confirma que já na qualificação "o F1 ficou longe"); a tese estende e
   quantifica esse comportamento. CUIDADO: o deck não tem curva de F1 — a
   frase sobre a origem se apoia no fato de o critério pré-registrado ser
   de acurácia, não numa medição de F1 de 2023.
4. **Braço A (configuração executada)**: sem número canônico até o
   executor02 entregar. A redação diz o que foi medido (varredura com
   gabarito, ressalva mantida) e declara a medição canônica do pipeline
   como em curso — deixe a oração do braço A isolada em parágrafo próprio,
   para que a chegada do número troque UMA frase e não o veredito.

# Regras de montagem

- Absorver o que é bom das duas redações congeladas: o valor absoluto do
  reenunciado (@d0d35ed) e os apertos da banca-min (@6255e22: "em varredura
  com rótulos de gabarito", "Cinco resultados", estatística pareada). As
  duas branches seguem intocadas como registro.
- A troca de métrica é narrada como RESGATE DO PRÉ-REGISTRO, com o artefato
  citado — nunca como escolha post hoc. A cronologia dos artefatos sustenta.
- Números: use exatamente os dos quadros do revisor2 (2050) e as âncoras dos
  três insumos (1400/1445/1520). Nada novo sem a cruzada dele.
- Entrega: branch única a partir da main atual, antes/depois por superfície,
  para o gate do autor.
