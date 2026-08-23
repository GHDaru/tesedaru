---
de: principal
para: banca
tipo: tarefa
acao_esperada: DUAS frentes novas, em sequencia apos fechar o lote do Cap.5 (prioridade): (1) RECONSTRUIR resumo e abstract com o veredito final (o "sera refeito" do autor); (2) varredura R2 (siglas) + R6 (terminologia) dos Caps 4 e 6, modo auditoria, voce consolida. Ordem: Cap.5 -> resumo/abstract -> R2/R6 caps 4/6.
referencia: decisao do autor 2026-08-23 (fazer tudo em paralelo) · veredito final (regime lote16, criterio em acuracia, atingido dentro do teto) · resumo/abstract atuais ja com item (v) novo mas a refazer por inteiro
criada_em: 2026-08-23T10:45:00Z
---

1. **Resumo/abstract**: reescreva os dois (espelhos PT/EN) com o veredito
   final consolidado — criterio em acuracia (pre-registro, qualificacao
   jun/2023) atingido dentro do teto (piso 30k em F1, 20k em acuracia),
   E35 supera na media (2 de 3 sementes, heterogeneidade declarada), a
   limitacao de "semente unica" ja removida. Sem numero provisorio: use os
   finais que ja estao na main. Cruzada do revisor2.
2. **R2/R6 Caps 4 e 6**: siglas (1a ocorrencia com extenso) e terminologia
   consistente; modo auditoria + consolidacao, como no Cap.5. Nenhum numero
   muda em R2/R6.

## Andamento (banca, 2026-08-23)

Frente 1 ENTREGUE: `banca/resumo-abstract-reconstruidos` @31fb778 — resumo e
abstract reescritos por inteiro com o veredito final (criterio em acuracia
atingido dentro do teto: 20 mil 3/3; F1 em 30 mil 3/3; E35 na media com
heterogeneidade declarada; executada parou em 11.936/5,2%). Mesmos numeros da
main, zero provisorio; pares de travessao removidos; "autoavaliacao"
espelhando o Cap.5; PT/EN simetricos. Aguarda cruzada do revisor2.
Frente 2 (R2/R6 Caps 4 e 6): proxima, em modo auditoria; previsao 1 ciclo.

## Andamento 2 (banca, 2026-08-23)

Frente 2 (R2/R6 Caps 4 e 6): auditoria FEITA e itens claros APLICADOS em
`banca/lote-caps46-r2r6` @0b25fc7 (2 arquivos, +19/-16, zero numeros).
Aplicados 9: Cap.4 — AG com extenso na 1a ocorrencia (l.11), "cold start"
unificado em "partida a frio" com o ingles so na glosa inicial (prosa e
legenda da tab:drisl-vs-ag), cabecalho "Acc"->"Acuracia"; Cap.6 — AL (l.77)
-> "aprendizado ativo" (ultima sobrevivente da decisao AA), LLM/LCE/ALC com
extenso na 1a ocorrencia do capitulo, "autoavaliacao" espelhando o Cap.5
(l.104), "Fase Inicial" -> "Fase 1 (o LLM Inicial)" (l.189), "cold start"
unificado (l.18 e l.120). DOIS achados FICAM DE FORA por exigirem
verificacao/decisao, roteados na entrega 1230: (a) Cap.6 l.146-148 diz
"semente unica, CPU" na validacao com classificador forte — contradiz as
tres sementes do regime final e o ambiente declarado no Cap.3 (GPU RTX
3090); e fato, nao estilo: revisor2 confirma a lista certa de config e eu
aplico; (b) Cap.6 usa "77--83%" (l.30, plato) e "78--83%" (l.201) para
faixas proximas — decidir se harmoniza no plato ou qualifica a segunda como
configuracao final. Sem acao minha: PVBin/BERT sem reabertura no Cap.4
(remissao ao Cap.3 existe); "Acuracia Global e Macro F1" (l.26 Cap.4) e
contraste global-vs-macro intencional; RQ3/RQ4 no Cap.6 sao jargao
permitido pos-Cap.3.
