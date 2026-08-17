---
de: revisor2
para: principal
tipo: aviso
acao_esperada: levar ao autor as 2 decisões de prosa que travam o fechamento do lote 1; avisar revisor1 que a branch bibfix/lotes já existe (ele rebaseia); lote 3 em execução
referencia: branch bibfix/lotes @ 51072c1 · docs/parecer-auditoria-bib.md §1 · tarefa 20260816-1849
criada_em: 2026-08-16T19:15:14Z
---
LOTE 1 CONCLUÍDO em bibfix/lotes (51072c1). A branch já está aberta — revisor1
rebaseia o lote 2 em cima.

O QUE MUDOU: 12 hipóteses do parecer confirmadas na fonte, 1 refutada, 1 com
correção do próprio parecer. 5 chaves mortas, 2 renomeadas, 8 com metadados
substituídos. Repontuei as citações nos Caps. 1-2 (9 sítios).

EVIDÊNCIA: scripts/check-bib.py, novo, com 6 invariantes — zero chave citada
ausente do bib, zero duplicata, zero chave morta ressuscitada, zero resíduo de
conversa de modelo em campo note, zero campo key= residual. Ele pegou um erro
MEU durante a execução (renomeei uma entrada sem repontuar a citação), o que é
a prova de que a checagem funciona. Fichamentos seguem verdes, grafo 527 nós.

CORREÇÕES QUE O PARECER NÃO TINHA CERTAS (registre para a banca, lote 4):
1. Xia2025 é ACL trilha PRINCIPAL, não Findings.
2. Ahmed2023 NÃO é obra distinta com metadados errados: é variante alucinada
   da mesma obra que já está no bib como Ahmed2022, e a tese cita as duas
   juntas. Trocar pelo artigo que o parecer sugeria injetaria no bib uma obra
   que o autor nunca leu.
3. Zhang2025 e Deng2023fedal têm versão publicada em periódico (o parecer só
   tinha o preprint). Adotei as publicadas.
4. Bayer/ActiveLLM: o ano da obra publicada é 2026 (TACL v.14), não 2024 — a
   chave guarda o ano do preprint. A tese passa a imprimir (BAYER; LUTZ;
   REUTER, 2026), coerente com o intervalo "2020-2026" já declarado na tabela
   de lacunas.

DUAS DECISÕES DO AUTOR TRAVAM O FECHAMENTO. Nos dois casos a entrada é
fantasma, mas matá-la agora quebraria a compilação, porque a prosa ainda cita:

(A) Cap. 2, linha 619 — "seleção ativa em múltiplos níveis: de instâncias, de
    prompts e do próprio oráculo \citep{Wu2022}". A obra Wu2022 não existe. O
    parecer mandava redirecionar para o survey de Zhang/Strubell/Hovy, mas
    esse survey é anterior aos LLMs e não fala de prompts nem de oráculo —
    seria trocar uma referência fantasma por uma citação que a obra não
    sustenta. Sugestão: dividir a citação por nível — instâncias com o survey,
    prompts com Diao2023, e oráculo sem citação, por ser contribuição da tese.

(B) Cap. 2, linha 568 — "sistemas híbridos humano-LLM, que roteiam casos
    difíceis ao humano \citep{Margatina2023}". Já corrigi os metadados para a
    obra real, mas ela trata de escolher exemplos para o prompt, sem humano no
    laço: não sustenta a frase. Duas saídas: recitar Rouzegar2024 (que
    sustenta, mas já aparece 4 vezes no mesmo capítulo) ou manter Margatina e
    reescrever o item para "seleção ativa de demonstrações".

Ambas mexem em prosa do Cap. 2 — sua superfície, não a minha. Me diga a
decisão e eu aplico junto do fechamento, ou aplique você.

EM CURSO: lote 3. O checador já mapeou o tamanho real: 25 entradas citadas com
ano >= 2020 sem DOI nem URL (o DoD do parecer exige). Sigo por aí.
