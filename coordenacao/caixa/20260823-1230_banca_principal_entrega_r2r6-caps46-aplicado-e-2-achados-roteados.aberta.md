---
de: banca
para: principal
tipo: entrega
acao_esperada: frente 2 da tarefa 1045 entregue — `banca/lote-caps46-r2r6` @0b25fc7 (R2/R6 dos Caps. 4 e 6, 9 itens aplicados, zero numeros). Despachar: (1) cruzada do revisor2 desta branch (pode ir junto com a de resumo/abstract @31fb778, que tambem aguarda); (2) DOIS achados que nao apliquei por serem fato, nao estilo — precisam de verificacao/decisao antes do texto mudar.
referencia: tarefa 1045 (frente 2) · branch banca/lote-caps46-r2r6 @0b25fc7 · Cap.6 l.146-148 e l.30/201
criada_em: 2026-08-23T12:30:00Z
---

# R2/R6 dos Caps. 4 e 6 — auditado e aplicado

**Aplicados** (@0b25fc7, 2 arquivos, +19/-16, nenhum numero alterado):

- **Cap. 4**: AG aberto por extenso na 1a ocorrencia (l.11, que vinha antes
  do extenso da l.86); "cold start" unificado em "partida a frio", com o
  ingles preservado so na glosa da 1a ocorrencia (prosa, parentese da l.79 e
  legenda da tab:drisl-vs-ag); cabecalho da tabela "Acc" -> "Acuracia",
  casando com as demais tabelas da tese.
- **Cap. 6**: "literatura classica de AL" -> "de aprendizado ativo" (era a
  ULTIMA ocorrencia de AL em capitulo, a decisao AA do autor fecha aqui);
  LLM, LCE e ALC abertos por extenso na 1a ocorrencia do capitulo (mesma
  convencao aplicada no Cap.5 e mantida pelo autor); "a avaliacao feita
  sobre os proprios dados" ganhou o nome unificado "autoavaliacao"
  espelhando o Cap.5; "Fase Inicial" (variante que so existia ali) ->
  "Fase~1 (o LLM Inicial)"; "cold start" -> "partida a frio" (sintese e
  contribuicoes).

**Sem acao, registrado**: PVBin/BERT sem reabertura no Cap.4 (ha remissao ao
Cap.3 na mesma frase); "Acuracia Global e Macro F1" do Cap.4 l.26 e
contraste intencional global-vs-macro; RQ3/RQ4 no Cap.6 sao jargao
operacional permitido pos-Cap.3 (principio VII).

# Dois achados roteados — fato, nao estilo; nao editei

1. **Cap. 6, Limitacoes (l.146-148)**: "a validacao com o classificador
   forte executada em configuracao uniforme mas economica (3 epocas,
   contexto de 32 tokens, **semente unica, CPU**)". Contradiz o regime final
   em dois pontos: a validacao tem TRES sementes (Cap.5, resumo, abstract —
   todos ja dizem tres), e o Cap.3 declara ambiente de treinamento com GPU
   RTX 3090. E o mesmo tipo de sobra que o autor mandou remover do resumo.
   Peca ao revisor2 a lista correta da configuracao (epocas, contexto,
   lote, sementes, hardware) contra o artefato `_bs16v2`; com ela eu aplico
   em uma edicao. Nao troquei por conta propria para nao inventar o
   hardware.
2. **Cap. 6, faixas vizinhas**: l.30 diz "77--83\%" (plato dos 4 melhores,
   espelhado no resumo) e l.201 diz "78--83\%" (na conclusao, "pagar bem").
   Se a segunda se refere aos oraculos da configuracao final
   (flash 78,3 / pro 82,6), basta qualifica-la; se e o plato, harmonizar em
   77--83. Decisao de leitura do autor; qualquer das duas eu aplico.

# Fila da banca apos esta entrega

Nada em execucao aguardando so a mim. Em aberto com outros: arco do braco E
(executor02) — fecho o lote do Cap.5 e sinalizo a cruzada final no instante
em que o valor chegar; cruzadas do revisor2 (lote-cap5 ja APROVADA as 1200;
resumo/abstract @31fb778 e caps46 @0b25fc7 na fila dele); R4/R3/R5 dos Caps.
4/6 e apendices (revisor1/revisor2, tarefas 1045 deles) — quando chegarem,
consolido no mesmo padrao. Caixa: 1045 em-andamento com dois registros;
minhas ativas 7 de 10.
