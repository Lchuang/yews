#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_html_components as html
import plotly.graph_objects as go
from funcs import *
from app import app
import glob
from obspy import UTCDateTime
import datetime
import pandas as pd
from layouts import Cont_control_tab, Cont_N_tab, Cont_E_tab, Cont_Z_tab, Cont_NEZ_tab

# ---- set some path
path_cont_wf = '../waveform/continuous'
deployment_out_pt = '../deployment'
path_station_cata = '../station_catalog'

# ---- 02. callback for continuous waveform path ----
@app.callback(
    Output("cont_wf_pt", "options"),
    [Input("cont_wf_pt", "search_value")],
)
def update_options(search_value):
    print(f'set waveform root path at {path_cont_wf}')
    options = []
    cata_list = glob.glob(f'{path_cont_wf}/*')
    for lst in cata_list:
        lst = lst.split('/')[-1]
        options.append({'label': lst, 'value': lst})
    return options

# ---- 02. callback for continuous waveform path ----
@app.callback(
    Output("deployment_pt", "options"),
    [Input("deployment_pt", "search_value")],
)
def update_options(search_value):
    print(f'set deployment root path at {deployment_out_pt}')
    options = []
    cata_list = glob.glob(f'{deployment_out_pt}/*')
    for lst in cata_list:
        lst = lst.split('/')[-1]
        options.append({'label': lst, 'value': lst})
    return options

# ---- 02. callback for station catalog search ----
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

# ---- cont_date_picker callback
@app.callback(
    [Output('cont_dtp', 'date'), Output('hour_inout', 'value'),
     Output('min_inout', 'value'), Output('sec_inout', 'value')],
    [Input('mode_switch', 'on'), Input('eq_loc_dw', 'value')])
def set_initial_datetime(on_off, eq_cata):
    if on_off is True and eq_cata is not None and len(eq_cata) >= 1:
        earlist, latest, total_event_number = quick_analysis_eq_catalog(path_earthquake_cata, eq_cata)
        return [str(earlist), earlist.hour, earlist.minute, earlist.second]
    else:
        nowt = datetime.datetime.now()
        return [str(nowt), nowt.hour, nowt.minute, nowt.second]


# ---- cont tab for controlling
@app.callback(
    Output('cont_wf_display_content', 'children'),
    [Input('cont_wf_tabs', 'value')])
def render_cont_wf_display_tab(tab):
    if tab == "N":
        return Cont_N_tab
    elif tab == "E":
        return Cont_E_tab
    elif tab == "Z":
        return Cont_Z_tab
    elif tab == "NEZ":
        return Cont_NEZ_tab

# ---- update N component waveform
@app.callback(
    [Output('N_comp_wfs', 'figure'),
     Output('E_comp_wfs', 'figure'),
     Output('Z_comp_wfs', 'figure'),
     Output('NEZ_comp_wfs', 'figure')],
    [Input('mode_switch', 'on'),
     Input('cont_wf_tabs', 'value'),
     Input('cont_dtp', 'date'),
     Input('hour_inout', 'value'),
     Input('min_inout', 'value'),
     Input('sec_inout', 'value'),
     Input('win_nob', 'value'),
     Input('filter_type', 'value'),
     Input('filter_low', 'value'),
     Input('filter_high', 'value'),
     Input('norm_control', 'value'),
     Input('cont_wf_pt', 'value'),
     Input('deployment_pt', 'value'),
     Input('sta_loc_dw', 'value')]
)
def update_graph(on_off, NEZ, date, hour, min, sec, win, filter, lf, hf, norm, cont_p, depl_p, stalst):
    date = date.split(' ')[0]
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])
    btime = UTCDateTime(year, month, day, hour, min, sec)
    etime = btime + win * 60
    wf_path = f'{path_cont_wf}/{cont_p}/{year}/{year}{month:02d}{day:02d}'
    if on_off is True and stalst is not None and len(stalst) >= 1:
        st_path = f'{path_station_cata}/{stalst[0]}'
        sta_lst = pd.read_csv(st_path).station.values
        if NEZ == 'N':
            print("loading waveform")
            st = load_wfs(wf_path, sta_lst, btime, etime, 'N')
        if NEZ == 'E':
            print("loading waveform")
            st = load_wfs(wf_path, sta_lst, btime, etime, 'E')
        if NEZ == 'Z':
            print("loading waveform")
            st = load_wfs(wf_path, sta_lst, btime, etime, 'Z')
        if NEZ == 'NEZ':
            print("loading waveform")
            st = load_wfs(wf_path, sta_lst, btime, etime, 'All')
        print(len(st))
        if len(st) >= 1:
            st = filters(st, filter, lf, hf)
            st = norm_wfs(st, norm)
            objs = wrap_wfs(st)
            print("finish loading waveform")
            objs.layout = {'height': len(st)*50, 'yaxis': {'autorange': "reversed"}, 'hovermode': 'closest'}
        else:
            objs = go.Figure()
    else:
        objs = go.Figure()
    return [objs, objs, objs, objs]