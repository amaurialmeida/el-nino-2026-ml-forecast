# 🌊 El Niño 2026 — ML Impact Forecast

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?logo=streamlit&logoColor=white)](https://el-nino-2026-ml-forecast.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: Academic](https://img.shields.io/badge/License-Academic-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

🌐 **Languages:** English | [Português](README.pt-BR.md) | [Español](README.es.md)

**Applied Data Science — Machine Learning Climate Forecasting**
Fernandópolis, SP, Brazil · May 2026
**Author:** Amauri Almeida de Souza Junior

---

## ❓ Project Question

> "Could the 2026 El Niño become one of the strongest events of the modern instrumental record, and which regions of the planet would face the most severe impacts on precipitation, temperature, and extreme weather through 2026–2027?"

**Answer:** Based on a 6-model ensemble (IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM, and this project's own XGBoost+LSTM model), the consensus as of May 2026 pointed to a Strong El Niño (Niño 3.4 anomaly of +1.5 to +2.5°C), with a meaningful probability of crossing the +2.0°C Super El Niño threshold, peaking around October–November 2026. Historical ENSO correlation flags Northeast Brazil, Indonesia, and Australia as highest drought risk, and Peru/Ecuador as highest flood risk.

---

## 📊 Data Summary

| Indicator | Value |
|---|---|
| Regions monitored | 9 (Niño 1+2, 3, 3.4, 4, PDO-North, Warm Pool, 2 TAO buoys, Kelvin Wave) |
| Historical ONI series | 1950–2026 (77 years) |
| Forecast models compared | 6 (IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM, project's own ML model) |
| Model architecture | XGBoost (1–3 month horizon) + Bidirectional LSTM (6–12 month horizon) |
| Reported model RMSE | 0.28°C (vs. 0.45°C for a climatology baseline) |
| Regional impact zones mapped | 10 |

---

## 🔵 Key Findings

- **Model ensemble pointed to a Strong-to-Super El Niño for late 2026** — the 6-model average projected a Niño 3.4 anomaly in the 1.5–2.5°C range by October–November 2026, with roughly a 1-in-3 chance (per the cited NOAA outlook referenced in the app) of crossing the +2.0°C Super El Niño threshold — a tier reached historically only in 2015/16, 1997/98, and 1982/83.
- **Subsurface Kelvin Wave anomaly as the key precursor signal** — the app highlights a subsurface heat anomaly of up to +6°C in the 50–150m layer between 150°W and 80°W, more than double the equivalent period in 2023, framed as the thermal "fuel" for further intensification.
- **Northeast Brazil flagged as highest drought risk in this model** — historical correlation across 15 El Niño events since 1950 suggests roughly 85% probability of severe drought in Brazil's semi-arid Northeast, a region home to ~27 million people.
- **Inverse relationship with Atlantic hurricane activity** — El Niño years are associated with below-normal Atlantic hurricane seasons, consistent with the reduced activity referenced in NOAA's seasonal outlook cited in the app.
- **Model validated against 2023–2025 events** — per the app's own reported metrics, the XGBoost+LSTM model correctly anticipated the general trajectory of the 2023–24 El Niño and the 2025 La Niña before reproducing the current transition.

> ⚠️ **Methodological note:** this is a personal, portfolio-scale ML exercise, not an official forecasting product. The Niño 3.4 anomaly for May 2026 (+0.9°C) is cited from IRI; most other historical values, all "current" regional anomalies, and the specific quoted probabilities (e.g., "98%") are illustrative parameters set within the app to demonstrate the methodology, not values independently re-verified against NOAA/IRI at publication time. Treat headline probabilities as a demonstration of the pipeline, and always cross-check current ENSO status against [NOAA CPC](https://www.cpc.ncep.noaa.gov/) or [IRI](https://iri.columbia.edu/) directly.

---

## 🗺️ Monitored Regions

| Region | Location | Role |
|---|---|---|
| Niño 1+2 | 5°S, 85°W | Coastal reference, NW Peru/Ecuador |
| Niño 3 | 5°S, 130°W | Historical primary warming index |
| Niño 3.4 | 5°S, 155°W | **Official NOAA/CPC ENSO index** |
| Niño 4 | 5°S, 175°W | Modoki-type El Niño signal |
| PDO (North) | 40°N, 155°W | Pacific Decadal Oscillation, long-term modulation |
| Warm Pool | 5°S, 165°E | Western Pacific subsurface heat reservoir |
| TAO Buoys A/B | 2°S, 140°W / 165°W | In-situ TOGA-TAO monitoring |
| Kelvin Wave | 5°S, 110°W | Subsurface precursor signal |

---

## 🔬 Methodology

```
Data inputs        →  Historical SST for Niño 1+2/3/3.4/4 (NOAA ERSSTv5-style),
                       Southern Oscillation Index (SOI), Ocean Heat Content
                       anomalies (0–300m), Indian Ocean Dipole Mode Index (DMI)
                       — 77 years × 12 months per variable

Feature engineering →  1–12 month lag features for teleconnections; 3- and
                       6-month rolling means; wavelet decomposition for 2–7
                       year ENSO cycles; PDO as a decadal modulation feature;
                       z-score standardized anomalies per region

Model architecture   →  XGBoost for short-term forecasting (1–3 months) +
                       bidirectional LSTM for 6–12 month horizon
                       Training: 1950–2020 (70%) · Validation: 2021–2023 (15%)
                       · Test: 2024–2025 (15%)
                       Reported RMSE: 0.28°C vs. 0.45°C climatology baseline

Validation           →  Backtested against known 2023–2024 El Niño and 2025
                       La Niña trajectories

2026 forecast         →  Weighted ensemble average across 6 models (IRI/CPC,
                       ECMWF, NOAA CFSv2, UK Met Office, BoM, project's ML
                       model)

Regional impact map    →  Historical correlation between the 15 recorded El
                       Niño events since 1950 and precipitation/temperature
                       anomalies across 10 regions

Live SST monitoring     →  Optional live fetch from NOAA ERDDAP (OISSTv2)
                       for near-real-time sea surface temperature by region,
                       refreshed hourly (falls back gracefully if the feed
                       is unavailable)
```

---

## 🖥️ Dashboard Overview

The Streamlit app is organized into seven tabs:

1. **🗺️ Map & Analysis** — interactive map of the 9 monitoring regions with live/estimated SST fetch via NOAA ERDDAP.
2. **🔬 Methodology & Pipeline** — the six-step ML pipeline, an ENSO/El Niño primer, and model architecture summary.
3. **💡 What We Found** — the key findings above, plus the project's conclusion.
4. **📈 Trends** — historical ONI index (1950–2026), monthly Niño 3.4 (2024–2026), and a Super El Niño comparison chart.
5. **🧪 Parameters** — per-parameter analysis (Niño 3.4, Niño 3, Niño 1+2, SOI, OHC).
6. **📋 Raw Data** — full per-model 2026 forecast table with CSV export.
7. **📚 Sources & Credits** — data sources, technologies used, and author credentials.

The full interface — labels, chart titles, and narrative text — is natively trilingual (PT/EN/ES), switchable from the sidebar.

---

## 🛠️ Tech Stack

| Technology | Use |
|---|---|
| Python 3.11 | Core language |
| Streamlit | Dashboard framework |
| Folium + streamlit-folium | Interactive ENSO monitoring-zone mapping |
| Plotly (Graph Objects) | Time series, model comparison, and parameter charts |
| Pandas / NumPy | Data processing and feature engineering |
| Requests | Live NOAA ERDDAP (OISSTv2) SST integration |

---

## 📁 Repository Structure

```
el-nino-2026-ml-forecast/
├── app.py                    # Main dashboard (7 tabs, ML pipeline, PT/EN/ES)
├── requirements.txt          # Python dependencies
├── README.md                   # This file (English)
├── README.pt-BR.md             # Portuguese version
└── README.es.md                # Spanish version
```

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/amaurialmeida/el-nino-2026-ml-forecast.git
cd el-nino-2026-ml-forecast

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

---

## 🌐 Live App

🔗 **[el-nino-2026-ml-forecast.streamlit.app](https://el-nino-2026-ml-forecast.streamlit.app/)**

Available in 🇧🇷 Portuguese, 🇺🇸 English, and 🇪🇸 Spanish.

---

## 📚 References

- NOAA Climate Prediction Center (CPC) — official ENSO monitoring and outlooks.
- International Research Institute for Climate and Society (IRI), Columbia University — ENSO probabilistic forecasts.
- NOAA ERDDAP / OISSTv2 — sea surface temperature reanalysis data.
- NOAA ERSSTv5 — Extended Reconstructed Sea Surface Temperature dataset.

---

## 🔗 Academic / Professional Links

| Platform | Link |
|---|---|
| Lattes | http://lattes.cnpq.br/9545242042800090 |
| Escavador | https://www.escavador.com/sobre/8577779/amauri-almeida-de-souza-junior |

---

## 🌿 Environmental Portfolio

This project is part of the author's environmental research and data science portfolio.
🔗 [amaurialmeida.github.io/environmental-portfolio](https://amaurialmeida.github.io/environmental-portfolio)

---

© 2026 · Amauri Almeida de Souza Junior · Portfolio Project
