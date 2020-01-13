#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import callbacks
from app import app
from layouts import *

# ---- 01. style sheets
style_temp = {'height': '6%', 'width': '100%', 'display': 'inline-block', 'automargin': True}
# ---- 02. Page contents
layout = html.Div([
    html.Div([
        html.Div([
            html.Center(html.P('Earthquake Catalog')),
            html.Div(eqs_loc_layout, className="geomap_drop_down")
        ]),
        html.Div([
            html.Center(html.P('Earthquake Phase Catalog')),
            html.Div(phase_loc_layout, className="geomap_drop_down")
        ]),
        html.Div([
            html.Center(html.P('Station Catalog')),
            html.Div(sta_loc_layout, className="geomap_drop_down"),
        ]),
        html.Div([
            html.Center(html.P('Catalog Statistics')),
            html.Div(idx_tabs),
            html.P(id='showtext'),
        ], className="geomap_showtexts"),
        html.Div([
            html.Div(view_events_sta, className="geomap_one_button"),
            html.Div(view_waveform_evt, className="geomap_one_button"),
            html.Div(view_waveform_cont, className="geomap_one_button"),
        ],
                 style=style_temp),
        html.Div([], style=style_temp),
        html.Div(mode_switch, className="geomap_drop_down"),
    ], className="geomap_left_block"),

    html.Div(geomap_layout,
             className="geomap_map_area"),
],
    className="geomap_background_canvas")