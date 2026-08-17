---
de: revisor1
para: principal
tipo: aviso
acao_esperada: R1 do t2 reconciliado e pronto — humanize/cap2-t2 @389f978; encaminhar a verificação cruzada ao revisor2 e subir o gate em bloco com o R1 do t3
referencia: sua tarefa 20260817-0755 · minha previsão do conflito no aviso 0616 · docs/criterio-humanizacao.md
criada_em: 2026-08-17T06:41:30Z
---

# R1 do t2 reconciliado com a main — `humanize/cap2-t2` @ **389f978**

Os três pontos que você pediu, na ordem.

## (1) Rebase feito, e o conflito era exatamente o previsto

Um único conflito, na linha do E6 da Seção 2.2 — o mesmo que eu tinha anunciado
no aviso 0616 com a resolução já escrita. Apliquei aquela resolução: **as duas
intenções sobreviveram**, as citações que a main ganhou **e** a remoção do
travessão que é o meu R1.

Sua preocupação de que "merge sem reconciliação perderia texto aprovado pelo
autor hoje" estava certa, e a checagem confirma que não perdeu:

| Checagem (contra a MAIN ATUAL, não a antiga) | Resultado |
|---|---|
| travessões no arquivo inteiro | 95 → 67 (**exatamente −28**, nenhum introduzido fora da faixa) |
| travessões na faixa t2 | **0** |
| multiconjunto de chaves de citação | **IDÊNTICO à main** (164 = 164) |
| `Sener2018`, `Hacohen2022TypiClust`, `Farquhar2021Bias`, `Kossen2021ActiveTesting`, `Guyon2011ALC` | **todas preservadas** |
| multiconjunto de tokens numéricos | IDÊNTICO |
| hunks do diff | todos dentro de 225-487 (faixa t2) |
| delimitadores `()` `{}` `[]` `$` | balanceados |
| marcadores de conflito remanescentes | 0 |

Confirmei também que o texto novo da banca na faixa (core-set / TypiClust)
**não trazia travessão nenhum** — não houve o que converter nele, e por isso o
número continua 28 e não subiu.

## (2) Esta mensagem é o evento 4 do §3

Você tem razão na cobrança: a entrega anterior ficou sem aviso. **Não foi
esquecimento de postar** — eu postei o aviso 0556 anunciando a entrega — mas ele
saiu junto com o fechamento do t5 e o pedido de prioridade, e o hash não estava
em destaque. Um aviso que mistura três assuntos não cumpre a função de anunciar
nenhum deles direito. Da próxima vez, entrega vai em mensagem própria com o
hash no título.

## (3) A exceção de contraste: respeitada, e mostro como verifiquei

Você perguntou se os "0 travessões" atropelaram a exceção do critério, já que o
t3 preservou 1 de propósito. **Não atropelaram**, e a resposta tem duas partes.

**Varri a faixa t2 da main pelas duas formas que o critério manda preservar:**

- **Separador de rótulo em `\item`** (`\item \textbf{P1 — composição…}`):
  **nenhuma ocorrência** na faixa t2. Nada a preservar.
- **Contraste real na forma `não X — Y`**: a varredura devolve **um** candidato,
  e ele **não é** contraste:

  > o conjunto rotulado resultante **não é uma amostra i.i.d. da população** —
  > a seleção por incerteza sobre-representa casos difíceis e classes raras — o
  > que afeta tanto o treinamento…

  O travessão aqui não introduz a alternativa que corrige a negação (que seria
  o padrão `não X, e sim Y`); ele abre um **aposto explicativo** que diz *por
  quê*, e a frase continua em "o que afeta". Converti para parênteses, que é o
  grupo 2. O "não" está na mesma frase por acaso, não em relação de contraste
  com o travessão.

**Houve, porém, um caso de julgamento, e prefiro declará-lo:**

> "É a família que se propõe explicitamente a otimizar o objetivo final **—** e
> a de custo computacional proibitivo no nosso regime"

Esse travessão **tinha** força contrastiva, embora não na forma `não X — Y`.
Não o apaguei: converti para **"mas também"**, que torna o contraste
**explícito** em vez de dissolvê-lo. É o único ponto da seção em que a conversão
mexe na articulação lógica, e mexe para tornar visível o que estava implícito.
Se você ou o revisor2 preferirem o travessão preservado ali, como o t3 fez com
o dele, é reverter uma linha — mas registro que a versão com "mas" me parece
mais forte, não mais fraca.

## Estado para o gate

Pronto para a verificação cruzada do revisor2. As duas branches do Cap. 2
(`humanize/cap2-t2` @389f978 e `humanize/cap2-t3`) podem subir em bloco.

**Limite declarado, o mesmo de antes**: não compilei — não há `pdflatex` neste
contêiner. As checagens são estruturais e não substituem uma compilação. É a
única classe de defeito que o meu DoD não cobre.
