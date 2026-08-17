---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: sanear a pasta a_sanear/ (3 PDFs novos identificados abaixo), mover para referencias-pdf/ com nome canônico, atualizar/criar fichamentos contra o PDF integral; prioridade 1 continua a Margatina2023 (agora com PDF no repositório)
referencia: a_sanear/ na main · sua tarefa 20260816-2152 (fichamento Margatina) · fichamentos/Bayer2024ActiveLLM.md (PDF declarado ausente, seu achado de 20260816-2041)
criada_em: 2026-08-16T22:20:00Z
---

O autor subiu 3 PDFs em `a_sanear/`. O principal identificou cada um pela
PRIMEIRA PÁGINA (não pelo nome do arquivo) — re-verifique ao fichar:

1. `2023.findings-emnlp.334.pdf` (24 pp.) = **Margatina2023**. Página 1 bate
   com a entrada verificada: "Active Learning Principles for In-Context
   Learning with Large Language Models", Margatina, Schick, Aletras,
   Dwivedi-Yu, Findings EMNLP 2023, pp. 5011-5034. ATENÇÃO: o autor recebeu
   este PDF sob o título ERRADO "Active Learning Strategies for LLMs: A
   Survey" — o conteúdo é a obra certa; se você encontrar TAMBÉM um survey
   com esse outro título em alguma fonte, é outra obra, não esta.
   → mover para `referencias-pdf/Margatina2023.pdf`, fichar contra o PDF
   integral (destrava o gate da prosa do Cap. 2).

2. `International Journal of Intelligent Systems - 2025 - Zhang - ....pdf`
   (14 pp.) = **Zhang2025** (Yejian Zhang e Shingo Takada, Keio). Já existe
   `referencias-pdf/Zhang2025.pdf` — confira se é o mesmo arquivo/obra;
   ficando com o melhor dos dois, e o fichamento Zhang2025 revisado contra o
   PDF (é uma das 5 chaves repontuadas que o Cap. 1 espera).

3. `tacl.a.63.pdf` (22 pp.) = **Bayer2024ActiveLLM** ("ActiveLLM...", TACL).
   Página 1 mostra TRÊS autores: Markus Bayer, **Justin Lutz** e Christian
   Reuter — confira a lista de autores e o ANO/volume da entrada no bib
   contra o PDF (a tabela do site exibe 2026; TACL imprime por volume —
   registre o que o PDF/DOI disser, não o que a chave sugere). Resolve
   também o PDF declarado ausente no fichamento (seu achado das 20:41).
   → `referencias-pdf/Bayer2024ActiveLLM.pdf`.

Sobre o restante da pasta: os `_TRIAGEM_*.pdf` são rejeitos de triagem
anterior e `tesedaru.pdf` é a própria tese compilada — proponha ao principal
a lista de remoção (nada some sem registro), não apague por conta.

Ao fichar a Margatina2023, avise o principal: eu atualizo a branch
fix/cap2-prosa-619-648 com a citação e levo ao merge (aprovação prévia do
autor já registrada no plano).

## Resultado (revisor2, 2026-08-16)

SANEAMENTO FEITO na branch **sanear/pdfs-e-bib** (@bef7566). Os três PDFs saíram
de a_sanear/ para referencias-pdf/ com a chave BibTeX como nome. Conferi cada
identidade na primeira página do arquivo, como você pediu.

1. MARGATINA2023 — nada a refazer, e isso é um bom sinal. O arquivo que o autor
   subiu é BYTE-IDÊNTICO (mesmo md5) ao que eu havia baixado da ACL Anthology
   às 21:5x. Ou seja, o fichamento entregue em 5334318 já foi feito contra este
   PDF. Sobre o alerta do título errado: confirmo que o conteúdo é a obra certa;
   não encontrei nem procurei o tal survey "Active Learning Strategies for LLMs",
   e ele NÃO está citado em lugar nenhum nosso.

2. BAYER — aqui havia problema real, dois na verdade.
   (a) O PDF que estava no repositório era OUTRA versão: 18 páginas contra 22 do
       publicado. Substituído pelo publicado.
   (b) Você tinha razão sobre a autoria: a primeira página traz TRÊS autores —
       Markus Bayer, JUSTIN LUTZ e Christian Reuter. O fichamento listava dois.
       Corrigido, junto com o venue completo: TACL, vol. 14, pp. 1-22, publicado
       em 1/2026, DOI 10.1162/TACL.a.63. O ano 2026 que a entrada já trazia está
       CERTO — é o ano de publicação impresso no rodapé, apesar de a chave dizer
       2024 (que é o ano do preprint).
   Aproveitei que agora temos o PDF integral e preenchi os 3 claims que estavam
   marcados "(preencher c/ PDF final)" — a skill proíbe inventar, então tinham
   ficado em aberto desde sempre. Entraram mais 2 claims. Registrei a limitação
   que mais nos importa: a anotação ali é SIMULADA (o rótulo verdadeiro é
   atribuído "como se tivesse sido anotado por um anotador perfeito", §4.1, p. 6).
   Ou seja, o ActiveLLM não mede erro de oráculo — que é justamente o que a tese
   mede no par A-B.

3. ZHANG2025 — o fichamento era um esboço: autor genérico "Zhang (et al.; ver
   PDF)" e nenhuma tabela de claims. Reescrito lendo o artigo publicado: 7 claims
   com seção e página, números com condições exatas, crítica e ideias.
   DOIS ACHADOS QUE VALEM SUBIR AO AUTOR:
   - Custo: eles retêm MAIS DE 93% do desempenho gastando cerca de 6% do tempo e
     do dinheiro, comparado a mandar tudo para o GPT (Resumo, p. 1). É a âncora
     externa mais direta que temos para a nossa própria conta de custo.
   - Método: eles escolhem o ponto de parada OLHANDO O PLATÔ da curva (25ª, 30ª e
     19ª iterações, §4.4). Nós paramos por critério pré-registrado. Dá um
     parágrafo a favor do rigor da tese, sem desqualificar o trabalho deles.

O BIB NÃO FOI TOCADO. Fui corrigir Bayer e Zhang e descobri que o lote 5 do
revisor1 já havia corrigido as duas, com os mesmos dados (inclusive o Justin
Lutz e os nomes reais Yejian Zhang / Shingo Takada). Descartei minha edição em
vez de duplicar. Lock do bib liberado neste push.

RESTO DA PASTA — proponho, não executo, como você mandou. Sugiro remover os 5
arquivos `_TRIAGEM_*.pdf` (rejeitos já triados: dois volumes de anais não
relacionados, um capítulo já arquivado, slides sem autoria e uma matriz de
indexação em chinês sem autoria) e o `tesedaru.pdf`, que é a própria tese
compilada e se regenera pelo Makefile. São 68 MB no total. Tudo reversível pelo
git. Se aprovar, faço na mesma branch e listo os arquivos no commit.
