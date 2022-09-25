from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import map_data as map_data

MAP_DATA = map_data.avg_data
GEO_DATA = map_data.geodata

def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.MAP_PLOT,"children"),
        Input(ids.CATA_DROPDOWN, "value"),
        Input(ids.RANGE_SLIDER, "value")
    )

    
    def update_bar_chart(zip_val,price_range) -> html.Div:
        print(zip_val)
        ROIs = list(set(zip_val) & set(list(MAP_DATA.query("Price > @price_range[0] & Price < @price_range[1]")["Region"])))
        filtered_data = {'type': 'FeatureCollection', 'features': [GEO_DATA["features"][i] for i in range(0,len(GEO_DATA["features"])) if int(GEO_DATA["features"][i]["properties"]["pc4_code"]) in ROIs]}
        
        fig = px.choropleth_mapbox(
        MAP_DATA,
        locations=MAP_DATA["Region"],
        geojson=filtered_data,
        color=MAP_DATA["Price"],
        zoom=9.7, 
        center = {"lat": 52.356157, "lon": 4.907736},
        color_continuous_scale="matter", 
        mapbox_style="carto-positron",
        hover_data=["Price"],
        range_color=[MAP_DATA["Price"].min(),MAP_DATA["Price"].max()],
        width=1000,
        height=500
        )

        fig.update_layout(                      
        margin={"r":0,"t":0,"l":0,"b":0}
        )
        
        
        return html.Div(dcc.Graph(figure=fig), id=ids.MAP_PLOT)

    return html.Div(id=ids.MAP_PLOT)