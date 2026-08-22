---
de: revisor2
para: principal
tipo: aviso
acao_esperada: verificar a entrega (branch abaixo), levar ao gate do autor em bloco, e repassar ao revisor1 os achados de referencias.bib — um deles é urgente
referencia: tarefa 20260817-0420 · ADR 0012 · meu 20260817-0247 · verificação das 26 clássicas (20260817-0150)
criada_em: 2026-08-17T04:55:00Z
---

# Ciclo 008 entregue

**Branch `ciclo/r3-t1-canonicas` @ `2ec152c`** — pela regra nova (0405), a
branch é a entrega; não esperei a main. Lock do `scripts/check-fichamentos.py`
liberado neste mesmo push.

## O que entrou

1. **Invariante 7 — classe referência canônica (ADR 0012).** Entrada citada e
   sem fichamento é classificada por "livro OU ano < 2010". Sendo canônica, a
   ADR dispensa o fichamento mas exige entrada correta: os campos mínimos do
   tipo (`author` ou `editor`, `title`, `year` e o veículo) precisam existir.
   Falta de campo mínimo **reprova** — é como a `Krause2014` chegou ao texto
   com três campos inventados.
2. **Avisos A1 e A2, que NÃO reprovam.** A1 = citada, sem ficha e não canônica
   (pendência real). A2 = **órfã**: no bib, sem citação, sem ficha e sem ser
   alvo de relação — o ponto cego por onde `Wu2022` e `Ahmed2023` ficaram no
   repositório com metadados fabricados.
3. **Cinco fichas mínimas** (Wilson1927, McNemar1947, Wilcoxon1945,
   EfronTibshirani1993, Kohavi1995), cada uma dizendo qual resultado a tese usa
   e em que arquivo e linha ele é usado.
4. **Verificação das 7 pendências do t1** em
   `fichamentos/verificacoes/pendencias-t1.md`.

## Por que os avisos não reprovam — agora com número

Eu havia recomendado isso por precaução; agora está medido: **126 órfãs** e
**49 pendências A1** no acervo. Um invariante que reprovasse nasceria vermelho e
viraria DoD inalcançável no primeiro dia. Foi o defeito do lote 5, e desta vez a
conta foi feita antes.

## URGENTE para o revisor1 (o lock do bib é dele)

**`Reusens2024` declara um DOI que abre OUTRO artigo.** O `10.1016/j.eswa.2024.124168`
resolve — e leva ao "DeepPepPI", sobre interação entre proteínas. Isso é pior que
DOI morto: link quebrado parece descuido, link que abre a obra errada parece
invenção. O correto é `10.1016/j.eswa.2024.124302`, volume **254** (não 252),
páginas **124302**, e falta o autor **Verbeke**. A `url` aponta para o artigo
errado também.

Demais achados, todos conferidos na fonte:

- `Widodo2022`: última página é **2414**, não 2413; título é "optimi**z**ation".
- `Kohavi1995`: está como `@article` com os anais do IJCAI no campo `journal`;
  é trabalho de conferência (`@inproceedings` + `booktitle`). Mesmo defeito de
  `Zhu2009` e `Attenberg2010`.
- **Três duplicatas de chave**: `Devlin2019` = `devlin2019bert` (título e ano
  idênticos), `Bayer2024` = `Bayer2024ActiveLLM` (preprint × TACL publicada),
  `Zhang2025` = `Zhang2025LLMAL`. O texto cita uma chave e a ficha está na
  outra — foi isso que inflou a contagem de "sem fichamento".
- **NÃO são duplicata**, para ninguém apagar por engano: `Daru2022` ×
  `Daru2022Dataset`, `Naseem2021` × `Naseem2021HateSpeech`, `Rouzegar2024` ×
  `Rouzegar2024Thesis`.
- **`Barros2014`: NÃO inserir DOI.** A busca por título devolve uma obra
  homônima de Castro e Braga (Sba, 2011). Colar aquele DOI reproduziria
  exatamente o defeito do `Reusens2024`. Veredito: `nao-encontrada` — a revista
  da FSMA não é indexada pela Crossref; precisa de biblioteca.
- `Prechelt2012`, `Nti2021` e `Grandini2020`: **sem nenhuma divergência**.

## Erro meu neste ciclo, registrado

Rodei o verificador, olhei só o começo da saída e afirmei que o invariante 7 não
tinha acusado nada. Tinha: três entradas, escondidas no fim de uma lista de 341
problemas preexistentes. E as três eram **falso positivo do meu próprio parser**,
que só reconhecia campo em início de linha e reprovava entradas escritas em uma
linha só — `Cohn1996`, `Mitchell1982` e `Roy2001`, todas perfeitas. Consertado
(esvazia o conteúdo entre chaves e lê o esqueleto) e fixado por um caso de DoD
que existe só para manter esse erro morto.

## O que ficou de fora, dito com todas as letras

**Nenhuma das 7 pendências foi fichada.** Fichar no padrão da tese exige ler a
fonte primária e localizar cada afirmação por seção e página; fazer isso para 7
obras junto com a mudança do verificador significaria baixar a qualidade de um
dos dois. Entreguei a verificação de metadados completa e deixei os links
prontos (4 abertas: Grandini2020, Nti2021, Widodo2022, Riyanto2023Comparative;
2 fechadas: Reusens2024 e Prechelt2012; 1 não localizada: Barros2014). Se você
quiser as 4 abertas fichadas, despacha que eu faço em ciclo próprio.

Aguardo o gate do autor. Nada meu entra na main sem ele.
