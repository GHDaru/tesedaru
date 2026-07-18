# Tese FALCO — build da tese (aplicável do relatório de escrita científica:
# "scripts auxiliares make build"). Uso: make | make clean | make check
PDF = principal.pdf
TEX = principal.tex

all: build

build:
	pdflatex -interaction=nonstopmode $(TEX)
	bibtex principal
	pdflatex -interaction=nonstopmode $(TEX)
	pdflatex -interaction=nonstopmode $(TEX)
	@echo "--- erros:"; grep -c '^!' principal.log || true
	@echo "--- refs indefinidas:"; grep -ci 'undefined' principal.log || true

check:
	@grep -c '^!' principal.log; grep -ci 'undefined' principal.log; \
	 grep -i 'warning' principal.blg | head -5 || true

clean:
	rm -f *.aux */*.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg *.fls *.fdb_latexmk
