import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import random

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])
app.title = "Flashcards for jazz practice"
server = app.server

app.layout = html.Div([
    dcc.Checklist(
        id='exercise-selection',
        options=[{'label': " " + i, 'value': i} for i in ["Arpeggio", "Chords", "Scale"]],
        value=["Arpeggio", "Chords", "Scale"],
        inline=True,
        labelStyle={'margin-right': '20px'}
    ),
    html.Div(style={'height': '50px'}),
    html.Button('Next', id='next-button', n_clicks=0),
    html.Div(style={'height': '50px'}),
    html.H1(id='flashcard-display', children='Press Next to start', style={'fontSize': '100px'}),
], style={'margin': '5% auto', 'maxWidth': '800px', 'textAlign': 'center'}, id='app-layout')

@app.callback(
    Output('flashcard-display', 'children'),
    [Input('next-button', 'n_clicks'),
     Input('exercise-selection', 'value')]
)
def update_output(n_clicks, selected_exercises):
    if n_clicks > 0:
        return flashcard(selected_exercises)
    else:
        return 'Press Next to start'

def flashcard(selected_exercises):
    keys = ["A", "B♭", "B", "C", "C♯", "D", "E♭", "E", "F", "F♯", "G", "A♭"]
    scales = ["Δ", "-7", "7", "ii-V7-I"]
    return random.choice(keys) + random.choice(scales) + ": " + random.choice(selected_exercises)

if __name__ == '__main__':
    app.run_server(debug=True)