---
de: banca
para: principal
tipo: aviso
acao_esperada: incluir no lote corretivo do bib-fix (patch pronto abaixo); fecha 1 dos 4 itens "sem DOI/URL" do Cap. 1
referencia: 1-intro/texto.tex:22 e :147 · referencias.bib entrada Daru2024Dissertacao · fonte: Biblioteca Digital de Teses e Dissertações da USP
criada_em: 2026-08-16T20:21:56Z
---
O autor forneceu o link do depósito da própria dissertação. Verifiquei na
página oficial (teses.usp.br): os metadados do bib estão CORRETOS, e agora há
DOI e URL para acrescentar — a entrada era a única do Cap. 1 marcada como
"registro público não localizado" no meu parecer de auditoria.

Confirmado na fonte: título idêntico ao do bib; autor Gilsiley Henrique Darú;
orientador Antonio Castelo Filho; Dissertação de Mestrado; ICMC/USP, São
Carlos; defesa em 23/09/2024; publicação em 07/01/2025.

PATCH (acrescentar 2 campos; nada mais muda):

@mastersthesis{Daru2024Dissertacao,
  author  = {Dar{\'u}, Gilsiley Henrique},
  title   = {Categoriza{\c c}{\~a}o de produtos em e-commerce: avalia{\c c}{\~a}o do m{\'e}todo Argmax para classifica{\c c}{\~a}o de descri{\c c}{\~o}es curtas em portugu{\^e}s},
  school  = {Instituto de Ci{\^e}ncias Matem{\'a}ticas e de Computa{\c c}{\~a}o, Universidade de S{\~a}o Paulo},
  address = {S{\~a}o Carlos},
  year    = {2024},
  doi     = {10.11606/D.55.2024.tde-07012025-171839},
  url     = {https://teses.usp.br/teses/disponiveis/55/55137/tde-07012025-171839/pt-br.html}
}

OBSERVAÇÃO PARA O R4/R5, NÃO PARA ESTE LOTE: a dissertação é citada em
1-intro:22 e :147. Com o localizador público disponível, a banca consegue
conferir a fronteira anti-sobreposição declarada entre dissertação e tese —
vale checar, na leitura final, se o texto explicita o que a tese acrescenta
em relação a ela.
