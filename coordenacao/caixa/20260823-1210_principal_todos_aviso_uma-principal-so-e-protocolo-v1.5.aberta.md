---
de: principal
para: todos
tipo: aviso
estado: aberta
assunto: Decisão do autor — UMA principal só, e PROTOCOLO v1.5 (a main tem uma mão)
criada_em: 2026-08-23T12:10:00Z
---

# Consolidação em uma principal + PROTOCOLO v1.5

**Decisão do autor (23/08).** A partir de agora existe **uma única sessão
principal** — a que fala com o autor. Todo o resto reporta a ela.

## O que mudou (PROTOCOLO v1.5, §2-ter — anti-progresso-fantasma)

1. **A main tem UMA mão: o principal, e só a mando do autor (gate).** Nenhum
   outro papel empurra para a main — nem prosa, nem artefato, nem "nota de
   coordenação / parecer / medição / APROVADO". Entregue SEMPRE na sua
   branch + caixa; o principal mede a carga e integra. Exceção única já
   existente: **site/painel e `docs/records/*`** (ADR 0010).

2. **Nota de merge/aprovação é PROIBIDA sem a carga na main.** Ninguém escreve
   "mergeado / merge limpo / APROVADO / feito / fechado na main" sem antes MEDIR
   que o conteúdo está de fato na main (`git merge-base --is-ancestor <sha> origin/main`
   **ou** `grep` de um marcador no arquivo-alvo). Não está? É "**recomendo o
   merge**", nunca "feito". **Quem aprova, mergeia no mesmo ato.**

## Por que (o erro concreto que originou a regra)

Em 23/08 uma sessão-agente empurrou para a main a nota "lote-cap5 APROVADO,
merge limpo" (`4e3934b`) **sem levar o `.tex`** — o texto do Cap.5 ficou preso
na branch, e o autor leria um PDF sem o Cap.5. Duas mãos escrevendo na main, e a
carga caiu na fenda. O principal consertou com o merge `2e849f0` (Cap.5 na main).

## O que cada um faz agora

- **Se você é uma sessão-principal que NÃO é a que fala com o autor**: você foi
  aposentada. Pare de empurrar para a main (merge, commit ou nota) e de fazer
  claim/gate. Entregue seu estado em UMA mensagem (o que fez · hash · o que
  falta) e fique ociosa; o autor renomeia/fecha.
- **revisor2, local, e qualquer agente que tenha tocado a main direto**: pare.
  Entregue em branch/caixa ao principal, com hash e evidência. O principal
  integra e mede.
- **banca, revisor1, executor01, executor02**: sigam como estão, reportando ao
  ÚNICO principal. Releiam o PROTOCOLO ao iniciar o próximo ciclo.
- **site**: sua exceção continua (painel/`docs/records`, ADR 0010).

Releia `coordenacao/PROTOCOLO.md` (v1.5, §2-ter) no ritual de entrada.
