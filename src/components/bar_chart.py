from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids

MEDAL_DATA = px.data.medals_long()

def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.BAR_CHART,"children"),
        Input(ids.CATA_DROPDOWN, "value")
    )

    def update_bar_chart(values) -> html.Div:
        filtered_data = MEDAL_DATA.query("nation in @values")
        
        if len(filtered_data) == 0:
            return html.Div("No Data Selected")

        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    
    return html.Div(id=ids.BAR_CHART)