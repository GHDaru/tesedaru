# Relatório de não conformidades — tese FALCO × padrão UFPR/PPGMNE

**Data:** 2026-08-16 · **Item do plano:** `normas-ufpr` (FASE LEVANTAMENTO) · **Autor do exame:** revisor2

**Escopo:** inspeção item a item do documento real (fonte LaTeX `principal.tex`,
`0-iniciais/*.tex`, `ppginf.cls`, `packages.tex`, `apalike-ptbr.bst`,
`referencias.bib` e o PDF compilado `principal.pdf`) contra o padrão
SiBi/UFPR e o Manual de Normalização UFPR (checklist do item: pré-textuais
obrigatórios, ficha catalográfica, folha de aprovação, listas,
citações/referências, numeração e margens). Este relatório **não altera a
tese**: cada correção listada é insumo para um futuro ciclo de texto gateado.

**Método:** (1) leitura das fontes normativas primárias obtidas nesta data —
quadro de estrutura SiBi/UFPR ("Orientação para normalização de trabalhos
acadêmicos no formato tradicional", Comissão de Normas SiBi, atualização
12/12/2017, PDF baixado de bibliotecas.ufpr.br) e **Manual de Normalização de
Documentos Científicos ABNT, Ed. UFPR, edição 2024** (PDF de 411 pp. baixado do
Acervo Digital UFPR, handle 1884/88892; seções citadas abaixo por número); (2)
inspeção do fonte com evidência `arquivo:linha`; (3) verificação no PDF
compilado quando o comportamento é gerado pela classe. Aprofunda — sem
duplicar — o levantamento de fontes de `docs/normas-ufpr-ppgmne-e-skills.md`.

**Aviso de escopo normativo:** a tese usa o template `ppginf.cls` (PPGInf/UFPR);
o Manual UFPR 2024 e o quadro SiBi são a referência institucional. Onde os dois
divergem, o veredito abaixo segue o Manual/SiBi e a divergência fica registrada
— a decisão final (template PPGInf aceito pelo PPGMNE ou modelo ABNT-UFPR)
está pendente com a secretaria (base §3, gate G4.1).

---

## 1. Estrutura pré-textual (ordem e presença)

Exigência-mestre: quadro SiBi/UFPR (tese, formato tradicional) — ordem: Capa* →
Folha de Rosto* → Ficha Catalográfica* (verso da folha de rosto) → Errata →
Termo/Folha de Aprovação* → Dedicatória → Agradecimentos → Epígrafe → Resumo +
palavras-chave PT* → Resumo + palavras-chave em língua estrangeira* → Lista de
ilustrações → Lista de tabelas → Lista de abreviaturas e siglas → Lista de
símbolos → Sumário* (* = obrigatório).

