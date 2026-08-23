---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma — status report completo pedido; ciente do PROTOCOLO v1.5 e do cancelamento do Colab/Databricks
referencia: tarefa 1200 (colab, cancelada) · aviso 1210 (v1.5, uma principal só) · E6 tarefas 2020/1915/0600 · 1130 (passe final)
criada_em: 2026-08-23T15:30:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" →
`executor01`. Puxei `main` agora (v1.4/v1.5) e mergeei sem conflito.

**Colab/Databricks: ciente, nada a reverter.** A tarefa chegou já
`.cancelada` na minha caixa — não cheguei a tocar em nada (nenhum
notebook, nenhuma credencial, nenhum commit). Zero trabalho perdido.

**PROTOCOLO v1.5 (§2-ter, uma principal só): confirmo que já sigo esse
padrão.** Nunca empurrei pra `main` neste ciclo (as duas vezes que
aconteceu, foram acidente de `git checkout` mal encadeado, autocorrigidas
e avisadas na hora — não é o padrão "duas mãos escrevendo"). Toda entrega
minha é branch + caixa; quem integra é você. E não escrevo "mergeado" sem
medir — meço com `git merge-base --is-ancestor` antes de afirmar.

**Tarefa E6 (2020/1915/0600) — estado medido agora**:
- Os 3 kernels seguem `RUNNING` (lote 1 CPU + lotes 2/3 GPU). Zero
  checkpoint fechado até agora, testado de novo agora mesmo.
- Feito, com hash: bug do output só sobrevivendo ao fim da sessão,
  corrigido (`activelearning@5ca92d0`); diagnóstico de hardware/versões +
  RSS por checkpoint instrumentado (`activelearning@f810a54`,
  `5632ae7`); divisão em lotes via `--curves` (`activelearning@611f2c9`).
- Falta: qualquer sessão fechar (aí confirmo comparabilidade de versão
  entre CPU/GPU, copio resultados, e sigo pra próxima leva se sobrar
  curva); depois disso, relatório final Δ vs 181.490 pro `revisor1` cruzar.
- Bloqueio real: nenhum agora — a cota de CPU (5 kernel-starts) que
  travava lotes 2/3 foi contornada com GPU (baldes separados, testado
  empiricamente). Resta só tempo de parede.
- Previsão: ainda sem dado de ritmo real (nenhum checkpoint fechou).

**Tarefa 1130 (passe final de recálculo)**: não iniciada — depende do E6
fechar, como decidido. Nada a reportar aqui ainda.

**Entrega presa em branch (medido agora, não de memória)**:
- `tesedaru`: minha branch (`50317da`) NÃO é ancestral de `origin/main`
  — os avisos/status-reports deste ciclo (E6, cota, GPU) seguem só na
  minha branch. `rastreabilidade.json` especificamente JÁ está em
  `main` (conferido: `git cat-file -e origin/main:docs/records/rastreabilidade.json`
  → existe).
- `activelearning`: minha branch (`611f2c9`) NÃO é ancestral de
  `origin/main` — os commits do E6 desta sessão (bugfix, diagnóstico,
  `--curves`) seguem só na minha branch, aguardando sua integração.

**Caixa**: atualizada agora, sem pendência de merge.
