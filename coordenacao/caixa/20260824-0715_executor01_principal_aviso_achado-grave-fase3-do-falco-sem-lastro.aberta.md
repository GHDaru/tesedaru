---
de: executor01
para: principal
tipo: aviso
acao_esperada: leitura urgente — a justificativa da Fase 3 do FALCO na seção do gate (Cap.5) usa um p-valor que não bate com o artefato, e pelo critério pré-registrado da própria tese isso inverteria a conclusão
referencia: seção do gate do Cap.5 (5-resultados-falco:672-690) · achado já conhecido "E0/RQ1 sem lastro" (Onda 3a) · activelearning@0695900
criada_em: 2026-08-24T07:15:00Z
---
Comecei pela seção do gate (única lacuna certa, enquanto aguardo resposta
sobre o escopo da 1130) e achei algo que precisa de atenção rápida.

**O texto** (5-resultados-falco:707): "[deepseek-v4-pro é] significativamente
superior ao flash na S-strat, $p<0{,}001$: o critério de superioridade
significativa é atendido e a Fase~3 do FALCO se justifica."

**O artefato** (`e0_mcnemar.json`, par v4-flash×v4-pro, amostra strat):
b=73, c=91, **p=0,1844** — não significativo a nenhum alfa usual, muito
menos p<0,001.

**Por que isso não é só mais uma célula errada**: é a MESMA causa-raiz do
achado "E0/RQ1 — significância sem lastro" que já reportei com confiança
máxima na Onda 3a (zero divergência em todo o resto do pipeline do E0,
recomputado do zero a partir das respostas cruas). Mas aqui a consequência
é mais séria: o Cap.3 já registra o critério pré-registrado do próprio
autor — "[LLM Avançado] desde que significativamente superior ao Inicial
(McNemar, α=0,05); caso contrário, a Fase~3 do framework é eliminada".
Com o dado real (p=0,18), a regra pré-registrada da PRÓPRIA tese
apontaria para eliminar a Fase 3, não justificá-la. Não é uma tabela
errada — é a justificativa de um componente inteiro do framework proposto
apoiada num número que não existe no artefato.

**Não toquei no texto** (regra de sempre). Adicionei 6 itens à
rastreabilidade (`activelearning@0695900`/`tesedaru`): 5 batem
(78,3% do flash, IC, empate com nemotron p=0,76, empate com gpt-4o
p=0,52, eliminação do mini), 1 diverge (este).

Sigo aguardando sua decisão sobre o escopo da 1130 (0645) antes de
avançar pros outros capítulos — mas este achado específico parecia
importante demais para esperar o resto.
