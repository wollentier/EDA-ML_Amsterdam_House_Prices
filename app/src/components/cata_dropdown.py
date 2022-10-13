from dash import Dash, html, dcc, ctx
from dash.dependencies import Input, Output
from . import ids
from . import map_data

MAP_DATA = map_data.avg_data

def render(app: Dash) -> html.Div:
    
    all_map_options = list(MAP_DATA.Region)
    button_state = False
    

    @app.callback(
        Output(ids.CATA_DROPDOWN, "value"),
        Output(ids.CATA_DROPDOWN, "disabled"),
        Output(ids.SELECT_ALL_BUTTON, "disabled"),
        Input(ids.SELECT_ALL_BUTTON, "n_clicks"),
        Input(ids.RANGE_SLIDER, "value"),
        Input(ids.CHECK_BOX, "value")   
    )

    def select_all_disable(button: int, prices: list, check_box: list) -> list[str]:
        
        all_map_options=list(MAP_DATA.Region)
                
        button_state = False

        if check_box == ["Sorted"]:
            
            button_state=True
            return all_map_options, button_state, button_state
        
        
        
        if ctx.triggered_id == "select_all_button":
            all_map_options=list(MAP_DATA.Region)
            return all_map_options, button_state, button_state

        if ctx.triggered_id == "range_slider":
            all_map_options=list(MAP_DATA.query("Price > @prices[0] & Price <= @prices[1]")["Region"])
            return all_map_options, button_state, button_state
            
        else:
            return all_map_options, button_state, button_state


    rendered = html.Div(
        children=[
            html.H6("Select Zip Codes"),
            dcc.Dropdown(
                id=ids.CATA_DROPDOWN,
                multi=True,
                options=all_map_options,
                value=all_map_options,
                disabled=button_state
            ),
            html.Button(
                className="cata_dropdown",
                children=["Select All"],
                id=ids.SELECT_ALL_BUTTON,
                disabled=button_state
            )
        ]
    )
    return rendered