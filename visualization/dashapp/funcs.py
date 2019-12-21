#!/Users/lindsaychuang/miniconda3/envs/obspy/bin/python
import pandas as pd
from obspy import UTCDateTime
import dash_html_components as html

def wrap_map_object_eq(path_earthquake_cata,pd_cata, map_data):
    pd_cata = pd.read_csv(f'{path_earthquake_cata}/{pd_cata[0]}')
    map_data[0]["lat"] = pd_cata.evla.values
    map_data[0]["lon"] = pd_cata.evlo.values
    map_data[0]['marker']['size'] = pd_cata.mag.values
    map_data[0]["text"] = pd_cata.time.values
    map_data[0]['marker']['color'] = pd_cata.evdp.values
    return map_data
def wrap_map_object_st(path_station_cata,st_cata, map_data):
    st_cata = pd.read_csv(f'{path_station_cata}/{st_cata[0]}')
    map_data[1]["lat"] = st_cata.stla.values
    map_data[1]["lon"] = st_cata.stlo.values
    map_data[1]["text"] = st_cata.station.values
    return map_data

def quick_analysis_eq_catalog(path,files):
    pd_cata = pd.read_csv(f'{path}/{files[0]}')
    pd_datetime = pd.to_datetime(pd_cata[["year", "month", "day", "hour", "minute", "second"]])
    earlist = pd_datetime.min()
    latest = pd_datetime.max()
    total_event_number = len(pd_cata)
    return earlist, latest, total_event_number

def quick_analysis_phase_catalog(path,files):
    pd_cata = pd.read_csv(f'{path}/{files[0]}')
    pd_datetime = pd.to_datetime(pd_cata[["year", "month", "day", "hour", "minute", "second"]])
    earlist = pd_datetime.min()
    latest = pd_datetime.max()
    total_event_number = len(pd_cata)
    return earlist, latest, total_event_number


def quick_analysis_sta_catalog(path,files):
    st_cata = pd.read_csv(f'{path}/{files[0]}')
    networks = st_cata.network.unique()
    channels = st_cata.channel.unique()
    total_number = len(st_cata.station.unique())
    return networks, channels, total_number








