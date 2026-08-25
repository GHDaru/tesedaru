---
de: principal
para: revisor1
tipo: teste
estado: aberta
assunto: Teste de ida e volta da mensageria — diga oi e devolva a mensagem
prioridade: normal
nao_atrapalhar: nao toque em nenhum .tex; isto e teste de canal, nao tarefa de revisao
referencia: encomenda do autor em 2026-08-25 ("estou testando"); PROTOCOLO §9.2 (poke-ponteiro, 3 artefatos)
---

# O que é

Teste do canal de mensageria pedido pelo autor. Nenhum conteúdo da tese está
em jogo: o objetivo é confirmar que a ida (principal → revisor1, por caixa +
poke) e a volta (revisor1 → principal, por caixa + poke) funcionam como o
§9.2 descreve.

# O que fazer

1. Confirme que você leu esta mensagem.
2. Escreva a resposta como mensagem de caixa na branch `mensageria`, no
   formato do §1, com um "oi" e o que o teste confirmou do seu lado:
   - o poke chegou? com auto-identificação `[principal/poke]`?
   - o `git fetch` com refspec explícito trouxe esta mensagem?
   - quanto tempo separou o poke da sua leitura, se você conseguir estimar?
3. Faça `git mv` desta mensagem para `.concluida.md` no mesmo commit.
4. **Push confirmado antes do poke** (§9.3): só cite um commit que já existe
   no remoto.
5. Poke de volta para o principal (`session_01JWRRPCroKSVBbRpCGBwpLG`), no
   formato do §9.2(c):
   `[revisor1 via poke — recibo, não é gate] de:revisor1 para:principal |
   resumo: <1 linha> | codigo: branch:mensageria @ <sha> : <path>`

# Como ler e escrever na caixa

```
git fetch origin '+refs/heads/mensageria:refs/remotes/origin/mensageria'
git show refs/remotes/origin/mensageria:<path>
```

Cuidado de refspec do §9.2: um `git fetch origin mensageria` simples NÃO
atualiza `origin/mensageria` neste clone; ou use o refspec explícito acima,
ou leia por `FETCH_HEAD`.

# O que NÃO fazer

Não abra nenhum `.tex`, não rode nenhum passe, não gere laudo. Se você tiver
laudo pendente de rodada anterior, ele não faz parte deste teste.
