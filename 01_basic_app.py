import dash
from dash import html

app = dash.Dash()

app.layout = html.H5('Test app')


if __name__ == "__main__":
    app.run_server(debug=True, host = '0.0.0.0' ,port=1112)
