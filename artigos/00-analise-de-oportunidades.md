# Análise de oportunidades de publicação — derivação de artigos da tese

Data: 18/07/2026 · Autor: Gilsiley H. Darú · Orientador: Prof. Gustavo V. Loch
Estado da evidência: E0/E0-P/E1/E4/E5/E6 concluídos; E3′ em execução; ablação
DRI-SL-C concluída.

## 1. Princípios da derivação

1. **Um artigo = uma pergunta**, com fronteira declarada contra os demais
   (anti-*salami slicing*: cada artigo usa um subconjunto disjunto de
   perguntas, ainda que compartilhe a base e a biblioteca).
2. **Publicar antes da defesa fortalece a tese**: capítulo com artigo aceito
   chega à banca pré-validado por pares.
3. **Cada claim com artefato rastreável** — os repositórios `activelearning`
   e `tesedaru` já entregam reprodutibilidade nível *code-available*, um
   diferencial em qualquer submissão.
4. Ordem de submissão dirigida por **maturidade da evidência**, não por
   ambição de veículo.

## 2. Quadro-resumo

| # | Artigo (título de trabalho) | Evidência | Pronto? | Alvo 1º | Alvo 2º | Prioridade |
|---|---|---|---|---|---|---|
| A1 | LLMs como oráculos de rotulagem em 621 categorias: avaliação instrumentada de custo e qualidade em português | E0, E0-P | **sim** | IPM ou ESWA (periódico) | EMNLP/ACL industry track | **1ª** |
| A2 | Autoavaliação enviesada sob amostragem ativa: acurácia subestima, Macro F1 superestima | E6 + ablação | +8 sementes (~1 dia CPU) | ECML-PKDD | IPM / Machine Learning j. | **2ª** |
| A3 | Cold start sem rótulos: DRI-SL vs. envelope evolutivo supervisionado — com auditoria de circularidade | P1, P2, replays | **sim** | BRACIS | Applied Soft Computing | 3ª |
| A4 | FALCO: framework completo com oráculo LLM progressivo (sistema + ciclo real + validação BERTimbau) | tudo + E3′ | após E3′ | ESWA ou ACM TIST | ECIR (industry) | 4ª (síntese) |
| A5 | Recurso: base auditada de 250k descrições de varejo PT + biblioteca | censo de conflitos, lib | sim | PROPOR (recursos) | LREC / Data in Brief | oportunista |

## 3. Análise por artigo

### A1 — O oráculo instrumentado (o mais forte e o mais pronto)

**O que publicar:** o E0 completo com sua instrumentação: 5+ oráculos LLM
avaliados em espaço fechado de 621 categorias de produtos em português;
acurácia com IC de Wilson; McNemar pareado; custo real por mil rótulos com
cache e lote; anatomia do erro (categorias-irmãs e guarda-chuva ≈ metade dos
erros); o efeito do instrumento (RQ4: sem restrição de saída, 6,8% de falsos
erros de fraseado); o achado de *serving* (mesmo modelo, provedores
diferentes, diferença significativa p<0,001); E0-P como ablação de prompt
(faca de dois gumes).

**Por que publicar:** a literatura de LLM-como-anotador opera com dezenas a
~370 classes (Roumeliotis 2025; Gholamian 2024); nenhum estudo conhecido
instrumenta custo com cache/lote nem trata a medição como fotografia
(modelo, provedor, data). A granularidade 621 + português + custo
instrumentado é uma lacuna literal — o artigo ocupa exatamente a célula que
a tabela de lacunas da tese (tab:lacunas) mostra vazia.

**Contribuição declarável:** (i) maior granularidade avaliada em
LLM-anotador para produtos; (ii) protocolo de medição com IC/McNemar/custo
reprodutível; (iii) dois achados de instrumento (enum; serving) que afetam
qualquer avaliação futura; (iv) anatomia de erro acionável (regras de
fronteira).

**Onde:** *Information Processing & Management* (A1 CAPES, escopo perfeito:
IR/NLP aplicado com metodologia) ou *Expert Systems with Applications* (A1,
mais rápido, escopo de sistemas). Conferência alternativa: EMNLP ou ACL
**industry track** (aceita trabalho aplicado com rigor, ciclo mais curto).
Nacional de apoio rápido: STIL/BRACIS se quiser feedback antes do periódico.

**Risco/aponte:** parecerista pode pedir segundo dataset → resposta: réplica
em AlleNoise já desenhada como extensão; ou incluí-la (sobe o custo ~2
semanas de execução, sobe o artigo de patamar).

### A2 — O viés da autoavaliação (o mais original metodologicamente)

**O que publicar:** o desenho interna×externa do E6: pool rotulável vs.
população reservada; a demonstração de que a avaliação nos próprios dados
coletados erra **em direções opostas conforme a métrica** (acurácia
subestima em até 14 p.p.; Macro F1 superestima em até 34 p.p.); o controle
com braço aleatório (Δ≈0) validando o instrumento; o corolário "menos é
mais" (treinar com 15k ativos > 50k completos no SGD, com explicação
mecanística: amostra ativa como currículo balanceado); e a ablação DRI-SL-C
→ estratificação por predição como política trivial e forte.

