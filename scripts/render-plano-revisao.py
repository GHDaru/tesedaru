#!/usr/bin/env python3
"""Gera as 4 páginas do site da tese FALCO a partir do plano JSON.

Uso (em qualquer sessão):
  python3 scripts/render-plano-revisao.py [dir-de-saida]

Lê docs/records/plano-revisao.json, kpis.json e mensagens.json e escreve,
no diretório de saída (padrão: /tmp/painel-tese-falco/):
  index.html        Controle    — "o que preciso decidir agora?"
  plano.html         Plano       — "onde está o trabalho e quanto falta?"
  mensagens.html      Coordenação — "o que os agentes estão fazendo?"
  resultados.html     Resultados  — "o que a tese já produziu?" (stub nesta
                       fatia; conteúdo real chega com docs/records/resultados.json,
                       entregue por outro agente — ver tarefa "fatia2" na caixa)

Arquitetura (redesenho de páginas — repasse do principal, 2026-08-16):
- UMA função (`sidebar`) gera a navegação lateral para as 4 páginas — nunca
  copiada por template, para não divergir entre elas.
- UM bloco de CSS (`SHARED_CSS`) e UM bloco de JS (`SHARED_JS`, o
  comportamento da sidebar) são compartilhados pelas 4 páginas — cada HTML
  gerado os contém inline (sem <link>/<script src>: o espelho do painel como
  Artifact roda em sandbox sem rede, e o próprio Pages não deve depender de
  um segundo arquivo estático para não quebrar se for aberto avulso).
- Os antigos `docs/records/plano-artefato-template.html` e
  `mensagens-template.html` (arquitetura de página única) foram retirados:
  o HTML nasce inteiro deste script agora, não de um template com marcador.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/painel-tese-falco")
out_dir.mkdir(parents=True, exist_ok=True)

plano = json.loads((ROOT / "docs/records/plano-revisao.json").read_text(encoding="utf-8"))
kpis_path = ROOT / "docs/records/kpis.json"
mens_path = ROOT / "docs/records/mensagens.json"
resultados_path = ROOT / "docs/records/resultados.json"
referencias_path = ROOT / "docs/records/referencias.json"
kg_path = ROOT / "fichamentos/kg.json"
kpis = json.loads(kpis_path.read_text(encoding="utf-8")) if kpis_path.exists() else {}
mens = json.loads(mens_path.read_text(encoding="utf-8")) if mens_path.exists() else {}
resultados = json.loads(resultados_path.read_text(encoding="utf-8")) if resultados_path.exists() else {}
referencias = json.loads(referencias_path.read_text(encoding="utf-8")) if referencias_path.exists() else {}
kg = json.loads(kg_path.read_text(encoding="utf-8")) if kg_path.exists() else {}


def as_json_script(elem_id: str, data) -> str:
    """JSON injetado como <script type=application/json>, nunca por fetch
    (o espelho como Artifact roda sem rede) — </script> dentro de string do
    JSON quebraria o bloco; escapa por segurança."""
    body = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    return f'<script id="{elem_id}" type="application/json">{body}</script>'


# --------------------------------------------------------------------------
# Sistema de design compartilhado
# --------------------------------------------------------------------------

SHARED_CSS = """
:root{
  /* cor — Fatia 1 (repasse do principal, 16/08/2026): mantém os tokens do
     painel anterior, formalizados com escala tipográfica e de espaço */
  --ground:#FAFAF8; --panel:#FFFFFF; --ink:#20261F; --muted:#68705F;
  --accent:#1E6B3C; --accent-soft:#E7F0E9; --border:#E2E5DF;
  --atencao:#8A5A00; --atencao-bg:#FBF1DC; --atencao-borda:#D9A73E;
  --st-feito:#2E7D4F; --st-feito-bg:#E3F0E7;
  --st-gate:#8A5A00; --st-gate-bg:#FBF1DC;
  --st-andamento:#2B6CB0; --st-andamento-bg:#E4EDF7;
  --st-pendente:#7C8378; --st-pendente-bg:#EFF1EC;
  --st-na:#B6BCB0; --st-na-bg:#F5F6F3;
  --grid:#ECEEE9;
  /* identidade por agente (kanban, ciclo 004b) — 5 matizes que não colidem
     com accent/atencao/st-andamento, que já carregam outro significado */
  --ag-principal:#6E42C1; --ag-banca:#0E7C86; --ag-revisor1:#B15C2E;
  --ag-revisor2:#9C3F76; --ag-autor:#4A4E9E;
  /* tipografia: escala fixa 12/13/15/20/28/44 — nunca tamanho arbitrário */
  --fs-1:12px; --fs-2:13px; --fs-3:15px; --fs-4:20px; --fs-5:28px; --fs-6:44px;
  /* espaço em múltiplos de 4px */
  --sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-5:20px; --sp-6:24px; --sp-7:32px;
  --sidebar-w:220px; --sidebar-w-collapsed:60px;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#131714; --panel:#1B211C; --ink:#E6EAE4; --muted:#9AA294;
    --accent:#6FC492; --accent-soft:#223B2C; --border:#2A302B;
    --atencao:#E8BE6A; --atencao-bg:#33290F; --atencao-borda:#8A6D24;
    --st-feito:#7DCB9B; --st-feito-bg:#1E3327;
    --st-gate:#E8BE6A; --st-gate-bg:#33290F;
    --st-andamento:#7FAEDF; --st-andamento-bg:#1C2C3E;
    --st-pendente:#9AA294; --st-pendente-bg:#232823;
    --st-na:#5C635A; --st-na-bg:#1D221E;
    --grid:#242A25;
    --ag-principal:#B79AF0; --ag-banca:#7FDBE0; --ag-revisor1:#E3A67A;
    --ag-revisor2:#E091C4; --ag-autor:#A7ABE8;
  }
}
:root[data-theme="dark"]{
  --ground:#131714; --panel:#1B211C; --ink:#E6EAE4; --muted:#9AA294;
  --accent:#6FC492; --accent-soft:#223B2C; --border:#2A302B;
  --atencao:#E8BE6A; --atencao-bg:#33290F; --atencao-borda:#8A6D24;
  --st-feito:#7DCB9B; --st-feito-bg:#1E3327;
  --st-gate:#E8BE6A; --st-gate-bg:#33290F;
  --st-andamento:#7FAEDF; --st-andamento-bg:#1C2C3E;
  --st-pendente:#9AA294; --st-pendente-bg:#232823;
  --st-na:#5C635A; --st-na-bg:#1D221E;
  --grid:#242A25;
  --ag-principal:#B79AF0; --ag-banca:#7FDBE0; --ag-revisor1:#E3A67A;
  --ag-revisor2:#E091C4; --ag-autor:#A7ABE8;
}
*{box-sizing:border-box}
html,body{height:100%}
body{background:var(--ground); color:var(--ink); margin:0;
  font:var(--fs-3)/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  font-variant-numeric:tabular-nums}
h1,h2,h3{font-family:Georgia,'Times New Roman',serif; font-weight:600; margin:0}
:focus-visible{outline:2px solid var(--accent); outline-offset:2px}
a{color:var(--accent)}

/* ---- casco: sidebar + conteúdo ---- */
.shell{display:flex; min-height:100vh}
.sidebar{width:var(--sidebar-w); flex:0 0 auto; background:var(--panel);
  border-right:1px solid var(--border); display:flex; flex-direction:column;
  transition:width .15s ease; overflow:hidden}
.shell.collapsed .sidebar{width:var(--sidebar-w-collapsed)}
.sidebar-head{display:flex; align-items:center; justify-content:space-between;
  gap:var(--sp-2); padding:var(--sp-4) var(--sp-3); border-bottom:1px solid var(--border)}
.brand{font-family:Georgia,serif; font-weight:700; font-size:var(--fs-4); color:var(--accent);
  white-space:nowrap; overflow:hidden}
.shell.collapsed .brand{opacity:0; width:0}
.sb-toggle{background:none; border:1px solid var(--border); border-radius:6px;
  width:32px; height:32px; flex:0 0 auto; display:flex; align-items:center; justify-content:center;
  color:var(--muted); cursor:pointer}
.sb-toggle:hover{background:var(--accent-soft); color:var(--accent)}
.sidebar-nav{list-style:none; margin:var(--sp-3) 0; padding:0 var(--sp-2); flex:1}
.sidebar-nav li{margin-bottom:var(--sp-1)}
.sidebar-nav a{display:flex; align-items:center; gap:var(--sp-3); padding:var(--sp-2) var(--sp-3);
  border-radius:6px; text-decoration:none; color:var(--ink); border-left:3px solid transparent;
  white-space:nowrap; overflow:hidden}
.sidebar-nav a:hover{background:var(--accent-soft)}
.sidebar-nav a[aria-current="page"]{background:var(--accent-soft); border-left-color:var(--accent); font-weight:600}
.sidebar-nav .glyph{flex:0 0 auto; width:1.3em; text-align:center; font-size:var(--fs-4); line-height:1}
.sidebar-nav .label{font-size:var(--fs-3)}
.shell.collapsed .sidebar-nav .label{display:none}
.sidebar-footer{padding:var(--sp-3); border-top:1px solid var(--border);
  color:var(--muted); font-size:var(--fs-1); white-space:nowrap; overflow:hidden}
.shell.collapsed .sidebar-footer{opacity:0}
.content{flex:1; min-width:0; padding:var(--sp-6) var(--sp-5) 4rem}
.wrap{max-width:1080px; margin:0 auto; display:flex; flex-direction:column; gap:var(--sp-5)}
.page-head{display:flex; align-items:baseline; gap:var(--sp-4); flex-wrap:wrap}
.page-head h1{font-size:var(--fs-5)}
.page-head .meta{color:var(--muted); font-size:var(--fs-1)}

/* mobile: sidebar vira barra superior + painel deslizante */
.sb-mobile-toggle{display:none}
@media (max-width:767px){
  .shell{flex-direction:column}
  .sidebar{position:fixed; inset:0 auto 0 0; z-index:20; width:78vw; max-width:280px;
    transform:translateX(-100%); transition:transform .18s ease; box-shadow:2px 0 12px rgba(0,0,0,.15)}
  .sidebar.mobile-open{transform:translateX(0)}
  .sidebar-head{padding-top:var(--sp-5)}
  .topbar{display:flex; align-items:center; gap:var(--sp-3); padding:var(--sp-3) var(--sp-4);
    background:var(--panel); border-bottom:1px solid var(--border); position:sticky; top:0; z-index:10}
  .topbar .brand{font-size:var(--fs-4)}
  .sb-mobile-toggle{display:flex; align-items:center; justify-content:center; width:36px; height:36px;
    border:1px solid var(--border); border-radius:6px; background:none; color:var(--ink); cursor:pointer}
  .sb-scrim{display:none; position:fixed; inset:0; background:rgba(0,0,0,.35); z-index:15}
  .sidebar.mobile-open ~ .sb-scrim{display:block}
  .content{padding:var(--sp-5) var(--sp-4) 4rem}
}
@media (min-width:768px){ .topbar{display:none} }

