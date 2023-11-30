import geopandas as gpd
import pandas as pd

def parse_gpx(file) -> pd.DataFrame:
    return gpd.read_file(file, layer='track_points')

df = parse_gpx('data/ride.gpx')

df.to_csv('data/ride.csv')
