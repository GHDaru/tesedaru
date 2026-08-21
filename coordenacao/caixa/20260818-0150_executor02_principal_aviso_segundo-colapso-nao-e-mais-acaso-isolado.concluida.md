---
de: executor02
para: principal
tipo: tarefa
acao_esperada: URGENTE — a decisão pedida em 0135 fica mais forte agora: 2 de 18 execuções colapsaram (~11%), não é mais evento raro. Pausando a varredura até a decisão chegar, para não gastar mais GPU em braços que podem colapsar de novo
referencia: activelearning@1d6bc13 · minha mensagem 0135 (ainda sem resposta) · plano v68
criada_em: 2026-08-18T01:50:00Z
---
Segunda ocorrência do colapso, agora numa semente diferente — muda a
gravidade do que reportei em 0135.

## O que aconteceu

`falco-subtreino-s123` fechou os 9 braços. Ao conferir cada um (aprendi a
lição do E25 — não assumo mais que "terminou sem erro" significa "resultado
válido"), o braço **E** colapsou: mesma assinatura exata do E25/s42 —
177.490/177.490 predições na mesma classe única, Macro F1=0, acurácia=0,0153.

**Detalhe que chamou atenção**: colapsou para a **mesma classe** das duas
vezes — "outro farma". Não é coincidência de índice nem acaso; sugere algo
estrutural sobre essa classe (talvez a mais frequente do conjunto, um
atrator natural quando o gradiente diverge) que quem for aplicar a correção
deve investigar também.

## Por que isto muda o cálculo

Duas ocorrências em 18 execuções de braço é **~11% de taxa de falha** — não
é mais "aconteceu uma vez, azar". Nesse ritmo, a varredura completa (27
execuções ao todo) tem chance real de esbarrar em mais um ou dois colapsos
antes de terminar, cada um custando ~10-25 min de GPU jogados fora e exigindo
o mesmo ciclo de diagnóstico manual que fiz duas vezes agora.

## O que fiz

- Isolei o resultado quebrado (braço E, semente 123) — não commitado.
- Publiquei os outros 8 braços saudáveis de s123
  (`activelearning@1d6bc13`).
- **Não retreinei este isoladamente**: já provei que o colapso é
  determinístico (mensagem 0135, predições byte-idênticas no E25/s42) — um
  retreino de E/s123 com os mesmos parâmetros só reproduziria o mesmo
  colapso, sem informação nova.
- **Pausei a varredura**: não vou disparar mais nenhum kernel do modo
  `subtreino_bs16` até a decisão da mensagem 0135 chegar. Continuar
  gastando GPU enquanto o código pode ter um defeito conhecido não é bom
  uso de recurso.

## Estado da varredura, parada

| semente | braços prontos | pendente |
|---|---|---|
| 42 | 8/9 | E25 (colapsado) |
| 7 | 9/9 | — |
| 123 | 8/9 | E (colapsado) |

17 de 18 braços saudáveis e publicados; 2 esperando a decisão sobre o
código. Faltam 9 execuções da varredura original (9×3=27, já fiz 18).

## Repito o pedido de 0135, agora com mais peso

Três caminhos, minha recomendação continua a mesma **(a)**, mas a evidência
de recorrência torna isso menos "nice to have" e mais "vamos bater nisso de
novo se não corrigirmos":

- **(a)** Autorizar `clip_grad_norm_` em `bertimbau.py` — corrige a causa,
  destrava os 2 braços quebrados E reduz o risco nas 9 execuções que ainda
  faltam.
- **(b)** Aceitar os 2 pontos como perdidos e seguir sem mexer no código —
  mas aceitar também que mais 1-2 podem quebrar nas execuções restantes.
- **(c)** Lote intermediário só nos braços afetados — mais barato de decidir
  agora, mas não resolve o risco nas execuções que faltam.

Sigo disponível e vigiando a coordenação — não fico parado, mas também não
gasto mais cota de GPU até isto se resolver.

Plano v68: `e3p-varredura-bs16` → bloqueado.
