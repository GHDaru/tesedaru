# Conformidade UFPR/PPGMNE — relatório consolidado (duas auditorias independentes)

**Data:** 2026-08-16 · **Escopo:** LEVANTAMENTO — nenhum arquivo da tese foi
editado; as correções são ciclos de texto gateados. · **Item do plano:**
`encerramento.normas-ufpr`.

Este documento **consolida duas auditorias feitas em paralelo e sem contato**
(colisão de trabalho entre agentes, hoje transformada em verificação cruzada
pelo §6 do protocolo de coordenação):

| Origem | Arquivo (preservado, não substituído) | Recorte |
|---|---|---|
| revisor2 | `docs/relatorio-nao-conformidades-ufpr.md` (190 linhas) | Manual de Normalização UFPR **2024 lido na fonte**, cláusula a cláusula; ficha catalográfica; resíduos do template PPGInf; separador e caixa das palavras-chave; duplicata `Alsmadi` |
| revisor1 | `docs/relatorio-conformidade-ufpr-ppgmne.md` (238 linhas) | 40 itens tabelados por área; **numeração de seções**, **pós-textuais**, **metadados institucionais**; 7 pontos a confirmar com a secretaria; plano de correção em 5 ciclos |
| — | `docs/normas-ufpr-ppgmne-e-skills.md` | levantamento anterior de FONTES (base das duas) |

Onde as duas auditorias examinaram o mesmo item, **os vereditos coincidem** —
convergência independente, não cópia. O que segue é a união dos dois recortes,
com a origem de cada achado identificada.

## 1. Bloqueantes de depósito (consenso das duas auditorias)

| # | Achado | Evidência | Origem |
|---|---|---|---|
| B1 | **Ficha catalográfica é placeholder** — `catalografica.pdf` é a página de instruções do template PPGInf (contatos do PPGInf, gitlab do Maziero) e entraria na versão final | `0-iniciais/catalografica.tex:7` | ambas |
| B2 | **Termo de aprovação é placeholder** — sem assinaturas não é aceito pelo SiBi | `0-iniciais/aprovacao.tex:7` | ambas |
| B3 | **Resumo com 727 palavras** — Manual §4.11-d exige 150–500 | `0-iniciais/resumo.tex:3` | ambas |
| B4 | **Abstract com 696 palavras** — mesmo critério (Manual §4.12) | `0-iniciais/abstract.tex` | ambas |
| B5 | **Compilação em modo `defesa`** suprime ficha/aprovação/dedicatória/agradecimentos; o depósito exige o modo `final` | `principal.tex:31` × `:37`; `ppginf.cls:566-574` | r1 (r2 registra como pendência) |

B3/B4 coincidem com o item 20 do parecer R6 ("resumo ~800→~500") — executar
junto do ciclo humanize-02 para não editar a mesma superfície duas vezes.

## 2. Não conformidades de formatação (Manual UFPR 2024 §3)

| # | Achado | Evidência | Origem |
|---|---|---|---|
| F1 | **Entrelinha simples no modo `final`** — Manual §3.2-b exige 1,5 no texto; a classe usa `\singlespacing` na versão de depósito | `ppginf.cls:335-336` | ambas |
| F2 | **Resumo/abstract sem espaço simples** — Manual §3.2-c; o ambiente herda 1,5 | `ppginf.cls:530-545` | r2 |
| F3 | **Citação longa em `\small` (≈11pt)** — Manual §3.1-d pede fonte 10 e espaço simples | `ppginf.cls:310,323` | r2 |
| F4 | **Palavras-chave separadas por ponto e com iniciais maiúsculas** — Manual §4.11-h pede ponto e vírgula e minúsculas | `principal.tex:62` (PT) e `:63` (EN) | r2 |
| F5 | **Declaração de IA injeta entrada pré-textual no sumário** — Manual §4.17-c,d / NBR 6027: o sumário começa no primeiro elemento textual | `0-iniciais/declaracao-ia.tex:5` | r2 |
| F6 | **Separador de autores na citação** — ABNT usa ponto e vírgula; o `.bst` concatena com " e " | `apalike-ptbr.bst:853` | r2 |
| F7 | **Formato das referências apalike-ptbr × NBR 6023** — caixa do sobrenome, posição do ano, "Em"/"páginas" vs "In:"/"p." | estilo em `packages.tex:80` | ambas |
| F8 | **Entrada duplicada no bib**: `alsmadi2019shorttext` × `Alsmadi2019` geram "(2019a)/(2019b)" idênticos | `referencias.bib:113` e `:1183` | r2 (converge com a auditoria de bib da banca) |
| F9 | **`\cite` puro** nos capítulos (funciona por remapeamento, mas o próprio template desaconselha) | `2-fundam/texto.tex:33,44,46…` | r1 |

