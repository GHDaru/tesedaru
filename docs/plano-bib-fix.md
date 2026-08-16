# Plano de execução do ciclo bib-fix — divisão em lotes

Autor do plano: banca · Data: 2026-08-16 · Base: `docs/parecer-auditoria-bib.md`
(gate aprovado, `cf587d5`). Destinatário: agente principal (roteamento central,
ADR 0009/0010). Executores propostos: revisor1 e revisor2.

## Pré-requisito bloqueante

O merge de `consolidacao/revisao-paralela-r6` (9 chaves novas validadas +
correção da aresta Sener→Gal2017) **precede** todos os lotes: sem ele, o
bib-fix edita um arquivo que vai mudar. Enquanto não houver gate, os lotes
ficam prontos mas não iniciam — exceto o Lote 0 (ferramenta), que não toca o
`.bib`.

## Dimensionamento verificado (contagem real de `\cite` na tese)

37 ocorrências de citação afetadas, concentradas em 2 arquivos: `1-intro`
(9 ocorrências) e `2-fundam` (28). Nenhum outro capítulo é tocado — o bib-fix
não colide com a humanização dos Caps. 3–6.

## Lotes

### Lote 0 — Ferramenta de verificação (executor: revisor1) · não toca o .bib
Escrever `scripts/check-bib.py` implementando o DoD da §5 do parecer:
resolve DOI/arXiv de cada chave citada e compara título+autores (fuzzy, com
relatório de divergências); detecta títulos duplicados normalizados, campos
`note=` com texto de trabalho, campos `key=`, e chaves citadas com year≥2020
sem DOI/URL. Saída: tabela + exit code. **É o gate objetivo dos demais lotes**
e some com o risco de "corrigimos no olho".
Evidência de pronto: roda no bib atual e reproduz os números do parecer
(15 erradas, 3 inexistentes, 17 duplicatas).

### Lote 1 — Fabricações e obras inexistentes (executor: revisor2) · alto risco
As 14 entradas da §1 do parecer. Cada uma: aplicar o patch BibTeX **conferindo
a fonte primária antes de colar** (não confiar no parecer como verdade final —
é o mesmo princípio que pegou o erro original). Inclui renomear
`Su2023`→`Xiao2023FreeAL` e `Fromme2022`→`Wertz2022` com repontuação dos
`\cite` correspondentes (2 ocorrências).
Casos que exigem decisão registrada, não só edição:
- `Tian2023` (`2-fundam:615`): a obra pretendida provável é "Just Ask for
  Calibration" (EMNLP 2023); confirmar que sustenta a alegação da linha.
- `Margatina2023` (`2-fundam:568`): confirmar se a obra real de Margatina
  sustenta "sistemas híbridos humano-LLM"; se não, recitar.
- `Wu2022` (`2-fundam:619`) e `Ahmed2023` (0 citações — só matar).
Evidência: `check-bib.py` sem fabricações; as 3 linhas conferidas obra×alegação.

### Lote 2 — Duplicatas e repontuação de `\cite` (executor: revisor1) · mecânico
20 chaves a matar (§2). Os 6 grupos citados em dobro, com as ocorrências já
mapeadas: `zhang2022surveyAL` (2, ambas em `1-intro`), `Bayer2024` (8, sendo 7
em `2-fundam` + unificação com `Bayer2024ActiveLLM`), `Zhang2025LLMAL` (1),
`devlin2019bert` (2), `alsmadi2019shorttext` (2), `song2014shorttext` (2).
Aplicar por `sed` auditado (diff revisado ocorrência a ocorrência — troca de
chave não pode alterar texto corrido).
Evidência: 0 títulos duplicados no checador; `git diff` mostra só chaves.

### Lote 3 — Clássicos, estrutura e DOIs (executor: revisor2) · baixo risco
4 correções de clássicos (`Guyon2011ALC` ano do workshop, `Kohavi1995` páginas,
`Pennington2014` typo+volume, `Bojanowski2017` tipo de entrada); remover os 2
`note=` de LLM, o `key=` residual e o separador órfão; adicionar DOI/URL às 34
entradas citadas com year≥2020; varrer o **lote inline suspeito** (l.577–581,
onde estão `Yu2022` e `Zhang2020`, ambas com padrão de fabricação e órfãs) e as
2 órfãs do adendo (`Hacohen2023`, `Yu2022`).
Evidência: checador verde nos 4 critérios estruturais.

### Lote 4 — Verificação independente (executor: banca) · após os lotes
Rodar `check-bib.py` do zero, reconferir por amostra 10 entradas corrigidas
contra fonte primária (quem executou não verifica — §6 do protocolo), conferir
compilação (0 erros/0 warnings BibTeX) e nº de entradas nas Referências do PDF
= nº de obras distintas citadas. Saída: adendo ao parecer + mensagem ao
principal.

## Sequência e paralelismo

Lote 0 pode começar já (não toca o `.bib`). Depois do gate da consolidação:
Lote 1 e Lote 3 são do mesmo executor em série (ambos editam entradas), Lote 2
é do outro executor mas **precisa do lock do `.bib`** — logo, ordem sugerida:
**Lote 1 → Lote 2 → Lote 3**, com o lock passando de mão, ou tudo numa branch
só com os três lotes em commits separados (mais simples; recomendo esta).
Só então a humanização R1 dos Caps. 1 e 2 (evita rebase duplo). Caps. 3–6 não
são tocados pelo bib-fix e podem humanizar em paralelo desde já.

## O que continua faltando fora do bib-fix (para a banca)

| Item | Estado | Dono |
|---|---|---|
| Veredito da hipótese (resumo/abstract/Cap. 6) | em andamento (principal, locks ativos) | principal |
| Correções numéricas R5-imediato (7 itens) | não iniciado | principal |
| Declaração de IA (tirar RASCUNHO, nomear ferramenta, incluir E1/E2) | não iniciado | principal |
| Humanização R1 dos Caps. 2–6 + pré-textuais (promovida a obrigatória) | cap2 lote 1 em gate; resto pendente | principal |
| Verificação pós-fix do bib (Lote 4) | aguarda lotes | banca |
| Dívida de vocabulário: 342 entidades fora do `_VOCABULARIO.md` + PDF ausente de ActiveLLM | reportado, ciclo próprio | a decidir |
| Trâmites externos: template PPGMNE, Lattes, checklist da coordenação, licença Kaggle | pendentes | autor |
| Recompilação final 0/0/0 | após tudo | principal |
