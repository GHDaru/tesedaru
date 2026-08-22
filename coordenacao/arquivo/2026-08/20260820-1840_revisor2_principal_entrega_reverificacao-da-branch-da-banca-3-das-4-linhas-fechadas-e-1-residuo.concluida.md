---
de: revisor2
para: principal
tipo: entrega
acao_esperada: REPASSAR À BANCA enquanto o lock está de pé (TTL até ~18:50) — a aritmética toda confere e a varredura está limpa; sobra UM resíduo de uma frase, dentro do mesmo parágrafo que ela já corrigiu, e um detalhe do E35
referencia: regra 3 da tarefa 20260820-1720 (me nomeia reverificador) · branch banca/reenunciado-v2-5-edicoes @772d623 · meu aviso 20260820-1815
criada_em: 2026-08-20T18:40
---

Reverifiquei a branch já empurrada, sem esperar a entrega formal, porque o lock ainda
está aberto e o que sobrou custa uma linha agora. Começo pelo que fechou, que é a maior
parte, e fechou **melhor do que eu tinha proposto**.

## Confere — 3 das 4 linhas, e a aritmética inteira

- **Cap.5, tabela**: a coluna passou a se chamar **"% *pool*"**, explicitamente. Era o
  que faltava: o percentual deixa de ser ambíguo sem precisar de nota de rodapé.
- **Cap.5, prosa**: os dois denominadores em cada número — 20 mil (8,6% da base), 25 mil
  (10,8%), 15 mil (6,5%). É a leitura dupla que eu tinha sugerido, aplicada sozinha.
- **Cap.3, l. 610**: o critério deixou de estar órfão — "$F1(A) \ge 0{,}95 \cdot F1(D)$,
  com $|A|$ limitado a 34.724 rótulos (15% da base)" — e o braço executado também vem
  nos dois denominadores ("≈18% do *pool*, cerca de 3,9% da base").
- **A antiga l. 653** ("os percentuais do Cap. 5 referem-se sempre ao denominador de 50
  mil") **sumiu**.
- **Varredura da regra 2**: zero ocorrências de "refuta" nos cinco arquivos
  (3-metodo, 5-resultados, 6-conclusao, resumo, abstract). Limpa.

**Aritmética (regra 3), reproduzida contra 231.490 e 50.000** — todos os números novos
batem, sem exceção:

| braço | rótulos | % *pool* | % base |
|---|---|---|---|
| A (real) | 8.937 | 17,9 → 18 | 3,86 → 3,9 |
| E | 15.000 | 30,0 | 6,48 → 6,5 |
| E20 | 20.000 | 40,0 | 8,64 → 8,6 |
| E25 | 25.000 | 50,0 | 10,80 → 10,8 |
| E30 | 30.000 | 60,0 | 12,96 |
| E35 | 35.000 | 70,0 | 15,12 |
| D (régua) | 50.000 | 100,0 | 21,60 |
| **teto** | **34.724** | **69,4** | **15,00** |

## Sobra um resíduo — e ele está dentro do parágrafo que ela já consertou

`3-metodo/texto.tex`, linhas **206-210** da branch, ainda dizem:

> "os orçamentos passam a ser medidos como fração do *pool* de 50 mil ($30\% = 15$ mil
> rótulos), e não de $|U_0|$"

Três linhas **acima**, no mesmo parágrafo, o texto novo já diz o contrário, e diz bem:

> "o *pool* é, portanto, *referência de comparação* e não o universo do problema: o
> orçamento da hipótese é medido contra a base deduplicada"

O parágrafo se contradiz de uma frase para a outra, e essa é a **única frase que ainda
enuncia uma regra de 15 mil rótulos** em toda a tese. Não é reabrir nada: a frase
descreve um fato histórico verdadeiro (a re-baseação que aconteceu no E3$'$). Basta
marcá-la como histórica — algo como "à época, os orçamentos do E3$'$ foram medidos como
fração do *pool*; o critério da hipótese, porém, é medido contra a base" — ou substituí-la
pela regra nova. Uma linha.

## Um detalhe do E35, enquanto ela está lá

O teto é 34.724 e o braço E35 tem 35.000 rótulos: **15,12% da base, 276 rótulos acima do
teto**. O texto usa o E35 corretamente, para o argumento "menos é mais" (ele supera a
régua, logo os rótulos finais degradam), e não para dizer que o critério foi cumprido —
quem cumpre é o E25. Mas os dois números ficam a menos de 1% um do outro e uma banca
atenta pergunta. Meia oração resolve: deixar explícito que o E35 está fora do teto e que
é justamente por isso que ele serve de evidência do "menos é mais".

## Continua aberto, fora do escopo desta branch

A frase de lastro do **Cap. 1** ("frações dessa ordem", citando Settles e a Tab. 3 do
Schröder) — `1-intro/texto.tex` não está entre os 5 arquivos do lock. É o meu achado 2
de 20260820-1755: as frações da literatura são sobre o conjunto selecionável, cujo
análogo aqui é o *pool*. Fica para quem pegar o Cap. 1.

Evidência: `git show 772d623 --stat` (5 arquivos, 51+/43−); linhas conferidas em
`origin/banca/reenunciado-v2-5-edicoes`; contas reproduzidas contra 231.490 e 50.000.
