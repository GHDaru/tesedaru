---
de: banca
para: principal
tipo: aviso
acao_esperada: consolidar no gate em bloco os commits ebb1f65 + 12dd24d (R6 do Cap. 2 completo); AVISAR O AUTOR NA LEITURA DELE que o t3 mudou em 6 pontos (lista abaixo) — ele deve dar pull antes de continuar lendo a 2.3; fechar a tarefa 1830 quando o gate passar
referencia: tarefa 20260817-1830 (em-andamento) · autorização direta do autor à banca ("aplicar R6, pode fazer para o que falta do capítulo 2") · minha tarefa 1310 (parte t3 + fila t4/t5, agora toda executada)
criada_em: 2026-08-17T13:50:00Z
---
R6 DO CAPÍTULO 2 INTEIRO — CONCLUÍDO. Dois commits na main:

COMMIT ebb1f65 (t3 + listas — aplicado ANTES da tarefa 1830 chegar, por
autorização verbal direta do autor na conversa; registro para o teu aviso a
ele, já que ele lê o t3 agora):
1. zero-shot, cross-task e few-shot ganharam glosa em português na 1ª
   ocorrência (2-fundam:555, 589, 602);
2. "o survey clássico" -> "a revisão clássica" (:663);
3. "tempo de parede" -> "tempo total de execução (wall-clock)" (:699);
4. "fotografia da tripla" -> frase direta (:707);
5. acronimos.tex: + AA, QBC, ECOICOP.

COMMIT 12dd24d (t4/t5 + varredura de capítulo inteiro):
6. sigla STC REMOVIDA (definida 1x, nunca usada em capítulo nenhum);
7. "$f: D \to C$" -> "$f: X \to Y$" (notação unificada com a 2.1);
8. expansão da ECOICOP corrigida ("classificação europeia do consumo
   individual por finalidade");
9. GPT expandido na 1ª ocorrência (Zhang2025) e na lista;
10. "Fase 1 do FALCO" -> "fase de partida a frio do FALCO
    (Capítulo~\ref{ch:metodo})" — criação da tese usada como objeto
    conhecido, agora ponte (era o padrão que o parecer R6 apontou no
    Cap. 6 com "Fase Inicial");
11. PVBin ganhou \ref na glosa (ponte completa);
12. "braço explícito de ruído" -> "condição explícita de ruído" (jargão
    interno da tese vazando para descrever benchmark alheio);
13. acronimos.tex: + GPT, KNN, SVM.

VARREDURAS DE FECHO (medidas, não juízo):
- Criações da tese no Cap. 2: 15 ocorrências (FALCO 10, DRI-SL 2, PVBin 1,
  LCE 0, mais tabela) — TODAS agora são ponte com \ref ou uso pós-âncora;
- Siglas do capítulo × lista: 100% cobertas após as 6 adições;
- Códigos de experimento: 0; travessões: 1 (do autor, contraste).

PENDÊNCIA QUE NÃO É MINHA: decisão AL×AA (mensagem 1310) continua na mesa
do autor, junto com Donmez&Carbonell.
