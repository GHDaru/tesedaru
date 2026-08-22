---
de: principal
para: banca
tipo: tarefa
acao_esperada: LOTE de correções pontuais achadas pelo revisor2 (todas "uma oração/uma célula", com proposta dele) — BAIXA prioridade, DEPOIS do Cap.4 (l.117) e da F6. Branch única; cruzada do revisor2 (são achados dele); gate do autor.
referencia: revisor2 1612 (achados 2,3 + 96%, Settles) e 1608 (divergências 2 e 3 da R4, com redação proposta)
criada_em: 2026-08-22T21:00:00Z
---

Seis correções, todas de texto, com a medição/proposta do revisor2:
1. **795 categorias**: a régua do gate-85 (89,56%) é medida em 795 classes; a
   tese compara com oráculos em 621 como se fosse a mesma régua. "795" não
   aparece em capítulo nenhum. Uma oração declarando a diferença de espaço de
   rótulo (favorece a tese: 795 é mais difícil, régua no máximo subestimada).
2. **Wertz2022 (2-fundam:400)**: a glosa "(centenas de classes)" descarta que
   o artigo é MULTIRRÓTULO — e é a metade multirrótulo que faz o resultado
   negativo não valer aqui. Ajustar a glosa para não importar multirrótulo
   para uma tese de rótulo único (resolve a tensão com o E1 do Cap.5).
3. **96% -> 95%** no Cap.6 (número errado).
4. **Settles2009**: o "menos de 10%" atribuído a ele — a ficha desautoriza
   números; ajustar conforme a ficha.
5. **Divergência 2 da R4** (entropia): resposta é (a) — o framework rodou
   entropia; o E1 não testa margem contra entropia (elege por estimativa
   pontual). Redija a distinção que o revisor2 propôs (não é contradição).
6. **Divergência 3 da R4** (epsilon): são DUAS constantes diferentes, não uma;
   a comparação favorece a tese. Redija a reconciliação proposta pelo revisor2.
Pegue os textos exatos nas mensagens 1612 e 1608 do revisor2. Não invente
número sem ele.

## Resultado (banca, 2026-08-22)

Entregue em `banca/lote-2100-pontuais` @aa669ec (base: origin/main, 5 arquivos,
+41/-20). As seis, na ordem da tarefa: (1) regua 89,56% declarada como medida
nas 795 categorias de menor nivel, espaco maior que as 621 da amostra dos
oraculos (3-metodo, gate-85); (2) glosa do Wertz2022 corrigida para
"multirrotulo extrema (centenas de rotulos possiveis e varios rotulos por
texto)" + oracao com o C3 do Wertz (baixa co-ocorrencia; rotulo unico e o
extremo) + contraponto Rouzegar2024 C3 (2-fundam:400); (3) 96%->95% no Cap.6
l.87; (4) Cap.1: "menos de 10%" removido, Settles2009 fica como revisao
canonica que estabelece o fenomeno, numero fica so no Schroder2022 (fichado);
(5) 3-metodo: redacao do revisor2 adaptada — Fase 2 seleciona por entropia,
varredura mostra estimativas pontuais superiores de margem/confianca SEM
teste entre si (comparacao medida e contra a aleatoria), troca registrada
como extensao imediata; (6) 3-metodo separa tolerancia de ruido amostral e
remete ao A7, que agora traz a reconciliacao completa (eps=1e-3 nao deriva de
1/sqrt(2000)=0,0224; e ~20x menor; parada nao e efeito de tolerancia estrita).
Nenhum numero fora dos medidos pelo revisor2. check-bib: PROBLEMAS nenhum;
check-travessao: nenhum. Proximo passo: cruzada do revisor2 (achados dele) e
gate do autor via principal.

ACHADO no caminho (para triagem do principal): 5-resultados-falco l.243-244
diz "a ablacao de lote repete a entropia, estrategia PRE-REGISTRADA da
Fase~2" — o pre-registro (deck) nao fixa estrategia de selecao; apos a
reancoragem do termo no Cap. 3, essa ocorrencia ficou mais forte do que o
documento sustenta. Nao editei (fora do escopo "uma oracao" do lote e
superficie ja em discussao do veredito); sugiro rotear para decisao.
