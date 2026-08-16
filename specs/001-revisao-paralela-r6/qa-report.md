# QA report 001 — Revisão paralela pós-R6: fichamentos de vizinhos + levantamento de normas

- **Date**: 2026-08-16 · **Lane**: full · **Verdict**: ✅ COMPLIANT (aguardando gate humano; colisão de branches em arbitragem)

## Fitness functions (DoD)

| Check | Expected | Result |
|---|---|---|
| `ls fichamentos/{FreeAL2023,…,Bengar2022ClassBalanced}.md` (11 chaves) | 11 arquivos, exit 0 | 11 arquivos ✅ |
| `ls referencias-pdf/<Chave>.pdf` (11 chaves) | exit 0 | 11 PDFs ✅ |
| script de sanidade dos front-matters (YAML, id=arquivo, falco_relation, PDF, vocabulário) | nenhum problema | "PROBLEMAS: nenhum" ✅ |
| `grep -c "@" referencias.bib` | 369 → 378 (+9) | 378 ✅ (revisão conferiu: sem duplicata das 9 chaves, diff 100% append) |
| `uv run --with pyyaml python fichamentos/build_kg.py` | exit 0, nós > 508 | 523 nós / 1035 arestas ✅ (revisão: kg.json/html byte-idênticos à regeneração em cópia limpa) |
| `test -f docs/relatorio-nao-conformidades-ufpr.md` | exit 0 | existe; 190 linhas ✅ |
| diff da branch não toca `*.tex`/`*.cls`/`*.bst` | vazio | vazio ✅ |

## Closing tail — the evidence

- **TAIL:review** — revisão independente em contexto fresco (agente `review`,
  2026-08-16). Veredito: **aprovado com ressalvas**. Amostragem de conteúdo:
  claims de FreeAL2023 (Tab. 3/5/6, pp. 14526–14528) e Hacohen2022TypiClust
  (§4.2.1/Fig. 4, p. 7) conferem exatamente contra os PDFs. Achados e
  disposição: (1) MAIOR colisão com a branch fwla6a do revisor1 → em
  arbitragem do autor (resposta na caixa 20260816-1724, verificação cruzada
  §6 feita nos dois sentidos: 11/11 identidades idênticas — título/ano/DOI —
  e achado da autoria fabricada do FreeAL replicado independentemente);
  (2) MAIOR qa-report ausente → este arquivo; (3) MENOR T8 antecipava v10 →
  v10 efetivado no fechamento; (4) MENOR locator Kossen C7 p.7→p.8 →
  CORRIGIDO; (5) MENOR declaração de preprint no Farquhar → nota de fonte
  explícita ADICIONADA; (6) MENOR vírgulas residuais no vocabulário →
  LIMPAS (0 ocorrências de ",,").
- **TAIL:security** — varredura de segredos no diff
  (`git diff origin/main...HEAD | grep -niE "api[_-]?key|secret|token|…"`):
  nenhum segredo — matches são falsos positivos de prosa ("secretaria").
  Diff só cria arquivos e faz appends; nenhum código executável novo além do
  já existente `build_kg.py`.
- **TAIL:gate** — aguardando gate humano do autor no merge da branch
  `claude/tesedaru-activelearning-maestro-bf56y7`. Insumo para a arbitragem:
  esta branch integra bib (9 chaves) + vocabulário por commit (lei da skill
  `fichamento`) e carrega o ciclo Maestro completo; a branch fwla6a
  (revisor1) tem os mesmos 11 vizinhos sob slugs diferentes, sem bib/
  vocabulário. Mergear as duas duplicaria fichamentos — escolher UMA.

## Requirement coverage

- **FR1**: entregue — 11 fichamentos, um commit por artigo com PDF + bib + vocabulário.
- **FR2**: entregue — divergências reportadas sem corrigir (FreeAL2023/Su2023 fabricadas, Sener2017 duplicata, sinais Diao/Margatina/Tian, Alsmadi a/b); encaminhadas também pela banca (parecer de auditoria do bib, mensagem 17:35).
- **FR3**: entregue — KG regenerado (523 nós/1035 arestas).
- **FR4**: entregue — relatório de não conformidades com evidência arquivo:linha (6 evidências amostradas pela revisão, todas conferem).

## Consolidação r1+r2 (2026-08-16, branch `consolidacao/revisao-paralela-r6`)

Por decisão do autor ("compila os dois resultados para não perdermos os
trabalhos"), a arbitragem "uma OU outra branch" foi substituída por uma branch
de consolidação. O que ela contém:

| Frente | Resultado |
|---|---|
| 11 fichamentos canônicos | absorveram os claims exclusivos da leitura do revisor1, **cada item verificado no PDF arquivado antes de entrar** |
| 11 leituras do revisor1 | preservadas verbatim em `fichamentos/leitura-cruzada-revisor1/` (fora do `glob("*.md")` do `build_kg.py` — não duplica nó) |
| Normas UFPR | `docs/normas-ufpr-consolidado.md` funde as duas auditorias; os dois relatórios-fonte seguem versionados |
| Dados (activelearning) | causa-raiz nominal do 715→714 do revisor1 virou o 17º invariante executável |

**Erros no trabalho canônico que só a fusão revelou** (evidência de que a
duplicação valeu como verificação, e não apenas custou tokens):

1. `Wang2021GPT3Labeling`: custos de SST-2 e TREC **trocados** — a leitura do
   revisor1 estava correta (Tab. 1, p. 4196). Linha marcada contra regressão.
2. `FreeAL2023`: a crítica "sem contabilidade de custo" era **falsa** — o paper
   tem Tab. 7 (p. 14532) com fórmula de tokens. Reformulada como ressalva de
   granularidade; o registro anterior não foi apagado.
3. `Zhang2023LLMaAA`: 6 locators deslocados em +1 página; mais 7 corrigidos em
   TypiClust, Kossen e Pangakis.
4. `Sener2018`: `compares_with` apontava `Gal2016` (Dropout as Bayesian
   Approximation); o DBAL do paper é `Gal2017` (Gal, Islam & Ghahramani), chave
   que já existia no bib.

**Itens da leitura cruzada REJEITADOS por não confirmação** (a fusão filtrou,
não apenas somou): complexidade assintótica do surrogate (Kossen — o paper só
trata custo qualitativamente); "ganhos crescem com o número de classes"
(Bengar — contradito pela Tab. 3, Tiny ImageNet com 200 classes tem os menores
ganhos). O custo por rótulo do Pangakis entrou marcado como **DERIVAÇÃO NOSSA**,
com a ressalva de que o paper só reporta o total.

### Fitness function nova

`uv run --with pyyaml python scripts/check-fichamentos.py [chaves]` — 6
invariantes por fichamento (YAML/id, `falco_relation`, entidades no
vocabulário, alvos de relação com entrada no bib, PDF existente, evidência por
claim).

| Check | Expected | Result |
|---|---|---|
| checador nos 11 novos | exit 0, "PROBLEMAS: nenhum" | exit 0 ✅ |
| checador com `falco_relation` removida (falha provada) | exit 1 nomeando o arquivo | exit 1 ✅ |
| `build_kg.py` após a fusão | exit 0, nós ≥ 523 | 527 nós / 1049 arestas ✅ |

**Achado reportado, não corrigido** (fora de escopo — anti-pattern 10): os 140
fichamentos legados acumulam 344 violações (342 entidades fora do vocabulário,
1 alvo de relação sem bib, 1 PDF inexistente em `Bayer2024ActiveLLM`).
Registrado na caixa de coordenação para o autor decidir se vira item do plano.
