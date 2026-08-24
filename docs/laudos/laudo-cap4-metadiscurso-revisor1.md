# Laudo: dry run LIDO do Cap.4 — metadiscurso encenado e registro acadêmico

- **Autor do laudo**: revisor1 · **Data**: 2026-08-24
- **Alvo**: `4-resultados-l0/texto.tex` na main `@7974563` (307 linhas)
- **Regra**: `docs/criterio-humanizacao.md`, seção "Metadiscurso: sóbrio sim, encenado não"
- **Natureza**: LAUDO. Nenhuma edição de `.tex`. Congelamento respeitado
  (capítulo de resultados: nenhum número tocado nem sugerido para mudança).

## Ponto de partida medido

`python3 scripts/checa-metadiscurso.py 4-resultados-l0/texto.tex` → **vazio, exit 0**.
O capítulo **passa no verificador**. Os achados abaixo são todos fora do alcance
do regex. Todas as reescritas sugeridas foram testadas e **passam** no próprio
`checa-metadiscurso.py`.

Cobertura: as cinco seções lidas. Seções sem achado declaradas.

## Comparação com o Cap.3

O Cap.4 é **sensivelmente mais limpo**: 11 achados em 307 linhas, contra 18 em
946. E o padrão dominante é **outro**. No Cap.3 era encenação estrutural nas
aberturas de seção; aqui é **registro de competição e de suspense** na discussão
dos resultados (§4.3), com o algoritmo genético tratado como adversário esportivo.

---

## 4.0 Abertura do capítulo

**B-01 · linha 10 · prioridade 2 (frase vazia)**
> "**Os resultados originais vêm do programa experimental da pesquisa.**"

Não informa nada: todos os resultados da tese vêm do programa experimental dela.
A frase parece ser resíduo de uma distinção que a frase seguinte já faz melhor
(original vs.\ reexecução).
**Sugestão**: suprimir, ou precisar: "Os resultados originais provêm da
implementação inicial do programa experimental."

**B-02 · linha 4 · prioridade 4 (âncora), severidade baixa**
> "Este capítulo apresenta os resultados dos **dois primeiros pilares**"

Âncora `pilar-N` em prosa. Diferente dos casos do Cap.3, aqui a função é
localizar (é o roteiro do capítulo), o que a regra admite. **Registro para
decisão do autor, sem sugestão de troca.**

## 4.1 Sensibilidade à composição e ao tamanho

**B-03 · linha 42 · prioridade 1 (direção do leitor), severidade baixa**
> "Três padrões **estruturam a leitura**:"

Instrui como ler em vez de afirmar o resultado.
**Sugestão**: "Os resultados mostram três padrões:".

**B-04 · linha 63 · prioridade 2 (figurativo), severidade baixa**
> "Lidos contra a literatura, esses padrões **ganham referência externa**."

**Sugestão**: "Esses padrões podem ser lidos contra a literatura."

**B-05 · linha 86 · prioridade 2 (registro de negócios)**
> "Construir $L_0$ deliberadamente, em vez de sorteá-lo, é portanto a
> **alavanca** disponível antes de existir qualquer rótulo."

"alavanca" é metáfora de gestão.
**Sugestão**: "é portanto o recurso disponível antes de existir qualquer rótulo."

