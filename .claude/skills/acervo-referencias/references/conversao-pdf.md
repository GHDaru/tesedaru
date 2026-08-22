# Estágio 1 — regras de conversão do PDF em markdown

## O que "o PDF todo" quer dizer

O documento convertido tem de permitir que alguém responda uma pergunta sobre
o artigo **sem reabrir o PDF**. Isso inclui o que está desenhado, não só o que
está escrito. Um artigo cujo resultado principal está num gráfico e cuja
conversão diz apenas `[Figura 3]` foi convertido pela metade.

## Estrutura do arquivo gerado

```markdown
---
chave: Xiao2023FreeAL
pdf: pdf/Xiao2023FreeAL.pdf
paginas: 14
convertido_em: 2026-08-22
conversor: pdf2md.py v1 (pymupdf 1.28)
---

<!-- p.1 -->
# FreeAL: Towards Human-Free Active Learning...

texto da página...

<!-- p.7 -->
...

![](figuras/Xiao2023FreeAL/p08-fig01.png)
> **FIG-0801 (p.8)** — Dois gráficos de linha lado a lado, desempenho em
> função de `m` (eixo x: 1, 5, 10, 15, 20). Duas séries em ambos: "Fully
> Supervised ICL" (azul) e "FreeAL" (laranja). Painel esquerdo, SST-2, eixo y
> 95,0–96,2: azul sobe de ≈95,2 a ≈96,2; laranja de ≈95,1 a ≈96,1, cruzando
> acima do azul em m=5 (≈95,65 contra ≈95,57) e ficando abaixo de m=10 a
> m=15. Painel direito, MR, eixo y 91,0–94,0: as duas séries praticamente
> coincidem, de ≈91,6 em m=1 a ≈93,6 em m=20.
```

> O exemplo acima é real: foi lido do PNG exportado por este pipeline a partir
> de `Xiao2023FreeAL.pdf`, p.8. Este é o nível de detalhe esperado — números
> que dá para ler ficam registrados; o que é estimativa vem com `≈`.

Marcas obrigatórias:

- `<!-- p.N -->` no início de **cada** página. É o que torna a evidência
  localizável e o que o portão usa para conferir a contagem.
- Um bloco `> **FIG-NN (p.N)** — ...` por figura, imediatamente após a imagem.
- Tabelas em markdown, com `<!-- TAB-NN (p.N) -->` acima.

## Descrever figura: o que entra e o que não entra

**Entra** — o que está visivelmente no desenho:

- tipo (linha, barra, dispersão, diagrama de blocos, captura de tela);
- o que cada eixo mede e a faixa;
- quais séries existem e como se distinguem;
- valores legíveis: pontos rotulados, extremos, cruzamentos;
- para diagrama: as caixas, as setas e a direção do fluxo.

**Não entra** — o que você conclui:

- "a figura mostra que o método é superior" → isso é claim, vai para a tabela
  de claims no fichamento, com a figura como evidência;
- valor interpolado a olho ("uns 0,85") sem dizer que é aproximado. Se
  estimou, escreva `≈0,85 (lido do gráfico)`.

**Casos especiais**:

| Caso | O que escrever |
|---|---|
| logo, selo, ornamento | `decorativa — sem conteúdo técnico` |
| imagem ilegível/borrada | `ilegível na resolução exportada` — e siga |
| figura que é tabela rasterizada | transcreva como tabela markdown |
| equação exportada como imagem | transcreva em LaTeX entre `$$` |
| foto/exemplo de dado | descreva o que a foto exemplifica |

Nunca escreva `figura omitida`. Se não deu, o motivo fica registrado.

## PDF que é só imagem (sem camada de texto)

O portão 1 mede caracteres por página. Abaixo de ~200, é quase certo que o PDF
é digitalização sem OCR. Nesse caso o portão **falha de propósito**, e a saída
é uma destas, nesta ordem:

1. procurar outra cópia do mesmo trabalho com camada de texto (editora, arXiv);
2. rodar OCR (`ocrmypdf`) e reconverter, registrando no front-matter
   `conversor: pdf2md.py v1 + ocrmypdf`;
3. se nada funcionar, marcar `status: nao-convertivel` com o motivo e avisar o
   `principal`. Documento vazio **não** passa como convertido.

## O que o script faz e o que você faz

| Faz o script | Faz você |
|---|---|
| extrair texto com ordem de leitura | revisar quebras de coluna trocadas |
| marcar páginas | — |
| detectar e converter tabelas | conferir tabela torta contra a página |
| exportar imagens | **descrever cada imagem** |
| contar páginas e caracteres | julgar se o texto ficou legível |

A divisão existe porque a parte automatizável é chata e determinística, e a
parte que exige olhar é justamente a que não dá para automatizar sem mentir.

## Higiene do texto extraído

- Junte palavras quebradas por hífen de fim de linha (`aprendiza-\ndo`).
- Preserve numeração de seção (`4.2`) — é o endereço da evidência.
- Cabeçalho/rodapé repetido em toda página pode sair; **número de página não**.
- Referências bibliográficas do artigo: mantenha. São a matéria-prima das
  arestas `builds_on` do estágio 5.
- Não "melhore" o texto do autor. Conversão é transporte, não edição.