| Item | Exigência (fonte) | Estado no documento (evidência) | Veredito | Correção proposta |
|---|---|---|---|---|
| Ordem geral dos pré-textuais | Ordem do quadro SiBi acima | `principal.tex:141-162`: rosto → ficha → aprovação → dedicatória → agradecimentos → resumo → abstract → *declaração-IA* → listas → sumário. Ordem SiBi respeitada, com um elemento extranumerário (ver linha "Declaração de IA") | ✅ | — |
| Capa | Obrigatória; conteúdo instituição/autor/título/local/ano (Manual 2024 §4.2; SiBi) | Gerada pela classe (`ppginf.cls:651-686`) com todos os campos; PDF p. 1 confere. Traz **imagem de fundo** `0-iniciais/fundo-capa.png` (`principal.tex:95`), não prevista no padrão | ⚠️ pendência do autor | Confirmar com secretaria/biblioteca se capa com imagem decorativa é aceita; senão, comentar `\coverimage` |
| Folha de rosto | Obrigatória; nota de natureza do trabalho em fonte 10, espaço simples (Manual §3.1-d, §3.2-c) | `ppginf.cls:690-775` (selo descritivo em `footnotesize`); dados PPGMNE corretos em `principal.tex:66-105` | ✅ | — |
| Errata | Opcional (SiBi) | Ausente | ✅ | — |
| Dedicatória | Opcional (SiBi) | Presente, porém placeholder: "Dedicatória a preencher pelo autor" (`0-iniciais/dedica.tex:4`) | ⚠️ pendência do autor | Preencher na versão final ou remover o `\include` (`principal.tex:146`) |
| Agradecimentos | Opcional (SiBi) | Placeholder: "Agradecimentos a preencher pelo autor na versão final" (`0-iniciais/agradece.tex:6`) | ⚠️ pendência do autor | Preencher na versão final |
| Epígrafe | Opcional (SiBi) | Ausente | ✅ | Registrar como decisão (não incluir) ou incluir |
| Resumo (presença) | Obrigatório, com palavras-chave (SiBi; Manual §4.11) | Presente (`0-iniciais/resumo.tex`, `principal.tex:150`) | ✅ | — |
| Resumo — extensão | "no mínimo 150 e o máximo de 500 palavras" (Manual §4.11-d) | **727 palavras** (`0-iniciais/resumo.tex:3`, contagem `wc -w`) | ❌ | Reduzir a ≤500 palavras — coincide com parecer R6 item 20 ("~800→~500"); executar junto do ciclo humanize-02 |
| Resumo — parágrafo único | Manual §4.11-f | Parágrafo único (`0-iniciais/resumo.tex:3`) | ✅ | — |
| Resumo — espaçamento | Espaço **simples** para resumo/palavras-chave/abstract/keywords (Manual §3.2-c) | Ambiente `resumo` da classe não força espaço simples; na versão defesa herda 1,5 do documento (`ppginf.cls:530-545`, `ppginf.cls:338`) | ❌ (leve) | No ciclo de formatação: envolver resumo/abstract em `\begin{singlespace}` ou ajustar o ambiente na migração de template |
| Palavras-chave (PT) | "antecedidas da expressão Palavras-chave, seguida de dois-pontos, **separadas entre si por ponto e vírgula** e finalizadas por ponto; grafadas com **inicial em minúsculo**, exceto substantivos próprios" (Manual §4.11-h) | `principal.tex:62`: `Aprendizado Ativo. Classificação de Textos Curtos. …` — separadas por **ponto** e com iniciais **maiúsculas**. Rótulo "Palavras-chave:" ✅ (`ppginf.cls:540`) | ❌ | Trocar para `aprendizado ativo; classificação de textos curtos; modelos de linguagem de grande porte; FALCO; rotulagem.` |
| Abstract + keywords | Mesmos critérios do resumo (Manual §4.12); obrigatório (SiBi; Res. 32/17-CEPE art. 39) | Presente (`0-iniciais/abstract.tex`); **696 palavras**; keywords com iniciais maiúsculas e separadas por ponto (`principal.tex:63`) | ❌ | Reduzir a ≤500 palavras e ajustar separador/caixa das keywords, em espelho com o resumo |
| Listas de figuras/tabelas/siglas/símbolos | Opcionais; ordem SiBi (ilustrações → tabelas → abreviaturas e siglas → símbolos) | Presentes na ordem correta (`principal.tex:157-161`); listas com espaçamento 1,25 (`ppginf.cls:605,616` — Manual pede 1,5 nas listas §4.13-15, divergência mínima) | ✅ | Conferir espaçamento das listas na migração; siglas PSI/RS/US ausentes já apontadas no parecer R6 item 20 (conteúdo, não estrutura) |
| Sumário — presença e posição | Obrigatório, último elemento pré-textual (Manual §4.17-a) | `\tableofcontents` após as listas (`principal.tex:162`) | ✅ | — |
| Sumário — sem elementos pré-textuais | "sem os elementos pré-textuais… iniciar com o primeiro elemento textual" (Manual §4.17-c,d; NBR 6027) | A declaração de IA **injeta entrada pré-textual no sumário**: `\addcontentsline{toc}{chapter}{Declara…de IA}` (`0-iniciais/declaracao-ia.tex:5`); confirmado no PDF (sumário lista "Declaração de uso de IA") | ❌ | Remover o `\addcontentsline` da declaração |
| Declaração de IA — posição | Elemento **não normalizado** (fora do quadro SiBi); posição a confirmar com o programa (base §1) | Incluída entre abstract e listas (`principal.tex:154`); o próprio arquivo diz "após agradecimentos ou como apêndice" (`declaracao-ia.tex:1-2`) — inconsistente com a posição real; marcada `RASCUNHO` (`declaracao-ia.tex:3`) | ⚠️ pendência do autor | Confirmar posição com PPGMNE (sugestão conservadora: apêndice, que é elemento normalizado); finalizar o texto (R6 item 18: tirar RASCUNHO, nomear ferramenta, incluir E1/E2) |
| Pré-textuais na versão defesa | — (informativo) | Com a opção `defesa`, ficha/aprovação/dedicatória/agradecimentos não são gerados (`ppginf.cls:566-574`; `principal.tex:31`) | ⚠️ pendência do autor | Compilar o depósito com a opção `final` (`principal.tex:37`) e reconferir tudo |

