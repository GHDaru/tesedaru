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
kpis = json.loads(kpis_path.read_text(encoding="utf-8")) if kpis_path.exists() else {}
mens = json.loads(mens_path.read_text(encoding="utf-8")) if mens_path.exists() else {}


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

  const EX = {{aguardando_inicio:['pendente','aguardando início'], rodando:['andamento','rodando'],
              concluido:['feito','concluído'], falhou:['gate','falhou']}};
  const exec = P.execucoes?.itens || [];
  el('exec').innerHTML = exec.length ? exec.map(i => {{
    const [cls, lab] = EX[i.estado] || ['pendente', i.estado];
    return `<div class="item"><span class="pill ${{cls}}">${{lab}}</span>
      <span class="t">${{esc(i.o_que)}} <small style="color:var(--muted)">· ${{esc(i.onde)}} · ~${{i.duracao}} · → ${{esc(i.resultado_esperado)}}</small></span>
      <span class="who">${{i.dono}}</span></div>`; }}).join('')
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
</script>"""
    return body, script


# --------------------------------------------------------------------------
# Coordenação (mensagens.html) — Fatia 1: renderização em tabela (o kanban é
# Fatia 2); mantém a função íntegra dentro do novo casco de navegação.
# --------------------------------------------------------------------------
def build_coordenacao() -> tuple[str, str]:
    body = """
<header class="page-head"><h1>Coordenação</h1>
  <span class="meta" id="meta"></span></header>

<section class="card"><h2 id="t-ativas">Ativas</h2>
  <div class="scroll"><table id="ativas"></table></div></section>
<section class="card"><h2 id="t-conc">Concluídas</h2>
  <div class="scroll"><table id="concluidas"></table></div></section>
<section class="card"><details><summary id="t-arq">Arquivadas</summary>
  <div class="scroll"><table id="arquivadas"></table></div></details></section>
<section class="card"><h2>Locks de superfície</h2><div id="locks"></div></section>
"""
    json_blocks = as_json_script('mensagens', mens)
    script = json_blocks + f"""
<script>
(function(){{
const M = JSON.parse(document.getElementById('mensagens').textContent);
const esc = s => String(s??'').replace(/&/g,'&amp;').replace(/</g,'&lt;');
const GL = {{aberta:'○ aberta', 'em-andamento':'◐ em andamento', concluida:'● concluída'}};
const fmts = ts => `${{ts.slice(6,8)}}/${{ts.slice(4,6)}} ${{ts.slice(9,11)}}:${{ts.slice(11,13)}} UTC`;
const idade = h => h < 1 ? `${{Math.round(h*60)}} min` : h < 48 ? `${{Math.round(h)}} h` : `${{Math.round(h/24)}} dias`;
document.getElementById('meta').textContent = `Atualizada em ${{M.computado_em}} · fonte: coordenacao/ no repositório`;
const linha = m => `<tr>
  <td><span class="estado ${{m.estado}}">${{GL[m.estado]}}</span></td>
  <td class="quando">${{fmts(m.ts)}}<br><small>há ${{idade(m.idade_horas)}}</small></td>
  <td class="rota">${{esc(m.de)}} → ${{esc(m.para)}}<small>${{esc(m.tipo)}}</small></td>
  <td class="assunto"><strong>${{esc(m.slug.replace(/-/g,' '))}}</strong>
    <small>${{esc(m.acao_esperada)}}${{m.prazo ? ' · prazo ' + esc(m.prazo).slice(0,10) : ''}}
    ${{m.referencia ? '<br>ref: ' + esc(m.referencia) : ''}}</small></td></tr>`;
const cab = '<thead><tr><th>Estado</th><th>Quando</th><th>De → Para</th><th>Assunto e ação esperada</th></tr></thead>';
const tab = (id, lista, vazioTxt) => {{
  const el = document.getElementById(id);
  el.innerHTML = lista.length ? cab + '<tbody>' + lista.map(linha).join('') + '</tbody>' : '';
  if (!lista.length) el.outerHTML = `<p class="vazia">${{vazioTxt}}</p>`;
  return lista.length;
}};
const ms = (M.mensagens||[]).slice().sort((a,b)=> b.ts.localeCompare(a.ts));
const ativas = ms.filter(m => m.estado !== 'concluida' && !m.arquivada);
const conc   = ms.filter(m => m.estado === 'concluida' && !m.arquivada);
const arq    = ms.filter(m => m.arquivada);
document.getElementById('t-ativas').textContent = `Ativas (${{ativas.length}})`;
document.getElementById('t-conc').textContent = `Concluídas (${{conc.length}})`;
document.getElementById('t-arq').textContent = `Arquivadas (${{arq.length}})`;
tab('ativas', ativas, 'Sem mensagens ativas.');
tab('concluidas', conc, 'Nenhuma concluída ainda na caixa.');
tab('arquivadas', arq, 'Nada arquivado ainda.');
const locks = M.locks || [];
document.getElementById('locks').innerHTML = locks.length ? locks.map(l => `
  <p style="margin:.25rem 0">${{l.vencido ? '✕' : '●'}} <code>${{esc(l.superficie)}}</code>
   · dono ${{esc(l.dono)}} · ${{l.vencido ? 'vencido — quebrável' : 'renovado há ' + l.renovado_ha_min + ' min'}}</p>`).join('')
  : '<p class="vazia">Nenhuma superfície travada.</p>';
}})();
</script>
<style>
.estado{{display:inline-flex; gap:.35rem; align-items:center; white-space:nowrap; font-weight:600}}
.estado.aberta{{color:var(--atencao)}}
.estado.em-andamento{{color:var(--accent)}}
.estado.concluida{{color:var(--muted)}}
td.quando{{white-space:nowrap; color:var(--muted)}}
td.rota{{white-space:nowrap; font-weight:600}}
td.rota small{{display:block; font-weight:400; color:var(--muted)}}
td.assunto strong{{display:block}}
td.assunto small{{color:var(--muted)}}
</style>"""
    return body, script


# --------------------------------------------------------------------------
# Resultados (resultados.html) — stub de navegação nesta fatia; o conteúdo
# real (achados por pilar, entregas, experimentos) é a Fatia 2.
# --------------------------------------------------------------------------
def build_resultados() -> tuple[str, str]:
    body = """
<header class="page-head"><h1>Resultados</h1>
  <span class="meta">o que a tese já produziu</span></header>

<section class="card">
  <p class="vazia">Esta página chega na próxima entrega: achados por pilar
  (P1–P4) com evidência, entregas da tese (artigos, biblioteca, dataset,
  fichamentos) e a tabela de experimentos executados. A estrutura de
  navegação já está pronta — o conteúdo é preenchido a partir de
  <code>docs/records/resultados.json</code>.</p>
</section>
"""
    return body, ""


def main() -> None:
    pages = {
        "index.html": build_controle,
        "plano.html": build_plano,
        "mensagens.html": build_coordenacao,
        "resultados.html": build_resultados,
    }
    titles = {"index.html": "Controle", "plano.html": "Plano",
              "mensagens.html": "Coordenação", "resultados.html": "Resultados"}
    for fname, builder in pages.items():
        body, script = builder()
        html = page_shell(titles[fname], fname, FOOTER_TEXT, body, script)
        (out_dir / fname).write_text(html, encoding="utf-8")
    print(f"ok: {out_dir}/ (index, plano, mensagens, resultados)  "
          f"plano v{plano['versao']}, PGP {kpis.get('prontidao', {}).get('global_pct', '?')}%")


if __name__ == "__main__":
    main()
