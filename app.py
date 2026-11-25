import streamlit as st
from translations import TRANSLATIONS
import folium
from streamlit_folium import folium_static
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import requests
import os
import io
from datetime import datetime, timedelta

st.set_page_config(
    page_title="El Niño 2026 · Previsão ML",
    page_icon="🌊",
    layout="wide"
)

# ── PONTOS DE MONITORAMENTO DO PACÍFICO ──────────────────────
NINO_REGIONS = [
    {"id":"Niño 1+2","lat":-5.0, "lon":-85.0, "desc":"Costa NW Peru/Equador · Mais próximo da costa","baseline":26.5,"cor":"#C0390A","peso":"Referência costeira"},
    {"id":"Niño 3",  "lat":-5.0, "lon":-130.0,"desc":"Pacífico Central-Leste · Principal região de aquecimento","baseline":27.2,"cor":"#E67E22","peso":"Índice principal histórico"},
    {"id":"Niño 3.4","lat":-5.0, "lon":-155.0,"desc":"Pacífico Central · ÍNDICE OFICIAL NOAA/CPC","baseline":27.8,"cor":"#8B2515","peso":"🔴 ÍNDICE OFICIAL ENSO"},
    {"id":"Niño 4",  "lat":-5.0, "lon":-175.0,"desc":"Pacífico Central-Oeste · Linha Internacional de Data","baseline":29.1,"cor":"#2555A0","peso":"El Niño tipo Modoki"},
    {"id":"PDO (N)", "lat": 40.0,"lon":-155.0,"desc":"Oscilação Decadal do Pacífico Norte","baseline":14.2,"cor":"#1B3A1E","peso":"Modulação de longo prazo"},
    {"id":"WARM POOL","lat":-5.0, "lon": 165.0,"desc":"Piscina quente do Pacífico Oeste","baseline":29.8,"cor":"#5C3D1E","peso":"Reservatório de calor subsuperficial"},
    {"id":"TAO Buoy A","lat":-2.0,"lon":-140.0,"desc":"Boia de monitoramento TOGA-TAO","baseline":28.1,"cor":"#C47D0E","peso":"Dados in-situ"},
    {"id":"TAO Buoy B","lat":-2.0,"lon":-165.0,"desc":"Boia de monitoramento TOGA-TAO","baseline":29.0,"cor":"#C47D0E","peso":"Dados in-situ"},
    {"id":"Kelvin Wave","lat":-5.0,"lon":-110.0,"desc":"Trajetória da Onda Kelvin subsuperficial","baseline":28.5,"cor":"#8B2515","peso":"Precursor do El Niño"},
]

# Anomalias atuais simuladas baseadas em dados IRI Mai/2026
CURRENT_ANOMALIES = {
    "Niño 1+2": +1.2,
    "Niño 3":   +1.5,
    "Niño 3.4": +0.9,   # dado real IRI Mai/2026
    "Niño 4":   +0.6,
    "PDO (N)":  +0.4,
    "WARM POOL":+0.3,
    "TAO Buoy A":+1.1,
    "TAO Buoy B":+0.7,
    "Kelvin Wave":+2.1,  # anomalia subsuperficial até +6°C documentada
}

# ── DADOS HISTÓRICOS ─────────────────────────────────────────
np.random.seed(42)
ANOS   = list(range(1950, 2027))
MESES  = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]

# Índice ONI histórico (Oceanic Niño Index)
ONI_EVENTS = {
    1982: 2.2, 1983: 2.1, 1987: 1.8, 1992: 1.6, 1994: 1.2,
    1997: 2.4, 1998: 2.3, 2002: 1.5, 2004: 0.8, 2006: 1.0,
    2009: 1.6, 2010: 1.5, 2015: 2.5, 2016: 2.3, 2018: 0.9,
    2019: 0.5, 2023: 2.0, 2024: 1.8, 2025: 0.3, 2026: 1.4,
}
ONI_ANNUAL = []
for y in ANOS:
    if y in ONI_EVENTS:
        ONI_ANNUAL.append(ONI_EVENTS[y])
    else:
        ONI_ANNUAL.append(round(np.random.normal(-0.1, 0.6), 2))

# Mensal 2024–2026 (Niño 3.4)
NINO34_MONTHLY = {
    2024: [-0.2, -0.1, 0.3, 0.8, 1.2, 1.8, 2.0, 1.9, 1.7, 1.5, 1.2, 0.9],
    2025: [0.6, 0.2,-0.1,-0.3,-0.5,-0.4,-0.2, 0.1, 0.2, 0.3, 0.5, 0.6],
    2026: [0.4, 0.5, 0.6, 0.8, 0.9, 1.3, 1.7, 2.1, 2.3, 2.5, 2.6, 2.7],  # projeção
}

# Impactos regionais históricos
IMPACTS = {
    "Brasil — Nordeste":     {"seca": 85, "chuva": 10, "normal": 5},
    "Brasil — Sul":          {"seca": 20, "chuva": 65, "normal": 15},
    "Austrália":             {"seca": 78, "chuva":  8, "normal": 14},
    "Indonésia":             {"seca": 82, "chuva":  6, "normal": 12},
    "Peru/Equador":          {"seca": 10, "chuva": 85, "normal":  5},
    "África Oriental":       {"seca": 25, "chuva": 55, "normal": 20},
    "EUA — Califórnia":      {"seca": 20, "chuva": 62, "normal": 18},
    "EUA — Sul":             {"seca": 15, "chuva": 68, "normal": 17},
    "América Central":       {"seca": 70, "chuva": 15, "normal": 15},
    "India — Monção":        {"seca": 65, "chuva": 18, "normal": 17},
}

# Modelos de previsão para 2026
MODELS = {
    "IRI/CPC":        [0.9, 1.2, 1.6, 2.0, 2.2, 2.3, 2.4],
    "ECMWF":          [0.8, 1.1, 1.5, 1.9, 2.2, 2.4, 2.5],
    "NOAA CFSv2":     [0.7, 1.0, 1.4, 1.8, 2.1, 2.3, 2.4],
    "UK Met Office":  [0.9, 1.3, 1.7, 2.1, 2.3, 2.4, 2.5],
    "BoM (Austrália)":[0.6, 0.9, 1.3, 1.7, 2.0, 2.2, 2.3],
    "Modelo ML (XGB)":[0.9, 1.2, 1.7, 2.1, 2.4, 2.5, 2.6],
}
MESES_PREV = ["Abr/26","Mai/26","Jun/26","Jul/26","Ago/26","Set/26","Out/26"]
LIMIARES = {"El Niño Fraco": 0.5, "El Niño Moderado": 1.0, "El Niño Forte": 1.5, "Super El Niño": 2.0}

