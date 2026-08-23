---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
assunto: Re-cruzar o A2 refinado (@1158bf8) + passar ao executor02 a referência exata da 3ª config (pop 100)
prioridade: alta
---

Duas coisas curtas:
1. **Re-cruzar o lote A2 refinado** da banca — ponta `banca/lote-a2-cap3-a7-laudo @1158bf8` (4 ressalvas com a fonte do notebook, nota do L0=10, população mantida). Rode o `confere-config-ag.py` e confirme; é minutos.
2. **Passe ao executor02** (que está fechando a pendência de reprodutibilidade da população) a **referência exata da 3ª configuração (pop 100, 200 gerações)** que você apontou — ele varreu e não achou o artefato; precisa do caminho/arquivo exato para mapear as três (_oldold=50 / canônica=20 / essa=100).

Entregue em branch/caixa ao principal (v1.5 §2-ter). Retorne em prosa com o veredito da re-cruzada e a ref da pop 100.
