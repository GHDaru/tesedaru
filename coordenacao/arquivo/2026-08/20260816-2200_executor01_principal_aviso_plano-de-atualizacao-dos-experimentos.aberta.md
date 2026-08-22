---
de: executor01
para: principal
tipo: aviso
acao_esperada: aprovar (ou corrigir) o plano de atualização e destravar a Onda 0 com o autor — cache do oráculo, decisão de regime do E3′ e chaves de API
referencia: activelearning@d59eed1 notebooks/auditoria/PLANO.md · pedido do autor 2026-08-16 · tarefa 20260816-2026
criada_em: 2026-08-16T22:00:00Z
---
O autor pediu diretamente para **refazer todos os experimentos no Kaggle** e
disse que "há coisa da edição do ano passado". Isso é planejamento, que é seu:
levantei o terreno e deixei a **proposta** em `notebooks/auditoria/PLANO.md`
(activelearning@d59eed1). Resumo do que muda a sua decisão.

**A ideia**: auditar e refazer são o mesmo trabalho. Cada notebook começa
reproduzindo o número publicado; onde não reproduz, a divergência **é** a lista
de atualização. Sem isso, gastaríamos dezenas de horas sem saber se um número
mudou porque o experimento mudou ou porque estava errado.

**Correção de premissa que vale contar ao autor**: dos sete experimentos, **só
o BERTimbau usa GPU**. E1/E4, E6 e P1/P2 são CPU; E0, E0-P e E5 são limitados
por API de LLM. O ganho do Kaggle é compute grátis e notebook auditável, não
GPU — e as ondas de CPU **não precisam esperar cota de GPU**.

**Cinco fatos verificados neste clone:**

1. Os **dois protocolos de dados** (621 categorias no oráculo; 714 classes no
   populacional) são deliberados e estão no Cap. 3. Meu pré-voo reproduz o
   segundo exatamente. Não é dívida — mas tem de estar no cabeçalho de cada
   notebook, senão lê-se como inconsistência.
2. **A dívida da edição antiga é o Capítulo 4.** P1/P2 vêm do draft antigo
   (`Tese-Vers-o-Draft`, read-only) e **`experiments/p1/results/` não existe**:
   o replay independente nunca foi commitado. Hoje o Cap. 4 **não é
   reproduzível a partir do repositório**. É o achado que responde ao que o
   autor sentiu.
3. **`tab:e3p-sweep` do Cap. 5 está contestada** pela semente 7 canônica —
   detalhe na minha mensagem das 21:30. Maior risco da lista, porque a leitura
   "menos é mais também no transformer" depende do regime.
4. **Sem chaves de API na sessão** — E0, E0-P e E5 não rodam.
5. **Cache do oráculo continua fora do repositório.**

**Ondas propostas**: 0 destravar (autor) · 1 reproduzir E6 e E3′ (começa já,
não depende da Onda 0) · 2 dívida do Cap. 4 (CPU, ~2 h — é aqui que a edição
antiga se resolve) · 3 oráculo (bloqueada, custa dinheiro) · 4 E1/E4 (CPU, ~9 h)
· 5 índice + consolidação multi-semente.

**Começo pela Onda 1 agora**, que não depende de ninguém. Se discordar da
ordem, me corrija que eu troco — mas não fico parado esperando aprovação.

Regra que mantenho em todas: número que não reproduz vira bloqueio a você, com
os dois valores e o artefato de cada um. **Não ajusto número** em nenhuma
direção.
