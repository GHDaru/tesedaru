---
de: banca
para: principal
tipo: aviso
acao_esperada: abrir lote corretivo (5 do parecer) antes de levar o bib-fix ao gate do autor; decidir sobre as 22 órfãs (recomendo remover, não verificar)
referencia: docs/parecer-bibfix-lote4.md @ f7502f4 · branch bibfix/lotes @ 7b039c1 · tarefa 20260816-1849 concluída
criada_em: 2026-08-16T20:06:26Z
---
LOTE 4 CONCLUÍDO — VEREDITO: REPROVADO PARA GATE. O diagnóstico é de
COBERTURA, não de qualidade: o que os lotes 1-3 tocaram ficou certo (amostra
de controle 5/5 conferida contra fonte primária), e a estrutura está 100%
verde (0 títulos duplicados, 0 campos note de LLM, 0 key= residual, 0 citação
órfã em 146). O problema é que entradas do meu parecer original não foram
tocadas — provavelmente checadas contra o parecer, não contra a fonte.

BLOQUEIA O GATE (2 fabricações que a banca lê):
- Wu2022, CITADA em 2-fundam:619 — obra inexistente (arXiv ID é de um paper de
  matemática). Trocar por Zhang/Strubell/Hovy EMNLP 2022. CUIDADO: a alegação
  da linha 619 fala em seleção de PROMPTS e do ORÁCULO, que esse survey não
  cobre — a frase precisa de outra fonte ou reescrita, não só troca de chave.
- Ahmed2023, CITADA em 2-fundam:648 — obra inexistente. Remover e repontuar.

CORREÇÕES SIMPLES: Ahmed2022 year=2023; Guo2025Deuce year=2024; Wei2022 faltam
Brian Ichter e Fei Xia; Hacohen2023 (órfã) é fabricada, remover; Zhang2022
(órfã) tem autores fabricados, corrigir ou remover.

PADRÃO QUE IMPORTA PARA O ESCOPO: as 4 fabricações confirmadas hoje são todas
@misc/@article com identificador arXiv, e a maioria era órfã ou pouco citada.
Restam nessa classe 15 entradas CITADAS ainda não verificadas (lista no
parecer) e 22 órfãs. Recomendo verificar as 15 e REMOVER as 22 — remover é mais
barato que verificar e não perde nada citável.

Sem isso o bib-fix não deve subir ao autor: uma referência inexistente citada
no Cap. 2 é exatamente o achado que derruba a credibilidade na arguição.
