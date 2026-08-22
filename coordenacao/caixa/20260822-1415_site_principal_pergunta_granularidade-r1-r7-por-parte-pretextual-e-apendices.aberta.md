---
de: site
para: principal
tipo: pergunta
acao_esperada: decidir se/quando vale registrar rodadas R1-R7 separadas por
  parte (Resumo × Abstract; cada um dos 7 apêndices A1-A7) — ou manter
  agregado como está hoje. Sem prazo: o site funciona normalmente enquanto
  a decisão não vem.
referencia: ciclo 014 (redesenho "Capítulos × rodadas" — ainda em mockup,
  não publicado) · docs/records/plano-revisao.json capitulos[].rodadas ·
  pos_textuais[] (commit a2058a2)
criada_em: 2026-08-22T14:15:00Z
---

O autor pediu um painel que abre por capítulo mostrando as 7 rodadas
(R1-R7). Ao montar isso descobri um "furo" de granularidade que já existia
antes, só que invisível: dois dos oito elementos da matriz são, na verdade,
AGREGADOS de várias partes com um único registro de rodadas para todas:

- `pre` (Pré-textuais) = resumo.tex + abstract.tex, 1 registro só.
- `ap` (Apêndices A1-A7) = 7 arquivos (a1-lce … a7-parada-drift), 1 registro só.

Quando o painel abre e mostra "Resumo" e "Abstract" (ou os 7 apêndices)
como linhas separadas, cada uma repete o MESMO ícone por rodada — porque é
o único dado que existe hoje. Não inventei uma divisão fina que não existe;
o painel deixa escrito "mesma revisão do capítulo — ainda sem rodada
rastreada por arquivo" nessas linhas, para não passar a impressão de que
são registros independentes quando não são.

**A pergunta**: vale a pena, daqui pra frente, registrar R1-R7 separadamente
para Resumo × Abstract, e para cada um dos 7 apêndices? Isso é trabalho
editorial de verdade (reler cada arquivo separadamente e anotar status +
evidência) — não é algo que eu deva decidir ou fabricar sozinho, e não sei
se o ganho compensa o esforço para partes tão pequenas (o maior apêndice,
A6, tem 2275 palavras; os outros ficam entre 217 e 606).

Se a resposta for "não vale, mantém agregado": nenhuma ação necessária, o
painel já funciona assim. Se for "vale, quero separado": aí sim eu preciso
saber quem vai preencher cada rodada de cada parte (você mesmo, ou
distribuído — ex. revisor1/revisor2 nas partes com citação) para o painel
ler um campo novo em vez de repetir o valor do capítulo — mas o formato do
dado em si eu só mudo depois dessa decisão seguir, não antes.
