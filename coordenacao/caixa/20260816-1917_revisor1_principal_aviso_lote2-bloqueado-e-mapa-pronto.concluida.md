---
de: revisor1
para: principal
tipo: aviso
acao_esperada: (1) confirmar o número real de \cite do Cap. 2 (contei 8, a tarefa dizia 28); (2) dizer se eu executo o lote 2b (prosa, sem lock) já e em qual branch — meu ambiente me prende a claude/maestro-cycles-statistical-analysis-fwla6a; (3) avisar quando o revisor2 liberar o lock do referencias.bib
referencia: mapa em docs/mapa-duplicatas-bib.md @ 873f0a6 (branch claude/maestro-cycles-statistical-analysis-fwla6a) · lock coordenacao/locks/referencias.bib.md (revisor2, 19:11, no prazo)
criada_em: 2026-08-16T19:17:07Z
---
BLOQUEIO PARCIAL do LOTE 2. Quem destrava: revisor2 (lock de referencias.bib,
criado 19:11, dentro do TTL — não encostei nele). O que destrava: a metade do
lote que unifica as entradas no .bib.

NÃO ESPEREI PARADO: fiz toda a preparação que não precisa do lock e ela mudou
o desenho do lote. Mapa completo em docs/mapa-duplicatas-bib.md (873f0a6).
Nada aplicado: bib intocado, prosa intocada.

TRÊS ACHADOS QUE MUDAM A EXECUÇÃO:

1. DIVERGÊNCIA DE CONTAGEM. Só 6 dos 17 grupos têm as DUAS chaves citadas, que
   são os únicos que exigem mexer na prosa: 17 ocorrências de \cite, sendo
   9 no Cap. 1 (bate com a tarefa) e 8 no Cap. 2 (a tarefa dizia 28). Suspeito
   que as outras 20 do Cap. 2 sejam citações cuja chave PERMANECE e cujos
   metadados mudam nos lotes 1 e 3 — nesse caso a prosa não é tocada. Confirme
   antes de eu executar, para não editarmos a mesma linha duas vezes.

2. O GRUPO FreeAL É DO LOTE 1, NÃO DO 2. A chave citada (2-fundam:564) é
   `Su2023`, e é exatamente ela que carrega a autoria fabricada. A duplicata
   `FreeAL2023` está órfã. Ou seja, aqui não é apagar duplicata: é trocar
   metadados inventados pelos reais (Xiao et al., EMNLP 2023,
   DOI 10.18653/v1/2023.emnlp-main.896, pp. 14520-14535), trabalho do revisor2.
   Sinalizo para não corrigirmos em duplicidade.

3. UMA UNIFICAÇÃO MUDA O TEXTO IMPRESSO. `Bayer2024` (2024) e
   `Bayer2024ActiveLLM` (2026, TACL v.14) são a mesma obra, e o parecer manda
   ficar com a segunda. As 10 citações passam a imprimir "(BAYER; LUTZ;
   REUTER, 2026)" em vez de "(BAYER; REUTER, 2024)" — muda ano e autoria
   visíveis ao leitor. Não é troca mecânica; merece o olho do autor no gate.

CAUSA-RAIZ das 17 duplicatas (para a retrospectiva): Cap. 1 e Cap. 2 foram
escritos com convenções de chave diferentes — slug minúsculo no Cap. 1
(`devlin2019bert`, `song2014shorttext`) e CamelCase no Cap. 2 (`Devlin2019`,
`Song2014`) — e cada capítulo cadastrou a mesma obra sob a sua convenção. É
padrão sistemático, não descuido pontual; por isso as duplicatas se concentram
nesses dois capítulos.

PROPOSTA DE ORDEM: as 6 chaves canônicas JÁ existem no bib, então a troca dos
\cite na prosa compila sem quebrar e NÃO precisa do lock. Posso executar o
lote 2b agora e deixar a limpeza do .bib (2a) para quando o lock cair. Diga
se autoriza e em qual branch — sobre a branch única bibfix/lotes preciso da
sua confirmação, porque meu ambiente exige que eu empurre para a minha branch
designada; se preferir, o revisor2 abre bibfix/lotes e eu rebaseio.
