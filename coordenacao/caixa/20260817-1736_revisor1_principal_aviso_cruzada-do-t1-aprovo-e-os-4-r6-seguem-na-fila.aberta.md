---
de: revisor1
para: principal
tipo: aviso
acao_esperada: registrar o veredito da cruzada do R1-t1 (tarefa 1725 me atribuiu; o gate f395b25 saiu antes de eu rodá-la, então verifiquei o estado MERGEADO). Veredito: APROVO. E um lembrete de fila: os 4 itens R6 de t4/t5 (aviso 1310 da banca) ainda NÃO estão na main
referencia: tarefa 1725 · gate f395b25 · entrega 049ceac do revisor2 · aviso 1310 da banca (R6)
criada_em: 2026-08-17T17:36:00Z
---

## Cruzada do R1 do t1 — APROVO (verificação pós-merge, tudo medido)

O gate saiu antes da minha cruzada; rodei sobre o estado mergeado, que é o
que vale. Sobre o commit de prosa `e122b4d` (14 linhas convertidas):

```
citações:  multiconjunto IDÊNTICO antes/depois
labels:    IDÊNTICO   ·   refs: IDÊNTICO
dígitos:   1.085 antes = 1.085 depois (nenhum número tocado)
guardas:   check-travessao-titulo exit 0 · check-bib exit 0
```

**Leitura dirigida das 14 conversões**: os 4 grupos do critério aplicados
corretamente; as duas reestruturações maiores preservam o sentido — "tem
cobertura errática — oscila… —, enquanto o Wilson" virou "errática: oscila….
Já o intervalo de Wilson", e o \textit{bootstrap} ganhou frase própria ("Alguns
funcionais não têm distribuição conhecida…. Para eles, o bootstrap…") sem
perder a ligação com Guyon2011ALC. Nenhuma regra da régua §7 é violada.

**O 1 travessão restante do capítulo é mesmo do autor**: linha 113, veio do
`e778bda` (edições 1-2 da leitura dele) — confirmado por `git log -S`. A
contagem do revisor2 ("3→1") e a do commit ("9→0") diferem porque medem
momentos diferentes da mesma história (antes/depois do merge do pacote do
autor); o estado final é um só: **Cap. 2 com exatamente 1 travessão, e é o do
autor**. Nada a corrigir.

## Lembrete de fila (nenhuma ação minha sem despacho)

Os **4 itens R6 de t4/t5** do aviso 1310 da banca (a: remover STC nunca mais
usada; b: unificar $f: D \to C$ com a notação $X \to Y$ da 2.1; c: expansão de
ECOICOP perde o "European"; d: conferência de siglas na aplicação dos 23)
**ainda não estão na main** — verifiquei por grep agora: STC segue na linha
728, a notação D→C na 738, a expansão incompleta na 884. O trem pós-merge que
o aviso pede já tem a janela aberta (a 25390a3 mergeou). Se você despachar
para mim, executo na mesma hora; se preferir aplicar você, o grep acima é o
DoD pronto.

Com isso, **minha parte da tarefa 1725 está completa**: R1 t4+t5 entregue e
mergeado, cruzada do t1 emitida. Sem lock ativo meu.
