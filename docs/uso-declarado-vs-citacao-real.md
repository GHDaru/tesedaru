# O que as obras fichadas sustentam além de onde estão citadas

**Escopo**: os 164 fichamentos contra os seis capítulos de texto.
**Skill**: `verifiable-dod` — a varredura que eu vinha propondo como leitura
manual virou checagem executável (`scripts/check-uso-declarado.py`), porque
juízo não escala para 164 fichas e não sobrevive à minha própria desatenção.
**Executado por**: revisor1 · **Data**: 2026-08-17
**Natureza**: levantamento. Nenhuma linha da tese foi editada.

---

## A ideia, em uma frase

Todo fichamento tem, na tabela de claims, uma coluna **"Uso na tese"** que diz
onde aquele claim deve entrar — "Cap. 5", "Cap. 3", "Cap. 6". Essa coluna é
uma **promessa escrita no momento da leitura**, que é exatamente quando se sabe
o que a obra sustenta. Depois, ninguém volta para conferir se foi cumprida.

O script confronta essa promessa com a citação real. É o inverso da R3: a R3
pergunta "esta citação tem lastro?"; esta varredura pergunta **"este lastro foi
usado?"**.

---

## O achado estrutural, que vale mais que a lista

Contando **chaves distintas citadas por capítulo**, contra o número de fichas
que prometem cada capítulo:

| Capítulo | Fichas que prometem | Chaves de fato citadas |
|---|---|---|
| 1 · Introdução | 15 | 8 |
| 2 · Fundamentação | 95 | **132** |
| 3 · Método | 20 | 19 |
| **4 · Resultados P1/P2** | **6** | **0** |
| **5 · Resultados P3/P4** | **23** | **9** |
| 6 · Conclusão | 14 | 20 |

**O Capítulo 4 não cita nenhuma obra.** Nenhuma. Um capítulo de resultados sem
uma única referência externa discute os próprios números contra o nada. O
Capítulo 5 cita nove, tendo vinte e três fichas que o prometem.

Enquanto isso a fundamentação concentra 132 chaves — mais do que as 95 fichas
que a prometem, o que é saudável e esperado num capítulo de revisão.

O padrão é claro e tem nome: **a literatura entra na tese para justificar a
pergunta e sai antes de discutir a resposta.** É a pergunta mais previsível de
uma banca — *"como o seu resultado se compara com o que já existe?"* — e hoje
os capítulos de resultado não têm com que respondê-la, apesar de o repositório
já ter as fichas prontas.

Isto não é uma opinião sobre estilo. É contagem, e qualquer pessoa reproduz
com `python3 scripts/check-uso-declarado.py .`

---

## As 52 promessas não cumpridas

O script separa duas classes que, misturadas, afogariam o sinal:

- **`promessa-nao-cumprida` (52)** — a obra **é** usada na tese, e a ficha
  promete **outro** capítulo além daquele. É o achado.
- **`orfa-ja-conhecida` (71)** — a chave não é citada em capítulo nenhum. É o
  conjunto das ~95 órfãs que já está na mesa do autor. Não é achado novo e sai
  separado justamente para não inflar o número.

### As dez mais consequentes

| Obra | Promete | Hoje citada em | Por que importa |
|---|---|---|---|
| **`Wertz2022`** | Cap. 3, **5**, 6 | só Cap. 2 (1 vez) | **o caso mais grave** — ver abaixo |
| `Xiao2023FreeAL` | Cap. 5 (5 claims) | só Cap. 2 | destilação ativa; comparador direto do laço FALCO |
| `Farquhar2021Bias` | Cap. 2, 3, **6** | só Cap. 5 | viés de amostragem ativa: é a teoria do fenômeno que o E6 mede |
| `Kossen2021ActiveTesting` | Cap. 2, **6** | só Cap. 5 | idem, pelo lado da avaliação enviesada |
| `Pangakis2023Validation` | Cap. 1, 3, 5 | só Cap. 2 | validar o oráculo por tarefa — decisão de método |
| `Zhang2023LLMaAA` | Cap. 5 (3 claims) | só Cap. 2 | LLM como anotador ativo; comparador do resultado |
| `Zhang2025` | Cap. 3, 5 | Cap. 1 e 2 | custo do oráculo LLM |
| `Romberg2025Reassessing` | Cap. 6 (3 claims) | só Cap. 2 | viabilidade operacional como obstáculo real |
| `Griesshaber2020` | Cap. 3, 4, 5, 6 | só Cap. 2 | ficha nova (hoje); ver o viés de classe |
| `Machado2026RetailPt` | Cap. 3, 6 | só Cap. 2 | único trabalho de produto em português |

