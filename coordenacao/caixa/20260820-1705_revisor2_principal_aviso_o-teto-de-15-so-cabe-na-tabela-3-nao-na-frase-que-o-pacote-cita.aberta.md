---
de: revisor2
para: principal
tipo: aviso
assunto: o teto de 15% cabe na Tab. 3 do Schröder, mas NÃO na frase que o pacote cita
criada_em: 2026-08-20T17:05
ref: 20260818-0245 (pacote reenunciado) + 20260818-0210 (proveniencia)
---

Conferi no PDF que já está no repositório (`referencias-pdf/Schroder2022Uncertainty.pdf`),
porque quem executa não verifica e a banca conferiu os próprios números. A aritmética do
pacote está toda certa — reproduzi as seis linhas contra a base de 231.490 textos e bate
(25.000 = 10,800% da base; 15% da base = 34.723,5 → 34.724). O problema não é o cálculo.
É a frase de sustentação.

**O que o Schröder diz — e ele se contradiz.**
São duas afirmações diferentes, em duas páginas diferentes, e elas não fecham entre si:

| onde | o que diz | maior uso de dados |
|---|---|---|
| Tab. 3, p. 2197 (medida) | coluna "Data Use" por dataset: AGN 0,4% · MR 0,547% · SUBJ 5,83% · TREC-6 9,55% · **CR 15,45%** | **15,45%** |
| §4 (prosa), p. 2198 | "using only between 0.4% **and 14%** of the data" | 14% |

A prosa dos autores arredonda para baixo o próprio número da tabela deles. A tabela é a
medida; a frase é o resumo — e o resumo está errado em relação à tabela.

**Consequência direta para a redação proposta.**
O 15% só "situa-se na faixa que a literatura reporta" se a âncora for a Tab. 3 (15 ≤ 15,45).
Se a âncora for a frase que a mensagem de proveniência 20260818-0210 cita textualmente
("between 0.4% and 14%"), a afirmação é aritmeticamente falsa: 15 > 14. E o Settles (2009),
citado no mesmo lugar como "less than 10% of the data was labeled", não cobre 15% de jeito
nenhum — ele não pode ser invocado como teto.

**Uma ação:** trocar a âncora da frase — citar Tab. 3, p. 2197 (CR, 15,45%), não a frase da
p. 2198; e retirar o Settles da posição de teto (ele serve como piso da faixa, não como topo).

**Duas coisas que isto NÃO muda, para o autor não gastar decisão à toa:**

1. **O veredito não depende disto.** Mesmo adotando 14% (32.409 rótulos), o piso de 25.000
   (10,8%) continua dentro e o E35 (35.000) continua fora. A virada de "refutada" para
   "sustentada" se sustenta com qualquer das duas âncoras. O que está em risco é só a frase
   que justifica o teto — e é ela que a banca prevê que a banca real vai atacar.

2. **A correção enfileirada da ficha C3 está na direção errada.** A fila prevê trocar
   "~15%" por "14%" em `fichamentos/Schroder2022Uncertainty.md`. Não trocar: a evidência
   declarada em C3 é "Tab. 3, p. 2197", e a Tab. 3 diz 15,45%. Aplicar a correção poria a
   ficha a citar uma tabela e a reportar um número que a tabela contradiz. C3 como está,
   com a ressalva já registrada no corpo da ficha (que documenta as duas leituras), está
   correta. Sugiro fechar esse item como "verificado, sem alteração".

Lembro o gatilho que já estava armado do meu lado e que continua valendo: se a reescrita do
critério de parada chegar ao Cap.3/A7/Cap.5, ela precisa declarar explicitamente o caráter
POST-HOC do corte — a própria banca levantou isso ("o teto foi reenunciado DEPOIS de o
resultado ser conhecido"). Trocar a âncora resolve a aritmética; não resolve a trave móvel.

Evidência: PDF pág. 4 do arquivo = p. 2197 impressa (Tab. 3, "15.45%"); pág. 5 = p. 2198
(frase "and 14% of the data"). Extração conferida com `pdftotext -layout`.
