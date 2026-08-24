# Matriz de pendências — FALCO (tese)

**Criada em:** 2026-08-24 · **Base:** v1 entregue na main @`2b07f8d` (gate do bloco A2 + braço E + fix §2.2.3).

## Regra desta fase (decisão do autor)

1. **Achados congelam.** Nada mais de mexer em números, artefatos ou executar código. O que já foi feito **vale como verdade** para a v1.
2. **Entregar a v1 sem se justificar.** Autocríticas ficam **fora do texto** da v1; entram aqui como pendência.
3. **Esta matriz é o registro** do que ficou aberto. O autor conduz a correção de metodologia/resultados sobre a base v1; depois voltamos às R's.
4. Qualquer novo achado a partir de agora → **entra aqui, não altera o texto agora.**

## Legenda

- **Severidade:** 🔴 Alta (pode inverter/afetar conclusão) · 🟡 Média (reprodutibilidade/rastreabilidade) · ⚪ Baixa (estilo/fragilidade/nota).
- **Tipo:** CIE científico · REP reprodutibilidade · EST estrutural · STY estilo/autocrítica.
- **Status:** ABERTA · FECHADA-NA-V1 (já resolvido) · DECIDIDA-NÃO-REABRIR.

## Tabela

| ID | Sev | Tipo | Item | Onde | Ação futura | Status |
|----|-----|------|------|------|-------------|--------|
| P-01 | 🔴 | CIE | Fase 3 do FALCO: p-valor da superioridade sem lastro no artefato. CRUZADA E CONFIRMADA em 2026-08-24 (leitura direta do principal em e0_mcnemar.json): S-strat pro×flash b=73,c=91,p=0,1844 (prosa imprime b=43,c=16,p<0,001); escopo ampliado: p=0,061 do empate pro×gpt-4o não existe no artefato (0,52/0,29) e 'nemotron abaixo apenas do v4-pro' é falso (abaixo também do gpt-4o nas duas amostras e do flash na S-strat). A tabela de pareamentos McNemar pedida pelo autor (§5.1.1) fica ADIADA junto (rascunho pronto do artefato) | `5-resultados-falco` §5.1.1 e §gate; critério pré-registrado no Cap.3; Cap.6/P-12 | Decisão do autor 2026-08-24: ADIAR. Quando reabrir: corrigir prosa conforme artefato + inserir tabela + reavaliar justificativa da Fase 3 (família P-12) + **achado 3 da auditoria da banca (2026-08-25)**: nos quatro pontos em que a prosa diz "empate estatístico" (§5.1.1 duas vezes, §5.7 duas vezes), ausência de significância está virando evidência de igualdade; trocar por "diferença não detectável (p=X)" com a magnitude observada e, onde o empate sustenta decisão do gate (nemotron como alternativa de custo zero; desqualificação do gpt-4o), reportar o IC da diferença | ABERTA (adiada, confirmada) |
| P-02 | 🟡 | REP | Braço E: 3ª semente (s123) no regime canônico `_bs16v2` nunca rodou | `5-resultados-falco`, tab:e3p, célula E | Opcional: rodar s123 em `_bs16v2` (GPU/código). Senão, manter 2 sementes com divergência declarada (já na v1) | ABERTA (opcional) |
| P-03 | 🟡 | EST | Artefatos `_bs16v2` completos (50) vivem numa branch, não na main do activelearning | repo activelearning (main @`cd6e1c0` tem 25; branch `rwatey` @`e88c20c` tem 50) | Consolidar `rwatey` → main do activelearning (barato, independe de rodar o arco) | ABERTA |
| P-04 | 🟡 | REP | População do AG: 20 (canônico) vs 50 (notebook versionado) | notebook no repo LEGADO `activetextclassification` (read-only); artefato usa 20 | Documental: registrar a reconstrução (nota no A2 ou doc no activelearning). Sem código | ABERTA |
| P-05 | ⚪ | STY | Critério de parada: descasamento ε=10⁻³ vs 1/√n_V=0,0224 (fator ~22) | `a7-parada-drift` §parada-laço | Autocrítica (política de parada "B") **aprovada mas adiada** por diretriz de não-autocrítica na v1. Texto já rascunhado | ABERTA (adiada) |
| P-06 | ⚪ | REP | tab:e6 com denominadores mistos (8 curvas em 177.490; 2 travadas em 181.490) | `5-resultados-falco`, tab:e6 | Opcional: reamostrar as 2 curvas sem estado (PVBin×Entropia, PVBin×Aleatório) para regime único — requer código | ABERTA (opcional) |
| P-07 | ⚪ | STY | Duas notas menores do A2 (revisor2) | `3-metodo`/`a2-ag` (Cap.3↔A2) | (a) "dez tamanhos entre 10 e 30.000" fecha só porque L0=250 é corrida abortada — frágil; (b) meia linha: sufixo da pasta não marca geração (`_100000v2`=pop20; `_30000v1`=pop100) | ABERTA (nota) |
| P-09 | ✅ | REP | Resumo e abstract excediam o teto de 500 palavras da SiBi/UFPR | `0-iniciais/resumo.tex`, `abstract.tex` | RESOLVIDA em 2026-08-25: o resumo em seis movimentos proposto pela banca, gateado em três passes (régua, humanize, leitura de metadiscurso), virou o oficial com 461 palavras; o espelho em inglês foi escrito pelo principal com 435. As versões de 862 e 831 palavras ficam preservadas em `resumo-estendido.tex` e `abstract-estendido.tex`, fora do PDF | FECHADA-NA-V1 |
| P-10 | 🟡 | EST | Branch `refatora/resultados-f4` (rebatismo E1→nome descritivo em 3.7.1 e resultados) ESTACIONADA — conteúdo pré-freeze não gateado | `3-metodo` §3.7.1; capítulos de resultados | Pós-freeze: rebasear sobre o texto de fluidez e gatear | ABERTA (estacionada) |
| P-11 | 🟡 | EST | Branch `banca/reenunciado-v2-5-edicoes` (reenuncia critério de aceitação: 34.724/15% da base vs ~18% do pool; "pré-registrado"→"planejado") ESTACIONADA — 344 commits atrás, imergível, conteúdo pré-freeze | `3-metodo` §3.8.1 | Pós-freeze: decidir com o autor se o reenunciado entra; rebasear e gatear | ABERTA (estacionada) |
| P-12 | 🔴 | CIE | Veredito do Cap.6 declara "critério atingível" atendendo as conjunções 1-2 do §1.3; a conjunção 3 (superar aleatória/incerteza com significância) não é tratada — e o Cap.5 afirma "a seleção ativa compra Macro F1 e cobertura, não acurácia" (na métrica do critério, a superioridade não se demonstra) | `6-conclusao` §veredito; §1.3; Cap.5 | Decisão do autor (adiada): (a) reportar a conjunção 3 com o resultado negativo, (b) declarar divergência pré-registrado×executado, ou (c) emendar por ADR. Achado das cruzadas r1/r2 da régua máxima; mesma família da P-01 | ABERTA (adiada) |
| P-13 | ⚪ | STY | Marco do pré-registro com datação dupla ("material datado de maio de 2022, na versão de maio de 2023") deixa ambíguo qual é o marco; sugestão S2 do painel da banca: nomear UM marco em frase própria | `3-metodo` §3.1 proveniência | Decisão editorial do autor (texto atual validado por ele); mandou registrar em 2026-08-24 | ABERTA (registrada) |
| P-14 | 🟡 | EST | Destino do conteúdo da seção **Ameaças à validade**, comentada por ordem do autor em 2026-08-24. O texto está preservado como comentário no `.tex` (validade externa, interna, de constructo e de conclusão estatística) e não aparece na v1; as remissões que apontavam para ele foram rebobinadas | `3-metodo`, bloco comentado após §3.8; Cap.6 §6.4 (limitações) | Decisão do autor: reincorporar reescrito, mover para apêndice, distribuir no Cap.6 ou manter fora. Registrado como pendência em 2026-08-24 por ordem do autor ("destinos viram P") | ABERTA (registrada) |
| P-15 | 🟡 | REP | Destino do conteúdo da seção **Reprodutibilidade e ambiente**, comentada na mesma ordem. Além do destino, há lacuna de conteúdo: o levantamento de ambientes mostra que a RTX 3090 citada não tem evidência de execução (todas as menções são planos ou estimativas) e que o regime impresso `_bs16v2` rodou em GPU não nomeada, em 3 sessões | `3-metodo`, bloco comentado após §3.8; §6.4; insumo em `docs/records/ambientes-por-experimento.md` | Decisão do autor sobre o destino **e** identificação da GPU do `_bs16v2`; sem isso a reescrita do ambiente não pode ser feita sem inventar. Registrado em 2026-08-24 por ordem do autor | ABERTA (registrada) |
| P-08 | ⚪ | CIE | Erros de ano na bibliografia (ex.: `Bayer2024ActiveLLM` citado como 2026 em prosa) | `referencias.bib` / citações | Auditoria de anos da bib. Já levantado; revisor2 decidiu não reabrir na rodada anterior | DECIDIDA-NÃO-REABRIR |
| — | ✅ | — | §2.2.3 `\ref{sec:fund-llm}` partido (render `??`) | `2-fundam` l.509 | — | FECHADA-NA-V1 |
| — | ✅ | — | Célula braço E: regime misto → 2 sementes honestas `_bs16v2` (0,822/0,351) | `5-resultados-falco` tab:e3p | — | FECHADA-NA-V1 |
| — | ✅ | — | Config canônica do AG (pop 20, N_elite 2, torneio 3, p_c 0,8, p_m 0,1) + espelho Cap.3↔A2 + nota L0=10 | `3-metodo`/`a2-ag`/`a7` | — | FECHADA-NA-V1 |

