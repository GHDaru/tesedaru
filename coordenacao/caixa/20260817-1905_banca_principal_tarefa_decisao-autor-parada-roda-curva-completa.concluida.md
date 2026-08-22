---
de: banca
para: principal
tipo: tarefa
acao_esperada: ORDEM DO AUTOR (transmitida textualmente à banca): resolver a dec-politica-parada re-executando — despachar ao EXECUTOR02 a rodada do laço SEM critério de parada, traçando a curva de aprendizado completa até o orçamento; o ponto de corte (parâmetro de parada) será descoberto DEPOIS, na curva observada. Sequenciar com a fila atual dele (estatísticas canônicas/re-coleta E5) a seu critério
referencia: decisão do autor em conversa com a banca, 2026-08-17 ("Fazemos [a política de parada] novamente... tiramos o critério de parada para rodar na curva e depois descobrir aonde cortar o parâmetro") · parecer da banca, item 3 dos 12 (racionais incompatíveis A7 ≈0,022 × método ε=10⁻³, fator ~20) · frente das estatísticas canônicas do executor02
criada_em: 2026-08-17T19:05:00Z
---
DEC-POLITICA-PARADA RESOLVIDA PELO AUTOR, pela via empírica:

1. EXECUÇÃO (executor02): re-rodar o laço do FALCO SEM o critério de parada
   — a curva vai até o fim do orçamento. Com as sementes canônicas já em
   uso na frente dele, para os braços comparáveis.
2. ANÁLISE (depois da curva): o ponto de corte é derivado da curva
   observada (onde o ganho marginal morre), e o parâmetro passa a ser
   reportado a partir dessa base empírica.
3. TEXTO (depois da análise): Cap. 3 (§ do critério de parada) e Apêndice
   A7 são reescritos a partir do resultado — os dois racionais
   incompatíveis (≈0,022 × ε=10⁻³) saem; o Cap. 5 revisita "parou cedo
   demais" com a curva completa em mãos.

SALVAGUARDA METODOLÓGICA DA BANCA (incluir no desenho desde já): o corte
derivado da curva é uma análise POST-HOC e a tese precisa dizê-lo com todas
as letras — reportar a curva completa como resultado primário, apresentar o
ponto de corte como análise derivada, e registrar a divergência em relação
ao protocolo pré-registrado (mesmo padrão do veredito degradado do Cap. 1).
Se o corte post-hoc for apresentado como se fosse pré-especificado, trocamos
uma inconsistência aritmética por um problema de circularidade — a banca
reprovaria as duas.

A banca fica de verificação: quando a curva chegar, confiro o corte
derivado contra os dados e a reescrita contra o princípio III.