## 2. Ficha catalográfica

| Item | Exigência (fonte) | Estado no documento (evidência) | Veredito | Correção proposta |
|---|---|---|---|---|
| Ficha catalográfica oficial | Obrigatória, no verso da folha de rosto, elaborada pela biblioteca (SiBi; Manual §4.4); fonte 10, espaço simples (Manual §3.1-d, §3.2-c) | `0-iniciais/catalografica.tex:7` inclui `catalografica.pdf`, que é **placeholder**: página de instruções do template PPGInf ("Substituir o arquivo… pela ficha fornecida pela Biblioteca da UFPR" + passos com contatos do PPGInf — `referencia.bct@ufpr.br`, "avisar a secretaria do PPGInf", gitlab do modelo Maziero; texto extraído do PDF) | ❌ (bloqueia depósito) | Solicitar a ficha oficial à biblioteca do setor (fluxo PPGMNE, não o do PPGInf impresso no placeholder) e substituir o PDF; incluir o DOI da base de dados na ficha (base §1) |
| Posição (verso da folha de rosto) | SiBi: "no verso da Folha de Rosto" | `principal.tex:144` logo após `\titlepage`; classe fecha a folha de rosto com `\clearpage` (`ppginf.cls:775`) e não conta a página da ficha (`ppginf.cls:498`) | ✅ (estrutura) | — |

## 3. Folha de aprovação

| Item | Exigência (fonte) | Estado no documento (evidência) | Veredito | Correção proposta |
|---|---|---|---|---|
| Termo/folha de aprovação | Obrigatório; "não serão aceitos… sem assinatura de todos os membros da banca" (SiBi, nota **) | `0-iniciais/aprovacao.tex:7` inclui `aprovacao.pdf`, **placeholder** ("Substituir o arquivo… pela ficha de aprovação fornecida pela secretaria do programa") | ⚠️ pendência do autor (pós-defesa) | Após a defesa, substituir pelo termo oficial assinado emitido pela secretaria do PPGMNE via SIGA |
| Posição | Após a ficha, antes da dedicatória (SiBi) | `principal.tex:145` | ✅ | — |

## 4. Margens, numeração, entrelinha e fonte (o que `ppginf.cls` define × Manual UFPR 2024 §3)