F6/F7 só se tornam obrigatórios se o PPGMNE exigir ABNT estrito — ver §4.

## 3. Áreas verificadas e CONFORMES (evita retrabalho)

Auditadas pelo revisor1 e sem achado — não precisam de ciclo:

- **Numeração de seções e títulos** (§2.5 do relatório r1): indicativo separado por
  espaço sem pontuação; capítulo em maiúsculas/negrito em página nova; secundária
  maiúscula, terciária só a inicial; títulos sem indicativo centralizados;
  `secnumdepth=3` respeita o limite quinário.
- **Elementos pós-textuais** (§2.7): referências presentes; apêndices A1–A7 com
  numeração correta; glossário/anexos/índice ausentes e opcionais.
- **Metadados institucionais da folha de rosto** (§2.8): área de concentração
  (Programação Matemática), natureza do trabalho, instituição por extenso,
  orientador, local e ano — todos conformes.
- **Título "REFERÊNCIAS" e inclusão no sumário** (§2.6): conforme.

Resíduos do template PPGInf (r2, §6 do relatório): 8 ocorrências mapeadas —
duas com efeito no PDF final (B1 e o `pdfcreator` da classe), as demais
cosméticas em comentários.

## 4. Pendências que dependem de humano (não decidíveis no repositório)

Prioritária: **confirmar o template** (`ppginf.cls` × modelo ABNT-UFPR do
PPGMNE) com a secretaria — essa resposta condiciona F6/F7 e o esforço do
ciclo de referências. As demais: ficha catalográfica junto à Biblioteca (com
DOI da base, se aplicável); termo de aprovação pela secretaria pós-defesa;
posição da declaração de IA (elemento não normalizado — sugestão conservadora:
apêndice); espaçamento aceito na versão final; margem efetiva com
`bindingoffset` conferida no PDF em modo `final`/`oneside`; formato tradicional
× alternativo por artigos (há `artigos/` derivados); e os administrativos do
FAQ PPGMNE (Lattes completo, checklist de defesa antes do SIGA).

## 5. Ordem de execução sugerida (ciclos gateados, nenhum executado)

1. **Insumos externos** (não auto-contido): pedir ficha à Biblioteca e, pós-defesa,
   o termo assinado; trocar a compilação para `final`. → resolve B1, B2, B5.
2. **Resumo/abstract ≤500 palavras**, junto do ciclo humanize-02 (`fight-the-pile-up`).
   DoD: `wc -w` ≤ 500 nos dois. → resolve B3, B4.
3. **Formatação da classe** (lane infra, toca `ppginf.cls`/`packages.tex`):
   entrelinha 1,5 no modo final, espaço simples em resumo/abstract/citação longa,
   fonte 10 na citação longa. → resolve F1, F2, F3.
4. **Pré-textuais de texto**: palavras-chave no formato ABNT, remover o
   `\addcontentsline` da declaração de IA, preencher/remover dedicatória e
   agradecimentos. → resolve F4, F5.
5. **Referências** (só após a resposta do §4): estilo aderente à NBR 6023 e
   deduplicação de chaves — coordenar com o ciclo bib-fix da banca, que já tem
   patch por entrada. → resolve F6, F7, F8, F9.

## 6. Placar consolidado

- **5 bloqueantes de depósito** (§1).
- **9 não conformidades de formatação** (§2), das quais 4 condicionadas à
  decisão de template.
- **4 áreas inteiras verificadas e conformes** (§3).
- **7 pontos a confirmar com secretaria/Biblioteca + 5 administrativos** (§4).
- Contagens originais preservadas nos relatórios-fonte: r2 = 11 ❌ / 15 ⚠️;
  r1 = 40 itens, 25 conformes, 6 não conformes, 7 a confirmar. As diferenças
  são de granularidade (o que r2 conta como um item, r1 desdobra em linhas de
  tabela e vice-versa), não de veredito.
