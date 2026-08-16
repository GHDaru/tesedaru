# ux-design.md — Páginas Grafo (grafo.html) e Bibliometria (bibliometria.html)

- **Ciclo**: 004-grafo-bibliometria · **Lane**: light · **Origem**: pedido
  direto do autor na sessão ("chame ao menos 3 especialistas em UX/UI e em
  bibliometria"). Consolida três pareceres independentes: `ux-semantics`
  (papel semântico), especialista em bibliometria acadêmica (o que é
  honesto de medir/rotular), especialista em visualização de dados (SVG
  inline sem biblioteca, mesmo padrão do burn-up de Plano).

## 1. Jornada de cada página

**Grafo**: exploração lenta, não escaneamento. O próprio instrumento
(`fichamentos/kg_template.html`) já assume isso — física de força que leva
segundos para convergir, filtros, painel de detalhe só após clique.
Pergunta que responde: "como este conceito/pilar/método se conecta ao
resto do aparato teórico, e quais artigos sustentam essa conexão?".
Visitantes: o autor (checando lastro de um conceito antes de escrever) e a
banca (avaliando amplitude/coerência do aparato teórico).

**Bibliometria**: dupla função — autodiagnóstico do autor ("estou
desequilibrado entre pilares? dependo demais de poucos veículos?") e
vitrine para a banca do RIGOR DA REVISÃO (não da pesquisa em si). Leitura
rápida por gráfico individual, mas a página inteira pede alguns minutos —
mais parecida com Plano (múltiplos KPIs + gráfico) que com Controle.

## 2. Grafo: janela para um instrumento externo, não um componente nativo

Decisão técnica: `<iframe>`, não reimplementação. `kg_template.html` tem
identidade visual própria (tokens de cor com outros nomes/matizes,
cabeçalho próprio, assume viewport inteiro) — é **outro sistema**, e a
moldura deve ser honesta sobre isso, não disfarçada de nativo:

- Sem `.card` ao redor (duplicaria moldura sobre moldura); só o
  `page-head` do site + uma frase de framing acima do iframe.
- Altura fixa relativa ao viewport (`calc(100vh - <cabeçalho>)`), nunca
  "altura de conteúdo" — mesmo princípio da raia limitada do ciclo 002:
  altura ~constante, não determinada pelo conteúdo.
- Largura: **rompe o `max-width:1080px` do `.wrap`** propositalmente —
  1080px existe para conforto de leitura de texto/tabela, não para um
  canvas de 527 nós em disposição de força.
- Tema: o iframe segue `prefers-color-scheme` de forma independente, com
  paleta de acento própria (não a verde do site) — aceito como sinal
  verdadeiro de "você entrou em outro instrumento", não escondido.
- **Escape hatch obrigatório**: link "abrir em nova aba" apontando pro
  arquivo standalone — serve acessibilidade (teclado/leitor de tela lidam
  mal com iframe) e fallback se o iframe falhar.
- Gap conhecido, registrado e não corrigido neste ciclo: o grafo não tem
  interação por teclado para selecionar nós, e distingue tipo de nó só por
  cor no canvas (rótulo textual só aparece nos filtros/painel de detalhe).
  Mesmo padrão do ciclo 002 (registrar gaps abertamente, não escondê-los).

## 3. Bibliometria vs. Resultados — a mesma vitrine não pode se repetir

Resultados é retrospectiva sobre a **investigação** (o que foi
descoberto/construído: achados, entregas, experimentos). Bibliometria é
retrospectiva sobre a **preparação** (como o terreno da literatura foi
coberto). Uma mede o produto, a outra mede o processo de revisão.

- Resultados responde "o que a tese prova"; Bibliometria responde "quão
  bem a tese leu o campo antes de provar".
- Bibliometria reusa literalmente os mesmos IDs/nomes de pilar (P1-P4) já
  em `resultados.json` — nunca redigita rótulos, para a banca cruzar
  "este pilar rendeu N achados (Resultados) apoiado em M referências
  (Bibliometria)" sem fricção de tradução.
- Frase de abertura fixa o escopo (mesmo padrão do parágrafo de Resultados):
  "Como a revisão de literatura desta tese foi conduzida — composição,
  atualidade e distribuição da bibliografia. Não é o que a pesquisa
  descobriu (isso está em Resultados) nem uma bibliometria do campo
  científico (não temos citação externa, afiliação ou busca sistemática
  — só o que este autor leu e citou)."

## 4. Honestidade dos números — decisão consolidada com o especialista de bibliometria

**O que fica fora deste ciclo, com razão registrada** (parecer do
especialista de bibliometria acadêmica, ver `qa-report.md` para o parecer
completo): lei de Lotka, lei de Bradford, h-index/proxy via
`total_ocorrencias`, mapa temático por co-ocorrência de palavras-chave.
Todos pressupõem um levantamento sistemático de campo — o que existe aqui
é uma bibliografia curada de UMA tese (378 itens, seleção editorial
deliberada do autor), não uma amostra do campo científico. Aplicar essas
técnicas aqui emprestaria autoridade estatística que os dados não
sustentam.

**O que entra, com o rótulo de escopo embutido no próprio texto visível
(nunca só em tooltip/rodapé — mesma régua de "rastreabilidade sem nota de
rodapé" já em Resultados)**:

| Gráfico | Rótulo de escopo (sempre visível) |
|---|---|
| Publicações por ano | "quando a literatura consultada nesta tese foi publicada" (não "tendência do campo") |
| Top 10 autores | "autores mais presentes NESTA bibliografia — não citação externa ao campo" |
| Top 10 veículos | "veículos mais presentes nesta bibliografia" |
| Top 10 mais citadas | "frequência de citação DENTRO DO TEXTO da tese" (não impacto externo) |
| Cobertura de fichamento | "quanto da bibliografia já foi processada pelo fichamento" |
| Distribuição por pilar | "referências fichadas por pilar (P1-P4) — uma obra pode contar em mais de um pilar" |

O grafo de relações do `kg.json` (extends/builds_on/contradicts/
compares_with) é chamado de **"mapa de argumentação"** ou **"grafo de
conhecimento fichado"** na página Grafo — nunca "rede de co-citação"
(termo técnico que pressupõe inferência estatística automática sobre uma
população grande de documentos citantes; aqui é julgamento humano direto
de conteúdo, categoria diferente e mais confiável, mas com nome próprio).

**Título da página**: "Bibliometria" no menu (termo familiar, curto,
cabe na sidebar); a precisão do escopo vem na frase de abertura (§3), não
no rótulo do menu — mesmo padrão de "Resultados" (rótulo curto no menu,
nuance na página).

## 5. Reuso vs. papel novo

**Reutilizados sem alteração**: `.card`, `.kpi`/`.kpi.hero` (linha de
agregados no topo: 378 referências · 152 citadas · 152 fichadas),
`.pill.feito`/`.pill.pendente` (badges sim/não com glifo+palavra),
`.achado`/`.achado-numero`/`.achado-evidencia` (anatomia de "afirmação +
número em destaque + evidência menor", estendida dos gráficos), técnica
de SVG inline + tooltip do burn-up de Plano (grid em `var(--grid)`, path/
barra em `var(--accent)`), `<details>/<summary>` para "ver dados em
tabela" sob cada gráfico (mesmo papel de "Dados da série" em Plano),
`.progress`/`.progress-bar` (barra de cobertura de fichamento).

**Genuinamente novo**:
- **"Barra de ranking"** (rótulo + barra horizontal proporcional ao
  máximo do próprio conjunto + valor sempre visível, nunca só hover) —
  para top-10 de autor/veículo/mais-citadas. Construída a partir do
  primitivo `.progress` já existente, não de uma técnica nova.
- **"Distribuição por pilar"** — barra segmentada por pilar, cores e
  nomes herdados de `resultados.json`.
- **"Janela de instrumento" (iframe)** — catalogado como papel novo
  reutilizável (pode se repetir se outro instrumento standalone entrar no
  site no futuro): `page-head` do site → frase de framing → iframe com
  `title` descritivo, altura relativa ao viewport, sem `.card` → link
  "abrir em nova aba" sempre visível.

## 6. Acessibilidade

- `role="img"` + `aria-label` descritivo em todo SVG novo (mesmo padrão
  do burn-up).
- Valor numérico de cada barra de ranking sempre em texto visível, nunca
  só no comprimento da barra ou em tooltip — resolve teclado/leitor de
  tela/touch ao mesmo tempo, sem precisar de interação.
- `<title>` SVG nativo em cada barra como reforço (não como único canal).
- Gráfico de publicações por ano ganha uma tabela HTML equivalente dentro
  de `<details>`, mesma técnica já usada na série de prontidão de Plano.
- iframe do Grafo: `title` obrigatório + link "abrir em nova aba" como
  rota alternativa para quem não consegue operar o instrumento embutido.
- Nenhuma alegação de escopo (§4) depende só de cor — texto é a fonte de
  verdade.

## 7. Decisão de dados (implementação)

- `referencias.json` já tem `ano`/`autores`/`venue`/`total_ocorrencias` —
  suficiente para os 4 primeiros gráficos sem tocar
  `compute-referencias.py`.
- Distribuição por pilar: computada a partir de `fichamentos/kg.json`
  (arestas tipo `pillars`) no momento do build — um agregado pequeno
  embutido na página, não o grafo inteiro (265KB) duplicado.
- Cobertura de fichamento: já existe em `referencias.json`
  (`fichado`/`pdf` por entrada) — só precisa de uma contagem.
- Nenhum campo novo inventado (ex.: "tipo de fonte" a partir de heurística
  sobre `venue`) — decisão do especialista de visualização de dados,
  ecoada pelo de bibliometria: não afirmar o que não está fundamentado
  nos dados (constituição da tese, "afirmações fundamentadas").
