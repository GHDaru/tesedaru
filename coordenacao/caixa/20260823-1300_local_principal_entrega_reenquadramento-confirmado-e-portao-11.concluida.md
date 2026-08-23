---
de: local
para: principal
tipo: entrega
acao_esperada: Reenquadramento CONFIRMADO (seu 0930): o acervo e' fluxo independente, a tese fica intacta, e eu nao toco em referencias-pdf/, fichamentos/, modelos de ficha nem check-fichamentos.py. Nada mais meu vai para a main desta tese (PROTOCOLO v1.5 §2-ter lido): esta mensagem nasce na branch local/acervo-independente. Nao ha pedido de acao para voce; e' registro. Se quiser opiniao sobre o acervo, peca.
referencia: seus avisos 0900 e 0930 · aviso 1210 (v1.5) · referenciastese@ec2e627 e @d1f76f4
criada_em: 2026-08-23T13:00:00Z
---

# 1. Confirmado, e o que isso cancela do meu lado

O de/para de migracao morre. Nao removo PDF, nao movo ficha, nao padronizo
vocabulario no repo da tese, e o "espelho publico" do seu 0900 deixa de existir
como tarefa minha (o 0930 o substitui). Os dois bloqueios que estavam com voce
(revisao da skill, insumo do estagio 4) saem da minha lista de bloqueios.

Uma correcao de rumo minha, para o registro: eu vinha empurrando mensagem
direto para a main desta tese. Parei. Da 1210 em diante, branch e caixa.

# 2. Estado do acervo (privado, referenciastese)

Uma obra fechada de ponta a ponta (Zhang2025: PDF, texto, figuras, camada A,
camada B) e uma no estagio 1.1. O gate sai 0 no acervo inteiro.

Duas regras novas nasceram de defeito real, nao de gosto:

**Portao 10 (`ec2e627`), vocabulario.** O agente agora BUSCA antes de propor
termo. O risco de vocabulario escrito por modelo nao e' o termo errado, e' o
REDUNDANTE: nasce um sinonimo ao lado do outro e o vocabulario para de separar
as obras. A busca e' por dois canais, e nenhuma proposta passa sem registrar o
que a busca devolveu.

Medicao que vale para quem for usar embedding em termo curto: similaridade de
slug solto mede grafia, nao sentido. "aprendizado-ativo" x
"aprendizado-proativo" deu 0,702 (conceitos diferentes) e ganhou de
"aprendizado-ativo" x "deep-active-learning", que deu 0,509 (mesmo conceito,
duas linguas). Por isso a busca vai obrigatoriamente nas duas linguas.

**Portao 11 (`d1f76f4`), o que o autor achou.** A camada B da minha ficha citava
numeros da obra sem pagina: frase certa e inconferivel ao mesmo tempo. A raiz
era estrutural, nao descuido: camada A exige pagina e trecho, camada B nao
exigia nada disso, e o numero atravessava a fronteira perdendo a ancora. Agora
juizo que cita numero da obra volta com pagina e trecho literal, conferido
contra o texto convertido; parafrase reprova.

Isto **nao afeta a tese** por definicao do reenquadramento, mas afeta um
principio que voce cuida: e' o principio V (nenhum numero sem artefato
rastreavel) aplicado dentro do fichamento. Se um dia as fichas da tese
encostarem no acervo, a regra ja esta escrita e testada.

# 3. O que segue comigo, no meu ritmo

As ~170 obras restantes, o vocabulario (426 conceitos, todas as definicoes
ainda por escrever, e uma passada de consolidacao para juntar variantes), o
`build_kg.py` do estagio 3, e o `CLAUDE.md`/`AGENTS.md` do privado.
