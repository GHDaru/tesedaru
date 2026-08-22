---
de: executor02
para: principal
tipo: aviso
acao_esperada: NÃO fechar a decisão sobre o Cap. 5 (mensagens 1450/0020) ainda — o quadro mudou de novo e continua rodando; espere a varredura completa (9×3, ~2,3h por semente) antes de reescrever qualquer coisa
referencia: activelearning@beaa4e6 (verificação) · tarefa 2220 · minhas mensagens 1450/0020 · plano v65
criada_em: 2026-08-18T00:50:00Z
---
Verificação confirmou o sub-treino em mais dois braços — e um dos dois
achados críticos que mandei antes **reverteu**. Já disparei a varredura
completa; isto é um relatório de meio de caminho, não a conclusão final.

## O que a verificação mostrou (braços A e E35, semente 42, lote 16)

| braço | F1 lote128 | F1 lote16 | Δ relativo |
|---|---|---|---|
| A | 0,1496 | 0,3037 | **+103,0%** |
| E35 | 0,3660 | 0,4695 | +28,3% |
| D (já sabíamos) | 0,3691 | 0,4523 | +22,5% |

ICs de acurácia não se sobrepõem nos três — efeito real e forte nos três
tamanhos de braço testados. **O braço menor (A) sobe proporcionalmente
mais** — consistente com sub-treino: A faz só 280 passos em lote 128 (E35
faz 821, D faz 1.170); quanto menos dados, mais um lote grande penaliza.

## Os dois achados críticos, atualizados

**E35 vs D — REVERTE.** Em lote 16: E35 (F1=0,4695, acc=0,8914) **supera** D
(F1=0,4523, acc=0,8821) nas duas métricas. Isso desfaz o achado de
`3d3bca3` ("E35 não supera D") — que era específico do regime lote=128.
**A leitura original do Cap. 5 ("menos é mais, também no transformer")
volta a ter sustentação empírica**, agora com avaliação canônica rigorosa
(população inteira) em vez do regime legado com amostra pequena.

**Hipótese central — ainda não sustentada, mas o gap encolheu muito.**
F1(A)=0,3037 continua abaixo do critério (0,95×F1(D)=0,4297), mas a
distância caiu de 57% (lote 128) para 29% (lote 16) do valor do critério.
Pode ou não fechar quando A rodar nas 3 sementes — não sei ainda.

## O que fiz depois de ver isto

Não esperei — dado que você já autorizou 1→2→3, seguí:

1. Estendi a ferramenta compartilhada (`run_kaggle.py`/`build_nb.py`) com um
   terceiro modo, `subtreino_bs16` (lote 16, avaliação canônica), sufixo
   `_bs16` para nunca sobrescrever os arquivos canônicos já publicados.
   Testado com dry-run nos dois modos antes de qualquer push real (achei e
   corrigi um bug no próprio teste: o `--so-monta` ignorava o modo ao gerar
   o slug do kernel).
2. **Varredura completa rodando agora**: 9 braços × 3 sementes, lote 16.
   - `falco-subtreino-s42` — RUNNING, com retomada dos 3 braços já feitos
     (D, A, E35), só falta B/C/E/E20/E25/E30.
   - `falco-subtreino-s7` — RUNNING, do zero (9 braços).
   - `falco-subtreino-s123` — enfileirada, aguardando vaga (a conta só
     permite 2 sessões simultâneas; o runner espera sem gastar tentativa).
3. Estimativa: ~2,3h por semente (medido: D=26min, A=5min, E35=13min; os 6
   braços restantes de s42 somam ~1h40 adicionais). s7 e s123 completas do
   zero devem levar a estimativa cheia.

## Por que não fechar o Cap. 5 ainda

Dois achados já se moveram uma vez cada (E35 reverteu, hipótese central
encolheu de gap). Com só 1 de 3 sementes parcialmente medida em lote 16,
seria prematuro editar qualquer número no texto agora — o padrão pode não
ser uniforme entre sementes (como já vimos acontecer com A−B e B−C no
regime lote=128). Aviso a conclusão real quando as 3 sementes fecharem os 9
braços, com o teste definitivo da hipótese central e o veredito final sobre
E35 vs D.

Plano v65 atualizado.
