# Lote 4 — verificação independente do bib-fix (banca)

Branch verificada: `bibfix/lotes` @ 7b039c1 (lotes 0-3 aplicados por revisor1 e
revisor2). Método: checagens estruturais na fonte + verificação de 6 entradas
suspeitas e amostra de controle de 5 corrigidas, todas contra fonte primária
(ACL Anthology, MDPI, DBLP, arXiv, MIT Press), por verificador que não
participou da execução nem da auditoria original.

## Veredito: REPROVADO para gate — falta cobertura, não qualidade

O que foi corrigido, foi corrigido bem: a amostra de controle saiu **5/5
correta** contra fonte primária (Xiao2023FreeAL, Tian2023, Margatina2023,
Wertz2022, Bayer2024ActiveLLM). O problema é que **entradas defeituosas do meu
parecer não foram tocadas**, e a varredura de vizinhança achou mais uma
fabricação que ninguém tinha visto.

## 1. Estrutura — PASSA em tudo

| Critério | Antes | Agora |
|---|---|---|
| Títulos duplicados | 17 | **0** |
| Campos `note` com anotação de LLM | 2 | **0** |
| Campos `key=` residuais | 1 | **0** |
| Citações órfãs (chave inexistente) | — | **0** de 146 |
| Citações dos Caps. 1-2 resolvendo | — | **131/131** |
| Entradas | 378 | 354 (24 mortas) |

Remoções conferidas: `Su2023`→`Xiao2023FreeAL`, `Fromme2022`→`Wertz2022`,
`Bayer2024`, `Zhang2025LLMAL`, `Yusuf2023`, `Jung2021`, `Yu2022`, `Zhang2020`.

## 2. Defeitos que sobreviveram (5 de 6 verificadas)

| Chave | Estado | Ação |
|---|---|---|
| `Wu2022` **citada** (2-fundam:619) | **INEXISTENTE** — autores, arXiv ID e venue fabricados (2212.06445 é paper de matemática) | Substituir por Zhang, Strubell & Hovy, EMNLP 2022, pp. 6166-6190, DOI 10.18653/v1/2022.emnlp-main.414. **ATENÇÃO SEMÂNTICA**: a linha 619 alega "seleção ativa de instâncias, de *prompts* e do próprio oráculo" — o survey de Zhang et al. NÃO cobre prompt/oráculo; a frase precisa de outra fonte ou reescrita |
| `Ahmed2023` **citada** (2-fundam:648) | **INEXISTENTE** — Information 14(4):215 é outro artigo (Nießner et al.); o grupo Ahmed/Tiun/Omar não tem esse survey | Remover e repontuar. Se precisar de survey de topic modeling de texto curto: Qiang et al. (IEEE TKDE) ou Fan, Shi & Yuan (JIFS 45(2), 2023) — exigem fichamento antes do uso |
| `Ahmed2022` **citada** | Ano errado | `year={2023}` (Appl. Sci. vol. 13 = 2023; DOI confirma) |
| `Wei2022` **citada** | Autores truncados | Inserir **Brian Ichter** e **Fei Xia** entre Bosma e Ed H. Chi |
| `Guo2025Deuce` **citada** | Ano errado | `year={2024}` (TACL v.12 = 2024; o arXiv 2025 é postprint) |
| `Hacohen2023` órfã | **INEXISTENTE** — não há esse artigo em TPAMI; 1º autor é **Guy** (não Gideon) e a coautora é **Daphna** Weinshall | Remover. Se o tema entrar no texto: Hacohen, Dekel & Weinshall, ICML 2022 |

## 3. Achado novo, fora do escopo pedido

`Zhang2022` (órfã, linhas 592-598): autores fabricados — os reais são
**Yiming** Zhang, **Shi** Feng, **Chenhao** Tan (EMNLP 2022, pp. 9134-9148,
DOI 10.18653/v1/2022.emnlp-main.622). Corrigir ou remover.

## 4. Onde as fabricações se concentram (escopo do próximo lote)

As 4 fabricações confirmadas hoje são todas `@misc`/`@article` com
identificador arXiv, e 3 das 4 eram órfãs ou pouco citadas. População ainda
não verificada nesta classe:

- **15 citadas na tese**: Baykal2021, Daru2022Dataset, Deng2023fedal,
  Grandini2020, Karl2023, Kholodna2024, Li2020, Mikolov2013,
  Qi2026MixtureLLMs, Raczkowska2024AlleNoise, Romberg2025Reassessing,
  Rouzegar2024, Schick2023, Schroder2021SmallText, Yuan2025NoiseAL
- **22 órfãs** (baixa prioridade: podem ser removidas em vez de verificadas)

Recomendo verificar as 15 citadas (é o que a banca vê) e **remover** as 22
órfãs — remoção é mais barata que verificação e não perde nada citável.

## 5. DoD do lote corretivo (mesmo critério, na fonte)

Além dos critérios já verdes da §1: as 6 ações da §2 aplicadas; `Zhang2022`
resolvida; as 15 citadas da §4 verificadas contra fonte primária com registro
do URL; `2-fundam:619` com fonte que sustente a alegação sobre prompts/oráculo.
