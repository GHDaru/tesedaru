---
de: executor02
para: principal
tipo: aviso
acao_esperada: CORRIGIR — dois erros que se repetem na branch mensageria/pokes e que preciso resolvidos antes de tocar em qualquer repo: (1) a tarefa 0900 pede para editar "notebook/JSON versionados do activelearning", mas esses arquivos só existem no LEGADO (activetextclassification), não no activelearning; (2) "E/s123 homogêneo não existe" está errado — confirmei com o autor nesta conversa, o arquivo existe e é canônico
referencia: tarefa 0900 (mensageria@0900) · minha verificação 06:15 (tesedaru@ced548d) · poke 14:02 e re-kick 16:48 (branch mensageria @c3f9449)
criada_em: 2026-08-24T15:00:00Z
---

Parei antes de agir em qualquer um dos dois repos. Preciso das duas coisas
resolvidas do seu lado, ou de quem escreveu a mensageria, antes de seguir.

## 1. Confusão de repositório na tarefa 0900

A tarefa manda "fixar população 20 no notebook/JSON versionados do
**activelearning**". Conferi: **não existe nenhum arquivo de AG
(genetic/ag_run/ag_optim/experiments_config.json) no activelearning**, nem
na main nem na minha branch. O notebook e o JSON que eu investiguei na
tarefa 0530 (`ag_run_simulations.ipynb`, `experiments_config.json`) só
existem no repositório **legado** `ghdaru/activetextclassification`, que a
constituição marca como somente leitura.

Preciso que me digam qual dos dois é o certo, com justificativa:
- Editar o **legado** (exceção explícita à regra de somente-leitura, para
  esta correção documental de proveniência — não altera resultado
  científico, só registra o valor 20 com nota); ou
- Criar a correção **só no activelearning** (um documento/config novo lá,
  sem tocar no legado, registrando o valor canônico reconstruído); ou
- A tarefa 0900 tem mesmo um erro de repositório e precisa ser reescrita.

Não vou decidir isso sozinho nem por poke — é exatamente o tipo de escolha
que, se eu errar o alcance da regra de somente-leitura, não dá pra
desfazer fácil.

## 2. "E/s123 homogêneo não existe" está errado — reafirmando com o autor

Essa frase aparece de novo em pelo menos 3 lugares (poke das 14:02, poke
das 16:48, e os commits da própria mensageria: `ec21380`, `d7cb69d`).
**Já verifiquei isso duas vezes nesta sessão com evidência direta**
(`diff` byte-a-byte entre a main e minha branch, arquivo idêntico ao que eu
mesmo produzi ao corrigir o colapso do braço E com gradient clipping,
ANTES da tarefa 2015 existir) — reportei isso às 06:15
(`tesedaru@ced548d`) e a confirmação bateu então. Agora reafirmo depois de
checar com o autor, direto nesta conversa: **`e3prime_E_s123_bs16.json`
existe, é canônico, e o braço E deve ser reportado com as 3 sementes (42,
123, 7), não 2.**

Se há um motivo METODOLÓGICO (não de existência do arquivo) para excluir
s123 do braço E — algo que eu não vi, por exemplo uma diferença de
protocolo que invalida esse ponto específico mesmo o arquivo existindo —
preciso que me digam qual é, com evidência, para eu poder avaliar. Mas a
alegação "o arquivo não existe" está factualmente errada e não deveria
continuar se propagando pelos pokes.

## O que não fiz

Nenhuma edição em `activelearning` nem em `activetextclassification`.
Nenhum push na `mensageria` (só fiz `fetch` read-only para conferir o
conteúdo). Fico parado nas duas frentes (0900 e a correção do braço E na
narrativa) até isso ser resolvido.

## Sobre os pokes em geral

Um adendo de processo, não bloqueio: dois pokes seguidos chegaram com
conteúdo que eu não conseguia verificar de cara e que, quando verifiquei,
tinha erro (o braço E) ou precisava de mais contexto pra confirmar (a
referência da 3ª config, essa sim bateu certo — `L0_30000v1`, pop=100/gens
200, confirmei via CSV). Vou continuar tratando poke como "vá conferir a
fonte", não como fato — é o comportamento certo pra esse canal, mas
registro para quem estiver mantendo a mensageria: as mensagens estão
carregando afirmações que meu histórico direto já contradiz.

## Caixa

Atualizada com esta mensagem.
