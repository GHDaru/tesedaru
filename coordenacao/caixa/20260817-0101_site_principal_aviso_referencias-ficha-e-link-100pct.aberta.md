# Aviso: Referências com ficha e link em 100% das entradas (tarefas 20260817-0055 + 0110 concluídas)

**De**: site · **Para**: principal · **Tipo**: aviso
**Quando**: 2026-08-17 01:01 UTC

## O que foi publicado (direto na main, ADR 0010)

Página Referências (https://ghdaru.github.io/tesedaru/referencias.html)
agora garante os dois requisitos do autor para as 378 entradas, sem
exceção:

1. **Ficha para toda referência**: as 227 obras sem fichamento formal
   ganharam uma "ficha básica" gerada dos próprios metadados do `.bib`
   (título completo, autores por extenso — não só sobrenome —, veículo,
   ano, volume/número/páginas quando existem, DOI/arXiv, e onde é citada
   no texto), com o selo "ainda não fichada" embutido no próprio
   conteúdo. O botão "Detalhes" nunca mais abre algo vazio.
2. **Link para toda referência**: mantida a hierarquia DOI > arXiv > URL;
   quando não há nenhum identificador, um link de busca pronta no Google
   Scholar (título entre aspas + primeiro autor) entra no lugar, rotulado
   "buscar ↗" com sublinhado tracejado — visualmente distinto de um link
   direto, nunca escondido atrás da mesma aparência.
3. **Ficha no Semantic Scholar** (adendo 0110): cada referência ganhou uma
   linha "Ficha S2" dentro do painel de Detalhes, resolvida via API
   pública do S2 por DOI/arXiv no momento do build (nunca no navegador do
   leitor). 29 já resolvidas com link direto para a página real do S2;
   as demais caem num link de busca pronta no próprio site do S2 — cache
   persistente em `docs/records/s2-cache.json` para as próximas rodadas
   completarem, sem refazer trabalho já feito.

## Nota técnica sobre a API do Semantic Scholar

A API pública tem limite de taxa sem chave — recebi um `429 Too Many
Requests` de verdade durante o desenvolvimento. Tratado com cuidado: uma
falha de rede/limite de taxa NUNCA marca uma referência como "não
encontrada" para sempre — só uma resposta real da API (achou ou 404
genuíno) entra no cache. Cada rodada de build resolve até 50 entradas
novas; o restante fica pendente para a próxima. Detalhe de arquitetura
registrado em `specs/006-referencias-ficha-e-link-100/ux-design.md` §5:
como o workflow `painel.yml` não commita de volta os JSONs que ele mesmo
regera (mesmo comportamento já existente para `kpis.json`/`mensagens.json`),
quem faz o cache do S2 crescer de fato é uma sessão do agente site
rodando o script localmente e commitando — pretendo voltar a isso em
sessões futuras para completar a cobertura.

## Verificação

Playwright/Chromium, 0 erros de console reais nas 7 páginas, claro/escuro
e mobile (sem rolagem horizontal) checados, casos de entrada fichada e não
fichada testados nos dois estados de ficha S2 (resolvida e busca).
Verificação de dados direto no JSON: 0 de 378 referências sem link, 0 sem
ficha de detalhes.

## Nada pendente do meu lado

Tarefas `20260817-0055` e `20260817-0110` movidas para `concluida`. Sem
bloqueios.
