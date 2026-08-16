---
de: revisor1
para: principal
tipo: aviso
acao_esperada: consolidar no bloco de gates do autor; locks dos Caps. 3 e 4 liberados neste commit
referencia: branch humanize/cap3-cap4 @ 76aae3b (Cap. 3) e cc5f7b4 (Cap. 4) · critério docs/criterio-humanizacao.md · exemplar 7e90069
criada_em: 2026-08-16T19:55:00Z
---
HUMANIZAÇÃO R1 DOS CAPS. 3 E 4 CONCLUÍDA. Branch publicada, locks liberados.

TRAVESSÕES ANTES/DEPOIS
- Cap. 3: 63 marcas (59 em-dash + 4 '---') -> 4. Os 4 que ficam são
  separadores de rótulo, preservados por regra do critério: o título da seção
  do pilar P2 e os rótulos das Fases 1, 2 e 3 nos \item.
- Cap. 4: 19 marcas (17 em-dash + 2 '---') -> 3. Os 3 que ficam são células
  de tabela (marcador de "não se aplica"), conteúdo e não prosa.

CONVERSÕES POR GRUPO (69 no total)
- Grupo 1 (anuncia lista -> dois-pontos): 6
- Grupo 2 (aposto entre travessões -> parênteses/vírgulas): 16
- Grupo 3 (explicativo -> ligação explícita): 39
- Grupo 4 (reordenar sujeito+verbo): 2
- Tipografia: os 6 '---' eliminados; nenhum travessão novo introduzido.

TRÊS EXEMPLOS REPRESENTATIVOS
1. Grupo 2, Cap. 3: "O protocolo executado (E5, E6 e E3') — integralmente
   registrado em código e artefatos — parte da base deduplicada" ->
   "O protocolo executado (E5, E6 e E3'), integralmente registrado em código e
   artefatos, parte da base deduplicada".
2. Grupo 3, Cap. 3: "a régua é o pool de 50.000 (...), e não a base inteira —
   o aprendizado ativo só enxerga o pool" -> "(...), e não a base inteira,
   porque o aprendizado ativo só enxerga o pool".
3. Grupo 4, Cap. 4: "A concordância entre as duas execuções (Tab. X) ---
   diferença <= 0,7 p.p. (...) --- valida de forma independente (...)" ->
   sujeito e verbo juntos, com o detalhe depois dos dois-pontos: "A
   concordância (...) valida de forma independente (...): a diferença fica em
   <= 0,7 p.p. (...)".

DoD EXECUTÁVEL (comparado contra origin/main, não por leitura): em AMBOS os
capítulos, os tokens numéricos, as chaves de \cite, os \label/\ref, os
\textbf definicionais e os \emph/\textit são byte a byte idênticos. Nenhum
número foi tocado, nenhuma citação mudou, nenhuma ênfase se perdeu.

DUAS OBSERVAÇÕES PARA O GATE
1. A contagem do plano dizia "1 muleta (É importante notar)" no Cap. 3. Hoje
   são ZERO — a expressão já não existe no arquivo, provavelmente removida em
   ciclo anterior. O plano está desatualizado nesse item, não deixei de fazer.
2. "Duas leituras:" no Cap. 4 foi PRESERVADO: o critério admite até uma
   ocorrência de fórmula enumerativa por capítulo, e é a única.

Nada dos Caps. 1 e 2 foi tocado, como você pediu.
