# Relatório de conformidade com as normas UFPR/PPGMNE

**Data:** 2026-08-16
**Autor da tese:** Gilsiley Henrique Darú — Tese de Doutorado, PPGMNE/UFPR
**Título (arquivo):** *Aprendizado Ativo com Modelos de Linguagem para Textos Curtos em Português* (FALCO)
**Escopo deste documento:** LEVANTAMENTO. Compara o estado atual da fonte LaTeX
(`principal.tex`, `ppginf.cls`, `packages.tex`, `0-iniciais/*`, `Makefile`) com o
padrão de normalização da UFPR/SiBi e com o que se conhece dos requisitos do
PPGMNE. **Nenhum arquivo da tese foi editado.** As correções apontadas aqui serão
tratadas depois, como ciclos de texto gateados (ver "Plano de correção sugerido").

> Aviso de método: cada não conformidade abaixo cita a evidência exata
> (arquivo:linha) e a fonte da exigência. Itens que a documentação online não
> resolve estão marcados como **a confirmar** e reunidos na seção própria.

---

## 1. Fontes consultadas (com URL)

| # | Fonte | URL | Uso |
|---|---|---|---|
| F1 | SiBi/UFPR — Estrutura de trabalhos acadêmicos (quadro de elementos obrigatórios/opcionais e ordem, tese formato tradicional e alternativo) | https://bibliotecas.ufpr.br/wp-content/uploads/2022/01/normas_estrutura.pdf | Elementos pré/textuais/pós-textuais e ordem; regra do termo de aprovação com assinaturas |
| F2 | SiBi/UFPR — Apresentação gráfica (checklist: folha A4, margens, fonte, espaçamento, recuo, paginação, títulos) | https://bibliotecas.ufpr.br/wp-content/uploads/2022/01/normas_apresentacao_grafica.pdf | Margens, fonte, espaçamento, paginação, numeração de seções |
| F3 | SiBi/UFPR — Modelo de trabalho acadêmico (regras de resumo, palavras-chave, abstract, listas, títulos sem indicativo) | https://bibliotecas.ufpr.br/wp-content/uploads/2022/01/normas_modelo_trabalho_academico.pdf | Limite do resumo (150–500 palavras), formato das palavras-chave, listas |
| F4 | SiBi/UFPR — Entrega de Teses e Dissertações (depósito legal, ficha catalográfica, fluxo SIGA) | https://bibliotecas.ufpr.br/servicos/teses-dissertacoes/ | Depósito só digital via SIGA; ficha solicitada à Biblioteca; checklist |
| F5 | SiBi/UFPR — Orientações para Normalização (Manual 2022, templates, tutorial de citação) | https://bibliotecas.ufpr.br/servicos/normalizacao/ | Manual vigente e templates oficiais |
| F6 | Manual de Normalização de Documentos Científicos da UFPR (registro no acervo, 2022) | https://acervodigital.ufpr.br/handle/1884/73330 · https://hdl.handle.net/1884/88892 | Documento-mãe (baseado em ABNT NBR 14724, 6023, 10520, 6027, 6028) |
| F7 | Resolução n. 32/17-CEPE (dispensa de cópia impressa; depósito legal digital) | citada em F2/F4 | Base normativa do depósito |
| F8 | PPGMNE/UFPR — página do programa (áreas de concentração: Mecânica Computacional e Programação Matemática) | https://exatas.ufpr.br/pos_mne/ · https://prppg.ufpr.br/ppgmne/ | Confirma a área de concentração e o vínculo institucional |
| F9 | Origem da classe `ppginf.cls` — modelo do PPGInf/UFPR (Prof. Carlos Maziero) | `ppginf.cls:35,41`; https://gitlab.c3sl.ufpr.br/maziero/tese | Explica divergências: a classe é do PPGInf, adaptada aqui para o PPGMNE |

Observação importante sobre a classe: `ppginf.cls` foi escrita para o **PPGInf**
(Programa de Pós-Graduação em Informática) e traz vários textos default apontando
para "Informática" (`principal.tex:108–132`, comentários). A tese já sobrescreveu
os campos para o PPGMNE (área, descrição), mas a classe **não é o template oficial
do SiBi** (F5) — as divergências abaixo derivam quase todas desse ponto.

---

## 2. Tabela de conformidade

Legenda de gravidade: **[BLOQ]** bloqueante para depósito · **[AJU]** ajuste
simples · **[COS]** cosmético.

### 2.1 Elementos pré-textuais (existência e ordem) — fonte F1, F3

