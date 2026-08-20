---
de: revisor1
para: principal
tipo: aviso
acao_esperada: (1) corrigir 5-resultados-falco/texto.tex:143 — o Song2023 NAO sustenta "menos danoso na mesma taxa"; a frase do RQ3 herda a formulacao condicionada do E4, como voce mesmo previu; (2) Frenay2014 segue pendente de PDF; (3) levar o fichamento no bloco de gate
referencia: tarefa 20260817-0215 · branch claude/maestro-cycles-statistical-analysis-fwla6a @57946a2 · fichamentos/Song2023NoisyLabels.md
criada_em: 2026-08-17T02:48:00Z
---
Voce pediu: "Se o survey NAO sustentar 'menos danoso na mesma taxa', avise o
principal". NAO SUSTENTA. Verificado, com pagina.

## O que a frase da tese diz

5-resultados-falco/texto.tex:143 afirma que o ruido estruturado, concentrado
em pares vizinhos, e "cenario menos danoso ao classificador treinado que ruido
uniforme", citando \citep{Frenay2014,Song2023NoisyLabels}.

## O que o survey diz, nas tres frentes onde a evidencia poderia estar

1. NAO HA comparacao de dano final entre simetrico e assimetrico na mesma
   taxa. As tabelas II e III organizam os 62 metodos por propriedade
   metodologica; nao medem acuracia por tipo de ruido. Ausencia de evidencia
   nessa metrica — o survey nao contradiz, simplesmente nao mede.

2. Na dimensao que ele MEDE — detectabilidade do rotulo errado — diz o
   contrario:
   - VII-A, p. 14: sob ruido assimetrico o desempenho dos metodos robustos
     "could considerably worsen" em relacao ao simetrico, porque as
     distribuicoes de perda de exemplos corretos e incorretos se sobrepoem, e
     "identifying clean examples becomes more challenging".
   - III-E Remark, p. 9: o small-loss trick "does not work well" exatamente
     nesse caso.
   - Figuras 5 e 7: a comparacao e feita NA MESMA TAXA (40%, CIFAR-100). E o
     experimento que a frase precisaria, e ele aponta para o outro lado.

3. A intuicao da frase nao e falsa, e de outra ordem. Trocar uma classe pela
   vizinha semantica preserva mais estrutura e pode custar menos em metrica
   final. So que isso e hipotese sobre o DANO, e o survey fala de DIFICULDADE
   DE DETECCAO. A citacao junta as duas.

## Recomendacao (nao apliquei — prosa e sua)

A frase herda a formulacao condicionada que o Cap. 2 JA usa corretamente nas
linhas 585-590: la o texto diz que o dano do caso do oraculo LLM "nao se deduz
da regra geral — e examinado empiricamente nesta [tese]". Essa e a formulacao
certa, e resolve a contradicao Cap.2:585 x Cap.5:143 sem perder o argumento: a
hipotese do ruido estruturado menos danoso e NOSSA, testada no E4, apoiada nos
nossos dados.

O survey continua citavel no MESMO lugar, com outro papel: para a taxonomia
formal e para o alerta de que a deteccao fica mais dificil. Usado assim, ele
ate fortalece o texto — explica por que o E4 precisou MEDIR o dano em vez de
deduzi-lo.

## Frenay2014 — pendente

E o outro fundamento da mesma frase, esta atras do paywall do IEEE e nao tenho
o PDF (DOI 10.1109/TNNLS.2013.2292894). Enquanto nao chegar, a frase tem uma
das duas fontes verificada e REFUTADA e a outra NAO VERIFICADA. Nao e base
para afirmacao positiva. Se o autor puder subir o PDF pelo agente local, eu
ficho e fecho.

## De quebra: vocabulario formal que faltava a tese

O survey da a matriz de transicao Tij = p(y~=j|y=i) e separa ruido SIMETRICO
(uniforme entre classes), ASSIMETRICO ou dependente de rotulo (o exemplo dele
e "cachorro" confundido com "gato", nao com "peixe") e DEPENDENTE DA
INSTANCIA. O ruido do FALCO e assimetrico nessa taxonomia. Sugiro trocar
"ruido estruturado" por "ruido assimetrico (dependente de rotulo)" no Cap. 5 —
ganha precisao e conecta a tese a literatura formal.

## Ressalva que registrei na propria ficha

E survey de VISAO COMPUTACIONAL: todos os conjuntos sao de imagem, nenhum de
texto, nenhum de rotulo extremo, e o ruido da literatura revista e
majoritariamente sintetico. Transportar para 621 classes de texto curto exige
ressalva explicita — o que, alias, e mais um motivo para a formulacao
condicionada.

## Estado

Branch claude/maestro-cycles-statistical-analysis-fwla6a @57946a2, agora com 3
fichamentos para o mesmo bloco de gate: Rouzegar2024, Fromme2022 e
Song2023NoisyLabels. Mergeei a main na branch antes de commitar (ela estava
atras); conflito unico em kg.html, artefato gerado, resolvido por build_kg.
Grafo: 581 nos, 1153 arestas.
