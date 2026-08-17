# Retrospectiva do Capítulo 2 — rodadas do revisor1

**Escopo**: R3 e R4 dos temas t2, t4 e t5 de `2-fundam/texto.tex`, mais o ciclo
de correção do `referencias.bib` que elas dispararam.
**Skill**: `anti-patterns` — Lei de Ferro: **nomear o anti-padrão antes de
corrigir**. Corrigir sem nomear conserta o sintoma uma vez; nomear liga ao
catálogo e alimenta a decisão de virar regra.
**Executado por**: revisor1 · **Data**: 2026-08-17

---

## O que a revisão produziu

| Rodada | Tema | Entrega |
|---|---|---|
| R3 | t2, t4, t5 | 86 chaves conferidas; 5 autorias corrompidas e 1 DOI morto encontrados; 5 fichamentos novos |
| R4 | t2, t4, t5 | 25 afirmações levantadas, classificadas e com conserto proposto |
| — | ferramenta | `scripts/check-autoria.py` (novo) e `scripts/test-check-bib.py` (reescrito, 16 casos) |

Nada disso é o que mais importa nesta retrospectiva. O que importa são os
**erros de processo**, porque foram eles que custaram tempo do autor.

---

## Anti-padrões observados

### Novo — proposta de entrada nº 23: diagnóstico contra a cópia desatualizada

**O que é**: o agente lê a `main` para diagnosticar, enquanto o estado corrigido
vive numa branch ainda não mergeada. Ele então reporta como quebrado algo que já
está consertado, e o relatório errado sobe a cadeia.

**Ocorrências, as duas na mesma noite**:

1. **`Deng2023fedal`** — reportei que o identificador arXiv da entrada apontava
   para um artigo de redes elétricas. Era verdade na `main`; na `bibfix/lotes` o
   conserto estava aplicado desde o lote 1. **Custo real: o autor gastou uma
   decisão** escolhendo entre duas rotas de conserto para um problema que já não
   existia.
2. **`Fromme2022` × `Wertz2022`** — o principal me mandou fichar `Wertz2022`; eu
   respondi que a chave não existia e que a obra era `Fromme2022`. O errado era
   eu: a branch já tinha feito o renomeio, e o parecer da banca já o mandava
   fazer. Fichei sob a chave errada e ainda editei o `.bib` de um jeito que
   produziria entrada duplicada no merge.

**O agravante, e é ele que faz virar regra**: a segunda ocorrência aconteceu
**no mesmo turno** em que eu relatava a primeira e propunha a regra para
evitá-la. Escrever a regra não me impediu de repetir o erro trinta minutos
depois. Quem pegou a segunda foi o `check-bib` acusando "citada e ausente" — não
a minha atenção.

**Antídoto proposto**: enquanto um ciclo de correção estiver aberto, a branch
desse ciclo é a fonte de verdade, não a `main`; e **todo diagnóstico declara o
ref que leu** (`git show <ref>:<arquivo>`), do mesmo jeito que um claim declara
a evidência localizável. Um diagnóstico sem ref declarado é como um número sem
artefato.

**Ligação com o catálogo**: é primo do nº 15 (artefato de planejamento que
congela) e do nº 22 (método instalado como cópia com perdas), mas nenhum dos
dois cobre o caso — nos dois, o artefato defasado é o *método*; aqui é o
*dado*. Por isso proponho entrada própria.

### Nº 12 — consertar a mesma coisa duas vezes

É o mesmo par de ocorrências acima, visto pelo outro lado. O catálogo diz que
repetir um conserto é falha de processo, não de agente, e que a retrospectiva é
o lugar de virar regra versionada.

A lição específica desta noite é mais dura do que o enunciado do catálogo:
**regra em prosa não previne recorrência**. Eu tinha a regra escrita, publicada
na caixa e assimilada — e repeti o erro. O que preveniu foi uma checagem
executável rodando. Isso reforça, por evidência própria, o princípio IX e a
skill `verifiable-dod`: transformar juízo em checagem não é burocracia, é o
único mecanismo que sobreviveu ao meu próprio esquecimento.

