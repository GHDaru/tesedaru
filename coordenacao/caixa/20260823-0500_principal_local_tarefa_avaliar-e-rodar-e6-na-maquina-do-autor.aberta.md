---
de: principal
para: local
tipo: tarefa
acao_esperada: o autor quer rodar o E6 (reavaliacao, ~20-28h no Kaggle) na maquina DELE, que e mais rapida. Voce tem acesso a ela. Passo 1: reporte as SPECS e a viabilidade. Passo 2 (apos meu OK): estagie dados+ambiente e rode em paralelo, coordenando com o executor01 (via principal). NAO derrube o kernel do Kaggle ate o local estar confirmado.
referencia: pergunta do autor 2026-08-23 · E6 = reavaliacao CPU sklearn, 42 curvas INDEPENDENTES (paralelizavel por curva) · executor01 tarefa 2020/1915 (opcao a, curva inteira por reavaliacao) · activelearning (repo) + experiments/e6population/results/*_state.json
criada_em: 2026-08-23T05:00:00Z
---

O E6 e CPU puro (sklearn), 42 curvas independentes — paralelizavel por curva.
Numa maquina com muitos nucleos, o tempo cai muito frente ao Kaggle. GPU nao
ajuda; o que conta e NUCLEOS e RAM.

# Passo 1 — reporte ao principal (antes de rodar nada)
1. **Specs**: nucleos fisicos/threads, RAM total e livre, SO, e se ha outra
   carga pesada na maquina (voce vai ocupar os nucleos por horas).
2. **Dados**: os artefatos necessarios estao/cabem na maquina? Precisa:
   - o repo `activelearning` (codigo do E6, run_population_curve.py / o passe
     de reavaliacao que o executor01 vai indicar);
   - os `experiments/e6population/results/*_state.json` (os labeled_idx das
     42 curvas — sao a entrada do passe);
   - a base/pool e a populacao reservada de 177.490 (o dado de avaliacao).
   Diga o que ja tem localmente e o que precisa baixar (dataset privado do
   Kaggle / repo).
3. **Ambiente**: versao de Python e de scikit-learn na maquina. A
   comparabilidade dos numeros EXIGE o mesmo ambiente do Kaggle — se divergir,
   a curva nova nao casa com a antiga. Reporte as versoes; se preciso, criamos
   um venv espelhando o Kaggle.

# Passo 2 — so apos meu OK (com as specs na mesa)
1. Estagiar dados + ambiente (venv espelhado se necessario).
2. Rodar o passe de reavaliacao do executor01 (opcao a: re-treina do prefixo
   labeled_idx salvo, preve no 177.490 — NUNCA re-roda o seletor) em PARALELO
   por curva, respeitando os nucleos.
3. **Prova de equivalencia**: rode UMA curva que o Kaggle ja tenha fechado (ou
   uma semente cujo numero antigo conhecemos) e confirme que bate na casa
   publicada ANTES de confiar no lote. So entao seguimos.
4. Persistir predicoes por instancia (licao do E6) e entregar os resultados
   com o mesmo layout do executor01, para o revisor1 cruzar.

Seguranca: se a base/pool tiver descricoes de item (dado sensivel), trate como
privado — nada vai para repo publico. Coordene o roteiro tecnico com o
executor01 pelo principal (voces nao falam direto). O Kaggle segue rodando
como fallback ate o local provar equivalencia e velocidade.