| Elemento exigido | Status | Evidência no repositório | Gravidade |
|---|---|---|---|
| Capa (externo, obrigatório) | Conforme | `ppginf.cls:651–686` gera a capa; `principal.tex:141` `\titlepage` | — |
| Folha de rosto (obrigatório) | Conforme | `ppginf.cls:690–775`; dados em `principal.tex:59–105` | — |
| Ficha catalográfica, no verso da folha de rosto (obrigatório) | **Ausente (placeholder)** | `0-iniciais/catalografica.tex:7` inclui `catalografica.pdf`, que é um **PDF-modelo** com instruções ("solicitar à Biblioteca", refs a template Maziero) — não é a ficha real | **[BLOQ]** |
| Errata (opcional) | Ausente (aceitável) | não há arquivo | — |
| Termo/Folha/Parecer de Aprovação (obrigatório; exige assinatura de TODA a banca) | **Ausente (placeholder)** | `0-iniciais/aprovacao.tex:7` inclui `aprovacao.pdf`, cujo texto é literalmente "Substituir o arquivo 0-iniciais/aprovacao.pdf pela ficha de aprovação fornecida pela secretaria do programa, em formato PDF A4" | **[BLOQ]** |
| Dedicatória (opcional) | Placeholder | `0-iniciais/dedica.tex:4` "Dedicatória a preencher pelo autor." | **[AJU]** (opcional; decidir manter ou remover) |
| Agradecimentos (opcional) | Placeholder | `0-iniciais/agradece.tex:6` "Agradecimentos a preencher pelo autor na versão final." | **[AJU]** |
| Epígrafe (opcional) | Ausente (aceitável) | — | — |
| Resumo em português + palavras-chave (obrigatório) | Conforme (existência) / **Não conforme (extensão)** — ver 2.3 | `0-iniciais/resumo.tex`; palavras-chave em `principal.tex:62` | **[BLOQ]** pela extensão |
| Abstract + keywords (obrigatório) | Conforme (existência) / **Não conforme (extensão)** | `0-iniciais/abstract.tex`; keywords em `principal.tex:63` | **[BLOQ]** pela extensão |
| Declaração de uso de IA (NÃO é elemento SiBi) | A confirmar (posição) | `0-iniciais/declaracao-ia.tex`; incluída em `principal.tex:154`, **entre** abstract e listas | **[AJU]** |
| Lista de figuras (opcional) | Conforme | `principal.tex:157` `\listoffigures` | — |
| Lista de tabelas (opcional) | Conforme | `principal.tex:159` `\listoftables` | — |
| Lista de siglas/abreviaturas (opcional) | Conforme | `0-iniciais/acronimos.tex`; `principal.tex:160` | — |
| Lista de símbolos (opcional) | Conforme | `0-iniciais/simbolos.tex`; `principal.tex:161` | — |
| Sumário (obrigatório, último pré-textual) | Conforme | `principal.tex:162` `\tableofcontents` (após as listas) | — |

**Ordem dos pré-textuais:** a ordem em `principal.tex:144–162` é
capa/folha-de-rosto → ficha → aprovação → dedicatória → agradecimentos → resumo →
abstract → **declaração-IA** → lista de figuras → lista de tabelas → siglas →
símbolos → sumário. A ordem SiBi (F1) é: ficha → aprovação → (dedicatória,
agradecimentos, epígrafe opcionais) → resumo → abstract → listas → sumário. A
única inserção fora do quadro SiBi é a **declaração de IA** entre o abstract e as
listas (ver item a confirmar).

### 2.2 Modo de compilação (impacta TODOS os pré-textuais obrigatórios)

| Item | Status | Evidência | Gravidade |
|---|---|---|---|
| Documento compilado em modo `defesa` (omite ficha, aprovação, dedicatória, agradecimentos) | **Não conforme para depósito** | `principal.tex:31` `\documentclass[defesa,oneside,english,brazilian]{ppginf}`; a classe transforma esses ambientes em comentário no modo defesa (`ppginf.cls:566–574`) | **[BLOQ]** — a versão de depósito precisa ser `final` (`principal.tex:37`) |

Consequência: enquanto a classe estiver em `defesa`, a ficha, a folha de
aprovação, a dedicatória e os agradecimentos **não são renderizados** — logo o PDF
atual não é depositável. Trocar para `final` é o gatilho que expõe os itens
[BLOQ] da seção 2.1 (ficha e aprovação reais).

### 2.3 Resumo, abstract e palavras-chave — fonte F3