**Registro positivo**: o fecho da seção ("O que esta seção mede é o custo dessa
arbitrariedade") é sóbrio e forte, e a comparação com \citet{Yu2023Patron} e
\citet{Griesshaber2020} é feita sem inflar o próprio resultado.

## 4.2 Limites por otimização evolutiva

**Nada encontrado.** É a seção mais limpa do capítulo, e vale como padrão: a
frase *"Separar por completo estrutura de deriva de busca exigiria um controle de
busca aleatória de mesmo orçamento, que não foi executado"* declara a limitação
sem drama e sem atenuar o achado. É exatamente o registro que a regra pede.

## 4.3 DRI-SL versus aleatório e envelope do AG

**B-06 · linha 140 · prioridade 1 (suspense: resultado como manchete)**
> "**Uma heurística que não consulta rótulo algum vence o otimizador que os
> consulta.** A Tabela~\ref{tab:drisl-vs-ag} compara..."

A seção abre com a conclusão em forma de manchete, antes de qualquer evidência,
e em registro de disputa ("vence"). Abrir pelo resultado é boa prática; o
problema é a **forma encenada**, não a ordem.
**Sugestão**: "Esta seção compara o DRI-SL com o envelope do AG." (o resultado
já é enunciado, com ênfase legítima, no parágrafo após a tabela: *"Este é o
resultado central da partida a frio: o DRI-SL supera não só a amostragem
aleatória média, mas o próprio melhor indivíduo encontrado pelo AG"*).

**B-07 · linha 179 · prioridade 2 (vocabulário narrativo)**
> "Esse **desfecho** confirma a expectativa mais bem estabelecida da literatura"

"desfecho" é vocabulário de enredo.
**Sugestão**: "Esse resultado confirma...".

**B-08 · linhas 194--198 · prioridade 1 e 2 — o achado mais forte do capítulo**
> "**A surpresa está no adversário** que a heurística supera. O AG não é um
> **competidor fraco**: otimiza a composição com acesso direto aos rótulos e à
> aptidão final, ao custo das 2.000 avaliações supervisionadas por cenário, e
> ainda assim **perde para** uma heurística que não consulta rótulo algum."

Acumula duas violações. **Encena surpresa para o leitor** (forma 2/3), e usa
**registro esportivo**: adversário, competidor fraco, perde para. O conteúdo
técnico (o AG é forte, tem acesso a rótulos, custa 2.000 avaliações, e mesmo
assim é superado) sobrevive inteiro sem a encenação.
**Sugestão**: "O AG otimiza a composição com acesso direto aos rótulos e à
aptidão final, ao custo das 2.000 avaliações supervisionadas por cenário, e
ainda assim fica atrás de uma heurística que não consulta rótulo algum."

**B-09 · linha 212 · prioridade 1 (revelação), severidade baixa**
> "Há, por fim, um efeito de variância **que as tabelas de média não mostram**."

Enquadra o achado como algo escondido das tabelas.
**Sugestão**: "A reexecução mede também um efeito de variância que as tabelas de
média não registram."

## 4.4 Reexecução independente e efeito da circularidade

**B-10 · linha 223 · prioridade 2, severidade muito baixa**
> "Os achados anteriores **sobrevivem** a uma reexecução independente"

"sobreviver a uma replicação" é uso corrente em texto científico. **Registro
apenas para completude; não recomendo mudar.**

**B-11 · linha 280 · prioridade 2 (adjetivo autoelogioso)**
> "**A reavaliação honesta**, porém, revela a inflação da circularidade."

Qualificar a própria reavaliação de "honesta" é autoelogio e, por contraste,
imputa desonestidade ao protocolo anterior, que foi apenas circular. O conteúdo
não precisa do adjetivo.
**Sugestão**: "A reavaliação em partição intocada quantifica a inflação da
circularidade."

**Registro positivo**: o restante de 4.4 é modelo de honestidade metodológica
(declara a grade reduzida, justifica-a, cita precedente publicado para a
redução, e conclui contra o próprio resultado anterior).

## 4.5 Síntese do capítulo

**Nada encontrado.** Enumeração sóbria ("O primeiro é... O segundo é...") e o
fecho não promete nada além do medido.

---

## Verificações que deram limpo (feitas, não presumidas)

- **Regra 3 (jargão definido na 1ª ocorrência)**: `conjunto-núcleo` (linha 185)
  **está** definido no Cap.2, com o inglês entre parênteses e a explicação junto.
  `envelope`, termo central deste capítulo, é introduzido no Cap.3. **Sem achado.**
- **Regra 4 (âncoras)**: **zero** identificadores `E*` no capítulo. Uma única
  ocorrência de `pilar-N`, na função de roteiro (B-02).
- **Congelamento**: nenhuma sugestão toca número, tabela ou veredito.

## Resumo por seção

| Seção | Achados |
|---|---|
| 4.0 abertura | B-01, B-02 (baixo) |
| 4.1 Sensibilidade | B-03, B-04, B-05 + registro positivo |
| 4.2 Otimização evolutiva | **nada encontrado** (seção-padrão) |
| 4.3 DRI-SL vs.\ AG | B-06, B-07, **B-08**, B-09 |
| 4.4 Reexecução | B-10 (não mudar), B-11 + registro positivo |
| 4.5 Síntese | **nada encontrado** |

**11 achados**, dos quais 3 de severidade baixa e 1 que recomendo **não** mudar.
O núcleo é a §4.3: quatro achados concentrados na discussão do resultado central,
todos do mesmo tipo — o texto encena uma disputa esportiva entre DRI-SL e AG.

## Proposta para `scripts/checa-metadiscurso.py`

```python
r"[Aa] surpresa (está|é|fica)",                              # B-08
r"\b(reavaliação|análise|leitura|medição) honesta\b",        # B-11
```

**Medido, não alegado**: rodei os dois padrões sobre os oito `.tex` de capítulo
da tese. **2 disparos, e os 2 são exatamente B-08 e B-11. Zero falso positivo.**

Os demais 9 achados **não** são capturáveis por regex, pela mesma razão do
Cap.3: o que fere a regra é o registro (competição, gestão, enredo) e a função
retórica, não um léxico fixo. "adversário", "competidor" e "alavanca" são
palavras legítimas em outros contextos, e um padrão para elas geraria falso
positivo em texto correto.
