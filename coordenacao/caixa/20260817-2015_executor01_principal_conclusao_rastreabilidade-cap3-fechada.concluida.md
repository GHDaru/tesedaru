---
de: executor01
para: principal
tipo: conclusao
acao_esperada: revisar os achados abaixo para o R5 do Cap. 3; decidir o que reportar ao autor
referencia: 20260817-1940 (tarefa) · activelearning@dac0179 · tesedaru@e67dc92
criada_em: 2026-08-17T20:15:00Z
---
Cap. 3 (método) casado com sua rastreabilidade: 24 itens novos, todos os que
consegui localizar dos ~36 números. `rastreabilidade.json`: 74→96 itens
(76 rastreado, 14 divergente, 5 sem-evidência, 1 legado). Fonte:
`activelearning/notebooks/auditoria/build_rastreabilidade.py`, regenerável.

RASTREADOS (batem exato): N=250.221; 144 linhas removidas (por subtração);
biscoito 14.292/5,7%; descrições 4-50 chars, mediana 32; 621 CategorySchema;
337 linhas raras (0,13%); 231.490/714 dedup; pool 50k+holdout 4k+177.490
reservada; JS=0,0022; Spearman=0,983; 649/714 classes no pool; ~70 ex/classe;
S-rand 1.000/S-strat 1.863; decaimento de peso 0,01 (default do AdamW); ε do
E4 (0,1/0,2/0,4, com 0 = E1 relido).

DIVERGÊNCIAS NOVAS (não corrijo, só reporto):
1. Conflitos de rótulo: tese diz 719 descrições/1.807 linhas; o script
   canônico (analyze_noise_impact.py — o mesmo que sustenta a análise de
   sensibilidade do próprio parágrafo), reexecutado agora, dá 693/1.720. O
   percentual arredondado bate (0,7%), os inteiros não (26 descrições/87
   linhas de diferença, não é ponto flutuante).
2. Taxa de aprendizado do BERTimbau: tese diz 3e-5; código usa 5e-5 em TODO
   lugar (default da classe, notebook real do E2, train_full.py) — nenhuma
   ocorrência de 3e-5 no repositório.
3. Lote de treinamento do BERTimbau: tese diz 32; código usa 16 (default)
   ou 128 (notebook real do E2), nunca 32. Hipótese não confirmada: 32 é o
   default de `max_length` (comprimento de token), parâmetro DIFERENTE no
   mesmo construtor — troca provável na redação.
4. Piso de 85% do critério de decisão do oráculo: nenhum oráculo do E0
   atinge 85% na S-rand (melhor: 82,1%, deepseek-v4-pro). O próprio
   `e0/config.json` anota deepseek-v4-flash (78,3%) como "LLM Inicial
   candidato" mesmo abaixo do piso declarado.
5. População reservada — achado que ajuda o #3 já reportado (E6, Cap. 5):
   o Cap. 3 já diz "≈177 mil", que BATE com o artefato (177.490). É o Cap. 5
   ("≈140 mil") que diverge — do artefato E do próprio Cap. 3. Dois números
   diferentes pra mesma quantidade em dois capítulos.

CORREÇÃO de achado anterior: o ganho do AG (+1,3 p.p. medido vs. +5,2 p.p.
relatado) segue divergente em número, mas D-002 (`docs/decisoes.md`)
documenta que o replay usa escala deliberadamente reduzida (N_pop=30/40
gerações vs. original 50/100) — a magnitude menor é esperada por desenho,
não achado sem explicação. Rebaixo a urgência deste, mantenho o número.

SEM EVIDÊNCIA (3 novos, além das figuras de plots/ já conhecidas):
janela de estagnação (p=5, ε=10⁻³) — não achei config/script; conjunto de
|L| varrido no E2 — notebook não fixa {10³,10⁴,5×10⁴}, sem resultado
versionado; calibração de lote do E0 (1/10/25, McNemar) — não versionada;
|A|/|D|≈18% do E3′ — mesmo bloqueio do cache do oráculo já conhecido.

Retomo as ondas restantes (3b, figuras) salvo instrução em contrário.
