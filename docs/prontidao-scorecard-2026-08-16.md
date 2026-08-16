# Scorecard de prontidão para a banca — Rodada 5 (2026-08-16)

Aplicação do framework `docs/analise-prontidao-framework.md`.
[B] = bloqueante · [NB] = não-bloqueante · ✅ passa · ❌ não passa · ⬜ pendente de terceiro.

## Veredito: **NÃO PRONTO** (7 gates bloqueantes abertos)

A ciência está fechada e a integridade técnica do documento está limpa; o que
bloqueia o envio é (a) a escrita — 6 arquivos entre severidade 6 e 9 na
auditoria anti-slop, com 1 erro factual no resumo/abstract — e (b) quatro
confirmações administrativas UFPR/PPGMNE nunca executadas.

## D1. Ciência fechada — 4/4

| Gate | Estado | Evidência |
|---|---|---|
| G1.1 [B] hipótese testada e respondida | ✅ | E3′ com varredura; "refutada em 30%, sustentada em ~50%, causa identificada" (parecer R5) |
| G1.2 [B] números rastreáveis | ✅ | regra de ouro auditada (R5: proveniência dupla verificada por cruzamento automático) |
| G1.3 [B] nenhum achado fora do texto | ✅ | auditoria de achados 18/07 |
| G1.4 [NB] limitações com direção de viés | ✅ | Cap. 3 ameaças à validade (R1-A5) — 5 alegações pontuais a ancorar (ver D2) |

## D2. Escrita anti-slop — 1/5 ⛔

| Gate | Estado | Evidência |
|---|---|---|
| G2.1 [B] humanização com gate em todos os arquivos | ❌ | só Cap. 1 (merge 2effcfc); faltam 7 ciclos: resumo+abstract, 6, 2, 5, 3, 4, a7/a4 |
| G2.2 [B] travessões ≤5/1000 por arquivo | ❌ | 8 arquivos acima: abstract 22,9 · resumo 21,9 · cap6 20,4 · cap2 17,7 · a7 14,8 · cap5 13,0 · cap3 12,7 · cap4 11,8 |
| G2.3 [B] zero fórmula enumerativa/staccato/aforismo | ❌ | ~29 fórmulas de molde, 6 staccatos (Cap. 5), fecho aforístico (Cap. 6 L195-197), slogan tripartite (L181-185) |
| G2.4 [NB] vocabulário IA/atribuições vagas = 0 | ✅ | script + 4 auditores: zero em toda a tese |
| G2.5 [NB] cadência variada nos parágrafos apontados | ❌ | 12 parágrafos-metrônomo mapeados (`auditoria-escrita-2026-08-16.md`) |

**Bloqueante NOVO achado na auditoria (classificar em G2.3/D5):** resumo e
abstract anunciam "Quatro resultados principais" e enumeram cinco — erro
factual, correção obrigatória no 1º ciclo de humanização.

## D3. Conformidade SiBi/UFPR — 2/4

| Gate | Estado | Evidência |
|---|---|---|
| G3.1 [B] elementos obrigatórios na ordem SiBi | ✅ | quadro cruzado em `normas-ufpr-ppgmne-e-skills.md`; ordem do `principal.tex` conforme |
| G3.2 [B] ficha catalográfica oficial (com DOI da base) | ⬜❌ | placeholder local; solicitar à biblioteca do programa |
| G3.3 [B] palavras-chave PT/EN explícitas | ✅ | `\pchave`/`\keyword` em `principal.tex` L62-63 |
| G3.4 [NB] posição da declaração de IA confirmada | ⬜ | elemento fora do quadro SiBi; confirmar com o programa |

## D4. Conformidade PPGMNE — 0/4 ⛔ (tudo dependente de ação externa)

| Gate | Estado | Evidência |
|---|---|---|
| G4.1 [B] template confirmado (`ppginf.cls` × modelo ABNT UFPR) | ⬜❌ | risco identificado na rodada 3; blog do programa aponta ABNTeX — decidir com orientador/secretaria e registrar em `records/decisoes.jsonl` |
| G4.2 [B] Lattes completo | ⬜❌ | ação do autor |
| G4.3 [B] checklist de defesa aprovado pela coordenação | ⬜❌ | pré-requisito do SIGA |
| G4.4 [NB] portarias de banca conferidas (H-index) | ⬜ | com o orientador |

## D5. Integridade técnica — 3/4

| Gate | Estado | Evidência |
|---|---|---|
| G5.1 [B] compila 0 erros / 0 refs / 0 warnings | ✅* | último registro: diário 17-18/07. *Revalidar após cada ciclo de humanização (sem LaTeX neste container; rodar local) |
| G5.2 [B] 0 citações órfãs, 0 \ref quebrado | ✅ | script desta sessão: 152 citações, todas no bib; 0 refs quebradas |
| G5.3 [NB] figuras/tabelas citadas; siglas expandidas | ✅ | passe de estilo 17-18/07 (diário) |
| G5.4 [NB] `a_sanear/` vazio | ❌ | 6 arquivos (5 já triados `_TRIAGEM_*` — basta remover/arquivar; 1 `tesedaru.pdf` deslocado) |

## D6. Pendências operacionais (R5 §4) — 0/6

| Gate | Estado | Dono |
|---|---|---|
| G6.1 [B] frase de proveniência dupla no Cap. 3 | ❌ | agente, sob OK do autor (10 min) |
| G6.2 [NB] licença Kaggle CC BY 4.0 | ⬜ | autor (5 min) |
| G6.3 [NB] rotação das 5 chaves de API | ⬜ | autor (15 min) |
| G6.4 [NB] autoria/ordem dos 5 artigos | ⬜ | autor + orientador |
| G6.5 [NB] DOI Zenodo do código | ⬜ | autor + agente (30 min) |
| G6.6 [NB] proofreading final PT | ❌ | após D2 fechar (para não retrabalhar) |

## Caminho crítico (ordem de execução recomendada)

1. **Ciclo humanize-02: resumo + abstract** — pior severidade (9/9), menor
   volume (~1.400 palavras), corrige o erro factual "quatro→cinco" e o
   "resposta primeiro" do veredito. Alavancagem máxima por hora investida.
2. **G6.1** frase de proveniência dupla (10 min, já aprovada em tese pelo R5).
3. **Disparar em paralelo as confirmações externas** (não dependem de texto):
   G4.1 template (e-mail à secretaria/orientador — maior risco de retrabalho
   se a resposta for "ABNT"), G3.2 ficha catalográfica, G4.2 Lattes.
4. **Ciclos humanize-03 a 08**: Cap. 6 → Cap. 2 → Cap. 5 → Cap. 3 → Cap. 4 →
   a7+a4, cada um com gate humano e recompilação (G5.1).
5. **G5.4** limpar `a_sanear/` (15 min) e **G6.6** proofreading final único.
6. Reaplicar este scorecard; com D2 e D6.1 verdes e as confirmações D3/D4
   respondidas, o veredito migra para PRONTO (ou COM RESSALVAS se restarem
   apenas NB).

Estimativa de esforço do que depende só de texto (itens 1, 2, 4, 5): ~7
ciclos de edição com gate. Nenhum experimento novo é necessário.