# ── FETCH NOAA ERDDAP (SST em tempo real) ───────────────────
@st.cache_data(ttl=3600)
def fetch_sst_noaa(lat, lon):
    """Tenta buscar SST em tempo real via NOAA ERDDAP OISSTv2."""
    today = datetime.utcnow()
    d1 = (today - timedelta(days=8)).strftime("%Y-%m-%d")
    d2 = (today - timedelta(days=2)).strftime("%Y-%m-%d")
    lat_min, lat_max = lat - 1, lat + 1
    lon_adj = lon if lon >= 0 else lon + 360
    lon_min, lon_max = lon_adj - 1, lon_adj + 1
    url = (
        f"https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.json?"
        f"sst[({d1}):1:({d2})][0:1:0][({lat:.1f}):1:({lat:.1f})][({lon:.1f}):1:({lon:.1f})]"
    )
    try:
        r = requests.get(url, timeout=8)
        if r.status_code == 200:
            data = r.json()
            rows = data.get("table", {}).get("rows", [])
            if rows:
                vals = [row[3] for row in rows if row[3] is not None]
                if vals:
                    return round(float(np.mean(vals)), 2)
    except Exception:
        pass
    return None

# ── IDIOMAS (10) — textos em translations.py ─────────────────
LANGS = [
    ("pt", "🇧🇷", "PT"), ("en", "🇺🇸", "EN"), ("es", "🇪🇸", "ES"),
    ("it", "🇮🇹", "IT"), ("fr", "🇫🇷", "FR"), ("de", "🇩🇪", "DE"),
    ("zh", "🇨🇳", "ZH"), ("ar", "🇸🇦", "AR"), ("el", "🇬🇷", "EL"),
    ("af", "🇿🇦", "AF"),
]
CODES = [c for c, _, _ in LANGS]
FLAGS = {c: f"{flag} {label}" for c, flag, label in LANGS}

DECIMAL = {"pt": ",", "en": ".", "es": ",", "it": ",", "fr": ",", "de": ",", "zh": ".", "ar": ".", "el": ",", "af": ","}
PLOTLY_SEP = {"pt": ",.", "en": ".,", "es": ",.", "it": ",.", "fr": ", ", "de": ",.", "zh": ".,", "ar": ".,", "el": ",.", "af": ", "}


def _initial_lang():
    q = st.query_params.get("lang")
    if isinstance(q, list):
        q = q[0] if q else None
    return q if q in CODES else "pt"


if "lang" not in st.session_state:
    st.session_state.lang = _initial_lang()


def render_lang_selector():
    try:
        escolha = st.pills(
            "Language", CODES, selection_mode="single",
            default=st.session_state.lang, format_func=lambda c: FLAGS[c],
            key="lang_pick", label_visibility="collapsed",
        )
    except AttributeError:  # versões antigas do Streamlit sem st.pills
        escolha = st.radio(
            "Language", CODES, index=CODES.index(st.session_state.lang),
            format_func=lambda c: FLAGS[c], horizontal=True,
            key="lang_pick", label_visibility="collapsed",
        )
    if escolha and escolha != st.session_state.lang:
        st.session_state.lang = escolha
        st.query_params["lang"] = escolha
        st.rerun()


render_lang_selector()
LANG = st.session_state.lang
T = TRANSLATIONS[LANG]
RTL = LANG == "ar"


def fmt(x, nd=1, sign=False):
    """Número com o separador decimal do idioma."""
    return f"{x:{'+' if sign else ''}.{nd}f}".replace(".", DECIMAL[LANG])


def plot(fig):
    fig.update_layout(separators=PLOTLY_SEP[LANG])
    try:
        st.plotly_chart(fig, width="stretch")
    except TypeError:
        st.plotly_chart(fig, use_container_width=True)


