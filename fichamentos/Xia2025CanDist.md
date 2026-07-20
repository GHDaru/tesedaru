---
id: Xia2025CanDist
title: "Prompt Candidates, then Distill: A Teacher-Student Framework for LLM-driven Data Annotation"
authors: ["Xia, Mingxuan", "Wang, Haobo", "Li, Yixuan", "Yu, Zewei", "Wang, Jindong", "Zhao, Junbo", "Wu, Runze"]
year: 2025
venue: "ACL 2025, pp. 2750-2770"
doi: "10.18653/v1/2025.acl-long.139"
pdf: referencias-pdf/Xia2025CanDist.pdf
paper_type: conferencia
pillars: [P3]
status: fichado
proposes: [rotulos-candidatos, destilacao-teacher-student]
datasets: [TREC, MedicalAbstract, DBpedia, AGNews, RCT, Banking77]
models: [gpt-3.5, roberta]
falco_relation:
  - type: estende
    target: E0P-invalidos-futuros
    note: "Correção conceitual importante: quando incerto, o LLM emite CONJUNTO
           de rótulos candidatos (não um único 'ouro'); um SLM destila. A
           incerteza do oráculo vira informação em vez de erro duro. Citado nos
           futuros como resposta aos nossos 2-4% de inválidos e ao erro de
           fronteira do RQ3. CanDist sem humanos supera baselines com 10% de
           anotação humana em TREC."
---

# CanDist / Prompt Candidates, then Distill (Xia et al., ACL 2025)

## Resumo
Framework teacher-student para anotação por LLM: em vez de forçar rótulo único,
o teacher (GPT-3.5) emite candidatos sob incerteza; o student (RoBERTa) destila
o conjunto ambíguo com garantias. Seis tarefas de classificação, incluindo
Banking77 (o maior espaço: 77 classes).

## Relação com a tese
Trabalhos futuros do Cap. 6 (rótulos candidatos p/ inválidos/fronteiras) e
revisão 2.5. Nosso espaço de 621 classes é ~8x o maior deles.

## Limitações
Teacher único; sem custo instrumentado por rótulo; inglês.
