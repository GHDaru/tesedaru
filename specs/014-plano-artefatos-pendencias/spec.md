# Spec 014 — Redesenho de "Artefatos e pendências" (página Plano)

**Status**: rascunho — aguardando decisão do autor (ainda não implementado)
**Pedido original do autor** (ciclo 014, 2026-08-22): "E regerar uma seção
similar para artefatos e pendências. (aqui quebrar em uma spec específica)."
**Origem do escopo**: parecer de 1 dos 3 especialistas consultados no mesmo
ciclo (linha de investigação 3/3 — "Quebra por tema" e "Artefatos e
pendências"), mais investigação própria confirmando os números citados.

## Por que uma spec própria, e não só um ajuste de CSS

O pedido do autor juntou, na mesma frase, o redesenho do "paradinha" por
capítulo (7 rodadas visíveis) e o redesenho de "Artefatos e pendências". São
coisas de natureza diferente: o primeiro é sobre a MESMA informação que já
existe na matriz, só mais visível; o segundo mexe em COMO os dados se
relacionam entre si (dependências entre itens) — decisão de produto, não só
de layout. Por isso o autor pediu explicitamente para separar em spec.

## Estado atual (medido, não citado de memória)

Seção `<details open><summary>Artefatos e pendências</summary>` na página
Plano (`scripts/render-plano-revisao.py`, HTML ~linha 543, JS ~linha 733-742
antes deste ciclo). Dado-fonte: `docs/records/plano-revisao.json`, campo
`artefatos[]` — hoje **9 grupos**, **36 itens** no total:

| Grupo | Itens |
|---|---|
| Experimentos (robustez E3′) | 3 |
| Publicações e deploys | 6 |
| Artigos derivados (a1-a5) | 3 |
| Defesa | 2 |
| Governança e qualidade | 3 |
| Biblioteca e software (concluídos recentes) | 3 |
| Melhorias do parecer R6 (agente executa, gate seu) | 7 |
| Encerramento e aprovação final | 6 |
| Dados (auditoria e publicação) | 3 |

Cada item usa o componente `.item` (mesma linha crua usada em "Execuções fora
do texto") — sem borda, sem card, status/título/dono numa linha só.

## Três achados que mudam o escopo (não é só "trocar `.item` por card")

**Achado 1 — `dono` tem baixo poder de diferenciação.** Os 36 itens usam só
dois valores em `dono`: `"autor"` ou `"agente"` — nunca um agente específico
(diferente do resto do site, que usa `.k-ag-dot` com `principal`/`revisor1`/
etc.). Agrupar por dono não separaria muita coisa.

**Achado 2 — `bloqueado_por` é um grafo de dependência real, hoje mostrado
como `id` cru.** Os itens têm `id` próprio e `bloqueado_por` referencia o
`id` de OUTRO item. Existe uma cadeia de 6 elos dentro de "Encerramento e
aprovação final": `normas-ufpr → dod-final → ars-fechamento →
aprovacao-orientador → gate-final → deposito` — na prática, o caminho crítico
até a defesa. Hoje isso aparece como texto cinza pequeno "⛓ normas-ufpr",
sem dizer que é uma corrente nem mostrar o título do item referenciado.

**Achado 3 — a seção duplica parcialmente "Fila do autor" (página
Controle/`index.html`).** `docs/records/kpis.json`, campo
`fila_autor.itens[]`, usa os MESMOS `id` de vários itens de `artefatos[]`
(`seed7`, `zenodo`, `kaggle-licenca`, `pypi-release`, `vercel`, `chaves`,
`autoria-ordem` aparecem nos dois). A fila do autor já agrupa por `trilha`
(texto/bibliografia/experimentos/processo/geral) e carrega
`pontos_destravados` — dois campos que `artefatos[]` não tem.

## O que entra no escopo desta spec (decisão de produto — não implementar sem decidir)

1. **Resolver `bloqueado_por` para título do item + navegação até ele**, em
   vez do `id` cru. Decidir como representar visualmente uma cadeia de
   bloqueio de vários elos (ex.: o caso de 6 elos em "Encerramento") — mini-
   fluxo em vez de 6 linhas soltas.
2. **Decidir a relação com "Fila do autor"** (mesmo `id`-space, vocabulário
   diferente): unificar campos (toda entrada de `artefatos[]` ganha `trilha`
   e `pontos_destravados` também) OU manter papéis conscientemente
   distintos — "Fila do autor" = ação imediata ordenada; "Artefatos e
   pendências" = registro completo por categoria — com link cruzado entre os
   dois quando o mesmo item aparece nas duas telas. Recomendação do
   especialista consultado: a segunda opção; mas é decisão do autor.
3. **Trocar `.item` pelo padrão de card** já usado em Resultados
   (`.experimento-card`) e no novo grid de capítulos deste ciclo — borda,
   fundo, grid responsivo.
4. **Ordenação dentro de cada grupo**: hoje é a ordem do JSON, sem critério
   visível. Com o grafo de bloqueio mapeado (achado 2), dá para ordenar por
   "quantos itens este item destrava".
5. **Revisitar nomes/fronteiras dos 9 grupos**: "Melhorias do parecer R6" e
   "Encerramento e aprovação final" têm sobreposição temática (ambos são
   pendências de fechamento) — perguntar ao autor se a divisão atual
   (crescida organicamente, ~1 grupo por rodada de pedido) ainda serve, ou se
   uma divisão por natureza do trabalho comunicaria melhor.

## O que NÃO precisa desta spec (pode entrar direto na implementação, sem decisão de produto)

- Trocar `.item` por card visual — reuso de componente já testado.
- Manter os 9 grupos como estão nesta rodada, se o autor não quiser mexer no
  item 5 agora.
- Manter `dono` como badge simples (autor/agente) sem tentar enriquecer —
  não há dado hoje para sustentar mais que isso (achado 1).
- O contador `${done}/${total}` no cabeçalho de cada grupo — já funciona bem,
  mantém.

## "Reatualizar os cálculos" aplicado aqui

Diferente da "Quebra por tema" (onde a fórmula do `%` não muda, só o
escopo visual), aqui a reatualização tem um componente de cálculo genuíno se
o item 1 for adotado: hoje nada calcula "quantos itens este item bloqueia" —
seria preciso somar, para cada `id`, quantas vezes ele aparece dentro de
algum `bloqueado_por` de outro item. Isso é um cálculo novo, pequeno, mas
precisa de artefato rastreável (princípio V da constituição da tese): ou
entra em `compute-kpis.py` (que já teria acesso ao grafo completo, e
alimentaria tanto `fila_autor` quanto `artefatos[]`), ou vira um campo
pré-computado no próprio `plano-revisao.json`. Essa decisão de ONDE calcular
também é parte desta spec, porque toca o pipeline, não só o template.

## Próximo passo

Aguardar a decisão do autor sobre os itens 1-5 (pode decidir uns e adiar
outros). Depois disso: `plan.md` com Constitution Check, `tasks.md`,
implementação em ciclo próprio — sem gate de merge (site/painel, ADR 0010),
mas com o mesmo tratamento de "trazer telas antes" se o autor pedir de novo.
