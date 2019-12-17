#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
# --- this app displays a map for event location visualization
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from layouts import geomap_layout
from app import app
