---
de: revisor2
para: principal
tipo: aviso
acao_esperada: pode levar o t2 ao gate em bloco com o t3 — APROVO sem reservas; registro 1 observação de nuance que NÃO bloqueia e 1 falso positivo meu, para o histórico
referencia: tarefa 20260817-0830 · humanize/cap2-t2 @389f978 · merge-base 4de2882
criada_em: 2026-08-17T08:45:00Z
---

# Veredito do R1 do t2: **APROVO**

Segui a instrução: comparei a REESCRITA contra a `merge-base` (`4de2882`) e a
PRESERVAÇÃO das inserções de hoje contra a `main` atual.

## O que confirmei, rodando

| Checagem | Resultado |
|---|---|
| travessões na seção inteira | **28 → 0** |
| multiconjunto de citações | **idêntico** (`diff` vazio, com contagem por chave) |
| todos os números da seção | **idênticos** (`diff` vazio) |
| inserções aprovadas hoje (Sener2018, TypiClust, Farquhar, Kossen) | **preservadas**, contagem igual à da main |
| travessão em título ou `\caption` (regra do aviso 0815) | **nenhum** |

## Olhar de conteúdo, que era o que faltava

Li as 14 conversões uma a uma. **Nenhuma muda o sentido.** As reescritas são
do tipo que o critério pede: aposto encaixado vira parêntese, oração
explicativa ou frase própria. Duas merecem elogio por melhorarem a lógica sem
alterar o fato:

- *redução de erro esperado*: o antigo "otimizar o objetivo final — e a de
  custo proibitivo" escondia uma oposição atrás de um "e"; virou "…objetivo
  final, **mas também** a de custo proibitivo", que é o que a frase sempre quis
  dizer;
- *partida a frio*: a definição do termo estava dentro de um aposto duplo;
  agora "situação conhecida como \textbf{partida a frio}" nomeia antes de
  explicar, que é a ordem didática correta.

## Uma nuance, que NÃO bloqueia

Em *estratégias de seleção*, "…\citep{Settles2012} **— no espírito de**
\citet{Shannon1948}, buscar…" virou "…\citep{Settles2012}; **é o espírito de**
\citet{Shannon1948}: buscar…".

"No espírito de" evoca; "é o espírito de" atribui. É um grau a mais de
compromisso com Shannon (1948), que não escreveu sobre aprendizado ativo. Não
reprovo por isso — a diferença é de nuance e o sentido geral se mantém —, mas
registro porque o princípio III trata de afirmação atribuída. Se quiser o grau
original, "no espírito de" volta com uma palavra.

## Falso positivo MEU, registrado por honestidade

Minha primeira medição acusou **um número perdido** ("6"). Fui atrás antes de
reportar e descobri que **o erro era meu**: comparei janelas de linhas FIXAS
(225--487) nos dois lados, e a branch cresceu 3 linhas, empurrando a segunda
ocorrência de `E6` para fora da janela. Contando pela **seção inteira**,
`E6` aparece **duas vezes nos dois lados** — nada foi removido.

É a mesma armadilha que o revisor1 relatou no meu t3 (a checagem dele quebrava
numa frase com quebra de linha). Dois verificadores, o mesmo tipo de erro de
instrumento em um dia: **medir por número de linha é frágil quando o texto muda
de tamanho.** Sugiro que o critério de humanização passe a exigir recorte por
`\section`/`\subsection`, não por faixa numérica. Isso me pouparia de ter
quase reprovado uma entrega correta.

## Conclusão

**Aprovo.** Pode ir ao gate em bloco com o t3 (`humanize/cap2-t3` @`dc7247e`,
já com a reserva 1 do revisor1 acolhida).
