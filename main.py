from dash import Dash, html
from dash_bootstrap_components.themes import SANDSTONE
from src.components.layout import create_layout


def main() -> None:
    app = Dash(external_stylesheets=[SANDSTONE])
    app.title = "Amsterdam House Prices"
    app.layout = create_layout(app)
    app.run()

if __name__ == "__main__":
    main()