---
de: principal
para: banca
tipo: tarefa
acao_esperada: PLANEJAR (não redigir ainda) o mapa de mudanças que os dados finais do executor02 impõem às 4 superfícies de veredito e às seções de resultado — entregar o plano ao principal antes de escrever, para eu conferir contra os quadros do revisor2 e levar o eixo ao autor. Números da varredura de HOJE são a base; os finais trocam pouco após a regeração dos 25 braços (aprovada).
referencia: entrega final do executor02 20260818-0235 · decisões do autor (regime lote16 + regerar 25) · quadros do revisor2 · docs/pre-registro/ (métrica = acurácia)
criada_em: 2026-08-21T21:30:00Z
---

Os dados mudaram — de forma que MELHORA a tese, mas mexe em vários pontos.
Planeje as mudanças antes de escrever; abaixo o que já é firme e o que ainda
oscila.

# O que mudou (firme)

1. **Regime de treino**: a tese passa a reportar **lote 16 corrigido**
   (gradient clipping), avaliação canônica na população de 177.490, 3
   sementes. O lote 128 sub-treinava (D: F1 0,3684 → 0,4508, +22,5%) e isso
   entra como ACHADO metodológico diagnosticado, não nota de rodapé.
2. **Métrica do critério**: ACURÁCIA (pré-registrada na qualificação,
   junho/2023); Macro F1 vira ROBUSTEZ — e agora o F1 TAMBÉM cruza dentro do
   teto, então a seção de robustez ganha tom de reforço, não de ressalva.
3. **Pisos** (varredura de hoje, k=3): F1 cruza em **E25 (25 mil, 10,8% da
   base)**; acurácia cruza em **E20 (20 mil, 8,6%)** — ambos dentro do teto.
4. **E35 > D**: supera o pool inteiro nas 3 sementes com significância forte
   (McNemar p entre 1e-8 e 1e-58). A leitura "menos é mais no transformer"
   volta, mais forte que a original — antes era ponto estimado no regime
   legado; agora é significância pareada no canônico.
5. **B − C** (valor da seleção vs aleatório): positivo e significativo nas 3
   sementes — não troca mais de sinal.
6. **Braço A** (pipeline executado, 11.936 rótulos = 5,2% da base): F1 0,3100
   vs critério 0,4283 — NÃO atinge, gap de 28% (era 57% no lote 128). A
   espinha "critério atingível dentro do teto (varredura com gabarito) vs
   configuração executada que parou cedo" continua.
7. Frase nova que os dados pedem: **A > B em F1** (0,3100 vs 0,2907) — o braço
   com oráculo LLM bate o gabarito nos mesmos itens.

# O que ainda oscila (marque como provisório)

- Os 25 braços pré-clipping SERÃO regerados (aprovado pelo autor). Efeito
  medido em controle: +2,26% relativo em F1 — pequeno, mas os pisos podem
  deslizar na 3ª casa. O E25 cruza o F1 por margem fina (~0,004): NÃO escreva
  frase que quebre se o piso do F1 for para 30 mil.

# O que quero de você (o plano, não o texto)

1. **Inventário de impacto**: liste cada local da tese que cita número desses
   (as 4 superfícies de veredito + `tab:e3p`, `tab:e3p-sweep`, `tab:e6`, a
   prosa das seções E3'/E6, resumo, abstract, Cap.6) e diga, por local, se
   muda VALOR, muda SINAL/CONCLUSÃO, ou só muda o denominador/qualificação.
2. **Ordem de aplicação** que minimize colisão de superfície (o Cap.5 e o
   Cap.6 estão nas suas mãos; o Cap.3 tem tabela recém-consertada — não a
   reabra sem necessidade).
3. **O que fica esperando a regeração** e o que pode ir já (o eixo conceitual
   e as qualificações não dependem dos 25 braços; só os valores finais).
4. Marque cada número provisório com `% PROVISORIO-ate-regeracao` para a troca
   final ser mecânica.

Cruzada do revisor2 nos números (os quadros são dele). Gate do autor no
merge, como sempre. Não redija o veredito ainda — quero ver o plano primeiro.
