# Skill: Construção e Validação de Documentos Científicos

**Propósito**: guia orientativo, em formato de skill consultável, para
construir e validar documentos científicos — destilado da produção real de
uma tese de doutorado, cinco artigos derivados e quatro rodadas de revisão
simulada. Cada regra aqui foi testada contra um erro que aconteceu ou uma
arguição que uma banca/parecerista faria.

**Quando usar**: ao iniciar, reestruturar ou revisar qualquer documento
científico (tese, dissertação, artigo, revisão, resumo). Consultar a seção
do tipo de documento + os princípios transversais + o checklist de
validação correspondente.

---

## 1. Princípios transversais (valem para todo documento)

1. **Nenhum número sem artefato rastreável.** Todo valor reportado deve
   resolver para um arquivo versionado (resultado de experimento, log,
   planilha). Se o artefato não existe, o número não entra — nem "de
   memória", nem estimado sem declarar que é estimativa. *Caso real: um
   draft descreveu a configuração de um algoritmo genético (população,
   crossover) que não constava dos artefatos; a revisão removeu os
   detalhes e remeteu ao repositório.*
2. **Resposta primeiro (Minto/SCQA).** Resumo, abstract, introdução de
   capítulo e conclusão declaram o resultado antes do processo. Um resumo
   que *promete* ("será avaliado...") está errado se o resultado já
   existe; atualize-o a cada resultado novo que mude a história.
3. **Resultado negativo com diagnóstico vale mais que positivo frágil.**
   Se um critério pré-registrado falhar, reporte a falha + a decomposição
   da causa + a distância até o critério. A frase-modelo: "refutada na
   configuração executada, com o gargalo identificado em X; a Y de
   distância do critério". Nunca mova a trave depois do registro.
4. **Declare o estatuto de cada coisa.** Revisão narrativa ≠ revisão
   sistemática; resultado descritivo (semente única) ≠ inferencial;
   comparação exploratória ≠ pré-registrada. Nomear o estatuto desarma o
   parecerista; escondê-lo é o que ele pune.
5. **O instrumento é parte do resultado.** Medições dependem de contrato
   de saída, versão, provedor, data, semente. Registre a proveniência e,
   quando possível, quantifique o efeito do próprio instrumento (um braço
   de controle do instrumento vale uma seção).
