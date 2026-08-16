# Rodada 3 — Normas UFPR/PPGMNE e varredura de skills

Data: 2026-08-16 · Parte da sessão de revisão crítica pré-banca (rodadas 1-5).
Fontes primárias consultadas nesta data; links ao final.

## 1. Normas SiBi/UFPR — estrutura da tese (formato tradicional)

Fonte: "Orientação para normalização de trabalhos acadêmicos" (Comissão de
Normas SiBi/UFPR, atualização 12/12/2017) + página de depósito legal.

Elementos obrigatórios × estado do repositório (`principal.tex`):

| Elemento (obrigatório) | Exigência SiBi | Estado no repo | Veredito |
|---|---|---|---|
| Capa | material flexível ou rígido; espiral não aceito | gerada pelo template | ✅ (física: decisão de impressão) |
| Folha de rosto | obrigatória | gerada pelo template | ✅ |
| Ficha catalográfica | verso da folha de rosto; **solicitar à biblioteca do programa**; se dados em BDC/UFPR, incluir DOI na ficha | `0-iniciais/catalografica.tex` placeholder | ⚠️ pedir ficha oficial à biblioteca (a base tem DOI — incluir) |
| Termo/folha de aprovação | **sem assinatura de todos os membros da banca não é aceito** | `0-iniciais/aprovacao.tex` | ✅ estrutura (assinaturas = pós-defesa) |
| Resumo + palavras-chave (PT) | obrigatório | `resumo.tex` | ✅ (conferir palavras-chave explícitas) |
| Resumo + palavras-chave (língua estrangeira) | obrigatório | `abstract.tex` | ✅ (idem) |
| Sumário | obrigatório | `\tableofcontents` | ✅ |
| Referências | obrigatório | `referencias.bib` (369 entradas) | ✅ |

Opcionais presentes: dedicatória, agradecimentos, listas de figuras/tabelas,
siglas, símbolos, apêndices A1-A7. Elemento **extra fora do quadro SiBi**:
`declaracao-ia.tex` (entre abstract e listas) — posição a confirmar com o
programa; não há vedação, mas não é elemento normalizado.

Depósito legal (pós-defesa): PDF único via SIGA; cópia impressa não é mais
obrigatória (Res. 32/17-CEPE); checklist de elementos do SiBi deve ser
preenchido; ficha catalográfica oficial obrigatória.

## 2. Requisitos administrativos PPGMNE (FAQ do programa)

1. **Lattes completo** com toda a produção intelectual do período antes da
   defesa (artigos, produção técnica, reconhecimentos).
2. **Checklist de defesa aprovado pela coordenação** ANTES de o orientador
   abrir a solicitação no SIGA.
3. Solicitação de defesa via SIGA pelo orientador, com **link do Lattes e
   H-index de todos os membros da banca** no campo Observações.
4. Composição da banca homologada pelo COMENE (portarias específicas).
5. O FAQ **não** especifica template/formatação — remete a portarias
   (ex.: Resolução 01/2021), que devem ser conferidas com a secretaria.

## 3. Risco de template identificado

O blog do PPGMNE aponta, desde 2008, um **modelo LaTeX ABNTeX "padrão UFPR"**
(Cassaredo, Carvalho e Kavamura; depois ABNTeX2/ufpr-abntex). A tese usa
`ppginf.cls` (template do PPGInf/UFPR — Informática, prof. Maziero), com dados
do PPGMNE. Tipograficamente os dois divergem (estilo de capa, citações
autor-data via natbib × ABNT NBR 10520).

**Decisão pendente (autor + orientador + secretaria):** confirmar se o PPGMNE
aceita o formato do `ppginf.cls` ou exige o modelo ABNT UFPR. Risco de retrabalho
de formatação tardio se não confirmado antes do depósito. Registrar a resposta
em `docs/records/decisoes.jsonl`.

## 4. Varredura de marketplace (skills/plugins)

| Busca | Resultado |
|---|---|
| Skills "academic writing/thesis/research/peer review" | **nenhuma** skill disponível no catálogo da conta |
| Plugins do marketplace (knowledge-work-plugins) | nada acadêmico: catálogo é de vendas/marketing/bio/SEO/design |
| "Maestro" (organizador de ciclos) | **não existe** como plugin/skill instalado ou disponível |

Consequência prática:

- O toolkit real para escrita é o que já está em mãos: skill pessoal
  `humanizer` (anti-sinais de IA, calibrada pelo ADR 0001), o guia local
  `docs/skill-documento-cientifico.md` (307 linhas, destilado das rodadas
  R1-R5) e a skill `fichamento` do repo.
- O "maestro" referido pelo autor (mapa de gates, ciclos com gate humano —
  citado no ADR 0001) não está implantado neste ambiente; o que existe é o
  processo manual (checklist.md + diario.md + records JSONL). Se desejado
  como skill executável, deve ser criado localmente (ex.: com `skill-creator`)
  em `.claude/skills/maestro/` — candidato a trabalho pós-sessão.

## 5. Varredura ampliada — skills.sh e diretórios abertos (2ª passada, 16/08)

Executada com o CLI `npx skills find` (skills.sh, o mesmo canal do caminho C de
instalação do Maestro) e busca web em diretórios (SkillsMP, explainx, GitHub).

### Skills relevantes encontradas

