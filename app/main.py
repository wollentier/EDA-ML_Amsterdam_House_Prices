from dash import Dash, html
from dash_bootstrap_components.themes import SANDSTONE
from src.components.layout import create_layout
from flask import Flask

server = Flask(__name__)
app = Dash(server=server,external_stylesheets=[SANDSTONE])

app.title = "Amsterdam House Prices"
app.layout = create_layout(app)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050")
