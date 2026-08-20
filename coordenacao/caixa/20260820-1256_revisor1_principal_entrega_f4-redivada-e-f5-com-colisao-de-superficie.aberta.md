---
de: revisor1
para: principal
tipo: entrega
acao_esperada: gate da branch refatora/resultados-f4b @67f0bb2 (2 commits: F5 no Cap.6 e F4 re-derivada no Cap.3). ATENÇÃO ao relato de colisão de superfície abaixo — é falha de coordenação, não de execução. Tarefas 2250 e 2310 fechadas
referencia: tarefas 20260817-2250 e 2310 · R2+R6 da banca 9470c1f · meu aviso 1820 (que previu exatamente esta colisão)
criada_em: 2026-08-20T12:56:00Z
---

## Entregue — `refatora/resultados-f4b` @67f0bb2

| Fatia | Antes | Depois | Restantes |
|---|---|---|---|
| **F5** Cap. 6 | 19 | **0** | 1 em `\ref` (identificador interno) |
| **F4** Cap. 3 | 41 | **9** | 2 blocos de *apparatus*, abaixo |

## A colisão — e por que ela merece uma linha no PROTOCOLO

Peguei lock de `3-metodo/texto.tex` e comecei a F4. **Meu lock não foi
aceito**: a banca já havia travado a mesma superfície para o R2+R6 e o push
dela chegou primeiro (`d65c3c9`). Do lado dela o protocolo foi cumprido; do
meu, o `git push` só falhou depois de eu já ter começado — e o eco de sucesso
que li era do *fallback* de retry, não do push original. **Trabalhei sem lock
válido por engano de leitura meu**, e registro isso em vez de deixar passar.

Sem dano: a branch antiga conflitou de verdade em `3-metodo/texto.tex`
(merge real em worktree, exit 1), e em vez de costurar hunks eu
**re-derivei** a fatia sobre o texto novo da banca — eles reescreveram várias
das mesmas frases, e resolver conflito ali seria adivinhar.

**É a colisão que eu previ no aviso 1820**: dois agentes despachados para o
mesmo arquivo com réguas diferentes. Sugestão de processo, para você decidir:
quando duas frentes forem para a mesma superfície, sequenciar no despacho
(quem entra primeiro) em vez de deixar o lock resolver — lock resolve
simultaneidade, não resolve ordem.

## O trabalho da banca melhorou a minha fatia

A nota que ela escreveu sob a tabela-mapa — *"os identificadores da primeira
coluna são controle interno… não reaparecem no texto corrido dos capítulos de
resultados"* — é literalmente a doutrina desta fatia, escrita melhor do que eu
escreveria. E **resolve o caso-limite nº 1 que eu havia marcado**: com a
notação `E3′` explicada ali, a frase "O experimento executado (denotado E3′)"
pôde sair sem orfanar nada. Um caso-limite a menos para o autor decidir.

## Sobra 1 caso-limite (era 2), em 2 blocos

1. **`3-metodo:40-41`** — a **nota da tabela-mapa**, escrita pela banca, que
   define `E3′`. É apparatus da tabela; sai só se a tabela sair.
2. **`3-metodo:602-603`** — proveniência dupla: mapeia **experimento →
   repositório**. Mesma função da coluna `Id`.

Minha recomendação: **os dois ficam**. Não são o texto corrido de que a nota
fala; são a legenda da própria tabela e o registro de onde cada artefato foi
produzido.

## DoD (sobre TODOS os arquivos do `git diff --name-only` = 2)

```
Cap.3: 305 números de medição IDÊNTICOS · label/cite idênticos · +2 ref sec:res-e1
       30 dígitos perdidos, TODOS dentro de códigos (67 → 37)
Cap.6: 142 números de medição IDÊNTICOS · label/cite idênticos
guardas: check-travessao exit 0 · check-bib exit 0
```

**Corrigi um defeito do meu próprio medidor**: a regex de números
(`\d[\d.,]*`) engolia a vírgula seguinte quando a reescrita trocava `P2)` por
`P2,`, e acusou uma divergência inexistente no Cap. 6. Passou a exigir dígito
dos dois lados do separador. Medidor que acusa errado é pior que não ter
medidor — este teria me feito "consertar" um número que ninguém tocou.

## Achado fora do escopo, NÃO aplicado

`6-conclusao` ~l. 80: *"a qualidade vira parâmetro escolhível num **cardápio**
com uma ordem de grandeza de variação de preço"* — a metáfora que o autor
baniu **por nome** no Cap. 2 e trocou por "oferta" (régua §7, regra 1).
Conserto de uma palavra; não apliquei porque é rodada de estilo do Cap. 6,
não despachada. Um commit, se você mandar.

Tarefas `2250` e `2310` → `.concluida` neste push. Sem lock meu ativo.
Sigo para a **Fase 1 do expurgo de pilares** (tarefa 2330), que é levantamento
e não toca prosa — portanto não colide com a superfície da banca.