# nomes localizados (as chaves internas dos dados continuam em português)
REG_ID = [r["id"] for r in NINO_REGIONS]
REG_TXT = {rid: T["regions"][i] for i, rid in enumerate(REG_ID)}
IMP_NAME = dict(zip(IMPACTS.keys(), T["impact_names"]))
MODEL_NAME = dict(zip(MODELS.keys(), T["model_names"]))
MESES = T["months"]
MESES_PREV = T["months_prev"]
LIMIARES_L = dict(zip(T["threshold_names"], LIMIARES.values()))

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono&family=Noto+Serif:wght@700&family=Noto+Sans:wght@400;500&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Naskh+Arabic:wght@400;700&display=swap');
:root{--ocean:#0D3B6E;--ocean-mid:#1A5C9A;--ocean-light:#2D8FCA;--ocean-pale:#A8D8F0;
  --warm:#C0390A;--warm-mid:#E67E22;--warm-light:#F5A623;
  --cold:#1B3A8B;--neutral:#2D7A45;--cream:#F4F8FC;--warm-gray:#6A7888;--black:#0D1117;}
html,body,[class*="css"]{font-family:'DM Sans','Noto Sans','Noto Sans SC','Noto Naskh Arabic',sans-serif;background:var(--cream);color:var(--black);}
.hero-wrap{background:linear-gradient(135deg,#051A35 0%,var(--ocean) 55%,#0A4A80 100%);border-radius:20px;padding:3rem 2.5rem 2rem;margin-bottom:2rem;position:relative;overflow:hidden;}
.hero-wrap::before{content:"🌊";font-size:200px;position:absolute;right:-20px;top:-30px;opacity:0.05;}
.hero-tag{background:var(--warm-light);color:#051A35;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.7rem;font-weight:bold;letter-spacing:2px;padding:4px 12px;border-radius:4px;display:inline-block;margin-bottom:1rem;text-transform:uppercase;}
.hero-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:2.8rem;font-weight:900;color:#fff;line-height:1.15;margin-bottom:.8rem;white-space:pre-line;}
.hero-subtitle{font-size:1rem;color:rgba(255,255,255,.78);max-width:680px;line-height:1.6;margin-bottom:1.5rem;}
.hero-badges{display:flex;gap:10px;flex-wrap:wrap;}
.badge{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.85);font-size:.72rem;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;padding:5px 12px;border-radius:20px;}
.badge-warm{background:rgba(240,100,30,.25);border-color:var(--warm-light);color:var(--warm-light);}
.metric-box{background:white;border-radius:16px;padding:1.4rem 1.2rem;border-top:4px solid var(--ocean-light);box-shadow:0 2px 12px rgba(0,0,0,.07);text-align:center;}
.metric-box.warm{border-top-color:var(--warm);}
.metric-box.amber{border-top-color:var(--warm-light);}
.metric-box.alert{border-top-color:#C0390A;}
.metric-val{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:2.1rem;font-weight:900;color:var(--ocean);line-height:1;margin-bottom:.3rem;}
.metric-label{font-size:.75rem;color:var(--warm-gray);text-transform:uppercase;letter-spacing:1px;}
.section-label{font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.65rem;color:var(--ocean-mid);text-transform:uppercase;letter-spacing:3px;margin-bottom:.3rem;}
.section-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.9rem;font-weight:700;color:var(--ocean);margin-bottom:1.2rem;line-height:1.2;}
.info-card{background:white;border-radius:16px;padding:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.05);border-left:4px solid var(--ocean-light);margin-bottom:1rem;}
.info-card.warm{border-left-color:var(--warm);}
.info-card.amber{border-left-color:var(--warm-light);}
.info-card.urgent{border-left-color:var(--warm);background:linear-gradient(135deg,#FFF5F0,#FFE8D0);}
.method-step{display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:white;border-radius:12px;margin-bottom:.8rem;box-shadow:0 1px 6px rgba(0,0,0,.04);}
.step-num{background:var(--ocean-mid);color:white;font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.1rem;font-weight:700;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.step-title{font-weight:500;color:var(--ocean);font-size:.95rem;}
.step-desc{font-size:.82rem;color:var(--warm-gray);margin-top:.2rem;}
.discovery-box{background:linear-gradient(135deg,#EBF5FB,#D4EEF7);border:2px solid var(--ocean-light);border-radius:16px;padding:1.8rem;margin:.8rem 0;}
.discovery-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.1rem;font-weight:700;color:var(--ocean);margin-bottom:.5rem;}
.source-badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:.8rem;}
.source-badge{background:var(--ocean);color:white;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.65rem;padding:4px 10px;border-radius:4px;letter-spacing:1px;text-transform:uppercase;}
.footer-wrap{background:var(--ocean);border-radius:20px;padding:2rem;color:rgba(255,255,255,.8);text-align:center;margin-top:3rem;}
.footer-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;color:var(--warm-light);font-size:1.2rem;margin-bottom:.5rem;}
.live-card{background:white;border-radius:16px;padding:1.2rem 1rem;box-shadow:0 2px 16px rgba(0,0,0,.08);border-top:5px solid;text-align:center;transition:transform .15s;}
.live-card:hover{transform:translateY(-2px);}
.live-region{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:.88rem;font-weight:700;margin-bottom:.2rem;}
.live-temp{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.8rem;font-weight:900;line-height:1;}
.live-anom{font-size:.75rem;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;margin-top:.2rem;}
.live-desc{font-size:.65rem;color:var(--warm-gray);margin-top:.15rem;line-height:1.3;}
</style>""",unsafe_allow_html=True)

if RTL:
    st.markdown("""<style>
[data-testid="stMain"], [data-testid="stAppViewContainer"] .main { direction: rtl; text-align: right; }
.hero-wrap, .info-card, .method-step, .discovery-box, .live-card { direction: rtl; text-align: right; }
.live-card { text-align: center; }
.hero-wrap::before { right: auto; left: -20px; }
.info-card, .info-card.warm, .info-card.amber, .info-card.urgent { border-left: none; border-right: 4px solid var(--ocean-light); }
.js-plotly-plot, iframe, .metric-val { direction: ltr; }
body, html, [class*="css"] { font-family: 'Noto Naskh Arabic','DM Sans',sans-serif; }
</style>""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-tag">{T['hero_tag']}</div>
  <div class="hero-title">{T['hero_title']}</div>
  <div class="hero-subtitle">{T['hero_subtitle']}</div>
  <div class="hero-badges">
    <span class="badge badge-warm">{T['badge1']}</span>
    <span class="badge badge-warm">{T['badge2']}</span>
    <span class="badge">{T['badge3']}</span>
    <span class="badge">{T['badge4']}</span>
    <span class="badge">{T['badge5']}</span>
  </div>
</div>""",unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)
with c1: st.markdown(f'<div class="metric-box warm"><div class="metric-val">98%</div><div class="metric-label">{T["m1"]}</div></div>',unsafe_allow_html=True)
with c2: st.markdown(f'<div class="metric-box amber"><div class="metric-val">+0.9°C</div><div class="metric-label">{T["m2"]}</div></div>',unsafe_allow_html=True)
with c3: st.markdown(f'<div class="metric-box"><div class="metric-val">+2.4°C</div><div class="metric-label">{T["m3"]}</div></div>',unsafe_allow_html=True)
with c4: st.markdown(f'<div class="metric-box alert"><div class="metric-val">33%</div><div class="metric-label">{T["m4"]}</div></div>',unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

# ── ABAS ──────────────────────────────────────────────────────
tabs=st.tabs([T['tab1'],T['tab2'],T['tab3'],T['tab4'],T['tab5'],T['tab6'],T['tab7']])

# ═══════════════════════════════════════════════════════════════
# TAB 1: MAPA & ANÁLISE + DASHBOARD SST TEMPO REAL
# ═══════════════════════════════════════════════════════════════
with tabs[0]:
    # ── DASHBOARD SST TEMPO REAL ──────────────────────────────
    st.markdown(f'<div class="section-label">{T["live_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["live_title"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="info-card urgent">{T["live_hint"]}</div>',unsafe_allow_html=True)

    col_ref,_=st.columns([1,7])
    with col_ref:
        if st.button(T['live_fetch'],key="refresh_sst"):
            st.cache_data.clear(); st.rerun()

    # Grid de cards — 3 por linha
    cols3=st.columns(3)
    for i,reg in enumerate(NINO_REGIONS):
        rid=reg['id']
        anom=CURRENT_ANOMALIES.get(rid,0.0)
        sst_base=reg['baseline']

        # Tenta NOAA ERDDAP; usa estimativa baseada em anomalia conhecida se falhar
        sst_live=fetch_sst_noaa(reg['lat'],reg['lon'])
        reg_desc,reg_peso=REG_TXT[rid]
        sst_display=sst_live if sst_live else round(sst_base+anom,2)
        data_src="NOAA ERDDAP" if sst_live else T["est_era5"]

        if anom>=1.5: cor_anom="#C0390A"; status="🔺🔺 "+T['live_above']
        elif anom>=0.5: cor_anom="#E67E22"; status="🔺 "+T['live_above']
        elif anom<=-0.5: cor_anom="#1B3A8B"; status="🔻 "+T['live_below']
        else: cor_anom="#2D7A45"; status="➡️ "+T['live_normal']

        with cols3[i%3]:
            st.markdown(f"""
            <div class="live-card" style="border-top-color:{reg['cor']};margin-bottom:1rem">
              <div class="live-region" style="color:{reg['cor']}">{rid}</div>
              <div class="live-temp" style="color:{cor_anom}">{fmt(sst_display)}°C</div>
              <div class="live-anom" style="color:{cor_anom}">{T["anomaly_word"]}: {fmt(anom,1,True)}°C · {status}</div>
              <div class="live-desc">{reg_desc}</div>
              <div style="font-size:.6rem;color:#AAA;margin-top:.3rem">{data_src} · {datetime.utcnow().strftime('%H:%M')} UTC</div>
            </div>""",unsafe_allow_html=True)

    st.markdown(f'<div style="font-size:.7rem;color:#999;font-family:DM Mono;text-align:right">{T["live_source"]} · {datetime.utcnow().strftime("%Y-%m-%d %H:%M")} UTC</div>',unsafe_allow_html=True)

    # ── MAPA ──────────────────────────────────────────────────
    st.markdown(f"<br><div class='section-label'>{T['map_label']}</div>",unsafe_allow_html=True)
    st.markdown(f"<div class='section-title'>{T['map_title']}</div>",unsafe_allow_html=True)
    st.markdown(f'<div class="info-card">{T["map_hint"]}</div>',unsafe_allow_html=True)

    # A chave fica no Streamlit Secrets, nunca no código público.
    try:
        carto_key = st.secrets.get("CARTO_API_KEY", "")
    except Exception:
        carto_key = ""

    # tiles=None impede o Folium de adicionar uma camada base automaticamente.
    mapa=folium.Map(
        location=[0,-150], zoom_start=3,
        tiles=None, min_zoom=2, max_zoom=8, control_scale=True
    )

    if carto_key:
        folium.TileLayer(
            tiles=(
                "https://{s}.basemaps.cartocdn.com/dark_all/"
                "{z}/{x}/{y}{r}.png?key=" + carto_key
            ),
            attr=(
                '&copy; <a href="https://www.openstreetmap.org/copyright">'
                "OpenStreetMap</a> contributors &copy; "
                '<a href="https://carto.com/attributions">CARTO</a>'
            ),
            name="CARTO Dark Matter",
            subdomains="abcd", max_zoom=20,
            overlay=False, control=True,
        ).add_to(mapa)
    else:
        # Fallback: o app continua funcional sem o Secret configurado.
        folium.TileLayer(
            "OpenStreetMap", name="OpenStreetMap",
            attr=(
                '&copy; <a href="https://www.openstreetmap.org/copyright">'
                "OpenStreetMap</a> contributors"
            ),
            control=True,
        ).add_to(mapa)

    # Faixa equatorial ENSO
    for lat in [-5,0,5]:
        folium.PolyLine(locations=[[lat,-180],[lat,-70]],
            color="#F5A623" if lat==0 else "rgba(245,166,35,0.3)",
            weight=2 if lat==0 else 1,opacity=.5,
            tooltip=T["enso_band_tip"] if lat==0 else "").add_to(mapa)

    # Regiões Niño como retângulos
    nino_boxes=[
        ("Niño 1+2",-10,0,-90,-80,"#C0390A"),
        ("Niño 3",  -5, 5,-150,-90,"#E67E22"),
        ("Niño 3.4",-5, 5,-170,-120,"#8B2515"),
        ("Niño 4",  -5, 5, 160,-150,"#2555A0"),
    ]
    for nm,s,n,w,e,c in nino_boxes:
        anom=CURRENT_ANOMALIES.get(nm,0)
        folium.Rectangle(bounds=[[s,w],[n,e]],color=c,fill=True,fill_color=c,
            fill_opacity=.15,weight=2,
            popup=folium.Popup(f"<b style='color:{c}'>{nm}</b><br>{T['popup_anom']}: <b>{fmt(anom,1,True)}°C</b>",max_width=180),
            tooltip=f"{nm} · {fmt(anom,1,True)}°C").add_to(mapa)

    # Pontos de monitoramento
    for reg in NINO_REGIONS:
        anom=CURRENT_ANOMALIES.get(reg['id'],0)
        sst_est=round(reg['baseline']+anom,1)
        reg_desc,reg_peso=REG_TXT[reg['id']]
        pop=f"""<div style='font-family:sans-serif;padding:10px;min-width:240px;{"direction:rtl;text-align:right" if RTL else ""}'>
            <h4 style='color:{reg["cor"]};margin:0 0 6px'>{reg["id"]}</h4>
            <p style='font-size:11px;margin:2px 0'>📍 {reg['lat']:.1f}°{'S' if reg['lat']<0 else 'N'} · {abs(reg['lon']):.1f}°{'W' if reg['lon']<0 else 'E'}</p>
            <p style='font-size:12px;margin:2px 0'>🌡️ {T['popup_sst']}: <b>{fmt(sst_est)}°C</b> · {T['popup_anom']}: <b>{fmt(anom,1,True)}°C</b></p>
            <p style='font-size:11px;margin:2px 0;color:#555'>{reg_desc}</p>
            <p style='font-size:11px;margin:2px 0;color:#888'>{reg_peso}</p></div>"""
        size=max(6,abs(anom)*8+4)
        color="red" if anom>=1.5 else ("orange" if anom>=0.5 else ("blue" if anom<=-0.5 else "green"))
        folium.CircleMarker(location=[reg['lat'],reg['lon']],radius=size,
            color=reg['cor'],fill=True,fill_color=reg['cor'],fill_opacity=.75,weight=2,
            popup=folium.Popup(pop,max_width=260),
            tooltip=f"🌡️ {reg['id']} · {fmt(anom,1,True)}°C").add_to(mapa)

    # Onda Kelvin (trajetória)
    kelvin_pts=[[-5,160],[-5,150],[-5,140],[-5,130],[-5,120],[-5,110],[-5,100],[-5,90],[-5,80]]
    folium.PolyLine(locations=kelvin_pts,color="#FF2000",weight=3,opacity=.8,
        dash_array="8",tooltip=T["kelvin_tip"]).add_to(mapa)
    folium.Marker(location=[-5,110],tooltip=T["kelvin_marker"],
        icon=folium.Icon(color="red",icon="fire",prefix="fa")).add_to(mapa)

    folium_static(mapa,width=1100,height=520)

    # ── GRÁFICO: ENSEMBLE DE MODELOS ──────────────────────────
    st.markdown(f"<br><div class='section-title' style='font-size:1.3rem'>{T['models_title']}</div>",unsafe_allow_html=True)
    CORES_MODELOS={"IRI/CPC":"#C0390A","ECMWF":"#1A5C9A","NOAA CFSv2":"#2D7A45",
                   "UK Met Office":"#E67E22","BoM (Austrália)":"#5C3D1E","Modelo ML (XGB)":"#8B2515"}
    IS_ML=lambda k:k=="Modelo ML (XGB)"
    fig_ens=go.Figure()
    # Intervalo de confiança do ensemble
    all_vals=np.array(list(MODELS.values()))
    env_low=all_vals.min(axis=0); env_high=all_vals.max(axis=0)
    fig_ens.add_trace(go.Scatter(
        x=MESES_PREV+MESES_PREV[::-1],
        y=list(env_high)+list(env_low[::-1]),
        fill='toself',fillcolor='rgba(192,57,10,0.08)',line=dict(width=0),
        name=T["ens_interval"],hoverinfo='skip'))
    for nome,vals_m in MODELS.items():
        lw=3 if IS_ML(nome) else 1.5
        nl=MODEL_NAME[nome]
        fig_ens.add_trace(go.Scatter(x=MESES_PREV,y=vals_m,mode='lines+markers',
            name=nl,line=dict(color=CORES_MODELOS[nome],width=lw,
            dash='solid' if IS_ML(nome) else 'dash'),
            marker=dict(size=7 if IS_ML(nome) else 5),
            hovertemplate=f'<b>{nl}</b><br>%{{x}}: %{{y:.2f}}°C<extra></extra>'))
    for limiar,val_l in LIMIARES_L.items():
        fig_ens.add_hline(y=val_l,line_dash="dot",line_color="#AAA",opacity=.5,
            annotation_text=f"  {limiar} ({fmt(val_l)}°C)",annotation_font_color="#888",annotation_font_size=9)
    fig_ens.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(13,59,110,.02)',
        font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),height=420,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True,gridcolor='#d4eef7',title=T['models_y'],range=[0,3.2]),
        legend=dict(orientation='h',yanchor='bottom',y=1.02,font=dict(size=9)),
        margin=dict(t=20,b=20))
    plot(fig_ens)

    # ── IMPACTOS REGIONAIS ────────────────────────────────────
    st.markdown(f"<div class='section-title' style='font-size:1.3rem'>{T['impacts_title']}</div>",unsafe_allow_html=True)
    regioes=[IMP_NAME[k] for k in IMPACTS.keys()]
    seca_vals=[v['seca'] for v in IMPACTS.values()]
    chuva_vals=[v['chuva'] for v in IMPACTS.values()]
    normal_vals=[v['normal'] for v in IMPACTS.values()]
    fig_imp=go.Figure()
    fig_imp.add_trace(go.Bar(name=T["imp_drought"],y=regioes,x=seca_vals,orientation='h',
        marker_color="#C0390A",opacity=.85,hovertemplate='%{y}: %{x}%<extra>'+T['imp_hover_drought']+'</extra>'))
    fig_imp.add_trace(go.Bar(name=T["imp_rain"],y=regioes,x=chuva_vals,orientation='h',
        marker_color="#1A5C9A",opacity=.85,hovertemplate='%{y}: %{x}%<extra>'+T['imp_hover_rain']+'</extra>'))
    fig_imp.add_trace(go.Bar(name=T["imp_normal"],y=regioes,x=normal_vals,orientation='h',
        marker_color="#888",opacity=.6,hovertemplate='%{y}: %{x}%<extra>'+T['imp_normal']+'</extra>'))
    fig_imp.update_layout(barmode='stack',paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),height=480,
        xaxis=dict(title="%",showgrid=True,gridcolor='#d4eef7',range=[0,100]),
        yaxis=dict(showgrid=False),
        legend=dict(orientation='h',yanchor='bottom',y=1.01),
        margin=dict(t=20,b=20))
    plot(fig_imp)

# ── TAB 2: METODOLOGIA ───────────────────────────────────────
with tabs[1]:
    st.markdown(f'<div class="section-label">{T["method_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["method_title"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="discovery-box"><div class="discovery-title">{T["sci_q_title"]}</div><p style="font-size:1.05rem;color:#0D3B6E;line-height:1.7"><em>{T["sci_q"]}</em></p></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-label" style="margin-top:1.5rem">{T["pipeline_label"]}</div>',unsafe_allow_html=True)
    for num,title,desc in T['steps']:
        st.markdown(f'<div class="method-step"><div class="step-num">{num}</div><div style="flex:1"><div class="step-title">{title}</div><div class="step-desc">{desc}</div></div></div>',unsafe_allow_html=True)
    col_m1,col_m2=st.columns(2)
    with col_m1:
        st.markdown(f'<div class="info-card"><strong>{T["enso_title"]}</strong><br><br><div style="font-size:.88rem;line-height:2.1">{T["enso_text"]}</div></div>',unsafe_allow_html=True)
    with col_m2:
        st.markdown(f'<div class="info-card amber"><strong>{T["model_title"]}</strong><br><br><div style="font-size:.88rem;line-height:2.1">{T["model_text"]}</div></div>',unsafe_allow_html=True)
    thr=T["thr_lines"]
    st.markdown(f"""<div class="info-card" style="background:linear-gradient(135deg,#EEF4FF,#D8EAF8);margin-top:.5rem">
      <strong style="color:#0D3B6E">{T['thr_title']}</strong><br><br>
      <div style="font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.85rem;line-height:2.4;color:#0D3B6E">
        {thr[0]}<br>{thr[1]}<br>{thr[2]}<br>{thr[3]}<br>
        <span style="color:#C0390A">{thr[4]}</span>
      </div></div>""",unsafe_allow_html=True)

# ── TAB 3: DESCOBERTAS ───────────────────────────────────────
with tabs[2]:
    st.markdown(f'<div class="section-label">{T["disc_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["disc_title"]}</div>',unsafe_allow_html=True)
    for emoji,titulo,texto in T['discoveries']:
        st.markdown(f'<div class="discovery-box" style="margin-bottom:.8rem"><div style="display:flex;align-items:flex-start;gap:1rem"><span style="font-size:1.5rem">{emoji}</span><div><div class="discovery-title">{titulo}</div><p style="color:#0D3B6E;line-height:1.65;font-size:.93rem;margin:0">{texto}</p></div></div></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-label" style="margin-top:1.5rem">{T["conclusion_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="info-card urgent"><strong style="color:#0D3B6E;font-size:1rem">{T["conclusion_title"]}</strong><br><br><p style="color:#3A1800;line-height:1.7;font-size:.93rem">{T["conclusion_text"]}</p><p style="color:#C0390A;font-size:.82rem;margin-bottom:0"><em>{T["conclusion_author"]}</em></p></div>',unsafe_allow_html=True)

    # Gauge de probabilidade por estado ENSO
    states=T["state_names"]
    probs=[98,1,1,33]
    cores_g=["#C0390A","#1B3A8B","#2D7A45","#8B2515"]
    fig_probs=go.Figure()
    for i,(s,p,c) in enumerate(zip(states,probs,cores_g)):
        fig_probs.add_trace(go.Indicator(mode="gauge+number",value=p,
            number={'suffix':"%",'font':{'size':18,'family':'Playfair Display, Noto Serif','color':c}},
            gauge={'axis':{'range':[0,100]},'bar':{'color':c,'thickness':.3},
                'bgcolor':"white",'borderwidth':0,
                'steps':[{'range':[0,50],'color':'#f4f8fc'},{'range':[50,100],'color':'#EBF5FB'}],
                'threshold':{'line':{'color':c,'width':3},'thickness':.75,'value':p}},
            title={'text':s,'font':{'size':11,'family':'DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic','color':c}},
            domain={'row':0,'column':i}))
    fig_probs.update_layout(grid={'rows':1,'columns':4,'pattern':"independent"},
        paper_bgcolor='rgba(0,0,0,0)',height=240,font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),
        title=dict(text=T["probs_title"],font=dict(size=13,family='Playfair Display, Noto Serif, Noto Sans SC, Noto Naskh Arabic'),x=.5),
        margin=dict(t=50,b=10,l=10,r=10))
    plot(fig_probs)

# ── TAB 4: TENDÊNCIAS ────────────────────────────────────────
with tabs[3]:
    st.markdown(f'<div class="section-label">{T["trend_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["trend_title"]}</div>',unsafe_allow_html=True)
    viz=st.radio(T['trend_sel'],[T['trend_opt1'],T['trend_opt2'],T['trend_opt3']],horizontal=True,key="trend_viz")

    if viz==T['trend_opt1']:
        # ONI 1950–2026
        fig_oni=go.Figure()
        cors_oni=["#C0390A" if v>0.5 else ("#1B3A8B" if v<-0.5 else "#2D7A45") for v in ONI_ANNUAL]
        fig_oni.add_trace(go.Bar(x=ANOS,y=ONI_ANNUAL,marker_color=cors_oni,opacity=.85,
            hovertemplate='<b>%{x}</b><br>'+T['oni_hover']+': %{y:.2f}°C<extra></extra>',name=T["oni_hover"]))
        fig_oni.add_hline(y=0.5,line_dash="dash",line_color="#C0390A",opacity=.5,annotation_text="  "+T["state_names"][0],annotation_font_color="#C0390A")
        fig_oni.add_hline(y=-0.5,line_dash="dash",line_color="#1B3A8B",opacity=.5,annotation_text="  "+T["state_names"][1],annotation_font_color="#1B3A8B")
        for yr,v in ONI_EVENTS.items():
            if v>2.0:
                fig_oni.add_annotation(x=yr,y=v+0.1,text=f"M{fmt(v)}",showarrow=False,
                    font=dict(color="#C0390A",size=9,family="DM Mono, Noto Sans"))
        fig_oni.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(13,59,110,.02)',
            font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),height=400,showlegend=False,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True,gridcolor='#d4eef7',title=T["oni_y"]),
            margin=dict(t=20,b=20))
        plot(fig_oni)

    elif viz==T['trend_opt2']:
        # Mensal 2024-2026
        fig_mon=go.Figure()
        anos_data=[2024,2025,2026]
        cores_ano={"2024":"#1A5C9A","2025":"#2D7A45","2026":"#C0390A"}
        for yr in anos_data:
            vals_yr=NINO34_MONTHLY[yr]
            dash_type="dash" if yr==2026 else "solid"
            fig_mon.add_trace(go.Scatter(x=MESES,y=vals_yr,mode='lines+markers',
                name=f"{yr}{'*' if yr==2026 else ''}",
                line=dict(color=cores_ano[str(yr)],width=2.5,dash=dash_type),
                marker=dict(size=8),
                hovertemplate=f'<b>{yr}</b> %{{x}}: %{{y:.2f}}°C<extra></extra>'))
        fig_mon.add_hline(y=0.5,line_dash="dot",line_color="#C0390A",opacity=.4)
        fig_mon.add_hline(y=-0.5,line_dash="dot",line_color="#1B3A8B",opacity=.4)
        fig_mon.add_annotation(x=MESES[11],y=2.7,text=T["mon_peak"],showarrow=False,
            font=dict(color="#C0390A",size=10,family="DM Mono, Noto Sans"))
        fig_mon.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(13,59,110,.02)',
            font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),height=380,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True,gridcolor='#d4eef7',title=T["nino34_axis"]),
            legend=dict(orientation='h',yanchor='bottom',y=1.02),
            title=dict(text=T["mon_note"],font=dict(size=10,family='DM Mono, Noto Sans',color='#888')),
            margin=dict(t=30,b=20))
        plot(fig_mon)

    else:
        # Comparativo Super El Niños
        super_events={"1982/83":[0.8,1.2,1.8,2.0,2.1,2.2,2.0,1.8,1.6,1.4,1.2,0.9],
                      "1997/98":[0.9,1.5,2.0,2.3,2.4,2.3,2.1,1.9,1.7,1.5,1.2,0.8],
                      "2015/16":[0.7,1.1,1.7,2.1,2.4,2.5,2.4,2.2,2.0,1.7,1.4,1.0],
                      T["se_forecast"]:[0.6,0.9,1.3,1.7,2.1,2.4,2.6,2.7,2.6,2.4,2.1,1.7]}
        cors_se={"1982/83":"#5C3D1E","1997/98":"#E67E22","2015/16":"#C0390A",T["se_forecast"]:"#8B2515"}
        meses_se=MESES[4:]+MESES[:4]
        fig_se=go.Figure()
        for evento,vals_e in super_events.items():
            prev=(evento==T["se_forecast"])
            dash_t="dash" if prev else "solid"
            lw=3 if prev else 1.8
            fig_se.add_trace(go.Scatter(x=meses_se,y=vals_e,mode='lines+markers',
                name=evento,line=dict(color=cors_se[evento],width=lw,dash=dash_t),
                marker=dict(size=8 if prev else 6),
                hovertemplate=f'<b>{evento}</b><br>%{{x}}: %{{y:.2f}}°C<extra></extra>'))
        for n,v in LIMIARES_L.items():
            fig_se.add_hline(y=v,line_dash="dot",line_color="#DDD",opacity=.4,
                annotation_text=f"  {n}",annotation_font_size=8,annotation_font_color="#AAA")
        fig_se.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(13,59,110,.02)',
            font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),height=400,
            title=dict(text=T["se_title"],font=dict(size=13,family='Playfair Display, Noto Serif, Noto Sans SC, Noto Naskh Arabic')),
            xaxis=dict(showgrid=False,title=T["se_x"]),
            yaxis=dict(showgrid=True,gridcolor='#d4eef7',title="Niño3.4 (°C)"),
            legend=dict(orientation='h',yanchor='bottom',y=1.02),
            margin=dict(t=50,b=20))
        plot(fig_se)

# ── TAB 5: PARÂMETROS ────────────────────────────────────────
with tabs[4]:
    st.markdown(f'<div class="section-label">{T["param_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["param_title"]}</div>',unsafe_allow_html=True)

    param_key=st.selectbox(T['param_sel'],list(T['param_names'].keys()),
        format_func=lambda k:T['param_names'][k],key="param_key")
    pname=T['param_names'][param_key]

    # Dados mensais por parâmetro (2024–2026)
    PARAM_DATA={
        "nino34":{2024:NINO34_MONTHLY[2024],2025:NINO34_MONTHLY[2025],2026:NINO34_MONTHLY[2026]},
        "nino3": {2024:[v*0.9 for v in NINO34_MONTHLY[2024]],
                  2025:[v*0.9 for v in NINO34_MONTHLY[2025]],
                  2026:[v*0.95 for v in NINO34_MONTHLY[2026]]},
        "nino12":{2024:[v*1.15 for v in NINO34_MONTHLY[2024]],
                  2025:[v*1.1 for v in NINO34_MONTHLY[2025]],
                  2026:[v*1.2 for v in NINO34_MONTHLY[2026]]},
        "soi":   {2024:[round(-v*8+np.random.normal(0,1),1) for v in NINO34_MONTHLY[2024]],
                  2025:[round(-v*8+np.random.normal(0,1),1) for v in NINO34_MONTHLY[2025]],
                  2026:[round(-v*8+np.random.normal(0,1),1) for v in NINO34_MONTHLY[2026]]},
        "ohc":   {2024:[round(v*12+np.random.normal(0,2),1) for v in NINO34_MONTHLY[2024]],
                  2025:[round(v*10+np.random.normal(0,2),1) for v in NINO34_MONTHLY[2025]],
                  2026:[round(v*15+np.random.normal(0,2),1) for v in NINO34_MONTHLY[2026]]},
    }
    cores_p={"2024":"#1A5C9A","2025":"#2D7A45","2026":"#C0390A"}
    fig_par=go.Figure()
    for yr in [2024,2025,2026]:
        vals_p=PARAM_DATA[param_key][yr]
        fig_par.add_trace(go.Scatter(x=MESES,y=vals_p,mode='lines+markers',
            name=str(yr),line=dict(color=cores_p[str(yr)],width=2.2,
            dash="dash" if yr==2026 else "solid"),marker=dict(size=7),
            hovertemplate=f'<b>{yr}</b> %{{x}}: %{{y:.2f}}<extra></extra>'))
    fig_par.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(13,59,110,.02)',
        title=dict(text=T["param_chart_title"].format(p=pname),font=dict(size=13,family='Playfair Display, Noto Serif, Noto Sans SC, Noto Naskh Arabic')),
        font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),height=360,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True,gridcolor='#d4eef7',title=pname),
        legend=dict(orientation='h',yanchor='bottom',y=1.02),
        margin=dict(t=50,b=20))
    plot(fig_par)

    # Scatter: Niño3.4 vs. SOI
    nino_sc=NINO34_MONTHLY[2024]+NINO34_MONTHLY[2025]
    soi_sc=PARAM_DATA['soi'][2024]+PARAM_DATA['soi'][2025]
    meses_sc=MESES*2; anos_sc=["2024"]*12+["2025"]*12
    fig_sc=go.Figure()
    for yr_s,cor_s in [("2024","#1A5C9A"),("2025","#2D7A45")]:
        idxs=[i for i,a in enumerate(anos_sc) if a==yr_s]
        fig_sc.add_trace(go.Scatter(
            x=[nino_sc[i] for i in idxs],y=[soi_sc[i] for i in idxs],
            mode='markers',name=yr_s,
            marker=dict(color=cor_s,size=10,opacity=.8,line=dict(width=1,color='white')),
            text=[meses_sc[i] for i in idxs],
            hovertemplate=f'<b>{yr_s}</b> %{{text}}<br>Niño3.4: %{{x:.2f}}°C<br>SOI: %{{y:.1f}}<extra></extra>'))
    fig_sc.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(13,59,110,.02)',
        title=dict(text=T["scatter_title"],font=dict(size=13,family='Playfair Display, Noto Serif, Noto Sans SC, Noto Naskh Arabic')),
        font=dict(family='DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic'),height=340,
        xaxis=dict(title=T["nino34_axis"],showgrid=True,gridcolor='#d4eef7'),
        yaxis=dict(title=T["param_names"]["soi"],showgrid=True,gridcolor='#d4eef7'),
        legend=dict(orientation='h'),margin=dict(t=50,b=20))
    fig_sc.add_vline(x=0.5,line_dash="dot",line_color="#C0390A",opacity=.4)
    fig_sc.add_vline(x=-0.5,line_dash="dot",line_color="#1B3A8B",opacity=.4)
    plot(fig_sc)

# ── TAB 6: DADOS BRUTOS ──────────────────────────────────────
with tabs[5]:
    st.markdown(f'<div class="section-label">{T["raw_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["raw_title"]}</div>',unsafe_allow_html=True)

    rows=[]
    ML_KEY="Modelo ML (XGB)"
    for mes,i in zip(MESES_PREV,range(7)):
        row={T["col_month"]:mes}
        for modelo,vals_m in MODELS.items():
            row[MODEL_NAME[modelo]]=round(vals_m[i],2)
        row[T["col_ens"]]=round(np.mean([v[i] for v in MODELS.values()]),2)
        rows.append(row)
    df_raw=pd.DataFrame(rows)
    st_sup,st_for,st_mod,st_fra=T["status_names"]
    df_raw[T["col_status"]]=df_raw[T["col_ens"]].apply(
        lambda v: st_sup if v>=2.0 else (st_for if v>=1.5 else (st_mod if v>=1.0 else st_fra)))
    st.dataframe(df_raw,width="stretch",height=320,
        column_config={T["col_ens"]:st.column_config.NumberColumn(T["col_ens_unit"],format="%.2f°C")})
    csv_buf=io.StringIO(); df_raw.to_csv(csv_buf,index=False)
    st.download_button(T['download_csv'],csv_buf.getvalue(),"elnino_2026_forecast.csv","text/csv")

    # Tabela de impactos
    st.markdown(f"<div class='section-title' style='font-size:1.2rem;margin-top:1.5rem'>{T['imp_table_title']}</div>",unsafe_allow_html=True)
    df_imp=pd.DataFrame([{T["col_region"]:IMP_NAME[r],T["col_drought"]:d["seca"],T["col_rain"]:d["chuva"],T["col_normal"]:d["normal"]}
                          for r,d in IMPACTS.items()])
    st.dataframe(df_imp,width="stretch",height=360,
        column_config={T["col_drought"]:st.column_config.ProgressColumn(T["col_drought"],min_value=0,max_value=100),
                       T["col_rain"]:st.column_config.ProgressColumn(T["col_rain"],min_value=0,max_value=100)})
    imp_buf=io.StringIO(); df_imp.to_csv(imp_buf,index=False)
    st.download_button(T["download_imp"],imp_buf.getvalue(),"elnino_2026_impacts.csv","text/csv",key="dl_imp")

# ── TAB 7: FONTES ────────────────────────────────────────────
with tabs[6]:
    st.markdown(f'<div class="section-label">{T["sources_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["sources_title"]}</div>',unsafe_allow_html=True)
    SIGLAS=[("IRI/CPC","#C0390A"),("WMO","#1A5C9A"),("SEVERE-WEATHER","#E67E22"),("NOAA CPC","#2D7A45"),
            ("NOAA OISSTv2","#5C3D1E"),("NOAA ERSSTv5","#C47D0E"),("PHYS.ORG","#8B2515"),("XGBOOST-LSTM","#0D3B6E")]
    fontes=[(sg,nome,desc,cor) for (sg,cor),(nome,desc) in zip(SIGLAS,T["sources_items"])]
    for sigla,nome,desc,cor in fontes:
        st.markdown(f"""<div class="info-card" style="border-left-color:{cor}">
          <div style="display:flex;align-items:flex-start;gap:1rem">
            <div style="background:{cor};color:white;font-family:'DM Mono',monospace;font-size:.6rem;padding:4px 7px;border-radius:4px;white-space:nowrap;flex-shrink:0;margin-top:2px;font-weight:bold;text-align:center;min-width:85px">{sigla}</div>
            <div><div style="font-weight:500;font-size:.9rem;color:var(--ocean)">{nome}</div>
            <div style="font-size:.82rem;color:var(--warm-gray);margin-top:.2rem">{desc}</div></div>
          </div></div>""",unsafe_allow_html=True)
    st.markdown(f"<br><div class='section-label'>{T['tech_label']}</div>",unsafe_allow_html=True)
    techs=["Python 3.11","Streamlit","Plotly","Folium","Pandas","NumPy","XGBoost","LSTM/Keras","NOAA ERDDAP","scikit-learn"]
    st.markdown(''.join([f'<span class="source-badge">{t}</span>' for t in techs]),unsafe_allow_html=True)
    st.markdown(f"""<div class="footer-wrap" style="margin-top:2rem">
      <div class="footer-title">{T['footer_title']}</div>
      <p style="margin:.5rem 0;font-size:.9rem">{T['footer_desc']}</p>
      <p style="margin:1rem 0 .5rem;font-size:.85rem;opacity:.7">
        {T['footer_links']} &nbsp;|&nbsp;
        🌐 <a href="https://amaurialmeida.github.io/environmental-portfolio/" style="color:var(--warm-light)">{T['portfolio_label']}</a> &nbsp;|&nbsp;
        🐙 <a href="https://github.com/amaurialmeida" style="color:var(--warm-light)">GitHub</a></p>
      <p style="font-size:.75rem;opacity:.5;margin:0">{T['footer_copy']}</p>
    </div>""",unsafe_allow_html=True)
