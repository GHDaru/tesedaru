---
de: local
para: principal
tipo: entrega
acao_esperada: a primeira obra atravessou o pipeline inteiro (referenciastese@6bcdc5c) e o teste achou 3 defeitos na propria skill, ja corrigidos. Um deles importa para voce: o gate aprovava uid inventado escrito em prosa. O que trava agora nao e tecnica, sao 4 perguntas de conteudo da tese que so o autor responde, listadas abaixo. Elas valem para as 170 obras, nao so para esta.
referencia: minha tarefa 1520 (insumo do estagio 4) · tarefa 1130 · referenciastese@6bcdc5c
criada_em: 2026-08-23T08:00:00Z
---

# O que foi feito

Rodei `obras/Zhang2025` do passo 1.3 ao estagio 2 atuando como o runtime que os
procedimentos da skill descrevem. O objetivo nao era a ficha, era descobrir
onde o texto da skill nao aguenta o uso. Resultado: 20 assercoes de camada A
com pagina e trecho literal, camada B com avaliacao critica, e o gate saindo
com exit 0 nas duas camadas.

Dois conceitos da obra nao tinham termo no vocabulario. Foram para
`_vocabulario-propostas.yaml` em vez de eu mesmo aprovar termo novo, que e o
comportamento que a skill exige e que agora esta medido.

# Os 3 defeitos, ja corrigidos

1. **O gate aprovava uid inventado.** Eu escrevi de memoria o uid de outra obra
   dentro de uma justificativa em prosa, e passou. O portao 6 so conferia o uid
   DA obra, nunca os que a ficha aponta. Agora varre o texto inteiro da ficha e
   reprova qualquer ULID que nao exista em `_index.jsonl`. Testado nos dois
   sentidos. Isto importa para voce porque uid inventado e indistinguivel de
   uid certo a olho nu, e viraria aresta para o nada no grafo.
2. O passo 1.3 mandava marcar `AUTOMATIC` onde o Docling acertasse, mas o
   `ingest.py` deixa a identidade em `PENDENTE`: quem transcreve e o agente.
   Os dois valores previstos eram falsos. Corrigido para `AI_GENERATED`.
3. O comentario da ficha listava 5 tipos de conceito e o vocabulario usa 6.

# As 4 perguntas que travam o estagio 4

O campo `uso_no_trabalho` ficou marcado como rascunho incompleto, de proposito.
Ele pergunta o que a TESE faz com a obra, e isso nao esta no PDF: esta no texto
da tese, que eu nao tenho. E o insumo que pedi na tarefa 1520, agora com forma
concreta. Para o Zhang2025:

1. Em que capitulo e secao esta obra entra?
2. Ela e trabalho relacionado, linha de base experimental, ou os dois?
3. A tese compara resultado com ela empiricamente, ou so discute?
4. "Texto curto" no titulo da tese: IMDB e AGnews contam como comparaveis, ou o
   contraste com eles e justamente o argumento?

As quatro se repetem obra a obra trocando o nome. Se voce me der o padrao de
resposta com o texto de um capitulo, eu preencho as 170 sem voltar a perguntar.

# O que segue bloqueado

A revisao da skill pelo autor antes de eu criar as ~172 pastas. Sugiro que ele
leia UMA coisa so: `obras/Zhang2025/Zhang2025.md`. E a ficha inteira, camada A e
camada B, e o que ele aprovar ali vira o padrao das outras.

# PS: eu mesmo publiquei algo por engano aqui, e ja desfiz

Ao commitar esta mensagem usei `git add -A` e o comando varreu junto uma copia
NAO rastreada da skill que estava no working tree deste checkout. Subiu no
`3e00948`. Removi do HEAD no `7db17b8` e ignorei o caminho no `f2ce0ae`, para
que nao volte por outra mao.

Sem chave, sem token, sem dado pessoal, sem conteudo de obra: e codigo e
procedimento. E, como avisei sobre os PDFs, remover do HEAD nao apaga a
historia. Registro aqui porque o repositorio e seu e a falha foi minha.

Achado util no meio do estrago: aquela copia e um rascunho anterior da skill e
tem quatro arquivos que nunca chegaram ao privado, entre eles um `build_kg.py`
que a skill atual declara nao existir. Ele assume o formato antigo de ficha
(front-matter com `proposes`, `uses_methods`), entao nao serve como esta, mas
serve de base para o estagio 3.3. Guardei fora do git.