| Regra SiBi (F3) | Status | Evidência | Gravidade |
|---|---|---|---|
| Resumo entre **150 e 500 palavras**, parágrafo único, justificado, espaçamento simples | **Não conforme (extensão)** | `0-iniciais/resumo.tex` tem ~**734 palavras** (parágrafo único ok) | **[BLOQ]** |
| Abstract idem (mesma faixa) | **Não conforme (extensão)** | `0-iniciais/abstract.tex` tem ~**701 palavras** | **[BLOQ]** |
| Palavras-chave separadas por ponto e finalizadas por ponto | Conforme | `principal.tex:62` "Aprendizado Ativo. Classificação de Textos Curtos. ... Rotulagem." | — |
| Keywords idem no idioma estrangeiro | Conforme | `principal.tex:63` "Active Learning. ... Labeling." | — |
| "Palavras-chave:" / "Keywords:" precedendo os termos | Conforme | `ppginf.cls:540,558` | — |

Nota: o número de palavras foi obtido por contagem aproximada do corpo (excluídos
comandos LaTeX). Ambos ultrapassam com folga o teto de 500 palavras — a Biblioteca
tende a devolver em diligência. Redução de conteúdo do resumo/abstract deve ser
tratada como ciclo de texto (não é mero corte cosmético).

### 2.4 Apresentação gráfica — fonte F2

| Regra SiBi (F2) | Status | Evidência | Gravidade |
|---|---|---|---|
| Folha A4 (21×29,7 cm) | Conforme | `ppginf.cls:73–82,121` `a4paper`; `packages`/classe base `book` 12pt | — |
| Fonte tamanho 12, Times New Roman ou Arial | Conforme | classe base `12pt` (`ppginf.cls:75`); `packages.tex:14` `newtxtext` (Times) | — |
| Margens anverso: superior 3, esquerda 3, direita 2, inferior 2 cm | Conforme (com ressalva) | `ppginf.cls:122–123` define `top=3,left=2,right=2,bottom=2` **mais** `bindingoffset=1cm`; em `oneside` o offset soma à esquerda → esquerda efetiva 3 cm, direita 2 cm | **[AJU]** verificar no PDF renderizado; confirmar que o `bindingoffset` cai à esquerda (não some no verso) |
| Espaçamento **1,5 entre linhas do texto** | **Não conforme no modo final** | `ppginf.cls:335–339`: modo `final` usa `\singlespacing` (espaçamento 1); apenas o modo `defesa` usa `\onehalfspacing` | **[BLOQ]/a confirmar** — a versão de depósito (final) ficaria com espaçamento 1, mas o SiBi F2 exige 1,5 no texto |
| Espaçamento simples em resumo, referências, notas, citações longas, legendas | Conforme | `ppginf.cls:331` legendas em `singlespacing`; resumo/abstract em ambiente próprio | — |
| Recuo de 1,5 cm na 1ª linha do parágrafo | Conforme | `ppginf.cls:291` `\parindent=15mm` | — |
| Recuo de 4 cm para citações longas | Conforme | `ppginf.cls:306–313` `quote`/`quotation` com `leftmargin=40mm` | — |
| Paginação em algarismos arábicos, tamanho 10, canto superior direito (anverso) | Conforme | `ppginf.cls:397–399` `\fancyhead[R]{\footnotesize\thepage}` | — |
| Páginas contadas da folha de rosto, número aparece só a partir do texto | Conforme | frontmatter sem número (`ppginf.cls:389–391`); reinício após capa (`ppginf.cls:685`); classe força numeração da introdução a considerar as preliminares (`ppginf.cls:383–386`) | — |

### 2.5 Numeração de seções e títulos — fonte F2

| Regra SiBi (F2) | Status | Evidência | Gravidade |
|---|---|---|---|
| Indicativo numérico separado do título por 1 espaço, sem ponto/hífen/travessão | Conforme | `ppginf.cls:131,134–159` usa `\numberspacing` (espaço), sem pontuação | — |
| Seção primária (capítulo) em maiúsculas e negrito, iniciando em nova página | Conforme | `ppginf.cls:134–138`; `book` inicia capítulo em nova página | — |
| Secundária maiúsculas; terciária/quaternária só a 1ª letra | Conforme | `ppginf.cls:141–159`: seção `\MakeUppercase`, subseção/subsubseção sem uppercase | — |
| Títulos sem indicativo (resumo, listas, sumário, referências, apêndice) centralizados, maiúsculas, negrito | Conforme | `ppginf.cls:162–166` (chapter numberless: centrado, uppercase, bfseries) | — |
| Não ultrapassar a seção quinária | Conforme | `secnumdepth=3` (`ppginf.cls:194`) limita a subsubseção | — |

