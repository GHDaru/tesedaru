---
de: revisor2
para: principal
tipo: entrega
assunto: com o eixo na acurácia o piso cai de 35 mil para 30 mil — e os dois "95%" não são a mesma coisa
acao_esperada: insumo para o rascunho da banca das 4 superfícies, ANTES de ela escrever o número; e uma decisão do autor sobre qual leitura de "95%" a tese enuncia
referencia: decisão do autor 6feff50 (eixo = regime canônico, critério na métrica pré-registrada = ACURÁCIA) · artefatos `e3prime_{D,E35,E30,E25,E20,E}_s{7,42,123}.json` · minha entrega 20260820-2050 (que era no eixo do F1)
criada_em: 2026-08-21T15:50
---

## O número muda, e muda para melhor

Recompus os dois quadros no eixo novo. Régua populacional (braço D, regime
canônico, avaliação em 177.490, três sementes):

**D: acurácia 0,8675 ± 0,0021** · Macro F1 0,3684 ± 0,0091.
Critério 0,95 × acc(D) = **0,8241**.

| braço | acurácia média | dp | passa? | sementes que passam | Macro F1 | passava no eixo antigo? |
|---|---|---|---|---|---|---|
| D (régua) | 0,8675 | 0,0021 | — | — | 0,3684 | — |
| **E35** | **0,8610** | 0,0040 | **SIM** | **3/3** | 0,3520 | sim (2/3) |
| **E30** | **0,8439** | 0,0042 | **SIM** | **3/3** | 0,3233 | não |
| E25 | 0,8281 | 0,0046 | sim na média | **2/3** | 0,3061 | não |
| E20 | 0,7748 | 0,0068 | não | 0/3 | 0,2533 | não |
| E | 0,6966 | 0,0061 | não | 0/3 | 0,2016 | não |

**O piso da hipótese cai de 35 mil para 30 mil rótulos**, e cai com folga: no
eixo do F1 só o E35 cruzava, e cruzava em 2 de 3 sementes; no eixo da
acurácia o E30 cruza em **3 de 3**. O E25 cruza na média mas só em 2 de 3 —
é o mesmo tipo de fragilidade que segurou o gate ontem, e recomendo não
apoiar o veredito nele.

Isso corrige, no eixo novo, a minha própria entrega de ontem
(20260820-2050), que dizia "o piso vai de 25 mil para 35 mil". Aquilo valia
no eixo do Macro F1. Com o eixo na acurácia, o piso é 30 mil.

## A armadilha: os dois "95%" não são a mesma coisa

Isto precisa chegar à banca antes de ela redigir, porque a frase mais natural
de escrever é justamente a errada.

- **O "95%" do documento pré-registrado é ABSOLUTO.** Slide 33: "com 15000
  rótulos estabiliza a generalização **em 95%**". É acurácia de 95%, não 95%
  de coisa alguma.
- **O "0,95" da tese é uma RAZÃO.** O critério é 0,95 × desempenho da régua
  populacional.

No estudo de 2022/2023 as duas leituras provavelmente coincidiam, porque o
modelo populacional daquela base rondava os 95% de acurácia. **Na tese, não
coincidem.** A régua de hoje (braço D) tem acurácia **0,8675** — ou seja,
sob a leitura absoluta o critério de 95% seria **inatingível até pela própria
régua**. Só a leitura em razão funciona com os números atuais.

Logo: a tese **não pode** escrever "o critério pré-registrado de 95%" como se
fosse o mesmo 95% do documento. A formulação honesta é dizer que o critério
pré-registrado é *desempenho similar ao do modelo populacional*, e que a tese
o operacionaliza como 0,95 × régua — o que é uma escolha da tese, não uma
citação do documento.

## O que continua sem fonte

Fica o que já estava registrado: o gate de 85% do oráculo e as partições
atuais não têm fonte pré-registrada, e os totais de 2022/2023 (180k/120k/60k)
não são os de hoje. E o "15%" do slide 38 segue sem denominador declarado —
15.000 ÷ 120.000 dá 12,5%, e o único par que dá 15% exatos é 18.000 ÷
120.000, com 18.000 ausente do deck.

## O que NÃO fiz

Não editei nenhuma das 4 superfícies de veredito — a reescrita única é da
banca, e eu sou o verificador dela. Não escolhi entre as leituras de "95%":
é decisão do autor. Entreguei os quadros prontos, como da outra vez, para
ele decidir vendo tabela e não amostra.
