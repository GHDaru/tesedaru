# Verificação das 7 pendências reais do tema t1 (pós-ADR 0012)

**Data:** 2026-08-17 · **Executor:** revisor2 · **Tarefa:** 20260817-0420
**Escopo:** as 7 chaves que a ADR 0012 deixou fora da categoria canônica e que,
portanto, seguem na regra cheia.

Vocabulário de veredito, o mesmo da verificação das 26 clássicas:
`existe` (localizada em fonte primária com identificador resolvível) ·
`nao-indexada-declarada` (real, mas sem identificador — propriedade da obra) ·
`nao-encontrada` (**a busca falhou; não equivale a "não existe"**).

| Chave | Veredito | Conferido contra | Situação da entrada |
|---|---|---|---|
| `Prechelt2012` | existe | Crossref, DOI `10.1007/978-3-642-35289-8_5` | **Nenhuma divergência.** Capítulo, editores, série, volume e pp. 53--67 conferem |
| `Nti2021` | existe | Crossref, DOI `10.5815/ijitcs.2021.06.05` | Confere: v. 13, n. 6, pp. 61--71, 2021 |
| `Grandini2020` | existe | arXiv `2008.05756` (página do artigo aberta) | Confere; só a caixa do título difere ("Multi-Class" no original) |
| `Widodo2022` | existe | Crossref, DOI `10.33395/sinkron.v7i4.11792` | **Duas divergências**: última página é **2414**, não 2413; e o título correto é "optimi**z**ation", não "optimation" |
| `Riyanto2023Comparative` | existe | IJACSA v. 14 n. 6 (página respondeu HTTP 200) | Sem DOI declarado pelo periódico; a URL abre |
| `Reusens2024` | existe | Crossref, DOI `10.1016/j.eswa.2024.124302` | **O PIOR CASO DESTE LOTE — ver abaixo** |
| `Barros2014` | **nao-encontrada** | Crossref (sem cobertura da revista); site da FSMA respondeu 404 | Precisa de biblioteca ou busca direta. **Atenção à armadilha descrita abaixo** |

## O achado grave: `Reusens2024` aponta para outro artigo

A entrada declara `doi = {10.1016/j.eswa.2024.124168}`. Esse DOI **resolve**, e é
esse o problema: ele leva a um artigo **completamente diferente** —
*"DeepPepPI: A deep cross-dependent framework with information sharing
mechanism..."*, de Wang, Meng, Dai e outros, sobre interação entre proteínas.

Um parecerista que clicar no DOI da tese vai parar num artigo de bioinformática.
É pior do que um DOI morto: um link quebrado parece descuido, um link que abre
a obra errada parece invenção.

O correto, conferido na Crossref:

| Campo | Está no `.bib` | Correto |
|---|---|---|
| `doi` | 10.1016/j.eswa.2024.124168 | **10.1016/j.eswa.2024.124302** |
| `volume` | 252 | **254** |
| `pages` | 124168 | **124302** |
| `author` | Reusens, Stevens, Tonglet, De Smedt | falta **Verbeke** |
| `url` | .../S095741742401168X | idem, aponta para o artigo errado |

O título e o ano estão certos — o que torna o erro mais difícil de ver a olho nu.

## A armadilha do `Barros2014`

Buscando pelo título, a Crossref devolve **uma obra homônima**: "Aprendizado
supervisionado com conjuntos de dados desbalanceados", de **Castro e Braga**,
*Sba: Controle & Automação*, 2011, v. 22, pp. 441--466, DOI
`10.1590/s0103-17592011000500002`.

**Não é a mesma obra** que a entrada declara (Barros, Garcia e Cavalcanti,
Revista de Sistemas de Informação da FSMA, v. 13, pp. 4--19, 2014).

Registro isto com destaque porque a tentação é óbvia e errada: colar o DOI que
apareceu para "resolver" a pendência produziria exatamente o defeito do
`Reusens2024` — identificador que abre a obra errada. **Não inserir esse DOI.**
O veredito é `nao-encontrada`: a revista da FSMA não é indexada pela Crossref, e
a busca precisa continuar por outra via.

## Duplicatas de chave descobertas no caminho

Ao classificar as entradas citadas sem fichamento, apareceram **três obras
cadastradas duas vezes** com chaves diferentes — o que explica por que elas
constavam como "sem fichamento" mesmo já tendo ficha:

| Par | Situação |
|---|---|
| `Devlin2019` e `devlin2019bert` | Título e ano **idênticos**. Duplicata inequívoca; a ficha está sob `devlin2019bert`, o texto cita `Devlin2019` |
| `Bayer2024` e `Bayer2024ActiveLLM` | Mesma obra: a primeira declara 2024 (preprint), a segunda 2026 (versão TACL publicada). A ficha está na segunda |
| `Zhang2025` e `Zhang2025LLMAL` | Mesmo título e mesmo ano. A ficha está sob `Zhang2025` |

E **três pares que NÃO são duplicata**, registrados para ninguém apagar por
engano — foi o erro que eu mesmo cometi uma vez com a `Naseem2021`:

- `Daru2022` (artigo) × `Daru2022Dataset` (conjunto de dados) — obras distintas;
- `Naseem2021` (survey de pré-processamento) × `Naseem2021HateSpeech` (estudo de
  caso em discurso de ódio) — títulos e escopos diferentes;
- `Rouzegar2024` × `Rouzegar2024Thesis` — títulos diferentes; conferir se é
  artigo × dissertação do mesmo autor antes de mexer.

## O que fica pendente de fichamento

Nenhuma das 7 foi fichada neste ciclo: a tarefa pedia fichar o que tivesse PDF
aberto, e fichar com o padrão da tese exige ler a fonte primária e localizar
cada afirmação por seção e página — trabalho que não cabia junto com a mudança
do verificador sem baixar a qualidade de um dos dois. Prefiro entregar a
verificação de metadados completa e honesta e deixar o fichamento explícito como
próximo passo, com os links já prontos:

| Chave | Acesso | Link pronto para o autor |
|---|---|---|
| `Grandini2020` | **aberto** | arXiv 2008.05756 |
| `Nti2021` | **aberto** | DOI 10.5815/ijitcs.2021.06.05 (MECS Press) |
| `Widodo2022` | **aberto** | DOI 10.33395/sinkron.v7i4.11792 |
| `Riyanto2023Comparative` | **aberto** | IJACSA v. 14, n. 6, pp. 1082--1090 |
| `Reusens2024` | fechado (Elsevier) | DOI 10.1016/j.eswa.2024.**124302** |
| `Prechelt2012` | fechado (Springer) | DOI 10.1007/978-3-642-35289-8_5 |
| `Barros2014` | não localizado | — precisa de biblioteca |
