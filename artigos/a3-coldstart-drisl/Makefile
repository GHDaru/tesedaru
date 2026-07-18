all:
	pdflatex -interaction=nonstopmode main.tex >/dev/null
	bibtex main >/dev/null || true
	pdflatex -interaction=nonstopmode main.tex >/dev/null
	pdflatex -interaction=nonstopmode main.tex | tail -2
	@grep -c "LaTeX Error" main.log || true
clean:
	rm -f *.aux *.bbl *.blg *.log *.out