/* ---- componentes ---- */
.label{font-size:var(--fs-1); text-transform:uppercase; letter-spacing:.09em;
  color:var(--muted); font-weight:600}
.card{background:var(--panel); border:1px solid var(--border); border-radius:8px; padding:var(--sp-4) var(--sp-5)}
.card h2{font-size:var(--fs-4); margin:0 0 var(--sp-3)}
.kpis{display:grid; grid-template-columns:minmax(190px,1.4fr) repeat(auto-fit,minmax(140px,1fr)); gap:var(--sp-3)}
.kpi{background:var(--panel); border:1px solid var(--border); border-radius:8px;
  padding:var(--sp-3) var(--sp-4); display:flex; flex-direction:column; gap:var(--sp-1)}
.kpi .v{font-size:var(--fs-4); font-weight:700}
.kpi.hero .v{font-size:var(--fs-6); line-height:1.05; color:var(--accent)}
.kpi .ctx{color:var(--muted); font-size:var(--fs-1)}
.kpi.alerta{border-color:var(--atencao-borda)}
.kpi.alerta .v{color:var(--atencao)}
.progress{background:var(--grid); border-radius:99px; height:8px; overflow:hidden; margin-top:var(--sp-2)}
.progress-bar{background:var(--accent); height:100%; border-radius:99px}
.fila{background:var(--atencao-bg); border:1px solid var(--atencao-borda)}
.fila h2{color:var(--atencao)}
.fila .item{display:flex; gap:var(--sp-3); align-items:baseline; padding:var(--sp-2) 0;
  border-top:1px dashed var(--atencao-borda); font-size:var(--fs-3)}
.fila .item:first-of-type{border-top:none}
.fila .pts{margin-left:auto; white-space:nowrap; font-weight:700; color:var(--atencao)}
.fila .tipo{font-size:var(--fs-1); color:var(--atencao); white-space:nowrap}
.vazia{font-size:var(--fs-3); color:var(--muted)}
.chart-wrap{position:relative}
svg text{fill:var(--muted); font:11px system-ui}
.tip{position:absolute; pointer-events:none; background:var(--panel); border:1px solid var(--border);
  border-radius:6px; padding:.3rem .55rem; font-size:var(--fs-2); display:none; white-space:nowrap;
  box-shadow:0 2px 8px rgba(0,0,0,.12)}
.scroll{overflow-x:auto}
table{border-collapse:collapse; width:100%; font-size:var(--fs-2)}
caption{text-align:left; color:var(--muted); font-size:var(--fs-1); padding-bottom:var(--sp-2)}
th,td{padding:var(--sp-2) var(--sp-2); text-align:left; border-top:1px solid var(--border); vertical-align:middle}
thead th{border-top:none; font-size:var(--fs-1); text-transform:uppercase; letter-spacing:.06em;
  color:var(--muted); white-space:nowrap}
td.chap{white-space:nowrap; font-weight:600}
td.chap small{display:block; font-weight:400; color:var(--muted); font-size:var(--fs-1)}
td.tot{color:var(--muted); font-size:var(--fs-1); white-space:nowrap}
.pill{display:inline-flex; gap:.3rem; align-items:center; padding:.12rem .5rem; border-radius:99px;
  font-size:var(--fs-1); font-weight:600; white-space:nowrap}
.pill.has-note{cursor:help; text-decoration:underline dotted 1px; text-underline-offset:3px}
.feito{color:var(--st-feito); background:var(--st-feito-bg)}
.gate{color:var(--st-gate); background:var(--st-gate-bg); outline:1px solid var(--atencao-borda)}
.andamento{color:var(--st-andamento); background:var(--st-andamento-bg)}
.pendente{color:var(--st-pendente); background:var(--st-pendente-bg)}
.na{color:var(--st-na); background:var(--st-na-bg)}
.rodadas-def{display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:.35rem .9rem;
  margin:0 0 var(--sp-3); padding:var(--sp-3) var(--sp-4); background:var(--ground);
  border:1px solid var(--border); border-radius:6px; font-size:var(--fs-2)}
.rodadas-def b{color:var(--accent)}
.rodadas-def small{color:var(--muted); display:block}
.groups{display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:var(--sp-4)}
.group h3{margin:0 0 var(--sp-2); font-size:var(--fs-3)}
.item{display:flex; gap:var(--sp-3); align-items:baseline; padding:var(--sp-2) 0;
  border-top:1px dashed var(--border); font-size:var(--fs-2)}
.item:first-of-type{border-top:none}
.item .who{color:var(--muted); font-size:var(--fs-1); white-space:nowrap}
.item span.t{flex:1}
details{margin-top:var(--sp-3)}
summary{cursor:pointer; font-size:var(--fs-2); font-weight:600}
.notes{margin:.4rem 0 0; padding-left:1.2rem; font-size:var(--fs-2); color:var(--muted)}
.legend{display:flex; gap:.8rem; flex-wrap:wrap; margin-top:var(--sp-3); align-items:center}
.atalhos{display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:var(--sp-3)}
.atalho{background:var(--panel); border:1px solid var(--border); border-radius:8px;
  padding:var(--sp-4); text-decoration:none; color:var(--ink); display:flex; flex-direction:column; gap:var(--sp-1)}
.atalho:hover{border-color:var(--accent)}
.atalho .n{font-size:var(--fs-5); font-weight:700; color:var(--accent)}
.atalho .l{font-size:var(--fs-2); color:var(--muted)}
@media (prefers-reduced-motion: no-preference){ .kpi.hero .v{transition:color .3s} }
/* identidade por agente: pontinho colorido + nome por extenso ao lado —
   nunca só a cor (mesma régua de estado do site inteiro). Decisão de UX
   (ciclo do kanban): tag pequena, não o elemento inteiro pintado — pintar o
   elemento inteiro competiria com outros sinais de cor já em uso (âmbar de
   "para você"/"atrasado", pills de status). Compartilhado entre páginas
   (Coordenação e Plano) — papel reutilizável, não específico do kanban. */
.k-ag-dot{display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:.35em;
  vertical-align:middle; flex:none}
.k-ag-dot[data-ag="principal"]{background:var(--ag-principal)}
.k-ag-dot[data-ag="banca"]{background:var(--ag-banca)}
.k-ag-dot[data-ag="revisor1"]{background:var(--ag-revisor1)}
.k-ag-dot[data-ag="revisor2"]{background:var(--ag-revisor2)}
.k-ag-dot[data-ag="autor"]{background:var(--ag-autor)}
"""

SHARED_JS = """
(function(){
  var KEY = 'falco.sidebar';
  var shell = document.querySelector('.shell');
  var sidebar = document.querySelector('.sidebar');
  var toggle = document.getElementById('sb-toggle');
  var mobileToggle = document.getElementById('sb-mobile-toggle');
  var isMobile = function(){ return window.matchMedia('(max-width:767px)').matches; };

  function applyDesktop(collapsed){
    shell.classList.toggle('collapsed', collapsed);
    toggle.setAttribute('aria-expanded', String(!collapsed));
    toggle.setAttribute('aria-label', collapsed ? 'Expandir menu' : 'Recolher menu');
  }
  var collapsed = localStorage.getItem(KEY) === '1';
  applyDesktop(collapsed);

  function setMobileOpen(open){
    sidebar.classList.toggle('mobile-open', open);
    if (mobileToggle) mobileToggle.setAttribute('aria-expanded', String(open));
  }

  toggle.addEventListener('click', function(){
    if (isMobile()){
      setMobileOpen(!sidebar.classList.contains('mobile-open'));
    } else {
      collapsed = !collapsed;
      localStorage.setItem(KEY, collapsed ? '1' : '0');
      applyDesktop(collapsed);
    }
  });
  if (mobileToggle){
    mobileToggle.addEventListener('click', function(){
      setMobileOpen(!sidebar.classList.contains('mobile-open'));
    });
  }
  var scrim = document.querySelector('.sb-scrim');
  if (scrim) scrim.addEventListener('click', function(){ setMobileOpen(false); });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') setMobileOpen(false);
  });
})();
"""

NAV = [
    ("index.html", "Controle", "◎"),
    ("plano.html", "Plano", "▤"),
    ("mensagens.html", "Coordenação", "✉"),
    ("resultados.html", "Resultados", "★"),
    ("referencias.html", "Referências", "❐"),
    ("grafo.html", "Grafo", "⬡"),
    ("bibliometria.html", "Bibliometria", "◫"),
]


def sidebar(active_file: str, footer_text: str) -> str:
    """Navegação lateral — função única, usada pelas 4 páginas (nunca copiada
    por template: uma mudança aqui alcança as 4 de uma vez)."""
    rows = []
    for href, label, glyph in NAV:
        is_active = href == active_file
        cls = "active" if is_active else ""
        aria = ' aria-current="page"' if is_active else ""
        rows.append(
            f'    <li><a href="{href}" class="{cls}"{aria}>'
            f'<span class="glyph" aria-hidden="true">{glyph}</span>'
            f'<span class="label">{label}</span></a></li>'
        )
    items = "\n".join(rows)
    return f"""<nav class="sidebar" aria-label="Navegação principal">
  <div class="sidebar-head">
    <span class="brand">FALCO</span>
    <button id="sb-toggle" class="sb-toggle" type="button" aria-expanded="true" aria-label="Recolher menu" title="Recolher menu">
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M10 2 L5 8 L10 14" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </button>
  </div>
  <ul class="sidebar-nav">
{items}
  </ul>
  <div class="sidebar-footer">{footer_text}</div>
</nav>
<div class="sb-scrim"></div>"""


def page_shell(title: str, active_file: str, footer_text: str, body_html: str, page_script: str = "") -> str:
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Tese FALCO</title>
<style>{SHARED_CSS}</style>
</head><body>
<div class="topbar">
  <button id="sb-mobile-toggle" class="sb-mobile-toggle" type="button" aria-expanded="false" aria-label="Abrir menu" aria-controls="sb-toggle">☰</button>
  <span class="brand">FALCO</span>
</div>
<div class="shell">
{sidebar(active_file, footer_text)}
  <main class="content">
    <div class="wrap">
{body_html}
    </div>
  </main>
</div>
<script>{SHARED_JS}</script>
{page_script}
</body></html>
"""