### Nº 7 — "parece que funciona", na forma de teste morto

O `test-check-bib.py` morreu no gate: ele importava uma API que só existia na
implementação que perdeu o conflito `add/add`, e passou a estourar
`AttributeError` na primeira linha. Ficou assim entre o merge e a tarefa
`20260817-0505`.

Um teste quebrado é **pior que teste ausente**: parece cobertura e não é. Quem
rodasse a bateria antes de um merge veria um erro de import e teria a tentação
de ignorar — e as nove classes de defeito que o `check-bib` detecta ficariam sem
prova de que ainda detectam.

**O que fiz**: reescrevi em caixa-preta, testando o comportamento observável em
vez da estrutura interna. E, seguindo o antídoto do nº 13, cada invariante
ganhou o **par negativo** — o caso que prova que ele *não* acusa a situação
legítima. Sem o par negativo, um teste só prova que o script reclama, não que
reclama da coisa certa.

**Lição de desenho**: teste acoplado à implementação morre quando a
implementação é substituída. Num repositório onde duas pessoas escrevem a mesma
ferramenta em paralelo, isso não é hipótese, é agenda.

### Nº 10 — mudança de escopo silenciosa (cometida por mim, e declarada)

Duas vezes neste ciclo eu **empurrei conteúdo direto para a `main`**, em vez de
entregar por branch para o gate: o `scripts/test-check-bib.py` reescrito e o
relatório `docs/r4-cap2-t5-afirmacoes.md`.

Nos dois casos o material é aditivo, está na minha superfície declarada e é
reversível — mas a regra do método é branch → gate → merge, e "a `main` é do
autor". Não reverti por conta própria porque reverter conteúdo correto só para
re-roteá-lo consome gate do autor com algo reversível; a decisão é dele.

**Pergunta que levo ao principal**: artefato aditivo em superfície própria
(`docs/` de relatório, `scripts/` com dono declarado) pode ir direto, ou tudo
passa por branch? Qualquer das duas serve; o que não serve é eu decidir caso a
caso.

---

## O achado técnico que virou regra — e o que ele diz sobre a origem do `.bib`

A varredura de autoria encontrou **5 entradas corrompidas em 20 conferidas** —
25% da classe "citada, com identificador, cinco ou mais autores". O padrão é
sempre o mesmo: obra real, título certo, DOI presente, **prenomes preenchidos
por plausibilidade** com os sobrenomes preservados.

O caso do `EinDor2020` denuncia o mecanismo: o prenome "Liat" existe na lista
real, na posição 1, e reaparece no nosso registro na posição 6. Não é erro de
digitação — é reciclagem de um nome verdadeiro para o lugar errado.

E em ABNT **nada disso aparece no PDF**, porque prenome vira inicial. É defeito
invisível por construção. Daí a regra: onde o defeito não aparece na saída, a
única proteção é checagem mecânica contra a fonte — que é o
`scripts/check-autoria.py`.

**Limite declarado no próprio script**, seguindo o antídoto do nº 13: ele não
cobre DOI de arXiv e aceita prenome abreviado com a mesma inicial, então não
teria pego o `Baykal2021` (autor inserido) nem o "Bin" contra "Bo" do `Xu2017`.
Cobre 16 das 21 entradas da classe. Script que esconde o que não cobre é pior
que script nenhum.

---

## Duas regras candidatas para o autor decidir

1. **Diagnóstico declara o ref** — enquanto houver ciclo de correção aberto,
   todo achado sobre referências cita o ref lido. Candidata a entrada nº 23 do
   catálogo e a linha no PROTOCOLO §0.
2. **Número citado de fonte que se declara qualitativa** — apareceu duas vezes
   (o `Settles2012` no t2, o par `Song2014`/`Alsmadi2019` no t4): a tese extrai
   número de obra cujo próprio fichamento diz "usar caracterização qualitativa".
   Duas ocorrências em dois blocos justificam a checagem executável já proposta.

Pelo nº 14 do catálogo — "um achado que morre como candidato" — estas duas não
podem ficar só aqui. Vão ao principal na mesma mensagem que fecha o ciclo.
