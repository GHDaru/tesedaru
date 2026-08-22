---
de: executor02
para: principal
tipo: aviso
acao_esperada: BLOQUEIO — falta OPENAI_API_KEY e MAAS_API_KEY (+MAAS_BASE_URL) para rodar a calibração; peça ao autor as duas chaves (ou confirme se alguma já existe em cofre que eu não enxergo) antes que eu gaste algo
referencia: tarefa 20260823-0230 · experiments/e0/config_calibration.json · REPRODUCIBILITY.md §3 (Credenciais)
criada_em: 2026-08-23T02:45:00Z
---

Nada rodado ainda — bati num bloqueio de credencial antes de gastar
qualquer coisa, exatamente como a tarefa pediu.

## O que verifiquei antes de tentar rodar

O `config_calibration.json` já existe e está bem formado: 100 itens (amostra
`rand`, semente 42, pareada — as MESMAS instâncias nos 3 tamanhos de lote),
2 modelos (`gpt-4o-mini` via OpenAI; `deepseek-v4-flash` via `huawei-maas`),
`items_per_call` em 1/10/25 para cada um — 6 execuções de oráculo no total.
Custo esperado é baixo (modelos baratos, DeepSeek com preço explícito no
próprio config: US\$0,135/0,135/0,27 por Mtok; gpt-4o-mini é da mesma faixa)
— mas eu não tenho como estimar em dólares sem saber se já existe conta/
crédito alocado, e de qualquer forma o problema agora não é custo, é acesso:
**não tenho nenhuma das duas chaves.**

Não existe `.env` na raiz do `activelearning` nesta sessão, e nenhuma das
variáveis (`OPENAI_API_KEY`, `MAAS_API_KEY`, `MAAS_BASE_URL`) está no
ambiente. `REPRODUCIBILITY.md §3` confirma que são essas as duas que o
`run_e0.py` precisa — sem chave, o provider é pulado silenciosamente (não dá
erro, só não produz nada), então rodar assim geraria um artefato incompleto
que pareceria válido. Preferi parar e perguntar a rodar pela metade.

## O que preciso

As duas chaves (`OPENAI_API_KEY`; `MAAS_API_KEY` + `MAAS_BASE_URL` do
provedor `huawei-maas`), num canal que não seja a caixa/commit (o
repositório é público — se o autor for passar, que seja por onde ele já
passou a chave da NVIDIA antes). Se alguma já estiver disponível em outro
lugar que eu não enxergo desta sessão, digam onde.

## Estado

Nenhum artefato gerado, nenhum McNemar medido, nenhuma degradação
detectada — a tarefa não chegou a começar. `results_calibration/` continua
não existindo. Não editei nada de texto. Assim que tiver as chaves eu rodo e
reporto o p real dos dois contrastes (b=1 vs b=10; b=1 vs b=25).

Caixa atualizada: esta é a mensagem nova, é bloqueio — registro aqui e
sigo disponível, não fico esperando parado; se houver outra frente
enquanto isso, aviso e pego.
