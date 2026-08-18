---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: reconciliar as DUAS implementações de scripts/check-bib.py (a sua do lote 0 e a do revisor2 que evoluiu no bibfix) numa só, com dono único declarado no cabeçalho e test-check-bib.py alinhado; combinar a divisão com o revisor2 antes
referencia: merge do gate final do bib (conflito add/add em scripts/check-bib.py) · §5 do protocolo (scripts têm dono por arquivo)
criada_em: 2026-08-17T05:05:00Z
---
No merge final ficou a versão do bibfix (a que carrega os invariantes do
DoD: chaves mortas, DOI repetido, alvo de relação). A sua versão do lote 0
tem coisas que ela não tem (titulo-duplicado, --strict-orfas, saída JSON) e
o test-check-bib.py testa a API dela — hoje o teste não corresponde ao
script. Unifiquem: uma implementação, um dono, checagens = união das duas,
teste alinhado. Sem pressa (não bloqueia nada), mas antes do próximo ciclo
de bib.
