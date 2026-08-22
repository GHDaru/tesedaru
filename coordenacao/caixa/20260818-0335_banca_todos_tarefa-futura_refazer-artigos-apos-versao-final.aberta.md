---
de: banca
para: todos
tipo: tarefa-futura
acao_esperada: NÃO EXECUTAR AGORA. Tarefa com gatilho: quando a versão final da tese estiver fechada, refazer TODOS os artigos de artigos/ a partir dela. Até lá, ninguém propaga edições da tese para artigos/ nem abre ciclo lá; principal, registrar a decisão em docs/records/decisoes.jsonl (é sua superfície)
referencia: decisão do autor 2026-08-18 ("Não foram submetidos, mas coloque como mensagem futura. Vou refazer todos os artigos quando tivermos a versão final pronta") · dependência levantada no pacote 0320 §3
criada_em: 2026-08-18T03:35:00Z
---

# Decisão do autor: os artigos esperam a tese

Nenhum dos cinco artigos de `artigos/` foi submetido. O autor decidiu
refazê-los TODOS a partir da versão final da tese, em vez de mantê-los
sincronizados edição a edição.

**Consequência operacional imediata:** `artigos/` sai do escopo de todas as
rodadas em curso. Não propagar para lá o reenunciado da hipótese, nem a
régua de tom, nem os expurgos de notação. Achado que envolva artigo vira
item desta lista, não tarefa.

**GATILHO desta tarefa:** versão final da tese fechada (todas as rodadas
concluídas e o depósito autorizado pelo autor).

**Quando disparar, o que já se sabe que precisa entrar em cada artigo:**

1. `a4-falco-framework` (linhas 51, 55, 216 da versão atual): carrega a
   moldura ANTIGA e agora incorreta. Diz "The pre-registered hypothesis
   ($F1 \ge 0.95$ of full-pool supervision at $\le 30\%$ labels) is not
   sustained at 30%" e "is refuted at 30%". Na tese isso deixou de existir:
   o critério é 34.724 rótulos (15% da base), com lastro em Settles (2009) e
   Schröder et al. (2022), e o resultado é sustentado dentro do teto, com o
   piso em 25 mil (10,8% da base) medido com rótulos de gabarito. O artigo
   também precisa perder a expressão "pre-registered" aplicada ao orçamento,
   pelo mesmo motivo que ela saiu da tese: não há registro.
2. `a2-vies-autoavaliacao` (linha 92): menciona parada em 30%, mesma
   correção de denominador.
3. Todos: a régua de estrangeirismos e a de tom valem para os artigos também
   quando forem refeitos; e a notação de experimento segue a decisão de
   nomenclatura vigente na tese naquele momento.
4. Reconferir contra os resultados canônicos daquele momento, que hoje ainda
   se movem (re-coleta E5, curva completa sem critério de parada, sementes
   do executor02).

A banca reabre esta mensagem no fechamento da tese.


## Anexado 2026-08-22 (decisao do autor + sugestao da banca)
- **apresentacao/defesa.tex** entra NESटE mesmo regime: ninguem toca ate a versao final da tese. A atualizacao dos numeros ja esta mapeada (defesa carrega varredura antiga: E20/E35 e A=8.937; alem de 'Quatro pilares P1-P4' nos slides). Executar TUDO neste momento, junto com os artigos.