# --------------------------------------------------------------------------
# Meta comum (rodapé da sidebar, todas as páginas)
# --------------------------------------------------------------------------
FOOTER_TEXT = f"atualizado em {kpis.get('computado_em', '—')} · plano v{plano.get('versao', '—')}"


# --------------------------------------------------------------------------
# Controle (index.html) — "o que preciso decidir agora?"
# --------------------------------------------------------------------------
def build_controle() -> tuple[str, str]:
    pr = kpis.get("prontidao", {})
    msgs_ativas = sum(1 for m in mens.get("mensagens", []) if m.get("estado") != "concluida")
    body = f"""
<header class="page-head"><h1>Controle</h1>
  <span class="meta" id="meta"></span></header>

<section class="card kpi hero" aria-label="Prontidão global">
  <span class="label">Prontidão global da tese</span>
  <span class="v">{pr.get('global_pct', '—')}%</span>
  <div class="progress" role="progressbar" aria-valuenow="{pr.get('global_pct', 0)}" aria-valuemin="0" aria-valuemax="100" aria-label="Prontidão global">
    <div class="progress-bar" style="width:{pr.get('global_pct', 0)}%"></div>
  </div>
  <span class="ctx" id="hero-ctx"></span>
</section>

<section class="card fila" id="fila-card">
  <h2 id="fila-titulo">🔒 Aguardando você</h2>
  <div id="fila"></div>
</section>

<section class="card">
  <span class="label">Próximo passo do agente</span>
  <p id="proximo-desc" style="margin:.4rem 0 0; font-size:var(--fs-3)"></p>
</section>

<section aria-label="Atalhos">
  <div class="atalhos">
    <a class="atalho" href="plano.html"><span class="n">{pr.get('global_pct', '—')}%</span><span class="l">Plano — onde está o trabalho</span></a>
    <a class="atalho" href="mensagens.html"><span class="n">{msgs_ativas}</span><span class="l">Coordenação — mensagens ativas</span></a>
    <a class="atalho" href="resultados.html"><span class="n">—</span><span class="l">Resultados — chega na próxima entrega</span></a>
  </div>
</section>
"""
    # blocos JSON como <script type=application/json> IRMÃOS do <script> de
    # lógica, nunca aninhados: um <script> executável termina no primeiro
    # "</script" literal que aparece nele, então um <script> aninhado dentro
    # fecharia o de fora cedo e quebraria o parsing (o HTML volta a modo
    # normal no meio da lógica JS, que passa a ser tratada como texto/markup).
    json_blocks = (
        as_json_script('kpis', kpis) + "\n"
        + as_json_script('mensagens', mens) + "\n"
        + as_json_script('plano', {'proximo': plano.get('proximo')})
    )
    script = json_blocks + f"""
<script>
(function(){{
  const K = JSON.parse(document.getElementById('kpis').textContent);
  const M = JSON.parse(document.getElementById('mensagens').textContent || '{{}}');
  const P = JSON.parse(document.getElementById('plano').textContent);
  const el = id => document.getElementById(id);
  const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
  const pr = K.prontidao, rt = K.ritmo;
  const serie = rt.serie || [];
  const delta = serie.length >= 2
    ? (() => {{ const d = (serie.at(-1).pct - serie[0].pct).toFixed(1);
               return `${{d >= 0 ? '▲ +' : '▼ '}}${{d}} p.p. desde ${{serie[0].data}}`; }})()
    : 'primeira medição';
  el('hero-ctx').textContent = `${{delta}} · ${{pr.pontos_feitos}}/${{pr.pontos_totais}} pontos de esforço`;
  el('meta').textContent = `KPIs de ${{K.computado_em}} (${{K.git_sha}})`;

  const GLIFO_MSG = {{aberta:'○', 'em-andamento':'◐', concluida:'●'}};
  const msgs = (M.mensagens || []);
  const msgsAutor = msgs.filter(m => m.para === 'autor' && m.estado !== 'concluida' && m.tipo !== 'aviso');
  const fila = (K.fila_autor.itens || []).concat(msgsAutor.map(m => ({{
    id: m.arquivo, tipo: 'mensagem',
    titulo: `${{GLIFO_MSG[m.estado]}} ${{m.acao_esperada || m.slug}} · de ${{m.de}} · há ${{m.idade_horas}}h${{m.prazo ? ' · prazo ' + m.prazo.slice(0,10) : ''}}`,
    pontos_destravados: 0}})));
  const doente = (M.saude || {{}}).bloqueio_mais_antigo_h > 48 || (M.saude || {{}}).locks_vencidos > 0;
  if (doente) fila.push({{id:'saude', tipo:'processo',
    titulo:'Processo de coordenação doente: destravar bloqueio/lock vencido (ver página Coordenação)',
    pontos_destravados: 0}});
  el('fila-titulo').textContent = fila.length
    ? `🔒 Aguardando você — ${{fila.length}} ${{fila.length === 1 ? 'item' : 'itens'}}`
    : 'Nada espera você';
  el('fila').innerHTML = fila.length ? fila.map(f => `
    <div class="item"><span class="tipo">${{({{gate:'GATE', execucao:'RODAR', acao:'AÇÃO', decisao:'DECISÃO', mensagem:'MSG', processo:'SAÚDE'}})[f.tipo] || f.tipo}}</span>
      <span class="t">${{esc(f.titulo)}}</span>
      <span class="pts">${{f.pontos_destravados ? '+' + f.pontos_destravados + ' pts' : ''}}</span></div>`).join('')
    : `<p class="vazia">O agente segue no próximo passo abaixo. ✓</p>`;

  el('proximo-desc').textContent = (P.proximo && P.proximo.descricao) || 'indefinido — definir no ritual';
}})();
</script>"""
    return body, script