6. **Limitação declarada é força; limitação escondida é rejeição.** Toda
   escolha econômica (amostra, sementes, épocas) entra em Limitações com a
   direção do viés que introduz ("a régua pode subir, o que torna o
   critério MAIS exigente — o sentido do veredito se preserva").
7. **Um documento = uma pergunta.** Se há duas perguntas, são dois
   documentos (com fronteira anti-sobreposição declarada entre eles).
8. **Tabela > figura para fatos enumeráveis; figura só quando a forma da
   curva É o achado.** Toda tabela em booktabs, todo símbolo definido,
   toda sigla expandida no primeiro uso.
9. **Decisões com racional registrado.** Tamanhos de amostra, escolha de
   métricas, cortes de desenho: cada um com justificativa escrita no
   próprio documento ou em registro de decisão vinculado.
10. **Compilação/validação contínua.** Nunca acumular texto sem compilar:
    0 erros, 0 referências indefinidas, 0 citações órfãs a cada sessão de
    escrita. Toda chave citada existe no `.bib`; todo PDF de referência é
    fichado antes de ser citado.

---

## 2. Instrumentação estatística mínima (situação → instrumento)

| Situação | Instrumento | Regra de uso |
|---|---|---|
| Precisão de uma proporção (acurácia) | IC de Wilson 95% | sempre que reportar acurácia em n finito; nunca IC normal-aproximado |
| Dois sistemas, mesmas instâncias | McNemar (binomial exato se b+c<25) | pareamento obrigatório; declarar quais comparações são pré-registradas vs. exploratórias |
| Dois sistemas, mesmas sementes/condições | Wilcoxon de postos sinalizados | mínimo 6–8 repetições (menor p = 2/2^n); abaixo disso, declarar descritivo |
| Funcional sem distribuição conhecida | IC bootstrap (percentil) | reportar nº de reamostragens |
| Multiplicidade | hierarquia declarada | pré-registradas poucas; demais exploratórias; nenhum achado central pode depender de p marginal |
| Semente única | estatuto descritivo explícito | ICs sobre a amostra de avaliação seguram comparações; generalização espera repetições |

Regra de ouro: **o teste acompanha o desenho, não o contrário** — se o
desenho não suporta inferência, o texto diz "descritivo" e sobrevive.

---

## 3. Construção por tipo de documento

### 3.1 Tese de doutorado

**Arquitetura**: Introdução (problema → hipótese falseável com critério
quantitativo → objetivos → delimitação) · Fundamentação (argumento em
seções, não enciclopédia) · Metodologia (decisões justificadas +
pré-registro) · Resultados (1+ capítulos) · Discussão/Conclusão ·
Apêndices operacionais.

- **Hipótese**: falseável, com critério numérico e definição prévia do que
  conta como refutação. O gate/critério se fixa ANTES dos dados.
- **Fundamentação**: máximo 2 níveis de numeração; cada seção com função,
  pergunta e mensagem declaradas; todo título abre com texto-ponte; nenhum
  bloco < ~60 palavras; a última seção termina na lacuna que a metodologia
  ocupa (idealmente materializada em tabela trabalhos × dimensões, com o
  próprio trabalho na última linha). *Sintoma de doença: 70 blocos de
  título em 13 mil palavras, 4 níveis — cura: reescrever por função, não
  por tópico.*
- **Metodologia**: seção nunca abre direto em subseção — parágrafo-ponte
  dizendo o que a seção decide e como se divide. Cada constante de projeto
  (tamanhos, limiares, sementes) com racional inline.
- **Resultados**: estilo integrado (número + leitura no mesmo capítulo) é
  válido se uniforme e declarado; a alternativa IMRaD estrita separa — 
  escolher um e manter.
- **Conclusão**: responde a hipótese literalmente (sustentada/refutada +
  números), recapitula por pilar, zero material novo. Trabalhos futuros
  saem DOS DADOS (cada direção ancorada num achado), com a extensão
  prioritária primeiro.
- **Resumo/Abstract**: espelham o estado FINAL da evidência — reescrever a
  cada resultado estrutural novo.

### 3.2 Dissertação de mestrado

Igual à tese com escopo reduzido: uma pergunta, um estudo bem executado.
Diferenças: hipótese pode ser exploratória; fundamentação proporcional
(não exige estado da arte exaustivo); contribuição = evidência sólida, não
necessariamente novidade teórica. Os checklists da §5 aplicam-se
integralmente.

### 3.3 Artigo empírico (avaliação/medição)

**Estrutura**: Introdução (lacuna + RQs numeradas + contribuições em
lista) · Related work (3–4 frentes, cada uma fechando com "o que falta") ·
Dados/tarefa (com auditoria do gabarito, se houver) · Instrumentação ·
Desenho · Resultados por RQ · Discussão (implicações + ameaças) ·
Conclusão · Artefatos.

- Abstract ≤ ~250 palavras, com os 3–5 números-âncora.
- Cada RQ da introdução tem uma subseção de resultados com o mesmo nome.
- Seção de instrumentação separada do desenho: contrato de medição,
  convenção de pontuação (ex.: inválidos contam como erro), método de
  custo, proveniência.
- Confundimentos conhecidos: declarados com a mitigação (ex.: modos de
  instrumento diferentes entre sistemas → reportar taxa de inválidos em
  separado + braço que quantifica o efeito máximo do contrato).

### 3.4 Artigo metodológico (viés/protocolo/instrumento)

Diferencial: o objeto é a MEDIÇÃO, não o sistema. Exige:
- **Braço de controle que valida o instrumento** (a condição em que o
  efeito deve ser zero — e é). Sem controle, o achado é anedota.
- Mecanismo explicado, não só efeito medido ("a amostra ativa infla o
  suporte das classes raras no teste interno" — e não apenas "há viés").
- Seção de guia operacional: o que o praticante deve fazer diferente
  amanhã (é a parte citável).
- Nível inferencial (repetições) antes de submeter a veículo de
  metodologia; descritivo só como draft declarado.

### 3.5 Artigo de sistema/framework

Diferencial: a contribuição é a integração e a disciplina operacional, não
um mecanismo isolado. Exige: figura de arquitetura; execução ponta a ponta
com custos reais; decomposição de perdas por componente (braços pareados);
fronteira explícita com os artigos-componentes (anti-salami); e o teste do
sistema contra critério pré-registrado — inclusive reportando falha com
correção identificada ("o framework converteu uma hipótese falha em
correção de desenho — é o que um framework deve ao seu adotante").

### 3.6 Artigo de recurso (dataset/biblioteca)

Diferencial: "measurement-grade resource, not a raw dump". Exige:
- **Auditoria do próprio gold**: censo de conflitos, protocolo multi-gold,
  sensibilidade das comparações ao ruído do gabarito, teto de medição.
- **Licença explícita** (License=Unknown → rejeição na triagem; CC BY 4.0
  maximiza adoção/citação) + **DOI persistente** + versão/hash declarados
  (se o texto usa versão corrigida, documentar changelog ou nova versão).
- Proveniência por anotação quando houver anotações de modelo (modelo,
  provedor, contrato, lote, temperatura, data).
- Baselines âncora com números artifact-backed para trabalhos futuros
  compararem.
- Ética: declarar ausência de dados pessoais/identificadores.

### 3.7 Revisão de literatura

**Decisão inicial e irreversível: declarar o estatuto.**
- **Narrativa focada**: válida para fundamentar lacuna em tese/artigo;
  declara escopo, período, termos e critérios de confronto (tabela de
  lacunas); NÃO alega exaustividade.
- **Sistemática (PRISMA/Kitchenham)**: exige protocolo prévio registrado,
  fluxo de seleção com contagens, critérios in/ex documentados. **Nunca
  reconstruir contagens a posteriori** para parecer sistemática — é
  fabricação.
- Síntese argumentativa, não inventário: cada frente fecha com a leitura
  comparativa e o que falta; referências descritas uma vez (a seção de
  estado da arte LÊ comparativamente o que a fundamentação descreveu).

### 3.8 Resumo/abstract (de qualquer documento)

Ordem: contexto (1 frase) → o que foi feito (1–2) → números-âncora
(3–5 achados com valores) → veredito/implicação → disponibilidade de
artefatos. Sem siglas não expandidas, sem promessa de resultado que já
existe, sem "paper is organized as follows".

---

## 4. Fluxo de construção (fases com gate de saída)

1. **Especificação** — pergunta, hipótese com critério, desenho, riscos.
   *Gate: outro leitor consegue prever o que contaria como refutação.*
2. **Evidência** — experimentos com artefatos versionados; retomada por
   estado; decisões D-nnn registradas.
   *Gate: todo número planejado tem artefato.*
3. **Esqueleto** — estrutura de seções com função/mensagem declaradas por
   seção (plano aprovado antes de redigir; em tese, aprovar com
   orientador).
   *Gate: o plano responde "cada seção contribui com o quê?".*
4. **Redação** — seção a seção, compilando sempre; citações só de fontes
   fichadas; números importados dos artefatos (nunca digitados de
   memória).
   *Gate: build limpo + inventário de citações preservadas se for
   reescrita.*
5. **Validação** — checklists da §5 + parecer simulado (§6) + correções.
   *Gate: zero majors abertos.*
6. **Fechamento** — resumo/abstract atualizados por último (resposta
   primeiro), veredito consistente em todas as camadas (resumo = conclusão
   = seção de resultados).

---

## 5. Checklists de validação

### 5.1 Universal (qualquer documento)
- [ ] Compila com 0 erros, 0 refs indefinidas, 0 citações órfãs
- [ ] Todo número resolve para artefato versionado
- [ ] Toda comparação declara o teste e o estatuto (pré-reg./exploratória)
- [ ] Acurácias com IC; pareamentos com o teste pareado correto
- [ ] Limitações listam as escolhas econômicas COM direção do viés
- [ ] Nenhuma promessa de coisa já feita; nenhum resultado sem escopo
- [ ] Terminologia uniforme (uma grafia por conceito, ex.: "Macro F1")
- [ ] Tabelas booktabs; figuras citadas no texto; siglas expandidas
- [ ] Impessoalidade/voz consistente com a norma do veículo

### 5.2 Por seção (visão do orientador/parecerista)

| Seção | Passa se... | Pergunta que deve sobreviver |
|---|---|---|
| Introdução | problema + relevância + objetivos + delimitação + hipótese com critério | "O que conta como refutação?" |
| Revisão | estatuto declarado; síntese, não pilha; termina na lacuna | "Cada citação sustenta a frase em que está?" |
| Metodologia | replicável; cada constante com racional; pré-registro visível | "Por que ESTE n / limiar / métrica?" |
| Resultados | números com IC/artefato; convenções de pontuação declaradas | "O que é dado e o que é leitura?" |
| Discussão | confronta literatura; mecanismos, não só efeitos; limitações | "O que muda na prática?" |
| Conclusão | responde a hipótese literalmente; zero material novo | "Os objetivos declarados foram cada um respondidos?" |

### 5.3 Pré-submissão (artigos)
- [ ] Template e limites do veículo; cover letter com fronteiras
      anti-sobreposição se há artigos-irmãos
- [ ] Autoria e ordem acordadas ANTES da submissão
- [ ] Artefatos com DOI; dataset com licença explícita
- [ ] Proofreading nativo/ferramenta na língua do veículo
- [ ] Nenhum \todo/TODO remanescente no PDF

---

## 6. Protocolo de parecer simulado (auto-revisão rigorosa)

Rodar ANTES de considerar qualquer versão "pronta":

1. **Persona**: parecerista cético do veículo-alvo (ou banca), sem acesso
   ao contexto da produção — só ao PDF.
2. **Dimensões com nota** (padrão: originalidade 20%, rigor 25%,
   evidência 25%, coerência 15%, apresentação 15%) — a nota serve para
   localizar o investimento, não para agradar; um avaliador que dá nota
   máxima é inútil por construção.
3. **Caça dirigida aos majors clássicos** (todos ocorreram nesta
   produção): confundimento de instrumento não declarado; multiplicidade
   sem hierarquia; método de um número não descrito (como o custo foi
   medido? como os erros foram categorizados?); detalhe de configuração
   não verificável no artefato; inconsistência numérica entre seções
   (população/classes divergindo entre abstract e corpo); promessa órfã;
   fragmentação estrutural (títulos demais por palavra).
4. **Aplicar as correções imediatamente** e registrar o que foi corrigido
   (o parecer sem aplicação é teatro).
5. Em tese: alternar personas (orientador construtivo / banca arguindo) e
   responder às arguições NO texto ou em registro de decisão.

---

## 7. Catálogo de erros observados (e a correção)

| Erro | Correção aplicada |
|---|---|
| Resumo promete resultado que já existe | reescrever "resposta primeiro" a cada resultado estrutural |
| Detalhe de método inventado de memória | remover e remeter ao artefato; regra: só escrever o que se verificou |
| Denominador errado em taxa (241/9.357 vs 241/6.250) | taxa sempre com numerador E denominador explícitos no texto |
| Números inconsistentes entre documentos-irmãos (621 vs 649 classes) | uma fonte canônica por número; distinção catálogo × visão experimental declarada |
| Título de seção com truque LaTeX que quebra o build (texorpdfstring) | títulos simples; caracteres especiais só no corpo |
| Citações no texto sem entrada no .bib (herdadas de versões antigas) | varredura automática chave-a-chave a cada reescrita |
| Comparar otimizador avaliado na própria partição de aptidão | protocolo anticircularidade: reavaliar SEMPRE em partição intocada |
| Avaliar no próprio conjunto coletado ativamente | população reservada + braço de controle aleatório |
| Critério de parada de um modelo usado para decidir por outro | o proxy de parada deve vir do modelo que importa (ou piso de orçamento) |
| "Grátis" tratado como custo zero | separar custo monetário de custo operacional (vazão, cota) |
| Licença de dado publicado = Unknown | licença explícita antes de qualquer submissão de recurso |

---

## 8. Diferenças-resumo entre documentos

| Aspecto | Tese PhD | Artigo empírico | Artigo metodológico | Artigo de sistema | Artigo de recurso | Revisão sistemática |
|---|---|---|---|---|---|---|
| Pergunta | programa (pilares) | RQs de medição | a medição em si | integração | o dado/ferramenta | o campo |
| Contribuição mínima | avanço + maturidade | números novos instrumentados | protocolo + controle | disciplina operacional ponta a ponta | auditoria + licença + DOI | protocolo + exaustividade |
| Estatística | completa (mapa §2) | IC + pareados | inferencial obrigatório | decomposição por braços | sensibilidade do gold | meta-análise/força de evidência |
| Fracasso aceitável | hipótese refutada com causa | resultado nulo instrumentado | efeito ausente no controle | critério falho + correção | — | lacuna confirmada |
| Tamanho típico | 150–300 pp | 8–14 pp | 6–12 pp | 10–16 pp | 4–8 pp | 15–30 pp |
| Armadilha nº1 | catálogo em vez de argumento | instrumento não declarado | sem braço de controle | salami dos componentes | dump sem auditoria | contagens fabricadas |

---

*Documento vivo: atualizar o catálogo de erros (§7) a cada erro novo
encontrado em produção — é a seção que mais paga.*
