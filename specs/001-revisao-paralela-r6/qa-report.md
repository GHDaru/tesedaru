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