---

## Detalhe dos itens de alta/média severidade

### P-01 🔴 Fase 3 do FALCO — p-valor sem lastro

- **Texto (v1):** "deepseek-v4-pro significativamente superior ao flash na S-strat, $b=43$, $c=16$, $p<0{,}001$ → o critério é atendido e a Fase 3 do FALCO se justifica."
- **Artefato** (`activelearning:experiments/e0/results/e0_mcnemar.json`, par v4-flash×v4-pro, amostra `strat`): $b=73$, $c=91$, **$p=0{,}1844$** — não significativo a nenhum α usual.
- **Por que importa:** o Cap.3 registra o critério **pré-registrado**: "[LLM Avançado] desde que significativamente superior ao Inicial (McNemar, α=0,05); caso contrário, a Fase 3 do framework é eliminada." Com o dado real, a regra da própria tese apontaria para **eliminar** a Fase 3 — o oposto do texto atual.
- **Origem:** executor01, recomputado do cru; branch `claude/e3prime-seed-7-bx08ks` @`24bf91b` (aviso) e @`928fce6` (detalhe). Mesma causa-raiz do achado "E0/RQ1 sem lastro" (Onda 3a, já confirmado).
- **Estado:** CRUZADA E CONFIRMADA em 2026-08-24 (leitura direta do principal no artefato; ver linha da tabela: escopo ampliado com o p=0,061 inexistente e o 'abaixo apenas' falso). **Ação:** ADIADA por decisão do autor; ao reabrir, corrigir prosa + inserir tabela de McNemar + reavaliar a Fase 3.

