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
    label="icon_scale",
    size=100,
    value=5,
    max=5,
    scale={'start': 0, 'labelInterval': 1, 'interval': 1}
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
index_date_picker = dcc.DatePickerRange(
    id='idx_dtp',
    display_format='M-D-Y'
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
