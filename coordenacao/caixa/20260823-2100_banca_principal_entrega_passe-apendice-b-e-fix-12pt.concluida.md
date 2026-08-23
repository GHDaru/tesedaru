---
de: banca
para: principal
tipo: tarefa
acao_esperada: integrar na main (1) o Apêndice B reescrito com a figura do laço e (2) a CORREÇÃO do esq-lce do Apêndice A (que já está na main com a fórmula transbordando em corpo 12); validar com a compilação completa (DoD IX) antes do merge
referencia: a2-ag/texto.tex + esq-ag-envelope.tex + esq-lce.tex · branch banca/esquemas-tikz-metodo · ordem do autor (2026-08-23)
criada_em: 2026-08-23T21:00:00Z
---
Conclusão do passe no Apêndice B (claim 2005 de hoje; ordem direta do
autor, com loop até excelência acadêmica). Ele já viu e recebeu as 3
páginas renderizadas.

1. **`a2-ag/texto.tex` reescrito**: autocontido (sem \ref para seções da
   tese, sem individual_id, sem "decisão D-002", sem nomes de formato de
   arquivo; anti-circularidade explicada em linha); Formulação em prosa
   contínua; proveniência consolidada em preâmbulo único que preserva a
   tripartição do laudo (notebook define; população e gerações conferidas
   contra artefatos; população sem fonte de configuração); números
   conferidos (2.000/4.000; 18,82/19,20; 30×40; 4×10 tamanhos 10–30.000);
   figura do laço inserida (fig:ap-ag-laco).
2. **`esq-ag-envelope.tex` REDESENHADO PARA CORPO 12**: a primeira versão
   (prévia em corpo 10) quebrava no corpo real da tese. Compilado como
   apêndice completo em 12pt/textwidth ~15cm: 0 erros, overfull 0,7pt.
3. **ATENÇÃO — correção que afeta a MAIN**: o `esq-lce` do Apêndice A (já
   integrado) tem a fórmula transbordando a caixa em corpo 12 (~4mm).
   Corrigido nesta branch (caixa 58→64mm, coluna reposicionada). Integrar
   junto.
4. **Pendência sistêmica registrada na NOTA**: esquemas 1/2/4/5 e o
   esq-drisl continuam calibrados em corpo 10 — re-verificar em 12pt antes
   de qualquer inserção. As prévias dos dois esquemas inseridos agora são
   renders de corpo 12.

O que não valido daqui: a tese inteira (sem toolchain ppginf) — a
compilação completa fica com a sua integração/cruzada.
