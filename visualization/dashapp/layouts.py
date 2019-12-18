#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
# this file defines all the layouts used in apps
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash_table.Format import Format

# ---- 01. map layout ------
map_layout = {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoieWNodWFuZzM1IiwiYSI6ImNqeGtzZDluZzFkcWgzem12ZDY2cWpoemsifQ.1_ZAhhpXtE2hnkSCtKIDZw',
                'style': 'mapbox://styles/ychuang35/cjxlwvwur15fj1cousoa18kju',
                'center': {'lat': 23.60, 'lon': 121.0},
                'zoom': 7,
            },
            'hovermode': 'closest',
            'height': 800,
            'yaxis': {'title': 'Latitude'},
            'xaxis': {'title': 'Longitude'},
            'margin': {"r": 0, "t": 0, "l": 3, "b": 0}
        }
map_data = [{'name': "events",
             'marker': {
                'opacity': 0.8,
                'colorscale': 'Portland',
                'cmax': 10,
                'cmin': 0,
                'colorbar': {'title': 'phase number'},
                'showscale': True,
                'sizeref': 0.4
             },
             'type': 'scattermapbox',
             'showlegend': False,
             'hovertemplate': '(%{lat:.2f}, %{lon:.2f})'
                                 '<br><b>%{text}</b>'
                                 '<br><b>M: %{marker.size:.f}</b>'
                                 '<br><b>Phase: %{marker.color:.f}</b>'
             }]
geomap_layout = dcc.Graph(id='map', figure={
        'layout': map_layout,
        'data': map_data
    })

# ---- 02. earthquake catalog drop-down list
eqs_loc_layout = dcc.Dropdown(id='eq_loc_dw',
                              options=[],
                              placeholder='select a standard earthquake catalog',
                              multi=True
                              )
# ---- 03. earthquake catalog table
eqs_table_layout = dash_table.DataTable(id='table',
                                        data=[],
                                        style_header={
                                            'backgroundColor': 'rgb(230,230,230)',
                                            'fontWeight': 'bold',
                                            'textAlign': 'center'
                                        },
                                        style_data_conditional=[{
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(2489,248,248)'
                                        }],
                                        style_table={
                                            #'maxHeight': '400px',
                                            'overflowY': 'scroll',
                                            'overflowX': 'scroll',
                                            #'maxWidth': '200px',
                                            'textAlign': 'center'
                                        },
                                        columns=[
                                            {'id': 'otime', 'name': 'otime'},
                                            {'id': 'evla', 'name': 'lat'},
                                            {'id': 'evlo', 'name': 'lon'},
                                            {'id': 'evdp', 'name': 'dep'},
                                            {'id': 'mag', 'name': 'mag'},
                                        ],
                                        fixed_rows={'headers': True, 'data': 0},
                                        style_cell={'width': '70px'},
                                        sort_action='native',
                                        sort_mode='multi',
                                        row_selectable='single',
                                        row_deletable=False,
                                        filter_action='native',
                                        page_size=50,
                                        )
# ---- 04. station catalog drop-down list
sta_loc_layout = dcc.Dropdown(id='sta_loc_dw',
                              options=[],
                              placeholder='select a station catalog',
                              multi=True
                              )
# ---- 05. mode radio buttons
mode_button = dcc.RadioItems(
    options=[
        {'label': 'simultaneous', 'value': 'sim'},
        {'label': 'manual', 'value': 'manual'}
    ]
)

# ---- 06. date range slider