# --------------------------------------------------------------------------
# Plano (plano.html) — "onde está o trabalho e quanto falta?"
# --------------------------------------------------------------------------
def build_plano() -> tuple[str, str]:
    body = """
<header class="page-head"><h1>Plano</h1>
  <span class="meta" id="meta"></span></header>

<section class="kpis" id="kpis-row" aria-label="Indicadores"></section>

<section class="card">
  <h2>Evolução da prontidão</h2>
  <div class="chart-wrap" id="chart-wrap"></div>
  <details><summary>Dados da série</summary>
    <div class="scroll"><table id="serie-tab"></table></div>
  </details>
</section>

<section class="card">
  <h2>Capítulos × rodadas</h2>
  <div class="rodadas-def" id="rodadas-def"></div>
  <div class="scroll"><table id="matriz">
    <caption>✓ feito · 🔒 em gate (espera você) · ◐ andamento · ○ pendente · – não se aplica · ⛓ bloqueado</caption>
  </table></div>
  <div id="aberturas"></div>
</section>

<section class="card" id="quebra-card">
  <h2>Quebra por tema</h2>
  <p class="vazia">Capítulos grandes demais para uma rodada só viram frentes
  menores — cada tema segue sua própria sequência R3→R4→R1 antes de entrar
  na reescrita do capítulo inteiro.</p>
  <div id="quebras"></div>
</section>

<section class="card">
  <details><summary>Execuções fora do texto</summary>
    <div id="exec"></div>
  </details>
</section>

<section class="card">
  <details open><summary>Artefatos e pendências</summary>
    <div class="groups" id="grupos" style="margin-top:.6rem"></div>
  </details>
</section>

<footer class="card">
  <details><summary>Ritual e legenda</summary>
    <ol id="ritual"></ol>
    <div class="legend" id="legenda"></div>
    <p id="meta-saida"></p>
  </details>
</footer>
"""
    json_blocks = as_json_script('plano', plano) + "\n" + as_json_script('kpis', kpis)
    script = json_blocks + f"""
<script>
(function(){{
  const P = JSON.parse(document.getElementById('plano').textContent);
  const K = JSON.parse(document.getElementById('kpis').textContent);
  const el = id => document.getElementById(id);
  const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');

  el('meta').textContent = `plano v${{P.versao}} · KPIs de ${{K.computado_em}} (${{K.git_sha}}) · fonte: docs/records/`;

  const pr = K.prontidao, rt = K.ritmo, dv = K.divida_fundamentacao;
  const serie = rt.serie || [];
  const delta = serie.length >= 2
    ? (() => {{ const d = (serie.at(-1).pct - serie[0].pct).toFixed(1);
               return `${{d >= 0 ? '▲ +' : '▼ '}}${{d}} p.p. desde ${{serie[0].data}}`; }})()
    : 'primeira medição';
  const vel = rt.velocidade_pontos_semana;
  el('kpis-row').innerHTML = `
    <div class="kpi hero"><span class="label">Prontidão global</span>
      <span class="v">${{pr.global_pct}}%</span>
      <span class="ctx">${{delta}} · ${{pr.pontos_feitos}}/${{pr.pontos_totais}} pontos de esforço</span></div>
    <div class="kpi"><span class="label">Velocidade</span>
      <span class="v">${{vel ?? '—'}}</span>
      <span class="ctx">${{vel != null ? 'pontos/semana (janela ' + rt.janela_dias + 'd)' : 'primeira medição'}}</span></div>
    <div class="kpi"><span class="label">ETA</span>
      <span class="v">${{rt.eta_confiavel ? rt.eta_semanas + ' sem' : '—'}}</span>
      <span class="ctx">${{rt.eta_confiavel ? 'projeção: ' + rt.eta_data : 'indeterminado (sem ritmo medível)'}}</span></div>
    <div class="kpi alerta"><span class="label">Aguardando você</span>
      <span class="v">${{K.fila_autor.total}}</span>
      <span class="ctx">itens que só o autor destrava</span></div>
    <div class="kpi"><span class="label">Maior destrava</span>
      <span class="v">${{K.represados.pontos}}</span>
      <span class="ctx">pontos represados atrás de 1 ação sua</span></div>
    <div class="kpi"><span class="label">Dívida de fundamentação</span>
      <span class="v">${{dv.citacoes_pendentes}}</span>
      <span class="ctx">citações a validar · ${{dv.chaves_sem_fichamento}} sem fichamento</span></div>`;

  (function chart(){{
    const wrap = el('chart-wrap');
    const W = 980, H = 240, mL = 34, mR = 12, mT = 10, mB = 26;
    if (serie.length < 3){{
      wrap.innerHTML = `<p class="vazia">Histórico insuficiente para tendência
        (${{serie.length}} ${{serie.length === 1 ? 'medição' : 'medições'}}). O gráfico nasce com a terceira.</p>`;
      return;
    }}
    const t0 = new Date(serie[0].data).getTime(), t1 = new Date(serie.at(-1).data).getTime();
    const X = d => mL + (W - mL - mR) * ((new Date(d).getTime() - t0) / Math.max(1, t1 - t0));
    const Y = pct => mT + (H - mT - mB) * (1 - pct / 100);
    const pts = serie.map(s => [X(s.data), Y(s.pct), s]);
    const grid = [0, 25, 50, 75, 100].map(g =>
      `<line x1="${{mL}}" x2="${{W - mR}}" y1="${{Y(g)}}" y2="${{Y(g)}}" stroke="var(--grid)"/>
       <text x="2" y="${{Y(g) + 4}}">${{g}}%</text>`).join('');
    const path = pts.map((p, i) => `${{i ? 'L' : 'M'}}${{p[0].toFixed(1)}},${{p[1].toFixed(1)}}`).join('');
    const marks = pts.filter(p => p[2].evento).map(p =>
      `<circle cx="${{p[0]}}" cy="${{p[1]}}" r="4.5" fill="var(--accent)" stroke="var(--panel)" stroke-width="2"/>`).join('');
    const xlab = [serie[0], serie.at(-1)].map(s =>
      `<text x="${{X(s.data)}}" y="${{H - 6}}" text-anchor="middle">${{s.data}}</text>`).join('');
    wrap.innerHTML = `<svg viewBox="0 0 ${{W}} ${{H}}" role="img" style="width:100%"
        aria-label="Prontidão da tese ao longo do tempo: de ${{serie[0].pct}}% em ${{serie[0].data}} a ${{serie.at(-1).pct}}% em ${{serie.at(-1).data}}.">
      ${{grid}}<path d="${{path}}" fill="none" stroke="var(--accent)" stroke-width="2"/>
      ${{marks}}<circle cx="${{pts.at(-1)[0]}}" cy="${{pts.at(-1)[1]}}" r="4" fill="var(--accent)"/>${{xlab}}
      <rect id="hit" x="${{mL}}" y="0" width="${{W - mL - mR}}" height="${{H}}" fill="transparent"/></svg>
      <div class="tip" id="tip"></div>`;
    const svg = wrap.querySelector('svg'), tip = el('tip');
    svg.addEventListener('mousemove', e => {{
      const r = svg.getBoundingClientRect(), mx = (e.clientX - r.left) * W / r.width;
      let best = pts[0];
      for (const p of pts) if (Math.abs(p[0] - mx) < Math.abs(best[0] - mx)) best = p;
      tip.style.display = 'block';
      tip.style.left = Math.min(best[0] / W * 100, 82) + '%';
      tip.style.top = (best[1] / H * 100) + '%';
      tip.innerHTML = `<strong>${{best[2].pct}}%</strong> · ${{best[2].data}}` +
        (best[2].evento ? `<br>${{esc(best[2].evento)}}` : '');
    }});
    svg.addEventListener('mouseleave', () => tip.style.display = 'none');
  }})();
  el('serie-tab').innerHTML = '<thead><tr><th>Data</th><th>%</th><th>Pontos</th><th>Evento</th></tr></thead><tbody>' +
    serie.map(s => `<tr><td>${{s.data}}</td><td>${{s.pct}}%</td><td>${{s.pontos}}</td><td>${{esc(s.evento || '')}}</td></tr>`).join('') + '</tbody>';

  el('rodadas-def').innerHTML = P.rodadas.map(r =>
    `<div><b>${{r.id}}</b> ${{esc(r.nome)}} <small>${{esc(r.descricao)}} (${{esc(r.ref)}})</small></div>`).join('');

  const GLIFO = {{feito:'✓', gate:'🔒', andamento:'◐', pendente:'○', na:'–'}};
  const ptsCap = Object.fromEntries((pr.por_capitulo || []).map(c => [c.id, c]));
  const pill = (cell, capTit, rid) => {{
    const s = cell?.status || 'pendente';
    const bloq = (cell?.bloqueado_por || []).length ? ' ⛓' : '';
    const note = cell?.nota ? ` title="${{esc(cell.nota)}}"` : '';
    const aria = `${{capTit}}, rodada ${{rid}}: ${{s}}${{bloq ? ', bloqueada' : ''}}${{cell?.nota ? ' — ' + cell.nota : ''}}`;
    return `<span class="pill ${{s}}${{cell?.nota ? ' has-note' : ''}}"${{note}} aria-label="${{esc(aria)}}">${{GLIFO[s]}}${{bloq}}</span>`;
  }};
  el('matriz').innerHTML += '<thead><tr><th scope="col">Capítulo</th>' +
    P.rodadas.map(r => `<th scope="col" title="${{esc(r.nome)}} — ${{esc(r.descricao)}}">${{r.id}}</th>`).join('') +
    '<th scope="col">Pontos</th></tr></thead><tbody>' +
    P.capitulos.map(c => {{
      const t = ptsCap[c.id] || {{pontos: 0, feitos: 0}};
      return `<tr><th scope="row" class="chap">${{c.titulo}}<small>${{c.arquivo}}</small></th>` +
        P.rodadas.map(r => `<td>${{pill(c.rodadas[r.id], c.titulo, r.id)}}</td>`).join('') +
        `<td class="tot">${{t.feitos}}/${{t.pontos}}</td></tr>`;
    }}).join('') + '</tbody>';

  el('aberturas').innerHTML = P.capitulos.map(c => c.abertura ? `
    <details><summary>${{c.titulo}} — o que abre esta frente</summary>
      <ul class="notes">${{c.abertura.map(a => `<li>${{esc(a)}}</li>`).join('')}}</ul></details>` : '').join('');

  // quebra por tema: capítulos grandes demais para uma rodada só (hoje só o
  // Cap.2) viram frentes menores, cada uma com sua própria sequência de
  // etapas — ver capitulos[].quebra / sequencia_rodadas no plano
  const STAGE_ORDER = ['aberto', 'r3', 'r4', 'r1', 'gate', 'feito'];
  const STAGE_CLASS = {{aberto: 'pendente', r3: 'andamento', r4: 'andamento', r1: 'andamento', gate: 'gate', feito: 'feito'}};
  const capsComQuebra = P.capitulos.filter(c => (c.quebra || []).length);
  if (capsComQuebra.length) {{
    el('quebras').innerHTML = capsComQuebra.map(c => {{
      const temas = c.quebra;
      const pct = Math.round(100 * temas.reduce((s, t) => s + STAGE_ORDER.indexOf(t.status), 0)
        / (temas.length * (STAGE_ORDER.length - 1)));
      const cards = temas.map(t => {{
        const cls = STAGE_CLASS[t.status] || 'pendente';
        return `<div class="tema-card">
          <div class="tema-top">
            <span class="pill ${{cls}}">${{GLIFO[cls]}} ${{esc(t.status)}}</span>
            <span class="tema-resp"><span class="k-ag-dot" data-ag="${{esc(t.responsavel)}}" aria-hidden="true"></span>${{esc(t.responsavel)}}</span>
          </div>
          <p class="tema-nome">${{esc(t.tema)}}</p>
          <p class="tema-dim">linhas ${{esc(t.linhas)}} · ${{t.palavras}} palavras · ${{t.travessoes}} travessões · ${{t.citacoes}} citações</p>
        </div>`;
      }}).join('');
      return `<div class="quebra-cap">
        <div class="quebra-cap-head"><h3>${{esc(c.titulo)}}</h3>
          <span class="quebra-pct">${{pct}}% <small>(ponderado pela etapa de cada tema)</small></span></div>
        <div class="progress" role="progressbar" aria-valuenow="${{pct}}" aria-valuemin="0" aria-valuemax="100"
          aria-label="Progresso por tema de ${{esc(c.titulo)}}"><div class="progress-bar" style="width:${{pct}}%"></div></div>
        ${{c.sequencia_rodadas ? `<p class="quebra-seq">${{esc(c.sequencia_rodadas)}}</p>` : ''}}
        <div class="temas-grid">${{cards}}</div>
      </div>`;
    }}).join('');
  }} else {{
    el('quebra-card').style.display = 'none';
  }}

  // dois formatos convivem em execucoes.itens: experimentos (o_que/onde/
  // duracao/resultado_esperado/dono) e itens de texto em gate (descricao/
  // branch/commit/responsavel/bloqueado_por) — normaliza os dois aqui
  const EX = {{aguardando_inicio:['pendente','aguardando início'], rodando:['andamento','rodando'],
              concluido:['feito','concluído'], falhou:['gate','falhou'],
              gate:['gate','gate'], bloqueado:['pendente','bloqueado']}};
  const exec = P.execucoes?.itens || [];
  el('exec').innerHTML = exec.length ? exec.map(i => {{
    const [cls, lab] = EX[i.estado] || ['pendente', i.estado];
    const oque = i.o_que || i.descricao || '';
    const dono = i.dono || i.responsavel || '';
    const bloqPor = Array.isArray(i.bloqueado_por) ? i.bloqueado_por.join(', ') : i.bloqueado_por;
    const extras = [
      i.onde || (i.branch ? `branch ${{i.branch}}${{i.commit ? ' @ ' + i.commit : ''}}` : ''),
      i.duracao ? `~${{i.duracao}}` : '',
      i.resultado_esperado ? `→ ${{i.resultado_esperado}}` : '',
      bloqPor ? `bloqueado por: ${{bloqPor}}` : '',
    ].filter(Boolean).map(esc).join(' · ');
    const aprov = i.aprovacao_previa_autor
      ? ` <span class="pill andamento" title="${{esc(i.aprovacao_previa_autor)}}">✓ aprovação prévia do autor</span>` : '';
    return `<div class="item"><span class="pill ${{cls}}">${{lab}}</span>${{aprov}}
      <span class="t">${{esc(oque)}}${{extras ? ' <small style="color:var(--muted)">· ' + extras + '</small>' : ''}}</span>
      <span class="who">${{esc(dono)}}</span></div>`; }}).join('')
    : '<p class="vazia">0 execuções ativas</p>';

  el('grupos').innerHTML = P.artefatos.map(g => {{
    const done = g.itens.filter(i => i.status === 'feito').length;
    const todosF = done === g.itens.length;
    const corpo = g.itens.map(i => `
      <div class="item"><span class="pill ${{i.status}}">${{GLIFO[i.status] || ''}} ${{i.status}}</span>
        <span class="t">${{esc(i.titulo)}}${{(i.bloqueado_por || []).length ? ' <small style="color:var(--st-gate)">⛓ ' + i.bloqueado_por.join(', ') + '</small>' : ''}}</span>
        <span class="who">${{i.dono}}</span></div>`).join('');
    return `<div class="card group"><h3>${{g.nome}} <small style="color:var(--muted)">${{done}}/${{g.itens.length}}</small></h3>
      ${{todosF ? `<details><summary>✓ concluído</summary>${{corpo}}</details>` : corpo}}</div>`;
  }}).join('');

  el('ritual').innerHTML = P.ritual.map(x => `<li>${{esc(x)}}</li>`).join('');
  el('legenda').innerHTML = '<span class="label">Legenda</span>' + Object.entries(P.status_legenda)
    .map(([k, v]) => `<span class="pill ${{k}}" title="${{esc(v)}}">${{GLIFO[k] || ''}} ${{k}}</span>`).join('');
  el('meta-saida').textContent = `Meta de saída: parecer ARS ${{K.meta_saida.parecer_ars}} → ${{K.meta_saida.alvo}}.`;
}})();
</script>
<style>
.quebra-cap{{border-top:1px dashed var(--border); padding:var(--sp-4) 0}}
.quebra-cap:first-of-type{{border-top:none; padding-top:0}}
.quebra-cap-head{{display:flex; flex-wrap:wrap; align-items:baseline; justify-content:space-between; gap:var(--sp-3)}}
.quebra-cap-head h3{{margin:0; font-size:var(--fs-3); min-width:0}}
.quebra-pct{{font-weight:700; color:var(--accent); min-width:0}}
.quebra-pct small{{font-weight:400; color:var(--muted); font-size:var(--fs-1)}}
.quebra-seq{{margin:var(--sp-2) 0 0; color:var(--muted); font-size:var(--fs-2)}}
.temas-grid{{display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:var(--sp-3); margin-top:var(--sp-3)}}
.tema-card{{background:var(--ground); border:1px solid var(--border); border-radius:8px; padding:var(--sp-3);
  display:flex; flex-direction:column; gap:var(--sp-1)}}
.tema-top{{display:flex; align-items:center; justify-content:space-between; gap:var(--sp-2)}}
.tema-resp{{font-size:var(--fs-1); color:var(--muted); display:inline-flex; align-items:center}}
.tema-nome{{margin:0; font-size:var(--fs-2); font-weight:600}}
.tema-dim{{margin:0; font-size:var(--fs-1); color:var(--muted)}}
</style>"""
    return body, script


