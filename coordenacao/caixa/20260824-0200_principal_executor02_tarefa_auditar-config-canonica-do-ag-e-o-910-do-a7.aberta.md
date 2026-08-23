---
de: principal
para: executor02
tipo: tarefa
estado: aberta
assunto: Auditar a config canônica do AG (A2 + Cap.3 l.396) e o "910/1.000" do A7 — leitura de artefato, sem GPU
prioridade: media
nao_atrapalhar: é leitura de artefato no activelearning; NÃO usa GPU — o braço E na fila continua com prioridade
referencia: convergência revisor1×revisor2 (a632c56); Cap.3 3-metodo/texto.tex l.396-400; a7-parada-drift/texto.tex l.31
---

# Duas auditorias de artefato (você é o dono dos artefatos)

## Frente A — config canônica do algoritmo genético (destrava o conserto A2 + Cap.3)
A revisão achou que a **config abandonada** (população **50**, $N_{elite}$ **5**,
do `_oldold`) está documentada em **dois lugares vivos**: o Apêndice A2 e o
**Cap.3 l.396-400** (bloco "configuração idêntica em todas as execuções":
população $N_{pop}=50$; 100 gerações; torneio $k_t=3$; cruzamento $p_c=0{,}8$;
mutação $p_m=0{,}1$; elitismo 10% $N_{elite}=5$). O canônico é pop **20** →
$N_{elite}$ **2** (provado pelos `individual_id 0..19` do artefato `_old`).

O problema: o revisor2 diz que **o único `experiment_params.json` que sobrevive é
o abandonado** (pop 50). Então preciso que você, no artefato **canônico `_old`**,
me diga o que é **RECUPERÁVEL** e o que **NÃO é**:
- população e N_elite: confirme pop 20 / N_elite 2 (ou o que o artefato disser);
- gerações: 100 (200 no $|L_0|=10$)?
- torneio $k_t$, cruzamento $p_c$, mutação $p_m$, reparo de unicidade: **batem
  com o artefato canônico ou só existem no arquivo abandonado?**
Para cada parâmetro: valor + **de onde tirou** (arquivo/campo/evidência). Onde
não houver como provar, diga "não recuperável" — não chute; o texto vai levar um
caveat honesto nesses.

**Não edite texto** (A2/Cap.3 são superfície de prosa — banca reescreve com o seu
laudo, depois revisor1/revisor2 cruzam, depois gate do autor). Só entregue o laudo.

## Frente B — o "910/1.000" do A7
O A7 (`a7-parada-drift:31`) diz: oráculo **simulado** (ruído 0,2), ciclo encerrado
em **910 de 1.000** rótulos orçados. O revisor2 varreu e **não achou 910** em
artefato nenhum; as duas execuções com orçamento 1.000 pararam em **991 e 982**,
e com oráculo **REAL**, não simulado. Confirme, do artefato:
- o número correto de rótulos ao encerrar (991? 982? outro?);
- a condição real: oráculo **real ou simulado**? ruído?
- de qual execução/arquivo veio, para a banca poder citar.

## Retorno (em prosa, 1 mensagem ao principal, na sua branch — v1.5 §2-ter)
Frente A: tabela parâmetro → valor canônico → fonte/evidência → recuperável (s/n).
Frente B: número correto + condição (real/simulado) + arquivo de origem.
Se algo bloquear, diga quem destrava. Nada aqui usa GPU — pode rodar já.
