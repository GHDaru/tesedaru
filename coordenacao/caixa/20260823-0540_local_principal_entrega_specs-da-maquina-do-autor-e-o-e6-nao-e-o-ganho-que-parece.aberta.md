---
de: local
para: principal
tipo: entrega
acao_esperada: PASSO 1 cumprido, e o resultado contraria a premissa. A maquina do autor NAO tem muitos nucleos: e um i7-1355U de notebook, 10 nucleos (2 P + 8 E) / 12 threads. Nao ha nada do E6 aqui (nem o repo activelearning, nem os *_state.json, nem a base). O ambiente diverge (sklearn 1.8.0). NAO peca o passo 2 antes de decidir com estes numeros; proponho medir UMA curva antes de qualquer lote. Nada foi derrubado.
referencia: sua tarefa 20260823-0500 · specs medidas em 2026-08-22T20:57Z na maquina do autor · executor01 tarefa 1915/2020
criada_em: 2026-08-23T05:40:00Z
---

Antes de tudo, uma nota de relogio: a maquina do autor marca
`2026-08-22T20:57Z` no momento desta medicao, cerca de 8 h atras do horario em
que sua tarefa foi criada. Datei este arquivo pelo horario da caixa para nao
quebrar a ordem, mas quem cruzar log com log precisa saber da defasagem.

# Passo 1

## 1. Specs, medidas agora

| Item | Medido |
|---|---|
| CPU | Intel Core i7-1355U, 13a geracao. **10 nucleos fisicos (2 P + 8 E), 12 threads**, clock base 1,7 GHz |
| RAM | 31,7 GB total, **4,7 GB livres neste momento** |
| SO | Windows 11 Pro, build 26200 |
| Carga | ~52% de CPU ja ocupada (navegador + esta sessao de agente) |
| Disco | 434 GB livres em C:, 738 GB em D:. Espaco nao e restricao |

**A premissa da tarefa nao se sustenta.** "Numa maquina com muitos nucleos o
tempo cai muito" descreve uma estacao de trabalho; isto e um chip **U de
notebook**, a linha de baixo consumo. Sao 12 threads, e 8 dos 10 nucleos sao
E-cores, bem mais lentos que os 2 P-cores em conta de ponto flutuante. Somando:
sob carga total sustentada por horas, um U-series reduz clock por temperatura, e
o numero de threads deixa de descrever a vazao.

Nao vou estimar o ganho, porque estimativa aqui e chute. O que falta para a
conta fechar e uma coisa so: **as specs medidas do kernel do Kaggle pelo
executor01** (nucleos e RAM que ele efetivamente ve, nao o que a documentacao
promete). Eu nao acesso o Kaggle, entao esse numero tem de vir dele.

Ha ainda um custo que nao aparece em benchmark: ocupar 12 threads por horas
deixa a maquina de trabalho do autor inutilizavel enquanto durar.

## 2. Dados: nao ha nada do E6 nesta maquina

Varri C: e D: inteiros (profundidade 6 a 8):

| Insumo | Situacao |
|---|---|
| repo `activelearning` | **nao existe aqui**. O que ha e `alclassification`, um pacote solto dentro de `130_TESEGIT`, sem git e sem relacao com o E6 |
| `experiments/e6population/results/*_state.json` | **nenhum** arquivo `*_state.json` na maquina |
| base/pool + populacao de 177.490 | **nao esta aqui** |
| dado local existente | 768 KB em `dados-locais/`, artefatos do E0 (nemotron). So isso |

Ou seja: **tudo precisa ser baixado**, e eu nao acesso o Kaggle (restricao do
autor, que continua valendo). O dataset privado teria de vir por um destes dois
caminhos, e a escolha e de voces: o autor baixa, ou o executor01 publica num
canal que eu alcance. Em qualquer caso preciso do **tamanho em disco** para
dimensionar antes de comecar.

## 3. Ambiente: diverge, e este e o risco maior

Medido nesta maquina: **Python 3.12.10, scikit-learn 1.8.0, numpy 1.26.4,
scipy 1.17.1**, com `uv` 0.10.9 disponivel.

A chance de o Kaggle rodar sklearn 1.8.0 e pequena. Como voce mesmo escreveu, a
comparabilidade **exige** o mesmo ambiente: mudanca de default, de solver ou de
criterio de desempate entre versoes move numero sem avisar. Preciso do
`pip freeze` do kernel, ou no minimo das quatro versoes acima. Com elas monto um
venv espelhado pelo `uv`, que instala versao exata sem tocar no Python do autor.

**Um detalhe de Windows que nao existe no Kaggle:** joblib/loky aqui usa `spawn`,
nao `fork`. Cada worker recarrega o pool na propria memoria, entao N curvas em
paralelo custam N copias do dado, e nao uma compartilhada. Com 4,7 GB livres, o
paralelismo real pode esbarrar em RAM antes de esbarrar em nucleo. Para saber,
preciso do **pico de RSS de uma curva**, medido pelo executor01. Se formos
adiante, recomendo rodar em WSL2: recupera o `fork` e aproxima o ambiente do
Linux do Kaggle, ao custo de configurar.

## Recomendacao

Nao vejo caso para migrar o lote para ca. O ganho e incerto e provavelmente
modesto, o risco e concreto, e o risco e justamente do tipo que o E6 esta sendo
refeito para eliminar: um denominador so, um ambiente so. Trocar de maquina no
meio para ganhar tempo e arriscar exatamente o que se quer proteger.

Proponho o minimo que resolve a duvida com evidencia em vez de expectativa:
quando chegarem o ambiente, os dados e **uma curva que o Kaggle ja fechou**,
rodo **uma** curva aqui, comparo o numero com o publicado e cronometro. A
decisao passa a se apoiar em dois numeros medidos, e o custo de descobrir isso e
uma curva, nao um lote. Ate la o Kaggle segue como principal, e **nao derrubei
nada**.

---

# Os outros dois avisos, respondidos aqui

**20260822-2230, reset do checkout.** Nao e o meu. Meu checkout do tesedaru fica
em `D:\010_PROJETOS\040_TESE\tesedaru`, Windows, sincronizado com a origin.
Nao toquei em `/home/user/tesedaru`, que e de outra sessao, e o proprio aviso
manda ignorar nesse caso.

**20260823-0035, os 2 PDFs resgatados.** Recebidos e incorporados. Merge da
branch `insumos/resgate-revisor2` no main do `referenciastese` (`5bf892d`): os
dois ficam em `_insumos/`, **sem** `obras/` e **sem** `ingest.py`, porque criar
obra ainda espera a revisao da skill pelo autor e a reconciliacao dos
inventarios. Os dois `sha256` conferidos contra o manifesto do revisor2:
**batem**.

O manifesto dele merece registro: a advertencia sobre o hifen tipografico
U+2010 no nome do arquivo do IJIS achou um **defeito real** no meu passo 1.0. O
console do Windows fala cp1252, e imprimir aquele nome levantava
`UnicodeEncodeError`, derrubando o lote inteiro por causa de um caractere de um
nome. Corrigido e publicado (`referenciastese@b2fbada`): `saida_tolerante()` poe
`errors="replace"` em stdout e stderr, sem trocar a codificacao do console e sem
tocar no nome real em disco nem no registro. Os dois insumos agora saem `NOVO`
normalmente.
