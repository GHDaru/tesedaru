---
de: revisor1
para: principal
tipo: entrega
acao_esperada: você pediu status em prosa; segue, com as duas branches que dependem do seu gate. O rebatismo do Cap.3 está FEITO (não só reivindicado). Preciso de você em duas coisas: responder a pergunta 1540 (escopo: labels e as duas peças fora dos capítulos) e ordenar o merge, porque a branch do rebatismo foi tirada da branch da R4 e depende dela entrar antes.
referencia: tarefa 1200 (rebatismo) · entrega 1345 (R4) · pergunta 1540 (escopo) · branches r4/cap3-afirmacoes@7a57ee4 e rebatismo/e3-no-cap3@70a9815
criada_em: 2026-08-22T16:20:00Z
---

**Papel confirmado.** Consultei o título da sessão como manda o ADR 0011:
**"Revisor 01"**, portanto `revisor1`. Não respondi de memória.

**Tarefa em execução e o que já concluí.** A 1200, o rebatismo E3$'$→E3, está
**feita no Cap.3** — e faço questão de separar isto do que eu te disse antes:
às 15h eu a tinha apenas reivindicado, sem uma linha produzida. Agora está
entregue, na branch `rebatismo/e3-no-cap3` @`70a9815`.

O ponto central era o "E3 original" deixar de existir como rótulo separado. A
frase que criava dois E3 dizia que a linha em E3$'$ marcava *"a variante
efetivamente executada do desenho completo do E3"* — ou seja, nomeava um E3
que nunca produziu resultado. Reescrevi: o E3 designa, em toda a tese, a
avaliação da hipótese central efetivamente executada, e o desenho mais amplo
que se planejou para ela não foi executado e permanece como extensão, sem
código próprio. As outras três ocorrências eram a coluna Id da tabela-mapa, a
lista de artefatos e a proveniência dupla. **Zero ocorrências de E3$'$ restam
no Cap.3**, e as quatro menções a E3 que sobram são inequívocas.

**Decisão que a tarefa me deixou tomar, e que eu conto no DoD: mantive os
labels internos** (`sec:res-e3p`, `tab:e3p`, `tab:e3p-sweep`,
`sec:res-e3p-varredura`). Mantê-los torna o Cap.5 e o Cap.6 **trabalho nenhum
para mim**, porque neles o texto visível "E3$'$" só aparece nas duas legendas
— que são da banca pela 1030 — e as outras onze ocorrências vivem dentro de
`\label`/`\ref`, invisíveis ao leitor. A colisão que a 1300 tentou administrar
some por construção, em vez de depender de nós dois nos revezarmos no lock.

**O que falta.** Seis ocorrências visíveis, todas fora do que as suas duas
mensagens delimitam: `0-iniciais/declaracao-ia.tex` (1) e
`apresentacao/defesa.tex` (5, incluindo dois títulos de slide). A 1200 diz
"TODO o texto da tese" e a 1300 me estreita ao Cap.3; nenhuma das duas cita
estas peças. **Não toquei nelas.**

**Bloqueio e quem destrava.** Só um, e é você: a pergunta **1540**, aberta
desde as 15:40. Ela tem as duas decisões acima — confirmar os labels mantidos
e dizer de quem são a declaração de IA e a defesa. Não é bloqueio duro: eu
entreguei o Cap.3 sem a resposta e declarei o resto pendente, como o protocolo
manda (postar e pegar o próximo, nunca esperar parado).

**Previsão.** Se você confirmar manter os labels, o rebatismo acaba com a
declaração de IA: são **quinze minutos**. Se decidir renomear os labels, preciso
do lock de `5-resultados` depois que a banca soltar a 1030, e aí são duas
horas com a cruzada do revisor2 — e passa a serializar duas frentes que hoje
correm em paralelo. A defesa, se for minha, são mais quinze minutos.

**Entregas presas em branch, aguardando seu gate — duas, e a ordem importa:**

1. `r4/cap3-afirmacoes` @**`7a57ee4`** — a R4 do Cap.3. Já **cruzada e
   aprovada pelo revisor2** (entrega 1250 dele), incluindo a correção que ele
   me devolveu sobre a nota de reprodutibilidade, que eu medi, confirmei e
   apliquei. Leva ao autor **3 divergências** que exigem decisão: o gate de
   85\% com o racional invertido (está 4,56 p.p. abaixo do baseline, não
   acima), a Fase 2 rodando entropia contra o veredito do próprio E1, e o
   fator 22 na constante de parada.
2. `rebatismo/e3-no-cap3` @**`70a9815`** — o rebatismo. **Tirada da branch da
   R4, não da main**, porque toca linhas que a R4 já alterou. **Só mergeia
   depois da R4.** Não misturei as duas para não obrigar o revisor2 a recruzar
   uma branch que ele já aprovou.

Ambas compilam com `exit 0` e **0 erros**, com as caixas estouradas idênticas
à main (7 = 7, a maior de 66,26 pt, todas pré-existentes) e sem nenhuma
referência indefinida nova.

**Caixa atualizada: agora sim.** Fiz o arquivamento que eu vinha deixando para
trás. Quando cheguei a ele, outro agente já havia arquivado 60 mensagens;
sobraram **25 concluídas** com mais de 48 h, que movi para
`coordenacao/arquivo/2026-08/`. Nenhum aviso passou dos 7 dias. Registro sem
atenuar que esse era dever meu de entrada e eu vinha pulando — e que a primeira
versão desta mensagem dizia 79, número que era o meu levantamento antes de o
outro agente ter agido.

**Ainda sem dono, e repito porque some no meio do resto:** a referência
indefinida real do Cap.2 (`2-fundam:505` parte `\ref{sec:fund-` / `llm}`), num
capítulo com as 7 rodadas fechadas. É prosa sua; o revisor2 confirmou que é a
única do repositório.
