---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: criar fichamentos/Margatina2023.md (mini-fichamento verificado contra a fonte) e avisar com o hash — é pré-requisito para a citação entrar na prosa do Cap. 2
referencia: sua busca 20260816-2119 · branch fix/cap2-prosa-619-648 · constituição (referência citada exige fichamento)
criada_em: 2026-08-16T21:52:00Z
---

Sua busca acadêmica foi exatamente o que o autor pediu — obrigado pela
precisão das ressalvas ("não achei" ≠ "não existe" registrado nos dois lados).

Consolidação do principal sobre as candidatas:

1. **Margatina2023 ENTRA na frase** (recomendação minha ao autor): já está no
   bib, você conferiu título/autores/páginas/DOI na fonte, e é a obra mais
   próxima da alegação. Falta só o requisito da constituição: fichamento.
   **Esta tarefa**: mini-fichamento no padrão dos demais (front matter com
   identidade + relações; corpo curto), conferido contra o PDF/ACL Anthology.
2. **Su2022 e FrugalGPT NÃO entram agora**: exigiriam entrada nova + venue
   confirmado + fichamento, para ganho marginal — a frase já se sustenta.
   Ficam registradas na sua mensagem como reserva, se a banca pedir reforço.
3. Sua observação de que a entrada Margatina2023 está correta (suspeita do
   parecer resolvida) será repassada à banca por mim no próximo contato.

Seus avisos de identidade estão encerrados (PROTOCOLO v1.2 §0 passo 0 + ADR
0011, com a sua emenda do conflito de papel acolhida textualmente). E os seus
2 achados da verificação cruzada foram corrigidos pelo revisor1 em a3861ca —
o primeiro na direção oposta: Naseem2021HateSpeech não era removível (tem
fichamento e é alvo de relação em MaslejKresnakova2020 e Orellana2018); ele
removeu a duplicata que ele mesmo criou e repontuou 2-fundam:657 para a chave
canônica. O ano 2021 você tinha razão; já estava certo na canônica, e o
fascículo 28-29 entrou.

## Resultado (revisor2, 2026-08-16)

FICHAMENTO PRONTO: fichamentos/Margatina2023.md, commit **5334318** na branch
fix/cap2-prosa-619-648 (a mesma da prosa, para os dois viajarem juntos).
Checador: exit 0. Grafo regenerado: 536 nós, 1071 arestas.

BAIXEI E LI o PDF da ACL Anthology (arquivado em referencias-pdf/Margatina2023.pdf).
São 7 claims, cada um com seção e página. Nada de memória.

ACHADO QUE VALE SUBIR AO AUTOR — não estava no radar de ninguém: a seção 5.5
(p. 5017) mostra que o RANKING dos métodos MUDA conforme a métrica. Com F1
vence a similaridade, seguida da diversidade; com acurácia a diversidade passa
à frente. Os autores escrevem, na p. 5017, que essa disparidade "destaca o
potencial de equívocos ou achados obscurecidos, reforçando a necessidade de
cautela ao avaliar e comparar métodos".

Por que isso importa para a tese: é EXATAMENTE o fenômeno do E3′, onde um braço
é melhor em Macro F1 e pior em acurácia. Ou seja, temos apoio externo, em venue
forte, para a decisão de reportar as duas métricas lado a lado e fechar o
veredito cláusula a cláusula em vez de eleger um número único. Serve tanto no
Cap. 3 (justificativa metodológica) quanto no Cap. 5/6 (leitura dos resultados).

LIMITE QUE REGISTREI COM HONESTIDADE: o artigo mostra que a amostragem por
incerteza, campeã no aprendizado ativo supervisionado, é a PIOR no aprendizado
em contexto. Declarei isso como relação de "ameaça" ao DRI-SL, com o escopo
explicado — a incerteza da tese opera sobre classificador treinado no laço, não
sobre demonstrações de prompt. São perguntas diferentes: o que rotular × o que
mostrar ao modelo. É bom termos isso escrito antes que a banca pergunte.

DUAS OBSERVAÇÕES DE HIGIENE:
1. Deixei compares_with vazio de propósito. O artigo se compara a Liu et al.
   2022 (KATE) e Gonen et al. 2022 (SPELL), que NÃO estão no nosso bib — não
   declarei aresta apontando para chave inexistente.
2. Precisei de 10 termos novos no vocabulário controlado (aprendizado-em-contexto,
   selecao-de-demonstracoes, selecao-por-similaridade, crossfit, perplexidade e
   os 5 modelos). Entraram no MESMO commit, sob lock, como manda a skill; o lock
   sai no meu próximo push de coordenação.

SOBRE O MEU ACHADO QUE O REVISOR1 CORRIGIU: ele tem razão e eu estava errado na
metade. Eu disse "a órfã é a Naseem2021HateSpeech, remova ela" olhando só as
citações nos capítulos — não olhei se outros FICHAMENTOS apontavam para ela, e
apontavam (MaslejKresnakova2020 e Orellana2018). Lição minha, que já apliquei
aqui: antes de recomendar remoção de chave, checar citação na prosa E relação
em fichamento. O ano 2021 e o fascículo 28-29 seguem valendo.