# --------------------------------------------------------------------------
# Coordenação (mensagens.html) — Fatia 2: board kanban somente-leitura
# (Aberta · Em andamento · Concluída), filtros por agente/tipo, arquivadas
# recolhidas abaixo, locks + saúde da coordenação.
# --------------------------------------------------------------------------
def build_coordenacao() -> tuple[str, str]:
    body = """
<header class="page-head"><h1>Coordenação</h1>
  <span class="meta" id="meta"></span></header>

<section class="card">
  <p class="ro-nota">🔒 quadro somente leitura — o estado muda pelos agentes no repositório (renomeação do arquivo é a reserva atômica do protocolo)</p>
  <div class="filtros" id="filtros" aria-label="Filtros do quadro"></div>
</section>

<div id="board-status" class="sr-only" role="status" aria-live="polite"></div>
<section class="k-board" id="board" aria-label="Quadro de coordenação"></section>

<section class="card"><details id="arq-det"><summary id="t-arq">Arquivadas</summary>
  <div class="scroll"><table id="arquivadas"></table></div></details></section>

<section class="card"><h2>Locks de superfície</h2><div id="locks"></div></section>

<section class="card"><h2>Saúde da coordenação</h2><p id="saude" class="vazia"></p></section>
"""
    json_blocks = as_json_script('mensagens', mens)
    script = json_blocks + """
<script>
(function(){
const M = JSON.parse(document.getElementById('mensagens').textContent);
const esc = s => String(s??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const idade = h => h < 1 ? `${Math.round(h*60)} min` : h < 48 ? `${Math.round(h)} h` : `${Math.round(h/24)} dias`;
document.getElementById('meta').textContent = `Atualizada em ${M.computado_em} · fonte: coordenacao/ no repositório`;

const AGENTES = ['principal', 'banca', 'revisor1', 'revisor2', 'autor'];
const TIPOS = ['tarefa', 'pergunta', 'aviso'];
const TIPO_LABEL = {tarefa: 'tarefa', pergunta: 'pergunta', aviso: 'aviso'};
const COLS = [
  {estado: 'aberta', nome: 'Aberta', glifo: '○'},
  {estado: 'em-andamento', nome: 'Em andamento', glifo: '◐'},
  {estado: 'concluida', nome: 'Concluída', glifo: '●'},
];

const todas = (M.mensagens || []).slice().sort((a, b) => b.ts.localeCompare(a.ts));
const ativas = todas.filter(m => !m.arquivada);
const arquivadas = todas.filter(m => m.arquivada);

// estado dos filtros: tudo ativo por padrão (mostra tudo até o usuário desligar algo)
const filtroState = {agente: Object.fromEntries(AGENTES.map(a => [a, true])),
                      tipo: Object.fromEntries(TIPOS.map(t => [t, true]))};

function hoje() { return new Date(); }
function prazoVencido(prazo) {
  if (!prazo) return false;
  const d = new Date(prazo);
  return !isNaN(d) && d < hoje();
}
function prazoFmt(prazo) { return esc(String(prazo).slice(0, 10)); }

// ux-design.md §4: fila priorizada dentro da raia — o essencial fica
// visível no topo mesmo sem rolar (atrasado+para-você > para-você > atrasado > recência)
function prioridade(m) {
  const pv = m.para === 'autor', atr = prazoVencido(m.prazo);
  if (pv && atr) return 0;
  if (pv) return 1;
  if (atr) return 2;
  return 3;
}
function ordenarPorPrioridade(itens) {
  return itens.slice().sort((a, b) => prioridade(a) - prioridade(b) || b.ts.localeCompare(a.ts));
}

function card(m) {
  const paraVoce = m.para === 'autor';
  const atrasado = prazoVencido(m.prazo);
  const tituloTxt = m.acao_esperada || m.slug.replace(/-/g, ' ');
  const titulo = esc(tituloTxt);
  const ref = m.referencia ? esc(m.referencia) : '';
  let rodape = `há ${idade(m.idade_horas)}`;
  if (m.prazo) rodape += ` · prazo ${prazoFmt(m.prazo)}`;
  const agDot = AGENTES.includes(m.de) ? `<span class="k-ag-dot" data-ag="${esc(m.de)}" aria-hidden="true"></span>` : '';
  return `<article class="k-card${paraVoce ? ' para-voce' : ''}${atrasado ? ' atrasado' : ''}"
      data-de="${esc(m.de)}" data-para="${esc(m.para)}" data-tipo="${esc(m.tipo)}">
    ${paraVoce ? '<span class="k-badge">para você</span>' : ''}
    <p class="k-titulo" title="${titulo}">${titulo}</p>
    <p class="k-rota"><strong>${agDot}${esc(m.de)} → ${esc(m.para)}</strong> <span class="k-tipo">${esc(TIPO_LABEL[m.tipo] || m.tipo)}</span></p>
    <p class="k-rodape">${rodape}${atrasado ? ' <strong class="k-atrasado">⚠ atrasado</strong>' : ''}</p>
    ${ref ? `<p class="k-ref" title="${ref}">${ref}</p>` : ''}
  </article>`;
}

function passaFiltro(m) {
  const agOk = filtroState.agente[m.de] || filtroState.agente[m.para] ||
    (!AGENTES.includes(m.de) && !AGENTES.includes(m.para));
  const tpOk = filtroState.tipo[m.tipo] !== undefined ? filtroState.tipo[m.tipo] : true;
  return agOk && tpOk;
}

function renderBoard() {
  const board = document.getElementById('board');
  const resumo = [];
  board.innerHTML = COLS.map(c => {
    const totalColuna = ativas.filter(m => m.estado === c.estado).length;
    const itens = ordenarPorPrioridade(ativas.filter(m => m.estado === c.estado && passaFiltro(m)));
    resumo.push(`${c.nome}: ${itens.length}`);
    const vazio = totalColuna === 0
      ? '<p class="vazia">Nada aqui</p>'
      : '<p class="vazia">Nada aqui com os filtros atuais</p>';
    const hId = `k-col-h-${c.estado}`;
    return `<div class="k-col" role="region" aria-labelledby="${hId}">
      <h2 class="k-col-h" id="${hId}">${c.glifo} ${c.nome} <span class="k-count">${itens.length}</span></h2>
      <div class="k-cards" tabindex="0" aria-label="Coluna ${esc(c.nome)}, ${itens.length} ${itens.length === 1 ? 'item' : 'itens'}">
        ${itens.length ? itens.map(card).join('') : vazio}
      </div>
    </div>`;
  }).join('');
  document.getElementById('board-status').textContent = resumo.join(' · ');
  // somente leitura: sem draggable, sem dragover/drop — arrastar não faz nada
}

function renderFiltros() {
  const wrap = document.getElementById('filtros');
  const pill = (grupo, val, label) => {
    const dot = grupo === 'agente' ? `<span class="k-ag-dot" data-ag="${esc(val)}" aria-hidden="true"></span>` : '';
    return `<button type="button" class="pilula on" data-grupo="${grupo}" data-val="${esc(val)}" aria-pressed="true">${dot}${esc(label)}</button>`;
  };
  wrap.innerHTML =
    `<div class="pilulas" aria-label="Filtrar por agente">` + AGENTES.map(a => pill('agente', a, a)).join('') + `</div>` +
    `<div class="pilulas" aria-label="Filtrar por tipo">` + TIPOS.map(t => pill('tipo', t, TIPO_LABEL[t])).join('') + `</div>`;
  wrap.querySelectorAll('.pilula').forEach(btn => btn.addEventListener('click', () => {
    const grupo = btn.dataset.grupo, val = btn.dataset.val;
    filtroState[grupo][val] = !filtroState[grupo][val];
    btn.classList.toggle('on', filtroState[grupo][val]);
    btn.setAttribute('aria-pressed', String(filtroState[grupo][val]));
    renderBoard();
  }));
}

renderFiltros();
renderBoard();

// arquivadas: recolhidas, não são coluna do board
const cab = '<thead><tr><th>Quando</th><th>De → Para</th><th>Assunto e ação esperada</th></tr></thead>';
const fmts = ts => `${ts.slice(6,8)}/${ts.slice(4,6)} ${ts.slice(9,11)}:${ts.slice(11,13)} UTC`;
const linha = m => `<tr>
  <td class="quando">${fmts(m.ts)}<br><small>há ${idade(m.idade_horas)}</small></td>
  <td class="rota">${esc(m.de)} → ${esc(m.para)}<small>${esc(m.tipo)}</small></td>
  <td class="assunto"><strong>${esc(m.slug.replace(/-/g,' '))}</strong>
    <small>${esc(m.acao_esperada)}${m.referencia ? '<br>ref: ' + esc(m.referencia) : ''}</small></td></tr>`;
document.getElementById('t-arq').textContent = `Arquivadas (${arquivadas.length})`;
const arqTab = document.getElementById('arquivadas');
arqTab.innerHTML = arquivadas.length ? cab + '<tbody>' + arquivadas.map(linha).join('') + '</tbody>' : '';
if (!arquivadas.length) arqTab.outerHTML = '<p class="vazia">Nada arquivado ainda.</p>';

const locks = M.locks || [];
document.getElementById('locks').innerHTML = locks.length ? locks.map(l => `
  <p style="margin:.25rem 0">${l.vencido ? '✕' : '●'} <code>${esc(l.superficie)}</code>
   · dono ${esc(l.dono)} · ${l.vencido ? 'vencido — quebrável' : 'renovado há ' + l.renovado_ha_min + ' min'}</p>`).join('')
  : '<p class="vazia">Nenhuma superfície travada.</p>';

const s = M.saude || {};
const doente = s.bloqueio_mais_antigo_h > 48 || s.locks_vencidos > 0;
document.getElementById('saude').textContent = doente
  ? `✕ Doente — bloqueio mais antigo ${s.bloqueio_mais_antigo_h}h · locks vencidos ${s.locks_vencidos} · mensagens ativas ${s.mensagens_ativas}`
  : `✓ Saudável — mensagens ativas ${s.mensagens_ativas} · para o autor (abertas) ${s.para_autor_abertas} · locks ativos ${s.locks_ativos}`;
})();
</script>
<style>
.sr-only{position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden;
  clip:rect(0,0,0,0); white-space:nowrap; border:0}
.ro-nota{margin:0 0 var(--sp-3); color:var(--muted); font-size:var(--fs-2)}
.filtros{display:flex; flex-wrap:wrap; gap:var(--sp-4)}
.pilulas{display:flex; flex-wrap:wrap; gap:var(--sp-2)}
.pilula{border:1px solid var(--border); background:var(--panel); color:var(--muted); border-radius:99px;
  padding:.25rem .7rem; font-size:var(--fs-2); cursor:pointer}
.pilula.on{border-color:var(--accent); color:var(--accent); background:var(--accent-soft); font-weight:600}
/* ux-design.md §2/§5: o board tem altura ~constante (raia limitada); quem
   rola é cada coluna (.k-cards), nunca a página inteira por causa de N cartões */
.k-board{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:var(--sp-4); align-items:start}
.k-col{background:var(--panel); border:1px solid var(--border); border-radius:8px; padding:var(--sp-3); display:flex;
  flex-direction:column; gap:var(--sp-2); min-width:0}
/* as duas media queries vêm DEPOIS das regras base — min-width:260px do
   breakpoint intermediário precisa vencer o min-width:0 da regra base na
   cascata (mesma especificidade; quem aparece por último ganha) */
@media (max-width:1099px) and (min-width:601px){
  .k-board{display:flex; overflow-x:auto; overscroll-behavior-x:contain; padding-bottom:var(--sp-2)}
  .k-col{min-width:260px; flex:1 0 260px}
}
@media (max-width:600px){ .k-board{grid-template-columns:1fr} }
.k-col-h{font-size:var(--fs-3); display:flex; align-items:center; gap:var(--sp-2); margin:0 0 var(--sp-1)}
.k-count{margin-left:auto; color:var(--muted); font-size:var(--fs-1); font-weight:400}
.k-cards{display:flex; flex-direction:column; gap:var(--sp-2); min-width:0;
  max-height:clamp(320px,58vh,640px); overflow-y:auto; overflow-x:hidden; overscroll-behavior:contain; padding-right:var(--sp-1)}
.k-card{background:var(--ground); border:1px solid var(--border); border-radius:8px; padding:var(--sp-2) var(--sp-3);
  cursor:default; position:relative; display:flex; flex-direction:column; gap:var(--sp-1); line-height:1.3; min-width:0}
.k-card.para-voce{border-color:var(--atencao-borda); box-shadow:inset 3px 0 0 var(--atencao)}
.k-badge{align-self:flex-start; background:var(--atencao-bg); color:var(--atencao); border:1px solid var(--atencao-borda);
  border-radius:99px; padding:.05rem .55rem; font-size:var(--fs-1); font-weight:700}
/* fonte um pouco menor no cartão inteiro (pedido do autor) — título sai de
   --fs-3 para --fs-2, o resto já estava no piso da escala (--fs-1) */
.k-titulo{margin:0; font-size:var(--fs-2); font-weight:600; line-height:1.25;
  display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden}
.k-rota{margin:0; font-size:var(--fs-1)}
.k-rota strong{font-weight:600}
.k-tipo{color:var(--muted); font-size:var(--fs-1)}
.k-rodape{margin:0; color:var(--muted); font-size:var(--fs-1)}
.k-atrasado{color:var(--atencao)}
.k-ref{margin:0; color:var(--muted); font-size:var(--fs-1); white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.pilula .k-ag-dot{margin-right:.4em}
.estado{display:inline-flex; gap:.35rem; align-items:center; white-space:nowrap; font-weight:600}
td.quando{white-space:nowrap; color:var(--muted)}
td.rota{white-space:nowrap; font-weight:600}
td.rota small{display:block; font-weight:400; color:var(--muted)}
td.assunto strong{display:block}
td.assunto small{color:var(--muted)}
</style>"""
    return body, script


