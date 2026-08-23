---
de: executor02
para: principal
tipo: aviso
acao_esperada: levar ao autor o número da banca (média±desvio, 3 sementes) e encaminhar as duas pendências finais: cache do oráculo (A/B/C ×3) e refazer McNemar/bootstrap sobre as predições canônicas (com o texto do Cap. 5 junto)
referencia: activelearning@4b685d4 (s42 canônica) · @ebd1797 (s7) · @9d74484 (s123) · plano v21
criada_em: 2026-08-16T23:44:00Z
---
FECHADAS as três sementes canônicas do E3′ (42, 7, 123) — 6 braços cada,
regime idêntico (3 épocas, lote 128, avaliação nos 177.490 da população
inteira), tudo na main do activelearning. A pendência nº 1 do parecer da
banca, na parte que independe do cache do oráculo, está atendida.

## O número da banca — média ± desvio, k=3

| braço | n | Macro F1 | acurácia |
|---|---|---|---|
| D (régua) | 50.000 | 0,3684 ± 0,0091 | 0,8675 ± 0,0021 |
| E35 | 35.000 | 0,3520 ± 0,0121 | 0,8610 ± 0,0040 |
| E30 | 30.000 | 0,3233 ± 0,0006 | 0,8439 ± 0,0042 |
| E25 | 25.000 | 0,3061 ± 0,0074 | 0,8281 ± 0,0046 |
| E20 | 20.000 | 0,2533 ± 0,0118 | 0,7748 ± 0,0068 |
| E | 15.000 | 0,2016 ± 0,0094 | 0,6966 ± 0,0061 |

**Piso de orçamento (0,95×F1(D)):** o E35 cruza em 2 das 3 sementes (42 por
0,015; 123 por 0,005) e falha na 7 (por 0,014); na média cruza por 0,002 —
dentro do desvio. Leitura honesta para o texto: **35k por entropia fica NO
limiar do critério, não confortavelmente acima**; 30k para baixo fica
claramente abaixo. Em **acurácia**, E30 e E35 cruzam nas três sementes. A
robustez multi-semente, portanto, MUDA a conclusão que o regime antigo
sugeria ("35k ≈ 50k, folgado") para "35k é o limiar, com sensibilidade à
semente" — o Cap. 5 precisa refletir isso quando as estatísticas forem
refeitas.

## O que resta do E3′ (nada depende de mim para começar)

1. **A/B/C ×3 sementes** — os braços centrais da hipótese (F1(A) ≥ 0,95×F1(D))
   esperam só o `annotation_cache_nemotron.jsonl` como dataset do Kaggle.
   Três retomadas curtas; os 18 resultados prontos são pulados.
2. **McNemar + bootstrap canônicos** — as predições das 3 sementes estão
   todas na main; quem assumir deve tratar junto o texto do Cap. 5.
3. Custo até aqui: ~4 h das 30 h semanais de GPU da conta.
