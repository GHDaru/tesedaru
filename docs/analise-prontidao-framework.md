# Framework de análise de prontidão para a banca (Rodada 4 — proposta)

Data: 2026-08-16 · Sessão de revisão crítica pré-banca.
Insumos: inventário (rodada 1), auditoria de escrita (rodada 2), normas
UFPR/PPGMNE e varredura de skills (rodada 3), pareceres R1-R5, ADR 0001.

## Racional da proposta

Os pareceres simulados (R1-R5) já cobrem o mérito científico com rubrica
própria (5 dimensões ponderadas; R5 = 88,4, "defensável"). O que NÃO existe
ainda é um instrumento que responda à pergunta operacional: **"pode mandar
para a banca?"**. A proposta é um scorecard de gates binários com evidência
rastreável, agrupados em 6 dimensões, cada gate classificado como
**[B] bloqueante** (impede envio) ou **[NB] não-bloqueante** (registra-se e
segue). Veredito possível: PRONTO · PRONTO COM RESSALVAS (só NB abertos) ·
NÃO PRONTO (algum B aberto).

A régua de escrita usa os limiares calibrados do ADR 0001 (não a regra crua
da skill humanizer, que é anglófona): densidade de travessões alvo ≤5/1000
palavras por capítulo (Cap. 1 humanizado ficou em 3,0), zero fórmula
enumerativa "N achados/leituras/...", zero staccato dramático e zero fecho
aforístico; negritos definicionais e tríades técnicas são preservados.

## Dimensões e gates

### D1. Ciência fechada (fonte: R5, regra de ouro)
- G1.1 [B] Hipótese central testada e respondida no texto, com estatuto declarado.
- G1.2 [B] Todo número do texto rastreável a artefato em `GHDaru/activelearning`.
- G1.3 [B] Nenhum achado científico fora do texto (auditoria de achados em dia).
- G1.4 [NB] Limitações com direção de viés declarada em todas as escolhas econômicas.

### D2. Escrita anti-slop (fonte: rodada 2 + ADR 0001)
- G2.1 [B] Ciclo de humanização calibrada executado com gate humano em TODOS os
  capítulos + resumo/abstract (hoje: só Cap. 1).
- G2.2 [B] Densidade de travessões ≤5/1000 palavras em cada arquivo de texto.
- G2.3 [B] Zero fórmula enumerativa; staccato e fechos aforísticos tratados.
- G2.4 [NB] Vocabulário de IA e atribuições vagas = zero (já atingido em 16/08).
- G2.5 [NB] Cadência de frases variada nos parágrafos apontados pela auditoria.

### D3. Conformidade SiBi/UFPR (fonte: rodada 3)
- G3.1 [B] Todos os elementos obrigatórios presentes e na ordem do quadro SiBi.
- G3.2 [B] Ficha catalográfica OFICIAL solicitada à biblioteca do programa
  (com DOI da base de dados incluído).
- G3.3 [B] Palavras-chave explícitas no resumo (PT) e abstract (EN).
- G3.4 [NB] Posição da declaração de uso de IA confirmada com o programa.

### D4. Conformidade PPGMNE (fonte: rodada 3)
- G4.1 [B] Template confirmado com secretaria/orientador (`ppginf.cls` × modelo
  ABNT UFPR do programa) — resposta registrada em `docs/records/decisoes.jsonl`.
- G4.2 [B] Lattes atualizado com toda a produção do período.
- G4.3 [B] Checklist de defesa aprovado pela coordenação (pré-SIGA).
- G4.4 [NB] Portarias de composição de banca conferidas (H-index dos membros).

### D5. Integridade técnica do documento
- G5.1 [B] Compila com 0 erros, 0 referências indefinidas, 0 warnings BibTeX.
- G5.2 [B] 0 citações órfãs (toda chave citada existe no `.bib`) e 0 \ref quebrado.
- G5.3 [NB] Toda figura/tabela citada no texto; siglas expandidas no 1º uso.
- G5.4 [NB] `a_sanear/` vazio (triagem concluída).

### D6. Pendências operacionais (fonte: R5 §4)
- G6.1 [B] Frase de proveniência dupla no Cap. 3.
- G6.2 [NB] Licença da base no Kaggle (CC BY 4.0) decidida e aplicada.
- G6.3 [NB] Rotação das 5 chaves de API.
- G6.4 [NB] Autoria/ordem dos 5 artigos decidida.
- G6.5 [NB] DOI Zenodo do código.
- G6.6 [NB] Proofreading final PT (após D2 fechar, para não retrabalhar).

## Procedimento de aplicação (rodada 5)

1. Preencher o scorecard gate a gate com evidência (arquivo, commit, medição
   ou "pendente + dono + esforço").
2. Emitir veredito (PRONTO / COM RESSALVAS / NÃO PRONTO) e a lista priorizada
   do caminho crítico: primeiro os [B] de menor esforço que destravam
   dependências (ex.: G2.x antes de G6.6).
3. Reaplicar o scorecard a cada ciclo de humanização mergeado; o scorecard é
   idempotente e barato (as medições D2/D5 são scriptáveis).

## Sugestão de direção (resposta ao item 4 do pedido)

O caminho crítico até a banca é: **(1)** ciclos de humanização calibrada
capítulo a capítulo com gate humano (resumo/abstract primeiro — são a pior
densidade e o cartão de visita da banca; depois 6→2 por ordem de densidade);
**(2)** em paralelo, as confirmações administrativas de baixo esforço e alto
risco de retrabalho (G4.1 template, G3.2 ficha); **(3)** por último,
proofreading final e pendências operacionais NB. Estimativa: 7 ciclos de
humanização restantes (resumo+abstract, 2, 3, 4, 5, 6, passe final).
