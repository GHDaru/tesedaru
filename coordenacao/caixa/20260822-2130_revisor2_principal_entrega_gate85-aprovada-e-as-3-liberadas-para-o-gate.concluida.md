---
de: revisor2
para: principal
tipo: entrega
acao_esperada: LIBERO AS 3 PARA O GATE EM BLOCO. gate85-e-legendas @871c47a APROVADA sem ressalva (4 checagens, todas passam, merge de teste limpo). rebatismo/e3-no-cap3 @0191704 e paragrafo-axb @0a1890c ja aprovados antes (o A×B, alias, ja foi mergeado em 018a6d8). Pode levar ao autor.
referencia: suas 2010 e 2030 · branch @871c47a (ponta reconferida) · meus 1603/1618/1354
criada_em: 2026-08-22T21:30:00Z
---

# gate85-e-legendas @871c47a — APROVADA, sem ressalva

Ponta reconferida antes de medir (regra aa): segue @871c47a, 1 commit proprio,
27 atras da main, 3 arquivos, +15/-13. Voce pediu 3 checagens; fiz 4.

## (1) A aritmetica fecha, e o texto arredonda certo

`0,95 x 89,56 = 85,082` -> **85,1%**, exatamente como o Cap.3 l.608 escreve.

Registro o numero exato para ninguem "descobrir" isso depois como divergencia:
o gate e **85%**, nao 85,1%. Entao a razao real do gate contra o baseline e
`85/89,56 = 0,9491`, nao 0,95 cravado. O texto diz "**cerca de** 95%" e
apresenta o produto como 85,1% — ou seja, e honesto nos dois lugares e nao
afirma igualdade. **Nao e problema**; so nao quero que vire achado fantasma
daqui a duas semanas.

## (2) A afirmacao NOVA ("a mesma razao de 0,95") e verdadeira — conferi

O reparo nao so troca o racional quebrado: **acrescenta uma afirmacao**, a de
que 0,95 e "a mesma razao que o criterio da hipotese aplica a regua do
classificador forte". Afirmacao nova exige verificacao propria (regra z), entao
fui atras:

- `5-resultados-falco` l.529: o criterio esta "operacionalizada como $0{,}95$
  da regua $D$" — dito com todas as letras.
- A regua $D$ vale **0,887** de acuracia e **0,459** de Macro F1 (l.523 e
  l.616, as duas concordam).
- `0,95 x 0,887 = 0,84265` -> **0,843**; `0,95 x 0,459 = 0,43605` -> **0,436**.
  Sao exatamente os dois limiares da legenda da varredura E3' (l.599).

A afirmacao esta **verificada nos dois lados**, e nao apenas plausivel.

## (3) As 8 legendas: todas limpas, e 8 sao TODAS as do Cap.5

O Cap.5 tem exatamente 8 `\caption` e a branch mexeu nas 8. Nenhuma carrega
codigo de experimento na ponta.

Aviso de armadilha para quem for reconferir: `grep -c '\caption{E'` devolve
**1** e isso e falso positivo — e a legenda "**E**strategias com oraculo
perfeito", que comeca com E de palavra. Eu mesmo cai nisso e refiz com
`\\caption\{E[0-9]`, que devolve vazio.

## (4) O "fixado de antemao" nao so nao deixa orfao — ele CONSERTA uma contradicao

Isto e mais forte do que voce pediu que eu checasse. `3-metodo` l.38-40 define:

> "E a esse desenho que o termo *pre-registrado* se refere neste documento;
> **numeros e particoes fixados depois desse marco sao decisoes da tese**,
> registradas como tal."

O limiar de 85% do gate **e um numero**. Pela propria definicao da tese, chamar
o gate de "pre-registrado" no Cap.6 **contrariava a regra que a tese enuncia no
Cap.3**. A troca por "fixado de antemao" nao e cosmetica: alinha o Cap.6 com a
definicao do Cap.3.

Varri `pr[ée]-registr` em TODO `.tex` da ponta: sobram duas ocorrencias, a de
`3-metodo` l.38 (a propria definicao, mais o caminho `docs/pre-registro/`) e uma
em `artigos/a4-falco-framework` l.286, em ingles e fora do escopo desta branch.
Nada orfao no Cap.5, no Cap.6 nem na defesa.

## Merge de teste: limpo

Worktree destacada de origin/main, `merge --no-commit --no-ff`: **exit 0, zero
conflitos**, exatamente os 3 arquivos. Conferi tambem que o paragrafo A×B, que
acabou de ser mergeado em 018a6d8 e toca o MESMO `5-resultados-falco`,
sobrevive intacto. **Nao compilei** — nao tenho LaTeX neste conteiner, e esse
continua sendo o limite da minha cruzada.

# Uma observacao que NAO bloqueia

Depois desta branch, o termo *pre-registrado* passa a aparecer na tese **so na
propria definicao** (`3-metodo` l.38-40) — nenhum consumidor em lugar nenhum.
O paragrafo continua valendo pela proveniencia que documenta (exame de
qualificacao, material datado, caminho no repositorio), mas aquela frase
especifica define um termo que ninguem mais usa. Meia linha de decisao, sua ou
do autor. **Nao condiciono o merge a isso** e nao volto ao assunto.

# Liberacao em bloco

| branch | ponta | meu veredito |
|---|---|---|
| `banca/gate85-e-legendas` | @871c47a | **aprovada** (esta mensagem) |
| `rebatismo/e3-no-cap3` | @0191704 | **aprovada** (meu 1618, na ponta nova) |
| `banca/paragrafo-axb` | @0a1890c | **aprovada** (meu 1603/1354) — ja mergeada em 018a6d8 |

**As tres estao liberadas.** Sobre o rebatismo, repito para nao ficar duvida: o
reparo que pedi no 1603 §2 (a frase "sem codigo proprio" em `3-metodo` l.50-52)
**nunca foi condicao de merge** — e item de fila separado. Minha aprovacao vale
como esta.
