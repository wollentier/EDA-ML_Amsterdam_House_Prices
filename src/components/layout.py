from dash import Dash, html
from . import bar_chart
from . import map_plot
from . import cata_dropdown
from . import price_slider

def create_layout(app: Dash) -> html.Div:
    layout = html.Div(
        className="app-div",
        children=[
            html.H1(app.title), 
            html.Hr(),
            html.Div(
                className="cata_dropdown",
                children=[
                cata_dropdown.render(app)]
            ),
            html.Div(
                className="price_slider",
                children=[
                price_slider.render(app)]
            ),
            map_plot.render(app)    
        ]
    )
    return layout