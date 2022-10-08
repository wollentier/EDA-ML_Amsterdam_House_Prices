from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import map_data as map_data

MAP_DATA = map_data.avg_data
MAP_PRICE_REGIONS = map_data.map_price_regions
GEO_DATA = map_data.geodata



def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.MAP_PLOT,"children"),
        Input(ids.CATA_DROPDOWN, "value"),
        Input(ids.RANGE_SLIDER, "value"),
        Input(ids.CHECK_BOX, "value")
    )

    
    def update_bar_chart(zip_val,price_range,check_box) -> html.Div:
        
        if check_box == ["Sorted"]:
            #Regions of interest = price-regions by fix labels
            ROIs = list(MAP_PRICE_REGIONS["Region"].unique())
            filtered_data = {'type': 'FeatureCollection', 'features': [GEO_DATA["features"][i] for i in range(0,len(GEO_DATA["features"])) if int(GEO_DATA["features"][i]["properties"]["pc4_code"]) in ROIs]}
            main_data = MAP_PRICE_REGIONS
            locs = MAP_PRICE_REGIONS["Region"]
            colors = MAP_PRICE_REGIONS["most_frequent_cat"]
            hover_data = main_data.columns
            
            
        
        if check_box != ["Sorted"]:
            #Regions of interest = set of dropdown selected and price slider range lists
            ROIs = list(set(zip_val) & set(list(MAP_DATA.query("Price > @price_range[0] & Price <= @price_range[1]")["Region"])))
            filtered_data = {'type': 'FeatureCollection', 'features': [GEO_DATA["features"][i] for i in range(0,len(GEO_DATA["features"])) if int(GEO_DATA["features"][i]["properties"]["pc4_code"]) in ROIs]}
            main_data = MAP_DATA
            locs = MAP_DATA["Region"]
            colors = MAP_DATA["Price"]
            hover_data = main_data.columns
            
        
        fig = px.choropleth_mapbox(
        main_data,
        locations=locs,
        geojson=filtered_data,
        color=colors,
        zoom=9.7, 
        center = {"lat": 52.356157, "lon": 4.907736},
        color_continuous_scale="matter",
        color_discrete_sequence = ["#fce6aa","#f08e62","#c53a59","#781a60","#282828"],
        category_orders={"most_frequent_cat":map_data.new_regions}, 
        mapbox_style="carto-positron",
        hover_data=hover_data,
        range_color=[MAP_DATA["Price"].min(),MAP_DATA["Price"].max()],
        width=1000,
        height=500
        )

        fig.update_layout(                      
        margin={"r":0,"t":0,"l":0,"b":0}
        )
        
        
        return html.Div(dcc.Graph(figure=fig), id=ids.MAP_PLOT)

    return html.Div(id=ids.MAP_PLOT)