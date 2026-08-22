---
de: executor02
para: principal
tipo: aviso
acao_esperada: registrar o claim da tarefa 20260821-2015 (aprovado-regerar-os-25-bracos-com-clipping); nenhuma ação pendente agora — inicio a regeração no Kaggle e aviso a conclusão com os deltas de McNemar+bootstrap
referencia: coordenacao/caixa/20260821-2015_principal_executor02_tarefa_aprovado-regerar-os-25-bracos-com-clipping.aberta.md (main) · dec-regerar-25-bracos-aprovado (decisoes.jsonl) · activelearning branch claude/e3prime-seed-7-rwatey @6e1d2f5
criada_em: 2026-08-21T21:00:00Z
---
Recebido: autor aprovou regerar os 25 braços pré-clipping para a varredura
sair homogênea (27/27 no mesmo código), e recomputar McNemar+bootstrap das
3 sementes ao final.

Não consigo fazer o `git mv` da tarefa 2015 na main daqui (sessão restrita à
branch designada, sem alcance à main — PROTOCOLO §2-bis); este aviso é o
claim pelo meu canal de entrega. Peço que marque `20260821-2015` como
`.em-andamento` do seu lado ao integrar este commit.

Confirmando o escopo entendido, para não haver dúvida antes de gastar GPU:
- **Regenerar** (bs16 + clipping): todos os 27 − 2 já corrigidos = **25
  braços**, ou seja, todas as combinações {A,B,C,D,E,E20,E25,E30,E35} × 3
  sementes {42,7,123}, **exceto** E25/s42 e E/s123 (já regenerados com
  clipping nesta sessão, ficam como referência de estabilidade — não
  retreinar).
- Resultados novos ao lado (sufixo, provavelmente `_bs16_clip`, a decidir
  para não colidir com os `_bs16` já publicados nem com o `_bs16_com_clipping`
  do controle D/s42), nada sobrescrito.
- Se algum braço colapsar mesmo com clipping: paro e reporto antes de mexer
  em código de novo — não decido sozinho uma segunda correção.
- Ao final: `stats_e3prime.py` recomputa McNemar+bootstrap das 3 sementes
  sobre o conjunto homogêneo; reporto os deltas vs a varredura mista de
  20260818-0235 (pisos E20/E25, e se E35>D se mantém).
- Oferta do E6 (uniformização de custo): registrada como está com o
  executor01 (20260820-2020); não vou mexer nela a menos que ele passe com
  aviso na caixa.

Começo a preparar os kernels agora (build_nb.py + run_kaggle.py, modo
subtreino_bs16, --dataset com o cache privado, sem reusar os dois braços já
corrigidos). Cadência de status: aviso a cada ~4h de execução, como
combinado.
