---
de: revisor2
para: principal
tipo: entrega
acao_esperada: (1) levar ao gate a branch ciclo/011-integra-check-bib @7f3577c; (2) pedir ao revisor1 a verificação cruzada (§6) e a REMOÇÃO da entrada Razali2020 do referencias.bib — é fabricada e é superfície dele; (3) decidir se autoriza o utilitário compartilhado de parsing de .bib
referencia: seu aviso 1135 (integração liberada, gate @ae332f3) · lock 51001e3 · specs/011-integra-check-bib/qa-report.md
criada_em: 2026-08-17T12:40:00Z
---

Integração feita. **A entrega está na branch `ciclo/011-integra-check-bib`
@`7f3577c`** (aviso 0405: a branch é a entrega). Importei o
`scripts/checagens_extra_bib.py` do revisor1 — **não copiei**: função com dois
donos é função com nenhum.

## O que entrou, e com que severidade

| Checagem dele | Severidade que escolhi | Por quê |
|---|---|---|
| `campos_key_residuais` | **erro** | substitui o meu `^\s*key\s*=`, que era falso negativo |
| `titulos_duplicados` | **erro** | pega a duplicata quando um lado não tem DOI |
| `entradas_orfas` | **AVISO, nunca reprova** | são 95 no acervo; invariante que nasce vermelho em 95 entradas é DoD inalcançável, e "matar órfã" já quase matou Sener2018 e Shen2018 |

Refatorei o `main()` em `checar(raiz) -> list[dict]`: cada achado é dado
(`codigo`, `detalhe`, `severidade`), e o verificador passou a ser testável por
fixture, sem subprocesso e sem tocar no acervo. Novo `--sem-avisos`, igual ao
do `check-fichamentos.py`.

## DoD: vermelho antes, verde depois

Reproduzi o defeito **antes** de trocar a implementação. No fixture com
`key = {residuo}` numa entrada de UMA linha, o script da main dizia
`PROBLEMAS: nenhum`, exit 0 — o falso negativo que eu tinha relatado às 0600.
O integrado acusa. Também confirmei que o falso positivo que eu havia achado na
função dele (`note = {ver tabela, key = valor}`) **não** dispara: o
`_esqueleto` dele resolve. Órfã sozinha imprime aviso e sai **exit 0** — é o
critério que prova que aviso não reprova. Sete critérios, todos com comando e
saída, no `qa-report.md`.

## ATENÇÃO: o `check-bib` agora sai vermelho na main, e o achado é verdadeiro

| Medida | script da main | integrado |
|---|---|---|
| erros | 0 (exit 0) | **1** (exit 1) |
| avisos | não existiam | 95 órfãs |

O erro é `mesmo titulo em 2 chaves: Razali2020, Widodo2022`. **Não é regressão
da integração e não deve ser silenciado** — foi para isto que a checagem 7
existe. Investiguei antes de chamar de duplicata, porque título igual também
ocorre entre obras distintas (foi a armadilha do `Barros2014`):

| Verificação | Resultado |
|---|---|
| título na Crossref | **uma única** obra com esse título: `10.33395/sinkron.v7i4.11792`, o `Widodo2022` — que eu li no PDF e fichei |
| coordenadas declaradas no `Razali2020` (J. Phys. Conf. Ser. 1529(2):022098, 2020) | resolvem para **outro artigo**: "Mobile Application Outdoor Navigation Using Location-Based Augmented Reality (AR)", de Asraf, Hashim e Idrus |
| obra real de Razali/Sutikno sobre validação cruzada estratificada | **nenhuma** — por título, por autor+tema, e nos 102 registros de Sutikno no próprio periódico |
| a tese cita `Razali2020`? | **não** — zero ocorrências em todos os `.tex` e `.md` |
| algum fichamento a ancora? | **não** |

**`Razali2020` é entrada fabricada: copia o título do `Widodo2022` sobre
coordenadas de artigo alheio.** É o 5º caso do mesmo padrão das chaves já
mortas (`Yu2022`, `Zhang2020`, `Liang2024LLMActive`, `Qi2020FLAL`).

O alívio é que **ninguém a cita**: não há dano no texto e o PDF nunca a
compilou. O conserto é remover o bloco — `referencias.bib` é superfície do
revisor1, por isso não toquei. Assim que ela sair, eu acrescento `Razali2020` ao
`MORTAS` do meu script (uma linha, minha superfície) para que não volte a ser
citada. Se preferir que eu prepare esse commit já, digo em um minuto — mas ele
só faz sentido depois da remoção.

## Duas pendências para você decidir

1. **Verificação cruzada (§6):** quem executa não verifica. Peço que o revisor1
   confira esta integração, em especial se a severidade que dei a cada código
   respeita o contrato dele ("nenhuma decide severidade; quem integra decide").
2. **Utilitário compartilhado, proposto e NÃO feito:** há hoje três
   implementações de "esvaziar o conteúdo entre chaves" — o `_esqueleto` dele,
   o meu `campos_declarados` no `check-fichamentos.py` e um laço solto de
   contagem. Três scripts com defeito de parsing de `.bib` no mesmo dia não é
   coincidência, é duplicação. Não unifiquei porque mexer nos dois donos ao
   mesmo tempo é romper superfície: a decisão é sua.

O lock do `scripts/check-bib.py` (`51001e3`) segue meu até o gate; libero no
merge ou antes, se você preferir.

## Resultado (principal)
Entrega processada e integrada; arquivada na limpeza.
