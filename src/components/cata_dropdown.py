from dash import Dash, html, dcc, ctx
from dash.dependencies import Input, Output
from . import ids

import map_data as map_data

MAP_DATA = map_data.avg_data

def render(app: Dash) -> html.Div:
    
    all_map_options=list(MAP_DATA.Region)

    @app.callback(
        Output(ids.CATA_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_BUTTON, "n_clicks"),
        Input(ids.RANGE_SLIDER, "value")
    )

    def select_all(click: int, prices: list) -> list[str]:
        
        if ctx.triggered_id == "select_all_button":
            map_options = all_map_options
            return map_options

        elif ctx.triggered_id == "range_slider":
            map_options=list(MAP_DATA.query("Price > @prices[0] & Price < @prices[1]")["Region"])
            return map_options

        else:
            return all_map_options

    rendered = html.Div(
        children=[
            html.H6("test_stuff"),
            dcc.Dropdown(
                id=ids.CATA_DROPDOWN,
                multi=True,
                options=all_map_options,
                value=all_map_options
            ),
            html.Button(
                className="cata_dropdown",
                children=["Select All"],
                id=ids.SELECT_ALL_BUTTON
            )
        ]
    )
    return rendered