**Por que publicar:** o viés de amostragem ativa é citado como aviso teórico
desde Settles, mas medições controladas em escala com decomposição por
métrica são raras; o resultado "a direção do viés depende da métrica" é
memorável, prático e imediatamente acionável (não use autoavaliação para
decidir liberação). É o achado da tese com maior potencial de citação fora
do nicho de e-commerce.

**Contribuição declarável:** (i) protocolo pool/população com controle
aleatório; (ii) quantificação bidirecional do viés; (iii) consequência
operacional (conjunto reservado obrigatório + critério de parada); (iv)
estratificação por predição como baseline representativo barato.

**Onde:** ECML-PKDD (casa natural de metodologia de AL empírica) ou
periódico: IPM / *Machine Learning*. Se encurtar: *findings* de EMNLP.

**Pendência antes de submeter:** rodar as 8 sementes (oráculo perfeito,
~1 dia de CPU — sem custo) para converter os achados de descritivos em
inferenciais; sem isso o parecerista de ECML derruba.

### A3 — Cold start sem rótulos (DRI-SL + a auditoria de circularidade)

**O que publicar:** P1 (sensibilidade de L0: 6,4 p.p. em |L0|=100, 47
tamanhos × 30 repetições, replicado ≤0,7 p.p.) + P2 (DRI-SL determinístico
supera o *melhor indivíduo* do AG supervisionado em 100–5.000) + o achado
metodológico da **circularidade** (envelope do AG inflado em até 6,3 p.p.
pela avaliação na partição de aptidão — e o protocolo anticircularidade que
corrige).

**Por que publicar:** duas audiências num artigo: quem trabalha com cold
start em AL (resultado prático) e quem usa metaheurísticas para compor
conjuntos (aviso metodológico de circularidade — generaliza para além de AL).
A ablação DRI-SL-C dá o fecho honesto: no regime contínuo o ganho é
estratificação; no cold start (sem rótulo nenhum) a novidade lexical é o que
existe — a fronteira entre os dois regimes é contribuição em si.

**Onde:** BRACIS (A3/A4 CAPES, comunidade certa, prazo anual) e depois
versão estendida em *Applied Soft Computing* ou *Neurocomputing* (a
comunidade de computação evolutiva precisa ler o resultado de
circularidade).

### A4 — O artigo-síntese do FALCO (o artigo "da tese")

**O que publicar:** o framework completo como sistema: fases com oráculo
progressivo, gate pré-registrado, ciclo real ponta a ponta com oráculo
gratuito (parada por estagnação em 32–40% do orçamento), validação com
classificador forte fora do laço (E3′), política de liberação e drift (A7).
É o artigo que corresponde ao Cap. 3 + Cap. 5 integrados.

**Por que publicar:** é a resposta à barreira apontada por Romberg 2025
(comunidade reclama de viabilidade operacional, não de acurácia): um
pipeline com custo zero de oráculo, critérios de decisão pré-registrados e
código aberto é exatamente o que falta na literatura aplicada.

**Onde:** ESWA ou ACM TIST (sistemas inteligentes aplicados); ECIR industry
como opção de conferência. **Submeter por último** — depende do E3′ e
ganha força se A1/A2 já estiverem aceitos (auto-citação de componentes).

### A5 — Artigo de recurso (oportunista, baixo custo)

Base auditada (censo de conflitos multi-gold, análise de sensibilidade do
gabarito) + biblioteca `activelearning`/FlowBuilder. PROPOR tem trilha de
recursos para português; Data in Brief é rápido. Só vale se a base puder ser
publicada integralmente (verificar restrições de origem dos dados ANTES —
decisão do autor).

## 4. Estratégia e sequência

```
hoje ────────► +1 mês ────────► +3 meses ────────► +6 meses ────► defesa
A1 escrever    A1 submeter      A2 submeter        A3 BRACIS      A4 submeter
(evidência     E6 8 sementes    (ECML ou IPM)      A5 se viável   (síntese,
 pronta)       A2 escrever                                        pós-E3′)
```

- **A1 primeiro**: evidência 100% pronta, lacuna clara, e é o artigo que a
  banca mais gostaria de ver aceito (valida o coração empírico da tese).
- **A2 logo após as 8 sementes**: originalidade metodológica mais alta;
  ECML-PKDD tem *deadline* anual — verificar a janela.
- **A3 no BRACIS** pelo ciclo curto e feedback da comunidade nacional.
- **A4 fecha** consumindo o E3′ e citando os anteriores.

## 5. Fronteiras anti-sobreposição (registrar em cada submissão)

| Par | Fronteira |
|---|---|
| A1×A4 | A1 avalia oráculos isolados (sem laço); A4 usa o vencedor no laço |
| A2×A4 | A2 é sobre MEDIÇÃO (viés); A4 é sobre o SISTEMA (usa a lição: conjunto reservado) |
| A3×A4 | A3 é a Fase 1 isolada com auditoria evolutiva; A4 consome DRI-SL como componente |
| A1×A5 | A5 descreve o recurso; A1 o consome |

## 6. Pendências que destravam artigos

1. E3′ concluir (hoje) → destrava A4.
2. 8 sementes no E6 (~1 dia CPU, custo zero) → destrava A2 no nível ECML.
3. Verificação de publicabilidade integral da base → decide A5.
4. Janelas de submissão (verificar datas correntes): BRACIS, ECML-PKDD,
   PROPOR, EMNLP industry.
5. Definir política de autoria com o orientador (ordem, coautores de
   engenharia se houver).
