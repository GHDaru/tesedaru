---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR — p real de gpt-4o-mini pronto (não é o que a tese cita hoje: 0,58 era de outro experimento); deepseek-v4-flash não mediu nada, é bloqueio de infraestrutura (endpoint MaaS 404), não achado de calibração; NÃO editei a frase da tese
referencia: tarefa 20260823-0230 · activelearning@e88c20c · experiments/e0/results_calibration/e0_mcnemar.json
criada_em: 2026-08-23T11:15:00Z
---

As 6 execuções fecharam. Dois resultados bem diferentes entre os modelos —
um é achado de verdade, o outro é bloqueio, não confundir os dois.

## gpt-4o-mini: p real medido, SEM degradação (b=10 até melhora)

| contraste | p (McNemar) | leitura |
|---|---|---|
| b=1 vs b=10 | **0,0391** | significativo — e a favor do b=10 (8 acertos exclusivos do b=10 contra 1 do b=1) |
| b=1 vs b=25 | 0,7905 | sem diferença |
| b=10 vs b=25 | 0,1797 | sem diferença |

Acurácia por lote: b=1 = 56%, b=10 = 63%, b=25 = 58% (n=100, pareado, mesmos
itens nos três). Custo cai forte com o lote: US\$0,28 → 0,05 → 0,03 por mil
rótulos (b=1→10→25).

**Isso muda a frase da tese (5-resultados:174).** Hoje ela diz "b=1 vs b=10:
p=0,58" — esse número é de outro experimento (b=20×b=50), não deste. O p
real é 0,0391, e a direção é **oposta a uma preocupação de degradação**: não
só não degrada, o b=10 sai significativamente melhor que o unitário. A
recomendação do próprio config ("usar o maior b sem degradação") aponta pra
**b=10** com folga — é mais barato que b=25 E com o melhor ponto medido.
Não decido a redação; devolvo o número para quem tem a superfície do Cap.5.

## deepseek-v4-flash: NÃO É achado de calibração — é bloqueio de infra

100% de respostas inválidas nos TRÊS tamanhos de lote, **inclusive b=1** —
não é efeito de lote, é o modelo não respondendo nada de válido em nenhuma
configuração. Abri o `raw_response` de várias anotações e é sempre o mesmo
erro, de toda chamada:

```
ERROR after 3 attempts: NotFoundError: Error code: 404 -
{'error_msg': 'The API does not exist or has not been published in the
environment', 'error_code': 'APIG.0101', ...}
```

Isso é o endpoint MaaS (`MAAS_BASE_URL` + o path do modelo
`deepseek-v4-flash`) não publicado/disponível no ambiente que a chave
aponta — configuração/infraestrutura, não ciência. Não tenho como calibrar
o lote deste modelo até isso ser corrigido do lado de quem gerencia o
provedor Huawei MaaS (endpoint certo, ou modelo publicado nesse ambiente).
Gastou tempo de parede (as 3 tentativas × timeout em cada uma das 100
chamadas, ~2h45 no total represadas pelo rate limit) mas praticamente nada
de crédito (`total_cost_usd: 0,0` nos três — chamada que falha não é
cobrada).

## Artefato

`experiments/e0/results_calibration/` (`activelearning@e88c20c`): as 6
anotações por instância (JSONL, retomável), os 6 relatórios, e
`e0_mcnemar.json`/`e0_table.json` com o McNemar completo (15 pares — inclui
os cruzados entre modelos, que não respondem à pergunta da calibração, mas
ficaram no artefato por serem gerados automaticamente pelo `analyze_e0.py`).

Não editei a frase da tese — o número está pronto para quem tem a
superfície do Cap.5 decidir a correção (e para alguém decidir se
`deepseek-v4-flash` entra ou sai da calibração até o endpoint ser
corrigido).

## Caixa

Atualizada com esta entrega. Sem tarefa pendente depois desta — sigo
disponível (braço E aguardando OK do autor, reconciliação rwatey aguardando
quem mergeia).
