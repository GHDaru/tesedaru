# Auditoria de escrita anti-slop — Rodada 2 (2026-08-16)

Método: skill `humanizer` (padrões Wikipedia/WikiProject AI Cleanup) calibrada
pelo ADR 0001 (registro acadêmico PT-BR preservado; negritos definicionais e
tríades técnicas legítimos; alvo de travessões ≤3-5/1000 palavras, referência
do Cap. 1 humanizado = 3,0). Varredura quantitativa por script + leitura
qualitativa integral de todos os arquivos por 4 auditores independentes.
Complementa e detalha a auditoria de 16/08 citada no ADR 0001.

## Placar de severidade ("cheiro de IA", 0 = humano, 10 = slop puro)

| Arquivo | Palavras | Travessões (dens./1000) | Severidade | Diagnóstico em uma linha |
|---|---|---|---|---|
| `0-iniciais/resumo.tex` | 729 | 16 (21,9) | **9** | pior assinatura da tese na página mais lida; veredito central enterrado |
| `0-iniciais/abstract.tex` | 698 | 16 (22,9) | **9** | espelho em inglês, onde em dash parentético é o tell máximo; "—," agramatical |
| `6-conclusao/texto.tex` | 1.714 | 35 (20,4) | **8,5** | fecho aforístico autoelogioso + slogan tripartite onde a banca lê com mais atenção |
| `5-resultados-falco/texto.tex` | 4.895 | 64 (13,0) | **7,5** | 6 aberturas telegráficas ("Três leituras."), ~22 negritos de ênfase, molde repetido de "achados" |
| `3-metodo/texto.tex` | 4.640 | 59 (12,7) | **6,5** | frases-quilômetro com travessões aninhados (braços A-E: 6 numa frase); 6 fórmulas enumerativas |
| `2-fundam/texto.tex` | 6.194 | 110 (17,7) | **6** | 11 anúncios numerados no mesmo template; tique "exatamente/precisamente + FALCO" 6× |
| `4-resultados-l0/texto.tex` | 1.435 | 17 (11,8) | **6** | negritos de frase inteira e fechos de efeito nos pontos de maior visibilidade |
| `a7-parada-drift/texto.tex` | 606 | 9 (14,8) | 6 | aforismo "rotular mais é pagar para medir ruído"; comentário via travessão sistemático |
| `a4-biblioteca/texto.tex` | 291 | 4 (11,7) | 5 | parentético de 2 linhas separando sujeito de verbo |
| `a3-drisl/texto.tex` | 276 | 3 (9,3) | 4 | aforismo binário no fecho da "Intuição" |
| `a1-lce/texto.tex` | 295 | 3 (8,6) | 3 | abaixo do limiar; 1 par parentético ruim |
| `a5-prompts/texto.tex` | 343 | 4 (10,0) | 2 | 1 travessão está DENTRO do prompt v3 citado — não editar sem alterar o artefato |
| `a2-ag/texto.tex` | 217 | 2 (7,4) | 1 | limpo |
| `a6-tabelas/texto.tex` | 2.275 | 1 (0,4) | 0 | limpo |
| `1-intro/texto.tex` | 1.309 | 4 (3,0) | — | referência: já humanizado com gate (ADR 0001) |

Vocabulário de IA, muletas ("é importante notar") e atribuições vagas
genéricas: **zero em toda a tese** (confirmado por script e leitura). O
problema é de RITMO e MOLDE, não de conteúdo: os auditores confirmam que a
substância é técnica, honesta e rastreável.

## Achados que exigem correção FACTUAL (além de estilo)

1. **Resumo e abstract anunciam "Quatro resultados principais" mas enumeram
   CINCO** (i-v). Erro visível a qualquer leitor. Corrigir a contagem ou
   eliminar a fórmula.
2. **Cap. 5 L337-339**: "o colapso descrito na literatura em que a incerteza
   persegue os rótulos errados" — alegação de literatura **sem `\citep`**.
   Citar ou cortar (única violação próxima da regra de ouro).
