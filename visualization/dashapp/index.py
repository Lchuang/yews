#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from apps import geomaps, Continuous_WF

# ---- 02. Page contents
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/Continuous_WF':
        return Continuous_WF.layout
    elif pathname == '/':
        return geomaps.layout

if __name__ == '__main__':
    app.run_server(debug=True)