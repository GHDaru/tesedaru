# Parecer da banca — Migração de `referencias-pdf/` para repositório privado

Data: 2026-08-16 · Agente: banca · Decisão do autor: mover os PDFs para um
repositório **privado** (conversa de 2026-08-16). Este documento descreve o
procedimento; a execução é de outro agente (banca não edita superfície alheia)
e o gate é do autor, via principal.

## 1. Por que (o problema)

`referencias-pdf/` contém **140 PDFs versionados** (294 MB no working tree; 155
blobs no histórico) dentro de `GHDaru/tesedaru`, que é **público**. Parte
relevante são artigos de Elsevier, IEEE, Springer, Sage e MDPI-pagos, cujas
licenças proíbem redistribuição. Consequências:

- **Jurídica/reputacional**: republicação de obra com copyright, em repositório
  associado ao nome do autor e à UFPR, durante o processo de defesa.
- **Persistência**: apagar na `main` não basta — os blobs continuam acessíveis
  pelo SHA e por clones/forks existentes. Exige reescrita de histórico.
- **Operacional**: 294 MB inflam clone e CI de todos os agentes.

Não afeta o mérito da tese e **não bloqueia a banca**; é higiene com prazo,
melhor resolvida antes do depósito e da divulgação do repositório.

## 2. Princípio da solução

Os PDFs **não são evidência da tese** — a evidência é o fichamento (que é
autoral e fica) mais o DOI/URL da obra (que é ponteiro público e legítimo).
Logo, mover 100% dos PDFs para privado não perde nada verificável, e evita a
triagem caso a caso entre licenças abertas e fechadas (arXiv/ACL seriam
redistribuíveis, mas a economia não compensa o risco de classificar errado).

## 3. Procedimento (5 fases, com dono e ponto de retorno)

### Fase 0 — Preparação (autor + executor) · reversível
1. Autor cria repositório **privado** `GHDaru/tesedaru-pdfs` (sem README que
   liste títulos — o índice fica na tese, não lá).
2. Executor faz **backup completo fora do git**: cópia de `referencias-pdf/`
   e um `git bundle` do repositório atual (`git bundle create ../tesedaru-pre-purge.bundle --all`).
   Sem esse bundle, a Fase 3 não começa.
3. Aviso na caixa: **congelamento de push** em `tesedaru` durante as Fases 3–4
   (a reescrita invalida os commits de quem estiver com branch aberta).

### Fase 1 — Popular o repositório privado · reversível
4. Copiar os 140 PDFs para o repositório privado, preservando os nomes de
   arquivo (é a chave de ligação com o campo `pdf:` dos fichamentos).
5. Commit + push no privado. Conferir contagem: 140 arquivos, mesmos nomes.

### Fase 2 — Desligar do repositório público (sem reescrever histórico ainda) · reversível
6. `git rm -r --cached referencias-pdf` (mantém os arquivos em disco).
7. Acrescentar `referencias-pdf/` ao `.gitignore`.
8. Atualizar quem cita o caminho: `.claude/skills/fichamento/SKILL.md`,
   `docs/inventario-prontidao-2026-08-16.md`. **Não alterar o campo `pdf:` dos
   141 fichamentos** — o caminho relativo continua válido para quem clonar os
   dois repositórios lado a lado; documentar isso em uma linha no README.
9. Commit + push. A partir daqui o repositório público **para de crescer** com
   PDFs, mesmo antes da limpeza do histórico.

### Fase 3 — Reescrita de histórico (irreversível — exige gate explícito do autor)
10. `git filter-repo --path referencias-pdf --invert-paths` (ferramenta
    recomendada pelo GitHub; `filter-branch` está obsoleto).
11. Conferir: `git count-objects -vH` (esperado: queda de ~290 MB) e
    `git rev-list --objects --all -- referencias-pdf` deve retornar **0**.
12. `git push --force-with-lease` em **todas** as refs. Exceção declarada ao
    "force-push em main é proibido" do PROTOCOLO §4 — só vale para esta
    operação, autorizada nominalmente pelo autor, com o bundle da Fase 0 como
    rede de segurança.
13. Cada agente com branch aberta refaz a sua sobre a nova `main`
    (`git rebase --onto`), guiado por um aviso do principal com o passo a passo.

### Fase 4 — Limpeza do lado GitHub (autor)
14. A reescrita **não** remove os objetos do servidor automaticamente: abrir
    chamado no GitHub Support pedindo *garbage collection* do repositório e
    informando que houve remoção de conteúdo por copyright.
15. Verificar forks e clones conhecidos (`Tese-Vers-o-Draft`, qualquer fork de
    terceiros): enquanto existir fork com os blobs, o conteúdo segue acessível.

### Fase 5 — Fechamento
16. ADR registrando decisão, escopo e a exceção ao §4 do protocolo; linha em
    `decisoes.jsonl`.
17. Item no plano: "PDFs em repositório privado" com estado concluído e
    ponteiro para o privado.

## 4. DoD verificável (na fonte, sem PDF compilado)

| Critério | Comando |
|---|---|
| Nenhum PDF de referência rastreado | `git ls-files referencias-pdf \| wc -l` → **0** |
| Nenhum blob no histórico | `git rev-list --objects --all -- referencias-pdf \| wc -l` → **0** |
| Repositório enxuto | `git count-objects -vH` → *size-pack* < 50 MB |
| Ignorado daqui em diante | `git check-ignore referencias-pdf` → sai 0 |
| Fichamentos intactos | 141 arquivos com campo `pdf:`, inalterados |
| Privado completo | 140 arquivos no `tesedaru-pdfs`, nomes idênticos |
| Nada quebrou | `scripts/check-links.sh` e `check-fichamentos.py` verdes |

## 5. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Perda de trabalho de outro agente na reescrita | Congelamento anunciado (Fase 0.3) + bundle + rebase guiado (13) |
| Blobs continuarem acessíveis por fork/cache | Chamado ao GitHub (14) + varredura de forks (15) |
| Quebrar o KG/fichamentos | Não mexer no campo `pdf:`; DoD confere 141 |
| Fazer no meio do mínimo-banca | **Executar depois** do bib-fix e do lote do veredito: são as frentes com branches abertas; a reescrita atrapalharia |

## 6. Recomendação de sequenciamento

Fases 0–2 podem rodar **já** (reversíveis, param o sangramento). As Fases 3–4
(irreversíveis) devem esperar o fechamento do bib-fix e das edições do
mínimo-banca, quando houver menos branches vivas. A prioridade continua sendo
o texto que vai à banca; isto é dívida com prazo, não bloqueio.
