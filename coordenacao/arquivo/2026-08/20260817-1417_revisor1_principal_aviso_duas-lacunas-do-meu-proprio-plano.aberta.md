---
de: revisor1
para: principal
tipo: aviso
acao_esperada: DUAS LACUNAS DO MEU PLANO DA FASE 1, achadas pelo revisor2 — (1) 2 códigos no Cap.2 sem fatia atribuída, um deles escrito por MIM; (2) a notação RQ não foi inventariada e é decisão de escopo do autor, não minha. Nada a executar sem gate.
referencia: aviso do revisor2 20260817-1410 · docs/plano-refatoracao-resultados.md §1.3 · tarefa 1400 (marcada em-andamento)
criada_em: 2026-08-17T14:17:01Z
---

# O revisor2 achou duas lacunas no meu plano. Confirmei as duas.

Ele aceitou a cruzada da F1+F2 e confirmou que as superfícies são disjuntas —
não preciso combinar janela com ele. Mas os itens 2 e 4 do aviso dele expõem
falhas da **minha** Fase 1.

## Lacuna 1 — dois códigos no Cap. 2 que nenhuma fatia cobre, e um é meu

Ele apontou 2 `E6` em prosa no Cap. 2 e disse, corretamente, que não são da
faixa dele. Confirmei: **linhas 524 e 536, dentro da faixa t2** (262-538).

O problema é meu por dois motivos:

1. **O meu inventário da Fase 1 registrou "Cap. 2: 2 códigos"** — está lá na
   tabela do §1.2 — **mas a minha tabela de fatias (F1 a F6) não atribuiu esses
   dois a lugar nenhum.** Inventariei e esqueci de alocar. Uma fatia que não
   existe é trabalho que ninguém pega.
2. **A linha 536 fui eu que escrevi**, no R1 do t2 de hoje de manhã: ao
   converter um travessão, produzi *"O fenômeno é quantificado no experimento
   **E6** desta tese"*. Naquele momento a política de expurgo ainda não existia
   e eu estava proibido de mudar conteúdo — então não era erro. Mas hoje é
   dívida, e é minha.

**Proposta**: criar a fatia **F7 — Cap. 2 (2 ocorrências)**, pequena, para ir
junto com F3. Não a executo agora: a faixa t2 é superfície de revisão e eu
preciso de lock e do gate, como nas outras.

## Lacuna 2 — a notação RQ nunca foi inventariada, e a decisão não é minha

Ele levantou que `RQ3` **não é código E** e por isso está fora das 191. Está
certo, e confirmei rodando: o padrão do meu inventário não casa com `RQ`.

Mas a consequência é maior do que a ressalva dele sugere. **Existe uma segunda
notação na tese que eu nunca medi**, e ela é bem mais visível:

| Arquivo | Ocorrências de `RQ` |
|---|---|
| `3-metodo` | 10 |
| `5-resultados-falco` | 8 |
| `6-conclusao` | 3 |

E **quatro delas são títulos de subseção** do Cap. 5: `\subsection{RQ1 ---
assertividade}`, `RQ2 --- custo e o efeito do cache`, `RQ3 --- perfil de erro`,
`RQ4 --- efeito do instrumento de medição`.

Ou seja: acabei de reescrever os sete títulos de **seção** para tirar `E0`,
`E1`, `E4`… e logo abaixo deles continuam quatro títulos de **subseção**
começando por `RQ1`, `RQ2`, `RQ3`, `RQ4`. **A metade de cima do sumário fala
por achado e a de baixo fala por código.**

**Não decido isso, e explico por quê**: a ordem do autor foi sobre a notação
`EXXX`, que é controle interno. `RQ` é diferente — "questão de pesquisa" é
categoria que o leitor acadêmico **reconhece**, e numerar questões é convenção
legítima em tese. Pode ser que ele queira manter. As duas leituras são
defensáveis e a escolha é dele.

**O que peço**: leve a pergunta ao autor junto com os sete títulos, porque é a
mesma decisão vista de outro ângulo — *"o sumário deve anunciar achados ou
rótulos?"*. Se ele mandar tirar, é fatia nova e eu meço antes, como fiz com os
códigos E. Se mandar manter, registro a exceção no plano para ninguém tentar
expurgar depois por analogia.

## Sobre a ressalva do RQ3 dele

Concordo com a leitura dele: dos 7 tokens que removeu no t3, **6 são código E e
estão cobertos** pela política aprovada; o `RQ3` é o único de outra classe. Se o
autor decidir manter a notação RQ, aquele token isolado deve voltar — é um
minuto, e é dele.

## Estado

Tarefa 1400 marcada `em-andamento` (F1+F2 entregues, aguardando gate). **Não
inicio F3, nem a F7 que acabo de propor, sem gate.** As lacunas acima são
levantamento, não execução.
