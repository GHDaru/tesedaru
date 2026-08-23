---
de: executor02
para: principal
tipo: aviso
acao_esperada: status consolidado das 4 frentes vivas, pedido pelo principal; braço E é prioridade — bloqueado por cota de GPU compartilhada (provável E6 do executor01), retentando sozinho
referencia: tarefas 1015/0230/2100 · protocolo v1.5 §2-ter
criada_em: 2026-08-23T12:00:00Z
---

Consolidando as 4, como pedido — reporto só a você (§2-ter), nada vai à
main pela minha mão.

## 1. Braço E/s123 homogêneo — PRIORIDADE, em fila de GPU

**Feito**: lançado, push aceito, kernel `falco-regen-clip-s123`, só o
braço E ativo. **Falta**: rodar de verdade — ainda não passou da fila.
**Bloqueio**: cota do Kaggle é 2 sessões de GPU simultâneas por conta;
`kaggle kernels list --mine` mostra 3 kernels `RUNNING` agora
(`falco-e6-lote3-gpu-teste`, `falco-e6-lote2-gpu-teste`,
`falco-e6-reavaliacao-177490`) — parecem ser do E6 do executor01. Não mato
kernel de ninguém; meu script reempurra sozinho a cada 5 min sem gastar
tentativa. **Previsão**: dependo de uma vaga abrir — se o E6 estiver perto
de terminar, minutos; se for sequência longa de lotes, pode ser mais.
Depois de entrar na fila, o braço sozinho deve rodar rápido (é 1 de 9, os
outros 8 da s123 levaram ~2h no total). Aviso a conclusão assim que sair.

## 2. Reconciliação (tarefa 1015) — sem mudança, aguardando quem mergeia

**Feito**: verificado de novo agora —
`git merge-base --is-ancestor origin/claude/e3prime-seed-7-rwatey
origin/main` → **NÃO**; 0 arquivos `_bs16v2` na main; 8 commits meus só na
branch designada. **Falta**: alguém com push em `main` mergear. **Entrega
presa na branch**: os 8 commits abaixo, todos já em
`origin/claude/e3prime-seed-7-rwatey` (activelearning):

```
e88c20c calibracao E0 (item 3)
89dbac3 REPRODUCIBILITY (item 4)
28da75b grad_clip no metadado
4e33c9a varredura homogenea: McNemar+bootstrap 3 sementes
9132b1d semente 7: 9 bracos com clipping
e51f4fe semente 42: 8 bracos com clipping
6609df0 semente 123: 8 bracos com clipping
c82a36c modo subtreino_bs16v2 + --pular-bracos
```

**Bloqueio**: eu não tenho push em `main` (restrição da sessão, não
escolha). Nada a fazer do meu lado além do que já fiz.

## 3. Calibração E0 (tarefa 0230) — FECHADA

**Feito**: 6/6 execuções, McNemar real calculado, artefato commitado
(`activelearning@e88c20c`, dentro dos 8 acima). `gpt-4o-mini`: b=1 vs b=10
→ p=0,0391 (sig., b=10 melhor — sem degradação); b=1 vs b=25 → p=0,7905
(sem diferença). `deepseek-v4-flash`: sem dado válido em nenhum lote — 404
no endpoint MaaS, bloqueio de infraestrutura, não achado de calibração.
**Falta**: nada do meu lado — a frase da tese (5-resultados:174, hoje cita
p=0,58 de outro experimento) precisa de quem tem a superfície do Cap.5, e o
endpoint do deepseek precisa de quem administra o MaaS. **Previsão**: N/A,
já terminou.

## 4. Consertos de reprodutibilidade (tarefa 2100) — FECHADA

**Feito**: cache do E2E — documentação em `REPRODUCIBILITY.md` (não abri
exceção no `.gitignore`, motivo já reportado: conflito com a política de
privacidade da tarefa 20260817-0020); `run_falco.py` — caminho certo
medido (`src/activelearning/application/run_falco.py`) e devolvido, sem
editar `a4-biblioteca/texto.tex` (superfície da tese). **Falta**: só a
edição do apêndice, que não é minha superfície.

## Caixa

Atualizada com esta mensagem. Braço E e reconciliação seguem abertos (1 em
execução, 1 bloqueado por acesso); calibração e consertos de repro estão
fechados do meu lado.
