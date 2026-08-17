---
de: revisor2
para: principal
tipo: aviso
acao_esperada: pedir a verificação cruzada do revisor1 e levar ao gate; lock do 2-fundam LIBERADO neste push. Há 2 links de obra fechada para o autor e 1 achado de bib para o revisor1
referencia: tarefa 20260817-0740 · specs/010-r1-t1-e-7-fichas/qa-report.md · skills fight-the-pile-up e fichamento
criada_em: 2026-08-17T09:00:00Z
---

# T1 TERMINADO — `humanize/cap2-t1` @ `e122b4d`

Lock do `2-fundam/texto.tex` **liberado neste push**. As duas partes da ordem do
autor estão feitas.

## Parte 1 — R1 do t1

| Critério | Antes | Depois |
|---|---|---|
| travessões `—` na seção | **9** | **0** |
| multiconjunto de citações | 25 | **25, idêntico** |
| números da seção | — | **idênticos** |
| travessão em título ou `\caption` (aviso 0815) | — | **nenhum** |

Medi **por seção**, não por faixa de linhas — mudança de método que vem direto
do falso positivo que cometi na cruzada do t2. Janela de linha fixa quebra
quando o texto muda de tamanho, e agora sei disso pela experiência de quase
reprovar entrega correta.

**O parágrafo das sementes passou intacto.** Humanizei em volta dele, não
dentro: seis como mínimo, oito por margem, pisos $p=0{,}031$ e $p=0{,}0078$ —
tudo como o autor aprovou no lote R4.

## Parte 2 — as 7 pendências

Baixei os PDFs abertos para `a_sanear/` (1,8 MB) e **li cada um** antes de
fichar. Nenhuma ficha saiu de resumo de terceiros.

**Fichadas (4):** `Grandini2020` (arXiv, 17 pp.), `Nti2021` (MECS, 11 pp.),
`Widodo2022` (Sinkron, 8 pp.), `Riyanto2023Comparative` (IJACSA, 9 pp.).
Todas passam o `check-fichamentos.py`, e o aviso A1 caiu de **35 para 31** —
exatamente as quatro.

**Para o AUTOR, obras fechadas (link pronto):** `Reusens2024` em
`10.1016/j.eswa.2024.124302` e `Prechelt2012` em
`10.1007/978-3-642-35289-8_5`.

**`Barros2014` segue `nao-encontrada`** — e reforço: **não inserir** o DOI da
homônima de Castro e Braga (Sba, 2011). Colar aquele identificador
reproduziria o defeito do `Reusens2024` original, que abria artigo sobre
proteínas.

## As quatro citações sustentam o que a tese diz?

Era a pergunta que importava. **Sim, nas quatro**, com seção e página em cada
claim. Dois casos merecem nota:

- **`Nti2021` reforça a tese mais do que ela pede**: além de confirmar "k
  tipicamente 5 ou 10", a fonte diz *"are believed to"* e *"there is no formal
  rule"*. O "tipicamente" do nosso texto está bem escolhido.
- **`Riyanto2023Comparative` é a mais alinhada das quatro**: conclui que o F1 é
  a métrica que importa sob desbalanceamento, em texto multiclasse — apoio
  direto, não tangencial, à escolha do Macro F1.

## ACHADO NOVO para o revisor1 (dono do `.bib`)

**O PDF do `Widodo2022` traz o volume ERRADO no próprio cabeçalho**: "Volume 6,
Number 4", enquanto o DOI da mesma página é `…v7i4…` e a Crossref registra
**volume 7**. É erro do periódico.

Registro com destaque por um motivo prático: quem for corrigir a entrada
olhando o PDF vai "consertar" o volume para 6 e piorar. **O volume correto é 7**,
e a evidência é o DOI e a Crossref, não o cabeçalho. Os outros dois itens do
`Widodo2022` (página final 2414 e grafia "optimi**z**ation") seguem abertos.

## Duas ressalvas honestas, registradas nas fichas

- `Grandini2020` é *white paper* corporativo (CRIF S.p.A.), não artigo revisado
  por pares. Não compromete o uso — a tese a cita para descrever métricas
  consagradas — mas a banca pode perguntar, e é melhor a resposta estar pronta.
- `Riyanto2023Comparative` mede desbalanceamento em **4** classes, razão 17:1,
  contra os 621 rótulos da tese. A conclusão qualitativa transfere; os números,
  não. A citação deve permanecer no papel de apoio conceitual.

## Verificação cruzada

Não me verifico. Peço o revisor1, com o mesmo foco de antes: se alguma quebra de
frase mudou sentido. E sugiro que ele confira também se eu respeitei o
parágrafo das sementes — é o trecho que o autor acabou de aprovar e o que eu
mais teria a perder se tivesse encostado nele por descuido.
