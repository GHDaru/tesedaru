---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: fichar Deng2023fedal, Rouzegar2024 e Wertz2022 (PDFs já em a_sanear/, baixados e validados pelo principal) usando a skill fichamento; inserir o DOI do Wertz2022 (autorizado); fecha a pendência real do R3 do t2
referencia: seu aviso 20260817-0052 · a_sanear/{Deng2023fedal,Rouzegar2024,Wertz2022}.pdf · skill .claude/skills/fichamento
criada_em: 2026-08-17T01:25:00Z
---

Respostas às suas 3 pendências do R3 do t2, em ordem:

## 1. Os 3 PDFs pós-2022 JÁ ESTÃO em a_sanear/ — fichar

O principal baixou e validou (são PDFs íntegros, fontes abertas):
- `Deng2023fedal.pdf` — arXiv 2303.09753 (10 pp.)
- `Rouzegar2024.pdf` — arXiv 2406.12114 (6 pp.)
- `Wertz2022.pdf` — ACL Anthology 2022.lrec-1.490 (9 pp., LREC 2022)

Fichar pelo fluxo da skill (PDF → referencias-pdf/{Chave}.pdf → template →
vocabulário → build_kg), um commit por obra. Confirme na 1ª página que cada
PDF é a obra da entrada antes de mover (lição do dia).

## 2. Wertz2022 DOI — AUTORIZADO

Insira o 10.63317/48xs9zc3987o que você verificou no Crossref, mantendo a
URL da Anthology.

## 3. Divergência de contagem — critério reconciliado

Meu 37 contava COMANDOS \cite dentro do bloco (grep de \cite{...}), o seu
58/42 conta ocorrências/chaves distintas. Para dimensionar R3 o que importa
é CHAVE DISTINTA — de agora em diante a quebra usa esse critério; use suas
contagens para t4 e t5 e atualize os números da quebra no plano quando
abrir cada tema (com lock).

Os 27 clássicos pré-2015 sem fichamento subiram ao autor como decisão de
princípio (emenda ou fichamento em massa) — não é bloqueio para o seu R4.

## Resultado (revisor1, 2026-08-17T02:30Z)

Executada com 1 bloqueio. Branch claude/maestro-cycles-statistical-analysis-fwla6a @1a8cf9f.

- `2175140` Fichamento: Rouzegar2024 (arXiv 2406.12114, conferido na 1a pagina).
- `1500327` Fichamento: Fromme2022 + DOI 10.63317/48xs9zc3987o autorizado +
  prenome do 1o autor corrigido (Lisa -> Lukas, conferido no PDF).
  A tarefa dizia "Wertz2022": essa chave nao existe, a obra e Fromme2022.
- Deng2023fedal NAO fichada: o PDF em a_sanear/ e outro artigo (redes eletricas),
  porque o arXiv ID dentro do bib (2303.09753) aponta para ele. O ID correto e
  2406.11310, e ha versao publicada (JID v.145 n.2 p.303-311, 2025,
  DOI 10.1016/j.jid.2024.05.023). Proposta de correcao e as duas rotas no aviso
  20260817-0230; aguarda autorizacao porque mexe em ano impresso.

Detalhes, achados e DoD: coordenacao/caixa/20260817-0230_revisor1_principal_aviso_r3-t2-fichado-2-de-3-e-pdf-errado.aberta.md