| Item | Exigência (fonte) | Estado no documento (evidência) | Veredito | Correção proposta |
|---|---|---|---|---|
| Papel | A4 (Manual §3-a) | `ppginf.cls:73-81` (`a4paper`) e `ppginf.cls:121` | ✅ | — |
| Margens | Anverso: sup. e esq. 3 cm; inf. e dir. 2 cm; digital: todas as páginas como anverso (Manual §3-c,e) | `ppginf.cls:122-123`: `right=2cm,left=2cm,top=3cm,bottom=2cm` + `bindingoffset=1cm`. Em `oneside` o bindingoffset soma à esquerda → margem esquerda **efetiva 3 cm**; em `twoside` espelha corretamente (interno 3 cm) conforme Manual §3-d | ✅ (efetivo) | Nenhuma; registrar que a conformidade vem do `bindingoffset`, não das margens nominais — não "corrigir" o 2 cm sem remover o offset |
| Fonte do texto | "sugere-se a fonte Arial ou Times New Roman", tamanho 12, uniforme (Manual §3.1-a,c) | Times via `newtxtext` (`packages.tex:14`); corpo 12pt (`ppginf.cls:73-81`) | ✅ | — |
| Fonte 10 nas exceções | Citação longa, rodapé, legendas, tabelas, nota da folha de rosto, ficha, paginação em tamanho 10 (Manual §3.1-d) | Legendas `footnotesize` ✅ (`ppginf.cls:330`); paginação `footnotesize` ✅ (`ppginf.cls:397-399`); **citação direta longa usa `\small` (≈11pt)** nos ambientes `quote`/`quotation` (`ppginf.cls:310,323`) | ❌ (leve) | Trocar `\small` por `\footnotesize` (e espaço simples) nos ambientes de citação longa no ciclo de formatação |
| Entrelinha do texto | **1,5 para todo o texto** (Manual §3.2-b), simples apenas nas exceções §3.2-c | Defesa: `\onehalfspacing` ✅ (`ppginf.cls:338`); **versão `final`: `\singlespacing`** (`ppginf.cls:335-336`) — tradição PPGInf contrária ao Manual | ❌ (na versão de depósito) | Antes do depósito: decidir com a secretaria; se o Manual prevalecer, forçar `\onehalfspacing` também no modo `final` |
| Citação longa — recuo 4 cm | Manual §3.2-i | `leftmargin=40mm` (`ppginf.cls:308,318`) | ✅ | — |
| Citação longa — espaço simples | Manual §3.2-c | Ambientes `quote`/`quotation` não definem espaçamento (herdam 1,5) (`ppginf.cls:306-325`) | ❌ (leve) | Adicionar espaço simples aos ambientes no ciclo de formatação |
| Recuo de parágrafo 1,5 cm | Manual §3.2-h | `\parindent` = 15mm (`ppginf.cls:291`) | ✅ | — |
| Alinhamento justificado | Manual §3.2-a | Default da classe `book`; sem `\raggedright` | ✅ | — |
| Linhas órfãs/viúvas | Manual §3.2-j | `\clubpenalty`/`\widowpenalty` = 10000 (`ppginf.cls:348-356`) | ✅ | — |
| Paginação — algarismos, posição | Arábicos, tamanho 10, canto superior direito no anverso, a 2 cm da borda (Manual §3.3-a) | `\fancyhead[R]{\footnotesize\thepage}` (`ppginf.cls:397-401`) — arábicos, ~10pt, canto sup. direito ✅; distância exata de 2 cm da borda depende de `headheight/headsep` | ✅ (posição vertical: conferir na prova impressa) | Medir no PDF final; ajustar `headsep` se necessário |
| Capa não contada | Manual §3.3-b | `\setcounter{page}{1}` após a capa (`ppginf.cls:682-685`) | ✅ | — |
| Pré-textuais contadas, não numeradas | Manual §3.3-c | Estilo `frontmatter` sem cabeçalho (`ppginf.cls:389-391`); `\pagenumbering` redefinido sem reset do contador (`ppginf.cls:383-386`, comentário "EXIGÊNCIA DA BIB@UFPR") | ✅ | — |
| Textual numerada em sequência | Manual §3.3-d | `\mainmatter` + estilo `mainmatter` (`principal.tex:167-168`) exibe o número mantendo a contagem | ✅ | — |
| Títulos de seção | Sem indicativo numérico: centralizados; numeração progressiva alinhada à esquerda (Manual §3.4, §4.17-h) | Capítulos não numerados centralizados em caixa alta (`ppginf.cls:162-166`); numerados alinhados à esquerda (`ppginf.cls:134-138`) | ✅ | — |

