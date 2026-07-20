# Folha de arguição — defesa FALCO

> Preparação para a banca. Perguntas difíceis, previsíveis, agrupadas por tema.
> Para cada uma: a resposta curta (o que dizer em 2–3 frases) e o lastro
> (o artefato/resultado que sustenta a resposta). Estude as respostas curtas;
> use o lastro só se a banca insistir. Regra de ouro: **conceder o que é
> justo, defender o que é medido, nunca inventar número.**

---

## 1. Sobre a hipótese e o critério pré-registrado

**P1.1 — Sua hipótese pré-registrada era 95% do Macro F1 com ≤30% dos rótulos.
O E3′ mostrou que 30% não atinge o critério. Sua hipótese não foi refutada?**

- **Resposta curta:** Sim, e isso está escrito na tese sem eufemismo: em 30%
  do pool a hipótese é *refutada*. O que a varredura de orçamento acrescenta é
  *onde* ela passa a valer — a partir de ~50% do pool os dois critérios
  (acurácia e Macro F1) são satisfeitos, e em 70% o modelo forte supera a
  supervisão completa. O critério não foi afrouxado depois do fato; ele
  continua sendo 95%/30%, e eu relato honestamente que nesse ponto ele não
  passa.
- **Lastro:** Tabela da varredura E20–E35 (Cap. 5, `tab:e3p-sweep`); veredito P4
  reescrito no Cap. 6 ("refutada em 30%, sustentada a partir de 50%").

**P1.2 — Isso não é "mover a trave" (moving the goalpost)? Você mudou o alvo
para poder declarar sucesso.**

- **Resposta curta:** Não. Mover a trave seria trocar 30% por 50% e apresentar
  como se sempre tivesse sido 50%. Eu faço o oposto: mantenho o 30% como
  critério, declaro a refutação nesse ponto, e trato o piso de 50% como um
  *achado medido*, não como a hipótese original. A contribuição científica aqui
  é justamente saber onde está o piso — que é uma informação de engenharia útil,
  não um sucesso disfarçado.
- **Lastro:** A decomposição de perda (ruído/seleção/orçamento) mostra que o
  fator dominante é o orçamento e a parada, não o oráculo. O critério pré-registrado
  está documentado no Cap. 3 antes de qualquer resultado.

**P1.3 — Qual era exatamente a definição de refutação, e ela foi fixada antes?**

- **Resposta curta:** Refutação = não atingir 95% do Macro F1 da supervisão
  completa com ≤30% dos rótulos, *ou* não superar amostragem aleatória e
  incerteza pura com significância estatística. Fixada no Cap. 3, antes dos
  experimentos, junto com o *gate* de qualidade do oráculo.
- **Lastro:** Seção de método (protocolo/critérios pré-registrados).

---

## 2. Sobre a generalização (dataset único)

**P2.1 — Todos os resultados vêm de um único conjunto de dados, coletado e
rotulado por você. Como isso generaliza?**

- **Resposta curta:** É a limitação mais legítima do trabalho e está declarada
  como tal. Concedo que os *valores absolutos* são específicos do domínio.
  Defendo que os *achados estruturais* — a sensibilidade do L0, o viés
  bidirecional da autoavaliação, a divergência entre provedores de serving,
  o "menos é mais" — são mecanismos que não dependem deste dataset em particular.
  Por isso proponho como trabalho futuro a réplica no AlleNoise, um benchmark
  público de texto curto de produto.
- **Lastro:** Seção de limitações (Cap. 6); trabalhos futuros com AlleNoise
  nomeado. A base é pública (DOI Kaggle), então qualquer um pode contestar.

**P2.2 — Por que não usou um benchmark público consagrado desde o início?**

- **Resposta curta:** Porque a pergunta da tese é específica de texto curto de
  varejo em português com cauda longa severa (621 classes, >1000:1) — condição
  que os benchmarks anglófonos usuais não reproduzem. Construí e publiquei a
  base justamente porque essa célula não existia. O preço é a generalização
  limitada; o ganho é atacar o problema real.
- **Lastro:** Tabela de lacunas (Cap. 2), base publicada em 2022 com DOI.

---

## 3. Sobre o rigor estatístico

**P3.1 — Vários braços do E3′ e do E6 rodaram com semente única. Como você
defende conclusões sem repetição?**

- **Resposta curta:** Distingo dois níveis de afirmação. Onde faço afirmação
  *inferencial* — E6 vencendo o aleatório —, rodei a campanha de 8 sementes e
  reporto Wilcoxon (p=0,0078, 8/8). Onde o braço é de semente única, trato o
  resultado como *descritivo* e digo isso explicitamente; não anexo p-valor a
  ele. Não misturo os dois registros.
- **Lastro:** Campanha multi-semente E6 (`analysis_multiseed.json`); limitações
  declaram semente única em parte dos braços.

**P3.2 — Por que 8 sementes e não 30?**

