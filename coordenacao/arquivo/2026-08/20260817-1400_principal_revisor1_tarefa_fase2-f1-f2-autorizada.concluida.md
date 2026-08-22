---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: FASE 2 AUTORIZADA pelo autor nos três pontos — (a) mantém os DOIS capítulos de resultados, contra fundir; (b) expurgo aprovado com a política "labels ficam"; (c) começar por F1+F2. Executar em branch própria, verificação cruzada do revisor2, gate do principal por fatia
referencia: sua Fase 1 (docs/plano-refatoracao-resultados.md) · aprovação do autor 2026-08-17 · exceção nominal de superfície já concedida na tarefa 1240
criada_em: 2026-08-17T14:00:00Z
---

# Fase 2 liberada: F1 (tabela-mapa) + F2 (os sete títulos)

O autor aprovou sua recomendação inteira, incluindo a decisão que zera o
custo de remissões (nenhum `\label` renomeado). Registro as três aprovações:

**(a) DOIS capítulos, sem fundir.** Seu argumento venceu: a assimetria não é
o problema, a falta de interlocução é — e fundir esconderia o defeito das
zero citações do Cap. 4 em vez de corrigi-lo. A F6 (reforço do Cap. 4) fica
como tarefa separada, para depois.

**(b) Expurgo aprovado**, com a classificação da sua Fase 1: 105 saem, 26
migram para a tabela-mapa, 60 ficam (labels/refs e caminhos de artefato).

**(c) F1 + F2 primeiro**, exatamente pelo motivo que você deu: o autor quer
julgar o TOM dos sete títulos antes de investir nas fatias grandes.

## Como entregar

- F1 e F2 podem vir na MESMA branch, mas em commits separados — se o autor
  quiser aprovar a tabela-mapa e pedir outro tom nos títulos, eu separo.
- Na conclusão, traga os **sete títulos em antes/depois numa tabela**, que é
  o que o autor vai ler para decidir. Sua proposta de tom da Fase 1 serve de
  partida; refine se achar melhor.
- DoD executável, como você propôs: multiconjunto de labels e refs idêntico
  antes/depois (comparação de conjuntos, não juízo), zero código E nos
  títulos, e o build do PDF verde (a regra do travessão em título vale para
  os títulos novos — seu próprio check-travessao-titulo.py é o guarda).
- Verificação cruzada do revisor2 antes do gate; ele está no t1, então
  combine a janela com ele por mim se houver colisão de superfície.

Após o gate de F1+F2, seguimos com F3/F4/F5 na ordem que você propôs.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
