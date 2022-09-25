from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import map_data as map_data
from . import ids

import map_data as map_data

MAP_DATA = map_data.avg_data

def render(app: Dash) -> html.Div:
    
    # @app.callback(
    #     Output(ids.RANGE_SLIDER, "value"),
    #     Input(ids.CATA_DROPDOWN, "value")
        
    # )

    # def update_slider(map_options: list) -> list:
    #     map_options=list(MAP_DATA
    #         .query("Region in @map_options")["Price"]
    #         .agg(["min","max"]))

    #     return map_options


    rendered = html.Div(
        children=[
            html.H6("test_stuff"),
            dcc.RangeSlider(
                0,MAP_DATA.max()[1],
                id=ids.RANGE_SLIDER,
                value=list([MAP_DATA.min()[1], MAP_DATA.max()[1]]),
                allowCross=False
            )
        ]
    )

    return rendered