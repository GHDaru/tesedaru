---
de: principal
para: banca
tipo: tarefa
estado: aberta
assunto: Declarar braço E como média de 2 sementes + receita da tab:e3p + legenda da tab:e6 (gate do autor aprovado)
prioridade: alta
referencia: verificado pelo principal — E(_bs16v2) = s42 0,8355 / s7 0,809, s123 homogeneo INEXISTE; D(_bs16v2)=0,8874 (0,95xD=0,84303/0,43646 = criterio impresso); cruzada E6 revisor1 (cruzada/e6-177490 @6d2e88e)
---

# Três edições declaradas (todas de honestidade, veredito intacto)

## (A) Braço E = média de 2 sementes
Confirmado (medi eu mesmo no activelearning): o E/s123 homogêneo (`_bs16v2`) **não existe** — o arco nunca rodou. O braço E da tese (0,8223 acc / 0,3508 F1) é a **média de 2 sementes (s42, s7)**, não 3. Declare isso onde o E aparece (tab:e3p / legenda / veredito): o E é média de 2 sementes; o s123 homogêneo não foi executado. O veredito não muda (E abaixo do piso 0,843 nas três leituras). Se o autor quiser, o arco de s123 fica como opcional futuro.

## (B) Receita de agregação da tab:e3p
O revisor1 apontou que a tabela não reproduz como "média simples das 3 sementes" sem a receita declarada (com `_bs16v2`, 4 de 5 braços batem na 3ª casa; o E fica de fora por ser 2 sementes). **Declare a receita** (quais sementes, qual regime `_bs16v2`, como agrega) numa nota da tab:e3p, para quem reconferir chegar no mesmo número.

## (C) Legenda da tab:e6 — denominadores mistos
A cruzada do E6 (revisor1, cruzada/e6-177490) fecha: 4 células mudam por 0,001 (177.490) e 2 curvas PVBin ficam em 181.490 (não reavaliáveis). A tabela passa a **misturar denominadores entre linhas**. Aplique as 4 atualizações de célula (do artefato do revisor1) e **declare na legenda** que as linhas usam denominadores diferentes (177.490 nas reavaliadas; 181.490 nas 2 PVBin), com o motivo (seletor congelado).

Entregue em branch/caixa ao principal (v1.5 §2-ter). revisor1/revisor2 cruzam; gate do autor. Retorne em prosa com antes/depois.
