---
de: banca
para: principal
tipo: tarefa
acao_esperada: gatear com o autor a nova introdução metodológica do Cap. 3 (proposta pronta, aprovada em verificação cega) e triar as 8 sugestões secundárias do parecer; a banca NÃO tocou no Cap. 3
referencia: encomenda direta do autor à banca · proposta-introducao-cap3.tex + parecer do painel · branch banca/esquemas-tikz-metodo
criada_em: 2026-08-24T19:30:00Z
---
Encomenda do autor à banca: "uma introdução metodológica que leve o leitor à
compreensão do que foi feito", avaliada por painel de 3 especialistas
(escrita acadêmica, storytelling científico, leitor de banca de outra área)
em loop até a excelência.

ENTREGA (2 artefatos):
1. `docs/pareceres/2026-08-24-painel-introducao-metodologica-cap3.md` —
   diagnóstico consolidado (a visão geral contada 3x; o elementar ausente:
   tarefa/dados/métrica não respondíveis pela abertura; DRI-SL fechada;
   promessa desmentida pela Tabela 3.1; pré-registro com marco ambíguo) +
   8 sugestões secundárias (S1-S8) para triagem.
2. `3-metodo/esquemas-propostos/proposta-introducao-cap3.tex` — o texto
   proposto: substitui as linhas 4-26 e 40-45 da abertura e o parágrafo
   59-78 da Seção 3.1 (instruções de recorte nos comentários do arquivo).
   A figura fig:metodo-sequencia fica onde está.

QUALIDADE (verificado, não julgado): compila 0 erros / 0 overfull em corpo
12; 13/13 rótulos de \ref existem; zero travessões; siglas na ordem (LLM
antes de FALCO; DRI-SL aberta idêntica à lista); "cerca de 250 mil" espelha
o §3.2. Verificador independente em contexto limpo: REPROVADO na 1ª rodada
(3 defeitos) → corrigido → APROVADO (teste cego de compreensão 10/10).

RISCO/REVERSIBILIDADE: substituição de prosa da abertura, sem tocar números,
resultados ou estrutura de seções; reversível por git. O único número da
proposta ("cerca de 250 mil") cria dever de espelho com o §3.2.
