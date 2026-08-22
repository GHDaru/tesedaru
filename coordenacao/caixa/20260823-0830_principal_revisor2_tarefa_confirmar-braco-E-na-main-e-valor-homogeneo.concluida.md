---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: os artefatos JA estao na main do activelearning (rwatey mergeada, 0 so-na-branch — sua checagem foi antes do merge). Remeça o braco E da tab:e3p CONTRA A MAIN: o E/s123 no regime homogeneo existe? Se sim, entregue o valor homogeneo 3-sementes correto (voce ja tinha 0,822/0,351) para a banca trocar a celula (0,816/0,341 -> valor real; 92,0% -> 92,7%) e a legenda "homogeneo/3 sementes" virar verdade. Se NAO existir, sinalize que precisa rodar (executor02, 1 arco).
referencia: seu achado R5 grave (braco E = mistura mal rotulada) · activelearning@main (rwatey mergeada) · tab:e3p Cap.5 · lote-cap5-varredura da banca
criada_em: 2026-08-23T08:30:00Z
---

Novidade que muda sua analise: os 50 artefatos do homogeneo NAO estao so na
rwatey — ela esta 100% mergeada na main (conferi: 0 commits e 0 results
so-na-branch). Entao remeça na MAIN:
1. O e3prime_E_s123 do regime homogeneo existe na main? (procure o arquivo com
   eval_n=177490 e batch_size=16 do braco E semente 123).
2. Se EXISTE: entregue o valor homogeneo 3-sementes do braco E (voce ja tinha
   0,822/0,351) — a banca troca a celula na tab:e3p (de 0,816/0,341, que e
   mistura, para o real) e o "92,0%" vira "92,7%"; a legenda passa a ser
   verdadeira. Vai no lote-cap5-varredura.
3. Se NAO existe (so o misto): entao e 1 arco a rodar (executor02) — sinalize
   e eu despacho; ate la a banca corrige para 2 sementes com legenda honesta.
Pointer-mover, mas a conclusao nao muda de direcao (E segue abaixo da regua).
