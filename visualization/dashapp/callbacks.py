#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_html_components as html
from funcs import *
from app import app
import glob
from obspy import UTCDateTime
import datetime
import pandas as pd

# ---- 02. callback for station catalog search ----
path_station_cata = '../station_catalog'
@app.callback(
    Output("sta_loc_dw", "options"),
    [Input("sta_loc_dw", "search_value")],
)
def update_options(search_value):
    print(f'searching station catalog in {path_station_cata}')
    options = []
    cata_list = glob.glob(f'{path_station_cata}/*')
    for lst in cata_list:
        lst = lst.split('/')[-1]
        options.append({'label': lst, 'value': lst})
    return options

# ---- 01. callback for earthquake catalog search ----
path_earthquake_cata = '../earthquake_catalog'
@app.callback(
    Output("eq_loc_dw", "options"),
    [Input("eq_loc_dw", "search_value")],
)
def update_options(search_value):
    print(f'searching earthquake catalog in {path_earthquake_cata}')
    options = []
    cata_list = glob.glob(f'{path_earthquake_cata}/*')
    for lst in cata_list:
        lst = lst.split('/')[-1]
        options.append({'label': lst, 'value': lst})
    return options

# ---- 01. callback for earthquake catalog search ----
path_earthquake_phase_cata = '../earthquake_phase'
@app.callback(
    Output("phase_loc_dw", "options"),
    [Input("phase_loc_dw", "search_value")],
)
def update_options(search_value):
    print(f'searching earthquake phase catalog in {path_earthquake_phase_cata}')
    options = []
    cata_list = glob.glob(f'{path_earthquake_phase_cata}/*')
    for lst in cata_list:
        lst = lst.split('/')[-1]
        options.append({'label': lst, 'value': lst})
    return options

# ---- 02. callbacks for earthquake stats
@app.callback(Output('showtext', 'children'),
              [Input('mode_switch', 'on'),
               Input('index_page_tab', 'value'),
               Input('eq_loc_dw', 'value'),
               Input('phase_loc_dw', 'value'),
               Input('sta_loc_dw', 'value')])
def render_content(on_off, tab, eq_cata, phase_cata, sta_cata):
    if on_off is True:
        if tab == 'earthquakes' and eq_cata is not None and len(eq_cata) >= 1:
            earlist, latest, total_event_number = quick_analysis_eq_catalog(path_earthquake_cata, eq_cata)
            container = html.Div([
                html.P(f'start date: {earlist}'),
                html.P(f'end date  : {latest}'),
                html.P(f'event number: {total_event_number}')]
            )
            return container
        if tab == 'phases' and phase_cata is not None and len(phase_cata) >= 1:
            earlist, latest, total_event_number = quick_analysis_phase_catalog(path_earthquake_phase_cata, phase_cata)
            container = html.Div([
                html.P(f'start date: {earlist}'),
                html.P(f'end date  : {latest}'),
                html.P(f'phase number: {total_event_number}')]
            )
            return container
        if tab == 'stations' and sta_cata is not None and len(sta_cata) >= 1:
            networks, channels, total_number = quick_analysis_sta_catalog(path_station_cata, sta_cata)
            container = html.Div([
                html.P(f'networks: {networks}'),
                html.P(f'channels  : {channels}'),
                html.P(f'station number: {total_number}')]
            )
            return container

@app.callback(Output('map', 'figure'),
              [Input('mode_switch', 'on'),
               Input('eq_loc_dw', 'value'),
               Input('sta_loc_dw', 'value')])
def updatemap(on_off, eq_cata, sta_cata):
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
        'margin': {"r": 0, "t": 0, "l": 5, "b": 0}
    }
    map_data = [
        {'name': "events",
         'marker': {
             'opacity': 0.8,
             'colorscale': 'Portland',
             'cmax': 150,
             'cmin': 0,
             'colorbar': {'title': 'Event depth (km)'},
             'showscale': True,
             'sizeref': 0.4
         },
         'type': 'scattermapbox',
         'showlegend': False,
         'hovertemplate': '(%{lat:.2f}, %{lon:.2f})'
                          '<br><b>%{text}</b>'
                          '<br><b>M: %{marker.size:.f}</b>'
                          '<br><b>Depth: %{marker.color:.f}</b>'
         },
        {'name': "stations",
         'marker': {
             'color': 'rgb(0, 0, 0)',
             'size': 9,
             'opacity': 1,
             'symbol': 'triangle',
             'line': {'color': 'rgb(0, 0, 0)'},
         },
         'type': 'scattermapbox',
         'showlegend': False,
         'hovertemplate': '(%{lat:.2f}, %{lon:.2f})'
                          '<br><b>%{text}</b>'
         },
    ]
    if on_off is True:
        if eq_cata is not None and len(eq_cata) >= 1:
            map_data = wrap_map_object_eq(path_earthquake_cata, eq_cata, map_data)
        if sta_cata is not None and len(sta_cata) >= 1:
            map_data = wrap_map_object_st(path_station_cata, sta_cata, map_data)
        return {'data': map_data, 'layout': map_layout}
    else:
        return {'data': map_data, 'layout': map_layout}

@app.callback(Output('url', 'value'),
              [Input('cont_button', 'on_clicks'), Input('view_cont_wf', 'href'),
               Input('evt_button', 'on_clicks'), Input('ana_eq_cata', 'href'),
               Input('evtwf_button', 'on_clicks'), Input('view_event_wf', 'href')])
def change_url(cont, cont_link, evt, evt_link, evtwf, evtf_link):
    if cont:
        return cont_link
    elif evt:
        return evt_link
    elif evtwf:
        return evtf_link
    else:
        return '/'