- **Resposta curta:** Porque o teste de Wilcoxon pareado tem p mínimo de
  2/2^n; com 8 sementes o menor p possível já é 0,0078 < 0,05. Oito é o mínimo
  que permite significância bilateral — é uma escolha de desenho, não um número
  arbitrário. Mais sementes só apertariam o intervalo, não mudariam o sinal.
- **Lastro:** Cap. 3 (instrumentação estatística), justificativa do n.

**P3.3 — Por que McNemar em vez de um teste t nas comparações de oráculos?**

- **Resposta curta:** Porque as comparações são pareadas sobre as mesmas
  instâncias (dois oráculos veem os mesmos itens), e o desfecho é acerto/erro —
  McNemar é o teste correto para tabelas de concordância pareada, com a versão
  exata binomial quando há poucos discordantes. Um t-test ignoraria o
  pareamento.
- **Lastro:** Slide de reserva "Instrumentação estatística" (situação→teste).

---

## 4. Sobre o DRI-SL e a comparação com o AG

**P4.1 — O DRI-SL vence o AG. Mas a comparação foi justa? O AG estava bem
configurado?**

- **Resposta curta:** A comparação é *conservadora contra o DRI-SL*, não a
  favor dele. A auditoria de circularidade revelou que o envelope do AG estava
  inflado em 6,3 p.p. porque selecionava usando o rótulo que depois seria usado
  para avaliar. Corrigido isso, o DRI-SL — que não usa nenhum rótulo — ainda
  supera o melhor indivíduo do AG supervisionado. Ou seja, a vantagem real é
  maior do que a tabela mostra.
- **Lastro:** Auditoria de circularidade (P2), envelope do AG; tabela DRI-SL vs
  AG por |L0|.

**P4.2 — DRI-SL é só k-means com um heurístico de novidade lexical. Onde está a
novidade científica?**

- **Resposta curta:** A novidade não é o k-means — é *combinar* densidade
  semântica com variedade lexical para construir o L0 sem nenhum rótulo, e
  demonstrar empiricamente que isso resolve a partida a frio melhor que uma
  busca supervisionada cara. E a ablação DRI-SL-CS mostra qual componente
  carrega o ganho em cada regime: a novidade lexical ajuda no cold start mas é
  contraproducente na seleção contínua, onde o agrupamento por predição é que
  importa. É um achado, não um pressuposto.
- **Lastro:** Ablação DRI-SL-C / DRI-SL-CS (E6).

---

## 5. Sobre os oráculos LLM

**P5.1 — Custos de API mudam toda semana. Sua análise de custo não fica
obsoleta?**

- **Resposta curta:** Os *valores absolutos* datam, sim — declaro isso. Mas o
  que sustenta a conclusão são as *razões*: um spread de 26× de custo dentro de
  um empate estatístico de qualidade. Essa razão é muito mais estável que o
  preço em dólar, e a lição — "escolher oráculo é decisão de engenharia, não de
  qualidade" — não depende do preço do mês.
- **Lastro:** Tabela de oráculos P3 (US$/1k pareado com Macro F1); limitações.

**P5.2 — Você encontrou que o mesmo modelo gratuito diverge de si mesmo entre
provedores. Isso não é um bug seu, e sim variância de amostragem?**

- **Resposta curta:** Não é variância de amostragem: a divergência é
  estatisticamente significativa (p<0,001) sobre as mesmas instâncias, com
  temperatura controlada. É um achado de instrumento — o provedor de serving
  (quantização, versão de pesos, pós-processamento) faz parte da medição.
  Justamente por isso reporto a tripla (modelo, provedor, data) em toda medida
  de oráculo, em vez de só o nome do modelo.
- **Lastro:** E0/serving (P3, RQ4); a lição "a medição é parte do método".

**P5.3 — Você mediu o oráculo contra o seu próprio gabarito. E se o gabarito
estiver errado nos casos em que o LLM "erra"?**

- **Resposta curta:** Antecipei isso. A auditoria de gabarito (censo de
  conflitos, itens multi-gold) estimou um teto de acurácia de ~99,3% e, mais
  importante, a análise de erros mostrou que ~48% do "erro" do oráculo é
  convenção de catálogo — o LLM está semanticamente certo mas na categoria
  vizinha à convencionada. Ou seja, parte do erro medido não é ignorância do
  produto, e eu reporto essa decomposição em vez de esconder.
- **Lastro:** Auditoria de gabarito (Cap. 3/4); análise de 48% convenção de
  catálogo.

---

## 6. Sobre o viés de autoavaliação (E6)

**P6.1 — O viés que você mede (acurácia interna subestima, Macro F1
superestima) não é só reflexo do desbalanceamento do teste interno?**

- **Resposta curta:** O desbalanceamento é o *mecanismo* — não uma objeção. O
  ponto do E6 é que o praticante que decide liberar o modelo olha o teste
  interno e é enganado nas duas direções ao mesmo tempo, dependendo da métrica.
  E o braço de controle aleatório, com Δ≈0, prova que o efeito não é artefato
  do protocolo: só aparece quando há seleção ativa. A consequência de projeto —
  conjunto reservado obrigatório — é o que importa.
