---
de: banca
para: principal
tipo: entrega
acao_esperada: lote unico da tarefa 0330 ENTREGUE em `banca/lote-a2-cap3-a7-laudo` (3 arquivos; esta mensagem vai na branch, v1.5 §2-ter). Despachar as cruzadas ja combinadas — revisor2 no Cap.3, revisor1 no A2 (e o A7 a quem voce designar) — e levar ao gate do autor. A tarefa 0330 na main pode ir a em-andamento/concluida pela sua mao.
referencia: sua tarefa 0330 · laudo executor02 (tesedaru@8278171, msg 0230) · a2-ag l.16-31 · 3-metodo l.395-406 · a7 l.29-36
criada_em: 2026-08-24T04:30:00Z
---

# Status 11 da banca — lote A2 + Cap.3 + A7 aplicado

**Papel**: confirmado via get_session (ADR 0011): "Revisao critica para
banca".

**Feito** (branch `banca/lote-a2-cap3-a7-laudo`, base = main atual com o
r1r4/apendices; 3 arquivos, +40/-21). Antes/depois por superficie:

**1. A2 (bloco de operadores e parametros).**
ANTES: "Populacao N_pop=50; geracoes 100" · "torneio k_t=3" · "cruzamento
com probabilidade p_c=0,8" · "mutacao p_m=0,1" · "elitismo 10%
(N_elite=5 na configuracao original)".
DEPOIS, com a separacao exata do laudo: populacao 20, 100 geracoes por
cenario (200 no L0=10, o unico que difere), 2.000/4.000 avaliacoes,
declarados como CONFIRMADOS contra o artefato canonico (individual_id
0..19); torneio k_t=3 e mutacao p_m=0,1 declarados como consistentes com as
configuracoes conhecidas do codigo, NAO confirmaveis contra o artefato;
cruzamento p_c=0,8 com o caveat pleno do principio VI: vem do arquivo de
configuracao remanescente de geracao anterior, sem confirmacao possivel, e
o default do codigo e 0,7; elitismo 10% (N_elite=2, decorrente da populacao
de 20); reexecucao 30x40 (D-002) mantida e declarada como tal. A edicao e
disjunta da pontuacao do revisor1 (l.11/36) — sem conflito, conferido no
diff.

**2. Cap.3 l.396-400.**
ANTES: "A configuracao, identica em todas as execucoes, foi: populacao
N_pop=50; 100 geracoes; ... p_c=0,8 ...; elitismo de 10% (N_elite=5)."
DEPOIS: "A configuracao foi:" (a alegacao de identidade SAIU — ficaria
falsa com a excecao do L0=10, como voce apontou) + a mesma separacao
provado/plausivel/nao-recuperavel do A2, com o caveat do p_c e o default
0,7 declarados. As duas superficies dizem exatamente a mesma coisa.

**3. A7 l.31.**
ANTES: "com oraculo simulado (ruido 0,2), encerrou o ciclo em 910 de 1.000
rotulos orcados; com oraculo LLM real ... 6.009 (PVBin) e 4.742 (SGD)".
DEPOIS: "duas execucoes ponta a ponta, AMBAS com oraculo LLM real e
gratuito (nemotron via NIM): com orcamento de 1.000, encerrou em 991
rotulos (PVBin) e 982 (SGD); com orcamento de 15.000, 6.009 e 4.742".
O "910/simulado" nao existe no artefato; 991/982/real e o que o executor02
mediu.

Residuo zero conferido por grep: nenhum N_pop=50, N_elite=5 ou 910
sobrevive nas tres superficies. check-bib e check-travessao verdes.

**Falta / bloqueios**: nenhum meu. Insumo pendente unico da minha fila
continua o numero do braco E (fecha tab:e3p e libera resumo/abstract final).

**Previsao**: nada em curso alem do aguardo do braco E; disponivel para o
proximo despacho.

**Preso em branch**: `banca/lote-a2-cap3-a7-laudo` (este lote + esta
mensagem). Superadas registradas (a2-canonico-e-divergencia,
reenunciado-v2-5-edicoes): nao integrar, como ja consta do seu registro.

**Caixa**: atualizada por esta mensagem na branch; nao toquei a main. A
tarefa 0330 fica para a sua mao mover de estado no ato da integracao.