### P-02 🟡 Braço E — 2 vs 3 sementes

- A célula da tab:e3p reporta, na v1, a **média honesta de 2 sementes** (`_bs16v2`: s7, s42) = **0,822 / 0,351**, 0/2 no sweep.
- O arco s123 **só existe no regime `_bs16` (antigo)**; `e3prime_E_s123_bs16v2` não existe (confirmado byte-level por revisor2, @`e88c20c`).
- **Veredito não muda:** E fica abaixo do piso (0,95×D) sob as três leituras (`_bs16` 3-sem, `_bs16v2` 2-sem, tese impressa).
- Fechamento das 3 sementes homogêneas é **opcional** e exige rodar código (fora de escopo agora).

### P-03 🟡 Rastreabilidade estrutural

- Os números dos braços A–E do Cap.5 reproduzem de `_bs16v2`. A main do activelearning @`cd6e1c0` já tem 25 (A/B/C/D com 3 sementes, E com 2); a branch `rwatey` @`e88c20c` tem os 50.
- **Risco:** apagar a `rwatey` levaria junto a rastreabilidade completa. **Ação:** merge `rwatey` → main do activelearning.

### P-04 🟡 População do AG (20 vs 50)

- Caminho de reprodução versionado (notebook no **legado** `activetextclassification`, read-only) define **50**; o artefato canônico usa **20**; o JSON não sobrescreve. Há ainda uma **3ª config** (pop 100, 200 gerações) que **não** alimenta a tese.
- A v1 já reporta 20 (o que rodou) e já declara que a população é o único parâmetro sem fonte de config versionada.
- **Ação:** decisão documental de onde registrar a reconstrução (o notebook está em repo read-only).

---

*Manutenção: novos achados entram como novas linhas P-NN com severidade/tipo/onde/ação. Itens fechados migram para FECHADA-NA-V1. Esta matriz não altera o texto — é o índice do que fica para depois da v1.*
