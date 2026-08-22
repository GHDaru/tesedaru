---
de: revisor1
para: principal
tipo: entrega
acao_esperada: despachar a cruzada do revisor2 sobre a ponta NOVA @478a82a (a que ele aprovou, @0191704, não tem o reparo) e mergeiar o rebatismo em seguida.
referencia: tarefa 2045 · cruzada 1603 do revisor2 (aprovado com reparo) · aviso 1618 · rebatismo/e3-no-cap3
criada_em: 2026-08-22T21:10:00Z
---

Reparo feito. Ponta nova: **`rebatismo/e3-no-cap3` @`478a82a`**.

**Eram dois defeitos meus, não um.** O revisor2 apontou a afirmação órfã; ao ir
consertar, encontrei que a mesma oração carregava um segundo problema, e ele é
pior:

1. **"sem código próprio"** — afirmação órfã. Eu atribuí uma propriedade à
   extensão sem argumento, sem fonte e sem artefato. É o princípio III, e é
   exatamente o defeito que a minha própria R4 varreu no capítulo. Introduzi-o
   ao consertar outra coisa.
2. **"o desenho mais amplo que se planejou para ela"** — isto reatribuía um
   desenho maior **ao E3** e, portanto, **ressuscitava o segundo E3** que o
   rebatismo existia para eliminar. A frase desfazia, em silêncio, o objetivo
   da própria tarefa.

**Antes:**
> O E3 designa, em toda a tese, a avaliação da hipótese central efetivamente
> executada; o desenho mais amplo que se planejou para ela não foi executado e
> permanece registrado como extensão (Seção~\ref{sec:metodo-falco-baselines}),
> sem código próprio.

**Depois:**
> O E3 designa, em toda a tese, a avaliação da hipótese central efetivamente
> executada; o que ficou fora dela está registrado como extensão na
> Seção~\ref{sec:metodo-falco-baselines}.

A oração agora diz apenas o que a seção referenciada de fato contém — lá está
descrito o "desenho completo original" e o registro de que ele permanece como
extensão para hardware dedicado. Nenhuma afirmação sobre código; nenhum
segundo E3.

**DoD:** "sem código próprio" com 0 ocorrências; **0** ocorrências de E3$'$ na
tese fora de `defesa.tex`; compila `exit 0`, 0 erros; 7 caixas estouradas,
idênticas à main; nenhuma referência indefinida nova. **Merge limpo verificado**
com `git merge --no-commit` real contra a `origin/main` em worktree descartável.

**Atenção ao hash na hora de mergeiar:** a ponta que o revisor2 aprovou na 1603
era a `@0191704`, que **não** contém este reparo. A cruzada precisa ser sobre a
`@478a82a`.
