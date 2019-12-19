#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import callbacks
from app import app
from layouts import eqs_loc_layout, sta_loc_layout, mode_switch, geomap_layout, icon_nob, idx_tabs

# ---- 01. style sheets
style_background_canvas = {'height': 800, 'automargin': True}
style_drop_down = {'height': '20%', 'width': '100%', 'display': 'inline-block', 'automargin': True}
style_update_mode = {'height': '100%', 'width': '40%', 'display': 'inline-block', 'automargin': True,
                     'vertical-align': 'bottom'}
style_update_switch = {'height': '100%', 'width': '59%', 'display': 'inline-block', 'automargin': True}
style_map_area = {'height': 800, 'width': '70%', 'display': 'inline-block',
                  'automargin': True, 'vertical-align': 'top'}
style_left_block = {'height': '100%', 'width': '30%', 'backgroundColor': 'rgba(249,249,249,1)',
                    'display': 'inline-block', 'automargin': True, 'vertical-align': 'top'}
style_temp = {'height': '40%', 'width': '100%', 'display': 'inline-block', 'automargin': True}

# ---- 02. Page contents
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Center(html.P('Earthquake Catalog')),
            html.Div(eqs_loc_layout, style=style_drop_down)
        ]),
        html.Div([
            html.Center(html.P('Station Catalog')),
            html.Div(sta_loc_layout, style=style_drop_down),
        ]),
        html.Div([
            html.Center(html.P('Catalog Statistics')),
            html.Div(idx_tabs),
            html.P(id='showtext'),
        ], style=style_temp),
        html.Div(icon_nob, style=style_drop_down),
        html.Div(mode_switch, style=style_drop_down),
    ], style=style_left_block),

    html.Div(geomap_layout,
             style=style_map_area),
],
    style=style_background_canvas)

if __name__ == '__main__':
    app.run_server(debug=True)