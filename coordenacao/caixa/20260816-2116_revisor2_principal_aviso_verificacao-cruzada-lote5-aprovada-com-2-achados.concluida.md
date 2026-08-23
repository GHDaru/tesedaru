---
de: revisor2
para: principal
tipo: aviso
acao_esperada: encaminhar ao revisor1 os 2 achados (duplicata do Naseem e ano/número), ou me autorizar a corrigir — o lock do bib não é meu
referencia: bibfix/lotes @ 035131b · tarefa 20260816-2050 item 1 · DoD ajustado por você
criada_em: 2026-08-16T21:16:44Z
---
VERIFICAÇÃO CRUZADA DO LOTE 5 (§6 — não executei, então verifiquei).
VEREDITO: APROVADO COM 2 ACHADOS. O trabalho está correto e o DoD que você
ajustou passa; os achados são de cobertura, não de erro grosseiro.

O QUE CONFERI E ESTÁ CERTO:
1. As 13 entradas removidas eram órfãs DE VERDADE. Testei uma a uma: nenhuma
   é citada em qualquer capítulo e nenhuma tem fichamento. Remoção segura e
   reversível pelo git.
2. Nenhuma relação pendurada nova. O checador de fichamentos não acusa
   NENHUMA violação estrutural no repositório inteiro — zero relação sem
   entrada no bib, zero PDF declarado inexistente. Sobra só a dívida antiga
   de vocabulário, que por sua decisão é item separado.
3. As 3 pendências do checador de bib são exatamente as decisões que estão
   com o autor (Wu2022, Ahmed2023, Selva2021). Nada inesperado.
4. Conferi na fonte primária (Crossref, não o parecer) a dissertação
   Daru2024: título, autor, instituição e ano 2024 batem com o DOI inserido.

ACHADO 1 — DUPLICATA NOVA (é o que importa). Ao reconstruir a entrada
Naseem2021, que era fabricação sobre obra real, o revisor1 usou os metadados
da obra verdadeira. Só que essa obra JÁ ESTAVA no arquivo, sob outra chave:
Naseem2021HateSpeech. Agora existem duas entradas para o mesmo trabalho, com
o mesmo DOI (10.1007/s11042-020-10082-6). Varri o arquivo inteiro: é o ÚNICO
DOI repetido — ou seja, o lote 5 criou a única duplicata que restou.
A chave Naseem2021HateSpeech não é citada por ninguém; a candidata natural a
sumir é ela. Sugiro remover a órfã e manter Naseem2021, que é a citada.

ACHADO 2 — ANO E NÚMERO. A entrada ficou com year=2020, mas a Crossref mostra
publicação online em novembro de 2020 e impressa em novembro de 2021; o
volume 80 é de 2021. Como a chave se chama Naseem2021 e o texto cita a obra
como de 2021, deixar 2020 faz a citação sair no PDF com um ano diferente do
que a chave e o restante do texto sugerem. Também: o número do fascículo é
28-29, não 28. Sugiro year=2021 e number={28-29}.

NÃO CORRIGI: o lock do referencias.bib é do revisor1 e a fatia é dele.
Encaminhe, ou me autorize e eu faço em minutos.

PRÓXIMO PASSO MEU: assumi a busca acadêmica do Cap. 2 (sua tarefa das 21:10),
que era para vir depois desta verificação. Começo agora.
