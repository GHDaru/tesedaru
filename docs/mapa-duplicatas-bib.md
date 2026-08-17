# Mapa de resolução das duplicatas do bib (LOTE 2 — preparação)

**Autor:** revisor1 · **Data:** 2026-08-16 · **Estado:** preparação, nada aplicado.
**Fonte dos vereditos:** `docs/parecer-auditoria-bib.md` (gate do autor) + medição
executável por `scripts/check-bib.py --json` sobre o `referencias.bib` da main
após o merge `e160cc0` (378 entradas).

## Causa-raiz (por que existem 17 duplicatas)

O Capítulo 1 e o Capítulo 2 foram escritos com **convenções de chave
diferentes**: o Cap. 1 usa chaves em minúsculas com sufixo temático
(`devlin2019bert`, `song2014shorttext`, `alsmadi2019shorttext`,
`zhang2022surveyAL`), e o Cap. 2 usa CamelCase (`Devlin2019`, `Song2014`,
`Alsmadi2019`, `ZhangHovy2022`). Cada capítulo cadastrou a mesma obra sob a sua
convenção. Não é descuido pontual: é um padrão sistemático, e é o que explica a
concentração das 17 duplicatas justamente nesses dois capítulos.

Consequência impressa: a mesma obra aparece **duas vezes** na lista de
Referências, e o leitor vê duas citações diferentes para a mesma fonte.

## A. Grupos com as DUAS chaves citadas (exigem trocar `\cite` na prosa)

| Grupo | Chave canônica | Chave a eliminar | Ocorrências a trocar |
|---|---|---|---|
| Bayer / ActiveLLM | `Bayer2024ActiveLLM` (parecer) | `Bayer2024` (8x), `activellm2024` (órfã) | 8 no Cap. 2 |
| Zhang LLM-AL | `Zhang2025` (parecer) | `Zhang2025LLMAL` (1x) | 1 no Cap. 1 (linha 69) |
| Survey de AL | `zhang-etal-2022-survey` (parecer) | `zhang2022surveyAL` (2x), `ZhangHovy2022` (órfã) | 2 no Cap. 1 (43, 57) |
| BERT | `Devlin2019` | `devlin2019bert` (2x) | 2 no Cap. 1 (30, 64) |
| Short text survey | `Song2014` | `song2014shorttext` (2x) | 2 no Cap. 1 (11, 64) |
| Review short text | `Alsmadi2019` | `alsmadi2019shorttext` (2x) | 2 no Cap. 1 (11, 64) |

**Total: 17 ocorrências de `\cite` a reescrever** — 9 no Cap. 1 e 8 no Cap. 2.

> Divergência a resolver com o principal: a tarefa falava em **37** citações
> afetadas (9 no Cap. 1 e 28 no Cap. 2). O número do Cap. 1 bate exatamente; o do
> Cap. 2 não. Minha contagem só inclui ocorrências cuja **chave muda**. As demais
> do Cap. 2 provavelmente são citações cuja chave permanece e cujos **metadados**
> mudam (lotes 1 e 3), o que não exige tocar a prosa. Confirmar antes de executar.

### Efeito visível no texto (não é troca mecânica)

Duas unificações **mudam o ano impresso** na citação, portanto mudam o que o
leitor vê e a ordenação nas Referências:

- `Bayer2024` (2024) → `Bayer2024ActiveLLM` (**2026**, TACL v.14, com o coautor
  Justin Lutz que faltava): as 10 citações passam de "(BAYER; REUTER, 2024)"
  para "(BAYER; LUTZ; REUTER, 2026)".
- `Bates2022` (2022) → `Karl2023` (2023) — só órfã, sem efeito na prosa.

## B. Grupos com UMA chave citada (só limpeza do bib, prosa intacta)

`Ein-Dor2020`→`EinDor2020` · `Settles2010`→`Settles2009` ·
`Settles2008a/b`→`Settles2008` · `Yusuf2023`→`Riyanto2023Comparative` ·
`Jung2021`→`Nti2021` · `Bojanowski2016`→`Bojanowski2017` ·
`Bates2022`→`Karl2023` · `FreeAL2023`→`Su2023` (ver ressalva) ·
`Sener2017`→`Sener2018` · `Ash2019`→`Ash2020` ·
`Souza2022Embedding`→`Souza2023`.

**Ressalva no grupo FreeAL:** a chave citada é `Su2023` (Cap. 2, linha 564) — e é
justamente ela que carrega a **autoria fabricada** ("Su, B.; Guo, J.; Liu, Q.;
Zhang, Y."). A autoria real é Xiao, Dong, Zhao, Wu, Lin, Chen e Wang (EMNLP 2023,
DOI 10.18653/v1/2023.emnlp-main.896), verificada por mim na ACL Anthology na
rodada de fichamentos. Unificar aqui é mais do que apagar a duplicata: é
substituir metadados inventados pelos reais. Como as páginas do bib também estão
erradas (7982–7995 em vez de 14520–14535), este grupo pertence de fato ao
**lote 1** (fabricações, revisor2), não ao lote 2 — sinalizado para não
corrigirmos em duplicidade.

## C. Ordem de execução segura

As seis chaves canônicas da seção A **já existem** no bib. Logo a troca dos
`\cite` na prosa pode ser feita **antes** da unificação no `.bib`, sem quebrar a
compilação e sem precisar do lock de `referencias.bib` — o que destrava metade do
lote enquanto o lock está com o revisor2. A remoção das entradas duplicadas fica
para quando o lock for liberado.
