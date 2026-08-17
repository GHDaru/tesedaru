---
de: revisor2
para: principal
tipo: entrega
acao_esperada: R3 do Cap. 3 ENTREGUE — branch ciclo/014-fichas-cap3 @0f724fa (3 fichas lidas na fonte + 3 canônicas conferidas). ACHADO que vale mais que a rodada: "SBERT multilíngue" está atribuído ao artigo de 2019, onde "multilingual" aparece ZERO vezes — e a obra certa não está no nosso bib
referencia: sua tarefa 20260817-1940 · 3-metodo/texto.tex · a3-drisl/texto.tex
criada_em: 2026-08-17T19:55:00Z
---

Rodada curta, como você diagnosticou. As três pendências estão fichadas, **cada
uma lida no PDF**, e as três canônicas conferidas.

| Chave | Fonte | Situação |
|---|---|---|
| `Loshchilov2019AdamW` | ICLR 2019, 19 pp. | **fichada** |
| `Reimers2019SBERT` | EMNLP 2019, 11 pp. | **fichada** — com o achado abaixo |
| `Wolf2020Transformers` | EMNLP demos 2020, 8 pp. | **fichada** (mínima: é citação de ferramenta) |
| `Bishop2006`, `Goldberg1989`, `Holland1975` | canônicas (ADR 0012) | **campos mínimos OK** nas três |

Segui a sua orientação de registrar **o que a tese usa** de cada uma, e não o
resumo do artigo. Um efeito disso: nas três fichas há uma linha dizendo o que a
obra **não** sustenta, para o R5 não herdar atribuição indevida.

## ACHADO: "SBERT multilíngue" não é o artigo de 2019

O apêndice do DRI-SL diz "SBERT **multilíngue** \citep{Reimers2019SBERT}". Medi
no PDF: **"multilingual" aparece ZERO vezes**. O SBERT de 2019 é treinado e
avaliado em **inglês** (SNLI, MultiNLI, STS).

A obra do modelo multilíngue é outra, dos mesmos autores: **Reimers & Gurevych,
*Making Monolingual Sentence Embeddings Multilingual using Knowledge
Distillation*, EMNLP 2020** — é ela que introduz a destilação entre línguas e os
modelos `paraphrase-multilingual-*`. **Não está no nosso `referencias.bib`**
(conferi).

**Por que isso importa mais do que parece:** a tese roda em **português**, e a
propriedade que sustenta a fase 1 do DRI-SL é exatamente a multilinguidade.
Atribuí-la ao artigo de 2019 deixa a decisão de método sem lastro no ponto em que
a banca vai olhar. É o mesmo padrão dos achados do Cap. 2 — **acrescentar, não
remover**: o `2019` continua certo onde se fala do codificador e do cosseno; o
`2020` entra onde se fala de multilíngue. `referencias.bib` é do revisor1;
**ficho a obra de 2020 assim que a entrada existir**.

## Dois registros menores, de reprodutibilidade

1. **`Loshchilov2019AdamW` fundamenta o método, não os números.** Escrevi na
   ficha que $3\times10^{-5}$, lote 32 e decaimento $0{,}01$ são **escolha da
   tese** — o artigo explica por que "AdamW" e não "Adam com $L_2$", e por que
   taxa e decaimento podem ser reportados como escolhas independentes. Ninguém
   deve atribuir os hiperparâmetros a essa referência.
2. **`Wolf2020Transformers` é citação de ferramenta e está correta assim.** A
   sugestão que deixo, para o autor decidir: citação de biblioteca ganha valor
   com a **versão** usada, e o lugar disso é o apêndice de reprodutibilidade —
   o dado não vem da obra, vem do nosso ambiente.

## Estado

Branch `ciclo/014-fichas-cap3` @`0f724fa`: 3 fichas + 3 PDFs arquivados em
`referencias-pdf/` + vocabulário + KG regenerado (629 nós, 1314 arestas).
Verificador verde nas três. Com isso, **o R3 do Cap. 3 fecha do meu lado**.
