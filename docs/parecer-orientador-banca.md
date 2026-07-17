# Parecer simulado — orientador e banca (pré-defesa)

Exercício solicitado pelo autor em 17/07/2026: crítica do trabalho nos papéis
de professor orientador e de banca examinadora. Complementa (não substitui) as
revisões simuladas R1–R3. Tom deliberadamente franco.

---

## 1. Na voz do orientador

Gilsiley, o trabalho amadureceu muito e rápido — a distância entre o draft e o
manuscrito atual é a distância entre uma coleção de experimentos e uma tese.
Três méritos que vou defender na banca sem hesitar: o rigor de instrumentação
(vocês raramente verão uma tese em que o INSTRUMENTO tem barra de erro), a
reprodutibilidade real (qualquer membro da banca pode reexecutar o replay do
P1 em uma tarde), e a honestidade — o E0-P negativo na S-strat está reportado
com o mesmo destaque do positivo, e isso vale mais que dez resultados bonitos.

Agora o que eu preciso te dizer como orientador:

**a) Você tem uma tese de MÉTODO tentando se vestir de tese de RESULTADO.**
O título e a hipótese prometem o framework validado; o corpo entrega (i) uma
anatomia de custo/erro de oráculos LLM que é a melhor que já vi para
português, (ii) um algoritmo de cold start com evidência forte, (iii) um
protocolo experimental exemplar — e (iv) um E3 desenhado mas não executado.
Minha orientação: reposicione UMA frase na introdução e uma na conclusão para
que o leitor entenda que a contribuição principal é o método+instrumental, e
que o E3 é a primeira APLICAÇÃO dele. Se o E3 rodar antes da defesa, ótimo,
você sobe o sarrafo; se não rodar, a tese continua de pé sobre P1–P3.

**b) Defina a data de corte do bloco H agora.** Você tem GPU, scripts prontos
e um notebook de Colab. O risco real não é técnico, é de agenda: E2+E3 com 8
sementes são dias de computação e você ainda precisa escrever os números.
Proponho: duas semanas para E2+E3; se estourar, defendemos com o texto atual
(que já declara a lacuna) e o E3 vira artigo pós-defesa.

**c) O ciclo de 30k que você pediu hoje: cuidado com a leitura.** Rotular 60%
do pool aproxima qualquer estratégia do teto do oráculo — o valor do AL
aparece no primeiro terço da curva. Use o resultado para mostrar SATURAÇÃO
(onde parar de pagar), não para comparar estratégias no final da curva. É
exatamente o argumento do seu critério de parada; o experimento de hoje é a
ilustração perfeita dele se você o ler assim.

**d) Pequenas dívidas de texto** (uma tarde de trabalho): fotografia
(modelo, provedor, data) nas ameaças à validade; frase de contingência do
ranking E1→E3; o guia de parada/drift como apêndice; agradecimentos e
dedicatória reais antes do depósito.

## 2. Na voz da banca

**Examinador 1 (metodologia experimental).** "O candidato construiu um
protocolo acima do padrão da área — pré-registro, partições imutáveis,
anticircularidade DEMONSTRADA com −6,3 p.p., análise pareada correta. Minhas
arguições: (i) por que devo acreditar que o ranking de estratégias medido com
um classificador de protótipos transfere para o transformer que o framework
de fato usará? (ii) o senhor quantificou o efeito do instrumento de saída
(enum), mas o instrumento de PROMPT variou entre provedores? (iii) com 8
sementes o menor p é 0,0078 — o senhor reportaria o mesmo efeito com 20
sementes? Por que 8 e não mais, sendo o custo simulado?" *(Resposta esperada:
(i) limitação declarada + revalidação no E3; (ii) prompt idêntico v3 em todos,
só o modo de saída variou — está no Cap. 3; (iii) 8 é o mínimo com folga para
o teto de significância; nas células simuladas do E1/E4 o custo de subir é
pequeno e é uma extensão razoável — boa sugestão.)*

**Examinador 2 (PLN/AL).** "A frente AL+LLM está bem coberta até 2026, e o
posicionamento contra ActiveLLM/Rouzegar é claro. Três perguntas: (i) o
DRI-SL vence o envelope do AG, mas o AG otimizava a MESMA função que o DRI-SL
aproxima? Se a aptidão do AG fosse diversidade+densidade, o envelope seria
outro; (ii) por que k-means e não uma seleção por facility location, que tem
garantias?; (iii) a taxa de inválidos do nemotron (2,6% na S-strat) entra
como erro — o senhor testou re-prompting simples antes de descartar?"
*(Respostas: (i) o AG otimizava desempenho direto — o ponto é justamente que
uma heurística sem rótulos alcança o envelope de quem VIU rótulos; (ii)
custo O(n·k) e determinismo; facility location é trabalho futuro legítimo;
(iii) não — uma rodada de retry elevaria a acurácia efetiva; fica como
melhoria de engenharia declarável.)*

**Examinador 3 (aplicações industriais).** "A contabilidade de custo com
cache e lote é a contribuição que a indústria vai citar. O achado de serving
(mesmo modelo, provedores divergentes, p<0,001) merece seção própria — hoje
está num parágrafo. O FlowBuilder demonstra o protocolo fora do papel. Minha
crítica: o guia de drift está na documentação do software, não na tese — a
banca avalia a tese; traga-o para um apêndice. E a rotação de credenciais
pós-experimentos deve constar como prática de pesquisa responsável."

**Pergunta incômoda provável (qualquer examinador):** "Se o oráculo LLM
empata com o gratuito e o classificador leve com 250 mil rótulos bate 89,6%,
por que uma empresa não rotularia TUDO com o LLM de custo zero e treinaria o
leve — sem aprendizado ativo nenhum?" *(Resposta que o texto já suporta: é o
braço oráculo-total do E3 — a decomposição ruído×parcimônia existe para
responder exatamente isso; com oráculo a US$ 0, a parcimônia perde valor
monetário mas mantém valor de LATÊNCIA/vazão (30k rótulos ≈ 12h no serviço
gratuito) e de curadoria — e o E4 mostra que treinar com 100% de rótulos a
~78% de acurácia tem teto pior que selecionar bem. Ensaie essa resposta: ela
é o coração da defesa.)*

## 3. Síntese do parecer

| Quesito | Avaliação |
|---|---|
| Contribuição científica | Forte em método/instrumentação; condicional em resultado final (E3) |
| Rigor | Acima do padrão da área; reprodutibilidade exemplar |
| Redação | Madura; pequenas dívidas listadas (uma tarde) |
| Riscos para a defesa | Agenda do bloco H; pergunta do "por que não rotular tudo"; transferência PVBin→BERTimbau |
| Recomendação | **Apta a seguir para defesa após bloco H OU com reposicionamento de uma frase (método como contribuição central)**; correções menores da R3 |
