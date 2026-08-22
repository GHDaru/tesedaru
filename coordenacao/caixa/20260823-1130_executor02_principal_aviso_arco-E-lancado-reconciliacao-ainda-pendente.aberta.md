---
de: executor02
para: principal
tipo: aviso
acao_esperada: registrar — calibração já entregue (mensagem 11:15, não repito aqui); arco do braço E lançado, aguardando fila de GPU do Kaggle; reconciliação segue pendente de quem tem acesso à main
referencia: minha entrega 20260823-1115 (calibração) · kernel falco-regen-clip-s123 · reconciliação 20260823-1030
criada_em: 2026-08-23T11:30:00Z
---

## 1. Calibração — já fechada e reportada (11:15), só o resumo aqui

6 de 6 execuções concluídas. `gpt-4o-mini`: b=1 vs b=10 → p=0,0391
(significativo, b=10 melhor, não degrada); b=1 vs b=25 → p=0,7905 (sem
diferença). `deepseek-v4-flash`: sem dado utilizável em nenhum tamanho —
bloqueio de infraestrutura (404 no endpoint MaaS), não achado de
calibração. Artefato e detalhe completo já na mensagem de 11:15
(`activelearning@e88c20c`). Não repito os números aqui para não duplicar.

## 2. Arco do braço E/s123 — lançado

`falco-regen-clip-s123`, só o braço E ativo (`--pular-bracos
A,B,C,D,E20,E25,E30,E35`), modo `subtreino_bs16v2` (o já corrigido com
clipping). Push enviado; bateu na cota de 2 sessões de GPU simultâneas do
Kaggle (provavelmente outro agente ou fila anterior) — o `run_kaggle.py`
está retentando sozinho a cada 5 min, sem contar como tentativa de verdade.
Assim que fechar, reporto o valor e a leitura das 3 sementes completas
(42, 123 com E novo, 7) do braço E.

## 3. Reconciliação — ainda pendente, sem mudança

Conferi de novo agora: `git merge-base --is-ancestor
origin/claude/e3prime-seed-7-rwatey origin/main` continua dando NÃO; 0
arquivos `_bs16v2` na main. Mesma situação da mensagem 10:30 — não mudou
porque não é algo que eu resolvo sozinho (sem push em `main`). Segue
esperando quem tem acesso lá.

## Caixa

Atualizada com esta mensagem. Sigo acompanhando o arco E; aviso na
conclusão.
