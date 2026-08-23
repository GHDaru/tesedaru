---
de: revisor2
para: principal
tipo: aviso
acao_esperada: decidir quais dos 6 achados viram edição de prosa (é sua superfície de decisão); os 2 primeiros mexem em argumento, não só em forma — sugiro levar ao autor junto com o gate
referencia: tarefa 20260816-2205 · 2-fundam linhas 28-209 (t1) e 472-604 (t3) · princípio III (afirmações fundamentadas)
criada_em: 2026-08-17T00:38:11Z
---
R4 EXECUTADO nos meus dois temas. O princípio III diz que nenhuma afirmação
fica órfã: ou tem argumento explícito, ou citação que a sustente, ou dado.
Varri as duas faixas procurando exatamente isso. Nada foi editado — a decisão
de mexer na prosa é sua.

Aviso de saldo: os dois temas estão BEM citados. Achei 6 pontos, e só 2 são
graves. Descrevo do mais para o menos importante.

## 1. GRAVE — um "portanto" que não se sustenta (t1, inferência estatística)
O texto afirma, corretamente, que no teste de Wilcoxon com n pares o menor
p-valor bicaudal possível é 2/2^n, e que "com menos de SEIS sementes a
significância a 5% é inalcançável por construção". Conferi a aritmética: com
5 sementes o mínimo é 0,0625 (não alcança 5%); com 6 é 0,03125 (alcança).
A frase está certa.

O problema é a conclusão colada nela: "...o que fundamenta o mínimo de OITO
sementes adotado no Capítulo 3". Não fundamenta. O argumento apresentado
justifica SEIS. O salto de seis para oito não tem premissa no texto — pode ter
uma boa razão (margem de segurança, potência do teste, número de braços), mas
essa razão não está escrita, e é justamente o tipo de "portanto" que uma banca
puxa. Isto é primo do item R5-imediato que o plano já registra para o Cap. 3
("8 sementes é o mínimo para p<0,05 é falso"): a frase do Cap. 3 foi corrigida,
mas a inferência sobreviveu aqui no Cap. 2, agora em forma mais sutil.
Remédio barato: ou declarar a razão real do oito, ou escrever "fundamenta o
mínimo de seis, e esta tese adota oito por margem".

## 2. GRAVE — bloco de seis afirmações sem nenhuma fonte (t3, capacidades)
A passagem "as vantagens estruturais — escalabilidade sem fadiga, consistência
entre anotações, velocidade — convivem com limitações conhecidas: qualidade
inferior à de especialistas em domínios de nuance, vieses herdados do
pré-treinamento, alucinação e conhecimento datado" enfileira SEIS afirmações
empíricas sobre LLMs sem uma citação sequer. O parágrafo anterior é bem
ancorado (Gilardi 2023, com números), e o seguinte também; este ficou solto.
São afirmações que a área aceita, mas "a área aceita" não é fundamentação —
é exatamente o que o princípio III proíbe. Remédio: ancorar cada par em
fonte já presente no bib, ou reduzir a uma frase de transição sem pretensão
empírica.

## 3. MÉDIO — "raramente tratada na literatura", duas vezes (t3)
Aparece na abertura da seção ("dimensão raramente tratada de forma
sistemática") e de novo na subseção de custo ("raramente instrumentadas na
literatura"). É o mesmo achado Dom-M5 do parecer R6, que pediu citação para
alegações desse tipo — ainda em pé, e agora em duplicata. Alegação de LACUNA é
das mais caras de defender: exige mostrar que se procurou. Remédio: ou citar
uma revisão que constate a lacuna, ou converter em afirmação sobre o escopo
desta tese ("esta tese instrumenta..."), que não precisa de fonte.

## 4. MÉDIO — perfil de erro do oráculo dado como fato de fundo (t3, ruído)
"...exatamente o perfil de erro observado em oráculos LLM, cujas confusões se
concentram em pares de classes vizinhas". A segunda metade é uma afirmação
empírica sobre COMO os oráculos erram, colocada no Cap. 2 como conhecimento
estabelecido, sem citação. Se isso é achado NOSSO (E0/E4), precisa de reenvio
ao capítulo de resultados; se é da literatura, precisa de fonte. Hoje não tem
nem um nem outro.

## 5. LEVE — atribuição difusa (t3, ruído)
"Dois resultados importam diretamente: redes profundas toleram ruído moderado
quando há dados suficientes, mas degradam sob ruído estruturado." Vem logo
depois de três fontes (Frenay, Natarajan, Song), então a atribuição é
plausível por vizinhança — mas nenhum dos dois resultados está amarrado a uma
fonte específica. Como é a mesma tese que cobra rastreabilidade de número,
vale amarrar.

## 6. LEVE — propriedade do bootstrap sem fonte (t1)
"...permanecendo informativo mesmo com poucas repetições". A citação
(Efron e Tibshirani) cobre o método, não essa propriedade específica em regime
de poucas repetições. Ou se cita onde isso é demonstrado, ou se remove o
adendo, que não é necessário ao argumento.

## Situação da tarefa
R3 e R4 feitos, nada editado. Falta o R1 (humanização) dos dois temas, que é
edição de forma e posso tocar em branch assim que você decidir o destino
destes 6 pontos — não faz sentido humanizar frases que talvez sejam
reescritas por mérito. Sigo aguardando também a decisão sobre fichamento de
obras canônicas (mensagem das 00:29, com a correção de número que publiquei
às 01:0x: são 15 canônicas, não 19).
