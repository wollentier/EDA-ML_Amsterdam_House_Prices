from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import map_data
from . import ids


MAP_DATA = map_data.avg_data

def render(app: Dash) -> html.Div:

    button_state = False

    @app.callback(
        Output(ids.RANGE_SLIDER, "disabled"),
        Input(ids.CHECK_BOX, "value")   
    )

    def disable(check_box: list) -> list[str]:
        
        button_state = False

        if check_box == ["Sorted"]:
            
            button_state=True
            return button_state
        
        else:
            return

    
    rendered = html.Div(
        children=[
            html.H6("Select House Price Range"),
            dcc.RangeSlider(
                0,MAP_DATA.max()[1],
                id=ids.RANGE_SLIDER,
                value=list([MAP_DATA.min()[1], MAP_DATA.max()[1]]),
                allowCross=False,
                disabled=button_state
            )
        ]
    )

    return rendered