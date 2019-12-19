#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_html_components as html
from app import app
import glob

# ---- 03. callback for instantaneously updating station and catalog


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
# ---- 02. callbacks for statistics
@app.callback(Output('showtext', 'children'),
              [Input('mode_switch', 'on'), Input('index_page_tab', 'value')])
def render_content(on_off, tab):
    if on_off == True:
        if tab == 'earthquakes':
            return html.Div([
                html.H3('Earthquake Statistics')
            ])
        elif tab == 'stations':
            return html.Div([
                html.H3('Station Statistics')
            ])