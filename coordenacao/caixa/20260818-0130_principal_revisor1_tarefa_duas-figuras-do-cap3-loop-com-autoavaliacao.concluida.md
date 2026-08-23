---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: produzir as DUAS figuras do Capítulo 3 (arquitetura do FALCO e fluxo dos dados), em TikZ, trabalhando em LOOP com autoavaliação por nota até você mesmo se convencer de que está boa; mostrar a figura renderizada ao AUTOR e obter a aprovação dele antes de fechar; branch própria + lock de 3-metodo; gate comigo depois do aceite dele
referencia: ordem do autor 2026-08-18 · achado da banca: a tese inteira tem 2 figuras, nenhuma no Cap. 3 e nenhuma no Cap. 5 · régua de tom vigente (docs/criterio-humanizacao.md)
---

# Por que esta tarefa existe

Medição da banca no repositório inteiro: a tese tem DUAS figuras. Zero no
Cap. 3, zero no Cap. 5, zero nos sete apêndices. A única figura conceitual
é a 2.1, que é o diagrama do ActiveLLM adaptado de Bayer (2024): está
desenhado o trabalho do concorrente e não está desenhado o FALCO. O autor
decidiu corrigir isso começando pelo capítulo metodológico.

# O que produzir

**Figura 3.1 — arquitetura e máquina de fases do FALCO.** Deve mostrar, sem
prosa de apoio: o pool não rotulado, a estratégia de seleção, o oráculo, o
classificador re-treinado a cada lote, e as TRÊS fases com o que muda em
cada uma (Fase 1: DRI-SL + LLM Inicial, lote inicial b_0; Fase 2: seleção
por entropia + LLM Inicial; Fase 3: mesma seleção, oráculo passa ao LLM
Avançado), a condição de transição da Fase 2 para a 3 (estagnação do Macro
F1 na validação) e o fato de a Fase 3 ser CONDICIONAL ao critério de
aprovação do oráculo. Fonte: Seções sec:metodo-falco-fases e
sec:metodo-oraculo-decisao. Nada além do que o texto já diz.

**Figura 3.2 — fluxo dos dados e partição.** A cadeia declarada no texto:
250.365 linhas originais -> auditoria (conflitos de rótulo, rótulo
operacional, duplicatas) -> 250.221 na versão corrigida -> visão
deduplicada com 231.490 textos únicos e 714 classes -> particionamento por
posição com semente 42: pool de 50.000, holdout do ciclo de 4.000 (2.000
validação + 2.000 teste) e população reservada de 177.490. Fonte:
sec:metodo-dados-auditoria, sec:metodo-dados-preproc e
sec:metodo-dados-particionamento.

ATENÇÃO, e isto é importante: há uma divergência ABERTA sobre a população
(o código do E6 usa 181.490 por não excluir o holdout; decisão pendente do
autor). A figura desenha o que o TEXTO declara (177.490) e você NÃO
resolve a divergência por desenho nem a esconde. Se quiser, registre no
seu aviso que a figura precisará de um ajuste caso o autor decida
reexecutar. Desenhar obriga a decidir, e é bom que obrigue.

# Restrições técnicas

- TikZ, sem imagem rasterizada. O autor já pegou uma quebra de layout na
  Fig. 2.1 (rótulo sobreposto a uma caixa) e é sensível a isso.
- Largura máxima: a da página, sem estourar margem. Fonte mínima
  \footnotesize nos rótulos.
- Travessão Unicode é proibido em TÍTULOS; em \caption vale a exceção
  aprovada. Na dúvida, escreva sem travessão.
- Rótulos nomeiam OBJETOS. Códigos de experimento só onde a tabela-mapa já
  os usa.
- Nenhum elemento na figura pode carecer de respaldo no texto do Cap. 3.
  Figura que afirma mais que o texto é afirmação sem fonte.

# Modo de trabalho: LOOP COM AUTOAVALIAÇÃO (pedido explícito do autor)

Você trabalha em ciclo fechado, se dá uma NOTA a cada iteração e só para
quando estiver convencido de que a nota está boa. A rubrica abaixo existe
para a nota não ser opinião solta. Avalie de 0 a 10 em cada critério:

1. **Fidelidade ao texto** (ELIMINATÓRIO): cada caixa, seta e rótulo tem
   respaldo explícito no Cap. 3; nada de novo entrou por conta do desenho.
   Nota abaixo de 10 aqui invalida a iteração inteira, qualquer que seja o
   resto.
2. **Legibilidade renderizada**: você COMPILA o PDF e olha. Sem
   sobreposição, sem texto cortado, sem seta cruzando caixa, legível em
   impressão A4 preto e branco.
3. **Autossuficiência da legenda**: alguém que leia só a figura e a legenda
   entende o que está vendo, sem procurar o parágrafo.
4. **Economia**: nenhum elemento decorativo; se apagar algo e nada se
   perde, apague.
5. **Build verde**: o PDF compila sem erro novo e a figura não estoura a
   margem.

CONDIÇÃO DE PARADA: nota >= 9 em todos os critérios, com o critério 1 em 10,
e duas iterações consecutivas sem que a nota suba. Aí você para. Registre a
nota de cada iteração no seu aviso final, com uma linha do que mudou entre
elas: o autor quer ver o caminho, não só o destino.

# Interação com o autor (exceção de roteamento autorizada por ele)

Nesta tarefa você fala DIRETO com o autor para mostrar a figura. Não mande
código LaTeX pedindo que ele imagine o resultado: RENDERIZE e mostre a
imagem. Caminho prático: compile o PDF (ou um documento standalone só com a
figura), converta a página/recorte em PNG e entregue o PNG a ele.

Mostre quando a sua autoavaliação já tiver parado pela condição acima, não
antes: ele é o recurso mais caro do projeto e não deve revisar rascunho que
você mesmo ainda melhoraria. Se ele pedir mudança, o loop recomeça com a
mudança dele como restrição nova.

Depois do aceite dele, me avise com o hash para eu consolidar o gate.
======================== COPIE ATÉ AQUI ========================