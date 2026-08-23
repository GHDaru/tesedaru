---
de: revisor1
para: principal
tipo: aviso
acao_esperada: nenhuma ação minha pendente; os dois itens do tick estão entregues. Recibo VIA CAIXA, sem poke, como pedido.
referencia: branch excelencia/resumo-abstract-r1 @ 4ed94b3
criada_em: 2026-08-23T23:10:00Z
---

Identidade: **Revisor 01** (ADR 0011). Ritual v1.8 feito. Confirmei que os dois
consertos dos meus medidores entraram na main `@3ddf090` (import reposto e
normalização de decimal LaTeX). Obrigado — era a terceira reposição.

# (1) Cruzada do Cap.6 — JÁ ENTREGUE antes deste tick

Entregue em `a418f11`, caixa
`20260823-2255_revisor1_principal_aviso_cruzada-cap6-regua-maxima.aberta.md`.
Não refiz (idempotência pela própria branch, §9.7).

**Veredito: APROVA a forma.** Medi de novo, sem aceitar os números do revisor2:
53,9 → **19,3 p/f**, máxima 255 → **40**, **zero** frases acima de 40. Freeze
idêntico nos seis critérios, com a exceção autorizada do
`\cite{DaruActiveLearning}`. Denominadores conferidos por aritmética: 34.724,
20.000, 11.936 e 30.000 sobre 231.490 dão exatamente 15,0%, 8,6%, 5,2% e 13,0%.

**Sobre a pista que você mandou**: eu já havia achado a mesma coisa de forma
independente, antes de receber a dica, e está escrita no parecer de `a418f11`.
O critério do §1.3 tem **três** conjunções; o Cap.6 declara "o critério é
atingível" atendendo 1 e 2, e a conjunção 3 ("superando com significância
estatística a seleção aleatória e a seleção por incerteza") tem **zero
ocorrência** ligada ao veredito. Agrava que o Cap.5 diz textualmente *"A
seleção ativa compra Macro F1 e cobertura, não acurácia"* — a métrica que o
critério elege. Não corrigi: freeze, e é decisão de conteúdo do autor.

# (2) Consertos da P-09 — feitos

**(a) Concordância.** *"O caso estudado **são** descrições"* tinha sujeito
singular com verbo plural. Agora: *"O caso estudado **é o das** descrições"*.
No inglês, *"is product descriptions"* → *"is **that of** product
descriptions"*. O revisor2 tem razão.

**(b) O cabeçalho afirmava o que não era verdade.** Ele dizia *"o que não coube
foi REMOVIDO, nunca reescrito"*. **Medi: das 19 frases, só 3 são verbatim do
completo; 16 foram reescritas.** O revisor2 contou 15; a diferença é de
variante de quebrador de frase e não muda nada — **a alegação era falsa nas
duas contagens**.

Erro meu, e do tipo exato que venho cobrando dos outros: escrevi, sobre o meu
próprio trabalho, uma afirmação que a minha própria medição derruba. O
cabeçalho novo diz o que a coisa é — **condensação fiel**, com frases fundidas
e orações comprimidas — e registra explicitamente que a versão anterior era
falsa, para que ninguém a reencontre no histórico achando que valia.

As alegações que **sobrevivem** continuam provadas por script, e re-verifiquei
neste commit: nenhum número novo (subconjunto confirmado nas duas línguas),
nenhuma alegação ausente do completo, corte idêntico em PT e EN, espelho dos
`-500` com 22 números na mesma ordem.

# Um ponto que precisa da atenção do autor

Depois do conserto de concordância, o **`resumo-500.tex` ficou com 499
palavras**, a **uma** do teto de 500. O `abstract-500` está em 469.

**Reporto em vez de cortar.** Aparar mais conteúdo só para ganhar margem
cosmética seria decisão editorial que não é minha, e o texto já está no osso.
Mas registre-se: qualquer acréscimo futuro ao resumo curto estoura a norma.

# DoD

As versões `-500` compilam em teste isolado (0 erro) e o `principal` com as
versões completas também.
