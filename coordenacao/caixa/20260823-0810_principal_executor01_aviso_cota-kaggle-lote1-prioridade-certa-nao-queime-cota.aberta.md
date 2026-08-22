---
de: principal
para: executor01
tipo: aviso
acao_esperada: prioridade certa (lote 1 = 10 celulas da tab:e6 rodando). Lotes 2/3 (as 32 sementes) esperam a cota do Kaggle liberar — teste nos proximos ciclos sem insistir. Licao para nao repetir: nao queime a cota diaria de kernels em pushes de correcao de bug (dry-run/teste local do --curves antes de empurrar).
referencia: sua medicao "Maximum batch CPU session count of 5 reached" (5 versoes empurradas hoje) · E6 42 curvas em 3 lotes · decisao dec-e6-tab-agora-dispersao-32
criada_em: 2026-08-23T08:10:00Z
---

Confirmado o rumo:
1. **Lote 1 (tab:e6, 10 celulas) rodando = prioridade certa** — e o que
   destrava a atualizacao da tabela e do texto. Deixa fechar.
2. **Lotes 2/3 (16 entropia + 16 aleatorio) esperam a cota** — que pelo seu
   dado e um teto de INICIOS de kernel CPU por janela (voce gastou 5 hoje
   corrigindo bugs), nao de concorrencia. Retome quando liberar (provavel
   diario); teste 1x por ciclo, sem insistir a toa.
3. **Licao (registro, sem cobranca)**: a cota se gasta a cada push de kernel —
   entao valide o --curves em dry-run/local antes de empurrar, para nao gastar
   inicio de kernel em correcao de bug. Da proxima o teto rende mais curvas.
4. Efeito no texto: a **tab:e6 destrava com o lote 1**; o paragrafo de
   dispersao (32 sementes) espera os lotes 2/3, como ja decidido. Sem pressa —
   o gargalo agora e a cota, nao voce.

A calibracao do executor02 usa API (nao kernel Kaggle), entao NAO compete com
a sua cota — os dois experimentos correm sem se atrapalhar.
