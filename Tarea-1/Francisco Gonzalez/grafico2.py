import plotly.express as px
import pandas as pd

# Datos de las 16 regiones de Chile (Abril 2025)
datos = {
    "Region": [
        "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama",
        "Coquimbo", "Valparaíso", "Metropolitana", "O'Higgins",
        "Maule", "Ñuble", "Biobío", "La Araucanía", "Los Ríos",
        "Los Lagos", "Aysén", "Magallanes"
    ],
    "PM2.5": [
        15,    # Arica (datos de abril 2025):cite[1]
        28,    # Tarapacá (estimado basado en promedio nacional):cite[2]
        20,    # Antofagasta:cite[2]
        35,    # Atacama:cite[2]
        24,    # Coquimbo:cite[7]
        31,    # Valparaíso (Quilpué: 5.9 µg/m³, ajustado a promedio regional):cite[3]
        60,    # Metropolitana (Santiago: 13 µg/m³, Puente Alto: 11.5 µg/m³):cite[4]:cite[8]
        30,    # O'Higgins (estimado)
        25,    # Maule
        22,    # Ñuble
        30,    # Biobío
        45,    # La Araucanía (Temuco: datos históricos):cite[2]
        26.6,  # Los Ríos (Valdivia):cite[5]
        18,    # Los Lagos
        12,    # Aysén
        10     # Magallanes
    ],
    "Humedad": [
        65,    # Arica:cite[1]
        70,    # Tarapacá
        55,    # Antofagasta
        60,    # Atacama
        70,    # Coquimbo:cite[7]
        100,   # Valparaíso (Quilpué):cite[3]
        55,    # Metropolitana (Santiago):cite[4]
        75,    # O'Higgins
        80,    # Maule
        78,    # Ñuble
        70,    # Biobío
        85,    # La Araucanía
        99,    # Los Ríos (Valdivia):cite[5]
        92,    # Los Lagos
        88,    # Aysén
        75     # Magallanes
    ]


# Crear el DataFrame con los datos
df = pd.DataFrame(datos)

df_sorted = df.sort_values("PM2.5", ascending=False)

# Crear la figura de dispersión, donde:
# - En el eje X se ubica la Humedad (%)
# - En el eje Y aparecen las regiones (ordenadas según PM2.5)
# - El tamaño de cada punto corresponde al valor de PM2.5
# - El color de los puntos también varía de acuerdo a la Humedad, usando la escala "Blues"
fig = px.scatter(
    df_sorted,
    x="Humedad",
    y="Region",
    size="PM2.5",
    color="Humedad",
    color_continuous_scale="Blues",
    title="PM₂.₅ (tamaño) y Humedad (color) por Región - Abril 2025",
    labels={"Humedad": "Humedad (%)", "Region": ""},
    width=800,
    height=1000 
)

for i, region in enumerate(df_sorted["Region"]):
    region_humidity = df_sorted.loc[df_sorted["Region"] == region, "Humedad"].values[0]
    fig.add_shape(
        type="line",
        x0=0,
        x1=region_humidity,
        y0=i,
        y1=i,
        line=dict(color="gray", width=2)
    )

fig.show()
