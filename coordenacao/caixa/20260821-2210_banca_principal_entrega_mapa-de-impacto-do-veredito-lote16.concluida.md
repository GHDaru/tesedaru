---
de: banca
para: principal
tipo: entrega
acao_esperada: conferir este MAPA contra os quadros do revisor2 e levar o eixo ao autor (tarefa 2130 pede o plano antes do texto — este é o plano); com o teu OK, a reescrita única sai numa branch só, com os PROVISORIO marcados
referencia: tarefa 20260821-2130 · entrega 0235 do executor02 (k=3, 27 braços) · insumos 1-6 · docs/pre-registro/LEIA-ME.md
criada_em: 2026-08-21T22:10:00Z
---

# MAPA DE IMPACTO — local por local (V = muda valor · C = muda conclusão · Q = só qualificação/denominador)

## Cap. 5 (zona de veredito congelada + tabelas)

1. `tab:e3p` (l.505-520) — **V + estrutura**. Todas as linhas trocam valor
   (D: 88,3%/0,451 -> 0,8829±0,0028/0,4508±0,0067; E: 83,1%/0,380 ->
   0,8142±0,0192/0,3317±0,0341; A/B/C ganham os números lote16) e a tabela
   ganha média±desvio (k=3). O braço A muda de cardinalidade (11.936
   rótulos). CONCLUSÃO da tabela (A não atinge) mantém-se.
2. Prosa da síntese (l.546, 559) — **V + C (enfraquece "quase")**: "83,1%
   = 94,1% da régua, a 0,75 p.p." vira 0,8142/0,8829 = 92,2%, a ~2,5 p.p.
   O "quase se sustenta em acurácia" do braço E perde força; a redação nova
   apoia o veredito na varredura, não no E.
3. `tab:e3p-sweep` (l.581-600) — **V**; coluna de veredito acc/F1 é
   recalculada. Pisos provisórios: acc cruza em E20 (8,6% da base), F1 em
   E25 (10,8%). Curiosidade útil: o piso do F1 VOLTA a 25 mil — a redação
   congelada @d0d35ed vira matéria-prima aproveitável quase inteira.
4. E35 vs D (l.611-612) — **C, para melhor**: era "+0,012 (bootstrap) e
   EMPATA em acurácia (p=0,10)"; agora SUPERA em ambas as métricas com
   McNemar p entre 1e-8 e 1e-58, nas 3 sementes. "Menos é mais" sobe de
   ponto estimado para efeito pareado significativo.
5. `tab:e6` (l.423) e prosa do E6 — **Q**: experimento de classificadores
   leves, não tocado pelo regime de treino do BERTimbau. Conferir apenas as
   referências cruzadas à trajetória usada pelo braço E.

## Resumo e abstract (congelados)

6. Item (v) — **V + C**: critério em acurácia (pré-registro), piso dentro do
   teto, E35 supera D em AMBAS as métricas 3/3, braço A não atinge (gap 28%)
   com 5,2% da base, A>B em F1 (oráculo bate gabarito). O par
   "refutada/atendida" segue a decisão já tomada (sem refutação; espinha
   "atingível dentro do teto × execução que parou cedo").
7. Item (v), "parando por estagnação com 32--40% do orçamento" — **V**:
   número do pipeline antigo; o braço A canônico parou com 11.936 rótulos.
   Parágrafo do braço A ISOLADO (ordem da tarefa 1600) para a regeração
   trocar uma frase.
8. Item (iv), "78% do Macro F1 com 15% dos rótulos" — **Q**: é o E1
   (PVBin, não afetado); só ganha denominador explícito (15% do orçamento
   daquele experimento), para não colidir com o teto de 15% da base.

## Cap. 6 (congelado)

9. l.55-67 (veredito 1), l.194-204 (veredito 2), l.160 e l.209 (pisos em %
   do pool) — **V + C**: mesma cadeia do item 6; os "40%/50% do pool" viram
   8,6%/10,8% da base (E20/E25) com PROVISORIO.

## Cap. 3 (NÃO reabrir tabela; itens para o trem da higiene)

10. **LOCAL QUE NINGUÉM LISTOU** — l.~614-616: "o E3$'$ executa-se com
    semente única e estatuto descritivo, como o E6". FALSO após as 3
    sementes canônicas — **C**. Corrigir no trem da higiene do Cap.3 (não
    agora): "executa-se com três sementes e análise pareada; o desenho de 8
    sementes permanece como extensão".
11. Sub-treino do lote 128 — **frase nova** (achado metodológico com teste
    de controle): entra na seção do E3'/reprodutibilidade no mesmo trem.

# Ordem de aplicação (mínima colisão)

1. **JÁ, branch própria**: tarefa 1210 (pré-registrado + lastro Cap.1) —
   não toca zona congelada nem tabela. ENTREGO NA SEQUÊNCIA DESTA MENSAGEM.
2. **Após teu OK neste mapa**: reescrita única (resumo + abstract + síntese
   Cap.5 + Cap.6 + as DUAS tabelas do Cap.5 na mesma branch — mesma
   superfície, um merge só). Cruzada do revisor2.
3. **Depois do merge da reescrita**: trem da higiene do Cap.3 (pool como
   referência, registro de percurso, l.656, teto no critério do E3',
   semente-única->3-sementes, frase do sub-treino) por cima do Cap.3
   re-derivado pela F4 — uma vez só.
4. **Pós-regeração dos 25 braços**: troca mecânica dos marcados.

# O que espera a regeração (e o que não)

- Esperam: valores das duas tabelas e frases numéricas marcadas com
  `% PROVISORIO-ate-regeracao`.
- Não esperam: eixo conceitual, qualificações (gabarito/oráculo), pré-
  registro, lastro, estrutura dos parágrafos, veredito qualitativo.
- REGRA DE MARGEM FINA (acatada): o E25 cruza o F1 por 0,0041 — nenhuma
  frase de prosa fixa "25 mil" como piso do F1; a prosa diz "dentro do
  teto" e aponta a tabela, que é quem carrega o número.
