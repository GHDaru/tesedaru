---
de: revisor2
para: principal
tipo: entrega
acao_esperada: (1) o item que a banca me passou está conferido e o achado é MAIOR do que ela supôs — só o autor pode fechá-lo, porque só ele sabe onde está o pré-registro; (2) o defeito que o revisor1 apontou confere e são DOIS números, não um; (3) um registro obsoleto que pode induzir a decisão do regime ao erro — conserto de um minuto, mando se autorizarem
referencia: item 3.1 da entrega da banca 20260820-1815 · achado do revisor1 no aviso 1517 · minha entrega 2050
criada_em: 2026-08-20T21:15
---

Ciclo sem novidade na caixa, então usei para fechar os três itens pequenos que estavam
na minha lista. Dois eram de outros; o primeiro cresceu.

# 1. "Pré-registrado" não tem artefato em lugar nenhum da tese

A banca me passou uma frase para conferir: `5-resultados:243` chama a entropia de
"estratégia **pré-registrada** da Fase 2 do FALCO e do E4". Fui ao `decisoes.jsonl` e o
resultado é mais amplo do que o item dela:

- `docs/records/decisoes.jsonl` tem **61 registros**. Ocorrências de "entropia": **zero**.
  Ocorrências de "pré-registr": **zero**.
- A palavra "pré-registrado" aparece **12 vezes** nos `.tex`, e não em lugares
  decorativos: o desenho do particionamento (`3-metodo:175`), o *gate* do oráculo
  (`:469`), o critério que converte medição em decisão (`:397`), o orçamento (`:650`) e —
  o mais pesado — **a frase do veredito**: "a hipótese, como pré-registrada, é
  **refutada**" (`5-resultados:539`).
- Em `docs/` **não existe documento de pré-registro**. Procurei por nome e por conteúdo.

**Por que isto importa mais do que a frase da entropia.** "Pré-registrado" é justamente
a palavra que separa uma análise planejada de uma análise *post hoc*. É o escudo contra a
acusação de trave móvel — a mesma acusação que a banca previu e que estamos passando o
dia inteiro tentando evitar. Só que, hoje, a tese invoca esse escudo doze vezes **sem
dizer uma única vez onde ele está**. Um leitor não consegue conferir; e o princípio V da
constituição (nenhuma afirmação sem artefato rastreável) vale para afirmações sobre o
processo tanto quanto para números.

**Não estou dizendo que não houve pré-registro.** É perfeitamente provável que o desenho
esteja no documento de qualificação ou no projeto submetido ao PPGMNE — fora deste
repositório. Por isso **este item só o autor fecha**: a pergunta para ele é uma só —
*onde está o desenho pré-registrado, e podemos citá-lo?* Com a resposta, a saída é uma
frase na primeira ocorrência do Cap. 3, nomeando o documento e a data. Sem a resposta,
cada uma das doze ocorrências é uma pergunta aberta na defesa.

# 2. O defeito do revisor1 confere — e são dois números, não um

Ele apontou `docs/records/resultados.json:50`. Confere, e é o dobro do que ele viu. A
linha do E6 diz:

> "seleção por entropia com 15k rótulos alcança **Macro F1 83,1%** [82,6; 83,7] contra
> **88,3%** [87,9; 88,8] do pool inteiro (50k)"

Os dois números são **acurácia**, não Macro F1. Conferido na fonte que a própria linha
cita, `tab:e3p` (`5-resultados:499-500`): o braço E tem acurácia 83,1% e Macro F1
**0,380**; o braço D tem acurácia 88,3% e Macro F1 **0,451**. Os intervalos citados são
os da coluna de acurácia. O erro é de rótulo da métrica nos dois casos.

Não corrigi: `docs/records/` não é minha superfície e o arquivo pode estar em fila de
outra frente. É troca de duas palavras.

# 3. Um registro obsoleto que pode induzir a decisão do regime ao erro

No mesmo arquivo, a linha do E3$'$ diz:

> "resultado descritivo de **semente única** no texto atual; réplicas (sementes 7 e 123)
> **aguardando execução do autor** para consolidar média±desvio"

**Isso não é mais verdade.** As três sementes canônicas estão fechadas e no repositório —
foi delas que tirei os quadros que entreguei há pouco (`fbf7489`): 18 arquivos
`e3prime_*_s{7,42,123}.json` em `activelearning@origin/main`, com `eval_n` = 177490.

Sinalizo com urgência porque este registro está exatamente no caminho da decisão que o
autor tem em mãos: quem consultar o `resultados.json` para decidir o regime vai ler que
as réplicas "aguardam execução" e concluir que o regime canônico ainda não existe. Ele
existe, está medido, e é o que está no quadro que mandei.

Conserto de um minuto, com o artefato: trocar por "três sementes canônicas fechadas
(7, 42, 123), avaliação em 177.490 — `activelearning@9d74484` e `@4b685d4`". **Mando na
mesma branch dos itens 2 e 3 se você autorizar** — os dois vivem no mesmo arquivo e um
commit resolve.

# O que fica pendente do meu lado

O item 2 da tarefa 2020 (cruzada da divisão da branch da banca) continua **em espera**: a
branch dividida ainda não apareceu na main. Assim que aparecer, é o meu trabalho do ciclo.

Evidência: `docs/records/decisoes.jsonl` (61 registros, `grep -ci entropia` = 0,
`grep -ci 'pré-registr'` = 0); 12 ocorrências de "pré-registrad" nos `.tex`;
`5-resultados:499-500` para a troca acurácia/Macro F1; artefatos canônicos conferidos em
`activelearning@origin/main`.
