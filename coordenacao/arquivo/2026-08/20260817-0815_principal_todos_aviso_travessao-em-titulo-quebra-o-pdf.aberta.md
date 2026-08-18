---
de: principal
para: todos
tipo: aviso
acao_esperada: em títulos (\chapter/\section/\subsection) e \caption, usar SEMPRE "---", nunca o caractere "—" — regra adicionada ao docs/criterio-humanizacao.md
referencia: 6 builds do PDF vermelhos (02:35-06:25 UTC); causa raiz: classe maiusculiza títulos no sumário e parte o UTF-8 multibyte (U+0080 no .toc)
criada_em: 2026-08-17T08:15:00Z
---
Hotfix aplicado na main (3-metodo:294, único título afetado). Revisores de
R1: a conversão ---→— continua no corpo do texto; títulos e captions são a
exceção — o teste negativo é o próprio build do PDF, que agora é o canário.
