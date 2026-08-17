---
id: Wilson1927
title: "Probable inference, the law of succession, and statistical inference"
authors: ["Wilson, Edwin B."]
year: 1927
venue: "Journal of the American Statistical Association, v. 22, n. 158, pp. 209--212"

paper_type: canonica
status: ficha-minima
ficha_minima_motivo: "ADR 0012, adendo das estatísticas — obra canônica que a banca argui"

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Intervalo de confiança para proporção binomial obtido resolvendo a
           desigualdade no parâmetro, e não na estimativa — é o IC de 95% usado
           em TODA acurácia de oráculo relatada na tese."
---

# Wilson (1927) — ficha mínima

**O que a tese usa:** o intervalo de confiança de Wilson a 95% para uma
proporção estimada.

**Onde:** `2-fundam/texto.tex:156` (definição e o contraste com a aproximação
normal), `2-fundam/texto.tex:199` (linha da tabela de decisão estatística) e
`3-metodo/texto.tex:248` (aplicação declarada no método).

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O IC para proporção deve ser obtido resolvendo a desigualdade no parâmetro, o que o mantém dentro de [0,1] e válido com n pequeno ou proporção extrema — ao contrário da aproximação normal | Wilson (1927), pp. 209--212 | Justifica a escolha do IC de Wilson em todas as acurácias (E0) |

**Por que basta uma linha:** a obra entra como resultado consagrado, sem que
nenhuma afirmação da tese dependa do conteúdo específico do artigo de 1927.
Se isso mudar, a ADR 0012 item 3 devolve a obra à regra cheia.
