---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR — conserto 1 feito diferente do pedido (motivo abaixo, cross-check com a tarefa 20260817-0020); conserto 2 medido mas NÃO aplicado (superfície da tese, não minha) — despachar a quem edita a4-biblioteca/texto.tex com o caminho certo
referencia: tarefa 20260822-2100 · revisor2 1612 (achados 1 e 6) · activelearning@89dbac3 · tarefa 20260817-0020 (arquivada) · a4-biblioteca/texto.tex:35
criada_em: 2026-08-22T21:45:00Z
---

## 1. Cache que o git apaga — corrigido, mas NÃO como pedido

O pedido oferecia duas opções: exceção no `.gitignore`, ou mover o caminho.
Cheguei a escrever a exceção — e revertida antes de commitar, porque cruzei
com a tarefa `20260817-0020` (a que criou o dataset Kaggle do cache) e ela
já tinha decidido, por um motivo que nem a 2100 nem o achado do revisor2
citam: **"o cache em si também não entra no git ... o conteúdo tem as
descrições do varejo; público só com ordem do autor."** Não é só "é grande
e é dado" — é dado potencialmente sensível. Abrir exceção no `.gitignore`
teria consertado o bug de hoje e criado um risco novo: qualquer `git add .`
distraído passaria a poder subir descrição de item de varejo pro histórico
de um repositório público.

**O que fiz em vez disso**: só documentação. Uma nota em
`REPRODUCIBILITY.md`, logo depois do mapa de reprodução, dizendo (a)
que aquele caminho é ignorado **de propósito**, com o motivo; (b) que foi
assim que o cache original se perdeu em julho, porque ninguém sabia; (c) que
o backup tem que ser o dataset privado do Kaggle, não o git; (d) o caminho
da proveniência da re-coleta atual (`recoleta-20260817/README.md`).
Resolve o mesmo problema — ninguém mais segue a doc sem saber do risco — sem
abrir a exceção que a 0020 tinha fechado por um motivo melhor que o meu.
Commit `activelearning@89dbac3`.

## 2. `run_falco.py` — caminho medido, NÃO corrigido (não é minha superfície)

Medido: `find . -iname run_falco.py` no `activelearning` dá **um** resultado,
`src/activelearning/application/run_falco.py`. É o caminho certo.

O texto errado está em `a4-biblioteca/texto.tex:35`
(`\texttt{application/run\_falco.py}`, faltando o prefixo
`src/activelearning/`) — **prosa da tese**, não código do `activelearning`.
Pela tabela de superfícies do PROTOCOLO (`N-*/texto.tex`, `0-iniciais/`:
dono único principal), não edito. Devolvo o caminho certo para você
despachar a quem tem a superfície:

```
src/activelearning/application/run_falco.py
```

(Os outros seis caminhos do mesmo mapa, linhas 27-35, já estão certos e
seguem a convenção "a partir da raiz" — só este quebra a convenção.)

## Fechamento

Não alcanço a `main`. Peço que marque a 2100 como `.concluida` do seu lado
e despache o conserto 2 a quem edita a a4-biblioteca. Caixa atualizada: esta
é a única mensagem nova desde a entrega da 1800 (18:30). Sem tarefa
pendente depois desta.
