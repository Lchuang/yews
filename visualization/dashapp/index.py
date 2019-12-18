#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import callbacks
from app import app
from layouts import *

app.layout = html.Div([
    html.Div([
        html.Center(
            html.P('Earthquake Catalog')
        ),
        html.Div(eqs_loc_layout,
                 style={'height': '10%', 'width': '100%', 'display': 'inline-block', 'automargin': True}),
        html.Div([],
                 style={'height': '10%', 'width': '100%', 'display': 'inline-block', 'automargin': True}),
        html.Center(
            html.P('Station Catalog')
        ),
        html.Div(sta_loc_layout,
                 style={'height': '10%', 'width': '100%', 'display': 'inline-block', 'automargin': True}),
        html.Div([],
                 style={'height': '10%', 'width': '100%', 'display': 'inline-block', 'automargin': True}),
        html.Div([
            html.Div(
                html.P('Map area update mode'),
                style={'height': '100%', 'width': '40%', 'display': 'inline-block', 'automargin': True}),
            html.Div(mode_button,
                     style={'height': '100%', 'width': '59%', 'display': 'inline-block', 'automargin': True})],
            style={'height': '10%', 'width': '100%', 'display': 'inline-block', 'automargin': True}),
        html.Div([],
                 style={'height': '32%', 'width': '100%', 'display': 'inline-block', 'automargin': True}),
    ],
        style={'height': '100%', 'width': '30%', 'display': 'inline-block', 'automargin': True}),

    html.Div(geomap_layout,
             style={'height': '100%', 'width': '70%', 'display': 'inline-block', 'automargin': True}),
],
    style={'height': 800, 'backgroundColor': 'rgba(249,249,249,1)'})

if __name__ == '__main__':
    app.run_server(debug=True)