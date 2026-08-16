# Verificação cruzada (protocolo §6) — revisor2 sobre os artefatos do revisor1

**Data:** 2026-08-16 · **Verificador:** revisor2 · **Verificado:** branch
`claude/maestro-cycles-statistical-analysis-fwla6a` (revisor1, tesedaru +
activelearning) · **Contexto:** colisão de claims (pergunta
`20260816-1724_revisor1_revisor2_*`, respondida e concluída); os dois
revisores produziram independentemente os mesmos três entregáveis, o que
transforma a duplicação em verificação cruzada bidirecional. Este é o arquivo
do verificador (§5: nunca edição no artefato do outro).

## 1. Execuções McNemar + bootstrap (main do activelearning, commit 3eff825)

Reproduzi a análise de forma totalmente independente (script próprio, mesma
fonte de predições `e3prime_*_s42_pred.json`, gabarito via
`run_e3prime.load_base`):

| Par | b/c (revisor1) | b/c (revisor2, indep.) | p exato (r1) | p exato (r2) |
|---|---|---|---|---|
| A–B | 1263/2143 | 1263/2143 | 7,963e-52 | 7,963e-52 |
| B–C | 1198/1788 | 1198/1788 | 2,957e-27 | 2,957e-27 |
| E35–D | 618/561 | 618/561 | 0,1029 | 0,1029 |

Bootstrap: deltas pontuais idênticos (+0,0332 / +0,0204 / +0,0117); ICs
ligeiramente diferentes por convenção de rótulos (r1 fixa união da amostra
completa; r2 segue convenção sklearn por reamostra) e fluxo de RNG — mesmas
conclusões: os três ICs excluem zero; E35–D no limite (r1:
frac(Δ≤0)=0,0071). **VEREDITO: CONFIRMADO.**

## 2. Grupo dados (branch fwla6a, `data/DICIONARIO.md` + `scripts/check_dataset.py`)

Números do dicionário do revisor1 conferidos contra os meus (computados
independentemente das funções reais): 250.221 · 231.490 · 714 · 620+`_rare_`
=621 · 649 · 177.490 — **todos idênticos**. Detalhe adicional do r1 que o meu
não tem: a causa-raiz nominal do 715→714 ("pomada massageadora" eliminada no
dedup). Meu equivalente (16 invariantes, revisão independente aplicada) está
em `activelearning:scripts/check_dataset_invariants.py`. **VEREDITO:
CONFIRMADO** (equivalentes; autor escolhe um para o merge).

## 3. Fichar-vizinhos (branch fwla6a, 11 fichamentos)

Comparação programática dos front-matters (11 pares, meu slug × slug do r1):
**11/11 com título idêntico, ano idêntico e DOI/venue equivalentes** (onde há
DOI dos dois lados, iguais; onde não há — ICLR/PMLR não emitem — os venues
coincidem). Convergências independentes notáveis:

- FreeAL = Xiao et al., EMNLP 2023 main, DOI 10.18653/v1/2023.emnlp-main.896 —
  ambos flagramos a autoria fabricada ("Su, B. …") da entrada bib existente;
- Bengar22 = WACV 2022, DOI 10.1109/WACV51458.2022.00376 (hipótese CAIP 2021
  descartada dos dois lados);
- PATRON = ACL 2023 **main** (não Findings), com o título completo ("Better").

Diferenças de escopo (não de conteúdo): meus fichamentos integram as 9
entradas bib novas + termos de vocabulário no mesmo commit (lei da skill
`fichamento`); os do r1 deixam bib/vocabulário como pendência declarada.
Slugs divergem (ex.: `Bengar2022` × `Bengar2022ClassBalanced`) — mergear as
duas branches duplicaria os 11 sob dois nomes. **VEREDITO: CONFIRMADO;
mergear apenas UMA das duas coleções.**

## 4. Normas UFPR (branch fwla6a, `docs/relatorio-conformidade-ufpr-ppgmne.md`)

Mesmo método (levantamento, evidência arquivo:linha, sem editar a tese),
recortes complementares: r1 organiza em ~40 itens com 5 bloqueantes e 7 "a
confirmar"; o meu (`docs/relatorio-nao-conformidades-ufpr.md`) baixou e leu o
Manual UFPR 2024 na fonte (11 ❌ / 15 ⚠️, com a correção da regra de caixa da
NBR 10520:2023). Achados centrais coincidem (ficha catalográfica placeholder,
resumo acima de 500 palavras, entrelinha do modo `final`, resíduos PPGInf).
**VEREDITO: CONFIRMADO; relatórios complementares — autor pode fundir ou
escolher um como canônico.**

## Conclusão

Nenhuma divergência de conteúdo encontrada entre as duas produções. A
duplicação custou tokens, não qualidade — e rendeu a verificação cruzada §6
nos dois sentidos. Recomendação ao autor: (i) gatear UMA branch por
entregável (a outra fica como registro de verificação); (ii) adotar daqui em
diante a divisão acordada na resposta da pergunta de colisão: revisor1
produz, revisor2 verifica.
