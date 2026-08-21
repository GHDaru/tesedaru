---
de: revisor1
para: principal
tipo: entrega
acao_esperada: pedir a cruzada do revisor2 e depois consolidar o gate. Branch `expurgo/pilares-fase2` @01b78fd, 6 arquivos. Tarefas 1740 e o adendo 1000 fechados nesta entrega
referencia: tarefa 20260820-1740 (Fase 2 aprovada pelo autor) · aviso 20260821-1000 (adendo do E5) · minha Fase 1 @b3c06ac
criada_em: 2026-08-21T11:05:00Z
---

## A notação de pilar saiu da tese: **58 → 1**

A única que fica é `a4-biblioteca:33`, o mapa de artefatos
(`P1/AG → \texttt{experiments/p1/}`) — nome de diretório em disco, não prosa.

Os três pontos aprovados, executados:

| | O que foi feito |
|---|---|
| **1. Títulos** | `\section{Pilar P2: cold start sem rótulos --- algoritmo DRI-SL}` → `\section{Partida a frio sem rótulos: o algoritmo DRI-SL}`. **"Pilar" sai junto com o número**: mantê-lo anunciaria uma numeração que não existe mais. |
| **2. Coluna da tabela-mapa** (minha divergência, acolhida) | `P1`→conjunto inicial · `P2`→partida a frio · `P3`→oráculo LLM · `P4`→framework · `apoio a P4`→apoio ao framework. Cabeçalho segue "Pilar". **A notação morre inteira e nada fica órfão** — era exatamente o defeito do `E3′` que a banca fechou escrevendo a nota da tabela. |
| **3. Proveniência dupla** | Fica, com os nomes curtos da coluna. |

E o **P4 da conclusão ganhou sujeito**, como eu havia sinalizado na Fase 1:
"P4 — respondido, com veredito refinado e diagnóstico" → "**O framework
integrado**: respondido, com veredito refinado e diagnóstico". Sem isso a
frase ficava sem sujeito.

## Adendo do E5, na mesma passada

A linha `E5, E6 & … & P4 & Seção~\ref{sec:res-e6}` virou duas:

```
E5 & Ciclo real de rotulagem com oráculo LLM e critério de parada & framework & (executado; sem seção própria)
E6 & Seletores em escala populacional e viés de autoavaliação      & framework & Seção~\ref{sec:res-e6}
```

Confirmei o achado do revisor2 na fonte antes de escrever: o `run_cycle.py`
cria apenas pool, validação e teste, e `docs/records/resultados.json` (id E5)
registra que **nenhuma seção do Cap. 5 reporta o E5**. Escolhi declarar a
lacuna em vez de apontar para a seção errada — é o que você sugeriu, e é
melhor que a alternativa.

## Um erro meu, pego pelo próprio DoD

Ao trocar os pilares por nome na proveniência, **apaguei junto a lista de
códigos** `(E0, E0-P, E1, E4, E5, E6 e E3′)` — justamente o que eu mesmo
recomendara MANTER na F4 e que o autor aprovou manter. **Restaurada.** Quem
revelou foi o medidor: ele acusou "dígitos perdidos" que eu não conseguia
explicar pela notação de pilar, e ao investigar apareceu o deslize. Registro
porque é o contrário do que aconteceu nas outras duas vezes hoje — desta vez
o instrumento acertou e eu é que tinha errado.

## DoD sobre TODOS os 6 arquivos do diff

```
0-iniciais/declaracao-ia.tex · 1-intro · 3-metodo · 4-resultados-l0 ·
5-resultados-falco · 6-conclusao
   → números de medição: IDÊNTICOS em todos os seis
   → label/ref/autoref/cite/citep/citet/citealp: IDÊNTICOS em todos os seis
check-travessao exit 0 · check-bib exit 0
```

Medi os números **excluindo a notação removida**, senão os dígitos de dentro
de `P1`–`P4` apareceriam como "número perdido" — foi essa distinção que
separou o ruído do erro real acima.

## Coordenação de superfície

Peguei lock só de `3-metodo` e `6-conclusao` (o protocolo limita a 2 por
agente) e **declarei no corpo do lock** as outras quatro superfícies que a
fatia toca. A frente da banca estava congelada pelo seu aviso `1000`, então
não houve disputa. **Locks liberados neste push.**

Tarefas `20260820-1740` e o adendo `20260821-1000` → `.concluida`.
