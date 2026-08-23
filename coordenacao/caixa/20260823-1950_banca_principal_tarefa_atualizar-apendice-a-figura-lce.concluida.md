---
de: banca
para: principal
tipo: tarefa
acao_esperada: integrar na main a edição do Apêndice A (a1-lce/texto.tex) desta branch — ORDEM DIRETA DO AUTOR na conversa da banca; validar com a compilação completa da tese (DoD IX) antes do merge
referencia: a1-lce/texto.tex + 3-metodo/esquemas-propostos/esq-lce.tex · branch banca/esquemas-tikz-metodo · ordem do autor (2026-08-23)
criada_em: 2026-08-23T19:50:00Z
---
O autor ordenou, na conversa da banca: "insira esta figura no apêndice A. E
mande uma mensagem para o principal para atualizar o apêndice A." Este é o
PRIMEIRO esquema da série promovido de sugestão a texto da tese.

O que está pronto nesta branch (edição em prosa entregue via branch, mão da
main continua sua — §2-ter):

1. **`a1-lce/texto.tex`**: no fim da seção Definição, frase de remissão +
   ambiente `figure` com `\input{3-metodo/esquemas-propostos/esq-lce}`,
   legenda com a ponte de notação (L_ideal,0 = n_1, L_final = n_K, na
   notação da eq:ap-lce) e rótulo `fig:ap-lce-geometria`.
2. **`esq-lce.tex`**: remissão interna ajustada para o novo lar — a caixa
   de fórmula agora aponta "(Equação~\ref{eq:ap-lce})" (apontar "Apêndice
   A" de dentro do Apêndice A seria autorreferência); cabeçalho atualizado.
3. O bloco `figure` + esquema foi **test-compilado** neste contêiner
   (pdflatex, 0 erros, 0 overfull; render conferido visualmente). O que EU
   NÃO consigo validar aqui é a tese inteira (sem a toolchain ppginf
   completa): a compilação completa com 0 erros/0 refs indefinidas
   (princípio IX) precisa rodar na sua integração ou na cruzada.

Nota: a figura já foi revisada pelo autor (sem faixa estatística, sem
precedência ALC, estouro da fórmula corrigido). Largura ~13,5 cm, cabe no
textwidth. FREEZE respeitado (curva declarada ilustrativa no título
interno, princípio V).
