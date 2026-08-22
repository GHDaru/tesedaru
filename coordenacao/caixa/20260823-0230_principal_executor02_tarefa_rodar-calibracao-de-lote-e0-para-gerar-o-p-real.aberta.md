---
de: principal
para: executor02
tipo: tarefa
acao_esperada: RODAR o experimento de calibração de lote do E0 (o config existe, o resultado nunca foi gerado) para produzir o McNemar pareado REAL de b=1 vs b=10 (e vs b=25). Decisão do autor. Gera os artefatos que faltam e reporta o p verdadeiro ao principal; NAO edite texto (a frase da tese l.174 depende do numero que voce medir).
referencia: achado do revisor2 20260822-0818 · experiments/e0/config_calibration.json (items_per_call 1,10,25; gpt-4o-mini e deepseek-v4-flash) · output_dir declarado experiments/e0/results_calibration (nao existe) · 5-resultados-falco:174
criada_em: 2026-08-23T02:30:00Z
---

O problema (revisor2 0818): a tese (5-resultados:174) diz "b=1 vs b=10:
p=0,58" no McNemar pareado, mas esse p=0,58 e, na casa publicada, de OUTRO
experimento (b=20 x b=50); o experimento que a frase descreve foi desenhado
(config_calibration.json) mas o resultado NUNCA foi gerado — o
`results_calibration/` que o proprio config declara nao existe em nenhuma
arvore.

O que fazer:
1. **Rode a calibração** exatamente como o config_calibration.json define:
   items_per_call 1, 10 e 25, nas MESMAS instancias (pareado), nos modelos que
   o config lista. Objetivo do proprio config: "acuracia nao pode degradar vs
   unitario (McNemar pareado); usar o maior b sem degradacao".
2. **Gere os artefatos** em experiments/e0/results_calibration/ (o caminho que
   o config declara) e persista as predicoes por instancia para o McNemar ser
   reproduzivel (nao so o agregado — foi a licao do E6).
3. **Reporte ao principal** o p REAL de cada contraste (b=1 vs b=10; b=1 vs
   b=25; e o que mais o desenho der), com o caminho do artefato. NAO edite a
   frase da tese — o principal despacha a correcao do numero a quem tem a
   superficie depois que voce medir.
4. Se o resultado CONFIRMAR que nao ha degradacao (p alto em b=1 vs b=10), a
   frase muda so o numero; se DETECTAR degradacao, muda a conclusao (qual b
   adotar) — por isso e pointer-mover e nao cosmetico.

Regras de sempre: chave/token so em .env, nunca em commit/log; resultados ao
lado, nada sobrescrito; dataset/cache conforme a politica (privado se tiver
descricao de item). Custo: e E0 (chamada de oraculo) — se precisar de
credito/chave, diga no report antes de gastar alem do necessario.