### 2.6 Citações e referências — fonte F6 (ABNT NBR 10520 e 6023)

| Regra | Status | Evidência | Gravidade |
|---|---|---|---|
| Sistema de citação autor-data (aceito pela NBR 10520; é o usado nos exemplos do manual UFPR) | Conforme | `packages.tex:78–82` `natbib` + `apalike-ptbr`; capítulos usam `\citep`/`\citet` | — |
| Uso de `\cite` puro desaconselhado (preferir `\citep`/`\citet`) | Ajuste | `2-fundam/texto.tex:33,44,46,49,53…` usam `\cite{}`; a classe remapeia `\cite`→`\citep` (`packages.tex:82`), então funciona, mas o `principal.tex:182` recomenda evitar | **[COS]** |
| Lista de referências no formato ABNT NBR 6023 | **A confirmar** | estilo `apalike-ptbr.bst` (`packages.tex:80`) é uma adaptação PT-BR do apalike, **próxima mas não idêntica** à NBR 6023 (ABNT usa AUTOR em versalete, título em negrito, pontuação própria) | **[BLOQ]/a confirmar** com a Biblioteca se o estilo é aceito |
| Título "REFERÊNCIAS" e inclusão no sumário | Conforme | `ppginf.cls:587` renomeia `\bibname`; `tocbibind` inclui no sumário (`ppginf.cls:253`) | — |

### 2.7 Elementos pós-textuais — fonte F1

| Elemento | Status | Evidência | Gravidade |
|---|---|---|---|
| Referências (obrigatório) | Conforme | `principal.tex:185` `\bibliography{referencias}` | — |
| Glossário (opcional) | Ausente (aceitável) | — | — |
| Apêndices (opcional) — A1…A7 | Conforme | `principal.tex:191–199` `\appendix` + 7 `\include`; numeração A, B, … no sumário (`ppginf.cls:281–286`) | — |
| Anexos (opcional) | Ausente (aceitável) | — | — |
| Índice (opcional) | Ausente (aceitável) | — | — |

### 2.8 Metadados institucionais (folha de rosto) — fonte F8

| Item | Status | Evidência | Gravidade |
|---|---|---|---|
| Área de concentração compatível com o PPGMNE | Conforme | `principal.tex:79,82` `\field{Programação Matemática}` (uma das áreas do PPGMNE, F8) | — |
| Descrição/natureza do trabalho (grau de Doutor, PPGMNE, Setores de Ciências Exatas e de Tecnologia) | Conforme | `principal.tex:105` | — |
| Instituição por extenso, em português | Conforme | `principal.tex:72,75` "Universidade Federal do Paraná" | — |
| Orientador nomeado | Conforme | `principal.tex:67` "Prof. Dr. Gustavo Valentim Loch" | — |
| Local e ano | Conforme | `principal.tex:85,89,92` "Curitiba PR", 2026 | — |
| Coerência do título (capa usa título descritivo; a tese é referida como "FALCO: Framework…") | A confirmar | `principal.tex:59` título ≠ nome-marca FALCO do repositório; verificar qual é o título oficial de depósito | **[COS]** (fora do escopo de normas; consistência editorial) |

---

## 3. Pontos a confirmar com a secretaria do PPGMNE / Biblioteca

Itens que a documentação online não resolve e que dependem de confirmação humana:

1. **Espaçamento na versão final (item 2.4).** O SiBi (F2) exige 1,5 entre linhas
   do texto; a classe `ppginf.cls` usa espaçamento simples no modo `final`. Confirmar
   se a Biblioteca aceita o espaçamento simples herdado do template PPGInf ou se é
   preciso forçar 1,5 no corpo (alterando a classe ou o modo). **Provável diligência.**
2. **Estilo de referências `apalike-ptbr` (item 2.6).** Confirmar se a Biblioteca
   aceita o autor-data adaptado do apalike ou se exige aderência estrita à NBR 6023
   (AUTOR em versalete, título em negrito). É o risco de normalização mais provável.
3. **Ficha catalográfica (item 2.1).** Deve ser **solicitada à Biblioteca** que
   atende o PPGMNE (fluxo F4), com opção de incluir DOI dos dados (BDC/UFPR). O PDF
   atual é apenas um modelo.
4. **Termo de aprovação (item 2.1).** Fornecido pela **secretaria do PPGMNE** após
   a defesa, com assinatura de todos os membros da banca (F1 exige; sem assinaturas
   não é aceito).
