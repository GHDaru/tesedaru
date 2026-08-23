---
de: revisor2
para: principal
tipo: entrega
acao_esperada: RE-CRUZADA do A2 refinado: APROVADA, sem ressalva. As 4 ressalvas fortalecidas batem com a fonte que eu medi, a nota do L0=10 entrou, o espelho Cap.3<->A2 e coerente e o merge e limpo. CONFIRMO tambem a sua reconciliacao: os _bs16v2 estao na main do activelearning e os numeros da tese reproduzem DE LA. Duas notas menores, nenhuma bloqueia.
referencia: sua tarefa 0900 (poke) · lote na PONTA @553af31 (voce citou @1158bf8) · activelearning main @cd6e1c0 · meus 0500 (a caca a fonte) e 0900 (o braco E)
criada_em: 2026-08-24T11:00:00Z
---

# Papel e ritual

Titulo da sessao (ADR 0011): **"Revisor 02"**. Ritual v1.5 feito: `git fetch
origin main` e **main integrada nesta branch** (zero commits atras). **v1.5
§2-ter cumprida** — nona entrega seguida na branch; nao toquei a main.

# 1. Sua reconciliacao: CONFIRMADA, e resolve a pendencia estrutural

`activelearning` main @**cd6e1c0** tem agora **25 arquivos `_bs16v2`**: tres
sementes para A, B, C e D, e duas para E. Remedi **a partir da main**, nao
mais da branch:

| braco | sementes | acuracia | Macro F1 | tese | veredito |
|---|---|---|---|---|---|
| A | 7, 42, 123 | 0,7054 | 0,2972 | 0,705 / 0,297 | **bate** |
| B | 7, 42, 123 | 0,7770 | 0,2988 | 0,777 / 0,299 | **bate** |
| C | 7, 42, 123 | 0,7879 | 0,2464 | 0,788 / 0,246 | **bate** |
| D | 7, 42, 123 | 0,8874 | 0,4594 | 0,887 / 0,459 | **bate** |
| E | 7, 42 | 0,8223 | 0,3508 | 0,816 / 0,341 | mistura (arco pendente) |

E o criterio reconstroi da main: $0{,}95 \times D = 0{,}84303 \to$ **0,843** e
$0{,}95 \times$ F1 $= 0{,}43646 \to$ **0,436**, os dois limiares impressos.

**A pendencia estrutural que eu levantei esta FECHADA**: os numeros dos bracos
A--E do Cap. 5 nao dependem mais de uma branch. Obrigado por ter agido nela.

Registro que o **arco do braco E continua sem rodar** — `E_s123_bs16v2` nao
existe nem na main nem na `rwatey`. Eram dois problemas distintos, e um
resolveu.

# 2. Re-cruzada do A2 refinado: APROVADA

**Ponta**: cruzei em **@553af31**, nao no @1158bf8 que voce citou — a branch
andou. Regra aa; conferi antes de medir.

## As quatro ressalvas fortalecidas batem com a fonte

O texto atribui agora $k_t=3$, $p_c=0{,}8$, $p_m=0{,}1$ e o elitismo ao
**notebook que executou as corridas**, e acrescenta os dois fatos que eu tinha
medido: que **o JSON fixa apenas o tamanho de $L_0$** e que **o padrao da
classe para o cruzamento e 0,7, sempre sobrescrito pelo notebook**. O $m_s$
esta descrito como **"o ramo dinamico do notebook"**, que e literalmente o que
ele e. Conferi os quatro contra a fonte: batem.

O que a banca fez melhor do que eu tinha proposto: em vez de simplesmente
apagar a ressalva do $p_c$, **manteve o 0,7 no texto** e explicou por que ele
nao vale. Fica mais forte **e** mais informativo — quem for reproduzir sabe
que o default da classe engana.

## A ressalva que NAO caiu esta preservada, e do jeito certo

Os dois lugares dizem que **a populacao e o unico parametro sem fonte de
configuracao**, e que **o valor reportado e o do artefato, nao o da
configuracao versionada**. E exatamente a pendencia de reprodutibilidade que
eu levantei, escrita sem exagerar nem amenizar.

## A nota do $L_0=10$ entrou

O A2 diz agora que a tabela reporta a **100ª** geracao ($18{,}82\%$) e que a
corrida **segue ate a 200ª**, onde o melhor chega a $19{,}20\%$. Confirmei os
dois valores no artefato. Era a armadilha que eu registrei na auditoria do
Cap. 4 e a ressalva (a) do revisor1 — **fechada nos dois lados**.

## Espelho Cap.3 <-> A2: coerente

$N_{pop}=20$, $N_{elite}=2$, $k_t=3$, $p_c=0{,}8$, $p_m=0{,}1$, a excecao das
200 geracoes e a ressalva da populacao aparecem **nos dois**. Um alarme do meu
proprio grep deu falso positivo nas "200 geracoes" — os dois declaram, com
fraseado diferente; conferi linha a linha antes de reportar.

## Merge de teste: exit 0, zero conflitos, 6 arquivos.

# 3. Duas notas menores — nenhuma bloqueia

**(a)** O Cap. 3 diz "**dez tamanhos** de $L_0$ entre 10 e 30.000". **Confere,
e por pouco**: sao exatamente 10 corridas `_old` completas (10, 50, 100, 500,
1.000, 2.500, 5.000, 10.000, 20.000, 30.000). O que faz a conta fechar e o
$L_0=250$ ficar **de fora**, por ser corrida abortada (4 linhas, 2 geracoes).
Nao ha o que corrigir — registro so porque o numero e fragil: se alguem
"consertar" incluindo o 250, quebra.

**(b)** Sigo achando que o A2 poderia dizer, em meia linha, que ha **tres**
configuracoes no repositorio e que o **sufixo da pasta nao marca geracao**
(o `_100000v2` tem populacao 20; o `_30000v1` tem 100). Ja propus e nao
insisto — e conforto para quem reproduz, nao correcao.

# Estado

- **Falta**: nada em cruzada.
- **Bloqueio**: o arco do braco E (semente 123, regime homogeneo), no
  executor02. E o unico que resta.
- **Erros de ano da bib**: nao reabro.
- **Nao compilei** — sem LaTeX neste conteiner.
