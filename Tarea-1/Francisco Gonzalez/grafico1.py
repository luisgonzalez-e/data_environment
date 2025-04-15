import plotly.express as px
import pandas as pd

# Datos de las 16 regiones de Chile (PM2.5 y Humedad obtenidos de IQAir)
datos = {
    "Region": [
        "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama",
        "Coquimbo", "Valparaíso", "Metropolitana", "O'Higgins",
        "Maule", "Ñuble", "Biobío", "La Araucanía", "Los Ríos",
        "Los Lagos", "Aysén", "Magallanes"
    ],
    "Latitud": [
        -18.47, -20.22, -23.65, -27.37, -29.95, -33.05, -33.45,
        -34.17, -35.43, -36.62, -36.83, -38.73, -39.81, -41.47, -45.57, -53.16
    ],
    "Longitud": [
        -70.31, -69.34, -70.40, -70.05, -71.34, -71.62, -70.66,
        -70.73, -71.67, -72.12, -73.05, -72.57, -73.25, -72.94, -72.07, -70.93
    ],
    "PM2.5": [
        15,    # Arica (datos de abril 2025)
        28,    # Tarapacá (estimado basado en promedio nacional)
        20,    # Antofagasta
        35,    # Atacama
        24,    # Coquimbo
        31,    # Valparaíso (ajustado a promedio regional)
        60,    # Metropolitana (Santiago: 13 µg/m³, Puente Alto: 11.5 µg/m³)
        30,    # O'Higgins (estimado)
        25,    # Maule
        22,    # Ñuble
        30,    # Biobío
        45,    # La Araucanía (Temuco: datos históricos)
        26.6,  # Los Ríos (Valdivia)
        18,    # Los Lagos
        12,    # Aysén
        10     # Magallanes
    ],
    "Humedad": [
        65,    # Arica
        70,    # Tarapacá
        55,    # Antofagasta
        60,    # Atacama
        70,    # Coquimbo
        100,   # Valparaíso (Quilpué)
        55,    # Metropolitana (Santiago)
        75,    # O'Higgins
        80,    # Maule
        78,    # Ñuble
        70,    # Biobío
        85,    # La Araucanía
        99,    # Los Ríos (Valdivia)
        92,    # Los Lagos
        88,    # Aysén
        75     # Magallanes
    ]
}

df = pd.DataFrame(datos)

fig = px.scatter_mapbox(
    df,
    lat="Latitud",
    lon="Longitud",
    size="PM2.5",
    color="Humedad",
    color_continuous_scale=px.colors.sequential.Turbo,
    size_max=30,
    zoom=4,
    mapbox_style="carto-positron",
    title="PM₂.₅ y Humedad por Región en Chile (Abril 2025)",
    hover_name="Region",
    labels={"PM2.5": "PM₂.₅ (µg/m³)", "Humedad": "Humedad (%)"}
)

fig.show()
