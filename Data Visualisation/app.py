import numpy as np
import pandas as pd
import plotly.express as px
import dash
import dash_table
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

#---------------------------------------------------------------
app.layout = html.Div(children=[
    html.H1(children='Time Series'),

    dcc.Graph(
        id='series-graph'
    ),

    dcc.Slider(
        id='rolMean-slider',
        value=15,
        min=1,
        max=100,
        step=1
    ),
    html.Div(id='slider-output')
])

@app.callback(
    dash.dependencies.Output('series-graph', 'figure'),
    dash.dependencies.Output('slider-output', 'children'),
    [dash.dependencies.Input('rolMean-slider', 'value')])

def update_output(value):
    df = pd.read_csv(f"LaPacks_data_cleaning.csv")
    df['Rolling Mean'] = df.iloc[:].rolling(window=value).mean()
    fig = px.line(df, y = ["Series1", "Rolling Mean"])
    spectrum = np.fft.fft(df.Series1)
    spectrum = np.abs(spectrum)
    return fig, ["Rolling Mean Window Value: " + str(value) + ", Highest data frequency: " + str(min(spectrum))]

if __name__ == '__main__':
    app.run_server(debug=True)
