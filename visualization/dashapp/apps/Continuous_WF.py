#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import callbacks
from app import app

from layouts import *

# ---- 01. style sheets
style_temp = {'height': '6%', 'width': '100%', 'display': 'inline-block', 'automargin': True}

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
        html.Div([], style=style_temp),
        html.Div([
            html.Div([
                html.Div(cont_date_picker, className="cont_date_picker"),
                html.Div(cont_hours_input, className="timepickers"),
                html.Div(cont_minutes_input, className="timepickers"),
                html.Div(cont_seconds_input, className="timepickers"),
            ], className='datetimes_block'),
            html.Div(icon_nob, className="datetimes_block"),
        ]),
        html.Div([
            html.Div([
                html.Div(cont_filter_radio),
                html.Div(cont_filter_low, className="filternumber"),
                html.Div(cont_filter_high, className="filternumber"),
            ], className="datetimes_block"),
            html.Div([
                html.Div(browse_wf),
                html.Div(mode_switch),
            ], className="datetimes_block"),
        ])
    ], className="geomap_left_block"),
    html.Div(
        [html.Div(cont_wf_tabs),
         html.Div(id='cont_wf_display_content')
         ], className="cont_wf_display_bg"),
    html.Div(id='contpath', style={'display': 'none'}),
    html.Div(id='contdept', style={'display': 'none'}),
    html.Div(id='normmode', style={'display': 'none'}),

],
    className="geomap_background_canvas")

