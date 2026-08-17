---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao gate; e ciência de que fiquei ~3h sem responder por falha do meu auto-check — as 3 tarefas ficaram .aberta esse tempo todo
referencia: bibfix/lotes @ 843cc46 · tarefas 20260816-2152 e 20260817-0045 · locks liberados neste commit
criada_em: 2026-08-17T00:55:00Z
---
Retomei e executei as duas tarefas de bib. Começo pela falha, que é minha.

LACUNA DE ~3 HORAS. Meu mecanismo de auto-verificação da caixa parou de
disparar por volta das 21:51 e só voltou às 00:30. Nesse intervalo as três
tarefas que você me endereçou (21:52, 22:05 e 00:45) ficaram em `.aberta`, sem
claim. Não foi decisão: foi a corrente de agendamento morrendo em silêncio, que
é o modo de falha que eu mesmo tinha previsto quando montei o mecanismo. Se
alguma delas era caminho crítico, o atraso é meu.

TAREFA 20260816-2152 — FEITA (843cc46)
- Os 4 DOIs inseridos exatamente como verificados: Kowsari2019, Xu2017,
  Reimers2019SBERT e Peters2018.
- Goldberg2017 virou @book (Synthesis Lectures, Morgan & Claypool, 2017), SEM
  DOI — confirmando o que eu havia levantado: o único DOI que o Crossref
  devolve para esse título é o da RESENHA na Computational Linguistics.
- Invariante implementado no check-bib e PROVADO por teste negativo: removi o
  Houlsby2011 numa cópia e o checador acusou "alvo de relacao sem entrada no
  bib: Houlsby2011 (referenciado em Farquhar2021Bias.md)"; restaurei. Sem a
  remoção, exit 0.
  Detalhe de alcance que vale registrar: a primeira versão varria subpastas e
  acusou 2 casos em fichamentos/leitura-cruzada-revisor1/. Alinhei o glob ao
  do build_kg.py (não recursivo), porque aquela pasta guarda leituras
  preservadas verbatim FORA do grafo — ali a referência é registro histórico,
  não aresta viva, e acusá-la seria falso positivo. O arquivo é do revisor2;
  editei sob lock declarado na main.

TAREFA 20260817-0045 — FEITA. Selva2021 conferida na fonte antes de aplicar,
como você pediu: o DOI 10.1007/978-981-15-9651-3_23 resolve para capítulo de
S. Selva Birunda e R. Kanniga Devi, em Innovative Data Communication
Technologies and Application, LNDECT v.59, pp. 267-281, Springer Singapore,
2021. Bate com o que você levantou. Tipo corrigido de @article para
@incollection, chave preservada, prosa intocada.

ESTADO DO check-bib: exit 0 com 2 pendências, que são as que dependem do merge
da prosa — Wu2022 e Ahmed2023. Ou seja, do lado do bib o ciclo está fechado.

EM ANDAMENTO: a terceira tarefa (20260816-2205, R3 dos temas T2/T4/T5 do
Cap. 2) está reivindicada e é a próxima. Ela é grande e vou entregá-la por
tema, como o plano define.

Locks de referencias.bib e de scripts/check-bib.py liberados neste commit.
