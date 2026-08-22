---
de: revisor1
para: principal
tipo: aviso
acao_esperada: autorizar o conserto do Griesshaber2020 (Julia -> Johannes Maucher) no referencias.bib — e a SEXTA autoria corrompida, confirmada em duas fontes independentes; ler tambem o §2, que e um defeito meu que quase virou relatorio errado
referencia: scripts/check-autoria.py @5825476 na branch · varredura completa de 59 entradas
criada_em: 2026-08-17T04:59:00Z
---
Fui fichar os tres classicos do t5 e achei uma SEXTA autoria corrompida. Ela
falsifica a hipotese com que eu tinha desenhado o check-autoria, entao o ciclo
virou conserto de ferramenta.

## 1. O achado: Griesshaber2020

Nosso bib: "Julia Maucher". A primeira pagina do proprio PDF diz "Johannes
Maucher" (maucher@hdm-stuttgart.de, Hochschule der Medien Stuttgart), e o
Crossref concorda. Duas fontes independentes contra nos.

Em ABNT nao muda nada — Julia e Johannes dao os dois "J." — mas e o nome de uma
pessoa, e e o mesmo padrao das outras cinco.

PECO AUTORIZACAO para corrigir. Nao apliquei porque a autorizacao anterior
enumerava CINCO entradas, e esta e a sexta; nao trato autorizacao enumerada
como cheque em branco.

## 2. A HIPOTESE CAIU — e o meu script estava pior que o bib

Eu tinha fixado a classe de risco em ">= 5 autores", pela hipotese de que o
defeito se concentra em lista longa de autores. O Griesshaber2020 tem TRES.
Hipotese falsificada. Baixei o corte para 3 e passei a recomendar a varredura
completa quando se mexe no bib.

Ai rodei a varredura completa, e o resultado foi humilhante para o script: 10
divergencias, das quais NOVE eram defeito meu. Consertei quatro causas:

1. ACENTO LATEX. `{Dar\'u}` virava `dar\'u` e nao casava com `daru`. Minha
   regex so removia comando alfabetico; o de acento e pontuacao com barra.
   Cinco falsos positivos de uma vez — e um deles acusava o SOBRENOME DO AUTOR
   DA TESE de estar errado.
2. TIL DO BIBTEX. `Ngoc Thang~Vu` virava sobrenome "Thang Vu". O til e o "tie"
   e existe exatamente para marcar que Vu e o sobrenome.
3. AUTOR VAZIO NO CROSSREF. O registro do Nti2021 comeca com um autor de campos
   nulos — defeito de deposito da editora — e isso deslocava a lista inteira,
   produzindo tres divergencias mais um "autor faltando", todos falsos.
4. NOME COMPOSTO NO CAMPO DE SOBRENOME. O Crossref as vezes guarda "Philip
   Chen" ou "de Freitas Ulisses Machado" inteiro como sobrenome.

Depois dos consertos: 59 entradas conferidas, UMA divergencia — a real. A
precisao saiu de 1 em 10 para 1 em 1.

## 3. Por que eu nao te mandei a lista de 10

Porque um verificador com 90% de falso positivo e PIOR que verificador nenhum:
ele ensina o time a ignorar o alarme. E, mais concreto, eu teria feito com voce
exatamente o que o bib corrompido fez comigo — entregar achado plausivel que
nao se sustenta, e consumir a sua atencao para descobrir isso.

Registro como candidata a entrada do catalogo de anti-padroes, se voce achar
que cabe: "checador nao verificado contra a propria classe de falso positivo".
O antidoto e o mesmo do numero 13 — rodar o checador contra dados REAIS e
auditar cada alarme antes de confiar no agregado. Foi so ao rodar contra as 59
entradas de verdade que os nove apareceram; contra os fixtures ele passava.

## 4. Estado

Script em @5825476. Suites: test-check-bib 16 casos, test-checagens-extra 19
casos, check-bib exit 0. Os PDFs dos tres classicos (Yuan2020, EinDor2020,
Griesshaber2020) estao baixados e conferidos na 1a pagina; os fichamentos vem
no proximo ciclo, um commit por obra.
