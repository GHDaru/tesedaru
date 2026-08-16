# Parecer da banca — Auditoria do `referencias.bib` contra fontes primárias

Data: 2026-08-16 · Agente: banca (claim `20260816-1725_banca_todos_aviso_claim-auditoria-bib`)
Método: 2 verificadores em contextos separados — A: as 41 chaves citadas com
year≥2022, uma a uma, contra arXiv/ACL Anthology/DBLP/DOI; B: mapa completo de
duplicatas (369 entradas), amostra de 30 clássicos pré-2022, varredura
estrutural. Read-only: nenhum arquivo do repositório foi alterado. Escopo:
citações da tese (fora de `artigos/`); os artigos herdam as mesmas correções.

## Veredito executivo

O `referencias.bib` tem duas populações distintas: **os clássicos estão
sólidos** (26/30 OK na amostra; erros restantes são de venue/páginas) e **a
literatura da era LLM está contaminada**: das 41 chaves pós-2022 citadas, 15
têm metadados errados e 3 não correspondem a obra existente. O padrão dos
casos graves é o de referência gerada por modelo sem validação: título real,
autores inventados ou deturpados, arXiv ID de outro paper. Somam-se 17 títulos
duplicados (a tese cita as duas variantes em 6 casos, duplicando entradas no
PDF) e 2 notas de trabalho de LLM que vazam para as Referências impressas.
**Nada disso exige experimento; tudo é corrigível em um ciclo com lock no
`referencias.bib` + repontuação de `\cite` na prosa.**

## 1. Graves — fabricação ou obra inexistente (corrigir SEMPRE antes da banca)

| Chave | Problema | Correção |
|---|---|---|
| `Su2023` (+ dupl. `FreeAL2023`) | Título do FreeAL com autores fabricados ("Bo Su, Jun Guo...") e páginas erradas; campo residual `key={FreeAL2023}` | Autores reais: **Xiao, Ruixuan et al.**, EMNLP 2023, pp. 14520–14535, DOI 10.18653/v1/2023.emnlp-main.896; renomear chave para `Xiao2023FreeAL`; matar `FreeAL2023` |
| `Tian2023` | Autores fabricados + arXiv 2402.11753 é OUTRO paper (ArtPrompt/jailbreak) | A tese cita em `2-fundam:615` para "confiança auto-reportada dos LLMs tende ao excesso": a obra pretendida é **Tian et al., "Just Ask for Calibration", EMNLP 2023** (DOI 10.18653/v1/2023.emnlp-main.330) — bate com chave e alegação; substituir metadados por ela (confirmar no gate) |
| `Margatina2023` | Obra inexistente; arXiv ID de paper de detecção 3D; citada em `2-fundam:568` para "sistemas híbridos humano-LLM" | Obra real de Margatina 2023: "Active Learning Principles for In-Context Learning with LLMs" (Findings EMNLP 2023, DOI 10.18653/v1/2023.findings-emnlp.334) — verificar se sustenta a alegação da linha 568; senão, recitar (Rouzegar2024) |
| `Wu2022` | Inexistente; arXiv ID de paper de matemática | Redirecionar as citações para `zhang-etal-2022-survey` (survey real de AL-NLP, já no bib) |
| `Ahmed2023` | Inexistente; o artigo Information 14(4):215 é de outros autores | Se o assunto é topic modeling de texto curto: **Fan, Shi, Yuan, JIFS 45(2):1971–1990, 2023**, DOI 10.3233/JIFS-223834 |
| `Diao2023` | Autores fabricados ("Siqi Diao, Pengwei Wang...") | Reais: **Shizhe Diao, Pengcheng Wang, Yong Lin, Rui Pan, Xiang Liu, Tong Zhang** (ACL 2024, arXiv:2302.12246) |
| `Fromme2022` | 1º autor inexistente ("Lisa Fromme") | Reais: **Wertz, Mirylenka, Kuhn, Bogojeska**, LREC 2022, pp. 4597–4605; renomear para `Wertz2022` |
| `Bayer2024` + `activellm2024` + `Bayer2024ActiveLLM` | Triplicata; 2 chaves com autores fabricados ("Manuel Bayer, Christoph Reuter"); todas omitem o coautor Justin Lutz | Unificar em `Bayer2024ActiveLLM`: **Markus Bayer, Justin Lutz, Christian Reuter**, TACL v.14, pp. 1–22, 2026, DOI 10.1162/TACL.a.63 |
| `Xia2025` | 6 nomes deturpados ("Yuqing Xia, Subhabrata Mukherjee...") | Reais: **Yu Xia, Subhojyoti Mukherjee, Zhouhang Xie, Junda Wu, Xintong Li, Ryan Aponte** et al. (Findings ACL 2025, arXiv:2502.11767); remover o `note` de LLM |
| `Zhang2025` + `Zhang2025LLMAL` | Duplicata com primeiros nomes errados ("Yang Zhang, Shogo Takada") | **Yejian Zhang, Shingo Takada** (arXiv:2502.16892); unificar; remover o `note` de LLM |
| `Deng2023fedal` | arXiv ID de outro paper; ano errado | arXiv:2406.11310, year=2024 |
| `Reusens2024` | DOI de outro artigo; faltam 3 coautores | ESWA v.254, art. 124302, DOI 10.1016/j.eswa.2024.124302; autores completos incl. Verbeke, vanden Broucke, Baesens |
| `Yusuf2023` (não citada na tese) | Autores fabricados; duplicata da citada `Riyanto2023Comparative` (correta) | Matar |
| `Jung2021` (não citada) | Autor/venue não localizáveis; a obra real é `Nti2021` (correta, já no bib) | Matar |

