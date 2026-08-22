---
de: site
para: principal
tipo: aviso
acao_esperada: ciência. Um ponto pede sua leitura: a prontidão global caiu
  de 36,7% para 34,1% como efeito mecânico do modelo de pontos ao desagregar
  em mais elementos — não é perda de trabalho, mas vale você saber a causa
  antes de alguém estranhar o número.
referencia: tarefa 20260822-1640 (concluída) · commits a68cebf/2f723cd ·
  plano v85 · pergunta 20260822-1415 (fechada por esta resposta)
criada_em: 2026-08-22T17:15:00Z
---

Papel confirmado pelo título da sessão (ADR 0011): "Site da Tese funcional"
→ sou o `site`. Ritual feito antes de responder: `git fetch origin main` +
rebase, li a caixa por glob, conferi a tarefa 1640 linha por linha antes de
executar.

**O que já publiquei.** A desagregação por elemento está feita e publicada
(commit `a68cebf`, plano v85): `capitulos[]` passou de 8 para 15 entradas —
"Resumo" e "Abstract" saíram do agregado "Pré-textuais" e viraram elementos
próprios; os 7 apêndices saíram do agregado "Apêndices A1-A7" e viraram
elementos próprios (A1 a A7), cada um mostrado como seu próprio painel na
página Plano, exatamente como pedido ("cada elemento na tabela"). Cada um
tem estado medido do arquivo (existe), rodadas R1-R7 e uma marcação "na"
(não "pendente") nas rodadas que genuinamente não se aplicam — medi isso
direto no arquivo, não chutei: contei quantas vezes cada apêndice usa
`\cite`/`\citep`/`\citet`, e 4 dos 7 (A2, A5, A6, A7) têm zero citações, então
a rodada R3 (referências × fichamento) está "na" neles; os outros 3 (A1, A3,
A4) têm 1 citação cada, aplicável. Os R7 de TODOS os 15 elementos (e também
dos 6 capítulos que não mudaram de estrutura) agora mostram o rótulo
"↻ a reauditar" em vez de "○ pendente" no pill — é um rótulo novo só na
tela, o status interno continua "pendente" (não mudei o vocabulário do
schema, que teria efeito em toda a conta de pontos). Testei nas 8 páginas
do site, claro/escuro/mobile, sem erro. Minha pergunta em aberto desde
20260822-1415 está respondida pela sua decisão 1640 — considero-a fechada.

**Achado que registrei, não corrigi.** A nota antiga do agregado
"Pré-textuais" dizia "32 travessões (16 no resumo + 16 no abstract)". Contei
direto no arquivo hoje: 22 (11 + 11). Não sei se o arquivo mudou desde que
alguém escreveu aquela nota, ou se a contagem original usou outro critério.
Não decidi qual número está certo — usei o que medi agora para os elementos
novos, e deixei a divergência escrita no `atualizado_por` do JSON para quem
for revisar R1 do Resumo/Abstract já saber que há um número desencontrado.

**O que falta.** Nada tecnicamente pendente da minha parte nesta tarefa.
Fica em aberto, para quando alguém tiver tempo de revisão editorial de
verdade: os 15 elementos novos estão todos com rodadas aplicáveis marcadas
"pendente" (exceto R6 do Resumo/Abstract, que herdei "feito" do agregado
anterior) — ninguém fez a leitura R1/R2/R4/R5/R6 individual de cada
apêndice ainda, porque isso é trabalho editorial de conteúdo, não coisa que
eu meça de um arquivo.

**Um ponto que pede sua leitura, não só ciência.** A prontidão global caiu
de 36,7% para 34,1% (pontos totais foram de 2032 para 2209; pontos feitos
quase não mudaram, de 877 para 887). Não é retrocesso de trabalho — é
efeito direto do modelo de pontos (ADR 0006, "especialista em indicadores"):
algumas rodadas têm custo FIXO por elemento (R2=15, R4=20, R6=10, R7=10 ou
20), não importa o tamanho do arquivo. Antes, esse custo fixo era cobrado 2
vezes (um para o agregado "pre", um para o agregado "ap"); agora é cobrado
9 vezes (Resumo + Abstract + 7 apêndices), porque cada elemento novo carrega
seu próprio custo fixo de revisão final. O trabalho realmente feito não
diminuiu — o "tamanho da régua" aumentou porque a régua agora tem mais
marcações. Não mudei a fórmula de pontos (não é minha alçada); só quero que
você saiba a causa antes que o número pareça um retrocesso para o autor.

**Bloqueios.** Nenhum.

**Caixa.** Atualizada — nada `.concluida` com mais de 48h, nada `.aviso`
para todos com mais de 7 dias. Restam abertas só avisos meus recentes
(informativos, sem ação pendente de ninguém) e um aviso seu de todos
(gate-so-pelo-principal), que não me diz respeito além de ciência.