## 5. Citações e referências (`natbib` + `apalike-ptbr.bst` × Manual UFPR 2024 §8-9 / NBR 10520:2023 / NBR 6023)

Nota normativa: o Manual 2024 (que incorpora a NBR 10520:2023) grafa a citação
parentética em **maiúsculas e minúsculas** — exemplos do próprio Manual:
"(Maranhão, 1998, p. 125)" (§8.6.1) e "(Marconi; Lakatos, 1997, p. 259-301)"
(§8.6.2). A grafia toda em MAIÚSCULAS — "(SILVA, 2020)" — era da NBR
10520:2002, superada. O checklist original deste item citava a regra antiga;
o veredito abaixo segue o Manual 2024 verificado nesta data.

| Item | Exigência (fonte) | Estado no documento (evidência) | Veredito | Correção proposta |
|---|---|---|---|---|
| Sistema de chamada | Autor-data ou numérico, uniforme (Manual §8.2) | Autor-data via natbib (`packages.tex:78-82`); `\cite`≡`\citep` uniformizado (`packages.tex:82`); 100+ usos de `\citep/\citet` nos capítulos | ✅ | — |
| Caixa do sobrenome na citação parentética | Maiúsculas e minúsculas (Manual §8.6.1: "(Maranhão, 1998, p. 125)") | `apalike-ptbr.bst` gera "(Silva, 2020)" — ex. real no PDF: "(Aliero et al., 2023)" | ✅ | — |
| Separador entre autores na citação parentética | **Ponto e vírgula**: "(Marconi; Lakatos, 1997)" (Manual §8.6.2-b, §8.6.3-b) | `apalike-ptbr.bst:853` concatena com `" e "` → PDF gera "(Aggarwal e Zhai, 2012)", "(Karl e Scherp, 2023)" | ❌ | Se o padrão ABNT for exigido (decisão de template): ajustar o `.bst`/`\bibpunct` ou migrar para `abntex2cite` — mudança global, ciclo próprio |
| Quatro ou mais autores | "convém indicar todos; permite-se… et al." (Manual §8.6.4) | apalike usa "et al." a partir de 3+ — ex. "(Ahmed et al., 2022)" | ✅ | — |
| Formato das referências | NBR 6023 / Manual §9: entrada "SOBRENOME, Nome." em caixa alta, ano no final do bloco de imprenta, "In:", "p." — exemplo do Manual: "HERSON, A. C.; HULLSAND, E. D. Conservas alimentícias… Zaragoza: Acribia, 1980." | Lista gerada em **estilo APA-like**: "Abe, N. e Mamitsuka, H. (1998). Query learning strategies… Em Shavlik, J. W., editor, Proceedings…, páginas 1–9. Morgan Kaufmann." (PDF, seção REFERÊNCIAS) — diverge em: caixa do sobrenome, posição do ano, conectivo "e" vs ";", "Em"/"páginas" vs "In:"/"p." | ❌ (condicionado à decisão de template) | Decisão G4.1 primeiro; se ABNT: trocar estilo bibliográfico (ex. `abntex2cite` alfabético) — retrabalho alto, planejar ciclo dedicado com DoD executável (grep no `.bbl`) |
| Espaçamento das referências | Espaço simples, linha em branco entre referências (Manual §3.2-c,d) | Herda espaçamento do documento; na defesa 1,5 (`ppginf.cls:338`) | ❌ (leve) | Junto com o ciclo de estilo bibliográfico |
| Unicidade das entradas | Uma referência por documento (NBR 6023; ordenação §9.3.1-c usa sufixo a/b só para obras distintas) | **Entrada duplicada**: `alsmadi2019shorttext` (`referencias.bib:113`) e `Alsmadi2019` (`referencias.bib:1183`) são o mesmo artigo → PDF lista "Alsmadi e Gan (2019a)" e "(2019b)" idênticos | ❌ | Unificar as chaves no `.bib` e nas citações (ciclo de texto; validar com fichamento, constituição da tese) |
| Sumário inclui REFERÊNCIAS | Título de seção pós-textual no sumário (Manual §4.17-i) | `tocbibind` com `nottoc,notlot,notlof` (`ppginf.cls:253`); PDF: "REFERÊNCIAS … 66" no sumário | ✅ | — |

