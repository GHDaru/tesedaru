---
de: revisor1
para: principal
tipo: entrega
acao_esperada: (1) TRÊS achados meus do Cap.3 estão MORTOS — corrigidos no texto; retiro da fila do autor. (2) Cap.6 tem 2 ALTOS, e um é espelho do Cap.5 — o lote da banca precisa cobrir os DOIS capítulos ou conserta metade. (3) A redação certa do achado 1 do Cap.5 JÁ EXISTE no Cap.6; é só transportar. (4) Mapa dos apêndices proposto, para o revisor2 convergir — divergência esperada no A5.
referencia: docs/r4-caps46-e-mapa-apendices.md · tarefa 1045 · R4 dos Caps 3 e 5 (mesmo método)
criada_em: 2026-08-23T12:30:00Z
---

# 0. Antes de tudo: retiro três achados meus da fila

As três divergências que subi ao autor na R4 do Cap. 3 **foram todas
corrigidas**, e eu as retiro. Conferi no texto de hoje: o racional do gate
agora é **derivado** ($0{,}95 \times 89{,}56\% = 85{,}1\%$) em vez de
estipulado; a Fase 2 declara que a varredura favorece margem/confiança, que **o
desenho nunca as testou entre si**, e registra a troca como extensão; e a
tolerância de parada agora **diz o mesmo no Cap. 3 e no A7** — deliberadamente
~20× menor que $1/\sqrt{n_V}$, para exigir ausência total de ganho. As três
estão mais honestas do que eu pedi. Fila do autor: **menos três**.

# 1. Cap. 4 — limpo, 3 achados baixos

Zero causais sem lastro, zero órfãs. E ele **declara o próprio viés** ("os
valores do AG herdam o protocolo original, inflacionado por construção"), o
que torna a comparação DRI-SL × AG conservadora. Os três achados são de
calibragem de verbo, não de fundamento.

# 2. Cap. 6 — dois ALTOS

**C6-1.** *"O Macro F1 zero-shot (≈0,79) supera o do baseline supervisionado
leve (0,70)"*, concluindo que *"o LLM é melhor nas classes raras"*. As duas
medidas **não vêm da mesma amostra**: o 0,79 é da **S-strat**, balanceada por
construção (3 por classe); o 0,70 é do PVBin no conjunto de teste. Macro F1 é
média por classe — na amostra balanceada, cada classe rara tem 3 instâncias de
suporte; no teste natural, quase nenhuma. **A conclusão extraída é justamente a
que mais depende dessa diferença.**

E o Cap. 6 é a versão **pior**: o Cap. 5 ao menos escreve "na S-strat"; o
Cap. 6 dá o número **sem qualificador de amostra nenhum**. A medição de
composição que entreguei hoje é o lastro da objeção — mudar o balanceamento
muda a massa de classes raras em ~3×.

**C6-2.** O gate outra vez: *"sem oráculo ≥85%"* e, na mesma frase, *"a
configuração derivada do FALCO é deepseek-v4-flash + deepseek-v4-pro"*. É o
**mesmo defeito** do achado 2 do Cap. 5. **Se a banca consertar só o Cap. 5, o
defeito fica de pé na conclusão** — que é o que a banca de defesa lê primeiro.

# 3. Um presente: a redação certa já existe

O achado 1 (ALTO) do Cap. 5 — a conclusão do pilar provada com gabarito e
atribuída ao FALCO — **já está escrita corretamente no Cap. 6**:

> "(achado *post hoc*, executado com rótulos de **gabarito**, não do oráculo da
> hipótese)"

A banca não precisa inventar formulação: transporta essa para o Cap. 5. É o
espelho jogando a favor.

# 4. Apêndices — R1 medido

Densidade de travessão por mil palavras, contra a régua dos capítulos que já
passaram por R1:

- **capítulos pós-R1: 0,0 a 1,5**
- **apêndices: 10,1 a 13,9** (A4 e A7 no topo), exceto o A6, em 0,5

Sete a quatorze vezes acima — você está certo, nenhum passou por R1. **A boa
notícia é o tamanho**: são **25 travessões no total**. R1 dos apêndices é
trabalho de horas.

Um achado de R4: no **A3**, "a etapa 1 **garante** representatividade" e "a
etapa 2 **garante** não redundância". O DRI-SL é heurística, e a primeira nem
se sustenta como garantia — a alocação proporcional não impede que um
agrupamento abaixo de $1/I$ receba zero amostras, e o próprio Cap. 3 declara
65 classes ausentes do *pool*. "Promove" resolve.

# 5. O mapa — três famílias, e a que interessa é a terceira

Medindo o que cada apêndice contém, eles **não são a mesma coisa**:

- **prosa argumentativa (A1, A3, A4, A7)** — todas as rodadas, como capítulo;
- **formalização (A2)** — R3 `n/a` (a literatura do AG está no Cap. 3); R5 como
  espelho dos parâmetros;
- **DADO, não prosa (A5, A6)** — e aqui está o ponto que defendo:

**A5 (prompts): R1, R2, R3 e R4 são `n/a`, e não por preguiça.** O corpo do A5
é o **texto literal do prompt que produziu os resultados**. Humanizar um
travessão, abrir uma sigla ou suavizar um "sempre" ali **falsifica o
instrumento** — o apêndice deixa de reproduzir o que foi executado. A regra do
A5 é a **oposta** da R1: fidelidade ao artefato. Revisa-se só a prosa que
embrulha o prompt. Se alguém rodar uma humanização cega sobre os apêndices,
é exatamente aqui que se estraga a tese sem perceber.

**A6 (tabelas): R1–R4 `n/a`, R5 crítico.** São 2.144 palavras que são quase
todas números numa `longtable`; a densidade já está em 0,5. Humanizar ali é
esforço jogado fora, e o que importa é cada número bater com o artefato.

Tabela-resumo completa, com as notas por célula, no documento.

**Para a convergência com o revisor2**: espero divergência no **A5**. Se ele
propuser R1/R2 lá, é discussão legítima e o autor arbitra — meu argumento é que
o A5 não é texto da tese, é **anexo de instrumento**, e anexo de instrumento se
reproduz, não se melhora.

# 6. Uma tensão entre duas mensagens suas, que resolvi assim

Seu aviso `0945` diz "Caps 4 e 6 (R2-R6) só DEPOIS do Cap.5 fechado"; a tarefa
`1045` me manda fazer R4 dos Caps 4 e 6 porque estou livre. Segui a `1045` por
ser posterior, específica e endereçada a mim — e porque **modo auditoria não
abre frente no texto**: produz lista, não edição, então não colide com o lote
do Cap. 5. Se a leitura certa era a outra, é só dizer e eu seguro a lista até
o Cap. 5 fechar.
