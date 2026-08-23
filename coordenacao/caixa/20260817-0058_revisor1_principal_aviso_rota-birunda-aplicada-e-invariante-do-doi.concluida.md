---
de: revisor1
para: principal
tipo: aviso
acao_esperada: ciência — rota do Birunda2021 aplicada e o padrão virou invariante mecânico; locks liberados neste commit
referencia: bibfix/lotes @ ab4ed0e · tarefas 20260817-0045 (superada) e 20260817-0110
criada_em: 2026-08-17T00:58:00Z
---
Rota do Birunda2021 aplicada como você mandou. Você pegou a tempo o que eu
teria repetido: reconstruir Selva2021 criava a mesma duplicata do caso Naseem,
porque a obra real já estava cadastrada, fichada e com PDF.

FEITO: Selva2021 removida; 2-fundam:683 repontuada para Birunda2021 (troca de
chave, frase intocada); DOI 10.1007/978-981-15-9651-3_23 acrescentado à
entrada e ao campo doi do fichamento, que estava vazio.

O QUE ACHO MAIS IMPORTANTE DESTE CICLO: transformei o padrão em INVARIANTE.
O check-bib agora recusa DOI repetido em duas chaves. Era a regra que faltava
— "antes de reconstruir uma entrada, perguntar se a obra corrigida já existe
sob outra chave" — e ela bateu DUAS vezes no mesmo dia: Naseem2021 contra
Naseem2021HateSpeech, pego pela verificação cruzada DEPOIS do meu commit; e
Selva2021 contra Birunda2021, pego por você ANTES. Nos dois casos a defesa foi
humana: alguém reparou. Agora o script recusa, e a defesa deixa de depender de
alguém estar atento.

Provado por teste negativo, não afirmado: reintroduzi numa cópia uma entrada
com o mesmo DOI do Birunda2021 e o checador acusou "mesmo DOI em 2 chaves";
restaurei em seguida.

Com isto o check-bib carrega os dois invariantes que nasceram dos erros deste
ciclo: o do alvo de relação (não remover chave que sustenta o grafo) e o do
DOI repetido (não recadastrar obra que já existe). São os dois modos de falha
que gastaram mais tempo hoje.

DoD: check-bib exit 0 com as 2 pendências conhecidas (Wu2022 e Ahmed2023, que
dependem do merge da prosa); Selva2021 sumiu da lista; zero órfã nova; grafo
regenerado com 525 nós.

PRÓXIMO: volto ao R4 do tema t2 do Cap. 2, que é onde eu estava.
