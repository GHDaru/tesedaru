# Aplicação do relatório de escrita científica (v2) — triagem e decisões

Data: 19/07/2026. Fonte: relatório "Spec-Kit de Escrita Científica" enviado
pelo autor. Regra da tese: toda decisão com justificativa. Itens triados
contra o estado atual (pós-E3', pós-reestruturação do Cap. 2, 5 artigos).

## Aplicado nesta passada

| Item do relatório | Aplicação | Onde |
|---|---|---|
| Minto/SCQA — "resposta primeiro" | Resumo e Abstract da tese terminavam nos resultados (i)-(iv) e **prometiam** o P4; agora reportam o item (v): ciclo real a custo zero, veredito do E3' (hipótese refutada na configuração executada + decomposição + 94,1%), viés de autoavaliação | `0-iniciais/resumo.tex`, `abstract.tex` |
| PRISMA/Kitchenham — transparência de revisão | A Seção 2.5.1 agora declara o estatuto metodológico: revisão **narrativa focada**, não RSL completa com protocolo registrado — com justificativa (papel do capítulo) e contrapartida (critérios explícitos na tab:lacunas). Kitchenham 2004 adicionada ao .bib | `2-fundam/texto.tex` §2.5.1 |
| Checklist do orientador (seção 6) | Auditoria pass/fail executada — resultado abaixo | este documento |
| Erro comum "promessas não cumpridas na conclusão" | Já corrigido no fechamento do E3' (conclusão reescrita); o Resumo era o último lugar com promessa — corrigido acima | Cap. 6 + resumo |

## Auditoria do checklist (visão do orientador)

| Seção | Veredito | Evidência / observação |
|---|---|---|
| Introdução | PASS | problema, relevância, objetivos, hipótese falseável com critério; delimitação explícita (sec:intro-delimitacao) |
| Revisão (Cap. 2) | PASS | reestruturado 18/07: síntese argumentativa, 2 níveis, lacuna materializada em tabela; estatuto da revisão agora declarado |
| Metodologia (Cap. 3) | PASS | justificativas de dimensionamento auditadas (18/07); pontes de fluidez; E3' com racional do corte registrado |
| Resultados (Caps. 4-5) | PASS com nota | o estilo integra resultado+leitura no mesmo capítulo (não IMRaD estrito); decisão deliberada e uniforme — capítulos argumentativos com números rastreáveis; a separação "dado cru vs. interpretação" é feita por parágrafo, não por seção. Defensável; registrar se a banca preferir separação formal |
| Discussão (Cap. 6) | PASS | confronta literatura, limitações honestas (config. econômica do E3' declarada), implicações |
| Conclusão | PASS | responde objetivamente à hipótese (refutada + causa + 94,1%), sem material novo, contribuições enumeradas |

## Descartado, com racional

| Item | Racional do descarte |
|---|---|
| Modelo de maturidade 1-5 | Diagnóstico, não ação: o fluxo atual já opera no nível 4-5 descrito (git+CI de LaTeX, checklists quantitativos, revisores-LLM, artefatos rastreáveis) |
| Stack recomendado 2026 | Já implementado equivalente: LaTeX+Makefile (=Overleaf), fichamentos+KG (=Zotero/Obsidian), runners versionados (=Jupyter), revisões R1-R4 (=LLM-review) |
| Template espec-driven de tese | Duplicaria o que existe: constituição spec-kit, pré-registro de critérios, planos aprovados em docs/ — a tese JÁ é espec-driven |
| Workflow IA-first (seção 5) | É a descrição do processo que esta colaboração já executa (RAG=fichamentos+KG; validação de citações=passes de bib; agentes=sessões) |
| Templates LaTeX alternativos (novathesis etc.) | O ppginf.cls do PPGInf/UFPR é obrigatório para o programa |
| PRISMA completo para o Cap. 2 | Custo alto (reconstruir contagens de triagem a posteriori) sem artefato original; a declaração honesta de revisão narrativa + tabela de critérios é a alternativa correta — inventar números de fluxo violaria a constituição |
| Toulmin formal por argumento | Os achados centrais já têm estrutura claim-grounds-qualifier (ex.: veredito E3' com decomposição e escopo declarado); formalização explícita seria cerimônia sem ganho |

## Pendências geradas

1. Nenhuma bloqueante. A nota sobre estilo de Resultados (PASS com nota)
   fica registrada para eventual arguição da banca.
