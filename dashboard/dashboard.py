#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

data = pd.read_csv('clients.csv',sep=",")
data2 = pd.read_csv('M.csv',sep=",")

header = html.H2(children="Credit Card Clients Dashboard")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

chart9 = px.pie(data_frame=data,names='MARRIAGE',labels='MARRIAGE', color='MARRIAGE',
           color_discrete_sequence=px.colors.sequential.Blugrn,
           title="Marriage Content of Clients")

graph9 = dcc.Graph(
        id='graph9',
        figure=chart9, 
        className="six columns")

chart10 = px.histogram(data_frame=data2,
             x="MARRIAGE",
             y="percent",
             color="MARRIAGE",
             facet_col = "default payment next month",
             color_discrete_sequence=px.colors.sequential.Blugrn,
             title="Default payment next month Content of Clients Color-encoded by Marriage ")
chart10.update_layout(yaxis_title="Percent")

graph10 = dcc.Graph(
        id='graph10',
        figure=chart10,
        className="six columns")

chart12 = px.scatter(data_frame=data,
           x="LIMIT_BAL",
           color="MARRIAGE",
           facet_col = "default payment next month",
           color_discrete_sequence=px.colors.sequential.Blugrn,
           title="Age vs Limit Balance of Clients Color-encoded by Marriage")
chart12.update_layout(yaxis_title="Clients")

graph12 = dcc.Graph(
        id='graph12',
        figure=chart12,
        className="six columns")

row5 = html.Div(children=[graph9,graph10])
row6 = html.Div(children=[graph12])

layout = html.Div(children=[header,row5,row6], style={"text-align": "center"})

app.layout = layout


if __name__ == "__main__":
    app.run_server(debug=False)


# In[ ]:


import numpy as np
import pandas as pd

import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

data = pd.read_csv('clients.csv',sep=",")
data1 = pd.read_csv('S.csv',sep=",")
header = html.H2(children="Credit Card Clients Dashboard")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

chart1 = px.pie(data_frame=data,names='SEX',labels='SEX', color='SEX',
                color_discrete_sequence=["#87CEFA","#00BFFF"],
                title="Gender Content of Clients")

graph1 = dcc.Graph(
        id='graph1',
        figure=chart1, 
        className="six columns")

chart2 = px.histogram(data_frame=data1,
             x = "SEX",
             y = " percent",
             color="SEX",
             facet_col = "default payment next month",
             color_discrete_sequence=["#87CEFA","#00BFFF"],
             title="Default payment next month Content of Clients Color-encoded by Gender ")
chart2.update_layout(yaxis_title="Percent")

graph2 = dcc.Graph(
        id='graph2',
        figure=chart2,
        className="six columns")

chart4 = px.scatter(data_frame=data,
           x = "LIMIT_BAL",
           color="SEX",
           color_discrete_sequence=["#87CEFA","#00BFFF"],
           facet_col = "default payment next month",
           title="Age vs Limit Balance of Clients Color-encoded by Gender")

graph4 = dcc.Graph(
        id='graph4',
        figure=chart4,
        className="six columns")

chart4.update_layout(yaxis_title="Clients")



row1 = html.Div(children=[graph1,graph2])
row2 = html.Div(children=[graph4])

layout = html.Div(children=[header, row1,row2], style={"text-align": "center"})

app.layout = layout


if __name__ == "__main__":
    app.run_server(debug=False)


# In[ ]:


import numpy as np
import pandas as pd

import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

data = pd.read_csv('clients.csv',sep=",")
data2 = pd.read_csv('E.csv',sep=",")

header = html.H2(children="Credit Card Clients Dashboard")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

chart5 = px.pie(data_frame=data,names='EDUCATION',labels='EDUCATION', color='EDUCATION',
           color_discrete_sequence=px.colors.sequential.Magenta,
           title="Education Content of Clients")

graph5 = dcc.Graph(
        id='graph5',
        figure=chart5, 
        className="six columns")

chart6 = px.histogram(data_frame=data2,
             x="EDUCATION",
             y = "percent",
             color="EDUCATION",
             facet_col = "default payment next month",
             color_discrete_sequence=px.colors.sequential.Magenta,
             title="Default payment next month Content of Clients Color-encoded by Education ")
chart6.update_layout(yaxis_title="Percent")

graph6 = dcc.Graph(
        id='graph6',
        figure=chart6,
        className="six columns")

chart8 = px.scatter(data_frame=data,
           x="LIMIT_BAL",
           color="EDUCATION",
           color_discrete_sequence=px.colors.sequential.Magenta,
           facet_col = "default payment next month",
           title="Age vs Limit Balance of Clients Color-encoded by Education")

graph8 = dcc.Graph(
        id='graph8',
        figure=chart8,
        className="six columns")
chart8.update_layout(yaxis_title="Clients")

row5 = html.Div(children=[graph5,graph6])
row6 = html.Div(children=[graph8])

layout = html.Div(children=[header,row5,row6], style={"text-align": "center"})

app.layout = layout


if __name__ == "__main__":
    app.run_server(debug=False)


# In[ ]:




