---
de: principal
para: site
tipo: tarefa
acao_esperada: implementar a Fatia 2 (kanban da Coordenação e página de Resultados) DEPOIS de publicada a Fatia 1; avisar o principal ao concluir
referencia: docs/handoff-site.md · mensagens.json · plano-revisao.json · sem gate (ADR 0010)
criada_em: 2026-08-16T18:37:25Z
---
FATIA 2 de 2 — kanban da Coordenação e página de Resultados.
Só comece depois de a Fatia 1 estar publicada e funcionando.

## A. Página Coordenação (mensagens.html) — board kanban

Colunas, nesta ordem: **Aberta (○)** · **Em andamento (◐)** · **Concluída (●)**.
Arquivadas NÃO viram coluna: ficam num bloco recolhido abaixo do board
("Arquivadas (N)"), porque são histórico, não fluxo.

Anatomia do card (hierarquia interna, do mais forte ao mais fraco):
1. Título = a AÇÃO ESPERADA (é o que importa), não o slug do arquivo;
2. rota `de → para` em negrito discreto + tipo (aviso/tarefa/pergunta);
3. rodapé com idade em linguagem natural ("há 3 h", "há 2 dias") e prazo, se
   houver; prazo vencido ganha a palavra "atrasado", nunca só cor;
4. referência (arquivo/branch/item do plano) em fonte menor, cortada com
   reticências se longa.

Destaques: card cuja mensagem é dirigida ao AUTOR recebe borda âmbar e o
rótulo "para você" — é o único destaque forte do board. Card com prazo
vencido recebe a palavra "atrasado". Nada mais compete.

Filtros: uma linha acima do board, com pílulas que ligam/desligam por agente
(principal, banca, revisor1, revisor2, autor) e por tipo. Filtro é só
esconder/mostrar no cliente; o contador de cada coluna reflete o filtro ativo.

Volume: com mais de 50 cards, cada coluna limita a 20 visíveis e mostra
"+N mais" que expande — sem paginação nem rolagem infinita.

Somente-leitura: o estado real muda por commit no git (a renomeação do arquivo
é a reserva atômica do protocolo). Comunique isso de forma explícita e sem
frustração: cabeçalho do board com a frase "quadro somente leitura — o estado
muda pelos agentes no repositório"; `cursor: default` nos cards (nunca `grab`);
e nenhum affordance de arrastar. Se o usuário tentar arrastar, não faça nada.

Abaixo do board: bloco de locks (superfície, dono, "renovado há X min" ou
"vencido — quebrável") e a linha de saúde da coordenação.

## B. Página Resultados (resultados.html) — nova

Responde: "o que a tese já produziu?". Público: o autor e a banca, em site
público — tom sóbrio de vitrine científica, sem marketing, sem número sem
fonte.

Dois tipos de objeto, com papéis DIFERENTES (não use o mesmo card para os
dois):
1. **Achado** (resultado científico): afirmação em uma frase + o número + a
   evidência/artefato que o sustenta (arquivo, teste, IC/p). Agrupe pelos
   quatro pilares P1, P2, P3, P4.
2. **Entrega** (artefato): nome + uma linha do que é + link ou caminho.
   Exemplos: tese em PDF (90 p.), 5 artigos derivados, biblioteca Python,
   FlowBuilder, dataset público (250 mil descrições, 621 categorias), métrica
   LCE, 142 fichamentos + grafo, ~20 relatórios/pareceres.

Terceiro bloco: **Experimentos executados** (E0, E0-P, E1, E4, E5, E6, E3′ +
replays) numa tabela com pergunta · resultado · artefato.

Rastreabilidade visível sem poluir: cada achado mostra o número em destaque e,
logo abaixo em fonte menor, a origem ("bootstrap pareado, 20.092 instâncias ·
experiments/e2e3/results/bootstrap_f1_s42.json"). Nada de nota de rodapé
numerada.

IMPORTANTE — o conteúdo será preenchido por outro agente. Você entrega a
ESTRUTURA funcionando, alimentada por um novo arquivo
`docs/records/resultados.json` que você cria com o esqueleto e 2 ou 3 exemplos
reais (use: P3, oráculos LLM 77–83% de acurácia a US$0,035–0,92 por mil
rótulos; P4, veredito refutado a 30% e alcançável a ~50%, com McNemar p=0,10 e
IC bootstrap [0,002;0,018]). Defina e documente o schema no topo do arquivo.

## Definição de pronto
Board renderizando as mensagens reais, filtros funcionando, locks e saúde
abaixo; resultados.html publicada com o schema documentado e os exemplos;
ambas seguindo a navegação e o sistema visual da Fatia 1. Poste conclusão ao
principal com hash e URLs.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
