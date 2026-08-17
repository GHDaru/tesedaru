---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: aplicar a rota (a) do Deng2023fedal aprovada pelo autor — entrada vira @article do periódico (JID 2025, DOI conferido); baixar o PDF certo (arXiv 2406.11310) e fichar, fechando o último item do R3 do t2
referencia: sua proposta em 20260817-0230 · decisão do autor 2026-08-17 · bibfix/lotes
criada_em: 2026-08-17T03:15:00Z
---
Autor aprovou a rota (a). Na branch bibfix/lotes, com lock:

1. Entrada Deng2023fedal vira @article: Journal of Investigative Dermatology,
   v. 145, n. 2, pp. 303-311, year=2025, DOI 10.1016/j.jid.2024.05.023 —
   conferindo tudo no Crossref antes de gravar, como sempre. Manter também o
   eprint correto (2406.11310) como campo adicional se o estilo aceitar.
2. Chave permanece Deng2023fedal (decisão do autor: não renomear; chave é
   interna e não imprime).
3. A citação da linha ~327 usa \cite, então o ano impresso atualiza sozinho
   pelo bib — se você constatar ano HARDCODED na prosa, não toque: me avise,
   que prosa é minha.
4. Substituir a_sanear/Deng2023fedal.pdf pelo PDF correto (arXiv 2406.11310,
   conferir 1ª página) e FICHAR — fecha o R3 do t2 por completo.
5. Este conserto entra no mesmo bloco do gate final do bib (junto com a
   remoção Wu2022/Ahmed2023 da tarefa 20260817-0305 e os fichamentos
   Rouzegar/Fromme).

## Resultado (revisor1, 2026-08-17T03:15Z)

Fichamento em fichamentos/Deng2023fedal.md, branch
claude/maestro-cycles-statistical-analysis-fwla6a @1138012. PDF correto baixado
de arXiv 2406.11310 e conferido na 1a pagina; o PDF errado foi removido de a_sanear/.
Itens 1 e 2 da tarefa: NAO foram necessarios — a entrada ja estava corrigida na
bibfix/lotes desde o lote 1 (51072c1, revisor2), e reconferi tudo no Crossref.
Item 3: nao ha ano hardcoded na prosa; \cite limpo, o ano atualiza no gate.
R3 do t2 fechado por completo. Detalhe e o risco de processo: coordenacao/caixa/20260817-0315_revisor1_principal_aviso_deng-fichado-e-conserto-ja-existia.aberta.md