| Skill (`owner/repo@skill`) | Instalações | O que é / relevância para a tese |
|---|---|---|
| `imbad0202/academic-research-skills@academic-paper-reviewer` | 7,4K | **A ARS** — a mesma skill de revisão por pares simulada que gerou os pareceres R1–R5. Instalável para reproduzir o re-review localmente |
| `imbad0202/academic-research-skills@academic-paper` / `@academic-pipeline` / `@deep-research` | 8,1K / 5,3K / 5,7K | família completa: research → write → review → revise → finalize |
| `devalissu/pesquisador-br-skill@pesquisador-br` | 8 | **PT-BR/ABNT**: artigos, dissertações e teses por área CAPES. Pouca tração (auditar conteúdo antes de adotar) |
| `devalissu/pesquisador-br-skill@tcc-abnt` / `@revisor-pares-br` | 11 / 6 | ABNT NBR 14724 (foco TCC) e revisão por pares em PT-BR |
| `blader/humanizer@humanizer` | 4,3K | a base da skill `humanizer` já em uso (calibrada pelo ADR 0001) |
| `santifs/thesis-writing-skill` | — | teses empíricas (escopo→estrutura→rascunho→revisão), agnóstica de formato; inglês, sem ABNT |
| `davila7/claude-code-templates@scientific-writing` | 1,8K | escrita científica genérica |
| `k-dense-ai/scientific-agent-skills@scientific-writing` | 1,4K | idem, de suíte científica maior |
| `bahayonghang/academic-writing-skills@latex-paper-en` | 4,8K | 12 módulos LaTeX (compilação, bibliografia, clareza, fluxo lógico, figuras) |
| `lingzhi227/agent-research-skills@latex-formatting` | 1,7K | formatação LaTeX |
| `sickn33/agentic-awesome-skills@professional-proofreader` | 424 | proofreading profissional (candidata ao passe final G6.6) |

### Leitura e recomendação

1. **Instalar** `academic-paper-reviewer` (ARS) no repo: dá reprodutibilidade
   local ao instrumento que gerou os R1–R5 (hoje o parecer é externo à sessão).
2. **Avaliar com cautela** a família `pesquisador-br` (única opção ABNT/PT-BR
   do diretório): tração baixíssima; auditar o SKILL.md antes de qualquer uso.
3. **Não substituir** a `humanizer` local: a upstream (`blader/humanizer`) é a
   mesma base, e a versão calibrada (ADR 0001) é superior para PT-BR acadêmico.
4. Regra de nascimento do Maestro se aplica: skill só entra com dor recorrente
   comprovada — proofreader e latex-* ficam como candidatas para o G6.6, não
   instalação especulativa.

## 6. Manual de Normalização UFPR (achado da 2ª passada)

- **Manual de Normalização de Documentos Científicos (ABNT), Ed. UFPR, 2022**
  — 411 pp., download livre:
  https://acervodigital.ufpr.br/handle/1884/73330
- **Edição atualizada 2024** (Acervo Digital UFPR):
  https://acervodigital.ufpr.br/xmlui/bitstream/handle/1884/88892/Manual_de_Normalizacao%202024.pdf
- É a referência normativa completa (citações, referências, apresentação
  gráfica) que detalha o quadro de estrutura da §1. Usar a edição 2024 no
  gate G3.1 da rodada 5.

## 7. Normas internas PPGMNE (achado da 2ª passada)

- **Resolução 01/2021** e **Portaria 12/2021-PPGMNE** regulamentam mestrado e
  doutorado (créditos, prazos, Trabalho Individual). O texto completo não está
  público no site — solicitar à secretaria (cesec@ufpr.br) junto com a
  confirmação do template (gate G4.1).

## 8. Fontes

- SiBi/UFPR — Orientações para normalização: https://bibliotecas.ufpr.br/servicos/normalizacao/
- SiBi/UFPR — Quadro de estrutura (PDF): https://bibliotecas.ufpr.br/wp-content/uploads/2022/01/normas_estrutura.pdf
- SiBi/UFPR — Depósito de teses: https://bibliotecas.ufpr.br/servicos/teses-dissertacoes/
- SiBi/UFPR — Novo manual de normalização (2022): https://bibliotecas.ufpr.br/2022/02/novo-manual-de-normas-da-ufpr/
- PPGMNE — FAQ: https://www.prppg.ufpr.br/site/ppgmne/pb/faq/
- PPGMNE — Modelo LaTeX padrão UFPR (blog do programa): http://ppgmne.blogspot.com/2009/12/modelo-latex-de-dissertacao-padrao-ufpr.html
- PPGInf/UFPR — modelo LaTeX (origem do ppginf.cls): https://wiki.inf.ufpr.br/maziero/doku.php?id=software:modelo_latex_do_ppginf_ufpr
- Editora UFPR — anúncio do Manual de Normalização: https://www.editora.ufpr.br/portal/manual-de-normalizacao-de-documentos-cientificos-esta-disponivel-para-download/
- skills.sh (diretório do padrão `npx skills`): https://skills.sh/
- academic-research-skills (ARS): https://github.com/imbad0202/academic-research-skills
- thesis-writing-skill: https://github.com/santifs/thesis-writing-skill
- pesquisador-br-skill (ABNT/PT-BR): https://skills.sh/devalissu/pesquisador-br-skill/tcc-abnt
- latex-document-skill: https://github.com/ndpvt-web/latex-document-skill
