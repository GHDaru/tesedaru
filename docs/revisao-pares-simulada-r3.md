# Revisão por Pares Simulada — Rodada 3 (academic-paper-reviewer v1.9.0, modo full)

**Manuscrito**: tese completa (89 pp., compilação limpa) + biblioteca (70 testes)
+ FlowBuilder + documentação operacional. Mudanças desde a R2: braço free
completo (nemotron/NIM) com achado de *serving*; ciclo E2E real com dois
classificadores; ciclo de vida pós-treinamento (parada/liberação/drift) no
Cap. 6 e na documentação; E5 fechado.
**Data**: 17/07/2026 · Notas ordinais, sem calibração com gold set.

## Fase 0 — banca reconfigurada

Mesmas cinco personas da R1 (EIC de PLN aplicado; metodologista experimental;
especialista em AL; engenheiro industrial de ML; advogado do diabo cético de
LLM), agora avaliando um manuscrito COMPLETO exceto pelo braço GPU declarado.

## Parecer 1 — Editor-Chefe (originalidade/significância): 82/100

O trabalho consolidou uma identidade rara: **tese de instrumentação** — as
contribuições mais fortes são sobre COMO medir (efeito do enum; inflação de
circularidade quantificada em −6,3 p.p.; teto do gabarito; e agora o achado de
que *o provedor de serving é parte do instrumento*, com o mesmo modelo
divergindo de si mesmo entre serviços, p<0,001). Esse último achado é inédito
na literatura de LLM-como-anotador que o Cap. 2 cobre e merece destaque no
resumo (hoje não está lá). Preocupação remanescente: a narrativa ainda promete
o E3 como clímax; se a defesa ocorrer antes da execução GPU, o texto precisa
de uma passagem de "leitura do estado atual" mais assertiva na conclusão.

## Parecer 2 — Metodologia: 86/100

Pontos fortes: cadeia inferencial disciplinada (Wilson/McNemar exato/Wilcoxon
com teto declarado/bootstrap); pré-registro do gate e das constantes;
anticircularidade demonstrada e quantificada; curvas interna/externa separadas
no ciclo E2E com teste fora de qualquer decisão.

Problemas remanescentes (nenhum bloqueante):

1. **[MODERADO] Reprodutibilidade de oráculo LLM é temporal.** Temperatura 0
   não garante determinismo entre versões/provedores — o próprio achado de
   serving da tese o prova. O texto data os custos, mas deveria declarar
   explicitamente que TODAS as medições de oráculo são fotografias de
   (modelo, provedor, data), idealmente na seção de ameaças à validade.
2. **[MODERADO] Transferência dos rankings do E1.** Menor margem/menor
   confiança vencem entropia COM PVBin; a ordem pode mudar com BERTimbau
   (probabilidades mais calibradas). O texto usa o resultado para configurar a
   Fase 2 do FALCO — vale uma frase de contingência ("ranking a revalidar no
   E3-GPU").
3. **[MENOR] Ciclo E2E n=1.** O ciclo real roda com semente única (demonstração
   de instrumental, não inferência) — está honesto no texto, mas a legenda da
   figura deve dizer "1 semente, ilustrativo".

## Parecer 3 — Domínio AL: 84/100

A tese agora cobre o ciclo completo: cold start → seleção → oráculo → parada →
(desenho de) drift. A conexão parada↔resolução da validação (≈1/√n) é
elegante e pouco explorada na literatura aplicada. Ausências toleráveis:
comparação com métodos de parada da literatura (e.g., Vlachos 2008;
Ishibashi & Hino 2020) — uma nota de rodapé resolveria; e o braço free único
(nemotron) não permite generalizar "modelos gratuitos empatam com pagos" —
o texto corretamente NÃO generaliza, mas o resumo deve manter essa cautela.

## Parecer 4 — Perspectiva industrial: 88/100

A parte mais transferível segue sendo custo/vazão/serving + FlowBuilder. O
guia de parada/drift com três camadas e gatilhos numéricos é diretamente
aplicável em produção — recomendo transformá-lo em apêndice da tese (hoje só
está na documentação da biblioteca). O episódio D-005→D-006 (cota → troca de
provedor do mesmo modelo) é um estudo de caso operacional que eu citaria no
corpo do texto, não só em decisões.

## Parecer 5 — Advogado do Diabo: 74/100

Ataques que permanecem de pé (mitigados, não eliminados):

1. **A hipótese central segue não testada.** Tudo até aqui é evidência de
   componentes. Se o E3 mostrar que com BERTimbau a seleção ativa não supera
   RS (plausível: classificadores fortes diluem o valor da seleção em pools
   médios), o framework vira "engenharia de custo de oráculo" — valiosa, mas
   não o que o título promete. A tese está protegida FORMALMENTE (hipótese
   condicional, critérios de refutação), não substancialmente.
2. **Dataset único do autor** — inalterado desde a R1; a réplica STOPS segue
   promessa.
3. **Novo**: o orçamento de 30.000 (60% do pool de 50k) do ciclo em execução
   é cientificamente estranho — em 60% de rotulagem, QUALQUER estratégia
   converge para o teto do oráculo; a leitura interessante está no primeiro
   terço da curva. Que o texto reporte a curva inteira mas ancore as
   conclusões na região ≤30%.
4. **LCE**: segue a contribuição mais frágil; a demarcação frente à ALC está
   correta, mas "métrica nova" é generoso — eu diria "variante operacional".

## Síntese editorial

| Dimensão (peso) | R1 | R2 | R3 |
|---|---|---|---|
| Originalidade (20%) | 78 | 80 | 82 |
| Rigor metodológico (25%) | 68 | 85 | 86 |
| Suficiência de evidência (25%) | 70 | 82 | 84 |
| Coerência argumentativa (15%) | 80 | 85 | 85 |
| Apresentação (15%) | 76 | 84 | 85 |
| **Média ponderada** | 73,6 | 83,3 | **84,5** |

### Decisão: **MINOR REVISION** (inalterada — o gap é o bloco H, não o texto)

Roteiro (não bloqueante, ordem de prioridade):

| # | Ação | Esforço |
|---|---|---|
| 1 | Ameaças à validade: declarar medição de oráculo como fotografia (modelo, provedor, data) | 1 parágrafo |
| 2 | Cap. 5/E1: frase de contingência sobre revalidação do ranking no E3-GPU | 1 frase |
| 3 | Resumo: incluir o achado de serving; manter cautela sobre free único | 2 frases |
| 4 | Apêndice novo: guia de parada/liberação/drift (portar da documentação) | baixo |
| 5 | Ciclo 30k: reportar curva inteira, concluir sobre a região ≤30% | na análise |
| 6 | Nota de rodapé: métodos de parada da literatura | baixo |