## 6. Resíduos do template PPGInf (parecer R6, item 20 — `docs/parecer-ars-r6.md:124`)

Varredura: `grep -nE 'PPGInf|PPGINF|Inform[áa]tica|Maziero|Ci[êe]ncia da Computa'` em `ppginf.cls`, `principal.tex`, `packages.tex`, `0-iniciais/*.tex` + inspeção dos PDFs incluídos.

| # | Resíduo (evidência) | Natureza | Veredito | Correção proposta |
|---|---|---|---|---|
| 1 | `principal.tex:5` — comentário "documentos de pesquisa do PPGINF/UFPR" | Comentário de fonte (não aparece no PDF) | ⚠️ cosmético | Atualizar o cabeçalho do arquivo para PPGMNE no próximo ciclo que tocar `principal.tex` |
| 2 | `principal.tex:11` — "Produzido por Carlos Maziero (maziero@inf.ufpr.br)" | Comentário de fonte | ⚠️ cosmético | Manter crédito da classe, mas mover para nota de créditos; opcional |
| 3 | `principal.tex:108-132` — blocos `\descr` comentados citando "Programa de Pós-Graduação em Informática" | Comentários (o `\descr` ativo, linha 105, já é PPGMNE ✅) | ⚠️ cosmético | Apagar os blocos não usados |
| 4 | `ppginf.cls:35,41` — autoria/identificação da classe PPGInf | Cabeçalho da classe (licença exige manter, `ppginf.cls:32-33`) | ✅ manter | Nenhuma — é a atribuição da classe |
| 5 | `ppginf.cls:636` — `pdfcreator = {LaTeX, using PPGInf/UFPR class}` | **Metadado do PDF final** (visível nas propriedades quando compilado com `metadados`) | ⚠️ | Sem edição da classe: aceitável; se a migração de template ocorrer, some naturalmente |
| 6 | `0-iniciais/catalografica.pdf` — página inteira de instruções do PPGInf (gitlab maziero, `referencia.bct@ufpr.br`, "avisar a secretaria do PPGInf") | **Conteúdo que entraria na versão final** se compilada hoje com `final` | ❌ | Substituir pela ficha oficial (ver §2) |
| 7 | `0-iniciais/aprovacao.pdf` — placeholder do modelo | Idem, pós-defesa | ⚠️ | Substituir pelo termo oficial (ver §3) |
| 8 | `packages.tex:104` — `\usepackage{lipsum}` ("gera texto aleatório (para os exemplos)") | Pacote do template de exemplo, sem uso no texto | ⚠️ cosmético | Remover no próximo ciclo de formatação |

Sem ocorrências de "Ciência da Computação" em arquivos ativos. Os campos ativos
(`\descr`, `\field`, `\instit`) já estão corretos para o PPGMNE
(`principal.tex:79-105`).

## 7. Pendências administrativas (listadas sem investigação — responsabilidade do autor)

