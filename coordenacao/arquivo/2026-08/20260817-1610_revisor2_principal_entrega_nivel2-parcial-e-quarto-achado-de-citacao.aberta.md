---
de: revisor2
para: principal
tipo: entrega
acao_esperada: NÍVEL 2 — bloco entregue no que é obtível (branch ciclo/012-fichas-nivel1-cap2 @6bb4b44): 2 fichadas na fonte, 3 viram link para o autor, 1 segue não localizada com suspeita registrada. QUARTO achado de citação: Reusens2024 não sustenta a frase do k-fold
referencia: sua tarefa 20260817-1420 (nível 2) · minha entrega do nível 1 (056f460)
criada_em: 2026-08-17T16:10:00Z
---

Das 6 que faltavam no nível 2 (as outras 4 já estavam prontas no ciclo 010):

| Chave | Situação | Resultado |
|---|---|---|
| `Reusens2024` | **aberta**, e eu achei | **fichada** — versão de acesso aberto no repositório da KU Leuven, 48 pp., autoria conferida |
| `Aliero2023` | aberta (IJCA, 12 pp.) | **fichada** |
| `Ahmed2022` | MDPI bloqueia meu acesso | link para o autor: DOI `10.3390/app13010342` |
| `Attenberg2010` | ACM, paywall (403) | link para o autor: DOI `10.1145/1835804.1835859` |
| `Hanneke2015` | Foundations and Trends, fechada | link para o autor: DOI `10.1561/9781601988096` |
| `Barros2014` | **não localizada** | segue pendente, com suspeita registrada abaixo |

Uma boa notícia: **o `Reusens2024` estava classificado como fechado e não é** —
o repositório institucional da KU Leuven publica a versão aceita. Fichei na
fonte, e de passagem confirmei os sete autores contra a folha de rosto.

Sobre o `Ahmed2022`: o artigo é de acesso aberto em princípio, mas a MDPI recusa
a minha requisição ("Access Denied", proteção contra robô, não paywall). Não é
falha de proxy — conferi o estado dele. **Do computador do autor deve abrir
normalmente.**

## QUARTO achado de citação: `Reusens2024` não sustenta a frase do $k$-fold

A §2.1 (`2-fundam/texto.tex:134`) diz "com $k$ tipicamente 5 ou 10, equilíbrio
entre viés, variância e custo \cite{Nti2021, Reusens2024}". Medi no PDF inteiro:
**a palavra "fold" aparece UMA vez em 48 páginas, dentro de "threefold"**, uso
retórico. A seção de metodologia trata de **seleção de conjuntos de dados**, não
de validação cruzada; o artigo não discute escolha de $k$ nem o compromisso
viés-variância-custo.

**A frase não fica órfã:** `Nti2021` sustenta com precisão — conferi no PDF hoje,
diz literalmente "$k$ tipicamente 5 ou 10" e admite que "there is no formal
rule".

**Recomendação: mover, não remover** — mesmo padrão dos outros três achados. O
`Reusens2024` é um benchmark imparcial (5 tarefas, 20 conjuntos, 11 arquiteturas,
**42.800 execuções**) cuja tese é que **os maiores modelos do estado da arte não
são sempre preferíveis e métodos simples competem em vários casos**. Isso
sustenta, e bem, a decisão de instrumento do Cap. 3 desta tese — usar um
classificador de porte médio em vez do maior modelo disponível. É citação
valiosa no lugar certo.

## `Barros2014`: suspeita registrada, NÃO concluída

O que medi, e o limite do que posso afirmar:

| Verificação | Resultado |
|---|---|
| título exato na Crossref | **um** registro, e é da **homônima**: Castro & Braga, *Sba: Controle & Automação*, 2011, v. 22, p. 441-466, DOI `10.1590/s0103-17592011000500002` |
| a obra declarada (Barros, Garcia, Cavalcanti · Rev. de Sistemas de Informação da FSMA, v. 13, p. 4-19, 2014) | **sem registro** na Crossref nem no OpenAlex |
| arquivo do próprio periódico (fsma.edu.br) | **inacessível daqui** — o servidor recusa com Mod_Security (HTTP 406), não é o nosso proxy |

O padrão — título de uma obra real sob autoria, veículo e ano diferentes — é o
**mesmo do `Razali2020`**, que se confirmou fabricada. Mas há uma diferença
honesta: a FSMA **não deposita DOI**, então ausência de registro é evidência
fraca, e não posso condenar a entrada por isso. **Não concluo, e não removo.**

O que peço: o autor abrir o arquivo da revista (o site responde a navegador
normal) e dizer se o artigo existe no volume 13. É uma checagem de dois minutos
para ele e destrava a decisão. **Alívio:** a frase que a cita (§2.1, l. 89) tem
outras duas chaves já verificadas — `Sokolova2009` e `Grandini2020` —, então a
afirmação não depende dela.

## Nota de bibliografia, para o revisor1

`Ahmed2022`: a chave diz 2022, mas o campo `year` diz **2023**, e o correto é
2023 (*Applied Sciences* 13(1):342). O campo está certo e a chave é só herdada —
registro para ninguém "corrigir" o ano para casar com a chave. Mesmo caso do
`Diao2023` (chave 2023, publicação ACL 2024) e possivelmente do `Hanneke2015`
(bib diz 2015; a Crossref registra a monografia em **2014**) — este último vale
uma conferida na fonte quando o autor tiver o PDF.

## Medições (princípio V)

| Medida | Resultado |
|---|---|
| `check-fichamentos.py` nas 2 fichas novas | `PROBLEMAS: nenhum` |
| check completo na minha branch | **333** problemas (main: 334) — segue **um a menos**, nenhum acrescentado |
| KG | regenerado, 658 nós / 1389 arestas |

## Próximo passo

Faltam do nível 2 apenas as **3 fechadas + `Barros2014`**, todas dependentes do
autor. Sigo para o **nível 3**: a análise das 8 obras-marco (`Radford2018`,
`Radford2019`, `Peters2018`, `Bojanowski2017`, `Xu2017`, `Krause2014`,
`Golovin2011`, `Yan2011`) com a proposta de política — se cabem em extensão da
regra canônica ou se alguma sustenta afirmação e sobe de nível. Análise minha,
consolidação sua, decisão do autor.

## Resultado (principal)
Entrega processada e integrada; arquivada na limpeza.
