---
de: revisor1
para: principal
tipo: entrega
acao_esperada: gate de `correcao/populacao-cap5` @af11ce8 (1 arquivo). O AUTOR JÁ APROVOU o conteúdo (itens 1 e 2 da recomendação do painel de dados). Ver também as duas mensagens irmãs deste push: pedido de tarefa de uniformização e um achado que abri em separado
referencia: painel de 3 especialistas de dados convocado pelo autor em 2026-08-20 · decisão dele no mesmo dia · divergência 177.490 × 181.490 × "≈140 mil"
criada_em: 2026-08-20T15:15:00Z
---

## O que foi decidido e aplicado

O autor convocou um painel de três especialistas (corretude estatística,
impacto numérico, abrangência documental) sobre a divergência da população
reservada. **Aprovou os itens 1 e 2**; o item 3 (alinhar slide da defesa e os
dois artigos) ele adiou para depois da tese.

Branch `correcao/populacao-cap5` @`af11ce8`:

1. **O "≈140 mil" saiu.** Não era recorte de nada: erra por −41.490 (−22,9%),
   nenhum artefato registra 140.000, e ele **nasce já errado no commit
   inicial**. Era o único erro factual entre os três números.
2. **O $n$ de avaliação passa a ser declarado**, com o motivo. O E6 avalia em
   **181.490** e o E3′ em **177.490**; a diferença são as 4.000 do conjunto
   retido. O texto agora diz por que o E6 não desconta: **ele não tem critério
   de parada** — percorre o orçamento inteiro e nunca consulta aquelas
   instâncias para decidir nada (quem para pelo conjunto retido é o E5).

## Um detalhe de terminologia que o autor pediu para detalhar

Usei **"conjunto retido"**, não *holdout*. A palavra *holdout* **não existe em
lugar nenhum da tese** — introduzi-la seria anglicismo sem glosa, contra a
régua de estrangeirismos que ele mesmo aprovou. É o mesmo achado que já tinha
aparecido ao desenhar a Figura 3.2.

## O que os especialistas mediram (para o seu registro)

- **Corretude**: não há vazamento. `run_population_curve.py:141-143` mostra
  que o laço do E6 só quebra por orçamento. Viés esperado **zero**, porque a
  partição é por posição *depois* do embaralhamento.
- **Impacto**: mudar de 181.490 para 177.490 desloca o Macro F1 em
  **≈0,04 p.p.** — uma ordem de grandeza **menor** que o desvio entre sementes
  já publicado. Nenhuma conclusão muda de sinal.
- **Custo**: **19,4 h** de CPU para reexecutar os 43 braços. Corrijo aqui um
  erro meu que reportei antes: eu havia dito 910 h, somando o campo
  `elapsed_s`, que é **acumulado** e não incremental — inflou em ~47×.

## Aviso de manutenção sobre este texto

O parágrafo que escrevi descreve o estado ATUAL (E6 em 181.490). O autor
manifestou preferência por **uniformizar** — ver a mensagem irmã. Quando a
reexecução entrar, este parágrafo troca de número e a explicação encurta.
Registro para ninguém achar depois que o texto ficou velho por descuido.

DoD: único número removido = `140`; nenhum `label`/`ref`/`cite` perdido, 3
`ref` ganhos; `check-travessao` e `check-bib` exit 0; 12 linhas acrescentadas,
1 alterada. Lock de `5-resultados-falco/texto.tex` liberado neste push.
