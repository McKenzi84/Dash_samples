# Import libaries
import dash
from dash import html, Input, Output
import dash_bootstrap_components as dbc

import ezdxf
from ezdxf.addons.drawing import matplotlib
import base64


app = dash.Dash()

app.layout = dbc.Row([
            html.H5('Test app'),
            dbc.Input(id='input',type='number', value=5),
            html.Div(id='output'),
])

@app.callback(
    Output('output', 'children'),
    Input('input', 'value'),
    
)

def render_dxf(radius):
    '''Function  creates .dxf file, .png file and renders using Matplotlib '''
    # Creating new document 
    doc = ezdxf.new()
    msp = doc.modelspace()
    # Adding circles entities  to modelspace
    msp.add_circle(center=(0,0), radius=5)
    msp.add_circle(center=(0,0), radius=radius)
    # Matplotlib saves document to .png
    matplotlib.qsave(doc.modelspace(),"_temporary/circle.png", dpi=150)
    

    test_png = "_temporary/circle.png"
    base64.b64encode(open(test_png,'rb').read()).decode('ascii')    
    test_base64 = base64.b64encode(open(test_png,'rb').read()).decode('ascii')
    pic = html.Img(src='data:image/png;base64,{}'.format(test_base64))

    # Save document to .dxf
    #doc.saveas('_temporary/circle.dxf')
    
    return pic


if __name__ == "__main__":
    app.run_server(debug=True, host = '0.0.0.0' ,port=1112)