# Constituição da Tese FALCO (princípios de conteúdo)

> Fonte de verdade dos princípios de CONTEÚDO desta tese. Complementa, sem substituir,
> os princípios do método Maestro (`principles.md`, instalados neste diretório), que
> governam o PROCESSO (spec, gates, reversibilidade). Emendas passam por ADR + bump de
> versão. Todo agente e todo humano DEVE ler este documento antes de editar a tese.
>
> **Versão**: 1.1.0 · **Ratificada**: 2026-08-16 (ADR 0002: I–IV; ADR 0003: V–X) ·
> Princípios I–IV ditados pelo autor; V–X propostos pelo agente e ratificados pelo
> autor no gate de 2026-08-16.

## Princípios ratificados

### I. Siglas abertas (ditado pelo autor)
Toda sigla é "aberta" (expandida) na primeira ocorrência no corpo do texto, com breve
explicação quando necessário, e DEVE constar na lista de siglas
(`0-iniciais/acronimos.tex`). A expansão na lista e a expansão no corpo DEVEM ser
idênticas. Resumo/abstract abrem suas siglas de forma independente do corpo.

### II. Referências validadas contra fichamento (ditado pelo autor)
Toda referência citada DEVE ser validada e checada contra seu fichamento
(`fichamentos/`). Citação sem fichamento correspondente é pendência: ou se ficha a
obra, ou se remove a citação. O fichamento é a evidência de que a obra foi lida e de
que a afirmação atribuída a ela existe nela.

### III. Afirmações fundamentadas (ditado pelo autor)
Toda afirmação DEVE ser fundamentada: justificada por argumento explícito,
referenciada (com citação que a sustente) ou provada com dados/artefatos. Afirmação
órfã — sem argumento, sem fonte e sem dado — não permanece no texto.

### IV. Decisões em ADR (ditado pelo autor)
Toda decisão de processo ou de conteúdo com efeito duradouro é registrada em ADR
imutável (`docs/adr/`) e indexada em `docs/records/decisoes.jsonl` (append-only).
Mudança de posição = novo ADR que supersede o anterior, nunca edição do registro.

## Princípios ratificados no gate de 2026-08-16 (ADR 0003)

### V. Nenhum número sem artefato rastreável
Todo número reportado no texto resolve para um artefato versionado (arquivo de
resultado, log, planilha) nos repositórios da tese. Já praticado desde o início do
programa experimental; este princípio o formaliza.

### VI. Divergência pré-registrado × executado declarada onde ocorre
Quando o desenho executado difere do pré-registrado (orçamento, amostragem,
sementes), a divergência é declarada na primeira menção do resultado afetado, e
achados posteriores à observação dos dados são marcados como *post hoc*.

### VII. Terminologia em camadas
Cada capítulo é legível usando apenas termos já definidos até ali. Jargão
operacional (códigos de experimento E0–E6/E3′, nomes de braços, siglas internas)
só aparece do Capítulo 3 em diante; a introdução fala em linguagem própria.

### VIII. Consistência espelhada
Resumo, abstract e corpo reportam os mesmos números e os mesmos vereditos. Toda
edição que toque um número dispara a checagem dos espelhos.

### IX. DoD de texto verificável
Antes de qualquer merge: a tese compila com 0 erros e 0 referências/citações
indefinidas; siglas do diff checadas contra a lista; números do diff checados
contra artefatos. Verificação por script sempre que possível (transformar
julgamento em checagem).

### X. Estilo humano calibrado
Registro acadêmico formal sem assinatura de máquina (ADR 0001): densidade de
travessões sob controle, sem fórmulas enumerativas repetidas, sem vocabulário
inflado; travessões e ênfases que fazem trabalho real permanecem.
