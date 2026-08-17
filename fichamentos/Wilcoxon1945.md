---
id: Wilcoxon1945
title: "Individual comparisons by ranking methods"
authors: ["Wilcoxon, Frank"]
year: 1945
venue: "Biometrics Bulletin, v. 1, n. 6, pp. 80--83"

paper_type: canonica
status: ficha-minima
ficha_minima_motivo: "ADR 0012, adendo das estatísticas — obra canônica que a banca argui"

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Teste de postos sinalizados: compara duas estratégias nas mesmas
           sementes sem supor normalidade — usado nos experimentos E1/E4."
---

# Wilcoxon (1945) — ficha mínima

**O que a tese usa:** o teste de postos sinalizados para amostras pareadas.

**Onde:** `2-fundam/texto.tex:174` (definição — compara os pares sem supor
distribuição), `2-fundam/texto.tex:201` (tabela de decisão: duas estratégias,
mesmas sementes) e `3-metodo/texto.tex:254` (aplicação sobre as métricas finais
e a LCE).

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Comparações pareadas podem ser feitas por postos, dispensando a suposição de normalidade exigida pelo teste t | Wilcoxon (1945), pp. 80--83 | Sustenta a comparação de estratégias sobre as 8 sementes (E1/E4) |

**Limite que a tese precisa respeitar:** com n sementes, o menor p bicaudal
alcançável é 2/2^n — com 8 sementes, 0,0078. Nenhum resultado pode reivindicar
p menor que isso.

**Por que basta uma linha:** resultado consagrado, citado como definição
(ADR 0012, item 1 + adendo).
