# Import Packages
import pickle
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly_express as px

# Load Data
import pandas as pd
from dash import html

filename = '/Users/bintualkassoum/Downloads/rooms_model.pkl'
rooms_model = pd.read_pickle(filename)
rooms_model

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

# Layout Section: Bootstrap
# ---------------------------------------------------------------------------------
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Netflix Rooms Dashboard',
                        className='sticky-top, mb-4'),
                wide=12)
    ]),



])

if __name__=='__main__':
    app.run_server(debug=True, port=3000)
