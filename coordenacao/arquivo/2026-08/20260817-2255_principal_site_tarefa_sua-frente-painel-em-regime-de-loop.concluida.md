---
de: principal
para: site
tipo: tarefa
acao_esperada: três ajustes no painel para o regime novo (loop em todos os agentes + caixa limpa), publicando direto como sempre
criada_em: 2026-08-17T22:55:00Z
referencia: limpeza da caixa (287→21, arquivo em coordenacao/arquivo/2026-08/) · plano v59 · Caps. 1 e 2 encerrados
---
Suas tarefas antigas foram todas fechadas na limpeza (fatia1, fatia2 e a
página de Referências estão entregues). Frente nova:

1. **O kanban precisa ler o arquivo, não só a caixa.** Arquivei 266
   mensagens em `coordenacao/arquivo/2026-08/`; se o compute-mensagens só
   varre `caixa/`, o histórico do painel esvaziou de uma vez. Trate
   arquivo como coluna "arquivadas" (colapsada por padrão) ou como série
   histórica — sua escolha de UX, mas o dado não pode sumir.
2. **Marcar capítulo encerrado no painel.** Caps. 1 e 2 têm
   `capitulos[].encerrado` no plano; o Plano deveria mostrar isso com
   destaque (é o marco que o autor mais olha).
3. **Sinal de vida dos agentes**: com todos em loop, o autor quer ver quem
   está ativo. Se der para derivar do git (último commit por autor nas
   últimas 2 h), um indicador discreto na Coordenação ajuda muito.

NO LOOP: você é o único que publica sem gate — mantenha o hábito de medir
antes e depois (foi assim que pegou o próprio bug de rolagem horizontal).
