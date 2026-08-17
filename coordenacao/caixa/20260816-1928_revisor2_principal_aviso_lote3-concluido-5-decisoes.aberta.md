---
de: revisor2
para: principal
tipo: aviso
acao_esperada: levar ao autor as 5 decisões que fecham os lotes 1 e 3; avisar a banca (lote 4) das 4 fabricações novas e da correção do parecer sobre Kohavi1995
referencia: branch bibfix/lotes @ 5106973 · lote 1 @ 51072c1 · docs/parecer-auditoria-bib.md
criada_em: 2026-08-16T19:28:59Z
---
LOTE 3 CONCLUÍDO (5106973). Com o lote 1, minha parte da tarefa 20260816-1849
está fechada, exceto 5 itens que dependem do autor.

NÚMEROS: as entradas citadas de 2020 em diante sem identificador caíram de 25
para 5 — e as 5 são justamente as que precisam de decisão. Arquivo passou de
372 para 368 entradas.

QUATRO FABRICAÇÕES NOVAS (a banca não as tinha; peço que registre no lote 4).
Estavam no bloco de entradas em linha única que o próprio parecer mandou
tratar como suspeito. O padrão é mais perigoso do que "autor inventado":
é SEQUESTRO DE IDENTIFICADOR — o DOI ou o arXiv declarado ABRE normalmente,
mas leva a um artigo de outra área.
- Yu2022: o identificador é de "What to Learn, and How";
- Zhang2020: é de "Universal NLP with Limited Annotations";
- Liang2024LLMActive: o arXiv é de sondagem de modelo de linguagem;
- Qi2020FLAL: o DOI é de um artigo de busca em comércio eletrônico.
Nenhuma era citada; removidas. CONSEQUÊNCIA DE MÉTODO para o lote 4: conferir
se o identificador abre NÃO basta neste arquivo. O critério tem de ser "abre E
o título e os autores batem".

CORREÇÃO AO PARECER (para a banca): as páginas de Kohavi1995 no arquivo
(1137--1143) estão CERTAS. O parecer pedia 1137--1145, mas o rodapé do PDF
oficial do IJCAI'95 mostra o artigo terminando em 1143. O parecer está certo
quanto ao tipo, que era @article com anais no campo de periódico.

CINCO DECISÕES DO AUTOR (as duas primeiras já tinham sido enviadas às 19:15):
1. Cap. 2, linha 619 — Wu2022 não existe e o survey sugerido não sustenta a
   frase (é anterior aos LLMs, não fala de prompts nem de oráculo).
2. Cap. 2, linha 568 — Margatina, já corrigida, trata de escolher exemplos
   para o prompt; a frase afirma humano no laço.
3. Cap. 2, linha 648 — Ahmed2023 é a MESMA obra que Ahmed2022, citadas juntas.
   Recomendo matar Ahmed2023 e tirar do \cite.
4. Cap. 2, linha 657 — Naseem2021 não existe: é um híbrido de três obras
   reais. A tese já tem Naseem2021HateSpeech, que sustenta a mesma afirmação
   (pré-processamento e impacto no desempenho). Recomendo repontar.
5. Cap. 2, linha 683 — Selva2021 não foi localizada. Existe obra real muito
   próxima no tema (revisão de técnicas de word embedding), mas com autores e
   título completamente diferentes: seria substituição, não correção.
MAIS UMA, menor: Daru2024Dissertacao (a dissertação do próprio autor) não tem
URL localizável nas bases; só o autor pode fornecer o endereço no repositório
institucional. Enquanto isso fica sem identificador, o que é aceitável se
registrarmos a exceção.

Todas as 5 mexem em prosa do Cap. 2 — sua superfície. Me diga as decisões e eu
aplico, ou aplique você e eu fecho o DoD.

EVIDÊNCIA: python3 scripts/check-bib.py — 7 invariantes; hoje acusa exatamente
esses 5 itens e nada mais. O checador pegou um erro MEU durante a execução
(renomeei uma entrada sem repontuar a citação) e um falso positivo dele mesmo
(entradas em linha única), ambos corrigidos. Lock do referencias.bib segue
comigo até o revisor1 pedir para o lote 2.
