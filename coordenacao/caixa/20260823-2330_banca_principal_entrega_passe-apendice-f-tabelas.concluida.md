---
de: banca
para: principal
tipo: tarefa
acao_esperada: somar o Apêndice F ao bloco de integração (B, A, C, D, E) — seis entregas juntas, com a compilação completa (DoD IX); repassar ao revisor1 a conferência do CV contra o artefato bruto (detalhe abaixo)
referencia: a6-tabelas/texto.tex · branch banca/esquemas-tikz-metodo · ordem do autor (2026-08-23)
criada_em: 2026-08-23T23:30:00Z
---
Conclusão do passe no Apêndice F (claim 2310; ordem do autor). Ele já
recebeu as páginas renderizadas.

1. **Verificação executável dos 94 valores**: script conferiu linha a
   linha mín≤P25≤mediana≤P75≤máx, mín≤média≤máx, IQR=P75−P25 e
   CV=DP/mediana. Ordem, média e IQR exatos em 94/94. O CV bate dentro do
   erro de arredondamento composto (foi calculado da fonte não
   arredondada) — SUGESTÃO: revisor1, que tem o repositório de dados,
   pode fechar essa ponta conferindo o CV contra o artefato bruto.
2. **Vírgula decimal**: a tabela usava ponto (0.067) contra a convenção
   da tese — 94 linhas convertidas por script, dígitos intocados.
3. **Limpeza**: removido o comentário-cicatriz "% DADOS ... COPIADOS DO
   SEU <DADOS>" (assinatura de máquina no fonte) e o vestígio "Base" do
   cabeçalho (agora uma linha, nas duas ocorrências do longtable).
4. **Prosa/autocontenção**: sem \ref de seção e sem o símbolo T; abertura
   define DP/quartis/IQR/CV; caption sem "Performance" e com $L_0$.
5. **Sem figura, por decisão fundamentada**: a figura natural seria a
   curva dos dados — exigiria pipeline de artefato (princípio V).
6. 0 erros / 0 overfull nas medidas reais (3 páginas).

Fila em bloco: B+A+C+D+E+F + correções 12pt. Resta o A7 (parada/drift).
