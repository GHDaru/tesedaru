---
de: executor02
para: principal
tipo: aviso
acao_esperada: URGENTE — levar ao autor ANTES de qualquer edição adicional no Cap. 5 §res-e3p-varredura; a seção cita um resultado que o regime canônico contradiz nas 3 sementes; decisão de como reescrever é do autor
referencia: activelearning@3d3bca3 (branch claude/e3prime-seed-7-rwatey) · tarefa 20260816-2152 (concluída) · 5-resultados-falco/texto.tex:547-590 (\label{sec:res-e3p-varredura}) · plano v40
criada_em: 2026-08-17T14:50:00Z
---
Executando a tarefa 2152 (McNemar/bootstrap canônicos), encontrei uma
contradição direta com o texto já escrito no Cap. 5. Não é ajuste de número —
é uma das três conclusões da seção que não se sustenta mais.

## O que o Cap. 5 afirma hoje (5-resultados-falco/texto.tex:588-592)

> "(iii) Menos é mais, também no transformer: o braço E35 (35 mil rótulos
> ativamente selecionados) supera a régua de supervisão completa do pool
> tanto em acurácia (88,6% vs. 88,3%) quanto em Macro F1 (0,463 vs. 0,451)
> — os 15 mil rótulos finais [...] não só são dispensáveis como degradam o
> modelo forte."

Esses números (88,6/0,463 para E35; 88,3/0,451 para D) são do regime LEGADO
(bs16, avaliação em 20.092 itens) — o McNemar legado tinha p=0,103
("sem diferença detectável", não "E35 supera D com significância").

## O que os dados canônicos mostram — nas 3 sementes, sem exceção

| semente | E35 acc | D acc | E35 F1 | D F1 | E35 supera D? |
|---|---|---|---|---|---|
| 42 | 0,8656 | 0,8694 | 0,3660 | 0,3691 | NÃO (nas duas métricas) |
| 7 | 0,8592 | 0,8678 | 0,3440 | 0,3771 | NÃO (nas duas métricas) |
| 123 | 0,8582 | 0,8652 | 0,3461 | 0,3590 | NÃO (nas duas métricas) |

E com estatística pareada rigorosa (McNemar + bootstrap, 10k réplicas,
`activelearning@3d3bca3`):

| semente | Δacc | p (McNemar) | ΔF1 | IC95% (F1) |
|---|---|---|---|---|
| 42 | −0,0038 | 2,5e-15 | −0,0030 | [−0,0055; −0,0008] |
| 7 | −0,0087 | 1,6e-62 | −0,0330 | [−0,0352; −0,0306] |
| 123 | −0,0070 | 3,3e-40 | −0,0129 | [−0,0149; −0,0111] |

**As 3 sementes concordam: D bate E35, com significância muito forte
(p<1e-14 em todas as 3), em ambas as métricas.** Não é sensibilidade a
semente — é o oposto: é o achado mais robusto que produzimos no E3′ inteiro.

## Por que os números legados diziam o contrário

Duas mudanças de regime ao mesmo tempo (documentadas desde a decisão da
s42 canônica): lote 16→128 no ajuste fino, e avaliação em 20.092→177.490
itens. A população maior expõe mais classes raras — o E35 aparentemente
"vencia" no regime antigo porque a amostra de 20k sub-representava
justamente as classes onde ter mais dados (D) ajuda mais. Isso também
explica por que a anomalia do revisor2 (ponto fora do próprio IC bootstrap
em D/E35, `20260817-0545`) **não se reproduz** no canônico: amostra maior,
menos classes desaparecendo em cada reamostragem, menos viés.

## As outras duas alegações da seção também precisam de revisão

- **(i) "F1 cruza em 25 mil (50%)"**: no canônico, só E35 (70%) cruza o
  critério de F1 (0,95×F1(D)) — E25 e E30 cruzam só acurácia. O piso
  correto passa de 50% para ~70% do pool.
- **(ii) "gargalo era a política de parada"**: continua defensável — o F1
  cresce monotonicamente com o orçamento nas 3 sementes — só a alegação
  (iii), específica sobre superar D, cai.

## Achado secundário, sensível a semente (não generalizar sem cuidado)

Os contrastes A−B e B−C trocam de sinal em F1 entre sementes (a acurácia é
consistente: sempre penaliza o oráculo em A−B, sempre favorece o aleatório
em B−C). Cada semente individual é estatisticamente significativa (CI
exclui zero em todos os 9 casos), mas a direção diverge — s42 destoa de
s7/s123 no B−C. Ressalva de desenho: o braço C sorteia com a PRÓPRIA
semente de treino (`run_e3prime.py`), então parte dessa variação é "qual
subconjunto aleatório caiu" e não só ruído de treino do BERTimbau. Tabela
completa em `activelearning@3d3bca3`. Não bloqueia nada — é informação para
quem escrever o parágrafo do A−B/B−C, se ele citar significância por
semente em vez da média das 3 (que já reportei antes: A−B≈0 no agregado,
B−C positivo no agregado).

## O que fiz

1. Recomputei McNemar+bootstrap sobre as predições canônicas das 3 sementes
   (tarefa 2152 pedia só s42; estendi às 3 porque o achado do E35−D exigia
   confirmação antes de generalizar).
2. Preservei os arquivos legados em `legacy_s42_bs16_eval20k/` (git mv, nada
   apagado) — README da pasta documenta a comparação regime a regime.
3. Verifiquei a anomalia do revisor2: não se reproduz no canônico, com
   explicação de causa.
4. Tarefa 2152 movida para `.concluida`. Plano v40 com item novo
   `e3p-estatisticas-canonicas`.

## O que preciso de você

Isto é uma decisão de conteúdo do Cap. 5, fora do meu escopo (não edito
texto). Sugiro ao autor duas opções, sem escolher por ele:

- **(a)** Reescrever a seção com os números canônicos: a conclusão vira
  "o FALCO com política de parada ancorada no modelo forte precisa de
  ~70% do pool (não 50%) para igualar D — e mesmo assim não o supera; a
  vantagem 'menos é mais' não se sustenta com avaliação rigorosa."
  Ainda é um resultado publicável (o F1 cresce continuamente e quase
  fecha a distância), só menos favorável que o atual.
- **(b)** Se o autor preferir investigar mais antes de reescrever — por
  exemplo, rodar a mesma varredura (E20-E35) com o teste de sub-treino já
  autorizado (tarefa 2220, que assumo agora) para descartar se o lote 128
  está sub-treinando também os braços E — eu sigo essa ordem.

Não travo em nenhuma das duas: sigo para a tarefa 2220 (sub-treino, braço D)
enquanto aguardo, porque ela mesma pode informar esta decisão (se o lote 16
também mudar o resultado de D isoladamente, isso é evidência adicional para
o Cap. 5).
