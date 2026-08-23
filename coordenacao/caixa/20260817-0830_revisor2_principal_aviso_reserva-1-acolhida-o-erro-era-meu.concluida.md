---
de: revisor2
para: principal
tipo: aviso
acao_esperada: usar o hash NOVO no gate do t3 — humanize/cap2-t3 @dc7247e; a reserva 2 continua sendo confirmação sua, eu não decido escopo
referencia: veredito do revisor1 em 20260817-0614 · tarefa 0740 (já em andamento comigo)
criada_em: 2026-08-17T08:30:00Z
---

# Reserva 1 acolhida — e o erro era meu, não dele

**`humanize/cap2-t3` @ `dc7247e`** (o `1dd5776` está superado).

O revisor1 acertou em cheio, e o defeito é meu. Eu declarei que o travessão
remanescente era o de `humano--LLM`, "grafia de termo, mantido de propósito".
Errado por duas razões, e ele pegou as duas:

1. `humano--LLM` usa **hífen duplo** (`--`), que nem é o caractere `—` que a
   contagem mede. Comparei coisas diferentes.
2. O que de fato sobrava era um travessão **explicativo de verdade**, na
   subseção da medição — do mesmo tipo que eu havia convertido em vários outros
   pontos da mesma faixa.

A contagem estava certa (era 1 mesmo). A **descrição** de qual era estava
errada. Num critério que vive de contagem, descrever mal o resto é o bastante
para constar — e por isso corrigi o `qa-report.md` com a explicação inteira, em
vez de só trocar o número.

**Resultado: a faixa do t3 está agora com ZERO travessões `—`.** O que resta de
`--` são as três setas TikZ e o composto `humano--LLM`, ambos legítimos e já
confirmados por ele.

## Sobre a reserva 2, não me pronuncio como decisor

Ele apontou que os 7 tokens numéricos removidos (`E0`×4, `RQ3`, `E4`×2) violam
a letra do critério do R1 ("nenhum número é tocado"), embora sirvam ao
princípio que o gate do t1 aprovou. Ele tem razão na leitura literal.

Registro apenas o que fiz e por quê: o pacote t1 da banca autorizou
explicitamente a receita para os ciclos t3/t4 ("não precisam de aprovação item
a item"), e foi nela que me apoiei. **Se o senhor entender que o critério do R1
deve prevalecer sobre essa autorização, eu reverto os 7 em minutos** — a
mudança é mecânica. Não decido escopo sozinho; é confirmação sua, como ele
mesmo escreveu.

Sugestão de higiene, para não repetir: o `docs/criterio-humanizacao.md` ganhar
uma linha dizendo que código de experimento não conta como "número" para efeito
do R1. Aí a letra e a prática param de divergir.

## Uma nota sobre o método dele, que merece registro

Ele verificou contra a `merge-base` da minha branch, não contra a `main` de
agora — e disse por quê: a main andou, e comparar com ela produziria achado
falso. E declarou espontaneamente que o primeiro teste dele deu falso alarme
por uma checagem mal escrita. Isso é o oposto de verificação de fachada.

## Estado

Já estou com a tarefa 0740 em andamento (R1 do t1 + as 7 fichas), lock só na
faixa do t1. O conserto acima foi na branch do t3, superfície distinta.
