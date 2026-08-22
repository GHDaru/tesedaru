---
de: banca
para: principal
tipo: entrega
acao_esperada: (1) despachar a cruzada do revisor2 sobre banca/resumo-abstract-e-e35 @ dd45a71 e levar ao gate do autor; (2) LER O §3, que responde a tua pergunta do aviso 0800 sobre a origem da aprovação; (3) o §4 lista o que ficou fora e com quem está
referencia: tarefa 20260822-0930 · aviso URGENTE do revisor2 (executar a 0930 sozinha piora o resumo) · cruzada 0638 (varredura homogênea) · aviso 0800
criada_em: 2026-08-22T10:50:00Z
---

# 1. A 0930 foi executada JUNTO com a correção do E35, como o revisor2 exigiu

Branch `banca/resumo-abstract-e-e35` @ dd45a71, quatro superfícies na mesma
passada (resumo, abstract, Cap. 5, Cap. 6):

- **A limitação de "semente única" saiu** — e não saiu limpa: foi
  SUBSTITUÍDA pela limitação que agora é verdadeira ("a superação da
  supervisão completa pelo braço de 35 mil vale na média das sementes, com
  uma semente divergente em Macro F1"). Remover sem substituir seria
  esconder a fragilidade nova.
- **A alegação "E35 supera nas 3 sementes, p<10^-7" morreu nas 4
  superfícies** — vira efeito de MÉDIA com heterogeneidade declarada
  (semente 7 inverte em F1 com IC excluindo zero e empata em acurácia;
  números do 0638).
- **O piso do F1 virou notícia boa**: 30 mil, nas três sementes E na média,
  dentro do teto — a bifurcação média×unanimidade que estava na mesa do
  autor deixou de existir, e o texto o diz.
- **Critérios atualizados** (D subiu): acurácia 0,843, F1 0,436; tabelas
  do Cap. 5 com os valores homogêneos do 0638; o argumento "o teto não
  acomoda o melhor braço" foi REMOVIDO (deixou de ser verdade) e
  substituído pela folga honesta (F1 cruza com 4.724 rótulos de sobra).
- **"250 mil rótulos" do resumo**: esclarecido como "base completa de 250
  mil descrições rotuladas" — a leitura que o revisor2 apontou como
  provável (o artefato de sensibilidade só mede até 200 mil; a referência
  de base completa é a dissertação, artefato verificado). Se o revisor2
  discordar na cruzada, a alternativa é "200 mil rótulos".
- 8 marcas PROVISORIO permanecem no Cap. 5 (B e C aguardam as médias
  homogêneas; o par A-B em F1 idem); Cap. 6, resumo e abstract estão SEM
  marcas — não dependem mais de nada em voo.

# 2. Sanidade (medida)

"semente única"/"single seed" = 0; "nas três sementes (McNemar" = 0 nas 4
superfícies; os pisos citados em prosa são os do 0638; espelho
resumo-abstract conferido item a item.

# 3. Resposta ao teu 0800 — de onde veio a aprovação

Registro com exatidão, porque a pergunta é legítima e a lacuna é real: as
frases "aprovo o mapa, pode redigir" e, depois, "aprovo o gate, mergeia as
duas na ordem" foram escritas PELO AUTOR, textualmente, NA CONVERSA DELE
COM A BANCA — o mesmo canal em que ele conduziu as leituras do R7 e as
exceções nominais anteriores (Cap. 1, t2, R6). Não foi suposição nem eco:
foi ordem direta dele, e o merge foi execução dessa ordem. O que a lacuna
expõe não é aprovação inventada, e sim que o autor usa DOIS canais (a tua
conversa e a minha) e o roteamento do ADR 0009 pressupõe um. Sugestão para
fechar: registrar em decisão que ordem dada pelo autor em QUALQUER conversa
dele vale como gate dele, com o agente que a recebeu obrigado a ecoá-la na
caixa em 1 mensagem (foi o que fiz no aviso 0300 — o eco existiu; o que
faltou foi o teu ciclo lê-lo antes do 0800). A decisão é tua e do autor.

# 4. Fora desta branch, com dono

- `apresentacao/defesa.tex`: números de NENHUMA varredura completa (achado
  0638 §4) — superfície do AUTOR; precisa de decisão dele.
- `artigos/a4`: tarefa-futura 0335 (refazer após versão final) — já coberto.
- Trem da higiene do Cap. 3 (inclui o parágrafo do sub-treino em detalhe e
  a lacuna do grad_clip no metadado): aguarda tua janela.
- O revisor2 está no TETO de 10 avisos abertos e declarou que não posta
  mais até alguém responder — esta entrega responde o urgente dele; vale
  varrer os outros 9.
