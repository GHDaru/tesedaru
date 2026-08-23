---
de: revisor1
para: principal
tipo: entrega
acao_esperada: CONSOLIDAR O GATE — o autor JÁ ACEITOU as duas figuras (exceção de roteamento autorizada por ele nesta tarefa). Branch figuras/cap3-arquitetura-e-dados @d00a847. Tarefa 0130 fechada nesta entrega
referencia: tarefa 20260818-0130 · aceite do autor em 2026-08-20 · achado da banca (a tese tinha 2 figuras, nenhuma no Cap.3)
criada_em: 2026-08-20T14:20:00Z
---

## Aceito pelo autor. Branch `figuras/cap3-arquitetura-e-dados` @`d00a847`

Duas figuras em TikZ no Cap. 3, renderizadas e mostradas a ele antes do
aceite, como a tarefa exigia:

- **Figura 3.1** — arquitetura e máquina de fases: o laço (pool, seleção,
  oráculo, classificador re-treinado a cada lote) e, abaixo, o que muda em
  cada fase, com a condição de transição e a Fase 3 desenhada tracejada
  por ser condicional;
- **Figura 3.2** — fluxo dos dados: da base original às três partições,
  passando por auditoria, deduplicação e particionamento por posição.

## Autoavaliação: 8 iterações, parada por convergência

Nota final: **fidelidade 10 · legibilidade 9,5 · legenda 9 · economia 9 ·
build 10**. Parei porque duas iterações consecutivas não subiram a nota (a 6
tentou mover o rótulo da transição e **piorou** para 5 em legibilidade; a 7
não recuperou; a 8 fechou).

Duas notas baixas no caminho merecem registro, porque só apareceram por eu
**compilar e olhar** o PDF, não o código: iteração 1 com legibilidade **3**
(o classificador ficou coberto pela caixa da Fase 2) e iteração 2 com build
**4** (a "População reservada" estourou a margem).

## Três decisões que o desenho forçou

1. **A palavra "holdout" não existe na tese.** Eu ia usá-la na Fig. 3.2 —
   ela vem do enunciado da tarefa. Conferi: zero ocorrências no repositório.
   Usá-la violaria a fidelidade ao texto E a régua de estrangeirismos.
   Passou a usar o termo do próprio Cap. 3: *validação e teste do ciclo real*.
2. **Meu medidor de margem estava errado.** O arranjo de prova usava 15 cm e
   acusava estouro; a tese tem **16 cm** (A4, margens 2+2, encadernação 1).
   Na geometria real: **zero `Overfull`**. É o segundo instrumento meu que
   erra hoje, e registro pelo mesmo motivo do primeiro.
3. **A divergência da população segue aberta e visível.** A Fig. 3.2 desenha
   os **177.490 que o TEXTO declara**. Não resolvi por desenho nem escondi.
   Se o autor decidir reexecutar (o código do E6 usa 181.490), a figura
   precisa de ajuste de **um número** — um `sed`, e eu faço.

## DoD

```
inserção aditiva: 97 linhas acrescentadas, 2 alteradas
   (as 2 alteradas são só as remissões Figura~\ref{} — figura não referenciada
    flutua para qualquer página; é a única prosa tocada, e declaro)
label/ref/cite: nenhum perdido; ganhos os 2 labels e as 2 remissões
números da prosa: IDÊNTICOS (excluindo os blocos de figura)
bibliotecas TikZ: NENHUMA nova — só arrows.meta e positioning, que a tese já carrega
guardas: check-travessao exit 0 · check-bib exit 0
travessão Unicode nas legendas novas: 0
```

## Sobre o lock

Tomei o lock de `3-metodo/texto.tex` **verificando o push**, não o eco do
retry — foi assim que errei de manhã. Liberado neste mesmo push.

Tarefa `0130` → `.concluida` com `## Resultado`. Continuam aguardando seu
gate, todas mergeando limpas: `refatora/resultados-f3` @`9d4a751`,
`refatora/resultados-f4b` @`67f0bb2`, `conserto/ficha-yuan2020-kmeans`
@`eb700a7`, `expurgo/pilares-fase1` @`b3c06ac` — agora cinco com esta.
