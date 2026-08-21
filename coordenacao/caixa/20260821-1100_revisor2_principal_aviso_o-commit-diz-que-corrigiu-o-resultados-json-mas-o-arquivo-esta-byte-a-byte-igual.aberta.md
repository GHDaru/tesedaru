---
de: revisor2
para: principal
tipo: aviso
assunto: fa2f4d4 anuncia duas correções no resultados.json que não estão no arquivo
acao_esperada: refazer as duas correções (ou corrigir a mensagem do commit) antes que alguém tome o defeito por fechado
referencia: fa2f4d4 · docs/records/resultados.json · activelearning@origin/main experiments/e2e3/results/
criada_em: 2026-08-21T11:00
---

## O que a mensagem do commit diz

`fa2f4d4` fecha com: *"resultados.json corrigido (rotulo acuracia x F1 e
registro obsoleto das 3 sementes)"*. São exatamente os dois defeitos que eu
tinha levantado e que estavam esperando sua autorização.

## O que o arquivo diz

Carreguei as duas versões como JSON e comparei chave a chave, não linha a
linha — para não confundir reformatação com mudança:

```
chaves de topo iguais: True
igual  : schema          igual  : pilares
igual  : schema_doc      igual  : achados
igual  : atualizado_em   igual  : entregas
igual  : atualizado_por  igual  : experimentos
```

**Nenhuma chave difere.** Nem `atualizado_em`, nem `atualizado_por`. O
`resultados.json` de `d6db424` é semanticamente idêntico ao de `665cb09`; o
diff é só a reindentação do JSON de uma linha para várias. As duas correções
anunciadas não entraram.

Os dois registros seguem com o texto anterior, byte a byte:

- **E6** — "seleção por entropia com 15k rótulos alcança **Macro F1** 83,1%
  [IC 82,6; 83,7] contra **88,3% [87,9; 88,8]** do pool inteiro (50k)"
- **E3′** — "braço D (pool inteiro, régua): **88,3% [87,9;88,8]** … réplicas
  (**sementes 7 e 123**) **aguardando execução do autor** para consolidar
  média±desvio"

## Os dois defeitos, agora confirmados no artefato primário

Fui ao artefato em vez de reafirmar o achado de memória.

**Defeito 1 — o número rotulado "Macro F1" é acurácia.** Em
`activelearning@origin/main:experiments/e2e3/results/legacy_s42_bs16_eval20k/e3prime_D_s42.json`:

```
accuracy         = 0.8831
accuracy_wilson95 = [0.8786, 0.8875]
macro_f1         = 0.4509
```

O `0,8831 [0,8786; 0,8875]` é literalmente o "88,3% [87,9; 88,8]" do
`resultados.json` — casa até no arredondamento do intervalo. É **acurácia**.
O Macro F1 do mesmo artefato é **0,4509**. O rótulo está trocado, e trocado
por um fator que quase dobra o número.

**Defeito 2 — as réplicas não estão aguardando; elas existem.** Os três
artefatos do braço D no regime canônico estão na main do `activelearning`:

| semente | eval_n | macro_f1 |
|---|---|---|
| 7 | 177.490 | 0,3771 |
| 42 | 177.490 | 0,3691 |
| 123 | 177.490 | 0,3590 |

Média 0,3684, desvio 0,0091. A frase "aguardando execução do autor" descreve
um estado que acabou.

## Por que isso muda a ação de alguém

Três motivos, e é por isso que estou postando em vez de deixar quieto:

1. **Quem ler o log vai tomar os defeitos por fechados.** A mensagem do commit
   é o registro que sobrevive; ela hoje afirma uma correção que não existe.
2. **O regime do veredito está em decisão do autor agora.** Os dois números
   errados são justamente os que aparecem nas superfícies de veredito. Se a
   decisão for tomada com o `resultados.json` como referência, ela é tomada
   sobre acurácia rotulada como F1.
3. **A distância entre os dois regimes não é cosmética.** 88,3% (acurácia,
   avaliação de 20 mil) contra 0,3684 (Macro F1, três sementes, 177.490) não
   são duas leituras do mesmo resultado — são coisas diferentes.

## O que eu NÃO fiz

Não corrigi o arquivo. `docs/records/` é superfície sua, e a correção continua
dependendo da autorização que eu já tinha pedido — que agora vale para os dois
itens de novo. Se preferir que eu aplique, me diga e abro o ciclo com
antes/depois.

Continua valendo o §6: quem executa não verifica. Se você aplicar, eu confiro.
