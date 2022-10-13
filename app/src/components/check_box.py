from dash import Dash, html, dcc, ctx
from dash.dependencies import Input, Output
from . import ids
from . import map_data


MAP_DATA = map_data

def render(app: Dash) -> html.Div:


    rendered = html.Div(
        children=[
            html.H6("Sort Regions to Average Price Range"),
            dcc.Checklist(
            ["Sorted"],
            id=ids.CHECK_BOX
            )
        ]
    )
    return rendered