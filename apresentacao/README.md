# Apresentação de defesa — FALCO

`defesa.tex` → dois PDFs, **alvo ~45-50 min** (padrão de doutorado):

- **`defesa.pdf`** — versão limpa para projetar (25 slides: 21 conteúdo + 4 reserva).
- **`defesa-notas.pdf`** — versão com **notas do apresentador** (roteiro de
  fala + tempo por slide), para ensaiar. Gerada com o flag `NOTAS.on`.

## Compilar
```bash
pdflatex defesa.tex ; pdflatex defesa.tex            # limpa
touch NOTAS.on && pdflatex -jobname=defesa-notas defesa.tex \
  ; pdflatex -jobname=defesa-notas defesa.tex ; rm NOTAS.on   # com notas
```

Capa (`capa.png`) = a arte de fundo da tese, no slide-título.
Cores institucionais UFPR (verde). Tempo total das notas ≈ 46 min +
perguntas; ajuste cortando "Objetivos" e "Fundamentação" se a banca fechar 40 min.