### O caso `Wertz2022`, que eu destacaria acima de todos

É **a única obra da tese que mede no regime de centenas de classes** — 100 a
739, contra as 621 do FALCO — e **a única que reporta que nenhuma estratégia de
seleção supera a aleatória de forma consistente** nesse regime.

Ela é citada **uma vez**, no Capítulo 2, como ressalva. A ficha dela promete:

- *"Cap. 5: comparador externo para a diferença E-D medida na tese"*
- *"Cap. 5: cobertura de classes como diagnóstico de estratégia de seleção em
  muitas classes"*
- *"Cap. 3/Cap. 5: condição sob a qual o ganho de seleção é esperado;
  caracterizar o nosso conjunto por essa métrica"*
- *"Cap. 3 (escolha da métrica): fundamenta reportar macro F1 como principal"*

Ou seja: o trabalho que estabelece **a expectativa contra a qual o resultado do
FALCO deve ser lido** não aparece no capítulo onde o resultado do FALCO é lido.

Vale nos dois sentidos, e é isso que o torna urgente em vez de opcional:

- se o FALCO **vencer** a aleatória em 621 classes, isso contraria o
  `Wertz2022` e é **contribuição forte** — mas só se a tese disser contra quem
  está contrariando;
- se **não vencer**, o `Wertz2022` transforma um resultado negativo em
  **replicação de um achado publicado**, que é resultado científico, e não
  fracasso.

Sem a citação, os dois cenários viram números soltos. Junto com a série de seis
trabalhos que fechei hoje (cinco medem abaixo de cinco classes e o aprendizado
ativo vence; só o `Wertz2022` mede nas centenas e ele não vence), esta é a peça
que faltava para o Capítulo 5 ter um interlocutor.

---

## Limites da varredura, declarados em vez de escondidos

Seguindo o antídoto do nº 13 do catálogo de anti-padrões — script que esconde o
que não cobre é pior que script nenhum:

1. **Não lê o conteúdo do claim.** Sabe dizer que a chave não aparece no
   capítulo prometido; **não** sabe dizer se uma citação existente sustenta
   aquele claim específico. É detector de ausência, não de adequação.
2. **Menções sem número são ignoradas.** "Fundamentação", "Método", "Estrutura"
   não viram capítulo, porque mapeá-las seria adivinhação. O efeito é
   conservador: a varredura **subconta**, nunca superconta.
3. **`Cap. 3/Cap. 5` numa mesma célula** é atribuído ao claim inteiro, sem
   separar qual metade vai para onde.
4. **Promessa não é ordem.** Uma promessa não cumprida pode ser decisão
   editorial legítima — a obra deixou de caber. O script não distingue "esqueci"
   de "decidi não usar", e não deve: quem decide é o autor.

Controles que rodei antes de reportar, porque **já publiquei um checador com
nove falsos positivos em dez esta noite** e não repito:

- `Wertz2022` — confirmado à mão: a ficha promete o Cap. 5 em quatro claims, e
  `grep Wertz2022 5-resultados-falco/texto.tex` devolve **0**.
- `Settles2012` — **controle negativo**: promete Cap. 2, é citada em 2, 3 e 6.
  Não aparece como promessa não cumprida. Correto.
- `Souza2020BERTimbau` — sem promessa de capítulo na ficha, citada em 1, 2 e 3.
  Não é acusada. Correto.

---

## O que eu proponho, e o que não é meu para decidir

**Não é meu para decidir**: quais das 52 viram citação. Isso é conteúdo, é do
autor, e várias podem ser recusadas com razão.

**Proponho**, em ordem de retorno pelo esforço:

1. **`Wertz2022` no Capítulo 5.** Uma obra, um parágrafo de discussão. É o
   maior ganho isolado da lista e não depende de mais nenhuma decisão.
2. **Olhar o Capítulo 4 de propósito.** Zero citações num capítulo de
   resultados é o tipo de coisa que ninguém decide — acontece. Seis fichas o
   prometem.
3. **`Farquhar2021Bias` + `Kossen2021ActiveTesting` no Capítulo 6.** As duas
   dão o vocabulário publicado para declarar a ameaça à validade que o E6 já
   mede. Declarar ameaça com apoio na literatura é mais forte que declará-la
   sozinho.
4. **Rodar a varredura antes do R6 de cada capítulo**, e não uma vez só. Custa
   um comando.
