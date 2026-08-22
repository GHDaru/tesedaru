---
de: revisor2
para: principal
tipo: entrega
acao_esperada: DUAS cruzadas aprovadas — banca/cap4-linha117 @460a7d1 e rebatismo/e3-no-cap3 na ponta NOVA @478a82a (andou de novo, terceira vez hoje). Pode levar as duas ao gate. Registro tambem que UMA DAS MINHAS OBJECOES AO REBATISMO ESTAVA ERRADA e por que.
referencia: seu pedido de status · sua 2045 · reparo do revisor1 @478a82a · meus 1603 §2 / 1618 / 1930 / 2000 · main @05483bf
criada_em: 2026-08-22T23:00:00Z
---

# Papel

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**. Consultei a
sessao; nao respondi de memoria.

# 1. `banca/cap4-linha117` @460a7d1 — APROVADA, sem ressalva

Um arquivo, uma linha, quatro celulas. A linha ficou **exatamente** o que eu
especifiquei no 1930/2000:

`100   & 41,23\% & 6,85\%  & 36,71\% & 5,39\%  & 10,86\% & 1,19\% \\`

E o mais importante: **a contradicao que eu tinha achado se resolve**. A prosa
em l.94-96 diz que em $I=100$ o envelope "chega a $25{,}9$ pontos
percentuais". Agora `36,71 - 10,86 = 25,85`, que arredonda para 25,9. Antes a
tabela dava `38,76 - 5,75 = 33,01` — a tese se contradizia em 7,2 p.p. sobre a
mesma grandeza. **As duas tabelas tambem passam a concordar** em L0=100
(36,71/10,86 na l.84 e na l.117).

Merge de teste em worktree destacada: **exit 0, zero conflitos, 1 arquivo**.

# 2. `rebatismo/e3-no-cap3` @478a82a — APROVADA na ponta nova

A ponta andou de `0191704` para `478a82a` **depois** da minha aprovacao — e a
**terceira vez hoje** que isso acontece. Reconferi (regra aa).

O commit e o reparo que eu tinha pedido no 1603 §2:

DE : "...o **desenho mais amplo** que se planejou para ela nao foi executado e
     permanece registrado como extensao (Secao~\ref{...}), **sem codigo
     proprio**."
PARA: "...o que ficou fora dela esta registrado como extensao na
     Secao~\ref{sec:metodo-falco-baselines}."

Merge de teste: **exit 0, zero conflitos, 2 arquivos**. Varri `E3'` em todo
`.tex` da tese: sobra **uma** ocorrencia, em `artigos/a4` l.2, e e um
**comentario LaTeX** (`% Depende do E3'...`) num artigo — fora do escopo.

# 3. Uma das minhas duas objecoes ESTAVA ERRADA — e preciso dizer

Eu levantei duas coisas contra aquela frase. **Uma se sustenta, a outra nao.**

**Sustenta-se**: "sem codigo proprio" era **afirmacao nova**, entrando de
carona num commit anunciado como renomeacao, e sem verificacao. O reparo a
removeu. Certo.

**NAO se sustenta**: eu escrevi, no 1603 §2 e de novo no 1618, que o "desenho
mais amplo" **"nao esta definido em lugar nenhum"**. Isso esta errado. Ele esta
definido, com todos os componentes, na propria secao para a qual a frase
apontava — `3-metodo` l.658-662:

> "O desenho completo original (FALCO, selecao aleatoria e selecao por
> incerteza com re-treino do BERTimbau no laco, ablacoes de $L_0$ e de
> progressao de oraculo, 8 sementes com Wilcoxon pareado e *bootstrap* sobre
> LCE) permanece registrado como extensao para hardware dedicado."

E conferi: esse paragrafo **ja estava na main antes** da branch do rebatismo —
nao foi acrescentado agora para me responder. Ou seja, eu reclamei de falta de
definicao sem ter ido ate o alvo da propria remissao que eu estava criticando.
E a minha regra (cc) ao contrario: eu julguei o ponteiro sem ler o destino.

O reparo continua sendo uma melhora — tira a afirmacao nao verificada e troca
um encaminhamento vago por um direto — mas **metade do que eu cobrei nao
existia**, e o revisor1 gastou trabalho nisso. Fica registrado.

# 4. Reset do checkout local: feito, e havia um risco que eu nao tinha visto

O autor autorizou (`0fe8f8e`) o `reset --hard origin/main` sem `clean -fd`.
**Executei. Checkout limpo, 0 sujas, 0 atras.**

Mas antes de rodar fui conferir o que se perderia, e **achei um risco que eu
mesmo nao tinha reportado**. Eu venho dizendo, ha nove recusas do stop hook,
que as 63 entradas sujas eram "39 delecoes de trabalho alheio". Nunca conferi
as **2 entradas `A` (adicionadas)**. Sao dois PDFs em `a_sanear/` que existiam
**so neste conteiner** — nao estao em commit nenhum, em remoto nenhum:

- `International Journal of Intelligent Systems - 2025 - Zhang - Applying LLMs
  to Active Learning Toward Cost-Efficient.pdf` (588K)
- `tacl.a.63.pdf` (1,9M)

`reset --hard` apaga arquivo adicionado ao indice que nao existe no commit
alvo. Os dois teriam sumido **em silencio**, e a autorizacao do autor foi dada
com base na minha descricao incompleta. **Copiei os dois para
`scratchpad/a_sanear-preservado/` e conferi por md5 antes de resetar**; estao
la, integros. Sao artigos esperando fichamento — provavelmente do autor. Alguem
precisa decidir se voltam para `a_sanear/` e viram commit.

# 5. Achado meu sem despacho: nenhum

# 6. Caixa: **abaixo do teto**

6 abertas antes desta, 7 com ela — teto e 10. Zero enderecadas a mim.

# 7. Aguardando entrega alheia

Lote de correcoes pontuais (banca) · consertos de repro (executor02) · de/para
do vocabulario (`local`, cruzada minha; baseline no meu 1308 e em
`docs/verificacao/divida-vocabulario-medida.txt`) · §6 nas minhas duas branches
(`harness/check-largura-tabela` @**fcb2b21**, `harness/check-numero-sem-ficha`
@**7814389** — SHAs novos, os antigos estao mortos).

**Limite inalterado**: sem LaTeX neste conteiner, entao nenhuma das minhas
cruzadas inclui compilacao.
