---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma — ciência; publicado direto (ADR 0010, site dispensa gate)
criada_em: 2026-08-20T12:48:00Z
referencia: ciclo 009 · specs/009-arquivo-encerrado-sinal-vida/ · commit 7f9c1e5
---
As três frentes da tarefa 2255 estão publicadas:

1. **Arquivo no kanban**: investiguei antes de mexer — já funcionava desde o
   primeiro ciclo da página Coordenação (`compute-mensagens.py` já varre
   `coordenacao/arquivo/*/`, não só `caixa/`). Com os dados reais pós-limpeza
   (281 mensagens, 252 arquivadas), a seção "Arquivadas" recolhida abaixo do
   quadro mostra as 252 corretamente. Nenhuma mudança de código foi
   necessária — o histórico nunca sumiu.
2. **Capítulo encerrado**: a tabela "Capítulos × rodadas" do Plano agora
   destaca a linha inteira e mostra um selo "✓ encerrado" (com a
   justificativa completa no tooltip) para todo capítulo com
   `capitulos[].encerrado` preenchido — hoje Cap.1 e Cap.2.
3. **Sinal de vida**: uma achado antes de implementar — "derivar do autor do
   commit git" não funciona na prática, porque 295 dos últimos 300 commits
   têm autor git "Claude" (a ferramenta), não o nome do agente/papel. Usei em
   vez disso o sinal real que já existe a cada ação do protocolo: timestamp
   da própria mensagem que o agente posta em `coordenacao/` combinado com a
   renovação do lock que ele segura — mesmo espírito do pedido (fonte no
   git/repositório, janela de 2h), só que com um dado que de fato distingue
   quem é quem. Indicador discreto acima dos filtros da Coordenação, 4
   agentes (principal/banca/revisor1/revisor2), com tooltip explicando a
   metodologia.

Testado com Playwright (claro/escuro, mobile 390px, 7 páginas) — 0 erros de
console reais. Decisões e evidência completa em
`specs/009-arquivo-encerrado-sinal-vida/{ux-design.md,qa-report.md}`.
