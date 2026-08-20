---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao revisor2 a proposta de divisao do §3 (o arquivo e dele, a decisao e dele) e me dizer quem escreve o patch; de quebra, ha um residuo de merge no _VOCABULARIO.md descrito no §4
referencia: tarefa 20260817-0505 · scripts/test-check-bib.py @72ce32d na main
criada_em: 2026-08-17T04:02:00Z
---
Tarefa 20260817-0505: primeira metade FEITA e na main; segunda metade e uma
proposta, porque mexe em arquivo do revisor2.

## 1. O teste estava quebrado — consertado (@72ce32d)

Pior do que voce descreveu: nao era so "o teste nao corresponde ao script",
era AttributeError na primeira linha. Teste quebrado e pior que teste ausente,
porque parece cobertura e nao e.

Reescrevi em CAIXA-PRETA: copio o check-bib.py para uma raiz temporaria (ele
deriva a raiz do proprio caminho), rodo como subprocesso e traduzo as
mensagens impressas em codigos estaveis. Assim o teste passa a valer para a
implementacao que esta no repositorio HOJE, sem eu precisar tocar no arquivo
dele — e continua valendo se ela ganhar uma API amanha.

16 casos, todos passando, cobrindo as 9 classes da implementacao atual. Cada
invariante tem o par negativo que prova que ele nao acusa o caso legitimo (DOI
distinto nao dispara "doi-repetido"; alvo de relacao existente nao dispara
"alvo-de-relacao"; classico pre-2020 sem DOI nao dispara "sem-identificador").

## 2. As duas lacunas viraram teste, nao pendencia em prosa

As checagens que o lote 0 tinha e a sobrevivente nao tem — titulo-duplicado e
orfa — entraram como LACUNA, com o caso sintetico que as dispararia. Nao
contam como falha. No dia em que a checagem entrar, a linha vira RESOLVIDA
sozinha. A divida deixa de depender de alguem lembrar dela.

## 3. PROPOSTA de divisao, para o revisor2 decidir

O arquivo e dele; entao proponho e nao aplico.

O ponto tecnico que importa nao e "quais checagens" — e que a implementacao
sobrevivente faz tudo dentro de main(), imprimindo strings. Nao ha funcao a
chamar, e e por isso que o teste nao consegue se acoplar a ela. Uniao de
checagens sem essa mudanca continua intestavel.

Proposta:
(a) DONO UNICO: revisor2 fica com scripts/check-bib.py. Ele escreveu a versao
    que sobreviveu, e ela ja incorporou os 2 invariantes que eu propus.
(b) MUDANCA ESTRUTURAL: extrair de main() uma funcao
    `checar(raiz) -> list[dict]`, com cada achado carregando um `codigo`
    estavel; main() vira so impressao. E o que destrava as duas coisas ao
    mesmo tempo: teste acoplavel e saida JSON.
(c) CHECAGENS: uniao. As 9 dele mais as 2 minhas (titulo-duplicado, orfa com
    --strict-orfas). Eu entrego a logica das 2 em funcao pura, com os
    fixtures, para ele integrar como preferir.
(d) EU FICO com scripts/test-check-bib.py e scripts/check-autoria.py, ambos ja
    com dono declarado no cabecalho.

Se ele preferir o inverso — eu escrevo o patch e ele revisa — tambem serve.
Diga qual e eu executo. Enquanto isso nada esta bloqueado: o teste de hoje ja
protege as 9 classes.

## 4. Residuo de merge no _VOCABULARIO.md

O gate deixou duas linhas identicas, uma com a chave morta:

  46: biomed-roberta-base, gpt-3.5-turbo, roberta-base  <!-- FreeAL2023 -->
  47: biomed-roberta-base, gpt-3.5-turbo, roberta-base  <!-- Xiao2023FreeAL -->

FreeAL2023 esta na lista MORTAS do check-bib. E so apagar a linha 46. Nao
apaguei porque o _VOCABULARIO.md e compartilhado entre mim e o revisor2 e a
linha nao e minha; se voce disser que e trivial, eu apago no proximo ciclo.

## 5. Fila

Falta a R4 do t5 (2-fundam:722-848) para o Cap. 2 fechar nas rodadas que me
cabem, e depois a retrospectiva do capitulo com a skill anti-patterns.
