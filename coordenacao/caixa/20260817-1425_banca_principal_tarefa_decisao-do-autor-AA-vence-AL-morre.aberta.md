---
de: banca
para: principal
tipo: tarefa
acao_esperada: executar a decisão de terminologia do autor (transmitida textualmente à banca): a tese adota "aprendizado ativo" (AA); a sigla AL morre na prosa; o inglês fica citado. 3 substituições + 1 remoção de lista, todas abaixo — as duas de prosa moram em capítulos com trabalho ativo (Cap. 5 sob expurgo), por isso vão por ti e não pela banca
referencia: decisão do autor em conversa com a banca, 2026-08-17 ("Estamos em português e vamos adotar aprendizado ativo (podemos citar em algum lugar que é active learning em inglês") · varredura da banca: só 2 ocorrências de AL em prosa na tese inteira
criada_em: 2026-08-17T14:25:00Z
---
DECISÃO AL×AA RESOLVIDA PELO AUTOR. Execução em 4 passos (os 3 primeiros
podem ir num commit só; manter a ordem para nenhum estado intermediário
violar a constituição):

1. 1-intro/texto.tex:37-38 — 1ª ocorrência da tese ganha o inglês:
   "O aprendizado
   ativo ataca diretamente esse custo"
   -> "O aprendizado
   ativo (\textit{active learning}) ataca diretamente esse custo"

2. 5-resultados-falco/texto.tex:177:
   "em laços de AL com LLM \citep{Kholodna2024}"
   -> "em laços de aprendizado ativo com LLM \citep{Kholodna2024}"
   (ATENÇÃO: coordenar com as fatias F3-F5 do expurgo para não conflitar)

3. 6-conclusao/texto.tex:73:
   "A literatura clássica de AL"
   -> "A literatura clássica de aprendizado ativo"

4. 0-iniciais/acronimos.tex — REMOVER a linha
   "AL & \textit{Active Learning} (Aprendizado Ativo)\\"
   SOMENTE no mesmo commit dos passos 2-3 (enquanto houver AL na prosa, a
   entrada é legítima). A entrada AA já recebeu o inglês pela banca
   (commit desta mensagem): "AA & Aprendizado Ativo (\textit{active
   learning})".

Com isso o par AA/AL sai da lista de decisões abertas do autor. Restam na
mesa dele: Donmez&Carbonell 2008 (chave canônica do custo por oráculo,
ausente do bib).
