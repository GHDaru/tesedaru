---
de: revisor2
para: principal
tipo: aviso
acao_esperada: LER JUNTO com o meu 0709 e repassar ao autor — terminei de rastrear as OUTRAS tabelas da defesa e elas estão limpas. O problema é UMA tabela, não a defesa inteira; ninguém precisa auditar o resto nem mexer nos outros slides
referencia: meu aviso 20260822-0709 (o achado da pasta SUPERSEDIDO) · apresentacao/defesa.tex em 796a0e4 · experiments/e0/results/e0_table.json (activelearning)
criada_em: 2026-08-22T07:18:00Z
---

O aviso das 07:09 foi urgente e podia soar como "a defesa está contaminada".
Fui rastrear as outras tabelas antes que alguém saísse auditando slide por
slide. **Não está.** São três tabelas com número na defesa, e só uma tem
problema.

| slide | tabela | origem conferida | veredito |
|---|---|---|---|
| l.268 | P2 — DRI-SL vs AG (cold start) | bate, casa por casa, com a `tab:drisl-vs-ag` do Cap.4 (41,23→41,2 · 6,85→6,9 · 67,39→67,4 · 25,83→25,8 · 76,87→76,9 · 44,09→44,1; e o AG idem) | **limpa** |
| l.291 | P3 — oráculos LLM | bate com a `tab:e0-principal` do Cap.5 **e** com o artefato `experiments/e0/results/e0_table.json` (deepseek-v4-pro 0,821 · 0,7846 · US$ 0,4099 → 82,1% · 0,785 · 0,410; nemotron 0,779 · 0,7516) | **limpa, até o artefato** |
| l.393 | E3′ — varredura de orçamento | pasta `legacy_s42_bs16_eval20k`, marcada SUPERSEDIDO | **é esta, e só esta** |

A quarta tabela (l.532, "Instrumentação estatística") é metodológica: mapeia
situação → teste, não tem número a rastrear.

**Duas honestidades sobre o alcance do que eu conferi**, para ninguém ler
mais garantia do que existe:

1. Na tabela do P2 eu conferi **defesa contra o capítulo**, não contra
   artefato — dizer que ela bate com o Cap.4 não é dizer que o Cap.4 bate
   com os dados do E1/E4. Isso é outra cruzada, que não fiz.
2. Na tabela do P3 eu fui até o artefato, e ali a garantia é completa.

**Sobre o "621 classes" do slide do P3** (l.304): fui conferir por parecer
estranho um Macro F1 de 0,785 ao lado de 82,1% de acurácia num problema de
621 classes. Não é erro: 621 é o tamanho do **espaço fechado** em que o
oráculo escolhe — é assim que o Cap.6 formula (*"no espaço fechado de 621
categorias"*) —, e não o número de classes presentes na amostra (S-rand tem
n=1.000, S-strat n=1.863). O Macro F1 é calculado sobre as classes
presentes. A frase está certa; anoto porque é o tipo de coisa que a banca
pergunta, e a resposta é essa.

Resumo para o autor, em uma linha: **trocar a tabela do E3′ resolve o
problema da defesa; os outros slides não precisam ser tocados.**
