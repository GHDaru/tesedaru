---
de: principal
para: banca
tipo: tarefa
acao_esperada: (autor aprovou a F6) reforçar o Cap. 4 — hoje com ZERO citações — escrevendo discussão nova e interlocução com a literatura, honrando os 6 fichamentos que o prometem. DEPOIS de fechar o veredito (tarefa 1030), que tem prioridade. Branch própria; cruzada do revisor2; gate do autor.
referencia: dec-reforco-cap4 (F6) aprovada pelo autor 2026-08-22 · 6 fichamentos que apontam o Cap.4 · 4-resultados-l0/
criada_em: 2026-08-22T12:00:00Z
---

O Cap. 4 (resultados L0: sensibilidade, AG, DRI-SL) discute os próprios
números mas não conversa com a literatura — uma banca pergunta "e o que a
literatura diz sobre isso?". Escreva a interlocução:
- identifique os 6 fichamentos que prometem o Cap. 4 e traga cada um para onde
  ele dialoga (composição de conjunto inicial, cold-start, diversidade, AG em
  seleção de features/instâncias);
- discussão nova: por que o DRI-SL sem rótulo supera o AG supervisionado à luz
  do que a literatura esperava; onde o resultado confirma e onde surpreende.
- é ESCRITA nova, não realocação — o único ponto da refatoração que gera
  conteúdo. Sem inventar resultado: só interpretação e diálogo, com cite real.
Cruzada do revisor2 (checa que todo cite novo existe e é fichado, ADR 0012).

## Resultado (banca, 2026-08-22)

Entregue em `banca/f6-cap4-literatura` @aacdbbf (base: `banca/cap4-linha117`
@460a7d1, ja aprovada na cruzada do revisor2 as 2300). O Cap. 4 sai de 0 para
11 citacoes. As 6 fichas que o prometiam foram honradas onde cada uma dialoga:
Daru2024Dissertacao e Daru2022 (teto supervisionado da base, §4.1), Yu2023Patron
(variancia com poucos rotulos §4.1; regime de partida a frio e reducao de
dispersao §4.3), Griesshaber2020 (L0 arbitrario na pratica corrente §4.1;
dispersao §4.3; pool reduzido por custo §4.4), Karl2023 (base real vs
benchmarks, abertura), Zhang2023LLMaAA (contraste de regime §4.3). Somou-se
Hacohen2022TypiClust (ja interlocutora do Cap. 2) para a transicao de regime.
Discussao nova do porque o DRI-SL sem rotulo supera o AG supervisionado:
confirmacao da expectativa de representatividade em orcamento baixo, surpresa
delimitada, leitura de variancia. check-bib: PROBLEMAS nenhum;
check-uso-declarado: zero promessas pendentes ao Cap. 4; check-travessao: ok.
Proximo passo: cruzada do revisor2 (todo cite novo existe e e fichado, ADR
0012) e gate do autor via principal.
