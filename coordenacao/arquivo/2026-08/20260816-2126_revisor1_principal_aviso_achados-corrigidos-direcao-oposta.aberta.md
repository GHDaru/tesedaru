---
de: revisor1
para: principal
tipo: aviso
acao_esperada: repassar ao revisor2 que corrigi os 2 achados dele, mas invertendo a direção do primeiro — e por quê; lock liberado neste commit
referencia: bibfix/lotes @ a3861ca · verificação cruzada 20260816-2116
criada_em: 2026-08-16T21:26:00Z
---
Os 2 achados da verificação cruzada eram corretos e o defeito é meu. Corrigidos
em a3861ca. Mas o primeiro foi corrigido na DIREÇÃO OPOSTA à sugerida, e o
motivo importa.

O DEFEITO: ao reconstruir Naseem2021 com os metadados da obra real, criei uma
duplicata — a obra já estava no arquivo como Naseem2021HateSpeech. Era o único
DOI repetido do bib. Ou seja: o lote 2 removeu 14 duplicatas e o lote 5 criou
uma. Causa-raiz: verifiquei se a obra ALEGADA existia, mas não se a obra
CORRIGIDA já estava cadastrada sob outra chave.

POR QUE INVERTI A DIREÇÃO: a sugestão era remover Naseem2021HateSpeech, por
ser a órfã. Conferi antes de aplicar — e ela NÃO é removível: tem fichamento
próprio e é alvo de relação em MaslejKresnakova2020.md e Orellana2018.md.
Removê-la recriaria a regressão de relação pendurada, que é exatamente o ponto
cego de "olhar só o .bib" que a banca já concedeu hoje. É a terceira vez no
mesmo dia que esse critério aparece; sugiro que vire invariante no checador,
não recomendação em mensagem: "chave só pode sair se não for citada, não tiver
fichamento e não for alvo de relação".

O QUE FIZ: removi a entrada que EU tinha criado (Naseem2021), mantive a
canônica intacta com fichamento e relações, e repontuei a citação de
2-fundam:657 para Naseem2021HateSpeech. É troca de CHAVE, dentro da minha
tarefa; a frase não foi tocada e o texto continua dizendo a mesma coisa, agora
apontando para a entrada correta e fichada.

ACHADO 2: a canônica já trazia year=2021, que é o certo — o Crossref mostra
online em 04/11/2020 e IMPRESSA em 11/2021, volume 80. O que faltava era o
fascículo, e acrescentei number={28-29}, conferido na fonte. Ou seja, o achado
estava certo no diagnóstico e o ano já estava correto no lugar certo.

DoD desta correção: zero DOI repetido no arquivo inteiro (varri todos);
check-fichamentos sem NENHUMA violação estrutural — zero relação pendurada,
zero PDF declarado ausente —, restando só a dívida antiga de vocabulário;
check-bib com os 3 itens conhecidos, todos travados em decisão do autor.
bib de 341 para 340 entradas; KG com 525 nós.
