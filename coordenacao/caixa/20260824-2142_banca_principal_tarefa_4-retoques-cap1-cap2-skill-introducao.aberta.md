---
de: banca
para: principal
tipo: tarefa
acao_esperada: triar os 4 retoques menores abaixo (risco zero, sem numeros novos) e aplicar/gatear conforme a superficie; o laudo completo ficou na conversa banca-autor
referencia: encomenda do autor (auditoria dos Cap.1-2 contra skill de introducao cientifica) · main @55908f9 · sem arquivo novo, achados abaixo
criada_em: 2026-08-24T21:42:00Z
---
Encomenda do autor: auditar os Capitulos 1 e 2 contra uma skill de
introducao cientifica (Information/Flow/Citations/Style: contextualizacao ->
lacuna -> estado da arte -> proposito). VEREDITO: os dois capitulos PASSAM
em todos os itens do checklist (fluxo geral->especifico, lacuna especifica e
tabelada, hipotese falseavel, seminais/recentes/importantes nos papeis
certos). O autor aprovou despachar apenas os 4 retoques menores:

1. 1-intro/texto.tex:36-43 — o paragrafo que APRESENTA o aprendizado ativo
   cita so a survey (zhang-etal-2022-survey); a definicao fica sem o
   seminal no Cap.1. Sugestao: acrescentar \citep{Settles2009} junto a
   definicao ("O aprendizado ativo (active learning) enfrenta diretamente
   esse custo: seleciona iterativamente os exemplos potencialmente mais
   informativos para anotacao \citep{Settles2009}."). Settles2009 ja e
   citado na nota da hipotese (fichamento existente).

2. 1-intro/texto.tex:24-25 — "alterou significativamente o estado da arte":
   adverbio sem trabalho (nao e significancia estatistica); cortar
   "significativamente" nao muda o sentido.

3. 1-intro/texto.tex:50-58 — "A principal delas e o problema de cold start":
   o ranking apoia-se na survey citada no fim do paragrafo; colar a citacao
   a afirmacao ("A principal delas \citep{zhang-etal-2022-survey} e o
   problema de cold start...") blinda contra arguicao.

4. 2-fundam/texto.tex:910-918 — bloco "LLM no laco" condensa 5 trabalhos em
   uma frase (selecao, rotulagem, roteamento, destilacao, misturas); e o
   trecho mais proximo da "sequencia de resumos". Desdobrar em duas frases
   (ex.: cortar apos "\cite{Zhang2025}," e retomar "Completam o quadro o
   roteamento hibrido humano-LLM...").

Nota de fluxo REGISTRADA SEM ACAO (conflito de genero, recomendo manter):
a skill manda estado da arte antes do proposito; na tese o proposito
(Cap.1) precede o estado da arte pleno (Cap.2). A mitigacao ja existe
(lacuna do Cap.1 cita ActiveLLM/Zhang2025 e remete a tab:lacunas).

Superficie: prosa do Cap.1/Cap.2 e dono unico do principal; a banca nao
tocou nos arquivos. Retoques 1-3 sao mecanicos; o 4 e editorial leve.
