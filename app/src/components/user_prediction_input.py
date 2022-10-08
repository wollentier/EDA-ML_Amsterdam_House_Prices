from dash import Dash, html, dcc, ctx
from dash.dependencies import Input, Output
from . import ids
import map_data as map_data

all_map_options=list(map_data.avg_data.Region)
area_options=[int(min(map_data.data["Area"])),max(map_data.data["Area"])]
room_options=[int(min(map_data.data["Room"])),max(map_data.data["Room"])]

def render(app: Dash) -> html.Div:

    Input_Fields = ["Area m²", "Rooms #","Zip Code"]
    out = []
    
    rendered = html.Div(
                
        children=[
        html.H6(Input_Fields[0]),
        dcc.Input(
            id=ids.USER_INPUT+"_"+Input_Fields[0],
            className="user_input"+" "+Input_Fields[0],
            value=30
            ),
            dcc.Markdown(
                children=[f"Select between {area_options[0]} and {area_options[1]}"]
            )
        ],
        style={"width": "30%", "display": "inline-block"}

    )
    out.append(rendered)

    rendered = html.Div(
                
        children=[
        html.H6(Input_Fields[1]),
        dcc.Slider(
            room_options[0], room_options[1], 1,
            id=ids.USER_INPUT+"_"+Input_Fields[1],
            className="user_input"+" "+Input_Fields[1],
            value=3
            ),
        ],
        style={"width": "30%", "display": "inline-block","vertical-align": "top"}

    )
    out.append(rendered)

    
    rendered = html.Div(
            
        children=[
        html.H6(Input_Fields[2]),
        dcc.Dropdown(
            options=all_map_options,              
            id=ids.USER_INPUT+"_"+Input_Fields[2],
            className="user_input"+" "+Input_Fields[2],
            value=1091
            ),
        ],
        style={"width": "30%", "display": "inline-block","vertical-align": "top"}

        )
    out.append(rendered) 
        
    return out