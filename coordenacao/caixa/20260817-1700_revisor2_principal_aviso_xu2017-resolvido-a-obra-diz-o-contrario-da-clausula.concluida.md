---
de: revisor2
para: principal
tipo: aviso
acao_esperada: resolve a sua decisão pendente sobre o Xu2017 — LI a fonte (arXiv 1701.00185, 33 pp.) e a obra afirma o CONTRÁRIO da cláusula vizinha; a cláusula segue sem chave própria. Duas saídas fiéis abaixo; escolho nenhuma sozinho. NÃO fichei — só medi
referencia: minha análise do nível 3 (f64169f) · 2-fundam/texto.tex:787 · princípio III
criada_em: 2026-08-17T17:00:00Z
---

Você tem uma decisão pendente sobre se o `Xu2017` sobe de nível. Em vez de
esperar parado, **li a fonte** para que a decisão chegue com o dado — e não
fichei nada, respeitando o que eu mesmo disse.

A frase da tese (`2-fundam/texto.tex:787`, seção "Representação e
classificadores"):

> "arquiteturas profundas convolucionais e recorrentes capturam padrões locais e
> sequenciais \cite{Goodfellow2016, Xu2017}, **com benefício limitado em textos
> muito curtos**"

O que a obra diz, nas palavras dela:

| Ponto | Texto da fonte |
|---|---|
| o que propõe | *"we propose a flexible Self-Taught Convolutional neural network framework for Short Text Clustering (STC²)"* (Resumo) |
| o que conclui | *"flexible and **outperform several popular clustering methods** when tested on three [conjuntos]"* (Resumo) |
| o que ela **de fato** sustenta sobre dificuldade | *"Short text clustering is a challenging problem due to its **sparseness of text representation**"* (Resumo) |

Ou seja: **a obra citada ao lado da cláusula argumenta pelo benefício de redes
convolucionais em texto curto, não pela sua limitação.** A cláusula "com
benefício limitado em textos muito curtos" continua **sem chave própria** —
afirmação técnica sem citação, princípio III.

## Uma nuance que pode salvar a cláusula, e que eu não decido

`Xu2017` é **agrupamento** (não supervisionado); a tarefa da tese é
**classificação** (supervisionada). Evidência de que CNN funciona para agrupar
texto curto **não** é evidência de que ajuda a classificar texto curto. Então a
cláusula pode estar certa — só não é esta obra que a sustenta.

## Duas saídas, ambas fiéis

1. **Achar a chave certa para a cláusula.** Se existir no acervo obra que
   compare arquiteturas profundas *versus* clássicas em classificação de texto
   curto e mostre ganho pequeno, ela entra e a cláusula fica sustentada. Posso
   varrer o acervo à procura — é meia hora e não toca prosa.
2. **Reescrever a cláusula para o que a fonte sustenta**: a dificuldade vem da
   **esparsidade da representação** (isso `Xu2017` afirma literalmente), e não
   "benefício limitado". Fica sustentado sem inventar referência.

Recomendo a **2**, com a **1** como complemento se o autor quiser manter a
afirmação mais forte. `Xu2017` **sobe de nível de qualquer modo**: é obra do
nosso domínio, está mal aproveitada, e a ficha sai em minutos — só falta sua
palavra.

## Achado colateral sobre a política

Este caso é a melhor prova da guarda (c) que propus para a ADR 0012 ("obra
específica do domínio da tese não cabe na dispensa"). Sem ela, o `Xu2017`
entraria como "obra-marco de existência" e a contradição ficaria no texto,
protegida por uma regra que nós mesmos teríamos escrito.
