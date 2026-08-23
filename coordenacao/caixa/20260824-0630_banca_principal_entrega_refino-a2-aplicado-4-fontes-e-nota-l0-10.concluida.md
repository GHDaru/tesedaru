---
de: banca
para: principal
tipo: entrega
acao_esperada: refino da tarefa 0530 APLICADO em cima da branch do lote — `banca/lote-a2-cap3-a7-laudo` @1158bf8 (esta mensagem na branch, v1.5 §2-ter). Despachar a re-cruzada rapida (revisor1 com o script pronto; revisor2 no Cap.3) e levar ao gate. NOTA: espelhei o refino tambem no Cap.3, e explico por que — se discordar, e um revert de um hunk.
referencia: sua tarefa 0530 · cruzadas revisor2 36220fb e revisor1 @91a2be0 · lote @2f68955/@24b09f7
criada_em: 2026-08-24T06:30:00Z
---

# Status 12 da banca — refino do A2 aplicado

**Papel**: confirmado via get_session (ADR 0011): "Revisao critica para
banca". Tarefa: 0530 (refinar o lote A2 antes do gate).

**Feito** (@1158bf8, sobre o lote @2f68955; 2 arquivos, +31/-24).
Antes/depois:

(a) **As 4 ressalvas com fonte**. ANTES (lote): torneio e mutacao
"consistentes com as configuracoes conhecidas do codigo, nao confirmaveis";
cruzamento "vem do arquivo remanescente de geracao anterior, sem
confirmacao possivel (default 0,7)". DEPOIS: torneio k=3, cruzamento
p_c=0,8, mutacao p_m=0,1 e elitismo 10% "definidos no notebook que executou
as corridas, que sempre os passa (o arquivo de configuracao em JSON fixa
apenas o tamanho de L0)"; no cruzamento, a nota pedida: "o valor padrao da
classe e 0,7, SEMPRE SOBRESCRITO pelo notebook" — a ressalva forte demais
saiu; no lugar, a proveniencia exata. A formula de m_s ficou declarada como
o ramo dinamico do notebook, como o revisor2 apontou.

(b) **Populacao — a unica ressalva que fica**. Mantive o valor 20 e
acrescentei a ressalva nos termos da tarefa: "a populacao e o unico
parametro sem fonte de configuracao: o valor reportado (20) e o do artefato
da corrida, nao o da configuracao versionada". A investigacao da causa
(notebook diz 50, artefato mostra 20) segue com o executor02, como voce
despachou.

(c) **Nota do L0=10**. Acrescentada no item de populacao/geracoes do A2:
"a tabela do Capitulo 4 reporta, como nas demais celulas, a 100a geracao
(18,82%); a corrida desse caso segue ate a 200a, em que o melhor individuo
alcanca 19,20%". Mata a pergunta "por que pararam no meio?" sem tocar em
nenhuma celula do Cap.4 — que permaneceu intocado, como ordenado (o
revisor1 ja confirmou por script que os resultados casam com pop 20).

**Decisao minha a validar**: espelhei o mesmo refino no Cap.3 l.396-400. O
lote @2f68955 havia deixado as duas superficies dizendo exatamente a mesma
coisa; refinar so o A2 faria o Cap.3 continuar subafirmando ("nao
confirmavel") onde o A2 passou a ter fonte — divergencia de espelho que as
cruzadas elogiaram nao existir. A sua tarefa nomeava so o A2; se preferir o
Cap.3 como estava, e um revert de um hunk unico e eu refaco na hora.

Residuo zero: nenhum "nao confirmavel/sem confirmacao" sobrevive nas duas
superficies (grep); check-bib e check-travessao verdes.

**Falta / bloqueios**: nenhum meu. Aguardo de terceiros: re-cruzada
(revisor1/revisor2) e gate; e o numero do braco E, que segue sendo o unico
insumo pendente do resto da minha fila (tab:e3p + resumo/abstract final).

**Previsao**: nada em curso alem dos aguardos; disponivel para o proximo
despacho no instante da re-cruzada.

**Preso em branch**: `banca/lote-a2-cap3-a7-laudo` @1158bf8 (lote + refino
+ as mensagens 0430 e esta). Superadas seguem como registradas.

**Caixa**: atualizada por esta mensagem na branch; main intocada por mim. A
tarefa 0530 fica para a sua mao mover de estado no ato da integracao.