| Item | Fonte | Estado | Veredito |
|---|---|---|---|
| Lattes completo com toda a produção do período antes da defesa | FAQ PPGMNE (base §2.1) | Não verificável no repo | ⚠️ pendência do autor |
| Checklist de defesa aprovado pela coordenação antes do SIGA | FAQ PPGMNE (base §2.2) | Não verificável no repo | ⚠️ pendência do autor |
| Confirmação do template: `ppginf.cls` × modelo ABNT-UFPR | Base §3 (decisão pendente registrada; gate G4.1); Resolução 01/2021 e Portaria 12/2021-PPGMNE a solicitar à secretaria (base §7) | Decisão em aberto — **condiciona os vereditos das áreas 4 e 5** | ⚠️ pendência do autor (**prioritária**) |
| Ficha catalográfica oficial + CND da biblioteca + depósito via SIGA | SiBi depósito (base §1); instruções no próprio placeholder | Pendente | ⚠️ pendência do autor |
| Checklist de elementos do SiBi preenchido no depósito | Base §1 (depósito legal) | Pendente | ⚠️ pendência do autor |

---

## Resumo executivo

**Contagem:** **11 ❌** (não conforme) · **15 ⚠️** (pendência do autor/cosmético) · demais itens ✅.

Dos ❌: 4 são de severidade plena (ficha catalográfica placeholder; resumo 727
palavras; abstract 696 palavras; palavras-chave/keywords fora da NBR 6028) e
dependem só do autor/ciclos de texto; 4 são estruturais condicionados à decisão
de template (referências APA-like × NBR 6023; separador "e" × ";" nas citações;
espaçamento simples no modo `final`; entrada pré-textual no sumário — este
último corrigível já); 3 são leves de formatação (espaçamento do
resumo/citações longas/referências, fonte da citação longa).

### O que bloqueia o depósito (ordem de prioridade)

1. **Decisão de template (G4.1)** — `ppginf.cls` × modelo ABNT-UFPR, com a
   secretaria do PPGMNE (§7). É a pendência-raiz: define se as não
   conformidades das áreas 4-5 precisam de correção pontual ou de migração.
   Risco de retrabalho tardio de formatação se ficar para depois.
2. **Ficha catalográfica** — placeholder com instruções do PPGInf entraria na
   versão final (§2, §6.6). Solicitar a ficha oficial (com DOI da base) à
   biblioteca.
3. **Referências fora da NBR 6023 + citações parentéticas com "e"** (§5) — se
   a ABNT for exigida, é a maior frente de retrabalho (estilo bibliográfico
   inteiro); planejar ciclo dedicado com DoD executável.
4. **Resumo/abstract acima de 500 palavras e palavras-chave fora da NBR 6028**
   (§1) — não conformidade direta com o Manual §4.11, já convergente com o
   parecer R6 item 20; executar junto do ciclo humanize-02 para não editar a
   mesma superfície duas vezes.
5. **Versão `final` da classe usa espaço simples** (contra o 1,5 do Manual
   §3.2-b) e **sumário com entrada pré-textual** da declaração de IA (contra o
   Manual §4.17-c) — a primeira exige decisão junto com o item 1; a segunda é
   correção de uma linha num ciclo gateado.

Cosmético (não bloqueia): resíduos de comentários PPGInf, `lipsum`, imagem de
fundo da capa (confirmar aceitação), fonte/espaçamento de citação longa,
espaçamento 1,25 das listas.

**Achados novos em relação à base** (`docs/normas-ufpr-ppgmne-e-skills.md`):
extensão do resumo/abstract medida (727/696 palavras × máx. 500); formato das
palavras-chave; entrada pré-textual no sumário; espaço simples no modo `final`;
conformidade **efetiva** das margens via `bindingoffset`; caixa da citação
parentética **conforme** o Manual 2024 (a regra de MAIÚSCULAS é da norma
antiga); separador de autores e formato de referências como as divergências
reais; referência duplicada Alsmadi 2019a/2019b; inventário completo dos
resíduos PPGInf com linha.
