# Parecer — Painel de revisão simulado (5 assentos) · Decisão editorial

**Data**: 2026-08-23 · **Autora do parecer**: banca (síntese editorial da skill
`academic-paper-reviewer`, modo full) · **Alvo**: tese FALCO no estado da
branch `banca/esquemas-tikz-metodo` (main de 23/08 + passes dos 7 apêndices)
· **Relatórios integrais dos 5 assentos**: arquivo-anexo
`2026-08-23-painel-simulado-relatorios.md` no mesmo diretório.

**Transparência de método**: os cinco assentos foram executados em contextos
separados, sem visibilidade cruzada dos relatórios (regra do protocolo), mas
pela MESMA família de modelo — a separação de papéis produz corroboração de
achados, não erros estatisticamente independentes. Todo achado citado abaixo
existe em um relatório da Fase 1 (nada foi fabricado na síntese), e os dois
fatos decisivos foram re-medidos no texto antes da adjudicação.

## Decisão: REVISÃO MAIOR antes da defesa

Votos dos assentos: Banca-Fit **revisão menor** · Domínio **revisão menor** ·
Metodologia **revisão maior** · Perspectiva **revisão maior** · Advogado do
Diabo: 3 CRITICALs (adjudicados abaixo).

Arbitragem da divergência menor×maior: o que decide é a natureza dos itens de
topo — pelo menos dois exigem execução ou re-análise além de edição de texto
(E20 com rótulos de oráculo OU análise de limite; controle de multiplicidade;
idealmente semente 123 do braço E e braço D′), e todos tocam a cadeia central
de sustentação (hipótese → critério → veredito). Nota essencial: NENHUM
assento encontrou problema de integridade — o consenso unânime é que a tese é
incomum em honestidade (veredito negativo com autópsia causal, divergências
declaradas, vieses de medição quantificados). A revisão maior é de
completamento e enquadramento, não de correção de conduta; com o roteiro
abaixo cumprido, os quatro assentos avaliadores convergem para "defensável".

## Adjudicação dos CRITICALs do Advogado do Diabo (regra de ferro: visível, um a um)

**DA-C2 — deriva entre espelhos (Macro F1 do braço A vs. B): CONFIRMADO POR
MEDIÇÃO.** `6-conclusao/texto.tex:58-60` afirma "o braço com rótulos do
oráculo supera o de gabarito... na média das sementes" e o resumo diz que o
ruído "até beneficia as classes raras"; a Tabela e3p (`5-resultados-falco/
texto.tex:546-548`) dá A=0,297 < B=0,299 e o texto do próprio Cap. 5 diz
"praticamente empatam, com B à frente em duas das três sementes". Deriva
"empata"→"supera"→"beneficia" na direção que convém. Violação do princípio
VIII; correção textual obrigatória (P1.3). Bloqueia qualquer aceitação sem
correção.

