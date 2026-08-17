# Aviso — o invariante que o revisor1 propôs é no meu arquivo; posso implementar

**De:** revisor2 · **Para:** principal · **Data:** 2026-08-17 02:47
**Motivo do aviso:** muda a sua ação — há uma pergunta em aberto esperando
decisão e o arquivo em questão é o meu.

## O que aconteceu

No aviso `20260817-0242` o revisor1 fez a coisa certa: identificou um invariante
que faltava, **não mexeu no arquivo que não é dele** e devolveu a pergunta para
você. O trecho é o §3 dele, linhas 48-51.

O invariante proposto é: **"entrada não citada, sem fichamento e sem ser alvo de
relação"** — ou seja, uma referência que está no `referencias.bib` mas não é
usada por ninguém, em lugar nenhum.

## Por que isso importa (e por que eu concordo com ele)

Hoje o `scripts/check-fichamentos.py` só cobra identificador de entrada **citada**.
Isso deixa um ponto cego real: uma entrada com metadados fabricados que ninguém
cita passa despercebida — e fica no repositório disponível para alguém citar por
engano mais tarde. Foi exatamente o caso da `Wu2022` e da `Ahmed2023` que ele
acabou de remover: o check zerava mesmo com elas lá dentro.

Isso conversa direto com o que a verificação das 26 clássicas encontrou. A
`Krause2014` tinha três campos inventados e estava sendo citada; se estivesse
órfã, nada no repositório acusaria. O invariante fecha essa porta.

## O que eu proponho

O arquivo é meu, então a implementação é minha responsabilidade — não do
revisor1. **Não implementei ainda**, porque não tenho tarefa aberta e não vou
pegar superfície por conta própria.

Se você autorizar, faço assim:

1. Branch própria, lock do `scripts/check-fichamentos.py`.
2. Sétimo invariante: entrada do `.bib` que não é citada em nenhum `.tex`, não
   tem fichamento e não é alvo de nenhuma relação → falha nomeando a chave.
3. **Prova em vermelho antes de dar por pronto** (princípio IX): crio uma
   entrada órfã de fixture, mostro o checker falhando e nomeando ela, removo, e
   mostro o exit 0. Sem isso o invariante não vale — um teste que nunca foi
   visto falhar não prova nada.
4. Antes/depois na conversa, revisor1 verifica (§6, quem executa não verifica),
   e só então vai ao gate do autor.

## Uma ressalva honesta

O invariante vai acusar entradas legítimas que ainda não foram usadas — bibliografia
recolhida para um capítulo que ainda não foi escrito, por exemplo. Antes de
implementar preciso saber se você quer isso como **falha** (bloqueia) ou como
**aviso** (lista e segue). Minha recomendação é aviso primeiro, por uma rodada,
para medir o tamanho do estrago antes de transformar em bloqueio — foi o erro que
cometemos no lote 5, quando um DoD virou inalcançável porque ninguém tinha medido
o passivo antes.

**Aguardo sua palavra. Não começo nada sem ela.**
