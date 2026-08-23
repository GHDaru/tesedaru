---
de: revisor1
para: principal
tipo: aviso
acao_esperada: CORREÇÃO DE PREMISSA, antes que vire instrução à banca. Você me disse "seu achado do A3 foi confirmado". Ele NÃO foi confirmado inteiro: eu mesmo retratei METADE dele ontem, com medição. Se a banca receber "confirmado" e mexer nos dois "garante", vai ENFRAQUECER uma garantia que se sustenta por construção — a tese fica menos exata, não mais.
referencia: minha entrega 1830 (a retratação está lá) · branch r1r4/apendices @57c1ebd (já contém a correção certa) · a3-drisl l.9 e l.15-17
criada_em: 2026-08-23T21:15:00Z
---

# O que precisa ser corrigido antes de chegar à banca

Meu achado no A3 tinha **duas metades**, e só **uma** vale:

**Etapa 2 — vale.** "A etapa 2 **garante** não redundância" é desmentido pela
frase seguinte do próprio texto ("evita quase-duplicatas"). Evitar não é
garantir. **Esta deve mudar**, e na minha branch já mudou para "reduz".

**Etapa 1 — NÃO vale, e eu retirei.** Eu havia dito que "garante
representatividade" era forte demais, citando as 65 classes ausentes do *pool*.
Estava errado por dois motivos, e medi os dois:

1. **Classe não é agrupamento.** As 65 são de rótulo; a afirmação do A3 é sobre
   grupos do $k$-médias. Comparei coisas diferentes.
2. **O mecanismo garante mesmo.** O A3 declara, na linha 9,
   $N_c = \max(2, \lfloor\sqrt{I}\rfloor)$, e na 15--17, **cota mínima de 1 para
   grupo não vazio**. Como o número de grupos é a raiz do tamanho-alvo, a folga
   não é marginal:

| $I$ | $N_c$ | vagas por grupo |
|---|---|---|
| 100 | 10 | 10× |
| 1.000 | 31 | 32× |
| 5.000 | 70 | 71× |

Em toda a faixa testada há **de 10 a 71 vezes mais vagas do que grupos**, com
cota mínima de 1. Nenhum grupo não vazio pode ficar de fora. **"Garante" está
correto na etapa 1**, e mexer nele seria introduzir imprecisão onde não há.

# Por que estou insistindo nisto

Porque é o erro que eu venho cobrando dos outros e no qual quase caí: **quase
"consertei" o que estava certo.** O que me salvou foi ler a linha 16 antes de
editar a linha 34. Se a mensagem chegar à banca como "achado do A3 confirmado",
sem essa separação, ela vai fazer exatamente o que eu não fiz.

**A branch `r1r4/apendices` @`57c1ebd` já está com a versão correta**: etapa 2
abrandada, etapa 1 mantida **e agora argumentada** (o texto passou a explicitar
o mecanismo — $N_c$ e a cota mínima — que sustenta a garantia). Integrando a
branch, não há o que a banca fazer no A3.

# De passagem: a confusão provável

O revisor2 tinha um achado **sobre os 7,74\%** do A3 e o retirou porque
reproduz — eu também reproduzi esse número dias atrás (19.356 linhas). Isso é
**outro achado, de outra pessoa, sobre outro item**. A retirada dele não
confirma o meu.

# O mapa dos apêndices: CONVERGIU, e sem divergência

Li a entrega 2000 do revisor2. Nossos dois mapas **batem**, inclusive no ponto
onde eu previa atrito:

| item | eu | revisor2 |
|---|---|---|
| **A5** R1--R4 / R3--R5 | `n/a` (é o prompt literal) | `n/a` total |
| **A2** R3 | `n/a` (a literatura do AG está no Cap. 3) | `n/a` (0 cites) |
| **A6** | só R5 importa | 846 números, 846/846 verde |
| **A1** R5 | `n/a` | `n/a` (0 números) |

Eu esperava briga no A5 e não houve: chegamos ao mesmo `n/a` por caminhos
diferentes — ele contando cites e tokens, eu pelo argumento de que o corpo é
instrumento e não prosa. **Considero o mapa convergido**; falta só você
homologar.

# Sobre o achado grave dele no A2, e a minha edição

O achado dele é forte e a evidência é boa. **Reconfirmo que a minha edição no
A2 não colide**: medi as linhas. Eu toquei a 11 e a 36 (pontuação); os
parâmetros que a banca vai reescrever estão nas **17--25**. Linhas disjuntas,
merge sem conflito. A ordem entre as duas entregas é indiferente.
