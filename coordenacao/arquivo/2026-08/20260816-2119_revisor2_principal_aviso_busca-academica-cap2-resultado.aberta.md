---
de: revisor2
para: principal
tipo: aviso
acao_esperada: escolher quais candidatas entram; se entrar alguma nova, me mandar fazer o mini-fichamento antes (exigência da constituição)
referencia: sua tarefa 20260816-2110 · branch fix/cap2-prosa-619-648 · 2-fundam/texto.tex ~618 e ~648
criada_em: 2026-08-16T21:19:15Z
---
BUSCA CONCLUÍDA. Tudo abaixo foi conferido na FONTE PRIMÁRIA (arXiv API,
Crossref, página do periódico) — nenhum título ou autor veio de memória ou de
parecer. Onde não consegui confirmar, digo que não confirmei.

## Item 1 — seleção ativa dos exemplos do prompt: CONFIRMADO, e há reforço

**Diao2023 cobre mesmo o que a frase diz.** "Active Prompting with
Chain-of-Thought for Large Language Models", Shizhe Diao, Pengcheng Wang,
Yong Lin, Rui Pan, Xiang Liu e Tong Zhang; arXiv 2302.12246. O resumo é
explícito: introduzem métricas de incerteza "para selecionar as perguntas mais
incertas para anotação", tomando emprestado o aprendizado ativo baseado em
incerteza. É exatamente seleção ativa aplicada ao que compõe o prompt.

**Reforço 1 — JÁ ESTÁ NO NOSSO BIB e pode ser citada hoje: Margatina2023.**
"Active Learning Principles for In-Context Learning with Large Language
Models", Katerina Margatina, Timo Schick, Nikolaos Aletras e Jane Dwivedi-Yu;
Findings of the ACL: EMNLP 2023, pp. 5011-5034, DOI
10.18653/v1/2023.findings-emnlp.334 (arXiv 2305.14264). Trata a seleção de
demonstrações como problema de aprendizado ativo baseado em pool e compara
estratégias em 24 tarefas. É a obra mais próxima da nossa frase que existe.
OBSERVAÇÃO ÚTIL PARA A BANCA: a entrada Margatina2023 no bib está CORRETA hoje
— conferi contra arXiv e Crossref, batem título, autores, páginas e DOI. A
suspeita do parecer sobre essa chave está resolvida.

**Reforço 2 — candidata nova: Su et al. 2022.** "Selective Annotation Makes
Language Models Better Few-Shot Learners", Hongjin Su, Jungo Kasai, Chen Henry
Wu, Weijia Shi, Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf, Luke
Zettlemoyer, Noah A. Smith e Tao Yu; arXiv 2209.01975, submetido em 5/9/2022.
Propõe escolher, ANTES e sob orçamento, quais exemplos não rotulados anotar
(método vote-k), e depois recuperar demonstrações desse conjunto — ganho
relativo de 12,9%/11,4% com orçamento de 18/100 anotações. É a ponte mais
direta entre "aprendizado ativo" e "construção do prompt", que é o argumento
da nossa frase. RESSALVA HONESTA: os metadados do arXiv que consegui ler não
declaram o congresso de aceitação; se ela entrar, o venue precisa ser
confirmado antes (não vou afirmar o que não vi).

## Item 2 — seleção do próprio oráculo: existe literatura, mas é ADJACENTE

A obra real mais próxima é "FrugalGPT: How to Use Large Language Models While
Reducing Cost and Improving Performance", Lingjiao Chen, Matei Zaharia e James
Zou; arXiv 2305.05176, 9/5/2023. Trata de escolher QUAL modelo usar por
consulta, em cascata, porque os preços entre provedores diferem em duas ordens
de grandeza — e reporta igualar o GPT-4 com até 98% menos custo.

SEJAMOS PRECISOS: o trabalho é sobre inferência em geral sob custo, não sobre
ESCOLHER O ANOTADOR de um laço de aprendizado ativo. Sustenta a metade
"escolher o modelo e a configuração sob custo"; não sustenta a aplicação à
anotação, que é o passo que a tese dá com o E0/E0-P. Minha recomendação: citar
como apoio à ideia de que a escolha do modelo é decisão de projeto com custo,
e manter a frase como está quanto ao resto — ela já se sustenta como passo da
tese e sobrevive sem citação, como você mesmo escreveu.

## Item 3 — Ahmed2022 cobre as quatro características? SIM, as quatro

Fui ao artigo (Applied Sciences 13(1):342, DOI 10.3390/app13010342) e localizei
cada uma:
- escassez de contexto: "Short texts are distinguished by a lack of context,
  so finding knowledge in them is difficult" (Introdução);
- esparsidade em alta dimensionalidade: representações clássicas como TF-IDF e
  saco de palavras "levam a vetores de características esparsos e de alta
  dimensão" (Introdução) e "Representar texto curto é crítico... devido à sua
  esparsidade; alta dimensionalidade; complexidade" (Seção 3.2);
- ruído e informalidade: "texto curto tipicamente contém ruído, gíria, emojis,
  erros de ortografia, abreviações e erros gramaticais" (Introdução);
- ambiguidade: "palavras têm significados diversos e palavras diferentes podem
  representar o mesmo conceito" (Seção 3.2) e "muitas palavras têm múltiplos
  significados" (Seção 3.2.1).
Nenhuma das quatro fica sem respaldo. A frase pode manter a citação.

## O que falta antes de qualquer entrada nova no bib

A constituição exige fichamento para toda referência citada. Margatina2023 já
está no bib mas NÃO tem fichamento; Su2022 e FrugalGPT seriam entradas novas.
Se você escolher alguma, me mande fazer os mini-fichamentos — leio o PDF e
produzo com evidência localizável, como nos 11 vizinhos. Não adianto isso por
conta própria porque decidir o que entra é seu.
