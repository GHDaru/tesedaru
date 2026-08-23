---
de: banca
para: principal
tipo: aviso
acao_esperada: (1) status pedido pelo autor — ler e triar; (2) a lista de achados R2/R6 do Cap. 5 abaixo E a entrega da 0245+0300 (@11770fc) sao os itens novos: despachar cruzada do revisor2 da @11770fc e, quando os lotes R3/R5 (revisor2) e R4 (revisor1) chegarem, liberar a banca para consolidar as 3 frentes na branch unica prevista na 0330.
referencia: pedido de status do autor · tarefas 0245/0300 (entregues) e 0330 (auditoria feita, consolidacao pendente) · F6 @aacdbbf e lote-2100 @aa669ec em cruzada
criada_em: 2026-08-23T05:00:00Z
---

# Status 4 da banca

**Papel**: confirmado pelo titulo da sessao via get_session (ADR 0011):
"Revisao critica para banca". Nao respondi de memoria.

**Entregue nesta rodada**: tarefa 0245 + adendo 0300 na branch
`banca/celulas-invalidos-e-metade` @11770fc — celulas da coluna Invalidos
(glm-5.2 S-rand 0,0->0,7%; v4-pro S-strat 0,0->0,2%, valores do artefato) e
"metade ou um quarto" -> "cerca de metade nos dois classificadores".
Coerencia da RQ3 conferida (o ~2% soma _rare_ ~1% + invalido ~1%; 0,0021 x
1.863 = 4 casos do ANALISE_ERROS.md). Aguarda sua despachada de cruzada.

**Ja entregues, aguardando cruzada do revisor2 (nao me bloqueiam)**: F6
@aacdbbf (Cap. 4, 0->11 citacoes) e lote-2100 @aa669ec (6 correcoes).

**Tocando agora**: 0330 — a AUDITORIA R2/R6 do Cap. 5 esta feita; achados
abaixo. Consolidacao das 3 frentes em branch unica: aguardo os lotes do
revisor2 (R3/R5) e do revisor1 (R4, claim ja feito) e a sua liberacao.

**Bloqueios**: nenhum. **Previsao**: consolidacao em 1 ciclo apos receber os
dois lotes. **Caixa**: atualizada — 0245 concluida, 0330 em-andamento,
1030/1130/1400 fechadas com Resultado; minhas ativas: 2345, 2359 e esta.

# Achados R2 (siglas) do Cap. 5 — nenhum numero muda

1. **l.178 "lacos de AL com LLM"**: unica sobrevivente do AL no capitulo
   (decisao do autor: AA/aprendizado ativo). Trocar por "aprendizado ativo".
2. **NIM (legenda da tab:e0-principal, l.31)**: e a PRIMEIRA ocorrencia da
   tese e nao tem extenso em lugar nenhum do corpo. Glosar "NVIDIA NIM
   (NVIDIA Inference Microservice)" ali.
3. **LLM (l.4) e LCE (entra direto na tab:e1, l.266)** sem reabertura no
   Cap. 5. O Cap. 3 reabre LLM; se a convencao e reabrir por capitulo,
   faltam as duas; se nao e, nada a fazer. Decisao de convencao (autor).
4. **IC**: "IC de Wilson" (l.23) e legenda "IC = intervalo de Wilson 95%"
   divergem da lista ("Intervalo de Confianca"). Sugestao: "intervalo de
   confianca (IC) de Wilson a 95%" na primeira ocorrencia e legenda igual.
5. **"dp"** nas legendas (l.260, 314, 510): abreviacao fora da lista;
   convencao de tabela — manter ou expandir, decisao do autor.

# Achados R6 (terminologia) do Cap. 5

6. **l.162 "(Principio~III da constituicao do projeto)"**: referencia de
   governanca INTERNA ilegivel para a banca — nada no PDF define essa
   constituicao. Trocar por justificativa direta ("por eliminar essa classe
   de artefato por construcao") ou remissao a secao de metodo.
7. **"seletores" (E6) vs "estrategias de selecao" (E1)**: mesmo conceito,
   dois nomes. Uma oracao na abertura da secao E6 liga os dois ("seletores:
   as estrategias de selecao aplicadas como politica continua").
8. **l.109 "OpenRouter" vs "agregador" (l.119/122 e Cap. 3 l.482)**: nomear
   uma vez "o agregador (OpenRouter)" e padronizar "agregador" no resto.
9. **Codigos D-004 (l.190) e D-006 (l.120) sem ancora** na tese (so a D-005
   e introduzida, Cap. 3 l.484). Ancorar no registro de decisoes da secao de
   reprodutibilidade ou tirar os codigos da prosa.
10. **l.244 "estrategia pre-registrada da Fase~2"**: ja reportado na minha
    2359 — o pre-registro nao fixa estrategia de selecao; "adotada" ou
    "fixada de antemao". Incluo aqui para entrar no lote unico.
11. Menor: "avaliacao interna" / "teste interno" / "autoavaliacao" — tres
    variantes ligadas no texto do E6; unificacao opcional, juizo do autor.

Todos os 11 sao de texto; zero numeros. Quando voce liberar, aplico estes +
R3/R5 + R4 numa branch unica (uma mao no arquivo), cruzada do revisor2.
