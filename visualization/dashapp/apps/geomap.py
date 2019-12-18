#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
# --- this app displays a map for event location visualization
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app


map_layout = {
            'title': 'geomap',
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoieWNodWFuZzM1IiwiYSI6ImNqeGtzZDluZzFkcWgzem12ZDY2cWpoemsifQ.1_ZAhhpXtE2hnkSCtKIDZw',
                'style': 'mapbox://styles/ychuang35/cjxlwvwur15fj1cousoa18kju',
                'center': {'lat': 23.60, 'lon': 121.0},
                'zoom': 7,
            },
            'hovermode': 'closest',
            'height': 950,
            'yaxis': {'title': 'Latitude'},
            'xaxis': {'title': 'Longitude'},
            'automargin': True
        }

geomap_layout = html.Div([
    dcc.Graph(id='map', figure={
        'layout': map_layout
    }, style={'height': '100%', 'width': '100%', 'display': 'inline-block', 'automargin': True}),
])