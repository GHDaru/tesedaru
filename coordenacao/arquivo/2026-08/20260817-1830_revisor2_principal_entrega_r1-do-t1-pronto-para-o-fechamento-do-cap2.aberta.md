---
de: revisor2
para: principal
tipo: entrega
acao_esperada: meu único item do fechamento do Cap. 2 está PRONTO — R1 do t1 na branch humanize/cap2-t1 @3ac3029, medido contra a main de agora. Uma decisão de uma linha para o autor (o travessão dele) e dois achados que entrego ao R2 da banca
referencia: sua tarefa 20260817-1725 (prioridade máxima) · régua nova do aviso 1700 · pacote 0815 aplicado em 03d88d5
criada_em: 2026-08-17T18:30:00Z
---

O R1 do t1 está pronto, e é menor do que era: o pacote de inferência do autor
(`03d88d5`) reescreveu os 4 parágrafos onde viviam 8 das minhas 9 conversões, e
esse texto é **aprovado e intocável**. O que sobra, medido no merge contra a main
de agora:

| Critério | main | **merge** |
|---|---|---|
| travessões `—` na §2.1 | 3 | **1** |
| chaves de citação na §2.1 | 32 | **32, idêntico** |
| dígitos na §2.1 (proxy de números) | 269 | **269, idêntico** |
| zona aprovada do pacote 0815 | — | **byte a byte idêntica** |
| travessão em título ou legenda | — | **nenhum** |
| estrangeirismos sem itálico (régua nova) | — | **nenhum na §2.1** |

O único travessão que resta é **o do autor**, criado por ele no `e778bda`:
"desempenho agregado) — separação que é operacional…". Não é meu para converter.
Se ele quiser zerar, **tem de ser vírgula, não dois-pontos** — a frase dele já usa
dois-pontos oito palavras depois.

## O que NÃO toquei, e por quê

Medi 11 frases longas na §2.1. **Nenhuma é candidata legítima do R1**, e a razão
importa mais que o número:

- **seis estão dentro do pacote 0815** (as fórmulas de Wilson, McNemar, Wilcoxon
  e bootstrap). São longas porque carregam equação em display — quebrar ali seria
  reescrever texto que o autor aprovou verbatim;
- **três são enumerações** — "(i) hold-out… (ii) validação cruzada… (iii)… (iv)"
  —, e a enumeração já **é** a des-densificação; quebrá-las piora;
- **duas são do parágrafo das métricas** que o autor reescreveu no `e778bda`.

Ou seja: a faixa do t1 chegou ao ponto em que **humanizar mais seria desfazer
decisão de autor**. Digo isso explicitamente para o gate não interpretar o número
baixo como trabalho pela metade.

## Dois achados que entrego ao R2 (siglas), da banca

Medi de passagem, e são da rodada dela, não da minha:

1. **`LLM` aparece sem expansão na §2.1** (l. 121, "oráculos LLM"). Não é defeito:
   o Cap. 1 introduz corretamente em `1-intro:65` ("modelos de linguagem de grande
   porte (LLMs, de \textit{large language models})"). Fica a decisão de convenção
   — reexpandir por capítulo ou confiar na lista de siglas.
2. **`IC` aparece sem a forma "(IC)"** na §2.1 (l. 176, "IC de Wilson a 95\%"). O
   termo está definido em português no mesmo parágrafo ("Um intervalo de confiança
   de 95\%"), mas a sigla nunca é apresentada formalmente. **Está dentro da zona
   aprovada do 0815** — quem mexer ali precisa do autor.

## Estado do meu lado do fechamento

`humanize/cap2-t1` @`3ac3029` merge **limpo** na main. Entrego para o gate e para
a verificação cruzada do revisor1, como você dividiu. Sigo disponível para a
minha metade da cruzada (t4 e t5) assim que ele publicar.

## Resultado (principal)
Entrega processada e integrada; arquivada na limpeza.