# --------------------------------------------------------------------------
# Resultados (resultados.html) — Fatia 2: o que a tese já produziu, para o
# autor e a banca. Três blocos com papéis diferentes: achados (conclusão
# científica sustentada por evidência), entregas (artefato que existe) e
# experimentos executados. Conteúdo lido de docs/records/resultados.json —
# outro agente aprofunda; esta função só entrega a estrutura + os exemplos
# reais já carregados no JSON.
# --------------------------------------------------------------------------
def build_resultados() -> tuple[str, str]:
    body = """
<header class="page-head"><h1>Resultados</h1>
  <span class="meta" id="meta"></span></header>

<section class="card">
  <p class="vazia">O que a tese já produziu, com a evidência que sustenta cada
  número — vitrine para o autor e a banca, sem afirmação sem fonte.</p>
</section>

<section aria-label="Achados por pilar">
  <div id="achados-pilares"></div>
</section>

<section class="card">
  <h2>Entregas</h2>
  <div class="entregas" id="entregas"></div>
</section>

<section class="card">
  <h2>Experimentos executados</h2>
  <div class="scroll"><table id="experimentos"></table></div>
</section>
"""
    json_blocks = as_json_script('resultados', resultados)
    script = json_blocks + """
<script>
(function(){
const R = JSON.parse(document.getElementById('resultados').textContent || '{}');
const esc = s => String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
document.getElementById('meta').textContent = R.atualizado_em ? `atualizado em ${R.atualizado_em}` : '';

const pilares = R.pilares || {};
const achados = R.achados || [];
document.getElementById('achados-pilares').innerHTML = Object.entries(pilares).map(([id, nome]) => {
  const itens = achados.filter(a => a.pilar === id);
  const corpo = itens.length ? itens.map(a => `
    <div class="achado">
      <p class="achado-afirmacao">${esc(a.afirmacao)}</p>
      <p class="achado-numero">${esc(a.numero)}</p>
      <p class="achado-evidencia">${esc(a.evidencia)}</p>
      ${a.detalhe ? `<p class="achado-detalhe">${esc(a.detalhe)}</p>` : ''}
    </div>`).join('') : '<p class="vazia">Sem achados registrados nesta versão.</p>';
  return `<div class="card" style="margin-bottom:var(--sp-4)">
    <h2>${esc(id)} — ${esc(nome)}</h2>
    ${corpo}
  </div>`;
}).join('');

const entregas = R.entregas || [];
document.getElementById('entregas').innerHTML = entregas.length ? entregas.map(e => {
  const isLink = /^https?:\\/\\/|^doi\\.org\\//.test(e.link_ou_caminho || '');
  const alvo = isLink
    ? `<a href="${/^https?:\\/\\//.test(e.link_ou_caminho) ? esc(e.link_ou_caminho) : 'https://' + esc(e.link_ou_caminho)}">${esc(e.link_ou_caminho)}</a>`
    : `<code>${esc(e.link_ou_caminho || '')}</code>`;
  return `<div class="entrega">
    <p class="entrega-nome">${esc(e.nome)}</p>
    <p class="entrega-descricao">${esc(e.descricao)}</p>
    <p class="entrega-link">${alvo}</p>
  </div>`;
}).join('') : '<p class="vazia">Nenhuma entrega registrada ainda.</p>';

const experimentos = R.experimentos || [];
const cab = '<thead><tr><th>Experimento</th><th>Pergunta</th><th>Resultado</th><th>Artefato</th></tr></thead>';
const linha = x => `<tr>
  <td class="chap">${esc(x.id)}</td>
  <td>${x.pergunta ? esc(x.pergunta) : '<span class="vazia">—</span>'}</td>
  <td>${x.resultado ? esc(x.resultado) : '<span class="vazia">pendente' + (x.nota ? ': ' + esc(x.nota) : '') + '</span>'}</td>
  <td class="tot">${x.artefato ? esc(x.artefato) : '—'}</td></tr>`;
const expTab = document.getElementById('experimentos');
expTab.innerHTML = experimentos.length ? cab + '<tbody>' + experimentos.map(linha).join('') + '</tbody>' : '';
if (!experimentos.length) expTab.outerHTML = '<p class="vazia">Nenhum experimento registrado ainda.</p>';
})();
</script>
<style>
.achado{border-top:1px dashed var(--border); padding:var(--sp-3) 0}
.achado:first-of-type{border-top:none; padding-top:0}
.achado-afirmacao{margin:0 0 var(--sp-1); font-size:var(--fs-3)}
.achado-numero{margin:0; font-size:var(--fs-5); font-weight:700; color:var(--accent)}
.achado-evidencia{margin:.2rem 0 0; color:var(--muted); font-size:var(--fs-1)}
.achado-detalhe{margin:.3rem 0 0; color:var(--muted); font-size:var(--fs-2)}
.entregas{display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:var(--sp-3)}
.entrega{border:1px solid var(--border); border-radius:8px; padding:var(--sp-3); background:var(--ground)}
.entrega-nome{margin:0; font-weight:600; font-size:var(--fs-3)}
.entrega-descricao{margin:.25rem 0; color:var(--muted); font-size:var(--fs-2)}
.entrega-link{margin:0; font-size:var(--fs-1); word-break:break-word}
</style>"""
    return body, script


