---
de: principal
para: executor02
tipo: tarefa
acao_esperada: DIREÇÃO NOVA DO AUTOR, prioridade máxima: (1) reconstruir o cache do oráculo do zero; (2) refazer a bateria SEM critério de parada (curva completa); (3) incluir a nova geração de modelos a que ele tem acesso — GLM 5.1, GLM 5.2, DeepSeek v4 Pro e DeepSeek v4 Flash. Planeje e reporte ANTES de queimar GPU/créditos
referencia: decisão do autor 2026-08-18 · dec-politica-parada (curva completa, já decidida) · seu claim da re-coleta E5 · aviso 2215 (população divergente)
criada_em: 2026-08-18T01:20:00Z
---

# Reconstrução completa + nova geração de oráculos

O autor decidiu três coisas de uma vez. Leia inteiro antes de começar.

## 1. Cache do oráculo: reconstruir do zero

Nada de recuperar o `annotation_cache_nemotron.jsonl` antigo. A re-coleta que
você já claimou passa a ser a fonte única. Suba como **dataset privado** no
Kaggle (regra de sempre) e registre o hash do arquivo no aviso de conclusão.

## 2. Sem critério de parada: curva completa

Já era decisão registrada (dec-politica-parada) e agora vira execução: rode
a **curva inteira**, sem early stopping. O corte, se houver, é derivado
post-hoc na análise, com a salvaguarda de transparência que o autor definiu.
Isso muda o desenho: não há mais "o laço parou aqui"; há a curva e uma leitura
sobre ela.

## 3. NOVOS ORÁCULOS — e aqui está a oportunidade real

O autor tem acesso agora a: **GLM 5.1, GLM 5.2, DeepSeek v4 Pro, DeepSeek v4
Flash**. Entram no E0 como oráculos candidatos, no mesmo protocolo dos
antigos (S-rand n=1.000, saída restrita ao espaço fechado, IC de Wilson 95%).

**Por que isto importa mais que uma linha a mais na tabela**: nenhum oráculo
da geração anterior atingiu o piso de 85% do gate, e a hipótese acabou testada
em configuração degradada — é a violação de pré-registro que hoje é decisão
pendente do autor. **Se algum destes novos passar do piso, a tese passa a
poder testar a hipótese no regime pré-registrado.** Trate a medição desses
quatro como o item de maior valor da sua fila.

## Antes de queimar recurso: PLANEJE E REPORTE

Quero, em UMA mensagem, antes da execução:
1. ordem de execução e custo estimado (GPU/tokens/créditos) de cada etapa;
2. o que é reaproveitável do que já rodou (as 3 sementes canônicas do E3'
   continuam válidas? o E6?);
3. se a população do E6 (aviso 2215) deve ser alinhada nesta refação — é a
   hora barata de fazer, se for fazer;
4. quanto tempo de parede a bateria inteira leva.

## Segurança (inegociável)

Chaves dos novos provedores **só** em `.env` gitignorado. Nunca em mensagem,
commit, notebook ou log. O repositório é público. Se precisar registrar que
um modelo foi usado, registre o NOME do modelo, jamais a credencial.
