---
de: revisor2
para: principal
tipo: entrega
acao_esperada: NÍVEL 1 ENTREGUE — branch ciclo/012-fichas-nivel1-cap2 @c50153f (6 fichas integrais lidas na fonte + 6 PDFs arquivados + KG). Três achados de citação precisam de decisão do autor sobre a prosa da §2.3, que eu NÃO editei. Sigo para o nível 2
referencia: sua tarefa 20260817-1420 · skill fichamento · ADR 0012
criada_em: 2026-08-17T15:50:00Z
---

As 6 obras do nível 1 estão fichadas, **cada uma lida no PDF**, com página em
cada evidência. PDFs arquivados em `referencias-pdf/` (como manda a skill, não
ficam em `a_sanear/`), KG regenerado, um commit por ficha.

| Chave | Fonte | Situação |
|---|---|---|
| `Diao2023` | ACL 2024, 21 pp. | fichada |
| `Gal2017` | ICML/PMLR v70, 10 pp. | fichada |
| `Natarajan2013` | NIPS 26, 9 pp. | fichada |
| `Wei2022` | NeurIPS 35, 14 pp. | fichada |
| `Tian2023` | EMNLP 2023, 10 pp. | fichada |
| `Schick2023` | arXiv 2302.04761, 17 pp. | fichada |

## Três achados de citação — os dois primeiros mudam a prosa da §2.3

**1. `Schick2023` (Toolformer) não sustenta a afirmação que lhe é atribuída.**
A §2.3 (l. 611) diz "a própria escolha de \textit{prompts} pode ser ativa
\citep{Diao2023, Schick2023}". Medi no PDF: a expressão "active learning"
aparece **zero** vezes no Toolformer. O que ele decide é *"which APIs to call,
when to call them, what arguments to pass"* (p. 1), por auto-supervisão via
perplexidade — não seleção ativa de prompt. **`Diao2023` sustenta a frase com
precisão** ("determining which questions are the most important and helpful to
annotate… borrowing ideas from uncertainty-based active learning", p. 1).
Recomendação: **mover, não remover** — o Toolformer sustenta a afirmação dos
sistemas compostos, que a própria §2.3 faz alguns parágrafos antes.

**2. `Tian2023` está citada na direção inversa do seu achado-manchete.**
A §2.3 (l. 704) diz "a confiança auto-reportada dos LLMs tende ao excesso,
exigindo calibração \citep{Tian2023}". O paper conclui o oposto sobre essa
grandeza: *"verbalized confidences … are typically better-calibrated than the
model's conditional probabilities … reducing the expected calibration error by a
relative 50%"* (p. 1). O excesso de confiança que ele discute está nas
**probabilidades internas**, degradadas pelo RLHF (p. 2). A metade "exige
calibração" está sustentada; a metade "auto-reportada tende ao excesso", não.

**3. E o conserto do item 2 já existe no acervo.** `Diao2023` mediu exatamente
isso, como falha operacional de um estimador que testou: *"self-confidence is
not working because LLMs are prone to be over-confident"* (p. 7). Duas saídas,
ambas fiéis, e a escolha é do autor: (a) atribuir o excesso a `Diao2023` e deixar
`Tian2023` sustentando a calibração; ou (b) manter `Tian2023` e ajustar a frase
para "a confiança de um LLM exige calibração, ainda que a versão verbalizada
seja frequentemente melhor calibrada que as probabilidades internas".

## Duas ressalvas de regime que registrei nas fichas

- **`Natarajan2013`**: as garantias são para ruído **aleatório dependente da
  classe, no caso binário**. O erro do nosso oráculo é dependente da
  **instância** (confusões em pares vizinhos) — que `Frenay2014` classifica como
  o caso difícil. A frase da §2.3 está correta como está; mas o Cap. 6, que cita
  a obra para dizer que erro estruturado é "cenário benigno", pede cuidado: o
  benigno dessa literatura é o ruído aleatório. Estruturado é mais fácil de
  *interpretar*, não necessariamente o caso coberto pelas garantias.
- **`Wei2022`**: cadeia de pensamento produz **texto livre**, o que conflita com
  a saída restrita ao espaço de rótulos que esta tese adota como parte do
  instrumento. Vale dizer isso explicitamente no Cap. 3 — abrimos mão de um
  recurso eficaz por razão de instrumento, e assumir a escolha é mais forte que
  omiti-la.

## Medições (princípio V)

| Medida | Resultado |
|---|---|
| `check-fichamentos.py` nas 6 fichas | `PROBLEMAS: nenhum` |
| `check-fichamentos.py` completo na **main** | exit 1, **334** problemas (dívida pré-existente, quase toda de vocabulário) |
| o mesmo na minha branch | exit 1, **333** — **não acrescentei nenhum e consertei um** de brinde: `Guyon2011ALC` usava `classificacao-binaria`, termo que eu precisei registrar no `_VOCABULARIO.md` para o `Natarajan2013` |
| `check-bib.py` | exit 0, 336 entradas |
| KG | regenerado, 655 nós / 1379 arestas |

Registro que o `check-fichamentos` está **vermelho na main com 334 problemas**:
é dívida antiga e sem dono, e por isso "verificador verde" não serve como DoD
aqui — o que serve é "não piorei e o meu bloco passa", que é o que medi.

## Um deslize meu, corrigido antes de avisar

Comitei as 6 fichas **na branch do t1** por inércia de diretório. São outra
tarefa e não devem viajar no gate do t1. Movi para a branch própria por
`cherry-pick` e limpei a do t1 com **um commit** — sem force-push, respeitando a
regra. Confirmei depois: a `humanize/cap2-t1` voltou a ser exatamente o que eu
declarei às 15:00 (2 linhas no `.tex` + as 4 fichas do ciclo 010).

## Próximo passo

Sigo para o **nível 2** (10 fichas mínimas). Quatro já estão prontas na branch do
t1 (`Grandini2020`, `Nti2021`, `Widodo2022`, `Riyanto2023Comparative`) — não vou
refazê-las; faltam 6 (`Barros2014`, `Aliero2023`, `Ahmed2022`, `Reusens2024`,
`Hanneke2015`, `Attenberg2010`). Aviso ao fechar o bloco. O nível 3 (política das
obras-marco) vem depois, como análise para você consolidar.

## Resultado (principal)
Entrega processada e integrada; arquivada na limpeza.
