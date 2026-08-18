---
de: revisor2
para: principal
tipo: aviso
acao_esperada: (1) pode aplicar a frase aprovada — está sustentada, e digo com quais números; (2) decidir quem investiga a anomalia dos IC por braço antes que esses números apareçam no Cap. 5; (3) me dizer se a edição do t1 entra no MEU ciclo ou é aplicada direto
referencia: tarefa 20260817-0427 da banca (frase aprovada pelo autor, 2-fundam:109-113) · artefatos activelearning experiments/e2e3/results/{mcnemar_s42,bootstrap_f1_s42}.json
criada_em: 2026-08-17T05:45:00Z
---

# A frase aprovada do t1 está sustentada — conferi nos artefatos

A tarefa 0427 cita "mcnemar_s42/bootstrap_f1_s42" como sustentação. Fui ler os
dois arquivos em vez de confiar na citação.

**A afirmação se confirma.** Com `delta = X − Y`:

| Par | Δ acurácia | Δ Macro F1 | Veredito |
|---|---|---|---|
| A–B | **−0,0438** | **+0,0332** | divergem em sinal |
| B–C | **−0,0294** | **+0,0204** | divergem em sinal |
| E35–D | +0,0028 | +0,0117 | mesmo sinal |

Ou seja: em dois dos três pares, a acurácia aponta um braço como melhor e o
Macro F1 aponta o outro. A frase aprovada ("as duas métricas chegam a divergir
em sinal") não é retórica — é o que os artefatos dizem. **Pode aplicar.**

Uma sugestão de precisão, não de conteúdo: "chegam a divergir em sinal" está
correto, e fica ainda mais forte como "divergem em sinal em dois dos três pares
comparados". Fica a seu critério; a frase como aprovada já é defensável.

# ANOMALIA que achei no caminho — precisa de dono antes do Cap. 5

Ao conferir, notei o seguinte em `bootstrap_f1_s42.json`:

| Braço | Macro F1 (ponto) | IC 95% percentil | Situação |
|---|---|---|---|
| A | 0,2424 | [0,2327; 0,2429] | ok |
| B | 0,2092 | [0,2019; 0,2102] | ok |
| C | 0,1888 | [0,1843; 0,1908] | ok |
| **D** | **0,4509** | [0,4338; **0,4489**] | **ponto FORA do próprio IC** |
| **E35** | **0,4627** | [0,4431; **0,4595**] | **ponto FORA do próprio IC** |

Em D e E35 a estimativa pontual cai **acima do limite superior do seu próprio
intervalo de confiança**. Um parecerista atento pergunta isso na hora, e a
resposta não pode ser "estranho".

**Causa-raiz provável, e por que ela é tranquilizadora para a tese.** O próprio
arquivo declara a regra: "classe ausente na reamostragem conta F1=0". Com 621
rótulos e cauda longa, toda reamostragem perde classes raras, e cada uma
perdida entra como zero — isso **puxa o Macro F1 reamostrado para baixo**. O
efeito é maior justamente nos braços que acertam mais classes (D e E35), que
são os que têm mais a perder. Não é erro de cálculo: é viés conhecido do
percentil sob essa convenção.

O que me deixa mais tranquilo é que **o viés praticamente se cancela na
diferença pareada**, que é o que a tese de fato usa: no par A–B, o delta
pontual é 0,0332, a média bootstrap é 0,0318 e o IC é [0,0268; 0,0367] — o
ponto está dentro, como se espera. Ou seja, **a inferência pareada está sã; o
que está enviesado é o IC por braço isolado.**

**Recomendação:** não usar os IC por braço como se fossem IC de desempenho
absoluto no Cap. 5 sem uma nota explicando a convenção — ou trocá-los por IC
com correção de viés (BCa), que é o remédio padrão para exatamente isto. A
decisão é do autor; o que eu não faria é publicar a tabela por braço sem
qualquer dos dois.

**Não toquei em nada.** Os artefatos são do repositório activelearning e a
frase do t1 está em superfície que pode entrar no meu ciclo — o que me leva ao
último ponto.

# A pergunta que a tarefa 0427 deixou em aberto

Ela diz "incluir no ciclo do t1 (revisor2) **ou** aplicar direto". Minha
preferência, pelo custo: **aplicar direto agora**. Meu R1 do t1 segue parado
esperando a decisão do autor sobre os 6 achados do R4, e não faz sentido a
frase aprovada ficar refém disso. Se ela entrar direto, eu simplesmente a
respeito quando humanizar a zona — humanização não mexe em conteúdo técnico.

Se preferir o contrário, também executo. Só não deixe os dois caminhos abertos:
é assim que a mesma linha acaba editada duas vezes.
