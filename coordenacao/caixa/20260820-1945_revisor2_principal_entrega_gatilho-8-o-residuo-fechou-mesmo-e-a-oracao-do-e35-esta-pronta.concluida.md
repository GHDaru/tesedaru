---
de: revisor2
para: principal
tipo: entrega
acao_esperada: (1) registrar que o resíduo fechou — conferido por MIM, não pela própria banca (§6, quem executa não verifica); (2) levar ao gate do autor, JUNTO com a branch, a oração do E35 já escrita abaixo, para ele aprovar TEXTO e não intenção
referencia: aviso da banca 20260820-1905 (f2e7b73) · branch @ d0d35ed · minha reverificação 20260820-1840
criada_em: 2026-08-20T19:45
---

# 1. O resíduo fechou — conferido por terceiro

A banca conferiu com o próprio `grep`, o que é natural, mas o protocolo pede
conferência de quem não executou. Fiz a minha, na branch `@ d0d35ed`:

- A frase que enunciava a regra ("os orçamentos passam a ser medidos como fração do
  *pool* de 50 mil, $30\% = 15$ mil rótulos") **saiu**, e o que entrou é registro de
  percurso, sem regra. Confere.
- A redação nova faz mais do que eu tinha pedido, e faz bem: **explica** por que a
  coluna da tabela do Cap. 5 segue no denominador do *pool* enquanto a prosa fala em
  percentual da base. Era o ponto que restava para o leitor não tropeçar.
- **Ela também consertou a segunda ocorrência**, que eu não tinha apontado: a
  "Segunda:" das ameaças à validade (l. 656) foi reescrita no mesmo espírito.
- Varredura minha, na branch inteira: sobraram duas ocorrências de "15 mil" em
  `3-metodo`, ambas **legítimas** — a l. 608 descreve o braço (E), que é de fato o
  prefixo de 15 mil da trajetória do E6, e a l. 656 descreve o orçamento *executado*.
  Nenhuma das duas enuncia regra.

**Veredito: o resíduo está fechado.** Do meu lado não há mais objeção à branch.

# 2. A oração do E35, escrita, para o gate decidir sobre texto

A banca leu meu achado melhor do que eu: eu tinha visto um risco de pergunta da banca
real, e ela viu que o fato é **blindagem** — o teto não foi esticado para acomodar o
melhor resultado. Ela tem razão, e por isso vale virar texto.

Aritmética reconferida: 35.000 / 231.490 = **15,1195%** da base; 35.000 − 34.724 =
**276 rótulos** acima do teto. 25.000 = 10,800% da base.

**Onde entra:** `5-resultados-falco/texto.tex`, na leitura (iii), logo depois de
"...reproduzindo no BERTimbau o efeito medido no E6 com os classificadores leves."

**O que entra** (proposta fechada, para aprovar ou recusar como texto):

> Note-se que o próprio E35 fica \emph{fora} do teto do critério: seus 35 mil rótulos
> são $15{,}12\%$ da base, 276 rótulos acima dos 34.724 admitidos. O braço que supera a
> supervisão completa não é, portanto, o braço que sustenta a hipótese --- quem a
> sustenta é o E25, com $10{,}8\%$ da base, folgado dentro do teto. O teto não foi
> esticado para acomodar o melhor resultado.

**Não apliquei.** `5-resultados-falco/texto.tex` está na branch da banca, que aguarda o
gate; escrever agora criaria conflito ou exigiria entrar na branch dela. Se o autor
aprovar, aplico em um commit só — na branch dela antes do merge, se ele preferir tudo
junto, ou numa branch minha depois, se preferir separado. Levo a decisão dele.

# 3. Continua aberto e sem dono

A frase de lastro do **Cap. 1** (o meu achado 2 de 20260820-1755): ela invoca Settles e a
Tab. 3 do Schröder como "frações dessa ordem", mas essas frações são sobre o conjunto
selecionável, cujo análogo aqui é o *pool* — nessa régua o critério é 69,4%, não 15%.
`1-intro` não estava no lock das 5 superfícies, então ninguém pegou. Com o Cap. 3 e o
Cap. 5 já consertados, é o último ponto da frente do critério que segue como estava.
