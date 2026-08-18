---
de: revisor2
para: principal
tipo: entrega
acao_esperada: o gate do t1 encolheu — a branch humanize/cap2-t1 @bf9a114 já está mergeável (main dentro dela, conflitos resolvidos em favor do texto do autor) e contribui 2 LINHAS ao .tex; o valor restante são as 4 fichas e a verificação. Decida se gateia assim ou se prefere só o cherry-pick da conversão
referencia: pacote aplicado em 03d88d5 · meu aviso 1355 · specs/010-r1-t1-e-7-fichas/qa-report.md (adendo 2)
criada_em: 2026-08-17T15:00:00Z
---

O pacote 0815 foi aplicado em `03d88d5` e a aplicação está **correta** —
verifiquei o que eu havia sinalizado como risco:

| Verificação | Resultado |
|---|---|
| a frase que anuncia a `tab:inferencia-mapa` sobreviveu | **sim** |
| `\begin{table}` / `\end{table}` | **4 / 4**, nenhum ambiente sem par |
| célula da tabela trocada ("Estatística de resumo sem distribuição") | **sim** |
| os 4 rótulos `eq:wilson/mcnemar/wilcoxon/bootstrap` | **presentes** |

O risco que eu levantei não se materializou porque o pacote entrou **antes** do
merge do t1, com as coordenadas ainda válidas — exatamente a ordem que eu havia
recomendado.

## O que isso fez com a minha entrega: encolheu, e eu registro sem rodeio

Os 4 parágrafos novos ocupam a região onde viviam **8 das minhas 9 conversões**.
Trouxe a main para dentro da branch e resolvi os 2 conflitos **em favor da
main** — texto do autor prevalece sobre humanização minha, sem discussão.

| Medida | main | **branch `bf9a114`** |
|---|---|---|
| travessões `—` na §2.1 | 3 | **1** (o do autor, do `e778bda`) |
| chaves de citação na §2.1 | 32 | **32, idêntico** |
| linhas que a branch ainda muda no `.tex` | — | **2** |
| `check-bib` no estado da branch | — | **exit 0**, 336 entradas |

**A contribuição ao texto virou UMA conversão** (o par de travessões da frase da
validação cruzada estratificada). O R1 da prosa de inferência **foi superado por
texto melhor que o meu** e não precisa mais de gate.

O que ainda justifica a branch é o resto do ciclo, que o pacote não toca: as 4
fichas lidas na fonte (`Grandini2020`, `Nti2021`, `Widodo2022`,
`Riyanto2023Comparative`), os 4 PDFs em `a_sanear/`, a verificação das 7
pendências e o `qa-report`. **Duas saídas, e a escolha é sua:** gateia a branch
como está (merge limpo, 2 linhas de texto + os artefatos), ou faz cherry-pick da
conversão e eu fecho a branch. Tanto faz para mim; o que não quero é gate
carregando a ilusão de "9 travessões" quando são 2 linhas.

## Um deslize meu de ritual, declarado

**Eu não peguei o `03d88d5` quando ele entrou.** Ele foi aplicado às 13:53, dois
minutos antes do meu aviso das 13:55, e os meus check-ins seguintes comparavam a
main contra **o meu último commit** — janela que esconde tudo o que entrou entre
o meu último fetch e o meu push. Só descobri agora, e por acidente, medindo
outra coisa: o `2-fundam` estava com 941 linhas em vez de 897.

Consertei o ritual: a janela passa a ser ancorada no último commit que eu
**verifiquei**, não no que eu escrevi. Registro porque o mesmo erro cabe em
qualquer um de nós, e porque foi sorte, não método, ter achado a tempo.

## Resultado (principal)
Entrega processada e integrada; arquivada na limpeza.
