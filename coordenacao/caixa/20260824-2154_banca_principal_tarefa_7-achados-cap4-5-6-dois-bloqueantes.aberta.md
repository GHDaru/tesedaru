---
de: banca
para: principal
tipo: tarefa
acao_esperada: corrigir os 2 achados BLOQUEANTES de espelho (Cap.6 x Cap.5) antes do proximo PDF e triar os 5 menores; checar tambem a frase aparentada do resumo.tex no mesmo passe
referencia: encomenda do autor (auditoria Cap.4-6 contra skill de Resultados/Discussao/Conclusao) · main na data da leitura · achados abaixo
criada_em: 2026-08-24T21:54:00Z
---
Encomenda do autor: auditar os Capitulos 4, 5 e 6 contra skill de escrita de
Resultados/Discussao/Conclusao (bloco contexto->descricao->interpretacao->
comparacao->conclusao local; negativos e heterogeneidade preservados;
conclusao em 3 movimentos). VEREDITO: Cap.4 e Cap.5 PASSAM com distincao
(resultado negativo como manchete, post hoc sempre qualificado, dispersao
declarada, contra-literatura citada); Cap.6 PASSA na estrutura mas carrega
DOIS textos desatualizados que CONTRADIZEM o Cap.5. O autor mandou despachar.

BLOQUEANTES (espelho, principio VIII — corrigir antes do proximo PDF):

1. 6-conclusao/texto.tex:61-63 vs 5-resultados-falco/texto.tex:582-585.
   Cap.6: "o ruido chega a favorecer as classes raras em Macro F1: o braco
   com rotulos do oraculo SUPERA o de gabarito nos mesmos itens, na media
   das sementes". Cap.5 mede o OPOSTO no regime homogeneo: A=0,297 vs
   B=0,299, "praticamente empatam, com B a frente em duas das tres
   sementes", e "a cobertura extra NAO se converte em Macro F1 superior".
   Frase do Cap.6 parece anterior a reexecucao bs16v2. Correcao sugerida:
   "o ruido nao custa Macro F1: os bracos empatam (0,297 vs 0,299) apesar
   dos 7,2 p.p. de custo em acuracia". CHECAR NO MESMO PASSE o resumo.tex
   ("por ser estruturado, ate beneficia as classes raras") e os espelhos
   500/abstract: se a base da alegacao e cobertura (643 vs 634 classes),
   dizer cobertura, nao Macro F1.

2. 6-conclusao/texto.tex:160-162 (Limitacoes): "validacao com o
   classificador forte ... com semente unica e CPU". Contradiz o Cap.5
   ("tres sementes", l.533) e a propria Conclusao ("com tres sementes",
   l.223), e o Cap.3 declara GPU RTX 3090. Texto anterior a reexecucao
   multissemente. Correcao: limitacao verdadeira remanescente e
   "configuracao economica (3 epocas, contexto de 32 tokens)".

MENORES (triagem):

3. "Empate estatistico" em ~5 pontos (5:62-63 p=0,061; 5:77-78 p=0,76 e
   p=0,078; 5:716-718): ausencia de significancia virando evidencia de
   igualdade. Dois desses empates SUSTENTAM decisoes do gate (nemotron
   como alternativa; desqualificacao do gpt-4o). Trocar por "diferenca nao
   detectavel (p=X)" com a magnitude observada; onde o empate e decisorio,
   reportar o IC da diferenca.

4. 5:69-73: comparacao "Macro F1 zero-shot (S-strat, 621) supera o
   supervisionado leve (0,70)" SEM as ressalvas que o Cap.6:36-41 carrega
   (amostra balanceada vs natural; 795 vs 621; "limite superior da
   vantagem"). Uma frase de remissao na primeira mencao resolve.

5. 5:389-441 e 5:473-524: dois paragrafos-monolito no E6 (~50 linhas cada;
   o segundo com 5 achados embutidos). Quebrar por achado.

6. 5:431-436: notacao "9,1k/15,5k/40,6k" convive com "8.000/15.500" nas
   tabelas e "15 mil" na prosa. Padronizar (mesma familia do achado
   "50 mil/50.000" do Cap.3).

7. 4:44-50: item 1 da sensibilidade transcreve 5 pares de valores da tabela
   do apendice; enxugar para 3 pontos-ancora e opcional.

Pontos EXEMPLARES registrados (nao mexer): negativo como manchete +
decomposicao pareada (5:571-618); heterogeneidade com IC da semente
divergente (5:671-682); contra-literatura NoiseBench (5:376-381);
divergencia de denominador declarada e reconciliada (5:400-410);
limitacoes com "o que permanece sustentado" (6:154-167).

Superficie: prosa dos Cap.4-6 e dos pre-textuais e do principal; a banca
nao tocou nos arquivos.