3. **Cap. 2 L479-480 e L603-604**: "raramente tratada/instrumentada na
   literatura" sem citação de apoio — alvo fácil de arguição.
4. **Cap. 3 L379-381, L449-450, L529**: contrafactuais/alegações empíricas
   sem artefato na frase ("dobrariam ou triplicariam o custo", "ordens de
   grandeza", "razões são mais estáveis") — quantificar, apontar artefato ou
   atenuar.
5. **Cap. 5 L521**: "subserve" — anglicismo inexistente em PT-BR.
6. **Cap. 6 L74-75**: números derivados (96% da acurácia por 8,5% do custo)
   sem ponteiro de tabela.

## Padrões dominantes por capítulo (para os ciclos de humanização)

- **Resumo/abstract**: 16 travessões cada (1 frase com 4 aninhados); 4-5
  caudas participiais ("recuperando/grounding"); híbrido "—,"; veredito da
  hipótese central só a ~70% do parágrafo (viola "resposta primeiro").
  Fix de maior alavancagem: quebrar a frase da varredura de orçamento
  (elimina 8 travessões de uma vez) e antecipar o veredito.
- **Cap. 2**: converter enumerações entre travessões em parênteses (L14,
  109, 145, 258, 492, 634, 652, 680, 690) e apostos em dois-pontos; quebrar
  o metrônomo da abertura (L10-26) e conclusão (L839-848); reduzir o tique
  "exatamente/precisamente" de 6 para ≤2; dissolver metade dos 11 anúncios
  numerados.
- **Cap. 3**: reescrever a frase dos braços A-E (L464-486, 6 travessões) e o
  parágrafo de particionamento (L147-175); desbolar 8 negritos de ênfase
  (o de frase inteira em L529-531 é o pior); 9 caudas participiais; tique
  "travessão + gerúndio".
- **Cap. 4**: desbolar/reescrever o resultado central do P2 (L127-133:
  "não só... mas" em negrito + "forte indício" + "exatamente"); desmontar as
  2 frases-quilômetro da reexecução (L179-196); rebaixar 2 fechos de efeito
  da Seção 4.1.
- **Cap. 5**: eliminar as 6 aberturas telegráficas (L57, 275, 331, 427, 478,
  577); desnegritar ~22 estatísticas/frases-tese; reduzir travessões de 64
  para ~15; reescrever fechos com punchline (L219, 539-541, 586, 593-594).
- **Cap. 6**: cortar o aforismo final (L195-197 "Uma tese que termina com um
  número honesto... vale mais que uma promessa" — o fecho fabricado do ADR);
  desmontar o slogan "começar bem, perguntar bem, pagar bem" (L181-185);
  travessões 35→~5; limitar "não X, e sim Y" a ≤2 (hoje 5); uniformizar
  vocabulário do veredito (eliminar "infirmada", "coração", "moeda",
  "cardápio", "apetite").
- **Apêndices**: tratar `a7-parada-drift` (aforismo L22 + 9 travessões) e
  `a4-biblioteca` (parentético L20-22); demais são ajustes pontuais.

## Notas transversais

- Variação elegante a padronizar ENTRE capítulos: "padrão-ouro/gabarito/
  régua/teto supervisionado/referência" (Caps. 3-6) e "modelo pequeno/fraco/
  classificador leve" (Cap. 5). Escolher 1 termo por referente e fixar.
- A fórmula enumerativa real é maior que a medida por regex (Cap. 2: 11;
  Cap. 3: 6; Cap. 5: 9) — os auditores distinguem as legítimas (taxonomias
  citadas, objetos concretos) das de molde; só as de molde saem.
- Correções devem ser coordenadas entre Caps. 5 e 6 (mesmo esqueleto de
  "achados" em negrito): humanizar só um denuncia o outro.
- Ordem sugerida dos ciclos (densidade × visibilidade): resumo+abstract →
  Cap. 6 → Cap. 2 → Cap. 5 → Cap. 3 → Cap. 4 → a7/a4. Cada ciclo em branch
  `humanize/<alvo>` com antes/depois na conversa e gate humano (ADR 0001).
