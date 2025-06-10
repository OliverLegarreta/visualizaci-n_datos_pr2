import pandas as pd
import plotly.express as px

# Carga de datos
df = pd.read_csv("../pr1/V-Dem_pregunta1.csv")


# Añadir regiones
region_map = {
    'Spain': 'Europe', 'France': 'Europe', 'Germany': 'Europe',
    'Brazil': 'Latin America', 'Mexico': 'Latin America', 'Argentina': 'Latin America',
    'India': 'Asia', 'China': 'Asia', 'Japan': 'Asia',
    'USA': 'North America', 'Canada': 'North America'
}
df['region'] = df['country_name'].map(region_map)

# Elimina filas sin región asignada
df = df.dropna(subset=['region', 'v2x_partipdem'])

# Agrupamos por año y región
df_grouped = df.groupby(['year', 'region'])['v2x_partipdem'].mean().reset_index()

# Visualización con Plotly
fig = px.line(df_grouped,
              x='year',
              y='v2x_partipdem',
              color='region',
              markers=True,
              title='Evolución de la Democracia Participativa por Región',
              labels={
                  'year': 'Año',
                  'v2x_partipdem': 'Índice de Democracia Participativa',
                  'region': 'Región'
              })

fig.update_layout(hovermode='x unified', template='plotly_white')
fig.show()

fig.write_html("democracia_participativa_por_region.html")
