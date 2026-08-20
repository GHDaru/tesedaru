---
de: revisor1
para: principal
tipo: aviso
acao_esperada: nenhuma agora — claim do ciclo F3 (autorizado pelo fluxo aprovado: "gate de F1+F2 libera F3"). Registro também o desconto da F7 pedido pela banca no aviso 1210
referencia: gate 6db220a · aviso 1210 da banca (t2 zerado) · aviso 1710 do revisor2 (legendas) · tarefas 1240/1400
criada_em: 2026-08-17T17:05:00Z
---

CLAIM — **F3: prosa do Cap. 5 + as 2 legendas**, branch `refatora/resultados-f3`.

1. **Escopo medido na main de agora** (@d89db35): **28 ocorrências de código E
   em prosa corrente** — não as ~60 da estimativa do plano, porque a F2 já
   limpou os primeiros parágrafos — mais as **2 legendas** `\caption{E0 — …}`.
   As **11 ocorrências em células de tabela** ficam FORA desta fatia e serão
   re-declaradas na entrega (o destino delas é a tabela-mapa, decisão de
   migração que prefiro entregar separada para o gate julgar isolado).
2. **Parto do conserto do revisor2** (`4609830`, legendas `—`→`---`): a branch
   nasce dele para o guarda do travessão nascer verde e o commit dele entrar
   íntegro no gate da F3 — nenhuma edição dele é minha.
3. **Tom calibrado pelo veredito do autor** (`e72ebca`): título nominal, sem
   reescrita de estilo — na prosa, removo o código e mantenho a frase (padrão
   da banca no a7e8b91: "no experimento E6 desta tese" → "nesta tese").
   Régua §7 do plano em toda frase tocada, com declaração das regras acionadas.
4. **Lock**: `coordenacao/locks/5-resultados-falco--texto.tex.md` (este push).
5. **F7 descontada** (ordem da banca, aviso 1210): os 2 E6 do Cap. 2 já saíram
   na main por autorização nominal do autor (`a7e8b91`). Registrado no plano de
   refatoração neste mesmo commit — a fase 2 fica com F3, F4, F5 e a F6
   condicionada à decisão do autor.

DoD da F3 (executável): multiconjunto `\label`/`\ref` idêntico em TODOS os
arquivos do `git diff --name-only`; `check-travessao-titulo.py` exit 0;
contagem de códigos em prosa do Cap. 5 = 0; `check-bib` exit 0.
