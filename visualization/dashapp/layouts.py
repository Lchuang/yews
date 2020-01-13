#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
# this file defines all the layouts used in apps
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_daq as daq
from dash_table.Format import Format
import datetime



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
            'margin': {"r": 0, "t": 0, "l": 5, "b": 0}
        }
map_data = [
            {'name': "events",
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
# ---- 04. phase catalog drop-down list
phase_loc_layout = dcc.Dropdown(id='phase_loc_dw',
                              options=[],
                              placeholder='select an earthquake phase catalog',
                              multi=True
                              )
# ---- 04. station catalog drop-down list
sta_loc_layout = dcc.Dropdown(id='sta_loc_dw',
                              options=[],
                              placeholder='select a station catalog',
                              multi=True
                              )
# ---- 06. continuous waveform path
deployment_path = dcc.Dropdown(id='deployment_pt',
                              options=[],
                              placeholder='select deployment output path',
                              multi=False
                            )
# ---- 05. mode radio buttons
mode_button = dcc.RadioItems(
    options=[
        {'label': 'simultaneous', 'value': 'sim'},
        {'label': 'manual', 'value': 'manual'}
    ]
)

# ---- 06. mode switch
mode_switch = daq.BooleanSwitch(
    id='mode_switch',
    on=False,
    label='Instant Update',
    labelPosition='top',
),

# ---- 07. Icon nob
icon_nob = daq.Knob(
    label="Display length (mins)",
    size=100,
    value=5,
    max=5,
    scale={'start': 0, 'labelInterval': 1, 'interval': 0.5},
    id="win_nob"
)

# ---- 08. Tabs
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}
idx_tabs = dcc.Tabs(id="index_page_tab", value='earthquakes', children=[
    dcc.Tab(label='earthquakes', value='earthquakes', style=tab_style, selected_style=tab_selected_style),
    dcc.Tab(label='phases', value='phases', style=tab_style, selected_style=tab_selected_style),
    dcc.Tab(label='stations', value='stations', style=tab_style, selected_style=tab_selected_style)
])

# ---- 09. date-time picker
cont_date_picker = dcc.DatePickerSingle(
    id='cont_dtp',
    display_format='M-D-Y',
)

# ---- 10. time input
cont_hours_input = daq.NumericInput(
    id='hour_inout',
    max=23,
    value=8,
    min=0,
    label='Hour'
)
cont_minutes_input = daq.NumericInput(
    id='min_inout',
    max=59,
    value=20,
    min=0,
    label='Min'
)
cont_seconds_input = daq.NumericInput(
    id='sec_inout',
    max=59,
    value=30,
    min=0,
    label='Sec'
)

# ---- 11. Time range slider
time_slider = dcc.RangeSlider(
    id="time_slider",
    min=0,
    max=86400,
    step=86400,
    value=[0, 86400],
    marks={i: f'{i}'
           for i in range(0, 86400, 10000)
           }

)
# ---- button css
# ---- 10.analysis button
view_waveform_evt = html.A(
    id='view_event_wf',
    children=html.Button('View Event Waveform', type='submit', id='evtwf_button'),
    href='http://www.yahoo.com',
    target='_blank'
)
# ---- 11. catalog analysis button
view_events_sta = html.A(
    children=html.Button(
        'Analyse Catalog', type='submit', id='evt_button'),
    id='ana_eq_cata',
    href='http://www.google.com',
    target='_blank'
)
# ---- 12. view continuous data
view_waveform_cont = html.A(
    children=html.Button(
        'View All Waveform', type='submit', id='cont_button'),
    id='view_cont_wf',
    href='/apps/Continuous_WF',
    target='_blank',
)
# ---- 13. radio item
cont_filter_radio = dcc.RadioItems(
    options=[
        {'label': 'raw', 'value': 'raw'},
        {'label': 'bandpass', 'value': 'bandpass'},
        {'label': 'highpass', 'value': 'highpass'},
        {'label': 'lowpass', 'value': 'lowpass'},
    ],
    value='bandpass',
    id='filter_type'
)
# ---- 14. filer
cont_filter_low = daq.NumericInput(
    id='filter_low',
    max=50,
    value=2,
    min=0.001,
    label='Low F',
    labelPosition='top',
)

cont_filter_high = daq.NumericInput(
    id='filter_high',
    max=100,
    value=8,
    min=0.001,
    label='High F',
    labelPosition='top',
)
# ---- normalization option
cont_control_norm = dcc.Dropdown(
    id='norm_control',
    options=[
        {'label': 'Original Scale', 'value': 'Original Scale'},
        {'label': 'Normalize', 'value': 'Normalize'},
    ],
    placeholder='select normalization style',
    multi=False,
    value="Normalize"
)
# ---- waveform source option
cont_wf_path = dcc.Dropdown(id='cont_wf_pt',
                              options=[],
                              placeholder='select continuous waveform path',
                              multi=False
                            )
# ---- 17. Tab control content
Cont_control_tab = html.Div([
    html.P("Settings for waveform display", className="cont_control_display_title"),
    html.Div([
        html.P("Waveform Normalization Mode"),
        html.Div(cont_control_norm),
        html.P("Select Continuous Waveform Source"),
        html.Div(cont_wf_path),
        html.P('Select CPIC Deployment Source'),
        html.Div(deployment_path),
    ], className="cont_control_display_left")
])
# ---- 15. Continuous waveform display
cont_wf_tabs = dcc.Tabs(id="cont_wf_tabs", value='Control',
                        children=[
                            dcc.Tab(label='N', value='N', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='E', value='E', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Z', value='Z', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='NEZ', value='NEZ', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(Cont_control_tab, label='Control', value='Control', style=tab_style, selected_style=tab_selected_style)
                        ])
# ---- 16. cont joy stick
browse_wf = daq.Joystick(
        id='move_handle',
        label="Browse waveform",
        angle=0,
        size=60,
    ),
# ---- 18. Tab N control content
Cont_N_tab = dcc.Loading(
    id='loadN', children=html.Div([dcc.Graph(id='N_comp_wfs')]))
Cont_E_tab = dcc.Loading(
    id='loadE', children=html.Div([dcc.Graph(id='E_comp_wfs')]))
Cont_Z_tab = dcc.Loading(
    id='loadZ', children=html.Div([dcc.Graph(id='Z_comp_wfs')]))
Cont_NEZ_tab = dcc.Loading(
    id='loadNEZ', children=html.Div([dcc.Graph(id='NEZ_comp_wfs')]))