# --------------------------------------------------------------------------
# Referências (referencias.html) — tabela ordenável de tudo o que a tese
# cita, cruzado com fichamento e PDF. Pedido literal do autor (tarefa do
# principal 20260816-2110). ux-design.md do ciclo 003 explica os porquês.
# --------------------------------------------------------------------------
def build_referencias() -> tuple[str, str]:
    body = """
<header class="page-head"><h1>Referências</h1>
  <span class="meta" id="meta"></span></header>

<section class="card">
  <input type="search" id="ref-busca" class="ref-busca"
    placeholder="Buscar por título, autor ou chave…" aria-label="Buscar referência">
</section>

<section class="card">
  <div class="scroll"><table id="ref-tabela"></table></div>
</section>
"""
    json_blocks = as_json_script('referencias', referencias)
    script = json_blocks + """
<script>
(function(){
const R = JSON.parse(document.getElementById('referencias').textContent || '{}');
const refs = R.referencias || [];
const esc = s => String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
document.getElementById('meta').textContent = R.computado_em
  ? `${R.total} referências · ${R.citadas} citadas no livro · atualizado em ${R.computado_em}` : '';

const COLS = [
  {key:'ordem',    label:'#',            kind:'num',  get:r=>r.ordem},
  {key:'titulo',   label:'Título',       kind:'str',  get:r=>r.titulo},
  {key:'autores',  label:'Autores',      kind:'str',  get:r=>(r.autores[0]||'')},
  {key:'ano',      label:'Ano',          kind:'num',  get:r=>(r.ano ? parseInt(r.ano,10) : null)},
  {key:'onde',     label:'Onde citada',  kind:'num',  get:r=>r.ordem},
  {key:'link',     label:'Link',         kind:'str',  get:r=>(r.link_tipo||'')},
  {key:'pdf',      label:'PDF',          kind:'bool', get:r=>r.pdf},
  {key:'fichado',  label:'Fichado',      kind:'bool', get:r=>r.fichado},
  {key:'detalhes', label:'Detalhes',     sortable:false},
];

let sortState = {campo:'ordem', dir:1};
let filtro = '';

function cmp(a, b, col, dir){
  const va = col.get(a), vb = col.get(b);
  if (va == null && vb == null) return 0;
  if (va == null) return 1;
  if (vb == null) return -1;
  let res;
  if (col.kind === 'num') res = va - vb;
  else if (col.kind === 'bool') res = (vb?1:0) - (va?1:0);
  else res = String(va).localeCompare(String(vb), 'pt-BR');
  return dir * res;
}

function shortCap(capStr){ return capStr ? capStr.split(' — ')[0] : ''; }

function autoresTxt(autores){
  if (!autores || !autores.length) return '—';
  if (autores.length <= 3) return esc(autores.join(', '));
  return `<span title="${esc(autores.join(', '))}">${esc(autores[0])} et al.</span>`;
}

function ondeCell(r){
  if (!r.primeira_aparicao) return '<span class="vazia">não citada</span>';
  const cap = shortCap(r.primeira_aparicao.capitulo);
  const sec = r.primeira_aparicao.secao;
  const tip = r.ocorrencias.map(o => `${o.capitulo}${o.secao ? ' § ' + o.secao : ''}`).join('\\n');
  return `<span title="${esc(tip)}">${esc(cap)}${sec ? ' §' + esc(sec) : ''}` +
    (r.total_ocorrencias > 1 ? ` <span class="ref-badge">${r.total_ocorrencias}×</span>` : '') + `</span>`;
}

function linkCell(r){
  return r.link ? `<a href="${esc(r.link)}" target="_blank" rel="noopener">${esc(r.link_tipo || 'link')} ↗</a>`
                : '<span class="vazia">—</span>';
}

function badge(ok){
  return ok ? '<span class="pill feito">✓ sim</span>' : '<span class="pill pendente">✕ não</span>';
}

function passaFiltro(r){
  if (!filtro) return true;
  const alvo = (r.titulo + ' ' + (r.autores||[]).join(' ') + ' ' + r.chave).toLowerCase();
  return alvo.includes(filtro);
}

function linha(r){
  const detId = `det-${r.chave}`;
  return `<tr>
    <td class="tot">${r.ordem ?? '<span class="vazia">não citada</span>'}</td>
    <td>${esc(r.titulo)}</td>
    <td>${autoresTxt(r.autores)}</td>
    <td class="tot">${r.ano ? esc(r.ano) : '<span class="vazia">—</span>'}</td>
    <td>${ondeCell(r)}</td>
    <td>${linkCell(r)}</td>
    <td>${badge(r.pdf)}</td>
    <td>${badge(r.fichado)}</td>
    <td><button type="button" class="ref-det-btn" data-target="${detId}" aria-expanded="false">ver</button></td>
  </tr>
  <tr id="${detId}" class="ref-det-row" hidden>
    <td colspan="9">${r.detalhes_html ? r.detalhes_html : '<p class="vazia">Ainda não fichada.</p>'}</td>
  </tr>`;
}

function headerCell(col){
  if (col.sortable === false) return `<th scope="col">${esc(col.label)}</th>`;
  const ativo = sortState.campo === col.key;
  const seta = ativo ? (sortState.dir === 1 ? ' ▲' : ' ▼') : '';
  return `<th scope="col"><button type="button" class="ref-th-btn" data-col="${col.key}" aria-sort="${ativo ? (sortState.dir===1?'ascending':'descending') : 'none'}">${esc(col.label)}${seta}</button></th>`;
}

function render(){
  const col = COLS.find(c => c.key === sortState.campo) || COLS[0];
  const visiveis = refs.filter(passaFiltro).slice().sort((a,b) => cmp(a,b,col,sortState.dir));
  const tab = document.getElementById('ref-tabela');
  tab.innerHTML = '<thead><tr>' + COLS.map(headerCell).join('') + '</tr></thead>' +
    '<tbody>' + (visiveis.length ? visiveis.map(linha).join('') : '<tr><td colspan="9" class="vazia">Nenhuma referência encontrada.</td></tr>') + '</tbody>';
  tab.querySelectorAll('.ref-th-btn').forEach(btn => btn.addEventListener('click', () => {
    const key = btn.dataset.col;
    if (sortState.campo !== key) sortState = {campo: key, dir: 1};
    else if (sortState.dir === 1) sortState.dir = -1;
    else sortState = {campo: 'ordem', dir: 1};
    render();
  }));
  tab.querySelectorAll('.ref-det-btn').forEach(btn => btn.addEventListener('click', () => {
    const row = document.getElementById(btn.dataset.target);
    const aberto = !row.hidden;
    row.hidden = aberto;
    btn.setAttribute('aria-expanded', String(!aberto));
    btn.textContent = aberto ? 'ver' : 'fechar';
  }));
}

document.getElementById('ref-busca').addEventListener('input', e => {
  filtro = e.target.value.trim().toLowerCase();
  render();
});

render();
})();
</script>
<style>
.ref-busca{width:100%; max-width:420px; padding:.4rem .6rem; border:1px solid var(--border);
  border-radius:6px; background:var(--panel); color:var(--ink); font-size:var(--fs-3)}
.ref-th-btn{background:none; border:none; color:var(--muted); font-size:var(--fs-1);
  text-transform:uppercase; letter-spacing:.06em; font-weight:600; cursor:pointer; padding:0; white-space:nowrap}
.ref-th-btn:hover{color:var(--accent)}
.ref-badge{color:var(--muted); font-size:var(--fs-1)}
.ref-det-btn{background:none; border:1px solid var(--border); color:var(--accent); border-radius:6px;
  padding:.15rem .5rem; font-size:var(--fs-1); cursor:pointer}
.ref-det-row td{background:var(--ground); padding:var(--sp-4)}
.ref-det-row h2, .ref-det-row h3{font-size:var(--fs-3); margin:.8rem 0 .3rem}
.ref-det-row h2:first-child, .ref-det-row h3:first-child{margin-top:0}
.ref-det-row p{margin:.3rem 0}
.ref-det-row table{margin:.4rem 0}
#ref-tabela td, #ref-tabela th{vertical-align:top}
</style>"""
    return body, script


# --------------------------------------------------------------------------
# Grafo (grafo.html) — janela para o instrumento externo já existente
# (fichamentos/kg_template.html, canvas de física de força). Embutido via
# iframe, nunca reimplementado — ux-design.md do ciclo 004 explica o porquê
# (é outro sistema, com identidade visual própria, não um componente nativo).
# --------------------------------------------------------------------------
def build_grafo() -> tuple[str, str]:
    n_nos = len(kg.get("nodes", []))
    n_arestas = len(kg.get("edges", []))
    body = f"""
<header class="page-head"><h1>Grafo</h1>
  <span class="meta">{n_nos} nós · {n_arestas} arestas</span></header>

<section class="card">
  <p class="vazia">Mapa de argumentação e grafo de conhecimento fichado —
  as relações (estende, compara, contradiz, sustenta-se em) foram lidas e
  registradas por quem fichou cada obra, não inferidas automaticamente.
  Não é uma rede de co-citação bibliométrica. Instrumento separado do
  site: física de força, filtros por tipo de nó e um painel de detalhe ao
  clicar — leva alguns segundos para os nós convergirem.
  <a href="grafo-embed.html" target="_blank" rel="noopener">abrir em nova aba ↗</a></p>
</section>

<div class="grafo-frame-wrap">
  <iframe id="grafo-iframe" class="grafo-frame" src="grafo-embed.html"
    title="Grafo de conhecimento da tese FALCO — instrumento interativo separado, {n_nos} nós e {n_arestas} arestas"
    loading="lazy"></iframe>
</div>
"""
    script = """
<style>
.grafo-frame-wrap{max-width:none; margin:0 calc(-1 * var(--sp-5))}
@media (max-width:767px){ .grafo-frame-wrap{margin:0 calc(-1 * var(--sp-4))} }
.grafo-frame{width:100%; height:calc(100vh - 260px); min-height:520px;
  border:1px solid var(--border); border-radius:8px; display:block; background:var(--panel)}
</style>"""
    return body, script


