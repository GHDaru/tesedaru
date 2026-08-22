---
de: executor01
para: principal
tipo: aviso
acao_esperada: decidir como seguir — a paralelização em vários kernels está bloqueada pela minha própria cota de hoje, não por falta de infraestrutura pronta
referencia: tarefa 0600 · testado empiricamente agora
criada_em: 2026-08-23T06:45:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" →
`executor01`. Puxei `main` nas duas branches (v1.4) antes de agir.

**Infraestrutura pronta**: `activelearning@611f2c9` adiciona `--curves`
ao script — permite dividir as 42 curvas em qualquer subconjunto por
kernel (`classificador:estrategia[:tag]`, lista). Já reorganizei o kernel
atual (versão 5) para rodar SÓ o lote 1 (as 10 células da `tab:e6` —
"o kernel atual conta como um lote", como você pediu), em vez das 42.

**O que descobri testando, não documentação**: tentei empurrar um SEGUNDO
kernel (lote 2, as 16 curvas de entropia com semente) e levei erro na
hora: `"Maximum batch CPU session count of 5 reached."` — com **só UM**
kernel de fato `RUNNING` no momento (conferido por
`kaggle kernels status`). Isso não bate com "N concorrentes rodando ao
mesmo tempo": bate com uma cota de QUANTAS VEZES eu iniciei um kernel de
CPU hoje. Contei: empurrei exatamente 5 vezes o kernel do E6 hoje (v1 a
v5, cada correção de bug uma nova versão) — o número fecha.

**Não achei documentação oficial que confirme o mecanismo exato** (se
reseta por dia, se sessões já terminadas continuam contando, etc.) —
tentei, sem sucesso. O que sei com certeza é o que medi: 5 pushes gastos,
próximo push rejeitado, só 1 rodando.

**Consequência prática**: não consigo lançar lote 2 nem lote 3 agora —
sou eu mesmo que já gastei a cota de hoje, corrigindo bugs (o do output
que só saía no fim, depois o dos diagnósticos). Se a cota for diária,
libera amanhã; não sei se é semanal. Vou monitorar e testar de novo nos
próximos ciclos, sem gastar push à toa.

**Estado agora**: só o lote 1 (10 células) rodando, versão 5, ambiente já
instrumentado (specs saem quando a sessão fechar, discutido no aviso
anterior). Zero curva fechada ainda.
