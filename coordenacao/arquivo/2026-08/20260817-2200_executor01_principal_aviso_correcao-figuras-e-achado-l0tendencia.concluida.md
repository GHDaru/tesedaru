---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma ação obrigatória — correção de auditoria + achado novo, para o quadro geral de decisões
referencia: rastreabilidade.json (tesedaru@30d758b, activelearning@3896780) · segue de 20260817-2015
criada_em: 2026-08-17T22:00:00Z
---
Retomando a fila (nada novo na caixa), reexaminei o item "sem-evidência"
sobre `experiments/plots/`. Minha nota anterior estava ERRADA: dizia "nenhuma
figura está versionada" — falso, as 6 (E1/E4/E6×2/ciclo/E0) estão commitadas
há vários commits e reproduzem byte-a-byte a partir dos artefatos já
auditados. Corrigido para "rastreado".

O achado real, que a nota errada escondia: nenhuma dessas 6 está de fato
`\includegraphics`'da no texto atual do Cap. 4/5 (conferi por grep) — script
e figura existem e batem, só não foram inseridas na tese ainda. E a ÚNICA
figura que de fato está no texto hoje (`L0tendenciagerallog.png`, Cap. 4)
NÃO tem gerador neste repositório — foi commitada direto no tesedaru, sem
script associado. Inverteu: a que eu marcava como faltando é a que existe;
a que eu dava como certa é a que falta.

rastreabilidade.json: 97 itens (77 rastreado, 14 divergente, 5 sem-evidência,
1 legado). Sem mais pendências que eu consiga destravar sozinho — os 3
sem-evidência do Cap. 3, o L0tendenciagerallog.png e o bloqueio do cache do
oráculo seguem precisando de decisão do autor/principal ou de dado que não
está neste repositório.
