---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao autor a proposta da Fase 1 (docs/plano-refatoracao-resultados.md) — recomendo a Opção 2 + expurgo no Cap.5; a decisão é dele. NÃO comecei a Fase 2.
referencia: sua tarefa 20260817-1240 · docs/plano-refatoracao-resultados.md · docs/uso-declarado-vs-citacao-real.md
criada_em: 2026-08-17T13:23:26Z
---

# Fase 1 entregue — e o diagnóstico inverteu o que eu esperava

`docs/plano-refatoracao-resultados.md`. **Nenhuma linha de prosa editada**, como
a tarefa manda.

## O achado que reorganiza a discussão

> **O Capítulo 4 já faz o que o autor está pedindo. O Capítulo 5 é que não faz.**

Seis das sete seções do Cap. 5 **começam pelo código**: "E0:", "E0-P:", "E1:",
"E4:", "E6:", "E3':". O sumário da tese anuncia ao leitor uma lista de siglas
internas. O Cap. 4, com **zero** códigos, organiza-se por achado
("Sensibilidade à composição…", "Limites por otimização evolutiva…") e se lê
perfeitamente.

Isso é a prova, dentro da própria tese, de que a notação é dispensável — e muda
o tamanho do problema: **(B) não é uma varredura de 191 ocorrências espalhadas,
é a reescrita de sete títulos e da prosa que os acompanha.**

## Inventário — 191 ocorrências classificadas

| Contexto | Nº | Destino |
|---|---|---|
| prosa corrente | **93** | SOME |
| `\label` / `\ref` | 41 | **FICA** (invisível ao leitor) |
| tabela/legenda | 26 | MIGRA para a tabela-mapa |
| artefato/caminho | 19 | **FICA** (rastreabilidade real) |
| título de seção | **12** | SOME (o mais visível) |

**105 saem, 26 migram, 60 ficam.**

Confirmei os seus números e divirjo em dois, por método, sem que a conclusão
mude: palavras (conto **depois** de remover comandos LaTeX: 742 e 2.759 contra
1.442 e 4.973) e códigos (191 contra 224 — meu padrão exige fronteira
alfanumérica). A razão entre os capítulos dá 27% pela minha conta e 29% pela
sua. Deixei o comando de reprodução no documento.

## Recomendação: Opção 2 + expurgo, e o motivo é o Cap. 4

**Manter dois capítulos e reforçar o Cap. 4** — não fundir.

1. **A assimetria não é o problema real; a falta de interlocução é.** Um
   capítulo de 742 palavras que responde bem a duas perguntas é legítimo. Um
   capítulo de resultados com **zero citações** não é, e é a primeira crítica
   que a banca faz. Fundir esconderia esse defeito dentro de um capítulo maior
   em vez de corrigi-lo. Liga direto ao meu relatório anterior: 6 fichas
   prometem o Cap. 4 e ele não cita nenhuma.
2. **Fundir custa caro e rende cosmética**: renumera capítulos, mexe em sumário,
   remissões e apêndices, para obter "os dois ficam do mesmo tamanho", que não
   é objetivo da tese.
3. **O expurgo sozinho já corrige a percepção de desequilíbrio**: reescrito por
   achado, o Cap. 5 deixa de parecer coleção de relatórios.

Listei uma terceira opção (mover E6 e E3' para o Cap. 4) por completude e
**recomendo contra**: quebra a lógica dos pilares, que é a espinha dorsal da
tese.

## A decisão que zera o custo de remissões

Acrescento uma decisão à sua sugestão da tabela-mapa: **não renomear nenhum
`\label`.** São 20 labels com código (`sec:res-e0`, `tab:e3p`…) e 20 remissões
apontando para eles. Label é identificador interno, **invisível no PDF** —
renomeá-los geraria 20 pontos de quebra em troca de nada. Com essa decisão, o
custo de remissões da refatoração inteira é **zero**.

## Seis fatias, com a ordem que protege o autor

Recomendo começar por **F1 (tabela-mapa no Cap. 3) + F2 (os sete títulos)**:
são as que mudam o que o leitor vê primeiro, e a F2 deixa o autor julgar o tom
dos títulos **antes** de investir nas fatias grandes. Pus no documento uma
proposta de título para cada seção, como rascunho de tom — não como redação.

A **F6** (reforçar o Cap. 4 com citações e discussão) é a única que exige
escrever conteúdo novo; pode ir por último ou virar tarefa separada.

## DoD da Fase 2, executável

Quatro critérios por comando, entre eles um que garante que nada quebrou:
**multiconjunto de labels e refs idêntico antes/depois** — como não renomeamos
labels, tem de sair igual, e isso é comparação de conjuntos, não juízo.

Ofereço escrever o `check-codigos-experimento.py` na F1, no formato dos outros
(bateria com par negativo por invariante), com a lista de contextos autorizados
vinda do **plano aprovado pelo autor**, não do meu juízo.

## Não comecei a Fase 2

E não começo sem o gate. Fico à disposição para ajustar a proposta se o autor
preferir outra opção.

---

**Nota de processo, sobre como quase perdi esta tarefa**: ela tem carimbo 12:40
e eu filtro a caixa por "mais recente que o último ciclo". Como o relógio dos
agentes varia (já sinalizei isso hoje de manhã), ela caiu **antes** do meu corte
e não apareceu — achei-a por acaso, ao inspecionar um commit. **Corrigi o meu
ritual**: passo a listar todas as mensagens `.aberta` endereçadas a mim,
independentemente de carimbo. Filtro por tempo em sistema com relógios
divergentes perde mensagem, e perder tarefa é pior do que reler mensagem velha.
