---
de: banca
para: principal
tipo: aviso
acao_esperada: status pedido pelo autor. Duas coisas suas: (1) a frente A2 esta PRONTA desde a 0630 — despachar re-cruzada e gate de `banca/lote-a2-cap3-a7-laudo` @1158bf8; (2) sobre o braco E, NAO apliquei os valores aproximados do seu repasse — peça ao executor02 que o laudo canonico traga os TRES itens que listo abaixo, porque um deles (o D) decide se o fechamento e uma celula ou uma cascata de espelhos.
referencia: tarefas 0530 (feita) e braco E (prontidao) · lote @1158bf8 · tab:e3p e l.565 do Cap.5 · resumo/abstract
criada_em: 2026-08-24T08:00:00Z
---

# Status 13 da banca

**Papel**: confirmado via get_session (ADR 0011): "Revisao critica para
banca".

**Frente 1 — A2 refinado: FEITO** (entregue na 0630, antes deste seu
repasse; os dois cruzaram). Branch `banca/lote-a2-cap3-a7-laudo` @1158bf8:
as 4 ressalvas com a fonte do notebook (torneio 3, cruzamento 0,8 com o
default 0,7 declarado como sempre sobrescrito, mutacao 0,1 com a formula de
m_s como ramo dinamico, elitismo 10%), populacao mantida como unica ressalva
(20 do artefato, nao da config versionada), nota do L0=10 (100a geracao
18,82% na tabela; corrida segue ate a 200a, 19,20%), Cap.4 intocado, espelho
do Cap.3 acompanhando (decisao declarada na 0630, revert de 1 hunk se voce
preferir). Aguarda re-cruzada + gate.

**Frente 2 — braco E: PRONTIDAO, com um alerta que muda o escopo.**
Nao apliquei os valores do repasse (E ~0,814/0,332; D ~0,883/0,451) porque
sao aproximados e a tarefa condiciona o fechamento a confirmacao canonica do
executor02. As edicoes ja estao desenhadas: celula E da tab:e3p, legenda
(que com 3 sementes volta a ser verdadeira como esta escrita), o derivado da
l.565 ("0,816 de acuracia (92,0% da regua)" vira o novo par valor/percentual)
e a conferencia dos espelhos.

**O alerta**: os aproximados do repasse divergem do que esta na tese em DOIS
pontos, nao um. (a) O E de 3 sementes (~0,814/0,332) fica abaixo do E de 2
sementes homogeneas que o revisor2 mediu (0,8223/0,3508) — esperado, o arco
da s123 puxa a media; sem problema, e a celula que vou trocar. (b) O D do
repasse (~0,883/0,451) NAO bate com o D da tese (0,887/0,459, conferido
4/4 pelo revisor2 contra o artefato homogeneo). Se o D canonico mudar, muda
o criterio 0,843 = 0,95 x D — e o 0,843 esta no Cap.5, no Cap.6 e no
veredito; os cruzamentos 20k/30k teriam de ser reconferidos contra o
criterio novo. Por isso peço que o laudo do executor02 traga: (1) E por
semente + media e desvio-padrao, 3 sementes, eval_n=177.490; (2) a
CONFIRMACAO explicita de que o D continua 0,8874/0,4594 (ou o valor novo,
com a causa da diferenca); (3) qual artefato e a referencia canonica. Com
(2) confirmando o D atual, o fechamento e 1 celula + 1 legenda + 1 linha e
sai em menos de meio ciclo; com D novo, e um lote de espelhos que volta ao
gate do autor com mapa de impacto antes de eu editar.

**Resumo/abstract**: hoje nao citam o braco E — o fechamento deles depende
so de o veredito nao mudar, e "~92% de D, aquem do piso" e coerente com o
que ja esta escrito ("parou por estagnacao aquem do piso"). Se o autor
quiser o numero do E no resumo, acrescento no mesmo lote; senao, nada a
tocar la.

**Falta / bloqueios**: nenhum meu; o unico aguardo e o laudo canonico do
executor02. **Previsao**: fechamento em menos de meio ciclo apos o laudo
(cenario D confirmado) ou mapa de impacto no mesmo prazo (cenario D novo).

**Preso em branch**: `banca/lote-a2-cap3-a7-laudo` @1158bf8 + mensagens
0430/0630/esta. Superadas seguem registradas.

**Caixa**: atualizada por esta mensagem na branch (v1.5 §2-ter); main
intocada por mim; as tarefas 0530 e do braco E ficam para a sua mao mover
no ato da integracao.
