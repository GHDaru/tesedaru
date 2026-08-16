#!/usr/bin/env python3
"""Gera o HTML do Painel da Tese FALCO a partir do plano JSON.

Uso (em qualquer sessão):
  python3 scripts/render-plano-revisao.py [saida.html]

Lê docs/records/plano-revisao.json, injeta no template
docs/records/plano-artefato-template.html e grava o HTML pronto para
publicação (padrão: /tmp/painel-tese-falco.html). Depois, publique o HTML
na MESMA URL do artefato (ferramenta Artifact com o parâmetro url) — a URL
vigente fica registrada em docs/records/plano-artefato-url.txt.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
plano_path = ROOT / "docs/records/plano-revisao.json"
template_path = ROOT / "docs/records/plano-artefato-template.html"
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/painel-tese-falco.html")

kpis_path = ROOT / "docs/records/kpis.json"
mens_path = ROOT / "docs/records/mensagens.json"
plano = json.loads(plano_path.read_text(encoding="utf-8"))  # valida o JSON
kpis = json.loads(kpis_path.read_text(encoding="utf-8")) if kpis_path.exists() else {}
mens = json.loads(mens_path.read_text(encoding="utf-8")) if mens_path.exists() else {}
html = template_path.read_text(encoding="utf-8")
for marker, data in (("__PLANO_JSON__", plano), ("__KPIS_JSON__", kpis), ("__MENSAGENS_JSON__", mens)):
    if marker not in html:
        sys.exit(f"template sem o marcador {marker}")
    # </script> dentro de strings do JSON quebraria o bloco; escapa por segurança
    html = html.replace(marker, json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/"))
out.write_text(html, encoding="utf-8")

# página completa da caixa de mensagens (mensagens.html, ao lado da saída)
mtpl = ROOT / "docs/records/mensagens-template.html"
if mtpl.exists():
    mhtml = mtpl.read_text(encoding="utf-8").replace(
        "__MENSAGENS_JSON__",
        json.dumps(mens, ensure_ascii=False, indent=1).replace("</", "<\\/"))
    (out.parent / "mensagens.html").write_text(mhtml, encoding="utf-8")
print(f"ok: {out} + mensagens.html  (plano v{plano['versao']}, PGP {kpis.get('prontidao',{}).get('global_pct','?')}%)")
