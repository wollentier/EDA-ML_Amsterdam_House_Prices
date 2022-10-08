from dash import Dash, html
from . import map_plot
from . import cata_dropdown
from . import price_slider
from . import check_box
from . import user_prediction_input
from . import user_prediction

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
            html.Div(
                className="select_price_regions",
                children=[
                check_box.render(app)]
            ),
            html.Div(
                className="map",
                children=[
                map_plot.render(app)]
            ),
            html.Hr(),
            html.H1("House Price Prediction"),
            html.Div(
                className="user_input",
                children=[
                *user_prediction_input.render(app)],
            ),
            html.Div(
                className="prediction",
                children=[
                *user_prediction.render(app)],
            )
        ]
    )
    return layout