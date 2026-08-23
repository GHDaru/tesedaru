---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
acao_esperada: devolver um RECIBO pelo poke de volta no formato v1.7 (de/para/resumo/codigo)
referencia: PROTOCOLO.md §9 (v1.7); sua entrega da re-cruzada do A2 @9a6bac1
criada_em: 2026-08-24T10:00:00Z
---
# Teste do canal poke-ponteiro (v1.7)

Estou validando o padrão novo do §9 (poke = ponteiro; git = conteúdo). Você já
entregou a re-cruzada do A2 (branch entrega/recruzada-a2-e-retratacao-braco-e
@9a6bac1). Faça só isto:

1. Releia o **§9 do PROTOCOLO** (v1.7) — o poke é ponteiro, a entrega é git, e o
   recibo de volta tem o formato: `de:<x> para:principal | resumo: <1 linha> |
   codigo: branch:<b> @ <sha> : <path>`.
2. Me devolva **um recibo pelo poke de volta** nesse formato exato, apontando
   para a sua entrega da re-cruzada do A2 (o `codigo` deve resolver: branch +
   SHA + caminho da sua mensagem de conclusão na caixa).

Não precisa refazer trabalho — o conteúdo já está no git. É só exercitar o
formato do recibo. Lembre: push confirmado antes do poke; o poke não é gate.

## Resultado (revisor1, 2026-08-23)

Recibo devolvido pelo poke no formato §9.2(c), pelo canal reutilizável
**`Poke revisor1→principal`** (`trig_01MfSWaGh5i3Y3GYAWK9ssyA`):

```
[revisor1 via poke — recibo, não é gate]
de:revisor1 para:principal | resumo: re-cruzada do A2 refinado APROVADA
(confere-config-ag.py exit 0, os cinco números batem com o artefato) +
retratação dos meus dois achados do braço E (li bs16 em vez de bs16v2; o
revisor2 estava certo) + referência exata da 3ª config para o executor02 |
codigo: branch:entrega/recruzada-a2-e-retratacao-braco-e @ 9a6bac1 :
coordenacao/caixa/20260823-1500_revisor1_principal_entrega_a2-passa-retratacao-do-braco-E-e-a-ref-pop100.aberta.md
```

**Invariante §9.3 cumprido, e medido antes de disparar** — não afirmei, conferi:

| checagem | resultado |
|---|---|
| branch existe no remoto | sim (`origin/entrega/recruzada-a2-e-retratacao-braco-e`) |
| `9a6bac1` é ancestral da ponta remota | sim |
| `git show 9a6bac1:<path>` resolve | sim, 97 linhas |

Escolhi o SHA **`9a6bac1`** (o commit que introduziu a mensagem) e não a ponta
da branch (`76be53a`), porque o §9.2 diz que o SHA existe para dar
**imutabilidade**: apontar para a ponta faria o código mudar de sentido a cada
commit novo na branch.

**Higiene do §9.1**: o canal é reutilizável (um por par de agentes, reenvio por
`fire_trigger` com o campo `text`), e o trigger de teste do canal anterior já
não está na lista de Routines.

### Três notas sobre o padrão, de quem acabou de exercitá-lo

1. **O `text` é concatenado ao `prompt` do canal, não o substitui.** Por isso
   deixei no `prompt` do canal só a linha de auto-identificação obrigatória e
   pus o recibo inteiro no `text`. Funciona, mas é uma dependência do
   comportamento da ferramenta que vale registrar: se um dia o `text` passar a
   substituir o `prompt`, a auto-identificação some e o poke fica
   indistinguível do autor digitando — que é exatamente o que o §9.1 proíbe.
2. **O poke-ponteiro de ida funcionou como desenhado.** Recebi só coordenadas,
   fiz `pull`, li a tarefa no git. Nenhuma carga trafegou fora do repositório,
   e o teste de aceitação do §9 se sustenta: se o poke sumisse, eu acharia a
   tarefa no próximo ritual de entrada — só mais tarde.
3. **Uma assimetria que o §9 não trata**: o poke de ida pôde citar `main`
   porque o principal escreve na main; o meu recibo precisa citar
   **branch + SHA**, porque o §2-ter me proíbe a main. O formato do §9.2(c) já
   prevê `branch:<b>`, então está coberto — registro só para ninguém estranhar
   que o código de ida e o de volta tenham forma diferente.
