---
de: principal
para: executor01
tipo: tarefa
acao_esperada: PARE a semente 7 (fica com o executor02 depois) e assuma esta missão: organizar os experimentos em notebooks auditáveis no Kaggle, com saída visual
referencia: decisão do autor 2026-08-16 · achado do executor02 sobre a P100 (kernel-metadata machine_shape=NvidiaTeslaT4) · activelearning/experiments/
criada_em: 2026-08-16T20:26:07Z
---
MUDANÇA DE MISSÃO (decisão do autor). A semente 7 sai da sua fila: o
executor02 já tem a receita funcionando e segue com as sementes. Você assume
a organização dos experimentos em NOTEBOOKS AUDITÁVEIS.

ANTES DE QUALQUER COISA — a armadilha que o executor02 já pagou: o Kaggle
entrega T4 ou P100 conforme disponibilidade, e a P100 (sm_60) NÃO roda o
PyTorch da imagem (que cobre sm_70+). Fixe sempre
"machine_shape": "NvidiaTeslaT4" no kernel-metadata.json; pela interface,
escolha GPU T4 x2. Leia a mensagem 20260816-2005 dele — a receita está lá.

MISSÃO: com GPU do Kaggle disponível, os experimentos da tese podem ser
reexecutados de forma rápida e — o que o autor quer — AUDITÁVEIS: ele precisa
abrir um notebook e VER o experimento, os dados, o resultado e o artefato,
sem depender de log de terminal.

ENTREGAS
1. Um notebook por experimento (E0 oráculos, E0-P prompt, E1/E4 estratégias e
   ruído, E5 ciclo real, E6 população, E3′ validação forte), padronizados:
   - cabeçalho: pergunta do experimento, hipótese, artefato de saída esperado;
   - carga de dados com a checagem de identidade (md5 do CSV, contagem de
     linhas, classes) impressa na tela;
   - execução parametrizada (semente, orçamento, braços);
   - saída VISUAL: tabela de resultados + gráfico (curva de aprendizado,
     comparação de braços, matriz de confusão quando couber);
   - rodapé: caminho do JSON gravado e como reproduzir.
2. Um notebook índice ("00-visao-geral") que liste os experimentos, o que cada
   um responde e o estado da última execução.
3. Tudo versionado em activelearning/notebooks/auditoria/ (crie a pasta) e
   executável no Kaggle sem edição manual — dados vêm do repositório.
4. Comece pelos que JÁ têm resultado gravado (E6 e E3′): o notebook deve
   reproduzir o número que está na tese hoje. Se divergir, é achado — poste
   bloqueio ao principal imediatamente, NÃO ajuste o número.

REGRAS: não edite texto da tese nem o plano; reporte ao principal; um commit
por notebook; se algo quebrar, poste bloqueio e siga para o próximo notebook.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
