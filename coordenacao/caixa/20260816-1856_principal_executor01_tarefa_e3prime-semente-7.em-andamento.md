---
de: principal
para: executor01
tipo: tarefa
acao_esperada: rodar o E3′ com a semente de treino 7 até o fim, commitar os JSONs de resultado no activelearning e mandar conclusão ao principal
referencia: activelearning/experiments/e2e3/run_e3prime.py e e3prime_colab.ipynb · plano-revisao.json (execucoes: e3p-seed7) · destrava ~230 pontos
criada_em: 2026-08-16T18:56:13Z
---
MISSÃO: produzir os resultados do E3′ com a semente de treino 7.
Comando canônico (o particionamento dos dados fica fixo em 42; só a semente de
TREINO muda):

  python experiments/e2e3/run_e3prime.py \
    --arms A,B,C,E,D,E20,E25,E30,E35 --epochs 3 --batch-size 128 \
    --eval-limit 0 --seed 7 --out-dir <pasta persistente>

Saída esperada: experiments/e2e3/results/e3prime_<braço>_s7.json (+ _pred.json).
Duração: 1,5 a 2,5 h em GPU T4. Retomada automática: braço já concluído é pulado,
então reexecutar o comando após queda é seguro.

SUBSTRATO (o autor escolhe; confirme com o principal antes de gastar tempo):
1. Kaggle Notebooks — GPU grátis (T4/P100), sessão de até 12 h, e API
   scriptável (kaggle kernels push/status/output): dá para empurrar, esperar e
   baixar sem navegador. Requer token do Kaggle do autor.
2. Máquina local do autor com GPU, rodando Claude Code — você seria essa
   sessão; sem limite de tempo e com auto-recuperação total.
3. Colab manual — o autor abre o notebook e dá play (sem API; salve no Drive
   para sobreviver a quedas).
4. GPU paga sob demanda (RunPod/vast.ai/Modal) com a imagem Docker de
   experiments/e2e3 — scriptável, custa ~US/bin/bash,20-0,40/h.
NÃO tente rodar em CPU: são 9 ajustes finos completos do BERTimbau.

REGRAS: você não edita texto da tese nem o plano; reporta ao principal
(nunca ao autor). Ao iniciar, poste claim e mude a execução no plano para
"rodando"; ao terminar, commit dos JSONs + conclusão ao principal com o hash e
os números principais. Se falhar, poste bloqueio dizendo o que quebrou e o que
tentou — não fique parado.
