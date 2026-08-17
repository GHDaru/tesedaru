---
id: Guyon2011ALC
title: "Results of the Active Learning Challenge"
authors: ["Guyon, Isabelle", "Cawley, Gavin", "Dror, Gideon", "Lemaire, Vincent"]
year: 2011
venue: "JMLR Workshop and Conference Proceedings, v. 16 (Active Learning and Experimental Design Workshop, AISTATS 2010), pp. 19--45"
url: "https://proceedings.mlr.press/v16/guyon11a.html"
pdf: referencias-pdf/Guyon2011ALC.pdf
paper_type: benchmark
pillars: [geral, P4]
status: fichado
verificado_em: 2026-08-17
verificado_por: banca (leitura dirigida do PDF, 27 pp. — definição da métrica, protocolo do desafio e achados)
proposes: [ALC, global-score-normalizado]
uses_methods: [curva-de-aprendizado, AUC, aprendizado-ativo]
datasets: [seis-bases-do-desafio-A-F]
metrics: [ALC, AUC]
tasks: [classificacao-binaria]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: LCE
    note: "Conceito-mãe da LCE: a ALC (área sob a curva de aprendizado) é a
           métrica consagrada pela literatura para resumir uma execução inteira
           de aprendizado ativo em um único número. A LCE da tese descende dela;
           o Cap. 2 cita a ALC como o conceito da literatura e a LCE nasce no
           capítulo de método (padrão de camadas do Cap. 2)."
---

# Results of the Active Learning Challenge (Guyon et al., 2011)

## Resumo
Relato oficial do desafio de aprendizado ativo organizado junto ao AISTATS
2010 (workshop Active Learning and Experimental Design). Participantes
compravam lotes de rótulos de tamanho livre e submetiam predições a cada
compra, permitindo aos organizadores traçar curvas de aprendizado; metade de
cada base era reservada como teste. A avaliação consagra a **área sob a curva
de aprendizado (ALC)** como métrica de execução inteira, e o ranqueamento usa
um escore global normalizado. Seis bases finais (A--F) de domínios distintos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A curva de aprendizado plota a AUC (computada nos exemplos de rótulo desconhecido) em função do número de rótulos consultados; a ALC é a área sob essa curva e foi o critério de avaliação do desafio | p. 23 ("The prediction performance was evaluated according to the Area under the Learning Curve (ALC). A learning curve plots the Area Under the ROC curve (AUC) [...] as a function of the number of labels queried") | Cap. 2 (2.1.4, parágrafo do bootstrap): a ALC é o exemplo da literatura de estatística que resume uma curva inteira em um número, sem distribuição amostral conhecida — o caso que motiva o IC por bootstrap |
| C2 | O ranqueamento usa o escore normalizado globalscore = (ALC − A_rand)/(A_max − A_rand), com A_max a área da melhor curva alcançável e A_rand a da predição aleatória | p. 23, fórmula explícita | Antecedente direto da normalização da LCE (Apêndice da tese); citar ao posicionar a LCE em relação à ALC |
| C3 | Achados qualitativos do desafio: estratégias ativas produziram curvas suaves; amostragem por incerteza pura pode DEGRADAR o desempenho no meio da curva (exemplo da base D) | p. 30 | Munição de literatura para o resultado E3′ da tese (incerteza não domina sempre); usar como paralelo, nunca como evidência do caso próprio |

## Números que posso citar
- Seis bases finais (A--F), metade de cada uma reservada como teste (p. 22-23).
- Fórmula do escore global normalizado (C2), p. 23.

## Fronteira de uso (camadas do Cap. 2)
O Cap. 2 cita a ALC como conceito consagrado da literatura. A LCE, criação da
tese, NÃO aparece no Cap. 2; a filiação LCE→ALC é declarada onde a LCE nasce
(método/apêndice). Nota de paginação: o artigo ocupa as pp. 19--45 do volume
16; as páginas citadas acima seguem essa numeração impressa.
