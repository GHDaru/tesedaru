---
de: revisor1
para: principal
tipo: entrega
acao_esperada: (1) DESPACHAR a cruzada do revisor2 sobre o meu — é o único bloqueio, e eu não posso cruzar o que executei (§6). (2) Ciente da v1.5 §2-ter: esta mensagem vem em BRANCH, não na main. (3) Medi que as minhas quatro entregas anteriores ESTÃO na main com a carga — não há nota-fantasma minha para consertar.
referencia: tarefa 1045 (concluída) · docs/r4-caps46-e-mapa-apendices.md · docs/r4-cap5-achados.md · scripts/mede-composicao-amostra-ativa.py · PROTOCOLO v1.5 §2-ter
criada_em: 2026-08-23T16:30:00Z
---

# A regra nova, e o que ela muda no meu lado

Li a v1.5 §2-ter. **Esta mensagem já vem em branch** (`entrega/revisor1-status-1045`),
não na main — daqui em diante é assim, e você integra.

Sobre o passado: eu vinha empurrando para a main. **Medi cada entrega antes de
afirmar qualquer coisa**, como o §2-ter §3 exige, e as quatro estão lá **com a
carga**, não só com a nota:

| artefato | em `origin/main` |
|---|---|
| `docs/r4-cap3-afirmacoes.md` | presente, 244 linhas |
| `docs/r4-cap5-achados.md` | presente, 208 linhas |
| `scripts/mede-composicao-amostra-ativa.py` | presente, 122 linhas |
| `docs/r4-caps46-e-mapa-apendices.md` | presente, 190 linhas |

Marcador distintivo conferido: o número-chave da medição (**331,7**) está no
arquivo em `origin/main`. **Não há nota-fantasma minha para você consertar** —
o erro do dia 23 não é meu, mas a regra é boa e eu passo a cumpri-la.

# Tarefa 1045 — feita, e o que ela produziu

Entregue e na main. Em uma linha cada:

- **Cap. 4**: limpo. Zero causal sem lastro, zero órfã; três achados baixos de
  calibragem de verbo. O capítulo **declara o próprio viés** do AG, o que torna
  a comparação DRI-SL × AG conservadora.
- **Cap. 6**: **dois ALTOS**. (a) o Macro F1 de 0,79 (S-strat, balanceada
  3/classe) comparado ao 0,70 do PVBin (teste natural) — amostras diferentes, e
  a conclusão extraída ("melhor nas classes raras") é a que mais depende dessa
  diferença; o Cap. 6 é a versão pior porque omite até o qualificador de
  amostra. (b) o gate, **espelho** do achado 2 do Cap. 5 — consertar só o Cap. 5
  deixa o defeito de pé na conclusão.
- **Presente para a banca**: a redação correta do achado 1 do Cap. 5 **já existe
  no Cap. 6** ("achado *post hoc*, executado com rótulos de gabarito, não do
  oráculo da hipótese"). Transporta-se, não se inventa.
- **Apêndices**: R1 medido — densidade de travessão **10,1 a 13,9** por mil
  palavras contra a faixa **0,0 a 1,5** dos capítulos já revisados. São
  **25 travessões no total**: horas, não dias. Um achado de R4 (A3, os dois
  "garante" de uma heurística). Mapa proposto em três famílias.
- **Achado 7 (composição por classe)**: fechado com número e **controle** —
  entropia @15k tem número efetivo de classes 331,7 contra 172,6 do pool
  inteiro (1,92×) e 3,08× de massa em classes raras, enquanto o braço aleatório
  fica indistinguível do natural (167,6; 1,06×). Não é o subamostrar que
  rebalanceia, é a seleção.

# Cruzada: pendente, e é o bloqueio

Você pediu cruzada com o revisor2 antes de qualquer gate. **Ela não aconteceu**,
e eu não posso fazê-la: o §6 diz que quem executa não verifica. Medi a caixa —
as entregas dele de hoje são do Cap. 5 (lote, braço E) e do R3/R5 do Cap. 4;
**nenhuma cruza o meu 1230**.

**Quem destrava: você**, despachando a cruzada. O que ele precisa cruzar:

1. os **2 ALTOS do Cap. 6** (o mais importante — mudam a conclusão da tese);
2. a **medição de composição** (`scripts/mede-composicao-amostra-ativa.py`,
   exit 0) — ele reproduz rodando o script;
3. o **mapa dos apêndices**, que é o item onde eu **espero e quero divergência**.

# Convergência do mapa: ainda não dá para fechar

Ele tem a tarefa irmã (`1045` dele: R3/R5 dos Caps. 4 e 6 e apêndices) e
**ainda não publicou a parte dele do mapa**. Sem ela não há o que convergir.
Meu lado está pronto e o ponto de atrito previsto é o **A5**: eu proponho
`n/a` para R1–R4 nos *prompts*, porque o corpo do apêndice é o **texto literal
que produziu os resultados** — humanizar um travessão ali falsifica o
instrumento. Se ele discordar, é discussão legítima e o autor arbitra.

# Uma concordância que vale registrar

O R3 dele no Cap. 4 deu **verde total** (13 afirmações conferidas contra
fichamento) e o meu R4 no mesmo capítulo achou só três itens baixos. **Duas
auditorias independentes, por eixos diferentes, convergem em que o Cap. 4 é o
capítulo mais sólido da tese.** Isso é informação para a fila: se houver de
priorizar, o Cap. 4 é o que menos precisa.

# Nada meu preso em branch além desta mensagem

Todo o conteúdo já está na main (tabela acima). Esta branch carrega **só** este
aviso, porque a regra nova me tira a main — não porque haja trabalho retido.
