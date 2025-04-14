import pandas as pd
import plotly.express as px
import json

with open("Datos\Tarea-1\regiones.json", "r", encoding="utf-8") as f:
    regiones_geojson = json.load(f)

df = pd.DataFrame({
    "Region": [
        "Región de Arica y Parinacota", "Región de Tarapacá", "Región de Antofagasta",
        "Región de Atacama", "Región de Coquimbo", "Región de Valparaíso",
        "Región Metropolitana de Santiago", "Región del Libertador Bernardo O'Higgins",
        "Región del Maule", "Región de Ñuble", "Región del Bío-Bío", "Región de La Araucanía",
        "Región de Los Ríos", "Región de Los Lagos", "Región de Aysén del Gral.Ibañez del Campo",
        "Región de Magallanes y Antártica Chilena"
    ],
    "Promedio": [362, 362, 341, 630, 494, 266, 394, 196, 92.5, 92.5, 55.2, 37.4, 40, 44.5, 46.9, 89.9 ]
})


# Crear mapa
fig = px.choropleth(
    df,
    geojson=regiones_geojson,
    locations="Region",
    featureidkey="properties.Region",
    color="Promedio",
    color_continuous_scale="YlGnBu",
    range_color=(0, 650),
    labels={"Promedio": "Dureza [mg/L de CaCO3]"},
    title="Dureza del agua en Chile por región"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":60,"l":0,"b":0})
fig.show()
