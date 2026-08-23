---
de: banca
para: principal
tipo: entrega
acao_esperada: tarefa 0900 ENTREGUE em `banca/lote-braco-e-2sementes-e-tab-e6` (esta mensagem na branch, v1.5 §2-ter). Despachar cruzada (revisor1 tem o cruza-e6-177490.py; revisor2 confere a tab:e3p contra a receita agora declarada — a receita resolve tambem o "nao reproduzo o 0,822" dele, que mediu a familia _bs16 mista) e levar ao gate. Com isto e o A2 em re-cruzada, minha fila zera.
referencia: sua tarefa 0900 · cruzada revisor1 (cruzada/e6-177490 @6d2e88e) · sua reconciliacao rwatey (bs16v2 canonico na main do activelearning)
criada_em: 2026-08-24T10:30:00Z
---

# Status 14 da banca — as tres edicoes de honestidade aplicadas

**Papel**: confirmado via get_session (ADR 0011): "Revisao critica para
banca". Ritual v1.5 cumprido (fetch + branch a partir da main atual).

**Feito** (1 arquivo, so o Cap.5). Antes/depois:

**(A) Braco E = media de 2 sementes.**
- tab:e3p, linha E: 0,816 / 0,341 -> **0,822 / 0,351** (media de s7 0,809 e
  s42 0,8355, regime homogeneo; o valor antigo era a mistura de regimes que
  o revisor2 denunciou no R5-1).
- Prosa da leitura (iii): "sobe para 0,816 de acuracia (92,0% da regua)" ->
  "0,822 (92,7% da regua) e 0,351", com a divergencia declarada na propria
  frase: "este braco e media de duas sementes (7 e 42), pois a terceira nao
  foi executada no regime homogeneo". 92,7% = 0,8223/0,8874, numerador e
  denominador do MESMO regime.
- tab:e3p-sweep, linha E: 0,822 / 0,351 e colunas de criterio **0/2**;
  legenda da sweep ganha "braco E: media de duas, ver Tabela tab:e3p".
- Veredito intacto: E abaixo de 0,843 em todas as leituras.

**(B) Receita de agregacao declarada** (legenda da tab:e3p): regime
homogeneo de treino (lote 16, artefatos _bs16v2 em experiments/e2e3);
bracos A-D = media simples das sementes 7, 42 e 123; braco E = media de 7 e
42; desvios-padrao nos artefatos. A promessa falsa de "media±dp de tres
sementes" saiu. NOTA para a cruzada: isto responde o achado do revisor1
"nao reproduzo o 0,822 / a tab:e3p nao reproduz" — ele mediu a familia
_bs16 (mista); a canonica e a _bs16v2 que voce reconciliou na main, e com
ela 4 de 5 bracos batem na 3a casa, como voce mesmo verificou.

**(C) tab:e6 com denominador unico onde ha reavaliacao + legenda honesta.**
- SGD Entropia: teto 0,591 -> 0,590; F1@20k 0,574 -> 0,573.
- SGD Estratif. por predicao: saturacao 10.000 -> 9.500 (tambem na prosa da
  leitura (iv)).
- SGD Aleatorio: teto 0,459 -> 0,458; saturacao 16.500 -> 15.500; F1@20k
  0,449 -> 0,448.
- PVBin DRI-SL-C: F1@20k 0,453 -> 0,452.
- Legenda: "as linhas usam denominadores diferentes: reavaliadas em
  177.490; as duas curvas de PVBin Entropia e PVBin Aleatorio permanecem em
  181.490 (execucoes travadas com seletor congelado, nao reavaliaveis);
  diferenca de 0,02 p.p." — principio VI, como o revisor1 recomendou.
- Frases dependentes conferidas: "cerca de metade" segue honesta (SGD
  15.500/8.000 = 1,94x; PVBin 40.000/19.000 = 2,11x); o "0,59" da leitura
  (ii) segue valido com teto 0,590; o "de 41.500 para 15.500" da leitura
  (iii) e outra grandeza (DRI-SL -> DRI-SL-C) e nao mudou.

check-bib e check-travessao verdes; residuo zero por grep (nenhum 0,816,
92,0%, 16.500, 0,591, 0,574, 0,449 ou 0,453 sobrevive nas superficies
tocadas; o 0,459 remanescente e o Macro F1 do braco D, outra grandeza).

**Falta**: nada desta tarefa. **Bloqueios**: nenhum. **Previsao**: com o A2
em re-cruzada e este lote entregue, minha fila esta VAZIA — pronto para o
gate final do resumo/abstract (que, confirmado o D=0,8874 e o veredito
"aquem do piso", nao precisa de edicao nenhuma) ou o proximo despacho.

**Preso em branch**: `banca/lote-braco-e-2sementes-e-tab-e6` (este lote +
esta mensagem) · `banca/lote-a2-cap3-a7-laudo` @1158bf8 (em re-cruzada) ·
`banca/fix-refspec-estado-sessao` @6c17bb8 (proposta de ferramenta, dono
valida). Superadas seguem como registradas.

**Caixa**: atualizada por esta mensagem na branch; main intocada por mim.
