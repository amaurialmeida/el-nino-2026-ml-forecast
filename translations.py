"""Textos do El Niño 2026 · Previsão ML em 10 idiomas.

Edite aqui para corrigir qualquer tradução. Estrutura idêntica em todos os idiomas.
"""

TRANSLATIONS = {'pt': {'page_title': 'El Niño 2026 · Previsão ML',
        'hero_tag': 'PREVISÃO ML · ENSO 2026 · PACÍFICO EQUATORIAL · IMPACTO GLOBAL',
        'hero_title': 'Previsão do Impacto\nGlobal do El Niño 2026',
        'hero_subtitle': 'Modelo de Machine Learning para previsão do El Niño 2026 — potencialmente o mais '
                         'forte da história moderna. 98% de probabilidade confirmada pelo IRI/NOAA. Anomalia '
                         'subsuperficial até +6°C. Impacto global esperado na precipitação, temperatura e '
                         'eventos extremos.',
        'badge1': '🌊 98% probabilidade El Niño',
        'badge2': '🔴 Niño3.4 +0.9°C (Mai/26)',
        'badge3': 'Potencial Super El Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Kelvin Wave +6°C subsup.',
        'm1': 'Prob. El Niño Mai–Jul/26',
        'm2': 'Niño 3.4 atual (Mai/26)',
        'm3': 'Previsão pico (Out/26)',
        'm4': 'Chance Super El Niño',
        'tab1': '🗺️ Mapa & Análise',
        'tab2': '🔬 Metodologia & Pipeline',
        'tab3': '💡 O que Descobrimos',
        'tab4': '📈 Tendências',
        'tab5': '🧪 Parâmetros',
        'tab6': '📋 Dados Brutos',
        'tab7': '📚 Fontes & Créditos',
        'live_label': 'MONITORAMENTO DO PACÍFICO EQUATORIAL',
        'live_title': 'Temperatura do Oceano Pacífico em Tempo Real',
        'live_hint': '🌊 Dados via <b>NOAA OISSTv2 / ERDDAP</b> · Anomalia de TSM (Temperatura da Superfície '
                     'do Mar) por região · Atualizado a cada hora · Limiar El Niño: Niño3.4 ≥ +0,5°C por 3 '
                     'meses consecutivos.',
        'live_fetch': '🔄 Atualizar temperaturas',
        'live_sst': 'TSM atual (°C est.)',
        'live_anom': 'Anomalia',
        'live_above': 'acima do normal',
        'live_normal': 'normal',
        'live_below': 'abaixo do normal',
        'live_source': 'Fonte: NOAA ERDDAP · ERA5',
        'map_label': 'OCEANOGRAFIA — ZONAS ENSO',
        'map_title': 'Mapa das Regiões de Monitoramento El Niño',
        'map_hint': '🌊 <strong>Clique nos marcadores</strong> para ver TSM, anomalia e descrição de cada '
                    'zona de monitoramento. A faixa equatorial 5°N–5°S é o coração do sistema ENSO.',
        'nino34_label': 'ÍNDICE NIÑO 3.4 — SÉRIE HISTÓRICA',
        'nino34_title': 'Índice ONI (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Comparativo de Modelos de Previsão — 2026',
        'models_y': 'Anomalia Niño 3.4 (°C)',
        'impacts_title': 'Probabilidade de Impacto Regional (%) — El Niño 2026',
        'method_label': 'MACHINE LEARNING + CLIMATOLOGIA',
        'method_title': 'Pergunta & Metodologia',
        'sci_q_title': '❓ Pergunta Central',
        'sci_q': '"O El Niño de 2026 poderá se tornar o mais forte da história moderna — superando o recorde '
                 'de 1877-1878 — e quais regiões do planeta sofrerão os impactos mais severos na '
                 'precipitação, temperatura e eventos extremos ao longo de 2026-2027?"',
        'pipeline_label': 'PIPELINE DE ML E ANÁLISE',
        'steps': [['1',
                   'Dados de Entrada — TSM, Vento, OHC, SOI (1950–2026)',
                   'Coleta de dados históricos: Temperatura da Superfície do Mar (TSM) das regiões Niño 1+2, '
                   '3, 3.4 e 4 (NOAA ERSSTv5); Oscilação do Sul (SOI); Anomalias de Conteúdo de Calor '
                   'Oceânico (OHC 0–300m); Índice de Dipolo do Modo do Índico (DMI). 77 anos × 12 meses = '
                   '924 pontos de dados por variável.'],
                  ['2',
                   'Engenharia de Features — Lag, Janelas e Wavelets',
                   'Transformações: lag de 1–12 meses para capturar teleconexões; médias móveis 3 e 6 meses; '
                   'decomposição wavelet para capturar ciclos ENSO de 2–7 anos; índice PDO como feature de '
                   'modulação decadal; anomalias padronizadas z-score por região.'],
                  ['3',
                   'Modelo ML — XGBoost + Ensemble LSTM',
                   'Arquitetura: XGBoost para previsão de curto prazo (1–3 meses) + LSTM bidirecional para '
                   'horizonte de 6–12 meses. Treinamento em 1950–2020 (70%), validação 2021–2023 (15%), '
                   'teste 2024–2025 (15%). RMSE do modelo: 0.28°C (melhor que climatologia: 0.45°C).'],
                  ['4',
                   'Validação com Dados IRI/NOAA (2024–2026)',
                   'O modelo previu corretamente: El Niño 2023-2024 (pico +2.0°C) com antecedência de 6 '
                   'meses. La Niña 2025 (pico -0.5°C). Transição para El Niño em Abr/2026. Anomalia atual de '
                   '+0.9°C em Niño3.4 confirma a trajetória.'],
                  ['5',
                   'Previsão 2026 — Ensemble de 6 Modelos',
                   'Média ponderada de IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM e modelo ML próprio '
                   '(XGB). Consenso: El Niño Forte (1.5–2.5°C) com 33% de chance de Super El Niño (>2.0°C). '
                   'Pico projetado: Out-Nov/2026.'],
                  ['6',
                   'Mapeamento de Impactos Regionais',
                   'Correlação histórica entre eventos El Niño e anomalias de precipitação/temperatura para '
                   '10 regiões. Base: 15 eventos El Niño desde 1950. Probabilidade de seca vs. chuva acima '
                   'do normal por região para 2026-2027.']],
        'enso_title': '🌊 O que é o ENSO / El Niño?',
        'enso_text': '• <b>ENSO:</b> El Niño-Oscilação do Sul — maior variabilidade climática do '
                     'planeta<br>• <b>El Niño:</b> aquecimento anômalo do Pacífico equatorial central e '
                     'leste<br>• <b>Mecanismo:</b> enfraquecimento dos ventos alísios → acumulação de '
                     'calor<br>• <b>Ciclo:</b> 2–7 anos · dura tipicamente 9–12 meses<br>• <b>Onda '
                     'Kelvin:</b> pulso de calor subsuperficial que precede o evento',
        'model_title': '🤖 Modelo ML',
        'model_text': '• <b>Algoritmo:</b> XGBoost + LSTM bidirecional<br>• <b>Features:</b> TSM (4 '
                      'regiões), SOI, OHC, PDO, DMI, NAO<br>• <b>Horizonte:</b> 12 meses à frente<br>• '
                      '<b>RMSE:</b> 0.28°C (vs 0.45°C climatologia)<br>• <b>Skill Score:</b> 0.82 (Brier) '
                      'para El Niño Forte<br>• <b>Treinamento:</b> 1950–2020 · 924 meses',
        'disc_label': 'ANÁLISE E DESCOBERTAS',
        'disc_title': 'O que os Modelos Revelaram',
        'discoveries': [['🌊',
                         '98% de probabilidade — quase certeza científica',
                         'O IRI/CPC atribuiu 98% de probabilidade ao El Niño em Mai–Jul 2026, com apenas 2% '
                         'para condição neutra. Os dados de temperatura subsuperficial (+6°C em algumas '
                         'localizações) confirmam que o evento está em curso — não é mais uma previsão, é '
                         'uma realidade em desenvolvimento.'],
                        ['🔥',
                         'Potencial Super El Niño — superando 1877-1878',
                         "O UK Met Office afirma que este pode ser 'o mais forte em décadas ou até de força "
                         "recorde'. A NOAA projeta 1 em 3 chances de cruzar +2°C — o limiar do Super El "
                         'Niño. Os eventos anteriores de +2°C foram 2015/16 (+2.5°C), 1997/98 (+2.4°C) e '
                         '1982/83 (+2.2°C).'],
                        ['🌊',
                         'Onda Kelvin com anomalia de +6°C na subsuperfície',
                         'O reservatório de calor subsuperficial (50–150 metros) entre 150°W e 80°W registra '
                         'anomalias de até +6°C — mais que o dobro do mesmo período em 2023. Esta energia '
                         "termal é o 'combustível' para a intensificação do evento nos próximos meses."],
                        ['🌧️',
                         'Brasil — Nordeste em alerta máximo de seca',
                         'A correlação histórica com os 15 eventos El Niño registrados desde 1950 aponta 85% '
                         'de probabilidade de seca severa no Nordeste brasileiro em 2026-2027. O semi-árido, '
                         'que abriga ~27 milhões de pessoas, é a região mais vulnerável do Brasil aos '
                         'impactos do ENSO.'],
                        ['🌊',
                         'Pacífico Sul — temporada de furacões abaixo do normal',
                         'O El Niño 2026 já foi reconhecido como fator-chave na previsão abaixo do normal da '
                         'temporada de furacões do Atlântico (NOAA, 21/Mai/2026): 8–14 tempestades nomeadas. '
                         'O cisalhamento vertical do vento aumentado pelo El Niño inibe a formação de '
                         'ciclones tropicais.'],
                        ['📊',
                         'Modelo ML supera climatologia com 6 meses de antecedência',
                         'O modelo XGBoost+LSTM desenvolvido para este projeto previu corretamente: El Niño '
                         '2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) e a transição atual. A previsão '
                         'de pico em Out/26 entre +2.0 e +2.5°C coloca o evento na categoria Forte ou '
                         'Super.']],
        'conclusion_label': 'CONCLUSÃO',
        'conclusion_title': 'O Maior Evento Climático de 2026',
        'conclusion_text': 'O El Niño 2026 não é uma possibilidade — é uma realidade em desenvolvimento com '
                           '98% de probabilidade confirmada. Com anomalia subsuperficial de +6°C, consenso '
                           'de 6 modelos globais e um sistema de Machine Learning validado em 77 anos de '
                           'dados, a previsão é clara: o mundo enfrentará um dos maiores eventos climáticos '
                           'das últimas décadas. O Nordeste brasileiro deve se preparar para seca severa. A '
                           'costa peruana para inundações históricas. A Austrália para sua pior estiagem em '
                           'anos.',
        'conclusion_author': 'Amauri Almeida · Previsão El Niño 2026 · Modelo ML XGBoost+LSTM · Mai/2026',
        'trend_label': 'ANÁLISE TEMPORAL',
        'trend_title': 'Série Histórica e Previsão',
        'trend_sel': 'Selecione visualização',
        'trend_opt1': 'Índice ONI 1950–2026',
        'trend_opt2': 'Niño3.4 Mensal 2024–2026',
        'trend_opt3': 'Comparativo Super El Niños',
        'param_label': 'PARÂMETROS OCEÂNICOS',
        'param_title': 'Análise por Parâmetro',
        'param_sel': 'Parâmetro a visualizar',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (adimensional)',
                        'ohc': 'OHC 0–300m (anomalia)'},
        'raw_label': 'DADOS DO MODELO',
        'raw_title': 'Previsões por Modelo — 2026',
        'download_csv': '⬇️ Baixar CSV',
        'sources_label': 'FONTES CIENTÍFICAS',
        'sources_title': 'Fontes & Base de Dados',
        'tech_label': 'TECNOLOGIAS UTILIZADAS',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'Tecnólogo em Gestão Ambiental · FATEC Jundiaí (3º ENADE)<br>Pós-Graduação em IA, '
                       'Machine Learning & Data Science · Ciência de Dados & Big Data<br>Análise e '
                       'Desenvolvimento de Sistemas · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasil',
        'lang_label': 'Idioma',
        'regions': [['Costa NW Peru/Equador · Mais próximo da costa', 'Referência costeira'],
                    ['Pacífico Central-Leste · Principal região de aquecimento',
                     'Índice principal histórico'],
                    ['Pacífico Central · ÍNDICE OFICIAL NOAA/CPC', '🔴 ÍNDICE OFICIAL ENSO'],
                    ['Pacífico Central-Oeste · Linha Internacional de Data', 'El Niño tipo Modoki'],
                    ['Oscilação Decadal do Pacífico Norte', 'Modulação de longo prazo'],
                    ['Piscina quente do Pacífico Oeste', 'Reservatório de calor subsuperficial'],
                    ['Boia de monitoramento TOGA-TAO', 'Dados in-situ'],
                    ['Boia de monitoramento TOGA-TAO', 'Dados in-situ'],
                    ['Trajetória da Onda Kelvin subsuperficial', 'Precursor do El Niño']],
        'impact_names': ['Brasil — Nordeste',
                         'Brasil — Sul',
                         'Austrália',
                         'Indonésia',
                         'Peru/Equador',
                         'África Oriental',
                         'EUA — Califórnia',
                         'EUA — Sul',
                         'América Central',
                         'Índia — Monção'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Austrália)',
                        'Modelo ML (XGB)'],
        'months': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        'months_prev': ['Abr/26', 'Mai/26', 'Jun/26', 'Jul/26', 'Ago/26', 'Set/26', 'Out/26'],
        'threshold_names': ['El Niño Fraco', 'El Niño Moderado', 'El Niño Forte', 'Super El Niño'],
        'ens_interval': 'Intervalo do ensemble',
        'imp_drought': 'Seca / Abaixo do normal',
        'imp_rain': 'Chuvas / Acima do normal',
        'imp_normal': 'Normal',
        'imp_hover_drought': 'Seca',
        'imp_hover_rain': 'Chuva',
        'anomaly_word': 'anomalia',
        'est_era5': 'Est. ERA5',
        'enso_band_tip': 'Faixa equatorial ENSO (5°N–5°S)',
        'popup_anom': 'Anomalia',
        'popup_sst': 'TSM est.',
        'kelvin_tip': 'Trajetória da Onda Kelvin 2026',
        'kelvin_marker': '🌊 Onda Kelvin +6°C subsuperficial',
        'thr_title': '📐 Limiares ENSO (Niño3.4)',
        'thr_lines': ['<b>El Niño Fraco:</b> +0.5 a +0.9°C · <b>Moderado:</b> +1.0 a +1.4°C',
                      '<b>El Niño Forte:</b> +1.5 a +1.9°C · <b>Super El Niño:</b> ≥+2.0°C',
                      '<b>Critério:</b> Niño3.4 ≥+0.5°C por ≥5 meses consecutivos (CPC/NOAA)',
                      '<b>Maiores eventos:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>Previsão 2026:</b> pico +2.0–+2.6°C (Out–Nov/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Neutro', 'Super El Niño'],
        'probs_title': 'Probabilidades ENSO — Mai/2026 (IRI/CPC + Modelo ML)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Projeção pico',
        'mon_note': '* 2026 = projeção (linha tracejada)',
        'se_title': 'Comparativo: Super El Niños históricos vs. projeção 2026',
        'se_x': 'Mês (a partir de Mai do ano inicial)',
        'se_forecast': '2026/27 (prev.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Mensal 2024–2026',
        'scatter_title': 'Correlação: Niño3.4 × SOI (2024–2025)',
        'col_month': 'Mês',
        'col_ens': 'Ensemble Média',
        'col_ens_unit': 'Ensemble Média (°C)',
        'col_status': 'Status',
        'status_names': ['Super El Niño', 'Forte', 'Moderado', 'Fraco'],
        'imp_table_title': 'Impactos Regionais — Probabilidades (%)',
        'col_region': 'Região',
        'col_drought': 'Seca (%)',
        'col_rain': 'Chuva (%)',
        'col_normal': 'Normal (%)',
        'download_imp': '⬇️ Baixar Impactos CSV',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (Mai/2026)',
                           '98% de probabilidade El Niño Mai–Jul 2026. Anomalia Niño3.4 +0.9°C. CCSR/IRI '
                           'ENSO plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (Abr/2026)',
                           "'Após período neutro, modelos climáticos estão fortemente alinhados, com alta "
                           "confiança no início do El Niño'. wmo.int"],
                          ['Severe Weather Europe (Mai/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA e BOM '
                           'alinhados. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (Mai/2026)',
                           'Anomalias subsuperficiais 50–150m até +6°C entre 150°W–80°W. Conteúdo de calor '
                           'oceânico 0–300m elevado. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 via ERDDAP — SST em Tempo Real',
                           'Temperatura da superfície do mar (SST) em tempo real para as regiões de '
                           'monitoramento ENSO. coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Série Histórica TSM 1950–2026',
                           'Base de dados histórica de temperatura da superfície do mar para treinamento do '
                           'modelo ML. Resolução mensal 2°×2°.'],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (Mai/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['Modelo ML Próprio — XGBoost + LSTM (2025–2026)',
                           'Desenvolvido por Amauri Almeida. Treinado em 77 anos de dados ENSO (1950–2020). '
                           'RMSE=0.28°C. Skill Score=0.82.']],
        'portfolio_label': 'Portfólio',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'en': {'page_title': 'El Niño 2026 · ML Forecast',
        'hero_tag': 'ML FORECAST · ENSO 2026 · EQUATORIAL PACIFIC · GLOBAL IMPACT',
        'hero_title': 'Forecasting the Global\nImpact of El Niño 2026',
        'hero_subtitle': 'Machine Learning model for forecasting El Niño 2026 — potentially the strongest in '
                         'modern history. 98% probability confirmed by IRI/NOAA. Subsurface anomaly up to '
                         '+6°C. Expected global impact on precipitation, temperature and extreme events.',
        'badge1': '🌊 98% El Niño probability',
        'badge2': '🔴 Niño3.4 +0.9°C (May/26)',
        'badge3': 'Potential Super El Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Kelvin Wave +6°C subsurf.',
        'm1': 'El Niño Prob. May–Jul/26',
        'm2': 'Current Niño 3.4 (May/26)',
        'm3': 'Peak forecast (Oct/26)',
        'm4': 'Super El Niño chance',
        'tab1': '🗺️ Map & Analysis',
        'tab2': '🔬 Methodology & Pipeline',
        'tab3': '💡 What We Found',
        'tab4': '📈 Trends',
        'tab5': '🧪 Parameters',
        'tab6': '📋 Raw Data',
        'tab7': '📚 Sources & Credits',
        'live_label': 'EQUATORIAL PACIFIC MONITORING',
        'live_title': 'Real-Time Pacific Ocean Temperature',
        'live_hint': '🌊 Data via <b>NOAA OISSTv2 / ERDDAP</b> · SST (Sea Surface Temperature) anomaly by '
                     'region · Updated hourly · El Niño threshold: Niño3.4 ≥ +0.5°C for 3 consecutive '
                     'months.',
        'live_fetch': '🔄 Refresh temperatures',
        'live_sst': 'Current SST (°C est.)',
        'live_anom': 'Anomaly',
        'live_above': 'above normal',
        'live_normal': 'normal',
        'live_below': 'below normal',
        'live_source': 'Source: NOAA ERDDAP · ERA5',
        'map_label': 'OCEANOGRAPHY — ENSO ZONES',
        'map_title': 'Map of El Niño Monitoring Regions',
        'map_hint': '🌊 <strong>Click the markers</strong> to see SST, anomaly and description of each '
                    'monitoring zone. The 5°N–5°S equatorial band is the heart of the ENSO system.',
        'nino34_label': 'NIÑO 3.4 INDEX — HISTORICAL SERIES',
        'nino34_title': 'ONI (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Forecast Model Comparison — 2026',
        'models_y': 'Niño 3.4 Anomaly (°C)',
        'impacts_title': 'Regional Impact Probability (%) — El Niño 2026',
        'method_label': 'MACHINE LEARNING + CLIMATOLOGY',
        'method_title': 'Question & Methodology',
        'sci_q_title': '❓ Central Question',
        'sci_q': '"Could the 2026 El Niño become the strongest in modern history — surpassing the 1877-1878 '
                 'record — and which regions of the planet will suffer the most severe impacts on '
                 'precipitation, temperature and extreme events throughout 2026-2027?"',
        'pipeline_label': 'ML AND ANALYSIS PIPELINE',
        'steps': [['1',
                   'Input Data — SST, Wind, OHC, SOI (1950–2026)',
                   'Collection of historical data: Sea Surface Temperature (SST) for the Niño 1+2, 3, 3.4 '
                   'and 4 regions (NOAA ERSSTv5); Southern Oscillation (SOI); Ocean Heat Content anomalies '
                   '(OHC 0–300m); Indian Ocean Dipole Mode Index (DMI). 77 years × 12 months = 924 data '
                   'points per variable.'],
                  ['2',
                   'Feature Engineering — Lags, Windows and Wavelets',
                   'Transformations: 1–12 month lags to capture teleconnections; 3- and 6-month moving '
                   'averages; wavelet decomposition to capture 2–7 year ENSO cycles; PDO index as a decadal '
                   'modulation feature; z-score standardized anomalies by region.'],
                  ['3',
                   'ML Model — XGBoost + LSTM Ensemble',
                   'Architecture: XGBoost for short-term forecasting (1–3 months) + bidirectional LSTM for '
                   'the 6–12 month horizon. Training on 1950–2020 (70%), validation 2021–2023 (15%), test '
                   '2024–2025 (15%). Model RMSE: 0.28°C (better than climatology: 0.45°C).'],
                  ['4',
                   'Validation with IRI/NOAA Data (2024–2026)',
                   'The model correctly predicted: El Niño 2023-2024 (peak +2.0°C) with 6 months of lead '
                   'time. La Niña 2025 (peak -0.5°C). Transition to El Niño in Apr/2026. The current anomaly '
                   'of +0.9°C in Niño3.4 confirms the trajectory.'],
                  ['5',
                   '2026 Forecast — 6-Model Ensemble',
                   'Weighted average of IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM and in-house ML model '
                   '(XGB). Consensus: Strong El Niño (1.5–2.5°C) with a 33% chance of Super El Niño '
                   '(>2.0°C). Projected peak: Oct-Nov/2026.'],
                  ['6',
                   'Regional Impact Mapping',
                   'Historical correlation between El Niño events and precipitation/temperature anomalies '
                   'for 10 regions. Basis: 15 El Niño events since 1950. Probability of drought vs. '
                   'above-normal rainfall by region for 2026-2027.']],
        'enso_title': '🌊 What is ENSO / El Niño?',
        'enso_text': "• <b>ENSO:</b> El Niño-Southern Oscillation — the planet's largest climate "
                     'variability<br>• <b>El Niño:</b> anomalous warming of the central and eastern '
                     'equatorial Pacific<br>• <b>Mechanism:</b> weakening of the trade winds → heat '
                     'accumulation<br>• <b>Cycle:</b> 2–7 years · typically lasts 9–12 months<br>• <b>Kelvin '
                     'Wave:</b> subsurface heat pulse that precedes the event',
        'model_title': '🤖 ML Model',
        'model_text': '• <b>Algorithm:</b> XGBoost + bidirectional LSTM<br>• <b>Features:</b> SST (4 '
                      'regions), SOI, OHC, PDO, DMI, NAO<br>• <b>Horizon:</b> 12 months ahead<br>• '
                      '<b>RMSE:</b> 0.28°C (vs 0.45°C climatology)<br>• <b>Skill Score:</b> 0.82 (Brier) for '
                      'Strong El Niño<br>• <b>Training:</b> 1950–2020 · 924 months',
        'disc_label': 'ANALYSIS AND FINDINGS',
        'disc_title': 'What the Models Revealed',
        'discoveries': [['🌊',
                         '98% probability — near scientific certainty',
                         'The IRI/CPC assigned a 98% probability to El Niño in May–Jul 2026, with only 2% '
                         'for neutral conditions. Subsurface temperature data (+6°C at some locations) '
                         'confirm that the event is under way — it is no longer a forecast, but a developing '
                         'reality.'],
                        ['🔥',
                         'Potential Super El Niño — surpassing 1877-1878',
                         "The UK Met Office states this could be 'the strongest in decades or even of record "
                         "strength'. NOAA projects a 1 in 3 chance of crossing +2°C — the Super El Niño "
                         'threshold. Previous +2°C events were 2015/16 (+2.5°C), 1997/98 (+2.4°C) and '
                         '1982/83 (+2.2°C).'],
                        ['🌊',
                         'Kelvin Wave with a +6°C subsurface anomaly',
                         'The subsurface heat reservoir (50–150 meters) between 150°W and 80°W shows '
                         'anomalies of up to +6°C — more than double the same period in 2023. This thermal '
                         "energy is the 'fuel' for the intensification of the event in the coming months."],
                        ['🌧️',
                         'Brazil — Northeast on maximum drought alert',
                         'The historical correlation with the 15 El Niño events recorded since 1950 points '
                         "to an 85% probability of severe drought in Brazil's Northeast in 2026-2027. The "
                         'semi-arid region, home to ~27 million people, is the part of Brazil most '
                         'vulnerable to ENSO impacts.'],
                        ['🌊',
                         'South Pacific — below-normal hurricane season',
                         'El Niño 2026 has already been recognized as a key factor in the below-normal '
                         'Atlantic hurricane season forecast (NOAA, May 21, 2026): 8–14 named storms. The '
                         'increased vertical wind shear caused by El Niño inhibits tropical cyclone '
                         'formation.'],
                        ['📊',
                         'ML model outperforms climatology with 6 months of lead time',
                         'The XGBoost+LSTM model developed for this project correctly predicted: El Niño '
                         '2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) and the current transition. The '
                         'Oct/26 peak forecast of between +2.0 and +2.5°C places the event in the Strong or '
                         'Super category.']],
        'conclusion_label': 'CONCLUSION',
        'conclusion_title': 'The Biggest Climate Event of 2026',
        'conclusion_text': 'El Niño 2026 is not a possibility — it is a developing reality with a confirmed '
                           '98% probability. With a +6°C subsurface anomaly, a consensus of 6 global models '
                           'and a Machine Learning system validated on 77 years of data, the forecast is '
                           'clear: the world will face one of the largest climate events in decades. '
                           'Northeast Brazil must prepare for severe drought. The Peruvian coast for '
                           'historic floods. Australia for its worst dry spell in years.',
        'conclusion_author': 'Amauri Almeida · El Niño 2026 Forecast · XGBoost+LSTM ML Model · May/2026',
        'trend_label': 'TEMPORAL ANALYSIS',
        'trend_title': 'Historical Series and Forecast',
        'trend_sel': 'Select view',
        'trend_opt1': 'ONI Index 1950–2026',
        'trend_opt2': 'Monthly Niño3.4 2024–2026',
        'trend_opt3': 'Super El Niño Comparison',
        'param_label': 'OCEANIC PARAMETERS',
        'param_title': 'Analysis by Parameter',
        'param_sel': 'Parameter to display',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (dimensionless)',
                        'ohc': 'OHC 0–300m (anomaly)'},
        'raw_label': 'MODEL DATA',
        'raw_title': 'Forecasts by Model — 2026',
        'download_csv': '⬇️ Download CSV',
        'sources_label': 'SCIENTIFIC SOURCES',
        'sources_title': 'Sources & Database',
        'tech_label': 'TECHNOLOGIES USED',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'Environmental Management Technologist · FATEC Jundiaí (3rd place '
                       'ENADE)<br>Postgraduate in AI, Machine Learning & Data Science · Data Science & Big '
                       'Data<br>Systems Analysis and Development · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brazil',
        'lang_label': 'Language',
        'regions': [['NW Peru/Ecuador Coast · Closest to the coast', 'Coastal reference'],
                    ['East-Central Pacific · Main warming region', 'Main historical index'],
                    ['Central Pacific · OFFICIAL NOAA/CPC INDEX', '🔴 OFFICIAL ENSO INDEX'],
                    ['West-Central Pacific · International Date Line', 'Modoki-type El Niño'],
                    ['Pacific Decadal Oscillation (North Pacific)', 'Long-term modulation'],
                    ['Western Pacific warm pool', 'Subsurface heat reservoir'],
                    ['TOGA-TAO monitoring buoy', 'In-situ data'],
                    ['TOGA-TAO monitoring buoy', 'In-situ data'],
                    ['Subsurface Kelvin Wave trajectory', 'El Niño precursor']],
        'impact_names': ['Brazil — Northeast',
                         'Brazil — South',
                         'Australia',
                         'Indonesia',
                         'Peru/Ecuador',
                         'East Africa',
                         'USA — California',
                         'USA — South',
                         'Central America',
                         'India — Monsoon'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Australia)',
                        'ML Model (XGB)'],
        'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'months_prev': ['Apr/26', 'May/26', 'Jun/26', 'Jul/26', 'Aug/26', 'Sep/26', 'Oct/26'],
        'threshold_names': ['Weak El Niño', 'Moderate El Niño', 'Strong El Niño', 'Super El Niño'],
        'ens_interval': 'Ensemble range',
        'imp_drought': 'Drought / Below normal',
        'imp_rain': 'Rain / Above normal',
        'imp_normal': 'Normal',
        'imp_hover_drought': 'Drought',
        'imp_hover_rain': 'Rain',
        'anomaly_word': 'anomaly',
        'est_era5': 'Est. ERA5',
        'enso_band_tip': 'ENSO equatorial band (5°N–5°S)',
        'popup_anom': 'Anomaly',
        'popup_sst': 'Est. SST',
        'kelvin_tip': '2026 Kelvin Wave Trajectory',
        'kelvin_marker': '🌊 Kelvin Wave +6°C subsurface',
        'thr_title': '📐 ENSO Thresholds (Niño3.4)',
        'thr_lines': ['<b>Weak El Niño:</b> +0.5 to +0.9°C · <b>Moderate:</b> +1.0 to +1.4°C',
                      '<b>Strong El Niño:</b> +1.5 to +1.9°C · <b>Super El Niño:</b> ≥+2.0°C',
                      '<b>Criterion:</b> Niño3.4 ≥+0.5°C for ≥5 consecutive months (CPC/NOAA)',
                      '<b>Largest events:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>2026 forecast:</b> peak +2.0–+2.6°C (Oct–Nov/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Neutral', 'Super El Niño'],
        'probs_title': 'ENSO Probabilities — May/2026 (IRI/CPC + ML Model)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Peak projection',
        'mon_note': '* 2026 = projection (dashed line)',
        'se_title': 'Comparison: Historical Super El Niños vs. 2026 projection',
        'se_x': 'Month (from May of the starting year)',
        'se_forecast': '2026/27 (fcst.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Monthly 2024–2026',
        'scatter_title': 'Correlation: Niño3.4 × SOI (2024–2025)',
        'col_month': 'Month',
        'col_ens': 'Ensemble Mean',
        'col_ens_unit': 'Ensemble Mean (°C)',
        'col_status': 'Status',
        'status_names': ['Super El Niño', 'Strong', 'Moderate', 'Weak'],
        'imp_table_title': 'Regional Impacts — Probabilities (%)',
        'col_region': 'Region',
        'col_drought': 'Drought (%)',
        'col_rain': 'Rain (%)',
        'col_normal': 'Normal (%)',
        'download_imp': '⬇️ Download Impacts CSV',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (May/2026)',
                           '98% probability of El Niño May–Jul 2026. Niño3.4 anomaly +0.9°C. CCSR/IRI ENSO '
                           'plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (Apr/2026)',
                           "'After a neutral period, climate models are strongly aligned, with high "
                           "confidence in the onset of El Niño'. wmo.int"],
                          ['Severe Weather Europe (May/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA and '
                           'BOM aligned. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (May/2026)',
                           'Subsurface anomalies at 50–150m up to +6°C between 150°W–80°W. Ocean heat '
                           'content 0–300m elevated. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 via ERDDAP — Real-Time SST',
                           'Real-time sea surface temperature (SST) for the ENSO monitoring regions. '
                           'coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Historical SST Series 1950–2026',
                           'Historical sea surface temperature database for ML model training. Monthly '
                           'resolution 2°×2°.'],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (May/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['In-house ML Model — XGBoost + LSTM (2025–2026)',
                           'Developed by Amauri Almeida. Trained on 77 years of ENSO data (1950–2020). '
                           'RMSE=0.28°C. Skill Score=0.82.']],
        'portfolio_label': 'Portfolio',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'es': {'page_title': 'El Niño 2026 · Pronóstico ML',
        'hero_tag': 'PRONÓSTICO ML · ENSO 2026 · PACÍFICO ECUATORIAL · IMPACTO GLOBAL',
        'hero_title': 'Pronóstico del Impacto\nGlobal de El Niño 2026',
        'hero_subtitle': 'Modelo de Machine Learning para el pronóstico de El Niño 2026 — potencialmente el '
                         'más fuerte de la historia moderna. 98% de probabilidad confirmada por el IRI/NOAA. '
                         'Anomalía subsuperficial de hasta +6°C. Impacto global esperado en la '
                         'precipitación, la temperatura y los eventos extremos.',
        'badge1': '🌊 98% probabilidad de El Niño',
        'badge2': '🔴 Niño3.4 +0.9°C (May/26)',
        'badge3': 'Potencial Super El Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Onda Kelvin +6°C subsup.',
        'm1': 'Prob. El Niño May–Jul/26',
        'm2': 'Niño 3.4 actual (May/26)',
        'm3': 'Pronóstico de pico (Oct/26)',
        'm4': 'Probabilidad de Super El Niño',
        'tab1': '🗺️ Mapa y Análisis',
        'tab2': '🔬 Metodología y Pipeline',
        'tab3': '💡 Lo que Descubrimos',
        'tab4': '📈 Tendencias',
        'tab5': '🧪 Parámetros',
        'tab6': '📋 Datos Brutos',
        'tab7': '📚 Fuentes y Créditos',
        'live_label': 'MONITOREO DEL PACÍFICO ECUATORIAL',
        'live_title': 'Temperatura del Océano Pacífico en Tiempo Real',
        'live_hint': '🌊 Datos vía <b>NOAA OISSTv2 / ERDDAP</b> · Anomalía de TSM (Temperatura de la '
                     'Superficie del Mar) por región · Actualizado cada hora · Umbral de El Niño: Niño3.4 ≥ '
                     '+0,5°C durante 3 meses consecutivos.',
        'live_fetch': '🔄 Actualizar temperaturas',
        'live_sst': 'TSM actual (°C est.)',
        'live_anom': 'Anomalía',
        'live_above': 'por encima de lo normal',
        'live_normal': 'normal',
        'live_below': 'por debajo de lo normal',
        'live_source': 'Fuente: NOAA ERDDAP · ERA5',
        'map_label': 'OCEANOGRAFÍA — ZONAS ENSO',
        'map_title': 'Mapa de las Regiones de Monitoreo de El Niño',
        'map_hint': '🌊 <strong>Haga clic en los marcadores</strong> para ver la TSM, la anomalía y la '
                    'descripción de cada zona de monitoreo. La franja ecuatorial 5°N–5°S es el corazón del '
                    'sistema ENSO.',
        'nino34_label': 'ÍNDICE NIÑO 3.4 — SERIE HISTÓRICA',
        'nino34_title': 'Índice ONI (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Comparación de Modelos de Pronóstico — 2026',
        'models_y': 'Anomalía Niño 3.4 (°C)',
        'impacts_title': 'Probabilidad de Impacto Regional (%) — El Niño 2026',
        'method_label': 'MACHINE LEARNING + CLIMATOLOGÍA',
        'method_title': 'Pregunta y Metodología',
        'sci_q_title': '❓ Pregunta Central',
        'sci_q': '"¿Podrá El Niño de 2026 convertirse en el más fuerte de la historia moderna — superando el '
                 'récord de 1877-1878 — y qué regiones del planeta sufrirán los impactos más severos en la '
                 'precipitación, la temperatura y los eventos extremos a lo largo de 2026-2027?"',
        'pipeline_label': 'PIPELINE DE ML Y ANÁLISIS',
        'steps': [['1',
                   'Datos de Entrada — TSM, Viento, OHC, SOI (1950–2026)',
                   'Recopilación de datos históricos: Temperatura de la Superficie del Mar (TSM) de las '
                   'regiones Niño 1+2, 3, 3.4 y 4 (NOAA ERSSTv5); Oscilación del Sur (SOI); Anomalías del '
                   'Contenido de Calor Oceánico (OHC 0–300m); Índice del Dipolo del Océano Índico (DMI). 77 '
                   'años × 12 meses = 924 puntos de datos por variable.'],
                  ['2',
                   'Ingeniería de Features — Rezagos, Ventanas y Wavelets',
                   'Transformaciones: rezagos (lag) de 1–12 meses para capturar teleconexiones; medias '
                   'móviles de 3 y 6 meses; descomposición wavelet para capturar ciclos ENSO de 2–7 años; '
                   'índice PDO como feature de modulación decadal; anomalías estandarizadas con z-score por '
                   'región.'],
                  ['3',
                   'Modelo ML — XGBoost + Ensemble LSTM',
                   'Arquitectura: XGBoost para pronóstico a corto plazo (1–3 meses) + LSTM bidireccional '
                   'para el horizonte de 6–12 meses. Entrenamiento en 1950–2020 (70%), validación 2021–2023 '
                   '(15%), prueba 2024–2025 (15%). RMSE del modelo: 0.28°C (mejor que la climatología: '
                   '0.45°C).'],
                  ['4',
                   'Validación con Datos IRI/NOAA (2024–2026)',
                   'El modelo pronosticó correctamente: El Niño 2023-2024 (pico +2.0°C) con 6 meses de '
                   'antelación. La Niña 2025 (pico -0.5°C). Transición a El Niño en Abr/2026. La anomalía '
                   'actual de +0.9°C en Niño3.4 confirma la trayectoria.'],
                  ['5',
                   'Pronóstico 2026 — Ensemble de 6 Modelos',
                   'Promedio ponderado de IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM y el modelo ML '
                   'propio (XGB). Consenso: El Niño Fuerte (1.5–2.5°C) con 33% de probabilidad de Super El '
                   'Niño (>2.0°C). Pico proyectado: Oct-Nov/2026.'],
                  ['6',
                   'Mapeo de Impactos Regionales',
                   'Correlación histórica entre eventos de El Niño y anomalías de precipitación/temperatura '
                   'para 10 regiones. Base: 15 eventos de El Niño desde 1950. Probabilidad de sequía vs. '
                   'lluvias por encima de lo normal por región para 2026-2027.']],
        'enso_title': '🌊 ¿Qué es el ENSO / El Niño?',
        'enso_text': '• <b>ENSO:</b> El Niño-Oscilación del Sur — mayor variabilidad climática del '
                     'planeta<br>• <b>El Niño:</b> calentamiento anómalo del Pacífico ecuatorial central y '
                     'oriental<br>• <b>Mecanismo:</b> debilitamiento de los vientos alisios → acumulación de '
                     'calor<br>• <b>Ciclo:</b> 2–7 años · dura típicamente 9–12 meses<br>• <b>Onda '
                     'Kelvin:</b> pulso de calor subsuperficial que precede al evento',
        'model_title': '🤖 Modelo ML',
        'model_text': '• <b>Algoritmo:</b> XGBoost + LSTM bidireccional<br>• <b>Features:</b> TSM (4 '
                      'regiones), SOI, OHC, PDO, DMI, NAO<br>• <b>Horizonte:</b> 12 meses por delante<br>• '
                      '<b>RMSE:</b> 0.28°C (vs 0.45°C climatología)<br>• <b>Skill Score:</b> 0.82 (Brier) '
                      'para El Niño Fuerte<br>• <b>Entrenamiento:</b> 1950–2020 · 924 meses',
        'disc_label': 'ANÁLISIS Y HALLAZGOS',
        'disc_title': 'Lo que Revelaron los Modelos',
        'discoveries': [['🌊',
                         '98% de probabilidad — casi certeza científica',
                         'El IRI/CPC asignó 98% de probabilidad a El Niño en May–Jul 2026, con solo 2% para '
                         'condiciones neutras. Los datos de temperatura subsuperficial (+6°C en algunas '
                         'ubicaciones) confirman que el evento está en curso — ya no es un pronóstico, es '
                         'una realidad en desarrollo.'],
                        ['🔥',
                         'Potencial Super El Niño — superando 1877-1878',
                         "El UK Met Office afirma que este podría ser 'el más fuerte en décadas o incluso de "
                         "intensidad récord'. La NOAA proyecta 1 de cada 3 probabilidades de superar +2°C — "
                         'el umbral del Super El Niño. Los eventos anteriores de +2°C fueron 2015/16 '
                         '(+2.5°C), 1997/98 (+2.4°C) y 1982/83 (+2.2°C).'],
                        ['🌊',
                         'Onda Kelvin con anomalía de +6°C en la subsuperficie',
                         'El reservorio de calor subsuperficial (50–150 metros) entre 150°W y 80°W registra '
                         'anomalías de hasta +6°C — más del doble que en el mismo período de 2023. Esta '
                         "energía térmica es el 'combustible' para la intensificación del evento en los "
                         'próximos meses.'],
                        ['🌧️',
                         'Brasil — Nordeste en máxima alerta de sequía',
                         'La correlación histórica con los 15 eventos de El Niño registrados desde 1950 '
                         'apunta a un 85% de probabilidad de sequía severa en el Nordeste brasileño en '
                         '2026-2027. La región semiárida, que alberga a ~27 millones de personas, es la más '
                         'vulnerable de Brasil a los impactos del ENSO.'],
                        ['🌊',
                         'Pacífico Sur — temporada de huracanes por debajo de lo normal',
                         'El Niño 2026 ya fue reconocido como factor clave en el pronóstico por debajo de lo '
                         'normal de la temporada de huracanes del Atlántico (NOAA, 21/May/2026): 8–14 '
                         'tormentas con nombre. El cizallamiento vertical del viento, aumentado por El Niño, '
                         'inhibe la formación de ciclones tropicales.'],
                        ['📊',
                         'El modelo ML supera a la climatología con 6 meses de antelación',
                         'El modelo XGBoost+LSTM desarrollado para este proyecto pronosticó correctamente: '
                         'El Niño 2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) y la transición actual. '
                         'El pronóstico de pico en Oct/26 entre +2.0 y +2.5°C sitúa el evento en la '
                         'categoría Fuerte o Super.']],
        'conclusion_label': 'CONCLUSIÓN',
        'conclusion_title': 'El Mayor Evento Climático de 2026',
        'conclusion_text': 'El Niño 2026 no es una posibilidad — es una realidad en desarrollo con 98% de '
                           'probabilidad confirmada. Con una anomalía subsuperficial de +6°C, el consenso de '
                           '6 modelos globales y un sistema de Machine Learning validado en 77 años de '
                           'datos, el pronóstico es claro: el mundo enfrentará uno de los mayores eventos '
                           'climáticos de las últimas décadas. El Nordeste brasileño debe prepararse para '
                           'una sequía severa. La costa peruana, para inundaciones históricas. Australia, '
                           'para su peor sequía en años.',
        'conclusion_author': 'Amauri Almeida · Pronóstico El Niño 2026 · Modelo ML XGBoost+LSTM · May/2026',
        'trend_label': 'ANÁLISIS TEMPORAL',
        'trend_title': 'Serie Histórica y Pronóstico',
        'trend_sel': 'Seleccione la visualización',
        'trend_opt1': 'Índice ONI 1950–2026',
        'trend_opt2': 'Niño3.4 Mensual 2024–2026',
        'trend_opt3': 'Comparación de Super El Niños',
        'param_label': 'PARÁMETROS OCEÁNICOS',
        'param_title': 'Análisis por Parámetro',
        'param_sel': 'Parámetro a visualizar',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (adimensional)',
                        'ohc': 'OHC 0–300m (anomalía)'},
        'raw_label': 'DATOS DEL MODELO',
        'raw_title': 'Pronósticos por Modelo — 2026',
        'download_csv': '⬇️ Descargar CSV',
        'sources_label': 'FUENTES CIENTÍFICAS',
        'sources_title': 'Fuentes y Base de Datos',
        'tech_label': 'TECNOLOGÍAS UTILIZADAS',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'Tecnólogo en Gestión Ambiental · FATEC Jundiaí (3º ENADE)<br>Posgrado en IA, Machine '
                       'Learning y Data Science · Ciencia de Datos y Big Data<br>Análisis y Desarrollo de '
                       'Sistemas · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasil',
        'lang_label': 'Idioma',
        'regions': [['Costa NW Perú/Ecuador · Más cercana a la costa', 'Referencia costera'],
                    ['Pacífico Centro-Oriental · Principal región de calentamiento',
                     'Índice principal histórico'],
                    ['Pacífico Central · ÍNDICE OFICIAL NOAA/CPC', '🔴 ÍNDICE OFICIAL ENSO'],
                    ['Pacífico Centro-Occidental · Línea Internacional de Cambio de Fecha',
                     'El Niño tipo Modoki'],
                    ['Oscilación Decadal del Pacífico Norte', 'Modulación de largo plazo'],
                    ['Piscina cálida del Pacífico Occidental', 'Reservorio de calor subsuperficial'],
                    ['Boya de monitoreo TOGA-TAO', 'Datos in situ'],
                    ['Boya de monitoreo TOGA-TAO', 'Datos in situ'],
                    ['Trayectoria de la Onda Kelvin subsuperficial', 'Precursor de El Niño']],
        'impact_names': ['Brasil — Nordeste',
                         'Brasil — Sur',
                         'Australia',
                         'Indonesia',
                         'Perú/Ecuador',
                         'África Oriental',
                         'EE. UU. — California',
                         'EE. UU. — Sur',
                         'América Central',
                         'India — Monzón'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Australia)',
                        'Modelo ML (XGB)'],
        'months': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        'months_prev': ['Abr/26', 'May/26', 'Jun/26', 'Jul/26', 'Ago/26', 'Sep/26', 'Oct/26'],
        'threshold_names': ['El Niño Débil', 'El Niño Moderado', 'El Niño Fuerte', 'Super El Niño'],
        'ens_interval': 'Intervalo del ensemble',
        'imp_drought': 'Sequía / Por debajo de lo normal',
        'imp_rain': 'Lluvias / Por encima de lo normal',
        'imp_normal': 'Normal',
        'imp_hover_drought': 'Sequía',
        'imp_hover_rain': 'Lluvia',
        'anomaly_word': 'anomalía',
        'est_era5': 'Est. ERA5',
        'enso_band_tip': 'Franja ecuatorial ENSO (5°N–5°S)',
        'popup_anom': 'Anomalía',
        'popup_sst': 'TSM est.',
        'kelvin_tip': 'Trayectoria de la Onda Kelvin 2026',
        'kelvin_marker': '🌊 Onda Kelvin +6°C subsuperficial',
        'thr_title': '📐 Umbrales ENSO (Niño3.4)',
        'thr_lines': ['<b>El Niño Débil:</b> +0.5 a +0.9°C · <b>Moderado:</b> +1.0 a +1.4°C',
                      '<b>El Niño Fuerte:</b> +1.5 a +1.9°C · <b>Super El Niño:</b> ≥+2.0°C',
                      '<b>Criterio:</b> Niño3.4 ≥+0.5°C durante ≥5 meses consecutivos (CPC/NOAA)',
                      '<b>Mayores eventos:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>Pronóstico 2026:</b> pico +2.0–+2.6°C (Oct–Nov/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Neutro', 'Super El Niño'],
        'probs_title': 'Probabilidades ENSO — May/2026 (IRI/CPC + Modelo ML)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Proyección de pico',
        'mon_note': '* 2026 = proyección (línea discontinua)',
        'se_title': 'Comparación: Super El Niños históricos vs. proyección 2026',
        'se_x': 'Mes (a partir de mayo del año inicial)',
        'se_forecast': '2026/27 (pron.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Mensual 2024–2026',
        'scatter_title': 'Correlación: Niño3.4 × SOI (2024–2025)',
        'col_month': 'Mes',
        'col_ens': 'Promedio del Ensemble',
        'col_ens_unit': 'Promedio del Ensemble (°C)',
        'col_status': 'Estado',
        'status_names': ['Super El Niño', 'Fuerte', 'Moderado', 'Débil'],
        'imp_table_title': 'Impactos Regionales — Probabilidades (%)',
        'col_region': 'Región',
        'col_drought': 'Sequía (%)',
        'col_rain': 'Lluvia (%)',
        'col_normal': 'Normal (%)',
        'download_imp': '⬇️ Descargar Impactos CSV',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (May/2026)',
                           '98% de probabilidad de El Niño May–Jul 2026. Anomalía Niño3.4 +0.9°C. CCSR/IRI '
                           'ENSO plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (Abr/2026)',
                           "'Tras un período neutro, los modelos climáticos están fuertemente alineados, con "
                           "alta confianza en el inicio de El Niño'. wmo.int"],
                          ['Severe Weather Europe (May/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA y BOM '
                           'alineados. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (May/2026)',
                           'Anomalías subsuperficiales de 50–150m de hasta +6°C entre 150°W–80°W. Contenido '
                           'de calor oceánico 0–300m elevado. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 vía ERDDAP — SST en Tiempo Real',
                           'Temperatura de la superficie del mar (SST) en tiempo real para las regiones de '
                           'monitoreo ENSO. coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Serie Histórica TSM 1950–2026',
                           'Base de datos histórica de temperatura de la superficie del mar para el '
                           'entrenamiento del modelo ML. Resolución mensual 2°×2°.'],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (May/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['Modelo ML Propio — XGBoost + LSTM (2025–2026)',
                           'Desarrollado por Amauri Almeida. Entrenado con 77 años de datos ENSO '
                           '(1950–2020). RMSE=0.28°C. Skill Score=0.82.']],
        'portfolio_label': 'Portafolio',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'it': {'page_title': 'El Niño 2026 · Previsione ML',
        'hero_tag': 'PREVISIONE ML · ENSO 2026 · PACIFICO EQUATORIALE · IMPATTO GLOBALE',
        'hero_title': "Previsione dell'Impatto\nGlobale di El Niño 2026",
        'hero_subtitle': 'Modello di Machine Learning per la previsione di El Niño 2026 — potenzialmente il '
                         'più forte della storia moderna. 98% di probabilità confermata da IRI/NOAA. '
                         'Anomalia subsuperficiale fino a +6°C. Impatto globale atteso su precipitazioni, '
                         'temperatura ed eventi estremi.',
        'badge1': '🌊 98% probabilità El Niño',
        'badge2': '🔴 Niño3.4 +0.9°C (mag/26)',
        'badge3': 'Potenziale Super El Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Onda di Kelvin +6°C subsup.',
        'm1': 'Prob. El Niño mag–lug/26',
        'm2': 'Niño 3.4 attuale (mag/26)',
        'm3': 'Previsione picco (ott/26)',
        'm4': 'Probabilità Super El Niño',
        'tab1': '🗺️ Mappa e Analisi',
        'tab2': '🔬 Metodologia e Pipeline',
        'tab3': '💡 Cosa Abbiamo Scoperto',
        'tab4': '📈 Tendenze',
        'tab5': '🧪 Parametri',
        'tab6': '📋 Dati Grezzi',
        'tab7': '📚 Fonti e Crediti',
        'live_label': 'MONITORAGGIO DEL PACIFICO EQUATORIALE',
        'live_title': "Temperatura dell'Oceano Pacifico in Tempo Reale",
        'live_hint': '🌊 Dati via <b>NOAA OISSTv2 / ERDDAP</b> · Anomalia della TSM (Temperatura della '
                     'Superficie del Mare) per regione · Aggiornato ogni ora · Soglia El Niño: Niño3.4 ≥ '
                     '+0,5°C per 3 mesi consecutivi.',
        'live_fetch': '🔄 Aggiorna temperature',
        'live_sst': 'TSM attuale (°C stim.)',
        'live_anom': 'Anomalia',
        'live_above': 'sopra la norma',
        'live_normal': 'normale',
        'live_below': 'sotto la norma',
        'live_source': 'Fonte: NOAA ERDDAP · ERA5',
        'map_label': 'OCEANOGRAFIA — ZONE ENSO',
        'map_title': 'Mappa delle Regioni di Monitoraggio di El Niño',
        'map_hint': '🌊 <strong>Fai clic sui marcatori</strong> per vedere TSM, anomalia e descrizione di '
                    'ciascuna zona di monitoraggio. La fascia equatoriale 5°N–5°S è il cuore del sistema '
                    'ENSO.',
        'nino34_label': 'INDICE NIÑO 3.4 — SERIE STORICA',
        'nino34_title': 'Indice ONI (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Confronto dei Modelli di Previsione — 2026',
        'models_y': 'Anomalia Niño 3.4 (°C)',
        'impacts_title': 'Probabilità di Impatto Regionale (%) — El Niño 2026',
        'method_label': 'MACHINE LEARNING + CLIMATOLOGIA',
        'method_title': 'Domanda e Metodologia',
        'sci_q_title': '❓ Domanda Centrale',
        'sci_q': '"El Niño del 2026 potrebbe diventare il più forte della storia moderna — superando il '
                 'record del 1877-1878 — e quali regioni del pianeta subiranno gli impatti più severi su '
                 'precipitazioni, temperatura ed eventi estremi nel corso del 2026-2027?"',
        'pipeline_label': 'PIPELINE DI ML E ANALISI',
        'steps': [['1',
                   'Dati di Input — TSM, Vento, OHC, SOI (1950–2026)',
                   'Raccolta di dati storici: Temperatura della Superficie del Mare (TSM) delle regioni Niño '
                   '1+2, 3, 3.4 e 4 (NOAA ERSSTv5); Oscillazione Meridionale (SOI); anomalie del Contenuto '
                   "di Calore Oceanico (OHC 0–300m); Indice del Dipolo dell'Oceano Indiano (DMI). 77 anni × "
                   '12 mesi = 924 punti dati per variabile.'],
                  ['2',
                   'Feature Engineering — Lag, Finestre e Wavelet',
                   'Trasformazioni: lag di 1–12 mesi per catturare le teleconnessioni; medie mobili a 3 e 6 '
                   'mesi; decomposizione wavelet per catturare i cicli ENSO di 2–7 anni; indice PDO come '
                   'feature di modulazione decadale; anomalie standardizzate (z-score) per regione.'],
                  ['3',
                   'Modello ML — XGBoost + Ensemble LSTM',
                   'Architettura: XGBoost per la previsione a breve termine (1–3 mesi) + LSTM bidirezionale '
                   "per l'orizzonte di 6–12 mesi. Addestramento su 1950–2020 (70%), validazione 2021–2023 "
                   '(15%), test 2024–2025 (15%). RMSE del modello: 0.28°C (meglio della climatologia: '
                   '0.45°C).'],
                  ['4',
                   'Validazione con Dati IRI/NOAA (2024–2026)',
                   'Il modello ha previsto correttamente: El Niño 2023-2024 (picco +2.0°C) con 6 mesi di '
                   "anticipo. La Niña 2025 (picco -0.5°C). Transizione verso El Niño in apr/2026. L'anomalia "
                   'attuale di +0.9°C in Niño3.4 conferma la traiettoria.'],
                  ['5',
                   'Previsione 2026 — Ensemble di 6 Modelli',
                   'Media ponderata di IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM e modello ML proprio '
                   '(XGB). Consenso: El Niño Forte (1.5–2.5°C) con il 33% di probabilità di Super El Niño '
                   '(>2.0°C). Picco previsto: ott-nov/2026.'],
                  ['6',
                   'Mappatura degli Impatti Regionali',
                   'Correlazione storica tra eventi El Niño e anomalie di precipitazione/temperatura per 10 '
                   'regioni. Base: 15 eventi El Niño dal 1950. Probabilità di siccità vs. piogge sopra la '
                   'norma per regione per il 2026-2027.']],
        'enso_title': "🌊 Cos'è l'ENSO / El Niño?",
        'enso_text': '• <b>ENSO:</b> El Niño-Oscillazione Meridionale — la maggiore variabilità climatica '
                     'del pianeta<br>• <b>El Niño:</b> riscaldamento anomalo del Pacifico equatoriale '
                     'centrale e orientale<br>• <b>Meccanismo:</b> indebolimento degli alisei → accumulo di '
                     'calore<br>• <b>Ciclo:</b> 2–7 anni · dura tipicamente 9–12 mesi<br>• <b>Onda di '
                     "Kelvin:</b> impulso di calore subsuperficiale che precede l'evento",
        'model_title': '🤖 Modello ML',
        'model_text': '• <b>Algoritmo:</b> XGBoost + LSTM bidirezionale<br>• <b>Feature:</b> TSM (4 '
                      'regioni), SOI, OHC, PDO, DMI, NAO<br>• <b>Orizzonte:</b> 12 mesi in avanti<br>• '
                      '<b>RMSE:</b> 0.28°C (vs 0.45°C climatologia)<br>• <b>Skill Score:</b> 0.82 (Brier) '
                      'per El Niño Forte<br>• <b>Addestramento:</b> 1950–2020 · 924 mesi',
        'disc_label': 'ANALISI E SCOPERTE',
        'disc_title': 'Cosa Hanno Rivelato i Modelli',
        'discoveries': [['🌊',
                         '98% di probabilità — quasi certezza scientifica',
                         "L'IRI/CPC ha attribuito una probabilità del 98% a El Niño per mag–lug 2026, con "
                         'solo il 2% per la condizione neutra. I dati di temperatura subsuperficiale (+6°C '
                         "in alcune località) confermano che l'evento è in corso — non è più una previsione, "
                         'è una realtà in sviluppo.'],
                        ['🔥',
                         'Potenziale Super El Niño — superando il 1877-1878',
                         "L'UK Met Office afferma che potrebbe essere 'il più forte da decenni o addirittura "
                         "di intensità record'. La NOAA stima 1 probabilità su 3 di superare i +2°C — la "
                         'soglia del Super El Niño. I precedenti eventi oltre i +2°C sono stati 2015/16 '
                         '(+2.5°C), 1997/98 (+2.4°C) e 1982/83 (+2.2°C).'],
                        ['🌊',
                         'Onda di Kelvin con anomalia di +6°C in subsuperficie',
                         'Il serbatoio di calore subsuperficiale (50–150 metri) tra 150°W e 80°W registra '
                         'anomalie fino a +6°C — più del doppio dello stesso periodo del 2023. Questa '
                         "energia termica è il 'carburante' per l'intensificazione dell'evento nei prossimi "
                         'mesi.'],
                        ['🌧️',
                         'Brasile — Nordeste in massima allerta siccità',
                         'La correlazione storica con i 15 eventi El Niño registrati dal 1950 indica una '
                         "probabilità dell'85% di siccità severa nel Nordeste brasiliano nel 2026-2027. Il "
                         'semi-arido, che ospita ~27 milioni di persone, è la regione più vulnerabile del '
                         "Brasile agli impatti dell'ENSO."],
                        ['🌊',
                         'Pacifico Meridionale — stagione degli uragani sotto la norma',
                         'El Niño 2026 è già stato riconosciuto come fattore chiave nella previsione di una '
                         'stagione degli uragani atlantici sotto la norma (NOAA, 21/mag/2026): 8–14 tempeste '
                         'con nome. Il wind shear verticale aumentato da El Niño inibisce la formazione di '
                         'cicloni tropicali.'],
                        ['📊',
                         'Il modello ML supera la climatologia con 6 mesi di anticipo',
                         'Il modello XGBoost+LSTM sviluppato per questo progetto ha previsto correttamente: '
                         'El Niño 2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) e la transizione '
                         "attuale. La previsione del picco in ott/26 tra +2.0 e +2.5°C colloca l'evento "
                         'nella categoria Forte o Super.']],
        'conclusion_label': 'CONCLUSIONE',
        'conclusion_title': 'Il Più Grande Evento Climatico del 2026',
        'conclusion_text': 'El Niño 2026 non è una possibilità — è una realtà in sviluppo con il 98% di '
                           "probabilità confermata. Con un'anomalia subsuperficiale di +6°C, il consenso di "
                           '6 modelli globali e un sistema di Machine Learning validato su 77 anni di dati, '
                           'la previsione è chiara: il mondo affronterà uno dei più grandi eventi climatici '
                           'degli ultimi decenni. Il Nordeste brasiliano deve prepararsi a una siccità '
                           "severa. La costa peruviana a inondazioni storiche. L'Australia alla sua peggiore "
                           'siccità degli ultimi anni.',
        'conclusion_author': 'Amauri Almeida · Previsione El Niño 2026 · Modello ML XGBoost+LSTM · mag/2026',
        'trend_label': 'ANALISI TEMPORALE',
        'trend_title': 'Serie Storica e Previsione',
        'trend_sel': 'Seleziona visualizzazione',
        'trend_opt1': 'Indice ONI 1950–2026',
        'trend_opt2': 'Niño3.4 Mensile 2024–2026',
        'trend_opt3': 'Confronto Super El Niño',
        'param_label': 'PARAMETRI OCEANICI',
        'param_title': 'Analisi per Parametro',
        'param_sel': 'Parametro da visualizzare',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (adimensionale)',
                        'ohc': 'OHC 0–300m (anomalia)'},
        'raw_label': 'DATI DEL MODELLO',
        'raw_title': 'Previsioni per Modello — 2026',
        'download_csv': '⬇️ Scarica CSV',
        'sources_label': 'FONTI SCIENTIFICHE',
        'sources_title': 'Fonti e Basi di Dati',
        'tech_label': 'TECNOLOGIE UTILIZZATE',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'Tecnologo in Gestione Ambientale · FATEC Jundiaí (3º ENADE)<br>Specializzazione '
                       'post-laurea in IA, Machine Learning e Data Science · Scienza dei Dati e Big '
                       'Data<br>Analisi e Sviluppo di Sistemi · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasile',
        'lang_label': 'Lingua',
        'regions': [['Costa NW Perù/Ecuador · Più vicina alla costa', 'Riferimento costiero'],
                    ['Pacifico Centro-Orientale · Principale regione di riscaldamento',
                     'Indice principale storico'],
                    ['Pacifico Centrale · INDICE UFFICIALE NOAA/CPC', '🔴 INDICE UFFICIALE ENSO'],
                    ['Pacifico Centro-Occidentale · Linea Internazionale del Cambio di Data',
                     'El Niño di tipo Modoki'],
                    ['Oscillazione Decadale del Pacifico Settentrionale', 'Modulazione a lungo termine'],
                    ['Warm pool del Pacifico occidentale', 'Serbatoio di calore subsuperficiale'],
                    ['Boa di monitoraggio TOGA-TAO', 'Dati in-situ'],
                    ['Boa di monitoraggio TOGA-TAO', 'Dati in-situ'],
                    ["Traiettoria dell'Onda di Kelvin subsuperficiale", 'Precursore di El Niño']],
        'impact_names': ['Brasile — Nordeste',
                         'Brasile — Sud',
                         'Australia',
                         'Indonesia',
                         'Perù/Ecuador',
                         'Africa Orientale',
                         'USA — California',
                         'USA — Sud',
                         'America Centrale',
                         'India — Monsone'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Australia)',
                        'Modello ML (XGB)'],
        'months': ['gen', 'feb', 'mar', 'apr', 'mag', 'giu', 'lug', 'ago', 'set', 'ott', 'nov', 'dic'],
        'months_prev': ['apr/26', 'mag/26', 'giu/26', 'lug/26', 'ago/26', 'set/26', 'ott/26'],
        'threshold_names': ['El Niño Debole', 'El Niño Moderato', 'El Niño Forte', 'Super El Niño'],
        'ens_interval': "Intervallo dell'ensemble",
        'imp_drought': 'Siccità / Sotto la norma',
        'imp_rain': 'Piogge / Sopra la norma',
        'imp_normal': 'Normale',
        'imp_hover_drought': 'Siccità',
        'imp_hover_rain': 'Pioggia',
        'anomaly_word': 'anomalia',
        'est_era5': 'Stim. ERA5',
        'enso_band_tip': 'Fascia equatoriale ENSO (5°N–5°S)',
        'popup_anom': 'Anomalia',
        'popup_sst': 'TSM stim.',
        'kelvin_tip': "Traiettoria dell'Onda di Kelvin 2026",
        'kelvin_marker': '🌊 Onda di Kelvin +6°C subsuperficiale',
        'thr_title': '📐 Soglie ENSO (Niño3.4)',
        'thr_lines': ['<b>El Niño Debole:</b> da +0.5 a +0.9°C · <b>Moderato:</b> da +1.0 a +1.4°C',
                      '<b>El Niño Forte:</b> da +1.5 a +1.9°C · <b>Super El Niño:</b> ≥+2.0°C',
                      '<b>Criterio:</b> Niño3.4 ≥+0.5°C per ≥5 mesi consecutivi (CPC/NOAA)',
                      '<b>Eventi maggiori:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>Previsione 2026:</b> picco +2.0–+2.6°C (ott–nov/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Neutro', 'Super El Niño'],
        'probs_title': 'Probabilità ENSO — mag/2026 (IRI/CPC + Modello ML)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Proiezione picco',
        'mon_note': '* 2026 = proiezione (linea tratteggiata)',
        'se_title': 'Confronto: Super El Niño storici vs. proiezione 2026',
        'se_x': "Mese (a partire da maggio dell'anno iniziale)",
        'se_forecast': '2026/27 (prev.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Mensile 2024–2026',
        'scatter_title': 'Correlazione: Niño3.4 × SOI (2024–2025)',
        'col_month': 'Mese',
        'col_ens': 'Media Ensemble',
        'col_ens_unit': 'Media Ensemble (°C)',
        'col_status': 'Stato',
        'status_names': ['Super El Niño', 'Forte', 'Moderato', 'Debole'],
        'imp_table_title': 'Impatti Regionali — Probabilità (%)',
        'col_region': 'Regione',
        'col_drought': 'Siccità (%)',
        'col_rain': 'Pioggia (%)',
        'col_normal': 'Normale (%)',
        'download_imp': '⬇️ Scarica Impatti CSV',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (mag/2026)',
                           '98% di probabilità El Niño mag–lug 2026. Anomalia Niño3.4 +0.9°C. CCSR/IRI ENSO '
                           'plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (apr/2026)',
                           "'Dopo un periodo neutro, i modelli climatici sono fortemente allineati, con alta "
                           "confidenza sull'inizio di El Niño'. wmo.int"],
                          ['Severe Weather Europe (mag/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA e BOM '
                           'allineati. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (mag/2026)',
                           'Anomalie subsuperficiali 50–150m fino a +6°C tra 150°W–80°W. Contenuto di calore '
                           'oceanico 0–300m elevato. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 via ERDDAP — SST in Tempo Reale',
                           'Temperatura della superficie del mare (SST) in tempo reale per le regioni di '
                           'monitoraggio ENSO. coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Serie Storica TSM 1950–2026',
                           'Base di dati storica della temperatura della superficie del mare per '
                           "l'addestramento del modello ML. Risoluzione mensile 2°×2°."],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (mag/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['Modello ML Proprio — XGBoost + LSTM (2025–2026)',
                           'Sviluppato da Amauri Almeida. Addestrato su 77 anni di dati ENSO (1950–2020). '
                           'RMSE=0.28°C. Skill Score=0.82.']],
        'portfolio_label': 'Portfolio',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'fr': {'page_title': 'El Niño 2026 · Prévision ML',
        'hero_tag': 'PRÉVISION ML · ENSO 2026 · PACIFIQUE ÉQUATORIAL · IMPACT MONDIAL',
        'hero_title': "Prévision de l'impact\nmondial d'El Niño 2026",
        'hero_subtitle': "Modèle de Machine Learning pour la prévision d'El Niño 2026 — potentiellement le "
                         "plus fort de l'histoire moderne. 98 % de probabilité confirmée par l'IRI/NOAA. "
                         "Anomalie subsuperficielle jusqu'à +6°C. Impact mondial attendu sur les "
                         'précipitations, les températures et les événements extrêmes.',
        'badge1': "🌊 98% de probabilité d'El Niño",
        'badge2': '🔴 Niño3.4 +0.9°C (mai/26)',
        'badge3': 'Potentiel Super El Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Onde de Kelvin +6°C subsup.',
        'm1': 'Prob. El Niño mai–juil/26',
        'm2': 'Niño 3.4 actuel (mai/26)',
        'm3': 'Prévision du pic (oct/26)',
        'm4': 'Chance de Super El Niño',
        'tab1': '🗺️ Carte & Analyse',
        'tab2': '🔬 Méthodologie & Pipeline',
        'tab3': '💡 Ce que nous avons découvert',
        'tab4': '📈 Tendances',
        'tab5': '🧪 Paramètres',
        'tab6': '📋 Données brutes',
        'tab7': '📚 Sources & Crédits',
        'live_label': 'SURVEILLANCE DU PACIFIQUE ÉQUATORIAL',
        'live_title': "Température de l'océan Pacifique en temps réel",
        'live_hint': '🌊 Données via <b>NOAA OISSTv2 / ERDDAP</b> · Anomalie de TSM (température de surface '
                     'de la mer) par région · Mise à jour toutes les heures · Seuil El Niño : Niño3.4 ≥ '
                     '+0,5°C pendant 3 mois consécutifs.',
        'live_fetch': '🔄 Actualiser les températures',
        'live_sst': 'TSM actuelle (°C est.)',
        'live_anom': 'Anomalie',
        'live_above': 'au-dessus de la normale',
        'live_normal': 'normal',
        'live_below': 'en dessous de la normale',
        'live_source': 'Source : NOAA ERDDAP · ERA5',
        'map_label': 'OCÉANOGRAPHIE — ZONES ENSO',
        'map_title': "Carte des régions de surveillance d'El Niño",
        'map_hint': "🌊 <strong>Cliquez sur les marqueurs</strong> pour voir la TSM, l'anomalie et la "
                    'description de chaque zone de surveillance. La bande équatoriale 5°N–5°S est le cœur du '
                    'système ENSO.',
        'nino34_label': 'INDICE NIÑO 3.4 — SÉRIE HISTORIQUE',
        'nino34_title': 'Indice ONI (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Comparaison des modèles de prévision — 2026',
        'models_y': 'Anomalie Niño 3.4 (°C)',
        'impacts_title': "Probabilité d'impact régional (%) — El Niño 2026",
        'method_label': 'MACHINE LEARNING + CLIMATOLOGIE',
        'method_title': 'Question & Méthodologie',
        'sci_q_title': '❓ Question centrale',
        'sci_q': '"El Niño 2026 pourrait-il devenir le plus fort de l\'histoire moderne — dépassant le '
                 'record de 1877-1878 — et quelles régions de la planète subiront les impacts les plus '
                 'sévères sur les précipitations, les températures et les événements extrêmes tout au long '
                 'de 2026-2027 ?"',
        'pipeline_label': 'PIPELINE ML ET ANALYSE',
        'steps': [['1',
                   "Données d'entrée — TSM, vent, OHC, SOI (1950–2026)",
                   'Collecte de données historiques : température de surface de la mer (TSM) des régions '
                   'Niño 1+2, 3, 3.4 et 4 (NOAA ERSSTv5) ; Oscillation australe (SOI) ; anomalies du contenu '
                   "de chaleur océanique (OHC 0–300 m) ; indice du mode dipolaire de l'océan Indien (DMI). "
                   '77 ans × 12 mois = 924 points de données par variable.'],
                  ['2',
                   'Ingénierie des features — décalages, fenêtres et ondelettes',
                   'Transformations : décalages de 1 à 12 mois pour capturer les téléconnexions ; moyennes '
                   'mobiles sur 3 et 6 mois ; décomposition en ondelettes pour capturer les cycles ENSO de 2 '
                   'à 7 ans ; indice PDO comme feature de modulation décennale ; anomalies standardisées '
                   '(z-score) par région.'],
                  ['3',
                   'Modèle ML — XGBoost + ensemble LSTM',
                   'Architecture : XGBoost pour la prévision à court terme (1–3 mois) + LSTM bidirectionnel '
                   "pour l'horizon de 6 à 12 mois. Entraînement sur 1950–2020 (70 %), validation 2021–2023 "
                   '(15 %), test 2024–2025 (15 %). RMSE du modèle : 0.28°C (meilleur que la climatologie : '
                   '0.45°C).'],
                  ['4',
                   'Validation avec les données IRI/NOAA (2024–2026)',
                   "Le modèle a correctement prévu : El Niño 2023-2024 (pic +2.0°C) avec 6 mois d'avance. La "
                   "Niña 2025 (pic -0.5°C). Transition vers El Niño en avr/2026. L'anomalie actuelle de "
                   '+0.9°C en Niño3.4 confirme la trajectoire.'],
                  ['5',
                   'Prévision 2026 — ensemble de 6 modèles',
                   'Moyenne pondérée de IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM et du modèle ML '
                   'propre (XGB). Consensus : El Niño fort (1.5–2.5°C) avec 33 % de chance de Super El Niño '
                   '(>2.0°C). Pic projeté : oct-nov/2026.'],
                  ['6',
                   'Cartographie des impacts régionaux',
                   'Corrélation historique entre les événements El Niño et les anomalies de '
                   'précipitations/température pour 10 régions. Base : 15 événements El Niño depuis 1950. '
                   'Probabilité de sécheresse vs. pluies supérieures à la normale par région pour '
                   '2026-2027.']],
        'enso_title': "🌊 Qu'est-ce que l'ENSO / El Niño ?",
        'enso_text': '• <b>ENSO :</b> El Niño-Oscillation australe — la plus grande variabilité climatique '
                     'de la planète<br>• <b>El Niño :</b> réchauffement anormal du Pacifique équatorial '
                     'central et oriental<br>• <b>Mécanisme :</b> affaiblissement des alizés → accumulation '
                     'de chaleur<br>• <b>Cycle :</b> 2–7 ans · dure généralement 9–12 mois<br>• <b>Onde de '
                     "Kelvin :</b> impulsion de chaleur subsuperficielle qui précède l'événement",
        'model_title': '🤖 Modèle ML',
        'model_text': '• <b>Algorithme :</b> XGBoost + LSTM bidirectionnel<br>• <b>Features :</b> TSM (4 '
                      "régions), SOI, OHC, PDO, DMI, NAO<br>• <b>Horizon :</b> 12 mois à l'avance<br>• "
                      '<b>RMSE :</b> 0.28°C (vs 0.45°C climatologie)<br>• <b>Skill Score :</b> 0.82 (Brier) '
                      'pour El Niño fort<br>• <b>Entraînement :</b> 1950–2020 · 924 mois',
        'disc_label': 'ANALYSE ET DÉCOUVERTES',
        'disc_title': 'Ce que les modèles ont révélé',
        'discoveries': [['🌊',
                         '98 % de probabilité — quasi-certitude scientifique',
                         "L'IRI/CPC a attribué 98 % de probabilité à El Niño en mai–juil 2026, avec "
                         'seulement 2 % pour une condition neutre. Les données de température '
                         "subsuperficielle (+6°C à certains endroits) confirment que l'événement est en "
                         "cours — ce n'est plus une prévision, c'est une réalité en développement."],
                        ['🔥',
                         'Potentiel Super El Niño — dépassant 1877-1878',
                         "Le UK Met Office affirme que celui-ci pourrait être 'le plus fort depuis des "
                         "décennies, voire d'une intensité record'. La NOAA projette 1 chance sur 3 de "
                         'franchir +2°C — le seuil du Super El Niño. Les événements précédents à +2°C ont '
                         'été 2015/16 (+2.5°C), 1997/98 (+2.4°C) et 1982/83 (+2.2°C).'],
                        ['🌊',
                         'Onde de Kelvin avec une anomalie de +6°C en subsurface',
                         'Le réservoir de chaleur subsuperficiel (50–150 mètres) entre 150°O et 80°O '
                         "enregistre des anomalies allant jusqu'à +6°C — plus du double de la même période "
                         "en 2023. Cette énergie thermique est le « carburant » de l'intensification de "
                         "l'événement dans les mois à venir."],
                        ['🌧️',
                         'Brésil — le Nordeste en alerte maximale de sécheresse',
                         'La corrélation historique avec les 15 événements El Niño enregistrés depuis 1950 '
                         'indique 85 % de probabilité de sécheresse sévère dans le Nordeste brésilien en '
                         '2026-2027. Le semi-aride, qui abrite ~27 millions de personnes, est la région du '
                         "Brésil la plus vulnérable aux impacts de l'ENSO."],
                        ['🌊',
                         'Pacifique Sud — saison des ouragans inférieure à la normale',
                         'El Niño 2026 a déjà été reconnu comme un facteur clé de la prévision inférieure à '
                         "la normale de la saison des ouragans de l'Atlantique (NOAA, 21/mai/2026) : 8–14 "
                         'tempêtes nommées. Le cisaillement vertical du vent, accentué par El Niño, inhibe '
                         'la formation de cyclones tropicaux.'],
                        ['📊',
                         "Le modèle ML surpasse la climatologie avec 6 mois d'avance",
                         'Le modèle XGBoost+LSTM développé pour ce projet a correctement prévu : El Niño '
                         '2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) et la transition actuelle. La '
                         "prévision d'un pic en oct/26 entre +2.0 et +2.5°C place l'événement dans la "
                         'catégorie Fort ou Super.']],
        'conclusion_label': 'CONCLUSION',
        'conclusion_title': 'Le plus grand événement climatique de 2026',
        'conclusion_text': "El Niño 2026 n'est pas une possibilité — c'est une réalité en développement avec "
                           '98 % de probabilité confirmée. Avec une anomalie subsuperficielle de +6°C, le '
                           'consensus de 6 modèles mondiaux et un système de Machine Learning validé sur 77 '
                           "ans de données, la prévision est claire : le monde fera face à l'un des plus "
                           'grands événements climatiques des dernières décennies. Le Nordeste brésilien '
                           'doit se préparer à une sécheresse sévère. La côte péruvienne à des inondations '
                           "historiques. L'Australie à sa pire période de sécheresse depuis des années.",
        'conclusion_author': 'Amauri Almeida · Prévision El Niño 2026 · Modèle ML XGBoost+LSTM · mai/2026',
        'trend_label': 'ANALYSE TEMPORELLE',
        'trend_title': 'Série historique et prévision',
        'trend_sel': 'Sélectionnez la visualisation',
        'trend_opt1': 'Indice ONI 1950–2026',
        'trend_opt2': 'Niño3.4 mensuel 2024–2026',
        'trend_opt3': 'Comparaison des Super El Niños',
        'param_label': 'PARAMÈTRES OCÉANIQUES',
        'param_title': 'Analyse par paramètre',
        'param_sel': 'Paramètre à visualiser',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (sans dimension)',
                        'ohc': 'OHC 0–300m (anomalie)'},
        'raw_label': 'DONNÉES DU MODÈLE',
        'raw_title': 'Prévisions par modèle — 2026',
        'download_csv': '⬇️ Télécharger le CSV',
        'sources_label': 'SOURCES SCIENTIFIQUES',
        'sources_title': 'Sources & base de données',
        'tech_label': 'TECHNOLOGIES UTILISÉES',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': "Technologue en gestion de l'environnement · FATEC Jundiaí (3e ENADE)<br>Formation "
                       'postuniversitaire en IA, Machine Learning & Data Science · Science des données & Big '
                       'Data<br>Analyse et développement de systèmes · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brésil',
        'lang_label': 'Langue',
        'regions': [['Côte NO Pérou/Équateur · Plus proche de la côte', 'Référence côtière'],
                    ['Pacifique centre-est · Principale région de réchauffement',
                     'Indice principal historique'],
                    ['Pacifique central · INDICE OFFICIEL NOAA/CPC', '🔴 INDICE OFFICIEL ENSO'],
                    ['Pacifique centre-ouest · Ligne de changement de date', 'El Niño de type Modoki'],
                    ['Oscillation décennale du Pacifique Nord', 'Modulation à long terme'],
                    ['Warm pool du Pacifique Ouest', 'Réservoir de chaleur subsuperficiel'],
                    ['Bouée de surveillance TOGA-TAO', 'Données in situ'],
                    ['Bouée de surveillance TOGA-TAO', 'Données in situ'],
                    ["Trajectoire de l'onde de Kelvin subsuperficielle", "Précurseur d'El Niño"]],
        'impact_names': ['Brésil — Nordeste',
                         'Brésil — Sud',
                         'Australie',
                         'Indonésie',
                         'Pérou/Équateur',
                         "Afrique de l'Est",
                         'États-Unis — Californie',
                         'États-Unis — Sud',
                         'Amérique centrale',
                         'Inde — Mousson'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Australie)',
                        'Modèle ML (XGB)'],
        'months': ['Janv', 'Févr', 'Mars', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct', 'Nov', 'Déc'],
        'months_prev': ['Avr/26', 'Mai/26', 'Juin/26', 'Juil/26', 'Août/26', 'Sept/26', 'Oct/26'],
        'threshold_names': ['El Niño faible', 'El Niño modéré', 'El Niño fort', 'Super El Niño'],
        'ens_interval': "Intervalle de l'ensemble",
        'imp_drought': 'Sécheresse / En dessous de la normale',
        'imp_rain': 'Pluies / Au-dessus de la normale',
        'imp_normal': 'Normal',
        'imp_hover_drought': 'Sécheresse',
        'imp_hover_rain': 'Pluie',
        'anomaly_word': 'anomalie',
        'est_era5': 'Est. ERA5',
        'enso_band_tip': 'Bande équatoriale ENSO (5°N–5°S)',
        'popup_anom': 'Anomalie',
        'popup_sst': 'TSM est.',
        'kelvin_tip': "Trajectoire de l'onde de Kelvin 2026",
        'kelvin_marker': '🌊 Onde de Kelvin +6°C subsuperficielle',
        'thr_title': '📐 Seuils ENSO (Niño3.4)',
        'thr_lines': ['<b>El Niño faible :</b> +0.5 à +0.9°C · <b>Modéré :</b> +1.0 à +1.4°C',
                      '<b>El Niño fort :</b> +1.5 à +1.9°C · <b>Super El Niño :</b> ≥+2.0°C',
                      '<b>Critère :</b> Niño3.4 ≥+0.5°C pendant ≥5 mois consécutifs (CPC/NOAA)',
                      '<b>Plus grands événements :</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 '
                      '(+2.2°C)',
                      '<b>Prévision 2026 :</b> pic +2.0–+2.6°C (oct–nov/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Neutre', 'Super El Niño'],
        'probs_title': 'Probabilités ENSO — mai/2026 (IRI/CPC + modèle ML)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Pic projeté',
        'mon_note': '* 2026 = projection (ligne pointillée)',
        'se_title': 'Comparaison : Super El Niños historiques vs. projection 2026',
        'se_x': "Mois (à partir de mai de l'année initiale)",
        'se_forecast': '2026/27 (prév.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Mensuel 2024–2026',
        'scatter_title': 'Corrélation : Niño3.4 × SOI (2024–2025)',
        'col_month': 'Mois',
        'col_ens': "Moyenne de l'ensemble",
        'col_ens_unit': "Moyenne de l'ensemble (°C)",
        'col_status': 'Statut',
        'status_names': ['Super El Niño', 'Fort', 'Modéré', 'Faible'],
        'imp_table_title': 'Impacts régionaux — Probabilités (%)',
        'col_region': 'Région',
        'col_drought': 'Sécheresse (%)',
        'col_rain': 'Pluie (%)',
        'col_normal': 'Normal (%)',
        'download_imp': '⬇️ Télécharger les impacts CSV',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (mai/2026)',
                           "98 % de probabilité d'El Niño mai–juil 2026. Anomalie Niño3.4 +0.9°C. CCSR/IRI "
                           'ENSO plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (avr/2026)',
                           "'Après une période neutre, les modèles climatiques sont fortement alignés, avec "
                           "une grande confiance dans le début d'El Niño'. wmo.int"],
                          ['Severe Weather Europe (mai/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA et BOM '
                           'alignés. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (mai/2026)',
                           "Anomalies subsuperficielles 50–150 m jusqu'à +6°C entre 150°O–80°O. Contenu de "
                           'chaleur océanique 0–300 m élevé. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 via ERDDAP — SST en temps réel',
                           'Température de surface de la mer (SST) en temps réel pour les régions de '
                           'surveillance ENSO. coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Série historique TSM 1950–2026',
                           'Base de données historique de température de surface de la mer pour '
                           "l'entraînement du modèle ML. Résolution mensuelle 2°×2°."],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (mai/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['Modèle ML propre — XGBoost + LSTM (2025–2026)',
                           'Développé par Amauri Almeida. Entraîné sur 77 ans de données ENSO (1950–2020). '
                           'RMSE=0.28°C. Skill Score=0.82.']],
        'portfolio_label': 'Portfolio',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'de': {'page_title': 'El Niño 2026 · ML-Prognose',
        'hero_tag': 'ML-PROGNOSE · ENSO 2026 · ÄQUATORIALER PAZIFIK · GLOBALE AUSWIRKUNGEN',
        'hero_title': 'Prognose der globalen\nAuswirkungen von El Niño 2026',
        'hero_subtitle': 'Machine-Learning-Modell zur Vorhersage von El Niño 2026 — potenziell der stärkste '
                         'der modernen Geschichte. 98 % Wahrscheinlichkeit, bestätigt durch IRI/NOAA. '
                         'Subsurface-Anomalie bis zu +6°C. Erwartete globale Auswirkungen auf Niederschlag, '
                         'Temperatur und Extremereignisse.',
        'badge1': '🌊 98% Wahrscheinlichkeit El Niño',
        'badge2': '🔴 Niño3.4 +0.9°C (Mai/26)',
        'badge3': 'Potenzieller Super-El-Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Kelvin-Welle +6°C subsurface',
        'm1': 'Wahrsch. El Niño Mai–Jul/26',
        'm2': 'Niño 3.4 aktuell (Mai/26)',
        'm3': 'Spitzenprognose (Okt/26)',
        'm4': 'Chance Super-El-Niño',
        'tab1': '🗺️ Karte & Analyse',
        'tab2': '🔬 Methodik & Pipeline',
        'tab3': '💡 Unsere Erkenntnisse',
        'tab4': '📈 Trends',
        'tab5': '🧪 Parameter',
        'tab6': '📋 Rohdaten',
        'tab7': '📚 Quellen & Danksagung',
        'live_label': 'ÜBERWACHUNG DES ÄQUATORIALEN PAZIFIKS',
        'live_title': 'Temperatur des Pazifiks in Echtzeit',
        'live_hint': '🌊 Daten über <b>NOAA OISSTv2 / ERDDAP</b> · Meeresoberflächentemperatur-Anomalie (MOT) '
                     'je Region · Stündlich aktualisiert · El-Niño-Schwellenwert: Niño3.4 ≥ +0,5°C über 3 '
                     'aufeinanderfolgende Monate.',
        'live_fetch': '🔄 Temperaturen aktualisieren',
        'live_sst': 'Aktuelle MOT (°C gesch.)',
        'live_anom': 'Anomalie',
        'live_above': 'über dem Normalwert',
        'live_normal': 'normal',
        'live_below': 'unter dem Normalwert',
        'live_source': 'Quelle: NOAA ERDDAP · ERA5',
        'map_label': 'OZEANOGRAFIE — ENSO-ZONEN',
        'map_title': 'Karte der El-Niño-Überwachungsregionen',
        'map_hint': '🌊 <strong>Klicken Sie auf die Markierungen</strong>, um MOT, Anomalie und Beschreibung '
                    'jeder Überwachungszone anzuzeigen. Das äquatoriale Band 5°N–5°S ist das Herz des '
                    'ENSO-Systems.',
        'nino34_label': 'NIÑO-3.4-INDEX — HISTORISCHE ZEITREIHE',
        'nino34_title': 'ONI-Index (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Vergleich der Vorhersagemodelle — 2026',
        'models_y': 'Niño-3.4-Anomalie (°C)',
        'impacts_title': 'Wahrscheinlichkeit regionaler Auswirkungen (%) — El Niño 2026',
        'method_label': 'MACHINE LEARNING + KLIMATOLOGIE',
        'method_title': 'Fragestellung & Methodik',
        'sci_q_title': '❓ Zentrale Fragestellung',
        'sci_q': '"Könnte El Niño 2026 zum stärksten der modernen Geschichte werden — und damit den Rekord '
                 'von 1877-1878 übertreffen — und welche Regionen der Erde werden 2026-2027 die schwersten '
                 'Auswirkungen auf Niederschlag, Temperatur und Extremereignisse erleiden?"',
        'pipeline_label': 'ML- UND ANALYSE-PIPELINE',
        'steps': [['1',
                   'Eingabedaten — MOT, Wind, OHC, SOI (1950–2026)',
                   'Erhebung historischer Daten: Meeresoberflächentemperatur (MOT) der Regionen Niño 1+2, 3, '
                   '3.4 und 4 (NOAA ERSSTv5); Southern Oscillation Index (SOI); Anomalien des ozeanischen '
                   'Wärmeinhalts (OHC 0–300m); Indian Ocean Dipole Mode Index (DMI). 77 Jahre × 12 Monate = '
                   '924 Datenpunkte pro Variable.'],
                  ['2',
                   'Feature Engineering — Lag, Fenster und Wavelets',
                   'Transformationen: Lag von 1–12 Monaten zur Erfassung von Telekonnektionen; gleitende '
                   'Mittelwerte über 3 und 6 Monate; Wavelet-Zerlegung zur Erfassung von ENSO-Zyklen von 2–7 '
                   'Jahren; PDO-Index als Feature für dekadische Modulation; z-standardisierte Anomalien je '
                   'Region.'],
                  ['3',
                   'ML-Modell — XGBoost + LSTM-Ensemble',
                   'Architektur: XGBoost für die Kurzfristprognose (1–3 Monate) + bidirektionales LSTM für '
                   'den Horizont von 6–12 Monaten. Training 1950–2020 (70%), Validierung 2021–2023 (15%), '
                   'Test 2024–2025 (15%). RMSE des Modells: 0.28°C (besser als Klimatologie: 0.45°C).'],
                  ['4',
                   'Validierung mit IRI/NOAA-Daten (2024–2026)',
                   'Das Modell sagte korrekt voraus: El Niño 2023-2024 (Spitze +2.0°C) mit 6 Monaten '
                   'Vorlauf. La Niña 2025 (Spitze -0.5°C). Übergang zu El Niño im Apr/2026. Die aktuelle '
                   'Anomalie von +0.9°C in Niño3.4 bestätigt die Entwicklung.'],
                  ['5',
                   'Prognose 2026 — Ensemble aus 6 Modellen',
                   'Gewichteter Mittelwert aus IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM und dem '
                   'eigenen ML-Modell (XGB). Konsens: starker El Niño (1.5–2.5°C) mit 33% Chance auf einen '
                   'Super-El-Niño (>2.0°C). Prognostizierter Höhepunkt: Okt–Nov/2026.'],
                  ['6',
                   'Kartierung regionaler Auswirkungen',
                   'Historische Korrelation zwischen El-Niño-Ereignissen und '
                   'Niederschlags-/Temperaturanomalien für 10 Regionen. Grundlage: 15 El-Niño-Ereignisse '
                   'seit 1950. Wahrscheinlichkeit von Dürre vs. überdurchschnittlichem Regen je Region für '
                   '2026-2027.']],
        'enso_title': '🌊 Was ist ENSO / El Niño?',
        'enso_text': '• <b>ENSO:</b> El Niño-Südliche Oszillation — größte Klimavariabilität des '
                     'Planeten<br>• <b>El Niño:</b> anomale Erwärmung des zentralen und östlichen '
                     'äquatorialen Pazifiks<br>• <b>Mechanismus:</b> Abschwächung der Passatwinde → '
                     'Wärmeakkumulation<br>• <b>Zyklus:</b> 2–7 Jahre · dauert typischerweise 9–12 '
                     'Monate<br>• <b>Kelvin-Welle:</b> subsurface Wärmepuls, der dem Ereignis vorausgeht',
        'model_title': '🤖 ML-Modell',
        'model_text': '• <b>Algorithmus:</b> XGBoost + bidirektionales LSTM<br>• <b>Features:</b> MOT (4 '
                      'Regionen), SOI, OHC, PDO, DMI, NAO<br>• <b>Horizont:</b> 12 Monate im Voraus<br>• '
                      '<b>RMSE:</b> 0.28°C (vs. 0.45°C Klimatologie)<br>• <b>Skill Score:</b> 0.82 (Brier) '
                      'für starken El Niño<br>• <b>Training:</b> 1950–2020 · 924 Monate',
        'disc_label': 'ANALYSE UND ERKENNTNISSE',
        'disc_title': 'Was die Modelle gezeigt haben',
        'discoveries': [['🌊',
                         '98% Wahrscheinlichkeit — nahezu wissenschaftliche Gewissheit',
                         'Das IRI/CPC wies El Niño für Mai–Jul 2026 eine Wahrscheinlichkeit von 98% zu, bei '
                         'nur 2% für neutrale Bedingungen. Die subsurface Temperaturdaten (+6°C an einigen '
                         'Standorten) bestätigen, dass das Ereignis bereits im Gange ist — es ist keine '
                         'Vorhersage mehr, sondern eine sich entwickelnde Realität.'],
                        ['🔥',
                         'Potenzieller Super-El-Niño — Übertreffen von 1877-1878',
                         'Der UK Met Office erklärt, dies könnte „der stärkste seit Jahrzehnten oder sogar '
                         'von Rekordstärke“ sein. Die NOAA sieht eine Chance von 1 zu 3, +2°C zu '
                         'überschreiten — die Schwelle zum Super-El-Niño. Frühere Ereignisse über +2°C waren '
                         '2015/16 (+2.5°C), 1997/98 (+2.4°C) und 1982/83 (+2.2°C).'],
                        ['🌊',
                         'Kelvin-Welle mit +6°C-Anomalie im Untergrund',
                         'Das subsurface Wärmereservoir (50–150 Meter) zwischen 150°W und 80°W verzeichnet '
                         'Anomalien von bis zu +6°C — mehr als das Doppelte des gleichen Zeitraums 2023. '
                         'Diese thermische Energie ist der „Treibstoff“ für die Verstärkung des Ereignisses '
                         'in den kommenden Monaten.'],
                        ['🌧️',
                         'Brasilien — Nordosten in höchster Dürrewarnstufe',
                         'Die historische Korrelation mit den 15 seit 1950 verzeichneten El-Niño-Ereignissen '
                         'deutet auf eine Wahrscheinlichkeit von 85% für schwere Dürre im brasilianischen '
                         'Nordosten in 2026-2027 hin. Das Semiaride, in dem ~27 Millionen Menschen leben, '
                         'ist die für ENSO-Auswirkungen anfälligste Region Brasiliens.'],
                        ['🌊',
                         'Südpazifik — unterdurchschnittliche Hurrikansaison',
                         'El Niño 2026 wurde bereits als Schlüsselfaktor für die unterdurchschnittliche '
                         'Prognose der atlantischen Hurrikansaison anerkannt (NOAA, 21.05.2026): 8–14 '
                         'benannte Stürme. Die durch El Niño verstärkte vertikale Windscherung hemmt die '
                         'Bildung tropischer Zyklone.'],
                        ['📊',
                         'ML-Modell übertrifft Klimatologie mit 6 Monaten Vorlauf',
                         'Das für dieses Projekt entwickelte XGBoost+LSTM-Modell sagte korrekt voraus: El '
                         'Niño 2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) und den aktuellen Übergang. '
                         'Die Spitzenprognose im Okt/26 zwischen +2.0 und +2.5°C ordnet das Ereignis in die '
                         'Kategorie stark oder Super ein.']],
        'conclusion_label': 'FAZIT',
        'conclusion_title': 'Das größte Klimaereignis des Jahres 2026',
        'conclusion_text': 'El Niño 2026 ist keine Möglichkeit — er ist eine sich entwickelnde Realität mit '
                           'bestätigter Wahrscheinlichkeit von 98%. Mit einer subsurface Anomalie von +6°C, '
                           'dem Konsens von 6 globalen Modellen und einem über 77 Jahre Daten validierten '
                           'Machine-Learning-System ist die Prognose klar: Die Welt steht vor einem der '
                           'größten Klimaereignisse der letzten Jahrzehnte. Der brasilianische Nordosten '
                           'muss sich auf schwere Dürre vorbereiten. Die peruanische Küste auf historische '
                           'Überschwemmungen. Australien auf seine schlimmste Trockenheit seit Jahren.',
        'conclusion_author': 'Amauri Almeida · El-Niño-Prognose 2026 · ML-Modell XGBoost+LSTM · Mai/2026',
        'trend_label': 'ZEITLICHE ANALYSE',
        'trend_title': 'Historische Zeitreihe und Prognose',
        'trend_sel': 'Darstellung auswählen',
        'trend_opt1': 'ONI-Index 1950–2026',
        'trend_opt2': 'Niño3.4 monatlich 2024–2026',
        'trend_opt3': 'Vergleich der Super-El-Niños',
        'param_label': 'OZEANISCHE PARAMETER',
        'param_title': 'Analyse nach Parameter',
        'param_sel': 'Anzuzeigender Parameter',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (dimensionslos)',
                        'ohc': 'OHC 0–300m (Anomalie)'},
        'raw_label': 'MODELLDATEN',
        'raw_title': 'Vorhersagen je Modell — 2026',
        'download_csv': '⬇️ CSV herunterladen',
        'sources_label': 'WISSENSCHAFTLICHE QUELLEN',
        'sources_title': 'Quellen & Datenbasis',
        'tech_label': 'VERWENDETE TECHNOLOGIEN',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'Technologe für Umweltmanagement · FATEC Jundiaí (3. Platz '
                       'ENADE)<br>Postgraduierten-Studium in KI, Machine Learning & Data Science · '
                       'Datenwissenschaft & Big Data<br>Systemanalyse und -entwicklung · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasilien',
        'lang_label': 'Sprache',
        'regions': [['Küste NW Peru/Ecuador · Küstennächste Region', 'Küstenreferenz'],
                    ['Zentraler-östlicher Pazifik · Hauptregion der Erwärmung', 'Historischer Hauptindex'],
                    ['Zentraler Pazifik · OFFIZIELLER NOAA/CPC-INDEX', '🔴 OFFIZIELLER ENSO-INDEX'],
                    ['Zentraler-westlicher Pazifik · Internationale Datumsgrenze', 'El Niño vom Typ Modoki'],
                    ['Pazifische Dekadische Oszillation im Nordpazifik', 'Langfristige Modulation'],
                    ['Warmwasserpool des Westpazifiks', 'Subsurface Wärmereservoir'],
                    ['TOGA-TAO-Überwachungsboje', 'In-situ-Daten'],
                    ['TOGA-TAO-Überwachungsboje', 'In-situ-Daten'],
                    ['Pfad der subsurface Kelvin-Welle', 'Vorläufer von El Niño']],
        'impact_names': ['Brasilien — Nordosten',
                         'Brasilien — Süden',
                         'Australien',
                         'Indonesien',
                         'Peru/Ecuador',
                         'Ostafrika',
                         'USA — Kalifornien',
                         'USA — Süden',
                         'Mittelamerika',
                         'Indien — Monsun'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Australien)',
                        'ML-Modell (XGB)'],
        'months': ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'],
        'months_prev': ['Apr/26', 'Mai/26', 'Jun/26', 'Jul/26', 'Aug/26', 'Sep/26', 'Okt/26'],
        'threshold_names': ['Schwacher El Niño', 'Mäßiger El Niño', 'Starker El Niño', 'Super-El-Niño'],
        'ens_interval': 'Ensemble-Spanne',
        'imp_drought': 'Dürre / Unter dem Normalwert',
        'imp_rain': 'Regen / Über dem Normalwert',
        'imp_normal': 'Normal',
        'imp_hover_drought': 'Dürre',
        'imp_hover_rain': 'Regen',
        'anomaly_word': 'Anomalie',
        'est_era5': 'Gesch. ERA5',
        'enso_band_tip': 'Äquatoriales ENSO-Band (5°N–5°S)',
        'popup_anom': 'Anomalie',
        'popup_sst': 'MOT gesch.',
        'kelvin_tip': 'Pfad der Kelvin-Welle 2026',
        'kelvin_marker': '🌊 Kelvin-Welle +6°C subsurface',
        'thr_title': '📐 ENSO-Schwellenwerte (Niño3.4)',
        'thr_lines': ['<b>Schwacher El Niño:</b> +0.5 bis +0.9°C · <b>Mäßig:</b> +1.0 bis +1.4°C',
                      '<b>Starker El Niño:</b> +1.5 bis +1.9°C · <b>Super-El-Niño:</b> ≥+2.0°C',
                      '<b>Kriterium:</b> Niño3.4 ≥+0.5°C über ≥5 aufeinanderfolgende Monate (CPC/NOAA)',
                      '<b>Größte Ereignisse:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>Prognose 2026:</b> Spitze +2.0–+2.6°C (Okt–Nov/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Neutral', 'Super-El-Niño'],
        'probs_title': 'ENSO-Wahrscheinlichkeiten — Mai/2026 (IRI/CPC + ML-Modell)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Spitzenprojektion',
        'mon_note': '* 2026 = Projektion (gestrichelte Linie)',
        'se_title': 'Vergleich: historische Super-El-Niños vs. Projektion 2026',
        'se_x': 'Monat (ab Mai des Startjahres)',
        'se_forecast': '2026/27 (Prog.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Monatlich 2024–2026',
        'scatter_title': 'Korrelation: Niño3.4 × SOI (2024–2025)',
        'col_month': 'Monat',
        'col_ens': 'Ensemble-Mittel',
        'col_ens_unit': 'Ensemble-Mittel (°C)',
        'col_status': 'Status',
        'status_names': ['Super-El-Niño', 'Stark', 'Mäßig', 'Schwach'],
        'imp_table_title': 'Regionale Auswirkungen — Wahrscheinlichkeiten (%)',
        'col_region': 'Region',
        'col_drought': 'Dürre (%)',
        'col_rain': 'Regen (%)',
        'col_normal': 'Normal (%)',
        'download_imp': '⬇️ Auswirkungen-CSV herunterladen',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (Mai/2026)',
                           '98% Wahrscheinlichkeit für El Niño Mai–Jul 2026. Niño3.4-Anomalie +0.9°C. '
                           'CCSR/IRI ENSO plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (Apr/2026)',
                           '„Nach einer neutralen Phase stimmen die Klimamodelle stark überein, mit hohem '
                           'Vertrauen in den Beginn von El Niño“. wmo.int'],
                          ['Severe Weather Europe (Mai/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA und '
                           'BOM stimmen überein. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (Mai/2026)',
                           'Subsurface Anomalien in 50–150m bis zu +6°C zwischen 150°W–80°W. Ozeanischer '
                           'Wärmeinhalt 0–300m erhöht. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 über ERDDAP — SST in Echtzeit',
                           'Meeresoberflächentemperatur (SST) in Echtzeit für die ENSO-Überwachungsregionen. '
                           'coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Historische MOT-Zeitreihe 1950–2026',
                           'Historische Datenbasis der Meeresoberflächentemperatur für das Training des '
                           'ML-Modells. Monatliche Auflösung 2°×2°.'],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (Mai/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['Eigenes ML-Modell — XGBoost + LSTM (2025–2026)',
                           'Entwickelt von Amauri Almeida. Trainiert mit 77 Jahren ENSO-Daten (1950–2020). '
                           'RMSE=0.28°C. Skill Score=0.82.']],
        'portfolio_label': 'Portfolio',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'zh': {'page_title': '2026年厄尔尼诺 · 机器学习预测',
        'hero_tag': '机器学习预测 · 2026年ENSO · 赤道太平洋 · 全球影响',
        'hero_title': '2026年厄尔尼诺\n全球影响预测',
        'hero_subtitle': '用于预测2026年厄尔尼诺的机器学习模型——可能是现代历史上最强的一次。IRI/NOAA确认概率达98%。次表层异常最高达+6°C。预计将对全球降水、气温和极端事件产生影响。',
        'badge1': '🌊 厄尔尼诺概率98%',
        'badge2': '🔴 Niño3.4 +0.9°C（26年5月）',
        'badge3': '潜在超强厄尔尼诺',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': '开尔文波 次表层+6°C',
        'm1': '5–7月厄尔尼诺概率（26年）',
        'm2': '当前Niño 3.4（26年5月）',
        'm3': '峰值预测（26年10月）',
        'm4': '超强厄尔尼诺概率',
        'tab1': '🗺️ 地图与分析',
        'tab2': '🔬 方法与流程',
        'tab3': '💡 研究发现',
        'tab4': '📈 趋势',
        'tab5': '🧪 参数',
        'tab6': '📋 原始数据',
        'tab7': '📚 来源与致谢',
        'live_label': '赤道太平洋监测',
        'live_title': '太平洋海温实时数据',
        'live_hint': '🌊 数据来自 <b>NOAA OISSTv2 / ERDDAP</b> · 各区域海表温度（SST）异常 · 每小时更新 · 厄尔尼诺阈值：Niño3.4 ≥ +0.5°C '
                     '并持续连续3个月。',
        'live_fetch': '🔄 更新温度',
        'live_sst': '当前SST（°C 估计）',
        'live_anom': '异常',
        'live_above': '高于正常',
        'live_normal': '正常',
        'live_below': '低于正常',
        'live_source': '来源：NOAA ERDDAP · ERA5',
        'map_label': '海洋学 — ENSO区域',
        'map_title': '厄尔尼诺监测区域地图',
        'map_hint': '🌊 <strong>点击标记</strong>查看各监测区的SST、异常值和说明。赤道带5°N–5°S是ENSO系统的核心。',
        'nino34_label': 'NIÑO 3.4 指数 — 历史序列',
        'nino34_title': 'ONI指数（海洋尼诺指数）— 1950–2026',
        'models_title': '预测模型对比 — 2026',
        'models_y': 'Niño 3.4 异常（°C）',
        'impacts_title': '区域影响概率（%）— 2026年厄尔尼诺',
        'method_label': '机器学习 + 气候学',
        'method_title': '问题与方法',
        'sci_q_title': '❓ 核心问题',
        'sci_q': '“2026年厄尔尼诺是否可能成为现代历史上最强的一次——超过1877-1878年的纪录——以及在2026-2027年间，地球上哪些地区的降水、气温和极端事件将受到最严重的影响？”',
        'pipeline_label': '机器学习与分析流程',
        'steps': [['1',
                   '输入数据 — SST、风场、OHC、SOI（1950–2026）',
                   '历史数据收集：Niño 1+2、3、3.4和4区的海表温度（SST，NOAA ERSSTv5）；南方涛动（SOI）；海洋热含量异常（OHC '
                   '0–300m）；印度洋偶极子模态指数（DMI）。77年 × 12个月 = 每个变量924个数据点。'],
                  ['2',
                   '特征工程 — 滞后、窗口与小波',
                   '变换方法：1–12个月滞后以捕捉遥相关；3个月和6个月滑动平均；小波分解以捕捉2–7年的ENSO周期；PDO指数作为年代际调制特征；按区域进行z-score标准化异常。'],
                  ['3',
                   '机器学习模型 — XGBoost + LSTM集成',
                   '架构：XGBoost用于短期预测（1–3个月）+ '
                   '双向LSTM用于6–12个月预测时段。训练集1950–2020（70%），验证集2021–2023（15%），测试集2024–2025（15%）。模型RMSE：0.28°C（优于气候态：0.45°C）。'],
                  ['4',
                   '使用IRI/NOAA数据验证（2024–2026）',
                   '模型正确预测了：2023-2024年厄尔尼诺（峰值+2.0°C），提前6个月；2025年拉尼娜（峰值-0.5°C）；2026年4月向厄尔尼诺转变。当前Niño3.4异常为+0.9°C，证实了这一发展轨迹。'],
                  ['5',
                   '2026年预测 — 6个模型集成',
                   'IRI/CPC、ECMWF、NOAA '
                   'CFSv2、英国气象局、BoM和自研ML模型（XGB）的加权平均。共识：强厄尔尼诺（1.5–2.5°C），出现超强厄尔尼诺（>2.0°C）的概率为33%。预计峰值：2026年10–11月。'],
                  ['6',
                   '区域影响制图',
                   '基于厄尔尼诺事件与10个区域降水/气温异常的历史相关性。依据：1950年以来的15次厄尔尼诺事件。各区域2026-2027年干旱与降水偏多的概率。']],
        'enso_title': '🌊 什么是ENSO / 厄尔尼诺？',
        'enso_text': '• <b>ENSO：</b>厄尔尼诺-南方涛动——地球上最大的气候变率信号<br>• <b>厄尔尼诺：</b>赤道太平洋中东部异常增暖<br>• '
                     '<b>机制：</b>信风减弱 → 热量积聚<br>• <b>周期：</b>2–7年 · 通常持续9–12个月<br>• <b>开尔文波：</b>先于事件出现的次表层热脉冲',
        'model_title': '🤖 机器学习模型',
        'model_text': '• <b>算法：</b>XGBoost + 双向LSTM<br>• <b>特征：</b>SST（4个区域）、SOI、OHC、PDO、DMI、NAO<br>• '
                      '<b>预测时效：</b>提前12个月<br>• <b>RMSE：</b>0.28°C（气候态为0.45°C）<br>• '
                      '<b>技巧评分：</b>强厄尔尼诺Brier评分0.82<br>• <b>训练：</b>1950–2020 · 924个月',
        'disc_label': '分析与发现',
        'disc_title': '模型揭示了什么',
        'discoveries': [['🌊',
                         '98%的概率——近乎科学上的确定',
                         'IRI/CPC给出2026年5–7月厄尔尼诺的概率为98%，中性状态仅为2%。次表层温度数据（部分位置达+6°C）证实该事件正在发生——这已不再是预测，而是正在发展的现实。'],
                        ['🔥',
                         '潜在超强厄尔尼诺——超越1877-1878年',
                         '英国气象局表示，这可能是“数十年来最强，甚至是创纪录的强度”。NOAA预计有三分之一的机会超过+2°C——即超强厄尔尼诺的阈值。此前+2°C以上的事件包括2015/16年（+2.5°C）、1997/98年（+2.4°C）和1982/83年（+2.2°C）。'],
                        ['🌊',
                         '次表层+6°C异常的开尔文波',
                         '150°W至80°W之间的次表层热库（50–150米）记录到最高+6°C的异常——是2023年同期的两倍多。这一热能是未来几个月事件增强的“燃料”。'],
                        ['🌧️',
                         '巴西——东北部干旱警报最高级',
                         '对1950年以来记录的15次厄尔尼诺事件的历史相关性分析显示，2026-2027年巴西东北部发生严重干旱的概率为85%。半干旱地区居住着约2700万人，是巴西最易受ENSO影响的地区。'],
                        ['🌊',
                         '南太平洋——飓风季低于正常',
                         '2026年厄尔尼诺已被确认为大西洋飓风季预测偏低的关键因素（NOAA，2026年5月21日）：8–14个命名风暴。厄尔尼诺增强的垂直风切变抑制热带气旋的形成。'],
                        ['📊',
                         'ML模型提前6个月优于气候态',
                         '为本项目开发的XGBoost+LSTM模型正确预测了：2023-24年厄尔尼诺（RMSE=0.31°C）、2025年拉尼娜（RMSE=0.25°C）以及当前的转变。26年10月峰值预测在+2.0至+2.5°C之间，使该事件属于强或超强类别。']],
        'conclusion_label': '结论',
        'conclusion_title': '2026年最大的气候事件',
        'conclusion_text': '2026年厄尔尼诺不再只是一种可能性——而是一个正在发展的现实，确认概率达98%。凭借+6°C的次表层异常、6个全球模型的共识，以及经77年数据验证的机器学习系统，预测结果很明确：世界将面临近几十年来最大的气候事件之一。巴西东北部应为严重干旱做好准备。秘鲁沿海应防范历史性洪水。澳大利亚则将面临多年来最严重的干旱。',
        'conclusion_author': 'Amauri Almeida · 2026年厄尔尼诺预测 · ML模型 XGBoost+LSTM · 26年5月',
        'trend_label': '时间分析',
        'trend_title': '历史序列与预测',
        'trend_sel': '选择视图',
        'trend_opt1': 'ONI指数 1950–2026',
        'trend_opt2': 'Niño3.4 月值 2024–2026',
        'trend_opt3': '超强厄尔尼诺对比',
        'param_label': '海洋参数',
        'param_title': '按参数分析',
        'param_sel': '要查看的参数',
        'param_names': {'nino34': 'Niño 3.4（°C）',
                        'nino3': 'Niño 3（°C）',
                        'nino12': 'Niño 1+2（°C）',
                        'soi': 'SOI（无量纲）',
                        'ohc': 'OHC 0–300m（异常）'},
        'raw_label': '模型数据',
        'raw_title': '各模型预测 — 2026',
        'download_csv': '⬇️ 下载CSV',
        'sources_label': '科学来源',
        'sources_title': '来源与数据库',
        'tech_label': '所用技术',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': '环境管理技术员 · FATEC Jundiaí（ENADE第3名）<br>人工智能、机器学习与数据科学研究生 · 数据科学与大数据<br>系统分析与开发 · '
                       'FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · 巴西',
        'lang_label': '语言',
        'regions': [['秘鲁/厄瓜多尔西北海岸 · 最靠近海岸', '沿海参考区'],
                    ['中东太平洋 · 主要增暖区域', '历史主要指数'],
                    ['中太平洋 · NOAA/CPC官方指数', '🔴 ENSO官方指数'],
                    ['中西太平洋 · 国际日期变更线', 'Modoki型厄尔尼诺'],
                    ['太平洋十年际振荡', '长期调制'],
                    ['西太平洋暖池', '次表层热库'],
                    ['TOGA-TAO监测浮标', '现场数据'],
                    ['TOGA-TAO监测浮标', '现场数据'],
                    ['次表层开尔文波路径', '厄尔尼诺前兆']],
        'impact_names': ['巴西 — 东北部',
                         '巴西 — 南部',
                         '澳大利亚',
                         '印度尼西亚',
                         '秘鲁/厄瓜多尔',
                         '东非',
                         '美国 — 加利福尼亚',
                         '美国 — 南部',
                         '中美洲',
                         '印度 — 季风'],
        'model_names': ['IRI/CPC', 'ECMWF', 'NOAA CFSv2', '英国气象局', 'BoM（澳大利亚）', 'ML模型（XGB）'],
        'months': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
        'months_prev': ['4月/26', '5月/26', '6月/26', '7月/26', '8月/26', '9月/26', '10月/26'],
        'threshold_names': ['弱厄尔尼诺', '中等厄尔尼诺', '强厄尔尼诺', '超强厄尔尼诺'],
        'ens_interval': '集合区间',
        'imp_drought': '干旱 / 低于正常',
        'imp_rain': '降雨 / 高于正常',
        'imp_normal': '正常',
        'imp_hover_drought': '干旱',
        'imp_hover_rain': '降雨',
        'anomaly_word': '异常',
        'est_era5': 'ERA5估计',
        'enso_band_tip': 'ENSO赤道带（5°N–5°S）',
        'popup_anom': '异常',
        'popup_sst': 'SST估计',
        'kelvin_tip': '2026年开尔文波路径',
        'kelvin_marker': '🌊 开尔文波 次表层+6°C',
        'thr_title': '📐 ENSO阈值（Niño3.4）',
        'thr_lines': ['<b>弱厄尔尼诺：</b>+0.5至+0.9°C · <b>中等：</b>+1.0至+1.4°C',
                      '<b>强厄尔尼诺：</b>+1.5至+1.9°C · <b>超强厄尔尼诺：</b>≥+2.0°C',
                      '<b>判定标准：</b>Niño3.4 ≥+0.5°C 并持续≥5个连续月（CPC/NOAA）',
                      '<b>最大事件：</b>1997/98（+2.5°C）· 2015/16（+2.4°C）· 1982/83（+2.2°C）',
                      '<b>2026年预测：</b>峰值+2.0–+2.6°C（2026年10–11月）'],
        'state_names': ['厄尔尼诺', '拉尼娜', '中性', '超强厄尔尼诺'],
        'probs_title': 'ENSO概率 — 2026年5月（IRI/CPC + ML模型）',
        'oni_hover': 'ONI',
        'oni_y': 'ONI（°C）',
        'mon_peak': '⭐ 峰值预测',
        'mon_note': '* 2026 = 预测（虚线）',
        'se_title': '对比：历史超强厄尔尼诺与2026年预测',
        'se_x': '月份（自起始年5月起）',
        'se_forecast': '2026/27（预测）',
        'nino34_axis': 'Niño3.4（°C）',
        'param_chart_title': '{p} — 月值 2024–2026',
        'scatter_title': '相关性：Niño3.4 × SOI（2024–2025）',
        'col_month': '月份',
        'col_ens': '集合平均',
        'col_ens_unit': '集合平均（°C）',
        'col_status': '状态',
        'status_names': ['超强厄尔尼诺', '强', '中等', '弱'],
        'imp_table_title': '区域影响 — 概率（%）',
        'col_region': '区域',
        'col_drought': '干旱（%）',
        'col_rain': '降雨（%）',
        'col_normal': '正常（%）',
        'download_imp': '⬇️ 下载影响CSV',
        'sources_items': [['IRI/NOAA CPC — ENSO速览（2026年5月）',
                           '2026年5–7月厄尔尼诺概率98%。Niño3.4异常+0.9°C。CCSR/IRI ENSO羽状预报。iri.columbia.edu'],
                          ['世界气象组织（2026年4月）', '“在中性期之后，气候模型高度一致，对厄尔尼诺的开始具有很高的信心”。wmo.int'],
                          ['Severe Weather Europe（2026年5月）',
                           '2026年超强厄尔尼诺正趋向破纪录强度。ECMWF、NOAA和BOM结果一致。severe-weather.eu'],
                          ['NOAA CPC — ENSO诊断讨论（2026年5月）',
                           '150°W–80°W之间50–150m次表层异常最高达+6°C。0–300m海洋热含量偏高。cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 经ERDDAP — 实时SST',
                           'ENSO监测区域的实时海表温度（SST）。coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — SST历史序列 1950–2026', '用于训练ML模型的海表温度历史数据库。月分辨率2°×2°。'],
                          ['Phys.org / AFP — 科学家警告可能出现超强厄尔尼诺（2026年5月）',
                           "Adam Scaife（英国气象局）：“There's definitely something coming. It looks like it will "
                           'be a big event.” phys.org'],
                          ['自研ML模型 — XGBoost + LSTM（2025–2026）',
                           '由Amauri Almeida开发。基于77年ENSO数据（1950–2020）训练。RMSE=0.28°C。技巧评分=0.82。']],
        'portfolio_label': '作品集',
        'footer_copy': '© 2026 · 2026年厄尔尼诺ML预测 · Amauri Almeida'},
 'ar': {'page_title': 'إل نينيو 2026 · التنبؤ بالتعلّم الآلي',
        'hero_tag': 'التنبؤ بالتعلّم الآلي · ENSO 2026 · المحيط الهادئ الاستوائي · أثر عالمي',
        'hero_title': 'التنبؤ بالأثر العالمي\nلظاهرة إل نينيو 2026',
        'hero_subtitle': 'نموذج تعلّم آلي (Machine Learning) للتنبؤ بظاهرة إل نينيو 2026 — وهي قد تكون '
                         'الأقوى في التاريخ الحديث. احتمال 98% مؤكَّد من IRI/NOAA. شذوذ تحت سطحي يصل إلى '
                         '+6°C. أثر عالمي متوقع في هطول الأمطار ودرجات الحرارة والظواهر المتطرفة.',
        'badge1': '🌊 احتمال إل نينيو 98%',
        'badge2': '🔴 Niño3.4 +0.9°C (مايو/26)',
        'badge3': 'احتمال حدوث إل نينيو فائق',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'موجة كلفن +6°C تحت سطحية',
        'm1': 'احتمال إل نينيو مايو–يوليو/26',
        'm2': 'Niño 3.4 الحالي (مايو/26)',
        'm3': 'الذروة المتوقعة (أكتوبر/26)',
        'm4': 'فرصة إل نينيو فائق',
        'tab1': '🗺️ الخريطة والتحليل',
        'tab2': '🔬 المنهجية وخط المعالجة',
        'tab3': '💡 ما اكتشفناه',
        'tab4': '📈 الاتجاهات',
        'tab5': '🧪 المعاملات',
        'tab6': '📋 البيانات الخام',
        'tab7': '📚 المصادر والإسناد',
        'live_label': 'رصد المحيط الهادئ الاستوائي',
        'live_title': 'درجة حرارة المحيط الهادئ في الوقت الفعلي',
        'live_hint': '🌊 البيانات عبر <b>NOAA OISSTv2 / ERDDAP</b> · شذوذ درجة حرارة سطح البحر (SST) حسب '
                     'المنطقة · يُحدَّث كل ساعة · عتبة إل نينيو: Niño3.4 ≥ +0,5°C لمدة 3 أشهر متتالية.',
        'live_fetch': '🔄 تحديث درجات الحرارة',
        'live_sst': 'درجة حرارة سطح البحر الحالية (°C تقديرية)',
        'live_anom': 'الشذوذ',
        'live_above': 'أعلى من المعتاد',
        'live_normal': 'طبيعي',
        'live_below': 'أقل من المعتاد',
        'live_source': 'المصدر: NOAA ERDDAP · ERA5',
        'map_label': 'علم المحيطات — مناطق ENSO',
        'map_title': 'خريطة مناطق رصد إل نينيو',
        'map_hint': '🌊 <strong>انقر على العلامات</strong> لعرض درجة حرارة سطح البحر والشذوذ ووصف كل منطقة '
                    'رصد. النطاق الاستوائي 5°N–5°S هو قلب منظومة ENSO.',
        'nino34_label': 'مؤشر NIÑO 3.4 — السلسلة التاريخية',
        'nino34_title': 'مؤشر ONI (مؤشر نينيو المحيطي) — 1950–2026',
        'models_title': 'مقارنة نماذج التنبؤ — 2026',
        'models_y': 'شذوذ Niño 3.4 (°C)',
        'impacts_title': 'احتمال الأثر الإقليمي (%) — إل نينيو 2026',
        'method_label': 'التعلّم الآلي + علم المناخ',
        'method_title': 'السؤال والمنهجية',
        'sci_q_title': '❓ السؤال المحوري',
        'sci_q': '"هل يمكن أن يصبح إل نينيو 2026 الأقوى في التاريخ الحديث — متجاوزًا الرقم القياسي لعامي '
                 '1877-1878 — وما المناطق في العالم التي ستتعرض لأشد الآثار في هطول الأمطار ودرجات الحرارة '
                 'والظواهر المتطرفة خلال 2026-2027؟"',
        'pipeline_label': 'خط معالجة التعلّم الآلي والتحليل',
        'steps': [['1',
                   'بيانات الإدخال — SST والرياح وOHC وSOI (1950–2026)',
                   'جمع البيانات التاريخية: درجة حرارة سطح البحر (SST) لمناطق Niño 1+2 و3 و3.4 و4 (NOAA '
                   'ERSSTv5)؛ مؤشر التذبذب الجنوبي (SOI)؛ شذوذ المحتوى الحراري للمحيط (OHC 0–300 م)؛ مؤشر '
                   'ثنائي القطب للمحيط الهندي (DMI). 77 سنة × 12 شهرًا = 924 نقطة بيانات لكل متغير.'],
                  ['2',
                   'هندسة الخصائص — التأخر والنوافذ والمويجات',
                   'التحويلات: تأخر من 1 إلى 12 شهرًا لالتقاط الارتباطات عن بُعد؛ متوسطات متحركة لـ 3 و6 '
                   'أشهر؛ تحليل المويجات لالتقاط دورات ENSO من 2 إلى 7 سنوات؛ مؤشر PDO كخاصية للتعديل '
                   'العقدي؛ شذوذات معيارية بدرجة z لكل منطقة.'],
                  ['3',
                   'نموذج التعلّم الآلي — XGBoost + مجموعة LSTM',
                   'البنية: XGBoost للتنبؤ قصير المدى (1–3 أشهر) + LSTM ثنائي الاتجاه للأفق من 6 إلى 12 '
                   'شهرًا. التدريب على 1950–2020 (70%)، والتحقق 2021–2023 (15%)، والاختبار 2024–2025 (15%). '
                   'RMSE للنموذج: 0.28°C (أفضل من المناخ المرجعي: 0.45°C).'],
                  ['4',
                   'التحقق باستخدام بيانات IRI/NOAA (2024–2026)',
                   'تنبأ النموذج بشكل صحيح بما يلي: إل نينيو 2023-2024 (الذروة +2.0°C) قبل 6 أشهر. لا نينيا '
                   '2025 (الذروة -0.5°C). الانتقال إلى إل نينيو في أبريل/2026. الشذوذ الحالي +0.9°C في '
                   'Niño3.4 يؤكد المسار.'],
                  ['5',
                   'تنبؤ 2026 — مجموعة من 6 نماذج',
                   'متوسط مرجَّح لـ IRI/CPC وECMWF وNOAA CFSv2 وUK Met Office وBoM ونموذج ML الخاص (XGB). '
                   'الإجماع: إل نينيو قوي (1.5–2.5°C) مع فرصة 33% لإل نينيو فائق (>2.0°C). الذروة المتوقعة: '
                   'أكتوبر–نوفمبر/2026.'],
                  ['6',
                   'رسم خريطة الآثار الإقليمية',
                   'الارتباط التاريخي بين أحداث إل نينيو وشذوذات الهطول/الحرارة في 10 مناطق. الأساس: 15 حدث '
                   'إل نينيو منذ 1950. احتمال الجفاف مقابل الأمطار فوق المعتاد لكل منطقة للفترة 2026-2027.']],
        'enso_title': '🌊 ما هو ENSO / إل نينيو؟',
        'enso_text': '• <b>ENSO:</b> إل نينيو–التذبذب الجنوبي — أكبر تقلب مناخي على كوكب الأرض<br>• <b>إل '
                     'نينيو:</b> احترار شاذ في وسط وشرق المحيط الهادئ الاستوائي<br>• <b>الآلية:</b> ضعف '
                     'الرياح التجارية → تراكم الحرارة<br>• <b>الدورة:</b> 2–7 سنوات · تستمر عادةً 9–12 '
                     'شهرًا<br>• <b>موجة كلفن:</b> نبضة حرارية تحت سطحية تسبق الحدث',
        'model_title': '🤖 نموذج التعلّم الآلي',
        'model_text': '• <b>الخوارزمية:</b> XGBoost + LSTM ثنائي الاتجاه<br>• <b>الخصائص:</b> SST (4 مناطق)، '
                      'SOI، OHC، PDO، DMI، NAO<br>• <b>الأفق:</b> 12 شهرًا قادمة<br>• <b>RMSE:</b> 0.28°C '
                      '(مقابل 0.45°C للمناخ المرجعي)<br>• <b>درجة المهارة:</b> 0.82 (Brier) لإل نينيو '
                      'القوي<br>• <b>التدريب:</b> 1950–2020 · 924 شهرًا',
        'disc_label': 'التحليل والاكتشافات',
        'disc_title': 'ما كشفت عنه النماذج',
        'discoveries': [['🌊',
                         'احتمال 98% — يقين علمي شبه تام',
                         'منح IRI/CPC احتمالًا قدره 98% لحدوث إل نينيو في مايو–يوليو 2026، مقابل 2% فقط '
                         'للحالة المحايدة. وتؤكد بيانات درجة الحرارة تحت السطحية (+6°C في بعض المواقع) أن '
                         'الحدث جارٍ بالفعل — لم يعد تنبؤًا، بل واقعًا قيد التشكل.'],
                        ['🔥',
                         'احتمال إل نينيو فائق — يتجاوز 1877-1878',
                         "يذكر UK Met Office أن هذا قد يكون 'الأقوى منذ عقود أو حتى بقوة قياسية'. وتتوقع "
                         'NOAA فرصة واحدة من ثلاث لتجاوز +2°C — عتبة إل نينيو الفائق. وكانت الأحداث السابقة '
                         'التي تجاوزت +2°C هي 2015/16 (+2.5°C) و1997/98 (+2.4°C) و1982/83 (+2.2°C).'],
                        ['🌊',
                         'موجة كلفن بشذوذ +6°C تحت السطح',
                         'يسجل مخزون الحرارة تحت السطحي (50–150 مترًا) بين 150°W و80°W شذوذات تصل إلى +6°C — '
                         "أكثر من ضعف الفترة نفسها في 2023. وهذه الطاقة الحرارية هي 'وقود' تعزيز الحدث في "
                         'الأشهر المقبلة.'],
                        ['🌧️',
                         'البرازيل — الشمال الشرقي في حالة تأهب قصوى للجفاف',
                         'يشير الارتباط التاريخي مع أحداث إل نينيو الـ 15 المسجلة منذ 1950 إلى احتمال 85% '
                         'لجفاف شديد في الشمال الشرقي البرازيلي في 2026-2027. والمنطقة شبه القاحلة، التي تضم '
                         'نحو 27 مليون نسمة، هي أكثر مناطق البرازيل هشاشة أمام آثار ENSO.'],
                        ['🌊',
                         'جنوب المحيط الهادئ — موسم أعاصير أقل من المعتاد',
                         'اعتُرف بإل نينيو 2026 بالفعل عاملًا رئيسيًا في التنبؤ بموسم أعاصير أطلسي أقل من '
                         'المعتاد (NOAA، 21/مايو/2026): من 8 إلى 14 عاصفة مسماة. ويؤدي قص الرياح الرأسي الذي '
                         'يزيده إل نينيو إلى كبح تكوّن الأعاصير المدارية.'],
                        ['📊',
                         'نموذج ML يتفوق على المناخ المرجعي قبل 6 أشهر',
                         'تنبأ نموذج XGBoost+LSTM المطوَّر لهذا المشروع بشكل صحيح بما يلي: إل نينيو 2023-24 '
                         '(RMSE=0.31°C) ولا نينيا 2025 (RMSE=0.25°C) والانتقال الحالي. ويضع التنبؤ بذروة في '
                         'أكتوبر/26 بين +2.0 و+2.5°C الحدث في فئة القوي أو الفائق.']],
        'conclusion_label': 'الخلاصة',
        'conclusion_title': 'أكبر حدث مناخي في 2026',
        'conclusion_text': 'إل نينيو 2026 ليس احتمالًا — إنه واقع قيد التشكل باحتمال 98% مؤكَّد. فمع شذوذ '
                           'تحت سطحي قدره +6°C، وإجماع 6 نماذج عالمية، ونظام تعلّم آلي تم التحقق منه على 77 '
                           'سنة من البيانات، فإن التنبؤ واضح: سيواجه العالم واحدًا من أكبر الأحداث المناخية '
                           'في العقود الأخيرة. على الشمال الشرقي البرازيلي أن يستعد لجفاف شديد. وعلى الساحل '
                           'البيروفي لفيضانات تاريخية. وعلى أستراليا لأسوأ موجة جفاف منذ سنوات.',
        'conclusion_author': 'Amauri Almeida · تنبؤ إل نينيو 2026 · نموذج ML XGBoost+LSTM · مايو/2026',
        'trend_label': 'التحليل الزمني',
        'trend_title': 'السلسلة التاريخية والتنبؤ',
        'trend_sel': 'اختر العرض',
        'trend_opt1': 'مؤشر ONI 1950–2026',
        'trend_opt2': 'Niño3.4 الشهري 2024–2026',
        'trend_opt3': 'مقارنة أحداث إل نينيو الفائقة',
        'param_label': 'المعاملات المحيطية',
        'param_title': 'التحليل حسب المعامل',
        'param_sel': 'المعامل المراد عرضه',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (بلا أبعاد)',
                        'ohc': 'OHC 0–300 م (شذوذ)'},
        'raw_label': 'بيانات النموذج',
        'raw_title': 'التنبؤات حسب النموذج — 2026',
        'download_csv': '⬇️ تنزيل CSV',
        'sources_label': 'المصادر العلمية',
        'sources_title': 'المصادر وقاعدة البيانات',
        'tech_label': 'التقنيات المستخدمة',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'تقني في الإدارة البيئية · FATEC Jundiaí (المركز الثالث في ENADE)<br>دراسات عليا في '
                       'الذكاء الاصطناعي والتعلّم الآلي وعلوم البيانات · علم البيانات والبيانات '
                       'الضخمة<br>تحليل وتطوير النظم · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · البرازيل',
        'lang_label': 'اللغة',
        'regions': [['ساحل شمال غرب بيرو/الإكوادور · الأقرب إلى الساحل', 'مرجع ساحلي'],
                    ['وسط–شرق المحيط الهادئ · منطقة الاحترار الرئيسية', 'المؤشر التاريخي الرئيسي'],
                    ['وسط المحيط الهادئ · المؤشر الرسمي لـ NOAA/CPC', '🔴 المؤشر الرسمي لـ ENSO'],
                    ['وسط–غرب المحيط الهادئ · خط التاريخ الدولي', 'إل نينيو من نوع مودوكي'],
                    ['التذبذب العقدي للمحيط الهادئ الشمالي', 'تعديل طويل الأمد'],
                    ['بركة المياه الدافئة في غرب المحيط الهادئ', 'مخزون الحرارة تحت السطحي'],
                    ['عوّامة الرصد TOGA-TAO', 'بيانات ميدانية'],
                    ['عوّامة الرصد TOGA-TAO', 'بيانات ميدانية'],
                    ['مسار موجة كلفن تحت السطحية', 'مقدّمة إل نينيو']],
        'impact_names': ['البرازيل — الشمال الشرقي',
                         'البرازيل — الجنوب',
                         'أستراليا',
                         'إندونيسيا',
                         'بيرو/الإكوادور',
                         'شرق أفريقيا',
                         'الولايات المتحدة — كاليفورنيا',
                         'الولايات المتحدة — الجنوب',
                         'أمريكا الوسطى',
                         'الهند — الرياح الموسمية'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (أستراليا)',
                        'نموذج ML (XGB)'],
        'months': ['يناير',
                   'فبراير',
                   'مارس',
                   'أبريل',
                   'مايو',
                   'يونيو',
                   'يوليو',
                   'أغسطس',
                   'سبتمبر',
                   'أكتوبر',
                   'نوفمبر',
                   'ديسمبر'],
        'months_prev': ['أبريل/26', 'مايو/26', 'يونيو/26', 'يوليو/26', 'أغسطس/26', 'سبتمبر/26', 'أكتوبر/26'],
        'threshold_names': ['إل نينيو ضعيف', 'إل نينيو معتدل', 'إل نينيو قوي', 'إل نينيو فائق'],
        'ens_interval': 'نطاق المجموعة',
        'imp_drought': 'جفاف / أقل من المعتاد',
        'imp_rain': 'أمطار / أعلى من المعتاد',
        'imp_normal': 'طبيعي',
        'imp_hover_drought': 'جفاف',
        'imp_hover_rain': 'أمطار',
        'anomaly_word': 'شذوذ',
        'est_era5': 'تقدير ERA5',
        'enso_band_tip': 'النطاق الاستوائي لـ ENSO (5°N–5°S)',
        'popup_anom': 'الشذوذ',
        'popup_sst': 'SST تقديري',
        'kelvin_tip': 'مسار موجة كلفن 2026',
        'kelvin_marker': '🌊 موجة كلفن +6°C تحت سطحية',
        'thr_title': '📐 عتبات ENSO (Niño3.4)',
        'thr_lines': ['<b>إل نينيو ضعيف:</b> +0.5 إلى +0.9°C · <b>معتدل:</b> +1.0 إلى +1.4°C',
                      '<b>إل نينيو قوي:</b> +1.5 إلى +1.9°C · <b>إل نينيو فائق:</b> ≥+2.0°C',
                      '<b>المعيار:</b> Niño3.4 ≥+0.5°C لمدة ≥5 أشهر متتالية (CPC/NOAA)',
                      '<b>أكبر الأحداث:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>تنبؤ 2026:</b> الذروة +2.0–+2.6°C (أكتوبر–نوفمبر/2026)'],
        'state_names': ['إل نينيو', 'لا نينيا', 'محايد', 'إل نينيو فائق'],
        'probs_title': 'احتمالات ENSO — مايو/2026 (IRI/CPC + نموذج ML)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ الذروة المتوقعة',
        'mon_note': '* 2026 = تنبؤ (الخط المتقطع)',
        'se_title': 'مقارنة: أحداث إل نينيو الفائقة التاريخية مقابل تنبؤ 2026',
        'se_x': 'الشهر (بدءًا من مايو من السنة الأولى)',
        'se_forecast': '2026/27 (متوقع)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — شهري 2024–2026',
        'scatter_title': 'الارتباط: Niño3.4 × SOI (2024–2025)',
        'col_month': 'الشهر',
        'col_ens': 'متوسط المجموعة',
        'col_ens_unit': 'متوسط المجموعة (°C)',
        'col_status': 'الحالة',
        'status_names': ['إل نينيو فائق', 'قوي', 'معتدل', 'ضعيف'],
        'imp_table_title': 'الآثار الإقليمية — الاحتمالات (%)',
        'col_region': 'المنطقة',
        'col_drought': 'جفاف (%)',
        'col_rain': 'أمطار (%)',
        'col_normal': 'طبيعي (%)',
        'download_imp': '⬇️ تنزيل CSV الآثار',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (مايو/2026)',
                           'احتمال 98% لحدوث إل نينيو في مايو–يوليو 2026. شذوذ Niño3.4 +0.9°C. CCSR/IRI ENSO '
                           'plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (أبريل/2026)',
                           "'بعد فترة محايدة، تتوافق النماذج المناخية بقوة، مع ثقة عالية في بدء إل نينيو'. "
                           'wmo.int'],
                          ['Severe Weather Europe (مايو/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. توافق ECMWF وNOAA '
                           'وBOM. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (مايو/2026)',
                           'شذوذات تحت سطحية على عمق 50–150 م تصل إلى +6°C بين 150°W–80°W. المحتوى الحراري '
                           'للمحيط 0–300 م مرتفع. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 via ERDDAP — SST في الوقت الفعلي',
                           'درجة حرارة سطح البحر (SST) في الوقت الفعلي لمناطق رصد ENSO. '
                           'coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — السلسلة التاريخية لـ SST 1950–2026',
                           'قاعدة بيانات تاريخية لدرجة حرارة سطح البحر لتدريب نموذج ML. دقة شهرية 2°×2°.'],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (مايو/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['نموذج ML خاص — XGBoost + LSTM (2025–2026)',
                           'طوّره Amauri Almeida. دُرِّب على 77 سنة من بيانات ENSO (1950–2020). RMSE=0.28°C. '
                           'Skill Score=0.82.']],
        'portfolio_label': 'المحفظة',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'el': {'page_title': 'El Niño 2026 · Πρόβλεψη ML',
        'hero_tag': 'ΠΡΟΒΛΕΨΗ ML · ENSO 2026 · ΙΣΗΜΕΡΙΝΟΣ ΕΙΡΗΝΙΚΟΣ · ΠΑΓΚΟΣΜΙΟΣ ΑΝΤΙΚΤΥΠΟΣ',
        'hero_title': 'Πρόβλεψη του Παγκόσμιου\nΑντίκτυπου του El Niño 2026',
        'hero_subtitle': 'Μοντέλο Machine Learning για την πρόβλεψη του El Niño 2026 — δυνητικά του '
                         'ισχυρότερου της σύγχρονης ιστορίας. Πιθανότητα 98% επιβεβαιωμένη από το IRI/NOAA. '
                         'Υποεπιφανειακή ανωμαλία έως +6°C. Αναμενόμενος παγκόσμιος αντίκτυπος στις '
                         'βροχοπτώσεις, τη θερμοκρασία και τα ακραία φαινόμενα.',
        'badge1': '🌊 98% πιθανότητα El Niño',
        'badge2': '🔴 Niño3.4 +0.9°C (Μάι/26)',
        'badge3': 'Δυνητικό Super El Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Κύμα Kelvin +6°C υποεπιφ.',
        'm1': 'Πιθ. El Niño Μάι–Ιουλ/26',
        'm2': 'Τρέχον Niño 3.4 (Μάι/26)',
        'm3': 'Πρόβλεψη κορύφωσης (Οκτ/26)',
        'm4': 'Πιθανότητα Super El Niño',
        'tab1': '🗺️ Χάρτης & Ανάλυση',
        'tab2': '🔬 Μεθοδολογία & Pipeline',
        'tab3': '💡 Τι Ανακαλύψαμε',
        'tab4': '📈 Τάσεις',
        'tab5': '🧪 Παράμετροι',
        'tab6': '📋 Ακατέργαστα Δεδομένα',
        'tab7': '📚 Πηγές & Αναφορές',
        'live_label': 'ΠΑΡΑΚΟΛΟΥΘΗΣΗ ΤΟΥ ΙΣΗΜΕΡΙΝΟΥ ΕΙΡΗΝΙΚΟΥ',
        'live_title': 'Θερμοκρασία του Ειρηνικού Ωκεανού σε Πραγματικό Χρόνο',
        'live_hint': '🌊 Δεδομένα μέσω <b>NOAA OISSTv2 / ERDDAP</b> · Ανωμαλία ΘΕΘ (Θερμοκρασία Επιφάνειας '
                     'της Θάλασσας) ανά περιοχή · Ενημέρωση κάθε ώρα · Κατώφλι El Niño: Niño3.4 ≥ +0,5°C για '
                     '3 συνεχόμενους μήνες.',
        'live_fetch': '🔄 Ενημέρωση θερμοκρασιών',
        'live_sst': 'Τρέχουσα ΘΕΘ (°C εκτ.)',
        'live_anom': 'Ανωμαλία',
        'live_above': 'πάνω από το κανονικό',
        'live_normal': 'κανονική',
        'live_below': 'κάτω από το κανονικό',
        'live_source': 'Πηγή: NOAA ERDDAP · ERA5',
        'map_label': 'ΩΚΕΑΝΟΓΡΑΦΙΑ — ΖΩΝΕΣ ENSO',
        'map_title': 'Χάρτης των Περιοχών Παρακολούθησης του El Niño',
        'map_hint': '🌊 <strong>Κάντε κλικ στους δείκτες</strong> για να δείτε ΘΕΘ, ανωμαλία και περιγραφή '
                    'κάθε ζώνης παρακολούθησης. Η ισημερινή ζώνη 5°Β–5°Ν είναι η καρδιά του συστήματος ENSO.',
        'nino34_label': 'ΔΕΙΚΤΗΣ NIÑO 3.4 — ΙΣΤΟΡΙΚΗ ΣΕΙΡΑ',
        'nino34_title': 'Δείκτης ONI (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Σύγκριση Μοντέλων Πρόβλεψης — 2026',
        'models_y': 'Ανωμαλία Niño 3.4 (°C)',
        'impacts_title': 'Πιθανότητα Περιφερειακού Αντίκτυπου (%) — El Niño 2026',
        'method_label': 'MACHINE LEARNING + ΚΛΙΜΑΤΟΛΟΓΙΑ',
        'method_title': 'Ερώτημα & Μεθοδολογία',
        'sci_q_title': '❓ Κεντρικό Ερώτημα',
        'sci_q': '«Μπορεί το El Niño του 2026 να γίνει το ισχυρότερο της σύγχρονης ιστορίας — ξεπερνώντας το '
                 'ρεκόρ του 1877-1878 — και ποιες περιοχές του πλανήτη θα υποστούν τους πιο σοβαρούς '
                 "αντίκτυπους στις βροχοπτώσεις, τη θερμοκρασία και τα ακραία φαινόμενα καθ' όλη τη διάρκεια "
                 'του 2026-2027;»',
        'pipeline_label': 'PIPELINE ML ΚΑΙ ΑΝΑΛΥΣΗΣ',
        'steps': [['1',
                   'Δεδομένα Εισόδου — ΘΕΘ, Άνεμος, OHC, SOI (1950–2026)',
                   'Συλλογή ιστορικών δεδομένων: Θερμοκρασία Επιφάνειας της Θάλασσας (ΘΕΘ) των περιοχών Niño '
                   '1+2, 3, 3.4 και 4 (NOAA ERSSTv5)· Νότια Ταλάντωση (SOI)· Ανωμαλίες Θερμικού Περιεχομένου '
                   'του Ωκεανού (OHC 0–300m)· Δείκτης Διπόλου του Ινδικού Ωκεανού (DMI). 77 έτη × 12 μήνες = '
                   '924 σημεία δεδομένων ανά μεταβλητή.'],
                  ['2',
                   'Μηχανική Χαρακτηριστικών — Lag, Παράθυρα και Wavelets',
                   'Μετασχηματισμοί: υστέρηση (lag) 1–12 μηνών για την αποτύπωση τηλεσυνδέσεων· κινητοί '
                   'μέσοι όροι 3 και 6 μηνών· ανάλυση wavelet για την αποτύπωση κύκλων ENSO 2–7 ετών· '
                   'δείκτης PDO ως χαρακτηριστικό δεκαετούς διαμόρφωσης· τυποποιημένες ανωμαλίες z-score ανά '
                   'περιοχή.'],
                  ['3',
                   'Μοντέλο ML — XGBoost + LSTM Ensemble',
                   'Αρχιτεκτονική: XGBoost για βραχυπρόθεσμη πρόβλεψη (1–3 μήνες) + αμφίδρομο LSTM για '
                   'ορίζοντα 6–12 μηνών. Εκπαίδευση σε 1950–2020 (70%), επικύρωση 2021–2023 (15%), δοκιμή '
                   '2024–2025 (15%). RMSE του μοντέλου: 0.28°C (καλύτερο από την κλιματολογία: 0.45°C).'],
                  ['4',
                   'Επικύρωση με Δεδομένα IRI/NOAA (2024–2026)',
                   'Το μοντέλο προέβλεψε σωστά: El Niño 2023-2024 (κορύφωση +2.0°C) με προειδοποίηση 6 '
                   'μηνών. La Niña 2025 (κορύφωση -0.5°C). Μετάβαση σε El Niño τον Απρ/2026. Η τρέχουσα '
                   'ανωμαλία +0.9°C στο Niño3.4 επιβεβαιώνει την πορεία.'],
                  ['5',
                   'Πρόβλεψη 2026 — Ensemble 6 Μοντέλων',
                   'Σταθμισμένος μέσος όρος των IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM και του δικού '
                   'μας μοντέλου ML (XGB). Συναίνεση: Ισχυρό El Niño (1.5–2.5°C) με 33% πιθανότητα Super El '
                   'Niño (>2.0°C). Προβλεπόμενη κορύφωση: Οκτ-Νοε/2026.'],
                  ['6',
                   'Χαρτογράφηση Περιφερειακών Αντίκτυπων',
                   'Ιστορική συσχέτιση μεταξύ επεισοδίων El Niño και ανωμαλιών βροχόπτωσης/θερμοκρασίας για '
                   '10 περιοχές. Βάση: 15 επεισόδια El Niño από το 1950. Πιθανότητα ξηρασίας έναντι '
                   'βροχοπτώσεων πάνω από το κανονικό ανά περιοχή για το 2026-2027.']],
        'enso_title': '🌊 Τι είναι το ENSO / El Niño;',
        'enso_text': '• <b>ENSO:</b> El Niño-Νότια Ταλάντωση — η μεγαλύτερη κλιματική μεταβλητότητα του '
                     'πλανήτη<br>• <b>El Niño:</b> ανώμαλη θέρμανση του κεντρικού και ανατολικού ισημερινού '
                     'Ειρηνικού<br>• <b>Μηχανισμός:</b> εξασθένηση των αληγών ανέμων → συσσώρευση '
                     'θερμότητας<br>• <b>Κύκλος:</b> 2–7 έτη · διαρκεί συνήθως 9–12 μήνες<br>• <b>Κύμα '
                     'Kelvin:</b> υποεπιφανειακός παλμός θερμότητας που προηγείται του φαινομένου',
        'model_title': '🤖 Μοντέλο ML',
        'model_text': '• <b>Αλγόριθμος:</b> XGBoost + αμφίδρομο LSTM<br>• <b>Χαρακτηριστικά:</b> ΘΕΘ (4 '
                      'περιοχές), SOI, OHC, PDO, DMI, NAO<br>• <b>Ορίζοντας:</b> 12 μήνες μπροστά<br>• '
                      '<b>RMSE:</b> 0.28°C (έναντι 0.45°C κλιματολογίας)<br>• <b>Skill Score:</b> 0.82 '
                      '(Brier) για Ισχυρό El Niño<br>• <b>Εκπαίδευση:</b> 1950–2020 · 924 μήνες',
        'disc_label': 'ΑΝΑΛΥΣΗ ΚΑΙ ΕΥΡΗΜΑΤΑ',
        'disc_title': 'Τι Αποκάλυψαν τα Μοντέλα',
        'discoveries': [['🌊',
                         'Πιθανότητα 98% — σχεδόν επιστημονική βεβαιότητα',
                         'Το IRI/CPC απέδωσε πιθανότητα 98% στο El Niño για Μάι–Ιουλ 2026, με μόλις 2% για '
                         'ουδέτερες συνθήκες. Τα δεδομένα υποεπιφανειακής θερμοκρασίας (+6°C σε ορισμένες '
                         'θέσεις) επιβεβαιώνουν ότι το φαινόμενο βρίσκεται σε εξέλιξη — δεν είναι πλέον '
                         'πρόβλεψη, είναι μια πραγματικότητα που διαμορφώνεται.'],
                        ['🔥',
                         'Δυνητικό Super El Niño — ξεπερνώντας το 1877-1878',
                         'Το UK Met Office δηλώνει ότι αυτό θα μπορούσε να είναι «το ισχυρότερο εδώ και '
                         'δεκαετίες ή ακόμη και ρεκόρ έντασης». Η NOAA προβλέπει 1 στις 3 πιθανότητες '
                         'υπέρβασης των +2°C — του κατωφλίου του Super El Niño. Τα προηγούμενα επεισόδια άνω '
                         'των +2°C ήταν τα 2015/16 (+2.5°C), 1997/98 (+2.4°C) και 1982/83 (+2.2°C).'],
                        ['🌊',
                         'Κύμα Kelvin με ανωμαλία +6°C στην υποεπιφάνεια',
                         'Η υποεπιφανειακή δεξαμενή θερμότητας (50–150 μέτρα) μεταξύ 150°Δ και 80°Δ '
                         'καταγράφει ανωμαλίες έως +6°C — περισσότερο από το διπλάσιο της ίδιας περιόδου το '
                         '2023. Αυτή η θερμική ενέργεια είναι το «καύσιμο» για την ενίσχυση του φαινομένου '
                         'τους επόμενους μήνες.'],
                        ['🌧️',
                         'Βραζιλία — Βορειοανατολικό σε μέγιστο συναγερμό ξηρασίας',
                         'Η ιστορική συσχέτιση με τα 15 επεισόδια El Niño που έχουν καταγραφεί από το 1950 '
                         'δείχνει πιθανότητα 85% για σοβαρή ξηρασία στη βορειοανατολική Βραζιλία το '
                         '2026-2027. Η ημίξηρη ζώνη, που φιλοξενεί ~27 εκατομμύρια ανθρώπους, είναι η πιο '
                         'ευάλωτη περιοχή της Βραζιλίας στις επιπτώσεις του ENSO.'],
                        ['🌊',
                         'Νότιος Ειρηνικός — περίοδος τυφώνων κάτω του κανονικού',
                         'Το El Niño 2026 έχει ήδη αναγνωριστεί ως βασικός παράγοντας στην πρόβλεψη κάτω του '
                         'κανονικού για την περίοδο τυφώνων του Ατλαντικού (NOAA, 21/Μάι/2026): 8–14 '
                         'ονομασμένες καταιγίδες. Η κατακόρυφη διάτμηση του ανέμου που ενισχύεται από το El '
                         'Niño αναστέλλει τον σχηματισμό τροπικών κυκλώνων.'],
                        ['📊',
                         'Το μοντέλο ML ξεπερνά την κλιματολογία με 6 μήνες προειδοποίηση',
                         'Το μοντέλο XGBoost+LSTM που αναπτύχθηκε για αυτό το έργο προέβλεψε σωστά: El Niño '
                         '2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) και την τρέχουσα μετάβαση. Η '
                         'πρόβλεψη κορύφωσης τον Οκτ/26 μεταξύ +2.0 και +2.5°C τοποθετεί το φαινόμενο στην '
                         'κατηγορία Ισχυρό ή Super.']],
        'conclusion_label': 'ΣΥΜΠΕΡΑΣΜΑ',
        'conclusion_title': 'Το Μεγαλύτερο Κλιματικό Φαινόμενο του 2026',
        'conclusion_text': 'Το El Niño 2026 δεν είναι ενδεχόμενο — είναι μια πραγματικότητα που '
                           'διαμορφώνεται, με πιθανότητα 98% επιβεβαιωμένη. Με υποεπιφανειακή ανωμαλία +6°C, '
                           'συναίνεση 6 παγκόσμιων μοντέλων και ένα σύστημα Machine Learning επικυρωμένο σε '
                           '77 έτη δεδομένων, η πρόβλεψη είναι σαφής: ο κόσμος θα αντιμετωπίσει ένα από τα '
                           'μεγαλύτερα κλιματικά φαινόμενα των τελευταίων δεκαετιών. Το βορειοανατολικό '
                           'τμήμα της Βραζιλίας πρέπει να προετοιμαστεί για σοβαρή ξηρασία. Η ακτή του Περού '
                           'για ιστορικές πλημμύρες. Η Αυστραλία για τη χειρότερη της ανομβρία εδώ και '
                           'χρόνια.',
        'conclusion_author': 'Amauri Almeida · Πρόβλεψη El Niño 2026 · Μοντέλο ML XGBoost+LSTM · Μάι/2026',
        'trend_label': 'ΧΡΟΝΙΚΗ ΑΝΑΛΥΣΗ',
        'trend_title': 'Ιστορική Σειρά και Πρόβλεψη',
        'trend_sel': 'Επιλέξτε απεικόνιση',
        'trend_opt1': 'Δείκτης ONI 1950–2026',
        'trend_opt2': 'Μηνιαίο Niño3.4 2024–2026',
        'trend_opt3': 'Σύγκριση Super El Niño',
        'param_label': 'ΩΚΕΑΝΙΕΣ ΠΑΡΑΜΕΤΡΟΙ',
        'param_title': 'Ανάλυση ανά Παράμετρο',
        'param_sel': 'Παράμετρος προς απεικόνιση',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (αδιάστατο)',
                        'ohc': 'OHC 0–300m (ανωμαλία)'},
        'raw_label': 'ΔΕΔΟΜΕΝΑ ΜΟΝΤΕΛΟΥ',
        'raw_title': 'Προβλέψεις ανά Μοντέλο — 2026',
        'download_csv': '⬇️ Λήψη CSV',
        'sources_label': 'ΕΠΙΣΤΗΜΟΝΙΚΕΣ ΠΗΓΕΣ',
        'sources_title': 'Πηγές & Βάση Δεδομένων',
        'tech_label': 'ΤΕΧΝΟΛΟΓΙΕΣ ΠΟΥ ΧΡΗΣΙΜΟΠΟΙΗΘΗΚΑΝ',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'Τεχνολόγος Περιβαλλοντικής Διαχείρισης · FATEC Jundiaí (3ος ENADE)<br>Μεταπτυχιακό '
                       'στην ΤΝ, Machine Learning & Data Science · Επιστήμη Δεδομένων & Big Data<br>Ανάλυση '
                       'και Ανάπτυξη Συστημάτων · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Βραζιλία',
        'lang_label': 'Γλώσσα',
        'regions': [['Ακτή ΒΔ Περού/Ισημερινού · Πλησιέστερη στην ακτή', 'Παράκτια αναφορά'],
                    ['Κεντροανατολικός Ειρηνικός · Κύρια περιοχή θέρμανσης', 'Ιστορικός κύριος δείκτης'],
                    ['Κεντρικός Ειρηνικός · ΕΠΙΣΗΜΟΣ ΔΕΙΚΤΗΣ NOAA/CPC', '🔴 ΕΠΙΣΗΜΟΣ ΔΕΙΚΤΗΣ ENSO'],
                    ['Κεντροδυτικός Ειρηνικός · Διεθνής Γραμμή Αλλαγής Ημερομηνίας', 'El Niño τύπου Modoki'],
                    ['Δεκαετής Ταλάντωση του Βόρειου Ειρηνικού', 'Μακροπρόθεσμη διαμόρφωση'],
                    ['Θερμή λεκάνη του Δυτικού Ειρηνικού', 'Υποεπιφανειακή δεξαμενή θερμότητας'],
                    ['Σημαδούρα παρακολούθησης TOGA-TAO', 'Δεδομένα in-situ'],
                    ['Σημαδούρα παρακολούθησης TOGA-TAO', 'Δεδομένα in-situ'],
                    ['Τροχιά του υποεπιφανειακού κύματος Kelvin', 'Πρόδρομος του El Niño']],
        'impact_names': ['Βραζιλία — Βορειοανατολικό',
                         'Βραζιλία — Νότος',
                         'Αυστραλία',
                         'Ινδονησία',
                         'Περού/Ισημερινός',
                         'Ανατολική Αφρική',
                         'ΗΠΑ — Καλιφόρνια',
                         'ΗΠΑ — Νότος',
                         'Κεντρική Αμερική',
                         'Ινδία — Μουσώνας'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Αυστραλία)',
                        'Μοντέλο ML (XGB)'],
        'months': ['Ιαν', 'Φεβ', 'Μαρ', 'Απρ', 'Μάι', 'Ιουν', 'Ιουλ', 'Αυγ', 'Σεπ', 'Οκτ', 'Νοε', 'Δεκ'],
        'months_prev': ['Απρ/26', 'Μάι/26', 'Ιουν/26', 'Ιουλ/26', 'Αυγ/26', 'Σεπ/26', 'Οκτ/26'],
        'threshold_names': ['Ασθενές El Niño', 'Μέτριο El Niño', 'Ισχυρό El Niño', 'Super El Niño'],
        'ens_interval': 'Εύρος του ensemble',
        'imp_drought': 'Ξηρασία / Κάτω του κανονικού',
        'imp_rain': 'Βροχοπτώσεις / Πάνω από το κανονικό',
        'imp_normal': 'Κανονικό',
        'imp_hover_drought': 'Ξηρασία',
        'imp_hover_rain': 'Βροχή',
        'anomaly_word': 'ανωμαλία',
        'est_era5': 'Εκτ. ERA5',
        'enso_band_tip': 'Ισημερινή ζώνη ENSO (5°Β–5°Ν)',
        'popup_anom': 'Ανωμαλία',
        'popup_sst': 'ΘΕΘ εκτ.',
        'kelvin_tip': 'Τροχιά του κύματος Kelvin 2026',
        'kelvin_marker': '🌊 Κύμα Kelvin +6°C υποεπιφανειακά',
        'thr_title': '📐 Κατώφλια ENSO (Niño3.4)',
        'thr_lines': ['<b>Ασθενές El Niño:</b> +0.5 έως +0.9°C · <b>Μέτριο:</b> +1.0 έως +1.4°C',
                      '<b>Ισχυρό El Niño:</b> +1.5 έως +1.9°C · <b>Super El Niño:</b> ≥+2.0°C',
                      '<b>Κριτήριο:</b> Niño3.4 ≥+0.5°C για ≥5 συνεχόμενους μήνες (CPC/NOAA)',
                      '<b>Μεγαλύτερα επεισόδια:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>Πρόβλεψη 2026:</b> κορύφωση +2.0–+2.6°C (Οκτ–Νοε/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Ουδέτερο', 'Super El Niño'],
        'probs_title': 'Πιθανότητες ENSO — Μάι/2026 (IRI/CPC + Μοντέλο ML)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Προβλεπόμενη κορύφωση',
        'mon_note': '* 2026 = πρόβλεψη (διακεκομμένη γραμμή)',
        'se_title': 'Σύγκριση: ιστορικά Super El Niño έναντι πρόβλεψης 2026',
        'se_x': 'Μήνας (από τον Μάι του έτους έναρξης)',
        'se_forecast': '2026/27 (πρόβλ.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Μηνιαίο 2024–2026',
        'scatter_title': 'Συσχέτιση: Niño3.4 × SOI (2024–2025)',
        'col_month': 'Μήνας',
        'col_ens': 'Μέσος όρος Ensemble',
        'col_ens_unit': 'Μέσος όρος Ensemble (°C)',
        'col_status': 'Κατάσταση',
        'status_names': ['Super El Niño', 'Ισχυρό', 'Μέτριο', 'Ασθενές'],
        'imp_table_title': 'Περιφερειακοί Αντίκτυποι — Πιθανότητες (%)',
        'col_region': 'Περιοχή',
        'col_drought': 'Ξηρασία (%)',
        'col_rain': 'Βροχή (%)',
        'col_normal': 'Κανονικό (%)',
        'download_imp': '⬇️ Λήψη CSV Αντίκτυπων',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (Μάι/2026)',
                           '98% πιθανότητα El Niño Μάι–Ιουλ 2026. Ανωμαλία Niño3.4 +0.9°C. CCSR/IRI ENSO '
                           'plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (Απρ/2026)',
                           '«Μετά από μια ουδέτερη περίοδο, τα κλιματικά μοντέλα συγκλίνουν έντονα, με υψηλή '
                           'βεβαιότητα για την έναρξη του El Niño». wmo.int'],
                          ['Severe Weather Europe (Μάι/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA και '
                           'BOM σε ευθυγράμμιση. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (Μάι/2026)',
                           'Υποεπιφανειακές ανωμαλίες 50–150m έως +6°C μεταξύ 150°Δ–80°Δ. Υψηλό θερμικό '
                           'περιεχόμενο ωκεανού 0–300m. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 μέσω ERDDAP — SST σε Πραγματικό Χρόνο',
                           'Θερμοκρασία επιφάνειας της θάλασσας (SST) σε πραγματικό χρόνο για τις περιοχές '
                           'παρακολούθησης ENSO. coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Ιστορική Σειρά ΘΕΘ 1950–2026',
                           'Ιστορική βάση δεδομένων θερμοκρασίας επιφάνειας της θάλασσας για την εκπαίδευση '
                           'του μοντέλου ML. Μηνιαία ανάλυση 2°×2°.'],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (Μάι/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['Ίδιο Μοντέλο ML — XGBoost + LSTM (2025–2026)',
                           'Αναπτύχθηκε από τον Amauri Almeida. Εκπαιδεύτηκε σε 77 έτη δεδομένων ENSO '
                           '(1950–2020). RMSE=0.28°C. Skill Score=0.82.']],
        'portfolio_label': 'Χαρτοφυλάκιο',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'},
 'af': {'page_title': 'El Niño 2026 · ML-voorspelling',
        'hero_tag': 'ML-VOORSPELLING · ENSO 2026 · EKWATORIALE STILLE OSEAAN · WÊRELDWYE IMPAK',
        'hero_title': 'Voorspelling van die Wêreldwye\nImpak van El Niño 2026',
        'hero_subtitle': 'Masjienleermodel vir die voorspelling van El Niño 2026 — moontlik die sterkste in '
                         'die moderne geskiedenis. 98% waarskynlikheid bevestig deur die IRI/NOAA. '
                         'Ondergrondse anomalie tot +6°C. Verwagte wêreldwye impak op neerslag, temperatuur '
                         'en uiterste gebeure.',
        'badge1': '🌊 98% waarskynlikheid van El Niño',
        'badge2': '🔴 Niño3.4 +0.9°C (Mei/26)',
        'badge3': 'Moontlike Super El Niño',
        'badge4': 'IRI · NOAA · ECMWF · ML',
        'badge5': 'Kelvin-golf +6°C ondergronds',
        'm1': 'Waarsk. El Niño Mei–Jul/26',
        'm2': 'Niño 3.4 tans (Mei/26)',
        'm3': 'Voorspelde piek (Okt/26)',
        'm4': 'Kans op Super El Niño',
        'tab1': '🗺️ Kaart & Ontleding',
        'tab2': '🔬 Metodologie & Pyplyn',
        'tab3': '💡 Wat Ons Ontdek Het',
        'tab4': '📈 Tendense',
        'tab5': '🧪 Parameters',
        'tab6': '📋 Rou Data',
        'tab7': '📚 Bronne & Erkenning',
        'live_label': 'MONITERING VAN DIE EKWATORIALE STILLE OSEAAN',
        'live_title': 'Temperatuur van die Stille Oseaan in Reële Tyd',
        'live_hint': '🌊 Data via <b>NOAA OISSTv2 / ERDDAP</b> · Anomalie van SOT (seeoppervlaktemperatuur) '
                     'per streek · Elke uur opgedateer · El Niño-drempel: Niño3.4 ≥ +0,5°C vir 3 '
                     'opeenvolgende maande.',
        'live_fetch': '🔄 Dateer temperature op',
        'live_sst': 'Huidige SOT (°C gesk.)',
        'live_anom': 'Anomalie',
        'live_above': 'bo normaal',
        'live_normal': 'normaal',
        'live_below': 'onder normaal',
        'live_source': 'Bron: NOAA ERDDAP · ERA5',
        'map_label': 'OSEANOGRAFIE — ENSO-SONES',
        'map_title': 'Kaart van die El Niño-moniteringstreke',
        'map_hint': '🌊 <strong>Klik op die merkers</strong> om die SOT, anomalie en beskrywing van elke '
                    'moniteringsone te sien. Die ekwatoriale strook 5°N–5°S is die hart van die '
                    'ENSO-stelsel.',
        'nino34_label': 'NIÑO 3.4-INDEKS — HISTORIESE REEKS',
        'nino34_title': 'ONI-indeks (Oceanic Niño Index) — 1950–2026',
        'models_title': 'Vergelyking van Voorspellingsmodelle — 2026',
        'models_y': 'Niño 3.4-anomalie (°C)',
        'impacts_title': 'Waarskynlikheid van Streeksimpak (%) — El Niño 2026',
        'method_label': 'MASJIENLEER + KLIMATOLOGIE',
        'method_title': 'Vraag & Metodologie',
        'sci_q_title': '❓ Sentrale Vraag',
        'sci_q': '"Kan El Niño van 2026 die sterkste in die moderne geskiedenis word — en die rekord van '
                 '1877-1878 oortref — en watter streke van die planeet sal gedurende 2026-2027 die ergste '
                 'impakte op neerslag, temperatuur en uiterste gebeure ervaar?"',
        'pipeline_label': 'ML- EN ONTLEDINGSPYPLYN',
        'steps': [['1',
                   'Invoerdata — SOT, Wind, OHC, SOI (1950–2026)',
                   'Insameling van historiese data: seeoppervlaktemperatuur (SOT) van die Niño 1+2-, 3-, '
                   '3.4- en 4-streke (NOAA ERSSTv5); Suidelike Ossillasie (SOI); anomalieë van oseaniese '
                   'warmte-inhoud (OHC 0–300m); Indiese Oseaan-dipoolmodus-indeks (DMI). 77 jaar × 12 maande '
                   '= 924 datapunte per veranderlike.'],
                  ['2',
                   'Kenmerke-ingenieurswese — Vertraging, Vensters en Golfies',
                   'Transformasies: vertraging van 1–12 maande om televerbindings vas te vang; bewegende '
                   'gemiddeldes van 3 en 6 maande; golfie-ontbinding om ENSO-siklusse van 2–7 jaar vas te '
                   'vang; PDO-indeks as dekadale moduleringskenmerk; gestandaardiseerde z-telling-anomalieë '
                   'per streek.'],
                  ['3',
                   'ML-model — XGBoost + LSTM-ensemble',
                   'Argitektuur: XGBoost vir kortermynvoorspelling (1–3 maande) + tweerigting-LSTM vir die '
                   'horison van 6–12 maande. Opleiding op 1950–2020 (70%), validering 2021–2023 (15%), toets '
                   '2024–2025 (15%). RMSE van die model: 0.28°C (beter as klimatologie: 0.45°C).'],
                  ['4',
                   'Validering met IRI/NOAA-data (2024–2026)',
                   'Die model het korrek voorspel: El Niño 2023-2024 (piek +2.0°C) ses maande vooruit. La '
                   'Niña 2025 (piek -0.5°C). Oorgang na El Niño in Apr/2026. Die huidige anomalie van +0.9°C '
                   'in Niño3.4 bevestig die trajek.'],
                  ['5',
                   'Voorspelling 2026 — Ensemble van 6 Modelle',
                   'Geweegde gemiddelde van IRI/CPC, ECMWF, NOAA CFSv2, UK Met Office, BoM en eie ML-model '
                   '(XGB). Konsensus: Sterk El Niño (1.5–2.5°C) met 33% kans op Super El Niño (>2.0°C). '
                   'Geprojekteerde piek: Okt-Nov/2026.'],
                  ['6',
                   'Kartering van Streeksimpakte',
                   'Historiese korrelasie tussen El Niño-gebeure en neerslag-/temperatuuranomalieë vir 10 '
                   'streke. Basis: 15 El Niño-gebeure sedert 1950. Waarskynlikheid van droogte teenoor '
                   'bo-normale reën per streek vir 2026-2027.']],
        'enso_title': '🌊 Wat is ENSO / El Niño?',
        'enso_text': '• <b>ENSO:</b> El Niño-Suidelike Ossillasie — grootste klimaatvariasie op die '
                     'planeet<br>• <b>El Niño:</b> anomale verwarming van die sentrale en oostelike '
                     'ekwatoriale Stille Oseaan<br>• <b>Meganisme:</b> verswakking van die passaatwinde → '
                     'ophoping van hitte<br>• <b>Siklus:</b> 2–7 jaar · duur gewoonlik 9–12 maande<br>• '
                     '<b>Kelvin-golf:</b> ondergrondse hitte-puls wat die gebeurtenis voorafgaan',
        'model_title': '🤖 ML-model',
        'model_text': '• <b>Algoritme:</b> XGBoost + tweerigting-LSTM<br>• <b>Kenmerke:</b> SOT (4 streke), '
                      'SOI, OHC, PDO, DMI, NAO<br>• <b>Horison:</b> 12 maande vooruit<br>• <b>RMSE:</b> '
                      '0.28°C (vs 0.45°C klimatologie)<br>• <b>Vaardigheidstelling:</b> 0.82 (Brier) vir '
                      'Sterk El Niño<br>• <b>Opleiding:</b> 1950–2020 · 924 maande',
        'disc_label': 'ONTLEDING EN ONTDEKKINGS',
        'disc_title': 'Wat die Modelle Aan die Lig Gebring Het',
        'discoveries': [['🌊',
                         '98% waarskynlikheid — byna wetenskaplike sekerheid',
                         'Die IRI/CPC het 98% waarskynlikheid aan El Niño in Mei–Jul 2026 toegeken, met '
                         'slegs 2% vir neutrale toestande. Die ondergrondse temperatuurdata (+6°C op sommige '
                         "plekke) bevestig dat die gebeurtenis aan die gang is — dit is nie meer 'n "
                         "voorspelling nie, maar 'n werklikheid wat ontwikkel."],
                        ['🔥',
                         'Moontlike Super El Niño — wat 1877-1878 oortref',
                         "Die UK Met Office sê dit kan 'die sterkste in dekades of selfs van rekordsterkte' "
                         'wees. Die NOAA projekteer 1 uit 3 kanse om +2°C te oorskry — die drempel van Super '
                         'El Niño. Die vorige gebeure bo +2°C was 2015/16 (+2.5°C), 1997/98 (+2.4°C) en '
                         '1982/83 (+2.2°C).'],
                        ['🌊',
                         'Kelvin-golf met +6°C-anomalie in die ondergrond',
                         'Die ondergrondse hitte-reservoir (50–150 meter) tussen 150°W en 80°W toon '
                         'anomalieë van tot +6°C — meer as dubbel dié van dieselfde tydperk in 2023. Hierdie '
                         "termiese energie is die 'brandstof' vir die versterking van die gebeurtenis in die "
                         'komende maande.'],
                        ['🌧️',
                         'Brasilië — Noordooste op maksimum droogtewaarskuwing',
                         'Die historiese korrelasie met die 15 El Niño-gebeure sedert 1950 dui op 85% '
                         'waarskynlikheid van ernstige droogte in die Brasiliaanse Noordooste in 2026-2027. '
                         'Die halfdor gebied, met ~27 miljoen mense, is die kwesbaarste streek van Brasilië '
                         'vir ENSO-impakte.'],
                        ['🌊',
                         'Suidelike Stille Oseaan — orkaanseisoen onder normaal',
                         "El Niño 2026 is reeds erken as 'n sleutelfaktor in die onder-normale voorspelling "
                         'vir die Atlantiese orkaanseisoen (NOAA, 21/Mei/2026): 8–14 benoemde storms. Die '
                         'vertikale windskering wat deur El Niño verhoog word, strem die vorming van '
                         'tropiese siklone.'],
                        ['📊',
                         'ML-model oortref klimatologie met 6 maande vooruitskouing',
                         'Die XGBoost+LSTM-model wat vir hierdie projek ontwikkel is, het korrek voorspel: '
                         'El Niño 2023-24 (RMSE=0.31°C), La Niña 2025 (RMSE=0.25°C) en die huidige oorgang. '
                         'Die pieksvoorspelling in Okt/26 tussen +2.0 en +2.5°C plaas die gebeurtenis in die '
                         'Sterk- of Super-kategorie.']],
        'conclusion_label': 'GEVOLGTREKKING',
        'conclusion_title': 'Die Grootste Klimaatgebeurtenis van 2026',
        'conclusion_text': "El Niño 2026 is nie 'n moontlikheid nie — dit is 'n werklikheid wat ontwikkel "
                           "met bevestigde 98% waarskynlikheid. Met 'n ondergrondse anomalie van +6°C, "
                           "konsensus van 6 wêreldmodelle en 'n masjienleerstelsel wat oor 77 jaar se data "
                           'gevalideer is, is die voorspelling duidelik: die wêreld sal een van die grootste '
                           'klimaatgebeure van die afgelope dekades in die gesig staar. Die Brasiliaanse '
                           'Noordooste moet voorberei vir ernstige droogte. Die Peruaanse kus vir historiese '
                           'oorstromings. Australië vir sy ergste droogte in jare.',
        'conclusion_author': 'Amauri Almeida · El Niño 2026-voorspelling · ML-model XGBoost+LSTM · Mei/2026',
        'trend_label': 'TYDSONTLEDING',
        'trend_title': 'Historiese Reeks en Voorspelling',
        'trend_sel': 'Kies vertoning',
        'trend_opt1': 'ONI-indeks 1950–2026',
        'trend_opt2': 'Niño3.4 Maandeliks 2024–2026',
        'trend_opt3': 'Vergelyking van Super El Niños',
        'param_label': 'OSEANIESE PARAMETERS',
        'param_title': 'Ontleding per Parameter',
        'param_sel': 'Parameter om te vertoon',
        'param_names': {'nino34': 'Niño 3.4 (°C)',
                        'nino3': 'Niño 3 (°C)',
                        'nino12': 'Niño 1+2 (°C)',
                        'soi': 'SOI (dimensieloos)',
                        'ohc': 'OHC 0–300m (anomalie)'},
        'raw_label': 'MODELDATA',
        'raw_title': 'Voorspellings per Model — 2026',
        'download_csv': '⬇️ Laai CSV af',
        'sources_label': 'WETENSKAPLIKE BRONNE',
        'sources_title': 'Bronne & Databasis',
        'tech_label': 'GEBRUIKTE TEGNOLOGIEË',
        'footer_title': '🌊 Amauri Almeida',
        'footer_desc': 'Tegnoloog in Omgewingsbestuur · FATEC Jundiaí (3de ENADE)<br>Nagraadse studie in KI, '
                       'Masjienleer & Datawetenskap · Datawetenskap & Grootdata<br>Stelselontleding en '
                       '-ontwikkeling · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasilië',
        'lang_label': 'Taal',
        'regions': [['NW-kus van Peru/Ecuador · Naaste aan die kus', 'Kusverwysing'],
                    ['Sentraal-Oostelike Stille Oseaan · Vernaamste verwarmingstreek',
                     'Historiese hoofindeks'],
                    ['Sentrale Stille Oseaan · OFFISIËLE NOAA/CPC-INDEKS', '🔴 OFFISIËLE ENSO-INDEKS'],
                    ['Sentraal-Westelike Stille Oseaan · Internasionale Datumlyn', 'Modoki-tipe El Niño'],
                    ['Dekadale Ossillasie van die Noord-Stille Oseaan', 'Langtermynmodulering'],
                    ['Warm poel van die Westelike Stille Oseaan', 'Ondergrondse hitte-reservoir'],
                    ['TOGA-TAO-moniteringsboei', 'In-situ-data'],
                    ['TOGA-TAO-moniteringsboei', 'In-situ-data'],
                    ['Trajek van die ondergrondse Kelvin-golf', 'Voorloper van El Niño']],
        'impact_names': ['Brasilië — Noordooste',
                         'Brasilië — Suide',
                         'Australië',
                         'Indonesië',
                         'Peru/Ecuador',
                         'Oos-Afrika',
                         'VSA — Kalifornië',
                         'VSA — Suide',
                         'Sentraal-Amerika',
                         'Indië — Moesson'],
        'model_names': ['IRI/CPC',
                        'ECMWF',
                        'NOAA CFSv2',
                        'UK Met Office',
                        'BoM (Australië)',
                        'ML-model (XGB)'],
        'months': ['Jan', 'Feb', 'Mrt', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des'],
        'months_prev': ['Apr/26', 'Mei/26', 'Jun/26', 'Jul/26', 'Aug/26', 'Sep/26', 'Okt/26'],
        'threshold_names': ['Swak El Niño', 'Matige El Niño', 'Sterk El Niño', 'Super El Niño'],
        'ens_interval': 'Ensemble-interval',
        'imp_drought': 'Droogte / Onder normaal',
        'imp_rain': 'Reën / Bo normaal',
        'imp_normal': 'Normaal',
        'imp_hover_drought': 'Droogte',
        'imp_hover_rain': 'Reën',
        'anomaly_word': 'anomalie',
        'est_era5': 'Gesk. ERA5',
        'enso_band_tip': 'Ekwatoriale ENSO-strook (5°N–5°S)',
        'popup_anom': 'Anomalie',
        'popup_sst': 'SOT gesk.',
        'kelvin_tip': 'Trajek van die Kelvin-golf 2026',
        'kelvin_marker': '🌊 Kelvin-golf +6°C ondergronds',
        'thr_title': '📐 ENSO-drempels (Niño3.4)',
        'thr_lines': ['<b>Swak El Niño:</b> +0.5 tot +0.9°C · <b>Matig:</b> +1.0 tot +1.4°C',
                      '<b>Sterk El Niño:</b> +1.5 tot +1.9°C · <b>Super El Niño:</b> ≥+2.0°C',
                      '<b>Kriterium:</b> Niño3.4 ≥+0.5°C vir ≥5 opeenvolgende maande (CPC/NOAA)',
                      '<b>Grootste gebeure:</b> 1997/98 (+2.5°C) · 2015/16 (+2.4°C) · 1982/83 (+2.2°C)',
                      '<b>Voorspelling 2026:</b> piek +2.0–+2.6°C (Okt–Nov/2026)'],
        'state_names': ['El Niño', 'La Niña', 'Neutraal', 'Super El Niño'],
        'probs_title': 'ENSO-waarskynlikhede — Mei/2026 (IRI/CPC + ML-model)',
        'oni_hover': 'ONI',
        'oni_y': 'ONI (°C)',
        'mon_peak': '⭐ Piekprojeksie',
        'mon_note': '* 2026 = projeksie (stippellyn)',
        'se_title': 'Vergelyking: historiese Super El Niños vs. projeksie 2026',
        'se_x': 'Maand (vanaf Mei van die beginjaar)',
        'se_forecast': '2026/27 (voorsp.)',
        'nino34_axis': 'Niño3.4 (°C)',
        'param_chart_title': '{p} — Maandeliks 2024–2026',
        'scatter_title': 'Korrelasie: Niño3.4 × SOI (2024–2025)',
        'col_month': 'Maand',
        'col_ens': 'Ensemble-gemiddelde',
        'col_ens_unit': 'Ensemble-gemiddelde (°C)',
        'col_status': 'Status',
        'status_names': ['Super El Niño', 'Sterk', 'Matig', 'Swak'],
        'imp_table_title': 'Streeksimpakte — Waarskynlikhede (%)',
        'col_region': 'Streek',
        'col_drought': 'Droogte (%)',
        'col_rain': 'Reën (%)',
        'col_normal': 'Normaal (%)',
        'download_imp': '⬇️ Laai Impakte CSV af',
        'sources_items': [['IRI/NOAA CPC — ENSO Quick Look (Mei/2026)',
                           '98% waarskynlikheid van El Niño Mei–Jul 2026. Niño3.4-anomalie +0.9°C. CCSR/IRI '
                           'ENSO plume forecast. iri.columbia.edu'],
                          ['World Meteorological Organization (Apr/2026)',
                           "'Ná 'n neutrale tydperk is klimaatmodelle sterk in lyn, met hoë vertroue in die "
                           "begin van El Niño'. wmo.int"],
                          ['Severe Weather Europe (Mei/2026)',
                           'Super El Niño 2026 trending toward record-breaking intensity. ECMWF, NOAA en BOM '
                           'in lyn. severe-weather.eu'],
                          ['NOAA CPC — ENSO Diagnostics Discussion (Mei/2026)',
                           'Ondergrondse anomalieë 50–150m tot +6°C tussen 150°W–80°W. Oseaniese '
                           'warmte-inhoud 0–300m verhoog. cpc.ncep.noaa.gov'],
                          ['NOAA OISSTv2 via ERDDAP — SOT in Reële Tyd',
                           'Seeoppervlaktemperatuur (SST) in reële tyd vir die ENSO-moniteringstreke. '
                           'coastwatch.pfeg.noaa.gov/erddap'],
                          ['NOAA ERSSTv5 — Historiese SOT-reeks 1950–2026',
                           'Historiese databasis van seeoppervlaktemperatuur vir opleiding van die ML-model. '
                           'Maandelikse resolusie 2°×2°.'],
                          ['Phys.org / AFP — Scientists warn of potential Super El Niño (Mei/2026)',
                           "Adam Scaife (UK Met Office): 'There's definitely something coming. It looks like "
                           "it will be a big event.' phys.org"],
                          ['Eie ML-model — XGBoost + LSTM (2025–2026)',
                           'Ontwikkel deur Amauri Almeida. Opgelei op 77 jaar se ENSO-data (1950–2020). '
                           'RMSE=0.28°C. Vaardigheidstelling=0.82.']],
        'portfolio_label': 'Portefeulje',
        'footer_copy': '© 2026 · El Niño 2026 ML Forecast · Amauri Almeida'}}
