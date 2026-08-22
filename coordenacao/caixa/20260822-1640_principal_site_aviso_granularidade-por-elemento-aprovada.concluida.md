---
de: principal
para: site
tipo: aviso
acao_esperada: resposta à sua pergunta 1415 — SIM, quebre por elemento. O autor pediu "cada elemento pós-textual na tabela"; então desagregue.
referencia: sua pergunta 1415 · decisão do autor 2026-08-22 (pós-textuais + apêndices na tabela e no resumo; R7 resetados) · pos_textuais[]
criada_em: 2026-08-22T16:40:00Z
---

Decisão:
1. **Desagregue a estrutura**: `pre` vira 2 linhas (Resumo, Abstract); `ap`
   vira 7 linhas (A1-A7), cada uma com seu estado (existe/em construção),
   medido do arquivo. É o que o autor pediu ("cada elemento na tabela").
2. **Rodadas**: registre R1-R7 por elemento SÓ onde a rodada se aplica — um
   apêndice não precisa das 7. Onde não se aplica, marque "n/a", não "pendente".
3. Os R7 estão RESETADOS (reauditoria do autor): mostre-os como "a reauditar"
   em todos os capítulos e elementos, não como concluídos.
4. Apêndices também no RESUMO/visão-geral do site, não só na tabela.
Sem gate (site). Publique e avise.

## Resultado (site, 2026-08-22T17:10:00Z)

Publicado em `main` @a68cebf (plano v85). capitulos[] passa de 8 para 15:
Resumo/Abstract e A1-A7 são elementos próprios agora, cada um com dimensões
(travessões/citações) medidas diretamente no arquivo e rodadas R1-R7 com
"na" só onde medido (não suposto) — 4 dos 7 apêndices têm R3=na (zero
citações). R7 de todos os 15 elementos mostra "↻ a reauditar" no lugar de
"pendente" (status interno continua "pendente", só o rótulo mudou).
pos_textuais[] ficou só com Referências. Testado: 8 páginas, 0 erro,
claro/escuro/mobile.

Achado a registrar: a nota antiga do agregado "pre" dizia 32 travessões
(16 resumo + 16 abstract); a contagem direta no arquivo hoje dá 22 (11+11).
Não corrigi — só usei o número medido para os elementos novos e deixei a
divergência escrita em `atualizado_por`.

Efeito colateral do modelo de pontos (ADR 0006), não de perda de trabalho:
prontidão global caiu de 36,7% para 34,1% porque rodadas de custo fixo
(R2/R4/R6/R7) agora contam 9 vezes (Resumo+Abstract+7 apêndices) onde antes
contavam 2 (o agregado pre + o agregado ap) — pontos_totais subiu de 2032
para 2209, pontos_feitos quase não mudou (877→887).
