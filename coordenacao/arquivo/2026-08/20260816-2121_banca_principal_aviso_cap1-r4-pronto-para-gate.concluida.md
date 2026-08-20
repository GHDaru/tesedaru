---
de: banca
para: principal
tipo: aviso
acao_esperada: consolidar e levar ao autor o gate da branch banca/cap1-r4-correcoes; ao mergear, remover o lock coordenacao/locks/1-intro--texto.tex.md no MESMO commit (liberação atômica, §4)
referencia: branch banca/cap1-r4-correcoes @ c501eb3 · parecer docs/parecer-r3-r4-r6-leitura-final.md · lock 63e5963
criada_em: 2026-08-16T21:21:32Z
---
O QUE MUDOU: 3 correções do R4 no Cap. 1, aplicadas pela banca a pedido direto
do autor (exceção pontual à divisão de superfície, com lock tomado antes).

1. 1-intro:159 "revisão sistemática" -> "revisão narrativa focada" (alinha com
   a declaração do próprio Cap. 2, linha 744).
2. 1-intro:69-74 lacuna central agora remete à Tabela~\ref{tab:lacunas}
   (referência verificada: label existe em 2-fundam:808).
3. 1-intro:161 "programa experimental E0--E4" -> "programa experimental" (a
   faixa fechada contradizia os sete experimentos executados; optei por remover
   a faixa em vez de listar códigos, que seriam vazamento de camada no Cap. 1).

EVIDÊNCIA: diff de 2 hunks, 5 linhas; branch compila as mesmas referências
(checagem de \ref x \label feita); zero ocorrências de "revisão sistemática"
restantes no Cap. 1.

RISCO: baixo — redação, sem mudança de conteúdo técnico. O autor já viu o
antes/depois na conversa e mandou "mandar para aprovação".

DUAS PENDÊNCIAS CORRELATAS QUE FICAM COM VOCÊ (fora do Cap. 1):
- 2-fundam:25 tem a mesma "revisão sistemática" a trocar;
- a causa-raiz do item 3 segue aberta: tab:metodo-experimentos (3-metodo:38-56)
  lista só E0-E4, e o E5 é declarado executado em 6-conclusao:210 sem seção de
  resultados em lugar nenhum.

Com o merge, o Cap. 1 fecha R1+R2+R3+R4+R6; a banca inicia agora o R5 dele
(espelho do critério 30%/95% contra Caps. 3 e 5).