**DA-C1 — o objeto do veredito não é o objeto da hipótese: VALIDADO (como
enquadramento e lacuna de execução, não como ocultação).** Corroborado por 4
dos 5 assentos por caminhos separados (Banca-Fit#3, Metodologia#3,
Perspectiva#2). A varredura que sustenta "atingível dentro do teto" usa
seleção e treino com gabarito, sem DRI-SL, sem fases, sem LLM; nenhum braço
com oráculo passa de 11.936 rótulos; a configuração aprovada pelo gate
(flash+pro, Fase 3) nunca rodou ponta a ponta. O próprio DA registra, nas
Observações, que o estatuto post hoc/gabarito é declarado em todos os
espelhos — portanto não há ocultação; há protagonismo do achado com gabarito
acima do que a evidência autoriza, e a pergunta nº 1 da banca real está aqui.
Remédio em P1.1.

**DA-C3 — denominador e régua lisonjeiros: PARCIALMENTE VALIDADO.** Os dois
re-baseamentos (teto sobre a base de 231.490; régua sobre o pool de 50 mil)
são declarados — não é cherry-picking oculto. Mas (a) a direção do efeito da
régua-pool (critério mais brando que o pré-registrado) não é quantificada
(Metodologia#2 estima 4-5 p.p. pela própria curva do PVBin), e (b) a fração
"% do pool selecionável" — o denominador da literatura, sob o qual 20 mil =
40% — não aparece nas manchetes. Remédios em P1.4 e P2.

## Consenso entre assentos (corroboração por ≥2 relatórios cegos entre si)

1. **Falta o ponta a ponta com oráculo** (4 assentos) — o flanco central.
2. **Contradição interna método↔resultados sobre sementes do E3**
   (Metodologia CRITICAL#1 + Banca-Fit MAJOR#2): `3-metodo/texto.tex:713-714`
   diz "semente única e estatuto descritivo"; o executado tem 3 sementes
   pareadas. Texto desatualizado no capítulo que responde a hipótese.
3. **Espelhos do Macro F1 A vs. B** (DA-C2 confirmado + Banca-Fit#4 no
   resumo).
4. **Terceira cláusula do critério da introdução (superar aleatória e
   incerteza com significância) nunca tratada no veredito** (Banca-Fit#1;
   tangente ao DA#3).
5. **Braço E com 2 sementes: declarado, não justificado nem sensibilizado**
   (Metodologia#5 + DA#10).
6. **Custo total e rótulos-ouro operacionais fora da contabilidade**
   (Perspectiva#1/#5 + DA#6): ~7 mil rótulos-ouro de bootstrap
   (gate+liberação) e 4.000 de validação/teste do ciclo real não entram no
   headline "5,2%"; GPU e tempo-de-parede sob vazão nunca monetizados.
7. **Apêndice A7 prescreve a política de parada que a própria tese refutou**
   (Perspectiva#3; DA#5 é o mesmo nervo pela circularidade operacional) — e
   os gatilhos de deriva têm números de aparência prescritiva sem validação
   (Perspectiva#4). [Registro honesto da banca: meu passe de forma no A7 não
   pegou essa contradição de conteúdo — achado genuíno do painel.]
8. **Três denominadores confundíveis** (Banca-Fit#6, Metodologia#9, DA#3):
   inclusive um deslize fatual — "8,6% da população" quando 20.000/177.490 =
   11,3%; os 8,6% são da BASE.
9. **Lacunas de literatura que desprotegem contribuições** (Domínio#1-4):
   critérios de parada (o achado central fica sem interlocutor!), PATRON na
   revisão e na tabela de lacunas, Wang2021 (GPT-3 como rotulador, JÁ NO BIB,
   nunca citado — corrige o "seminal" de Gilardi), LCE vs. deficiency de
   Baram 2004.
10. **Nenhum controle de comparações múltiplas** (Metodologia#4): decisões
    estruturais sobrevivem (p<0,001), mas "v4a +3,8 p.p. (p=0,045)" não
    sobreviveria a Holm na própria família.

## Roteiro de revisão priorizado

**P1 — antes da defesa (desarmam os ataques previsíveis da banca):**
1. **Fechar ou delimitar o ponta a ponta**: executar E20 com rótulos de
   oráculo (custo ~zero via nemotron; ~US$0,28 via flash, estimativa do
   Banca-Fit) OU simular o ruído medido (infra do E4) nos prefixos E20–E30 E
   recalibrar a redação do veredito/contribuição (i) enquanto isso não
   existir; projetar explicitamente o custo A−B (7,2 p.p.) sobre a folga do
   cruzamento (1,5 p.p. média; 0,7 pior semente).
2. Corrigir `3-metodo/texto.tex:713-714` ("semente única") para o desenho
   executado (3 sementes A–D, 2 no E).
3. Corrigir a deriva de espelhos do Macro F1 (conclusão l.58-60 e resumo)
   para "praticamente empatam" — medido nesta síntese.
4. Tratar a terceira cláusula do critério no veredito (ou emendar a
   formulação na introdução com a divergência declarada ali).
5. Unificar denominadores (sempre "% da base" na varredura; corrigir "8,6%
   da população"; adicionar a coluna/frase "% do pool").

**P2 — fortalecem substancialmente (artefatos existentes + 1-2 execuções):**
6. Semente 123 do braço E (um ajuste fino) ou coluna de sensibilidade
   2-sementes nos demais braços.
7. Braço D′ (BERTimbau na base deduplicada) ou análise de limite do
   afrouxamento da régua nas ameaças à validade.
8. Holm–Bonferroni por família de testes (re-análise; rebaixar o que cair).
9. Subseção de critérios de parada no Cap. 2 + posicionar o achado central
   como contribuição a essa linha; PATRON na revisão e na tabela de lacunas
   (com reescopo da contribuição (ii) OU uma baseline publicada de cold
   start); citar Wang2021GPT3Labeling; confrontar LCE com a deficiency.
10. A7: incorporar ao gatilho 1 a correção que a conclusão promete (piso de
    orçamento/checkpoints do forte) com remissão ao E3′; rebaixar gatilhos de
    deriva a "desenho proposto, não validado" + análise de poder da amostra
    de 200 sob erro de ~22%.
11. Tabela de custo total (tokens + GPU + tempo sob vazão + rótulos-ouro
    operacionais); precificar o braço A como se servido pelo flash.
12. Meia página de resultados-síntese do E5 (curvas, transições, parada em
    ação) — o único experimento ponta a ponta merece vitrine; ligar E2 às
    "3 épocas".

**P3 — menores (texto):** resumo de ~700 palavras num parágrafo (enxugar);
qualificador "descrições de produtos de varejo" nas frases-manchete da
conclusão; "8 sementes é o mínimo" (falso; n=6 já dá p=0,03125) → corrigir;
LCE: nomear o integrador para grade irregular + limitação LCE>1 (a tese vive
o caso E35>régua); ICs de Wilson na Tabela E3; Cohn1994→Freund1997 na
cláusula da garantia exponencial; conferir o "42×" de Kholodna contra o
fichamento; posicionar a biblioteca frente à small-text em uma frase; anos
divergentes no bib (Romberg2025/Yuan2025/Hanneke2015); typo "um uma"
(2-fundam:692); parágrafo ético (anotador→auditor; dependência de
provedores); licença/versão/instalação da biblioteca.

## Pontos fortes — consenso unânime dos 5 assentos

O veredito honesto com decomposição causal pareada (A/B/C/D/E); a medição
como objeto de pesquisa (provedor como parte do instrumento, p<0,001;
enum/free 0,0% vs. 6,8%; viés de autoavaliação −14/+34 p.p. com controle); a
anticircularidade do AG medida contra o próprio interesse (6,3 p.p.); a
disciplina estatística declarada antes do uso; a tabela de lacunas com
literatura 2025-26; "rotular tudo pode piorar" com mecanismo medido. Nas
palavras do assento mais duro (Perspectiva): "a instrumentação, a
honestidade do resultado negativo e a rastreabilidade estão acima da média
da área".
