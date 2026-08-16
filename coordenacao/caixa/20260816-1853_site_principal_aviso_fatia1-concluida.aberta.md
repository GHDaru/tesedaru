---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma ação obrigatória — registro de conclusão da Fatia 1; leia se quiser repassar ao autor
referencia: tesedaru branch main (ec2bf01) · tarefas 20260816-1836/1837
criada_em: 2026-08-16T18:53:00Z
---
Fatia 1 concluída e publicada direto na main (ADR 0010), commits e1a4843 +
ec2bf01 (hash final ec2bf01).

## O que mudou
- 4 páginas geradas pela mesma função: Controle (index.html), Plano
  (plano.html), Coordenação (mensagens.html), Resultados (resultados.html,
  stub — Fatia 2 preenche).
- Sidebar recolhível (220px/60px), estado em localStorage, painel deslizante
  no mobile (<768px) com fechamento por ESC/clique fora.
- Sistema visual formalizado: cores mantidas do painel anterior + escala
  tipográfica 12/13/15/20/28/44px + espaço em múltiplos de 4px, num único
  CSS compartilhado pelas 4 páginas.
- ADR 0006 preservado: fila "Aguardando você" é o único grito visual (âmbar);
  estado nunca só por cor (glifo + palavra); burn-up eixo Y fixo 0–100%.
- Coordenação mantém a tabela de hoje dentro do casco novo (kanban é Fatia 2
  — não implementado ainda, por instrução da tarefa).
- Retirados docs/records/plano-artefato-template.html e
  mensagens-template.html — o HTML nasce inteiro do script agora (a
  arquitetura de template com marcador não serve mais 4 páginas geradas por
  uma função compartilhada de sidebar).

## Achado durante o teste (documentado no commit e1a4843)
As três páginas com JS (Controle/Plano/Coordenação) aninhavam
`<script type=application/json>` DENTRO do `<script>` executável — o HTML
fecha um `<script>` no primeiro "</script" literal, então o aninhamento
cortava a lógica ao meio (causa do "Unexpected token '<'" e de atributos SVG
aparecendo como `${W}` sem substituir, no meu primeiro teste local).
Corrigido antes de publicar: blocos JSON como irmãos do `<script>` de lógica.

## Evidência
- Testado no Chromium (Playwright) local antes E depois do deploy: 0 erros de
  console nas 4 páginas, navegação por clique funcional, sidebar recolhe e
  persiste, tema claro/escuro corretos, painel mobile abre/fecha.
- As 4 URLs conferidas ao vivo (200, sem erro de console) após o deploy do
  GitHub Actions (run 31965835478, sucesso):
  - https://ghdaru.github.io/tesedaru/
  - https://ghdaru.github.io/tesedaru/plano.html
  - https://ghdaru.github.io/tesedaru/mensagens.html
  - https://ghdaru.github.io/tesedaru/resultados.html

## Próximo
Começo a Fatia 2 (kanban da Coordenação + Resultados de verdade) agora, como
instruído — "publique a Fatia 1 antes de começar a Fatia 2" já está feito.
