---
de: banca
para: principal
tipo: tarefa
acao_esperada: somar o esquema 6 (laço do AG, Seção 3.5.2) ao bloco de sugestões TikZ para decisão do autor (pedido direto dele na conversa da banca; prévia já enviada a ele)
referencia: 3-metodo/esquemas-propostos/esq-ag-envelope.tex · branch banca/esquemas-tikz-metodo · pedido direto do autor (2026-08-23)
criada_em: 2026-08-23T19:15:00Z
---
Terceira extensão da série, por pedido direto do autor (ele colou o texto da
Seção 3.5.2 pedindo "aqui também uma explicação"):

**`esq-ag-envelope.tex`** — o laço evolutivo do envelope desdobrado:
população (N_pop=20; indivíduo = I índices únicos) → torneio (k=3) →
cruzamento de um ponto (0,8; reparo de unicidade) → mutação (0,1; m_s
genes) → aptidão na partição de aferição DISJUNTA → elitismo 10%
(N_elite=2) → repete; saída após 100 gerações (200 só no |L0|=10) para a
reavaliação no teste intocado (o envelope reportado). Carrega a nota de
proveniência da configuração (notebook define; JSON fixa só |L0|; população
é o único valor do artefato — a tripartição do lote A2) e a razão da
anti-circularidade. Números todos da própria seção.

Prévia versionada (preview-esq-ag-envelope.png); NOTA atualizada com o loop
(2 renders; defeitos: seta curva atravessando a própria nota, matemática
quebrada no "=", e hifenização errada por falta dos padrões pt — resolvida
instalando texlive-lang-portuguese e adicionando babel brazilian aos
invólucros de pré-visualização, o que torna o teste realista para TODOS os
esquemas da série).

FREEZE respeitado; nada na main. A pasta soma agora 6 esquemas propostos.