# --------------------------------------------------------------------------
# Bibliometria (bibliometria.html) — perfil descritivo da bibliografia da
# tese (não uma bibliometria de campo: sem citação externa, sem busca
# sistemática — só o que este autor leu e citou). ux-design.md do ciclo 004
# registra, com um especialista em bibliometria acadêmica, o que é honesto
# de medir aqui e o que NÃO é (Lotka/Bradford/h-index ficam fora, com razão
# documentada em qa-report.md).
# --------------------------------------------------------------------------
def build_bibliometria() -> tuple[str, str]:
    refs_list = referencias.get("referencias", [])
    pilares_nomes = resultados.get("pilares", {})

    pilar_counts: dict[str, int] = {}
    for e in kg.get("edges", []):
        if e.get("type") == "pillars":
            target = str(e.get("target", "")).removeprefix("pilar:")
            pilar_counts[target] = pilar_counts.get(target, 0) + 1

    total = referencias.get("total", len(refs_list))
    citadas = referencias.get("citadas", sum(1 for r in refs_list if r.get("ordem")))
    fichadas = sum(1 for r in refs_list if r.get("fichado"))
    com_pdf = sum(1 for r in refs_list if r.get("pdf"))

    body = """
<header class="page-head"><h1>Bibliometria</h1>
  <span class="meta" id="meta"></span></header>

<section class="card">
  <p class="vazia">Como a revisão de literatura desta tese foi conduzida —
  composição, atualidade e distribuição da bibliografia. <strong>Não</strong>
  é o que a pesquisa descobriu (isso está em Resultados) nem uma
  bibliometria do campo científico: sem citação externa, sem afiliação,
  sem busca sistemática de base — só o que este autor leu e citou.</p>
</section>

<section class="kpis" id="kpis-bib" aria-label="Indicadores da bibliografia"></section>

<section class="card">
  <span class="label">Quando a literatura consultada nesta tese foi publicada</span>
  <h2>Publicações por ano</h2>
  <div id="chart-anos"></div>
  <details><summary>Ver dados em tabela</summary>
    <div class="scroll"><table id="tab-anos"></table></div>
  </details>
</section>

<div class="groups">
  <section class="card">
    <span class="label">Autores mais presentes nesta bibliografia — não citação externa ao campo</span>
    <h2>Top 10 autores</h2>
    <div id="rank-autores"></div>
  </section>
  <section class="card">
    <span class="label">Veículos mais presentes nesta bibliografia</span>
    <h2>Top 10 veículos</h2>
    <div id="rank-venues"></div>
  </section>
  <section class="card">
    <span class="label">Frequência de citação dentro do texto da tese — não impacto externo</span>
    <h2>Top 10 mais citadas no texto</h2>
    <div id="rank-citadas"></div>
  </section>
  <section class="card">
    <span class="label">Referências fichadas por pilar (P1–P4) — uma obra pode contar em mais de um pilar</span>
    <h2>Distribuição por pilar</h2>
    <div id="rank-pilares"></div>
  </section>
</div>
"""
    json_blocks = (
        as_json_script('bib-refs', refs_list) + "\n"
        + as_json_script('bib-pilares', {'nomes': pilares_nomes, 'contagens': pilar_counts})
    )
    script = json_blocks + """
<script>
(function(){
const REFS = JSON.parse(document.getElementById('bib-refs').textContent || '[]');
const PILARES = JSON.parse(document.getElementById('bib-pilares').textContent || '{}');
const esc = s => String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const el = id => document.getElementById(id);

const total = REFS.length;
const citadas = REFS.filter(r => r.ordem).length;
const fichadas = REFS.filter(r => r.fichado).length;
const comPdf = REFS.filter(r => r.pdf).length;

el('meta').textContent = `${total} referências · ${citadas} citadas · ${fichadas} fichadas`;
el('kpis-bib').innerHTML = `
  <div class="kpi hero"><span class="label">Total na bibliografia</span><span class="v">${total}</span>
    <span class="ctx">${citadas} citadas de fato no texto</span></div>
  <div class="kpi"><span class="label">Fichadas</span><span class="v">${fichadas}</span>
    <span class="ctx">${(fichadas/total*100).toFixed(0)}% do total processado</span></div>
  <div class="kpi"><span class="label">Com PDF</span><span class="v">${comPdf}</span>
    <span class="ctx">${(comPdf/total*100).toFixed(0)}% com arquivo físico</span></div>`;

// ---- barra de ranking reutilizável: rótulo + barra proporcional + valor sempre visível ----
function hbar(containerId, itens) {
  const max = Math.max(...itens.map(i => i.valor), 1);
  el(containerId).innerHTML = itens.map(it => {
    const pct = (it.valor / max * 100).toFixed(1);
    const rotulo = `${it.label}: ${it.valor}`;
    return `<div class="hbar-row">
      <span class="hbar-label" title="${esc(it.label)}">${esc(it.label)}</span>
      <svg class="hbar-track" viewBox="0 0 100 14" preserveAspectRatio="none" role="img" aria-label="${esc(rotulo)}">
        <rect x="0" y="0" width="100" height="14" fill="var(--grid)" rx="2"/>
        <rect x="0" y="0" width="${pct}" height="14" fill="var(--accent)" rx="2"><title>${esc(rotulo)}</title></rect>
      </svg>
      <span class="hbar-valor">${it.valor}</span>
    </div>`;
  }).join('') || '<p class="vazia">Sem dados.</p>';
}

function topN(getter, n) {
  const contagem = new Map();
  for (const r of REFS) {
    const vals = getter(r);
    for (const v of (Array.isArray(vals) ? vals : [vals])) {
      if (!v) continue;
      contagem.set(v, (contagem.get(v) || 0) + 1);
    }
  }
  return [...contagem.entries()].sort((a,b) => b[1]-a[1]).slice(0, n).map(([label,valor]) => ({label, valor}));
}

hbar('rank-autores', topN(r => r.autores, 10));
hbar('rank-venues', topN(r => r.venue, 10));
hbar('rank-citadas', REFS.filter(r => r.total_ocorrencias > 0)
  .sort((a,b) => b.total_ocorrencias - a.total_ocorrencias).slice(0,10)
  .map(r => ({label: r.titulo, valor: r.total_ocorrencias})));

const nomesPilar = PILARES.nomes || {};
const contagensPilar = PILARES.contagens || {};
const ORDEM_PILAR = ['P1','P2','P3','P4'];
const itensPilar = ORDEM_PILAR.filter(p => contagensPilar[p]).map(p =>
  ({label: `${p} — ${nomesPilar[p] || ''}`, valor: contagensPilar[p]}));
const outros = Object.entries(contagensPilar).filter(([k]) => !ORDEM_PILAR.includes(k))
  .reduce((s,[,v]) => s+v, 0);
if (outros) itensPilar.push({label: 'Geral / transversal', valor: outros});
hbar('rank-pilares', itensPilar);

// ---- publicações por ano: bucket <2000 + barra por ano 2000..max ----
(function chartAnos(){
  const CORTE = 2000;
  const porAno = new Map();
  let antes = 0;
  for (const r of REFS) {
    const a = parseInt(r.ano, 10);
    if (!a) continue;
    if (a < CORTE) { antes++; continue; }
    porAno.set(a, (porAno.get(a) || 0) + 1);
  }
  if (porAno.size === 0 && !antes) { el('chart-anos').innerHTML = '<p class="vazia">Sem dados de ano.</p>'; return; }
  const anoMax = Math.max(...porAno.keys());
  const dados = [{rotulo: `≤${CORTE-1}`, valor: antes, bucket: true}];
  for (let a = CORTE; a <= anoMax; a++) dados.push({rotulo: String(a), valor: porAno.get(a) || 0, bucket: false});

  const W = 980, H = 240, mL = 32, mR = 12, mT = 10, mB = 30;
  const n = dados.length;
  const bw = (W - mL - mR) / n;
  const max = Math.max(...dados.map(d => d.valor), 1);
  const Y = v => mT + (H - mT - mB) * (1 - v / max);
  const passo = Math.max(1, Math.round(n / 10));
  const barras = dados.map((d, i) => {
    const x = mL + i * bw, y = Y(d.valor), h = (H - mT - mB) - (y - mT);
    const rotula = i === 0 || i === n - 1 || i % passo === 0;
    return `<g><rect x="${(x+1).toFixed(1)}" y="${y.toFixed(1)}" width="${Math.max(bw-2,0.5).toFixed(1)}" height="${h.toFixed(1)}"
        fill="var(--accent)" ${d.bucket ? 'opacity="0.55"' : ''}><title>${esc(d.rotulo)}: ${d.valor} referência(s)</title></rect>
      ${rotula ? `<text x="${(x+bw/2).toFixed(1)}" y="${H-mB+14}" text-anchor="middle">${esc(d.rotulo)}</text>` : ''}</g>`;
  }).join('');
  const gMax = Math.max(1, max);
  const grid = [0, Math.round(gMax/2), gMax].map(g =>
    `<line x1="${mL}" x2="${W-mR}" y1="${Y(g).toFixed(1)}" y2="${Y(g).toFixed(1)}" stroke="var(--grid)"/>
     <text x="2" y="${(Y(g)+4).toFixed(1)}">${g}</text>`).join('');
  const picoIdx = dados.reduce((best,d,i) => d.valor > dados[best].valor ? i : best, 0);
  el('chart-anos').innerHTML = `<svg viewBox="0 0 ${W} ${H}" role="img" style="width:100%"
      aria-label="Publicações por ano: de ${dados[0].rotulo} a ${dados.at(-1).rotulo}, pico de ${dados[picoIdx].valor} em ${dados[picoIdx].rotulo}.">
    ${grid}${barras}</svg>`;
  el('tab-anos').innerHTML = '<thead><tr><th>Período</th><th>Referências</th></tr></thead><tbody>' +
    dados.filter(d => d.valor > 0).map(d => `<tr><td>${esc(d.rotulo)}</td><td>${d.valor}</td></tr>`).join('') + '</tbody>';
})();
})();
</script>
<style>
.hbar-row{display:grid; grid-template-columns:minmax(0,180px) 1fr auto; gap:var(--sp-3);
  align-items:center; padding:var(--sp-1) 0}
.hbar-label{font-size:var(--fs-2); color:var(--ink); overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
.hbar-track{height:14px; width:100%; display:block}
.hbar-valor{font-size:var(--fs-1); color:var(--muted); font-variant-numeric:tabular-nums;
  text-align:right; min-width:2.2em}
#chart-anos text{font-size:10px}
</style>"""
    return body, script


def main() -> None:
    pages = {
        "index.html": build_controle,
        "plano.html": build_plano,
        "mensagens.html": build_coordenacao,
        "resultados.html": build_resultados,
        "referencias.html": build_referencias,
        "grafo.html": build_grafo,
        "bibliometria.html": build_bibliometria,
    }
    titles = {"index.html": "Controle", "plano.html": "Plano",
              "mensagens.html": "Coordenação", "resultados.html": "Resultados",
              "referencias.html": "Referências", "grafo.html": "Grafo",
              "bibliometria.html": "Bibliometria"}
    for fname, builder in pages.items():
        body, script = builder()
        html = page_shell(titles[fname], fname, FOOTER_TEXT, body, script)
        (out_dir / fname).write_text(html, encoding="utf-8")
    print(f"ok: {out_dir}/ ({', '.join(titles.values())})  "
          f"plano v{plano['versao']}, PGP {kpis.get('prontidao', {}).get('global_pct', '?')}%")


if __name__ == "__main__":
    main()
