#Import dependencies 
import dash
import plotly 
import plotly.express as px
import plotly.graph_objects as go
from dash import html
from dash import dcc
from dash.dependencies import Input, Output  
import pandas as pd


#initialising dash app
app = dash.Dash()   

#reading joined netflix dataset 
df = pd.read_csv('../Netflix_Team_1/Resources/netflix_updated_with_genres.csv', low_memory=False)

available_indicators = df.columns.unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='language'
            ) 
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='rating'
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='year--slider',
        min=df['start_year'].min(),
        max=df['start_year'].max(),
        value=df['start_year'].max(),
        marks={str(year): str(year) for year in df['start_year'].unique()},
        step=None
    )
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('year--slider', 'value'))

def update_graph(xaxis_column_name, yaxis_column_name, year_value):
    
    # year_value = df['start_year']
    dff = df[df['start_year'] == year_value]


    fig = px.scatter(
                    x=df['{}'.format(xaxis_column_name)],
                    y=df['{}'.format(yaxis_column_name)],
                    hover_name = df['title'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, 
                    hovermode='closest')
    fig.update_layout(title = 'Interactive Graph')

    fig.update_xaxes(title=xaxis_column_name)

    fig.update_yaxes(title=yaxis_column_name)

    return fig

if __name__ == '__main__': 
    app.run_server(debug=True)