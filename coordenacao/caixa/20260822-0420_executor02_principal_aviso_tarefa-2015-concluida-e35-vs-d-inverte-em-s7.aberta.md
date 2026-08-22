---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR e levar ao autor — a regeração dos 25 braços (tarefa 2015) terminou e um achado muda o veredito do Cap. 5 sobre E35 vs D (deixa de ser unânime nas 3 sementes); marcar 20260821-2015 como concluída do seu lado (não alcanço a main); atualizar o plano com os novos números quando puder
referencia: activelearning branch claude/e3prime-seed-7-rwatey @4e33c9a (25 bracos + stats) · tarefa 20260821-2015 (main) · minha entrega anterior 20260818-0235 · dec-regerar-25-bracos-aprovado (decisoes.jsonl)
criada_em: 2026-08-22T04:20:00Z
---
**Tarefa 2015 concluída: 25/25 braços regerados com gradient clipping, sem
nenhum colapso, e as estatísticas recomputadas nas 3 sementes.** Achei uma
mudança de veredito que precisa subir ao autor — não é só "os números
tremeram um pouco".

## Execução

25 braços (8 na semente 42, pulando E25 que já estava corrigido; 8 na
semente 123, pulando E; 9 na semente 7, nenhum já corrigido) retreinados
com `bertimbau.py` já com `clip_grad_norm_` (commit `1dabdbb`). Saída com
sufixo `_bs16v2`, nada sobrescrito — os `_bs16` antigos continuam intactos
para comparação. Nenhum braço colapsou. Estatística (McNemar + bootstrap
pareado, 10k réplicas) recomputada sobre o conjunto 100% homogêneo em
`experiments/e2e3/results/homogeneo_clip/` (README lá com o detalhe
completo).

## O que NÃO mudou

- **Hipótese central (F1(A) ≥ 0,95×F1(D)): segue NÃO sustentada**, sem
  mudança material. A médio 0,2972 vs 0,95×D médio 0,4365 — gap ainda
  maior que antes em termos absolutos.
- **B > C (seleção do laço bate aleatório): segue consistente** nas 3
  sementes, positivo e significativo.
- **Piso de orçamento por acurácia: continua em E20 (40% do pool)**.

## O que MUDOU — precisa de decisão do autor

**E35 > D deixava de ser unânime.** Na varredura mista (0235) eu tinha
reportado significância forte nas 3 sementes, sempre na mesma direção.
Agora, com os 27 braços saindo do mesmo código:

| semente | resultado | detalhe |
|---|---|---|
| 42 | E35 > D, significativo | ΔF1 bootstrap +0,0081 [+0,0051; +0,0111], McNemar p≈6,7e-15 |
| 123 | E35 > D, significativo | ΔF1 bootstrap +0,0077 [+0,0043; +0,0113], McNemar p≈0,0052 |
| **7** | **E35 < D, significativo (invertido)** | ΔF1 bootstrap **-0,0050 [-0,0084; -0,0017]** (IC não cruza zero); McNemar por acurácia não significativo (p=0,67 — o efeito é só em Macro F1, não em acurácia) |

Causa provável, não confirmada: D/s7 subiu bastante com o clipping (Macro
F1 0,4435→0,4625, o maior salto de D entre as 3 sementes), enquanto
E35/s7 quase não mudou (0,4592→0,4575). D "alcançou" E35 nessa semente
específica. Não investiguei mais fundo — é constatação, não diagnóstico
completo; digam se querem que eu aprofunde.

**Piso de orçamento por F1 subiu de E25 (50%) para E30 (60%).** Mesma
causa: D médio subiu (0,4508→0,4594) mais que E25 médio ficou parado
(0,4324→0,4324, quase idêntico — E25/s42 nem foi retreinado, é a
referência fixa). 0,95×D passou de 0,4283 para 0,4365, e o F1 de E25 não
acompanhou.

## Para o Cap. 5

A alegação "menos é mais, também no transformer" (E35 supera a régua) não
é mais 3-de-3 — é 2-de-3, com uma inversão estatisticamente significativa
na semente 7. Isso é diferente de "efeito frágil que sobe e desce com
ruído": nas 3 sementes o efeito é real e mensurável, só que não é sempre a
favor de E35. Não decido a redação — só que a frase "supera a régua nas 3
sementes" deixou de ser verdadeira e precisa de ajuste antes de qualquer
texto novo sair.

## Fechamento

Não consigo fazer `git mv` na `main` (sessão restrita à branch designada).
Peço que marque `20260821-2015` como `.concluida` do seu lado e leve isto
ao autor. Plano (`docs/records/plano-revisao.json`) não toquei — está
muitas versões à frente do que tenho localmente; deixo a atualização com
vocês para não arriscar conflito.

Sem tarefa pendente da minha fila agora. Disponível para o E6 se
executor01 preferir passar (2020), ou qualquer outra frente.
