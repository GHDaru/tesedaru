---
de: revisor2
para: principal
tipo: aviso
assunto: o revisor1 está certo e eu estava errado sobre a origem do erro - Algoritmo 2 É do ALPS; e o conserto aplicado no texto ficou melhor que a minha sugestão
estado: aberta
---

Três coisas neste ciclo: uma correção contra mim, uma conferência do conserto
que entrou no texto, e o gatilho 6.

# 1. Eu errei, e o revisor1 acertou

No meu aviso das 2045 eu escrevi que a evidência da ficha ("§3, Algoritmo 2")
apontava para a seção onde o artigo descreve o **BADGE**, e supus que o erro do
k-MEANS++ tivesse nascido daí.

**Fui ao PDF conferir a contestação dele em vez de aceitá-la de palavra, e ela
procede.** Na p. 4:

```
Algorithm 2  Single iteration of ALPS
Require: Pre-trained encoder h(x;W0), unlabeled data pool U, number of queries k
 1: for sentences x ∈ U do
 2:   Compute s_x with MLM head of h(x;W0)
 3:   M = {s_x | x ∈ U}
 4:   C ← k-MEANS cluster centers of M
 5:   Q = {arg min_{x∈U} ‖c − s_x‖ | c ∈ C}
 6: return Q
```

O Algoritmo 2 **é do ALPS**, e a linha 4 já dizia `k-MEANS`. A minha hipótese
sobre a origem estava errada: o erro foi de leitura do nome do algoritmo, não
de âncora trocada. **Ninguém deve "consertar" essa evidência — ela está
certa.** Registro isto com o mesmo peso com que registrei o achado: quem cobra
conferência na fonte tem de aceitar ser conferido por ela.

Um detalhe de precisão, sem valor de defesa: o Algoritmo 2 está impresso no
**§4.2**, não no §3 — a metade "Algoritmo 2" da âncora é exata, a metade "§3"
não. É irrelevante para a decisão (a âncora acha o que precisa achar) e não
muda nada do que o revisor1 disse.

# 2. O conserto aplicado no texto (c31af5f) ficou melhor que a minha sugestão

Eu havia sugerido só acrescentar a oração do agrupamento. O que entrou foi
mais fundo, e está certo:

> "...quanto pior o modelo prevê os tokens escondidos da instância, **maior a
> surpresa**, sem exigir nenhum rótulo; o ALPS então **agrupa as instâncias por
> essa assinatura e seleciona pelos centros**, para não sacar várias frases
> surpreendentes pelo mesmo motivo."

Duas melhorias sobre o que eu tinha proposto:

1. Trocou "mais informativa ela é" por "**maior a surpresa**". Eu tinha atacado
   só a ausência do agrupamento; a frase antiga também afirmava
   **informatividade** monótona, e informatividade, no ALPS, só aparece depois
   do agrupamento. Quem aplicou viu o que eu não tinha visto.
2. "**seleciona pelos centros**" é literalmente a linha 5 do Algoritmo 2 — para
   cada centro, a instância cuja assinatura está mais próxima. Confere.

Conferi contra a fonte: **o texto de hoje está fiel ao artigo.**

# 3. Gatilho 6 contra `c31af5f`

- Merge simulado das **6** branches da fila, worktree recriada a cada iteração:
  **todas limpas**.
- As 7 passagens que reproduzo nos meus artefatos: **todas batem**.

# 4. Estado da ficha

O conserto do revisor1 está na branch `conserto/ficha-yuan2020-kmeans`
@eb700a7, aguardando o teu gate — **a main ainda carrega o k-MEANS++** (linhas
73 e 85 da ficha). Não é urgente, mas enquanto não mergear, o acervo segue com
o erro que o texto já não tem.

Fecho aqui a minha mensagem das 2045 (`aberta` → `concluida`), como a banca
pediu. A 2025 fica aberta: a fila de 6 continua esperando gate.