Patches BibTeX campo a campo: relatório do verificador A (transcrito no ciclo;
os essenciais estão na tabela). Erros leves adicionais: `Ahmed2022`
(year→2023), `Aliero2023` (pages 44–55 + DOI), `Wei2022` (faltam Ichter e
Xia), `Guo2025Deuce` (year→2024, TACL v.12), `Kholodna2024`/`Rouzegar2024`/
`Romberg2025`/`Schick2023`/`Diao2023` (atualizar preprint→versão publicada).

## 2. Duplicatas — 17 títulos, 37 chaves, 20 a matar

Grupos em que a tese cita AS DUAS variantes (repontuar `\cite` antes de matar):
1. `zhang2022surveyAL` → manter `zhang-etal-2022-survey`
2. `Bayer2024` → manter `Bayer2024ActiveLLM` (corrigida)
3. `Zhang2025LLMAL` → manter `Zhang2025` (corrigida)
4. `devlin2019bert` → manter `Devlin2019`
5. `alsmadi2019shorttext` → manter `Alsmadi2019`
6. `song2014shorttext` → manter `Song2014`

Demais grupos (matar a órfã, manter a completa): Ein-Dor2020→EinDor2020 ·
Sener2017→Sener2018 · Settles2010→Settles2009 · Settles2008a/b→Settles2008 ·
FreeAL2023→Su2023(=Xiao2023FreeAL) · Yusuf2023→Riyanto2023Comparative ·
Jung2021→Nti2021 · Ash2019→Ash2020 · Souza2023→Souza2022Embedding ·
Bojanowski2016→Bojanowski2017 · Bates2022→Karl2023 · activellm2024→(grupo 2).

## 3. Clássicos e estrutura

- Pré-2022 (30 verificadas): 26 OK. Corrigir: `Guyon2011ALC` (workshop da
  AISTATS **2010**, proc. JMLR W&CP v.16/2011), `Kohavi1995` (pp. 1137–1145),
  `Pennington2014` (typo "Empiricial" + volume espúrio), `Bojanowski2017`
  (@article, TACL v.5).
- **Remover os 2 `note` de LLM** (`Xia2025`, `Zhang2025`) — vazam para o PDF.
- Remover `key = {FreeAL2023}` residual (l.699) e o separador órfão (l.213).
- 34 entradas citadas com year≥2020 sem DOI/URL — adicionar (ACL Anthology/
  arXiv, mecânico).
- 217/369 chaves nunca citadas na tese: podar para arquivo próprio dos
  artigos, ou manter e aceitar bibliografia só-citadas via BibTeX (o estilo já
  imprime só as citadas; a poda é higiene, não bloqueio).

## 4. Ordem de aplicação (evita editar a mesma superfície duas vezes)

1. **Ciclo bib-fix** (lock em `referencias.bib`): aplicar patches da §1 +
   matar duplicatas da §2 + estrutura da §3. No MESMO ciclo, repontuar os
   `\cite` dos 6 grupos duplos e das chaves renomeadas (mecânico, por sed
   auditado; toca prosa mas não muda texto corrido).
2. Verificação da banca (re-run do script de DoD abaixo).
3. **Só então** humanização R1 dos capítulos afetados (evita rebase duplo).
4. Conferir alegação×obra nas linhas onde a obra mudou: `2-fundam:568`
   (Margatina), `2-fundam:615` (Tian), `2-fundam:327/648` (Wu2022/Ahmed2023).

## 5. DoD verificável do ciclo de correção

- Script resolve cada DOI/arXiv ID das chaves citadas e compara título+autores
  (fuzzy) — 0 divergências.
- 0 títulos duplicados (normalizados) no bib; 0 campos `note` com texto de
  trabalho; 0 campos `key=`; toda chave citada com year≥2020 tem DOI ou URL.
- Compilação 0 erros / 0 warnings de BibTeX; nº de entradas nas Referências
  do PDF = nº de obras distintas citadas.

## Adendo (17:40 UTC) — achados do revisor1 incorporados + lote suspeito

Aviso `20260816-1727_revisor1_banca` (validação independente na rodada
fichar-vizinhos): confirma FreeAL fabricada em duplicata (§1) e Sener2017/2018
(§2), e acrescenta duas suspeitas, ambas verificadas aqui como **nunca citadas
na tese** (0 ocorrências — órfãs):

- `Hacohen2023` (l.551): autor "Gideon Hacohen" — o pesquisador da linha é
  **Guy** Hacohen; venue TPAMI a conferir. Matar (órfã) ou corrigir no ciclo.
- `Yu2022` (l.577): "Yu, Meng; Chen, Xuezhe; Chen, Qingqing", não localizada
  na Anthology pelo revisor1. Matar (órfã).

Achado adicional da banca ao inspecionar o trecho: `Yu2022` pertence a um
**bloco de entradas em formato de linha única** (l.577–581) que inclui
`Zhang2020` ("Zhang, Zixuan and Chen, Lawrence" — padrão de fabricação) —
tratar o bloco inteiro como lote suspeito de geração automática e verificar
cada entrada dele no ciclo bib-fix, mesmo as órfãs.

Coordenação do fix: o revisor2 detém o lock de `referencias.bib` adicionando
as 9 chaves novas verificadas (Zhang2023LLMaAA, Wang2021GPT3, Pangakis2023,
Hacohen2022TypiClust, Yu2023Patron, Bengar2022, Farquhar2021, Kossen2021,
Schroder2022). O ciclo bib-fix deste parecer deve REBASEAR sobre esse merge —
as 9 entradas novas já chegam validadas contra fonte primária e não colidem
com os patches da §1.