- **Lastro:** Protocolo pool/população; braço de controle aleatório Δ≈0;
  campanha 8 sementes (−17,1±1,0 p.p.).

**P6.2 — "Menos é mais" é contraintuitivo demais. Como você garante que não é
overfitting ao pool completo?**

- **Resposta curta:** O efeito é o inverso de overfitting: treinar com a
  amostra ativa (mais balanceada) supera treinar com o pool completo
  (desbalanceado) justamente na métrica *macro*, que pesa as classes raras. O
  pool completo tem mais dados mas também mais viés de frequência; a seleção
  ativa compra cobertura de cauda. E isso reaparece no BERTimbau do E3′ (E35
  supera D), então não é peculiaridade do classificador leve.
- **Lastro:** E6 (amostra ativa vs pool); E3′ E35 (70%) > D (100%) em Macro F1.

---

## 7. Sobre o framework e as entregas

**P7.1 — FALCO é um framework ou uma coleção de experimentos? Qual é a
contribuição integrada?**

- **Resposta curta:** É um framework, e a contribuição integrada não é uma
  estratégia de seleção nova — é a *disciplina de medição*: cada decisão do laço
  (como começar, quando parar, qual oráculo, como avaliar) vem de um critério
  pré-registrado e de um artefato rastreável. Os quatro pilares não são
  independentes: cada um responde uma pergunta e alimenta o próximo — começar
  bem, perguntar bem, pagar bem, integrar e testar.
- **Lastro:** Arquitetura FALCO (Cap. 3); catálogo executável (reproduzir/reprisar).

**P7.2 — O que garante que os números da tese são reproduzíveis?**

- **Resposta curta:** Reprodutibilidade clicável: a interface FlowBuilder tem um
  catálogo executável onde cada número da tese pode ser *reproduzido* (reexecutar
  do zero) ou *reprisado* (carregar o artefato gravado). A biblioteca
  activelearning é instalável por pip, com 80 testes, e a proveniência dupla
  (legado activetextclassification × biblioteca nova) foi verificada por
  igualdade de escores.
- **Lastro:** Catálogo `experiments_catalog.py`; auditoria de porte legado
  (10/10 números P2 conferem); declaração de proveniência dupla (Cap. 3).

**P7.3 — Você declarou uso de IA na confecção da tese. O que exatamente foi
feito por IA e como você garante a autoria?**

- **Resposta curta:** A declaração está no pré-textual e separa com honestidade:
  a concepção (pergunta, hipótese, FALCO, DRI-SL, desenho do E6), o dataset, os
  experimentos originais P1/P2 e todas as decisões metodológicas são minhas; a
  IA auxiliou na refatoração de código, na execução dos experimentos novos com
  parâmetros que eu defini, na instrumentação estatística e na redação sob minha
  direção e revisão. Nenhum número foi gerado sem artefato rastreável, e eu
  verifiquei e assumo a responsabilidade por todo o conteúdo.
- **Lastro:** Declaração de uso de IA (`0-iniciais/declaracao-ia.tex`);
  constituição "nenhum número sem artefato rastreável".

---

## 8. Perguntas-armadilha curtas (respostas de uma linha)

- **"Qual a maior fraqueza da tese?"** → Dataset único; declarada, com plano de
  réplica no AlleNoise.
- **"Se tivesse mais 6 meses, o que faria?"** → Parada ancorada no modelo forte
  (já medida como correção) e a réplica em benchmark público.
- **"O DRI-SL funcionaria em imagens/áudio?"** → O mecanismo (densidade +
  variedade sobre embeddings) é agnóstico à modalidade; não testei — seria
  especulação afirmar.
- **"Você usaria isto em produção amanhã?"** → Sim, com o gate de oráculo e o
  conjunto reservado obrigatório; o ciclo real já rodou a custo zero de oráculo.
- **"O que te surpreendeu?"** → O "menos é mais" e a divergência de um modelo
  consigo mesmo entre provedores.
- **"Qual número você mais confia?"** → O viés de −17,1±1,0 p.p. do E6: 8
  sementes, braço de controle, direção estável.
- **"E o que menos confia?"** → Os custos absolutos em dólar; por isso reporto
  razões.

---

### Postura na arguição

1. **Conceda rápido o que é justo.** "Sim, essa é uma limitação real" desarma e
   transmite maturidade. Está tudo declarado — não há o que esconder.
2. **Separe o descritivo do inferencial.** Só anexe p-valor onde há campanha de
   sementes. Onde é semente única, diga "é descritivo".
3. **Volte ao artefato.** Toda afirmação empírica tem um artefato por trás;
   quando pressionado, aponte-o em vez de argumentar.
4. **Não invente.** Se não mediu, diga "não medi, seria especulação". A banca
   respeita mais isso do que um número improvisado.
5. **Reancore no fio condutor.** Começar bem, perguntar bem, pagar bem,
   integrar e testar — quando a pergunta desviar, volte ao argumento em quatro passos.
