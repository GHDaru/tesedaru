---
de: banca
para: principal
tipo: tarefa
acao_esperada: apresentar ao autor o esquema 3 (DRI-SL) junto com os dois da tarefa 1810, como sugestão para decisão dele; se aprovado, a citação Reimers2019SBERT vai na legenda da figure
referencia: 3-metodo/esquemas-propostos/esq-drisl.tex · branch banca/esquemas-tikz-metodo · pedido direto do autor (conversa da banca, 2026-08-23)
criada_em: 2026-08-23T18:45:00Z
---
Extensão da entrega da tarefa 1810, por pedido direto do autor na conversa da
banca: ele apresentou um infográfico gerado por ferramenta de imagem para o
DRI-SL e pediu "a versão TikZ sóbria para a tese em loop".

Entregue na mesma branch `banca/esquemas-tikz-metodo`:

1. **`esq-drisl.tex`** — o DRI-SL em duas fases (densidade semântica →
   cotas proporcionais → laço de variedade lexical intragrupo → $L_0$) mais
   a faixa de avaliação (aleatório + envelope do AG) SEM afirmar resultado
   (camadas: o veredito da comparação é do Cap. 4). Idioma visual das
   figuras aceitas; citação do codificador vai na legenda (check-bib).
   Entra no fim de `sec:metodo-drisl`.
2. **`preview-esq-drisl.png`** — render final aprovado (evidência visual).
3. **`NOTA-esquemas.md`** atualizada com a seção do esquema 3: parecer sobre
   o infográfico (bom para slides da defesa, inadequado ao PDF), o que a
   versão sóbria preserva/corrige, e o loop de 5 iterações com compilação
   real (defeitos achados: cruzamento seta×título, colisão de rótulo no vão
   curto, quebra de matemática no "=", hifenizações — todos corrigidos).

FREEZE respeitado; nada na main. O conteúdo foi conferido linha a linha
contra a Seção `sec:metodo-drisl` antes de desenhar.
