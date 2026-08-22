---
de: revisor1
para: principal
tipo: entrega
acao_esperada: consolidar no gate do autor. Entrego a R4 do Cap.3 (tarefa 1000). Três itens PRECISAM de decisão do autor porque mudam o sentido de um critério metodológico e atravessam o Cap.5 — não são conserto de redação e por isso eu NÃO os corrigi. Há também um achado fora da minha superfície, no Cap.2, que está com as 7 rodadas fechadas e tem uma referência indefinida real.
referencia: branch r4/cap3-afirmacoes @908a840 · docs/r4-cap3-afirmacoes.md · plano v76 (cap3.R4 = gate) · cruzada da entrega 20260822-0921 do revisor2
criada_em: 2026-08-22T13:45:00Z
---

R4 fechada. **Nenhuma afirmação órfã** no capítulo — ele descreve e não conclui.
O que havia era lastro apontando para o lugar errado (7 casos, corrigidos) e
justificativa que a própria evidência citada contradiz (3 casos, declarados).

# Corrigido (7) — lastro existia, estava implícito ou errado

Destaque, porque o erro era meu: a nota `†` que escrevi na Fase 2 mandava o
leitor a `experiments/e6population` atrás dos artefatos do E5. Eles estão em
**`experiments/e5cycle`** — diretório que existe e que o Apêndice A7 já citava
certo. Os outros seis: nota de reprodutibilidade da base; E2 sem desfecho
(agora diz "três épocas" e remete); artefato da calibração de lote nomeado;
"ordens de grandeza" trocado por argumento verdadeiro por construção; "5×"
com denominador declarado (4,6×); verificador executável citado no texto.

# Para o autor decidir (3) — não corrigi de propósito

1. **Gate de 85% com o racional invertido.** O texto diz que 85% "fica um
   desvio ACIMA" do baseline de 89,56%. Está **4,56 p.p. ABAIXO**. E "um
   desvio" não diz desvio de quê — é número sem artefato. O resto da frase só
   fecha com "abaixo". **A banca já apontou isto duas vezes**
   (`parecer-ars-r6` §3.3 e `parecer-r3-r4-r6-leitura-final` item 2) e
   continua no texto. Redação proposta no relatório.
2. **A Fase 2 roda entropia; o E1, que deveria justificá-la, elege menor
   margem/menor confiança** (`5-resultados:281-290`). O Cap.3 afirma que a
   escolha é "justificada por LCE" pela varredura — a varredura diz o
   contrário. Ou o método explica por que manteve entropia apesar do E1, ou
   larga a reivindicação de lastro. É o de maior risco de arguição.
3. **Fator 22 na constante de parada**: Cap.3 justifica ε=10⁻³ pelo "ruído
   típico"; o A7 justifica pelo próprio limite 1/√n_V, que com n_V=2.000 dá
   **0,0224**. Não coloquei remissão cruzada aqui de propósito: certificaria
   um lastro que a aritmética nega.

# Cruzada do revisor2 (entrega 0921) — achado real, causa errada

Os oito números dele **conferem**, e a conferência vale. Mas a causa não: ele
atribuiu a diferença 719/657 à **remoção de acentos**. Esta base tem **zero
caracteres acentuados** em 250.365 linhas — remover acento não muda contagem
alguma. O que muda é o **colapso de espaços internos**. E 231.490 só reproduz
com o filtro `≥2` aplicado ANTES do dedup (ordem que elimina a classe *pomada
massageadora* e explica 715→714).

Isto tem consequência prática: eu ia escrever no capítulo a nota que ele
propôs, e ela afirmaria algo que um `grep` derruba. A nota que entrou é a que
eu medi. Sugiro devolver isto ao revisor2 — não como reprovação, o trabalho
dele encurtou o meu, mas para ele não repetir a atribuição.

# Fora da minha superfície — para você despachar

`2-fundam/texto.tex:505` parte a chave no meio da linha:
`\ref{sec:fund-` / `llm}`. O LaTeX lê `sec:fund- llm` e emite **referência
indefinida real**, num capítulo com as **7 rodadas fechadas** — ou seja, passou
pelo DoD. Conserto: juntar as duas linhas. Não editei (prosa é sua, e eu não
tinha lock em `2-fundam`). Varri a tese inteira: **é o único caso**. Como a
humanização reflui linhas e pode partir chaves sem ninguém ver, proponho um
guarda executável (a regexp está no relatório) — proposta, não coisa feita.

# DoD

`pdflatex`+`bibtex`+2 passes: **exit 0, 0 erros**. Referências indefinidas
introduzidas por mim: **0**. Caixas estouradas >20pt: **7 na main, 7 no branch,
lista idêntica**. Lock de `3-metodo` liberado neste mesmo commit.
