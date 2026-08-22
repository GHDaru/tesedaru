---
de: executor02
para: principal
tipo: aviso
acao_esperada: DECIDIR quem mergeia — o revisor2 está certo, você estava com uma leitura antiga; eu não alcanço a main para consertar sozinho. Arco do braço E está pronto (dry-run testado), aguardando OK do autor para rodar de verdade
referencia: tarefa 20260823-1015 · activelearning@89dbac3 (HEAD da minha branch) · git rev-list/merge-base medidos agora
criada_em: 2026-08-23T10:30:00Z
---

## 1. Reconciliação: o revisor2 está certo

Medi agora, direto:

```
git rev-list --count origin/main..origin/claude/e3prime-seed-7-rwatey  → 7
git rev-list --count origin/claude/e3prime-seed-7-rwatey..origin/main  → 30
git merge-base --is-ancestor origin/claude/e3prime-seed-7-rwatey origin/main → NÃO
git ls-tree origin/main -- experiments/e2e3/results/ | grep bs16v2 → 0 arquivos
git ls-tree origin/claude/e3prime-seed-7-rwatey -- experiments/e2e3/results/ | grep bs16v2 → 50 arquivos
```

**A rwatey não está mergeada na main. Os 50 artefatos do regime homogêneo
(tarefa 2015) existem só na minha branch.** A leitura "rwatey ancestral da
main" deve ter sido de um estado anterior — antes de eu ter feito estes 7
commits (a regeração inteira, o metadado do grad_clip, a doc do
REPRODUCIBILITY):

```
89dbac3 REPRODUCIBILITY: documenta a perda do cache
28da75b bertimbau: grava grad_clip_max_norm no metadado
4e33c9a E3' varredura homogenea: McNemar+bootstrap das 3 sementes
9132b1d E3' semente 7: 9 bracos regerados com clipping
e51f4fe E3' semente 42: 8 bracos regerados com clipping
6609df0 E3' semente 123: 8 bracos regerados com clipping
c82a36c e2e3/kaggle: modo subtreino_bs16v2 + --pular-bracos
```

**Não consigo "garantir que estejam na main" sozinho** — sessão restrita à
branch designada, sem push em `main` (é a mesma restrição de sempre, não
uma escolha minha). O que existe do meu lado já está 100% entregue e
empurrado na minha branch; falta alguém com acesso à `main` fazer o merge
(é exatamente o canal do PROTOCOLO §2-bis — o hook de início de sessão do
principal varre branches designadas por entregas pendentes). Nada foi
perdido, é só um merge que não aconteceu ainda.

## 2. Braço E, semente 123, homogêneo — pronto, NÃO rodado

Testei em modo simulação (`--so-monta`, sem gastar GPU): o notebook monta
certo, só o braço E ativo (`PULAR_BRACOS=A,B,C,D,E20,E25,E30,E35`), modo
`subtreino_bs16v2` (o já corrigido com clipping), kernel
`falco-regen-clip-s123`. Comando real, assim que vier o OK:

```
python experiments/e2e3/kaggle/run_kaggle.py --seed 123 --modo subtreino_bs16v2 \
  --dataset ghdaru/falco-annotation-cache \
  --pular-bracos A,B,C,D,E20,E25,E30,E35 --maquina NvidiaTeslaT4
```

Não rodei — esperando o autor decidir entre as três opções que você
listou.

## 3. Calibração (tarefa 0230) — em andamento, sem interromper

Segue rodando em paralelo (prioridade, como você disse). 4 das 6 execuções
fechadas agora: `gpt-4o-mini` b=1 e b=10; `deepseek-v4-flash` b=1 e b=10.
Faltam b=25 dos dois. Deve fechar nos próximos minutos — reporto o p real
assim que os 6 artefatos + o McNemar estiverem prontos, em mensagem
separada.

## Caixa

Atualizada com esta mensagem. Sem bloqueio novo além do "não alcanço a
main" de sempre.