5. **Declaração de uso de IA (item 2.1).** Não é elemento previsto no quadro SiBi.
   Confirmar com o PPGMNE se pode figurar como pré-textual (posição atual) ou se
   deve migrar para apêndice, para não quebrar a sequência obrigatória.
6. **`bindingoffset` e margens (item 2.4).** Confirmar no PDF renderizado em modo
   `final`/`oneside` que a margem esquerda efetiva é 3 cm e a direita 2 cm.
7. **Formato tradicional vs. alternativo.** Esta tese é por capítulos (formato
   tradicional). Confirmar que o PPGMNE não exige/permite o formato alternativo por
   artigos (há `artigos/` derivados no repositório) — se optar por artigos, muda o
   quadro de exigências (F1, formato alternativo).

---

## 4. Plano de correção sugerido (agrupado em ciclos gateáveis — NÃO executado)

Cada ciclo abaixo é um candidato a ciclo Maestro (branch própria → DoD → gate
humano). Ordenados por bloqueio de depósito.

- **Ciclo N-1 — Chave de compilação e páginas oficiais (infra).**
  Trocar `\documentclass` para `final` na versão de depósito (`principal.tex:31→37`);
  inserir a **ficha catalográfica** real (solicitada à Biblioteca) e o **termo de
  aprovação** assinado (secretaria) nos respectivos `.pdf`. DoD verificável: PDF em
  modo final renderiza ficha no verso da folha de rosto e aprovação com assinaturas;
  `grep` do texto placeholder em `aprovacao.pdf`/`catalografica.pdf` retorna vazio.
  *Depende de artefatos externos (Biblioteca + secretaria) — não é auto-contido.*

- **Ciclo N-2 — Resumo e abstract dentro de 150–500 palavras (texto).**
  Reduzir `0-iniciais/resumo.tex` (~734→≤500) e `0-iniciais/abstract.tex` (~701→≤500)
  preservando os resultados-chave. DoD: contador de palavras ≤ 500 em ambos. É ciclo
  de conteúdo (usar `fight-the-pile-up` para densificar sem perder técnica).

- **Ciclo N-3 — Espaçamento e referências (a confirmar antes).**
  Depois de confirmar itens 3.1 e 3.2: se necessário, forçar 1,5 no corpo do modo
  final e/ou trocar `apalike-ptbr` por um `.bst` aderente à NBR 6023. DoD: PDF final
  com espaçamento 1,5 no texto; amostra de 5 referências conferida contra NBR 6023.
  *Toca `ppginf.cls`/`packages.tex` — lane infra (reversibilidade).*

- **Ciclo N-4 — Elementos opcionais e posição da declaração de IA (texto leve).**
  Preencher ou remover dedicatória/agradecimentos (`dedica.tex`, `agradece.tex`);
  decidir a posição da declaração de IA (`principal.tex:154`) conforme resposta do
  item 3.5. DoD: sem texto "a preencher" remanescente; ordem pré-textual alinhada a F1.

- **Ciclo N-5 — Higiene de citação (cosmético).**
  Substituir `\cite{}` por `\citep{}`/`\citet{}` nos capítulos (ex.: `2-fundam/texto.tex`).
  DoD: `grep -n '\\cite[^pt]' */texto.tex` retorna vazio.

---

## 5. Resumo do levantamento

- **Itens verificados:** 40.
- **Conformes:** 25.
- **Não conformes:** 6 — modo `defesa` (2.2); ficha placeholder (2.1); aprovação
  placeholder (2.1); resumo >500 palavras (2.3); abstract >500 palavras (2.3);
  espaçamento simples no modo final (2.4).
- **Ausentes (obrigatórios):** contados acima como não conformes (ficha e aprovação
  são placeholders, não documentos reais).
- **A confirmar:** 7 (seção 3), com destaque para espaçamento final e estilo de
  referências (`apalike-ptbr` vs. NBR 6023).
- **Cosméticos/opcionais:** os demais (dedicatória/agradecimentos placeholder,
  `\cite` puro, coerência de título).

**Bloqueantes para depósito (5):** (1) compilar em modo `final`; (2) ficha
catalográfica real da Biblioteca; (3) termo de aprovação assinado pela banca;
(4) resumo ≤ 500 palavras; (5) abstract ≤ 500 palavras. O espaçamento do modo final
e o estilo de referências são bloqueantes **prováveis**, pendentes de confirmação
com a Biblioteca.
