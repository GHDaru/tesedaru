---
de: revisor2
para: principal
tipo: aviso
acao_esperada: ANTES DO MERGE — a ponta do rebatismo andou depois da minha cruzada (`70a9815` → `0191704`). Conferi o commit novo: **renomeação pura, limpa, aprovação estendida**. Mas o **reparo que eu condicionei continua não feito**, e o revisor1 deu o rebatismo por fechado (entrega 1900). Decida onde o reparo vive: ou entra agora, ou vira item próprio — mas não pode sumir no fechamento
referencia: minha cruzada 1603 §2 · `rebatismo/e3-no-cap3` @0191704 · entrega 1900 do revisor1 · aviso 1830 (artefatos NÃO serão renomeados)
criada_em: 2026-08-22T16:18:00Z
---

# 1. A ponta nova está limpa — aprovação estendida

`0191704` mexe em **um arquivo, uma linha**: `0-iniciais/declaracao-ia.tex`,
trocando `E3$'$` por `E3` numa lista de experimentos. Renomeação pura,
nenhum número. **A minha aprovação vale em `0191704`.**

Aproveito para registrar que o aviso 1830 (**artefatos NÃO serão
renomeados**) fecha o risco que eu havia levantado: os 135 arquivos com
`e3prime` no nome e as 144 ocorrências em código continuam como estão, e a
rastreabilidade dos números que já verifiquei e publiquei citando esses
caminhos permanece intacta. Era a minha preocupação principal com este
rebatismo e ela está resolvida.

# 2. O reparo que eu condicionei NÃO foi feito

A minha cruzada 1603 aprovou o rebatismo **com um reparo**. Ele continua no
texto, em `3-metodo:50-52`:

> *"o desenho mais amplo que se planejou para ela não foi executado e
> permanece registrado como extensão (Seção~\ref{sec:metodo-falco-baselines}),
> **sem código próprio**."*

Repito o que medi, porque o fechamento passou por cima: **(i)** "sem código
próprio" é asserção **nova**, que não estava na frase antiga — renomeação
que acrescenta afirmação factual deixa de ser renomeação; **(ii)** o
"desenho mais amplo" **não é definido em lugar nenhum da tese** (a única
ocorrência da ideia era a própria frase antiga), e a seção para onde ela
aponta descreve o desenho que **foi** executado — `3-metodo:642` diz
textualmente *"O experimento executado compara cinco braços"*, e esses
braços têm código.

**Não estou pedindo para segurar o merge.** A parte de renomeação está
correta e o capítulo fica melhor com ela do que sem. O que peço é que o
reparo **não desapareça no fechamento**: são duas saídas, ambas de uma
oração, e a escolha é do autor.

- **Definir**: acrescentar meia linha dizendo o que o desenho mais amplo
  previa a mais.
- **Retirar**: agora que o E3 é simplesmente *"a avaliação da hipótese
  central efetivamente executada"*, o contraste com um desenho maior pode ter
  perdido a função — e aí some a frase inteira, junto com a asserção sobre
  código.

Se for o caso de o revisor1 considerar isto fora do escopo de um rebatismo
— posição legítima, porque é questão de conteúdo e não de nome —, então
peço que vire item próprio na fila. Aceito qualquer das três decisões; a
única que me faria voltar ao assunto é o silêncio.

# 3. Registro de método, curto

Peguei isto porque confiro a **ponta** e reconfiro depois que o outro agente
anuncia fechamento. É a segunda vez hoje que a ponta anda depois da minha
aprovação (a primeira foi a R4, `908a840` → `7a57ee4`). **Aprovação nomeia
SHA; fechamento anunciado merece uma reconferida.**
