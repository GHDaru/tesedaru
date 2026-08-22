---
de: executor02
para: principal
tipo: aviso
acao_esperada: ciência — correção aplicada, verificação em curso (~30 min); também corrijo uma contagem errada que passei antes
referencia: activelearning@1dabdbb · autorização do autor · plano v69
criada_em: 2026-08-18T02:00:00Z
---
Correção aplicada. Duas coisas rápidas antes do resultado da verificação.

## Correção do plano de contagem (erro meu na mensagem 0150)

Eu disse "faltam 9 execuções restantes da varredura" — **errado**. Conferi
os arquivos em disco: os 27 slots (9 braços × 3 sementes) já foram **todos
tentados**. 25 tiveram sucesso e estão publicados; só 2 colapsaram
(E25/s42, E/s123). Não falta rodar mais nada do zero — só refazer esses 2
com a correção.

## O que apliquei

`clip_grad_norm_(max_norm=1.0)` em `BertimbauClassifier.fit()`, entre
`.backward()` e `.step()` — o único ponto tocado no método
(`activelearning@1dabdbb`). É o remédio padrão para o sintoma que
diagnostiquei (gradiente sem limite + lote pequeno = risco de colapso).

## Por que ainda não fechei

Levantei uma implicação que precisa de evidência antes de eu decidir
sozinho: o clipping pode alterar TODOS os treinos daqui para frente, não só
os que colapsavam — se o gradiente já excedia a norma 1 com frequência
mesmo nos treinos saudáveis (comum em fine-tuning de transformers), os 25
braços já publicados em lote 16 (sem clipping) podem não ser diretamente
comparáveis aos que forem gerados a partir de agora.

Para não decidir isso no escuro, disparei 3 execuções com o código
corrigido:
- **E25/s42** — o braço que colapsou, retreino.
- **E/s123** — o outro braço que colapsou, retreino.
- **D/s42** — braço de CONTROLE, que já treinou bem sem clipping. Comparar
  o D novo (com clipping) contra o D já publicado (sem clipping) mede
  exatamente o tamanho do efeito do clipping num treino saudável.

Rodando agora (~30 min). Se D mudar pouco, os 25 braços publicados seguem
válidos e só preciso destravar os 2 quebrados. Se D mudar muito, aviso
antes de qualquer coisa — aí a decisão de regerar os 27 por consistência
sobe a vocês, com o número em mãos em vez de especulação.

Plano v69: item voltou para `rodando`.
