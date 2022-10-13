from dash import Dash, html, dcc, ctx
from dash.dependencies import Input, Output
from . import ids
from . import model_OH_predict


def render(app: Dash) -> html.Div:

    model = model_OH_predict.model
    enc = model_OH_predict.enc
    
    text = "Prediction"
    Input_Fields = ["Area m²", "Rooms #","Zip Code"]
    out = []

    rendered = html.Div(
            children=[
                html.Button(
                className="prediction_button",
                children=["Start Prediction"],
                id=ids.PREDICTION_BUTTON,
                disabled=False
                )

            ],style={'display': 'inline-block'}
    )
    out.append(rendered)

# PREDICTION ----------------------------------------------

    @app.callback(
        Output(ids.PREDICTION_OUTPUT, "children"),
        Input(ids.PREDICTION_BUTTON, "n_clicks"),
        *[Input(ids.USER_INPUT+"_"+i, "value") for i in Input_Fields]
    )

    def make_prediction(button: int, *args: int) -> int:
        
        nonlocal text

        if ctx.triggered_id == "prediction_button":
            
            args = [int(i) for i in args]
            
            data = model_OH_predict.list_to_pandas(list(args))
            data = model_OH_predict.OH_encoding(data,enc,"Region")
            text = str(model_OH_predict.OH_prediction(data))
            text = " Predicted House Price: "+text+" Euro"
            
            return text
        
        else:
            return text

    
    rendered = html.Div(
            children=[
                dcc.Markdown(
                children=[text],
                className="prediction_output",
                id=ids.PREDICTION_OUTPUT,
                )

            ],style={"display": "inline-block"}
    )
    out.append(rendered)
    
    return out