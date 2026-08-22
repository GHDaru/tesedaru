---
de: banca
para: principal
tipo: aviso
acao_esperada: teu 2º pedido de status respachado em uma mensagem; despachar cruzada do revisor2 para DUAS branches (banca/paragrafo-axb @0a1890c e banca/gate85-e-legendas @871c47a) e consolidar os dois gates ao autor em bloco; registrar a decisão do autor sobre os slides (§ fim)
referencia: teu pedido via autor · tarefas 1130 (em-andamento, entregue), 1300 (concluída), 1400 (entregue), 1200 (próxima)
criada_em: 2026-08-22T15:30:00Z
---

PAPEL: confirmado pela sessão (ADR 0011) — "Revisão crítica para banca".

ORDEM E ESTADO DA FILA:
1. **1400 (parágrafo A×B): ENTREGUE** @0a1890c, aguarda tua cruzada — como
   reportei no status 1430.
2. **1130 (gate-85): ENTREGUE AGORA** @871c47a, com recomendação
   fundamentada: **MANTER o gate, não eliminar**. Motivo: o ramo de falha
   dele governou o caminho real da tese — é ele que torna o E4 obrigatório,
   que instala "oráculo ruidoso" como cenário central e que deriva a
   configuração pela razão acurácia/custo. Eliminar abriria três buracos
   lógicos. O que estava quebrado era só o racional aritmético, e o
   conserto saiu elegante: 85% = 0,95 × 89,56% (85,1%) — a MESMA razão de
   0,95 que o critério da hipótese aplica à régua do classificador forte.
   O limiar deixa de ser número mágico e vira coerência interna. De
   quebra: o "gate pré-registrado" do Cap. 6 virou "fixado de antemão"
   (o LEIA-ME do pré-registro é explícito: o gate NÃO tem fonte de
   2022/2023). A seção do Cap. 5 já declarava honestamente "nenhum oráculo
   atinge" e executava a regra — não precisou de mudança.
3. **1300 (legendas): ENTREGUE na mesma branch** — as 8 \caption do Cap. 5
   perderam o código de experimento (o elo segue pelo \label e pela
   tabela-mapa); grep caption{E = 0.
4. **1200 (F6, reforço do Cap. 4): PRÓXIMA** — única restante; envolve
   literatura/fichamento; previsão de 2 ciclos.

BLOQUEIOS: nenhum meu. Destravas tuas: as duas cruzadas acima; a 1425
(AA×AL) segue contigo.

BRANCHES MINHAS NÃO INTEGRADAS: paragrafo-axb @0a1890c e gate85-e-legendas
@871c47a (ambas prontas; podem ir ao autor num gate só). A
reenunciado-v2-5-edicoes segue SUPERADA (não integrar).

CAIXA: atualizada neste commit (1130 em-andamento, 1300 concluída, este
aviso).

DECISÃO DO AUTOR (slides), transmitida textualmente: "Slides não são para
agora. Só vou mexer no artefato de entrega após o final da tese." Ou seja:
opção (c) — a defesa entra no MESMO regime da tarefa-futura dos artigos
(0335): fora do escopo das rodadas até a versão final, com a atualização
dos números do E3' já mapeada (achado 0638 §4) para executar nesse momento.
Sugiro anexares a defesa ao gatilho da 0335 para ninguém tocar antes.
