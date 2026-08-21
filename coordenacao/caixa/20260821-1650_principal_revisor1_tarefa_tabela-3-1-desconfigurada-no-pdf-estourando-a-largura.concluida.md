---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: consertar a LARGURA da Tabela 3.1 (tabela-mapa, 3-metodo/texto.tex ~linhas 50-88) — o autor viu no PDF a última coluna estourando a página ("Resultado em" cortado para "Resultad", "(executado; sem seção própria)" cortado em "(executad"). Entregar em branch com o PDF da página como prova de antes/depois. Lock de 3-metodo é seu de qualquer forma (figuras).
referencia: leitura do autor no PDF, 2026-08-21 (pág. 39) · sua Fase 2 (linha do E5 em duas) · tab:mapa-experimentos
criada_em: 2026-08-21T16:50:00Z
---

Diagnóstico provável: a tabela já era larga e as células novas mais longas
("framework (condicional)", "(executado; sem seção própria)", "conjunto
inicial / partida a frio") empurraram a última coluna para fora da mancha.
Não é defeito do conteúdo — é o contêiner.

Caminhos aceitáveis (a escolha técnica é sua):
- `tabularx`/colunas `p{}` com a coluna Objetivo elástica e quebra de linha
  nas células longas; ou reduzir para `\small`/`\footnotesize` se bastar;
- encurtar células sem perder conteúdo: "(executado; sem seção própria)"
  pode virar "(executado)\tnote" com a explicação na nota da tabela, onde já
  existe o bloco de Artefatos; "framework (condicional)" idem.

Invariantes: NENHUM conteúdo some (o que sair de célula vai para nota da
própria tabela); labels/refs intactos; check-travessao e compilação do PDF
verdes; conferir que a página 39 não quebra a tabela no meio de forma feia.
Cruzada: revisor2 (diff de conteúdo célula a célula = zero perda).
