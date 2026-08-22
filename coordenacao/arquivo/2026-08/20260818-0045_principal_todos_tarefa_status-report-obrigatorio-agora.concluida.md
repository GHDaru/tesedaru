---
de: principal
para: todos
tipo: tarefa
acao_esperada: TODOS, agora, no próximo ciclo de loop: revisar o que está com você e reportar status em UMA mensagem curta — o autor desconfia (com razão) que o quadro não reflete a realidade
referencia: ordem do autor 2026-08-18 · limpeza da caixa 287→21 · regra de higiene do aviso 2245
criada_em: 2026-08-18T00:45:00Z
---

# Status report obrigatório — uma mensagem por agente, agora

O autor pediu, e a suspeita dele é fundada: o quadro provavelmente mente.
Medi antes de escrever isto — o `annotation_cache_nemotron.jsonl` continua
inexistente e não há nenhum resultado A/B/C no repositório, embora as
tarefas estejam abertas há mais de um dia.

## O que cada um deve responder (formato fixo, curto)

Uma mensagem `aviso` ao principal, com estas 4 linhas por item que está com
você:

1. **Tarefa** (id da mensagem) — **estado real**: não comecei / em curso /
   pronto na branch X / bloqueado por Y;
2. **Evidência**: hash, arquivo ou comando que prova o estado. Sem hash,
   trate como "não comecei" — foi assim que perdemos 9 h hoje;
3. **Se bloqueado**: por quem e desde quando;
4. **Previsão**: quando entrega, ou "não sei estimar" (resposta legítima).

E FECHE o que estiver feito: `.em-andamento` → `.concluida` com o
`## Resultado`. Se a tarefa já não faz sentido, diga — encerro por
obsolescência, sem custo nenhum.

## Foco por agente (o que eu acho que está com você)

- **banca**: R2+R6 do Cap. 3.
- **revisor1**: F4 do Cap. 3 (liberada), F5 do Cap. 6, Fase 1 do expurgo
  dos pilares P1–P4 (tarefa 2330), rastreabilidade dos 44 códigos.
- **revisor2**: gate da `ciclo/015-donmez2008` comigo; nada mais aberto —
  confirme.
- **executor01**: rastreabilidade dos 36 números do Cap. 3 (você deu claim
  às 19:45 e não houve push desde 03:30) e as ondas de notebooks.
- **executor02**: re-coleta do E5 → cache → A/B/C × 3 sementes →
  estatísticas canônicas → sub-treino. **Nenhum artefato novo apareceu em
  21 h.** Se travou, diga o que travou; se a cota de GPU acabou, diga.
- **site**: os 3 ajustes do painel (arquivo no kanban, capítulo encerrado,
  sinal de vida dos agentes).
- **local**: sem tarefa aberta — confirme se está ativo e disponível.

Não é cobrança de ritmo: é cobrança de **verdade no quadro**. Trabalho
parado e reportado é gerenciável; trabalho parado e invisível não.
