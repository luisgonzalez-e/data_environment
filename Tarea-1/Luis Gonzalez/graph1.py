import plotly.graph_objects as go

labels = [
    "Agua", "Agricultura", "Agua potable", "industria",
    "Eléctrico", "Minería", "Pecuario"
]

# Conexiones entre nodos
source = [0, 0, 0, 0, 0, 0, 0]
target = [1, 2, 3, 4, 5, 6]
values = [72, 12, 7, 5, 4, 1]

# Lista de colores 
colors = [
    "#1f77b4", "#2ca02c", "#ff7f0e","#9467bd","#8c564b","#e377c2"]

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=source,
        target=target,
        value=values,
        color=colors,
        hovertemplate='%{source.label} → %{target.label}: %{value}%<extra></extra>'
    )
)])

fig.update_layout(
    title_text="Consumo de Agua por Sector Económico en Chile",
    font_size=14
)

fig.show()
