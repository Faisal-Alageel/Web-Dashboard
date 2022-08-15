import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import plotly as p
import plotly.offline as pyo 
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash()


x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
y1 = np.random.randint(2,20,12)
y2 = np.random.randint(2,20,12)

def cards():
    first_card = dbc.Card(
        dbc.CardBody(
            [
                html.H5("Population size", className="card-title"),
                html.H3(str(np.random.randint(20,30)),style={'color':'#6b6a6b'}),
            ]
        )
        
    ,
    style={'maxWidth': '200px','display': 'inline-block', 'border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'height':'193px',
                                 'width':'200px',
                                 'padding': '5px',
                                 'background-color' : '#ffffff',
                                'textAlign':'center',
                                 'margin-left': '5px',
                                 'margin-bottom': '10px',})


    second_card = dbc.Card(
        dbc.CardBody(
            [
                html.H5("Population age range", className="card-title"),
                html.H3(str(np.random.randint(0,5))+" - "+str(np.random.randint(50,70)),style={'color':'#6b6a6b'}),
            ]

        )
    ,
    style={'maxWidth': '200px','display': 'inline-block', 'border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'height':'193px',
                                 'width':'200px',
                                 'padding': '5px',
                                'textAlign':'center',
                                 'background-color' : '#ffffff',
                                 'margin-bottom': '10px',
                                 'margin-left': '5px'})

  

    cards = dbc.Col(children=[
            dbc.Row(first_card),
            dbc.Row(second_card)],
            style={'maxWidth': '800px','display': 'inline-block', 
                                 'verticalAlign': 'top',
                                'textAlign':'center',
                                'color':'#575757', 'font-size':25,'font-family':'Segoe UI',
                                 'margin-left': '5px'}
            )
    return cards

def bubble(colorscale,fig_title):
    Ages = np.random.randint(5,70,20)
    Heights = np.linspace(140,200,20)
    weights=np.random.randint(50,150,20)
    DATA=[go.Scatter(x=Heights,y=weights,mode='markers',marker=dict(size=Ages/1.5, color=Ages,colorbar=dict(title='Ages'), colorscale=colorscale,  opacity=0.8, showscale=True), name='markers')]
    layout= go.Layout(title=fig_title,title_x=0.5, xaxis=dict(title='Height (cm)'),
    yaxis = dict(title='Weight (kg)'),
    paper_bgcolor = '#ffffff',
    width=700,
    height = 300,
    margin=dict(l=5, r=50, t=30, b=20),
    hovermode = 'closest',plot_bgcolor='#ffffff', font=dict(family='Segoe UI',size=15),title_font_size=20)
    fig = go.Figure(data=DATA,layout=layout)
    fig.update_xaxes(gridcolor='#e8e8e8'),
    fig.update_yaxes(gridcolor='#e8e8e8')

    return fig


def doublebar(fig_title=''):
    x = ['Skinny','Normal','Over-Weight','Obese']
    y1 = np.random.randint(15,30,4)
    y2 = np.random.randint(15,30,4)                                                         
    
    DATA=[go.Bar(x=x,y=y1,name='Males', marker_color='#2B2B2B', marker_line_color='#ffffff',marker_line_width=1,opacity=0.8,textposition='auto'),
    go.Bar(x=x,y=y2,name='Females', marker_color='#AFAFAF', marker_line_color='#ffffff',marker_line_width=1,opacity=0.8,textposition='auto')]

    layout= go.Layout(title=fig_title,
    font=dict(family='Segoe UI',size=12),
    plot_bgcolor='#ffffff',
    xaxis=dict(title='Body Mass Index'),
    height=300,
    width=500,
    showlegend=True,
    title_x=0.5,
    title_font_size=30,
    yaxis = dict(title='Count'),
    paper_bgcolor = '#ffffff',
    legend=dict(
    bgcolor='rgba(0,0,0,0)',
    yanchor="top",
    y=1.15,
    xanchor="right",
    font = dict( size = 10),
    x=1.2),
    margin=dict(l=5, r=30, t=20, b=20),
    hovermode = 'closest')

    fig = go.Figure(data=DATA,layout=layout)
    fig.update_yaxes(gridcolor='#e8e8e8')
    return fig


def pie(fig_title):
    x = ['Skinny','Normal','Over-Weight','Obese']
    y = np.random.randint(10,100,4)
    x2 = ['Females','Males']
    y2 = np.random.randint(15,20,2)
    DATA=[go.Pie(labels=x2,values=y2,opacity=0.8, textfont_color = '#ffffff',                                        
    textposition='inside', rotation = 90,texttemplate = "%{label}<br>%{percent}",showlegend=False,marker=dict(colors=['#AFAFAF','#2B2B2B'])),                                                                                    
    go.Pie(labels=x,values=y, opacity=0.8,hole=.75, textposition="outside",textfont_color = '#0d0d0d',marker=dict(colors=['#E1E1E1','#B3BDD4' ,'#365194','#253354']))]
    layout= go.Layout(title=fig_title,
    font=dict(family='Segoe UI',size=18),
    plot_bgcolor='#ffffff',
    title_x=0.5,
    title_font_size=30,
    paper_bgcolor = '#ffffff',
    width=500,
    height = 300,
    margin_autoexpand=False,
    margin=dict(l=30, r=50, t=28, b=30),
    legend=dict(
    bgcolor='rgba(0,0,0,0)',
    yanchor="top",
    y=1.15,
    xanchor="right",
    font = dict( size = 10),
    x=1.1,
),
    hovermode = 'closest')

    fig = go.Figure(data=DATA,layout=layout)
    fig.data[0].domain = {'x': [0, 1], 'y': [0.2, 0.8]}
    return fig



def pie2(fig_title):
    x = ['< 1500','1500-2000','2000-2500','> 2500']
    y = np.random.randint(10,100,4)                                                                                   
    DATA=[go.Pie(labels=x,values=y, opacity=0.8, textposition="outside",textfont_color = '#0d0d0d',marker=dict(colors=['#E1E1E1','#B3BDD4' ,'#365194','#253354']))]
    layout= go.Layout(title=fig_title,
    font=dict(family='Segoe UI',size=20),
    plot_bgcolor='#ffffff',
    title_x=0.5,
    title_y=1,
    title_font_size=15,
    paper_bgcolor = '#ffffff',
    width=400,
    height = 250,
    margin_autoexpand=False,
    margin=dict(l=40, r=100, t=60, b=30),
    legend=dict(
    bgcolor='rgba(0,0,0,0)',
    yanchor="top",
    y=1,
    xanchor="right",
    font = dict( size = 10),
    x=1.4),
    hovermode = 'closest')

    fig = go.Figure(data=DATA,layout=layout)
    return fig


def scatter2(Quarter,x,y1,y2):
    if Quarter=='First Quarter': 
        x=x[0:3]
        y1=y1[0:3]
        y2=y2[0:3]
    elif Quarter=='Second Quarter':
        x=x[3:6]
        y1=y1[3:6]
        y2=y2[3:6]
    elif Quarter=='Third Quarter':
        x=x[6:9]
        y1=y1[6:9]
        y2=y2[6:9]
    elif Quarter=='Forth Quarter':
        x=x[9:]
        y1=y1[9:]
        y2=y2[9:]
    elif Quarter=='Default':
        x=x
        y1=y1
        y2=y2

    d1=go.Scatter(x=x,y=y1,mode='lines+markers',name='Fast Food consumption', marker=dict(color='#707070'))
    d2 = go.Scatter(x=x,y=y2,mode='lines+markers',name='Healthy Food consumption',marker=dict(color='#365194'))
    DATA = [d1,d2]  
    layout= go.Layout(title='Average meals consumed per week by the individual in the past year',
    font=dict(family='Segoe UI',size=15),
    plot_bgcolor='#ffffff',
    title_x=0.5,
    title_y = 1,
    xaxis=dict(title='Month'),
    yaxis = dict(title='Meals per week'),
    paper_bgcolor = '#ffffff',
    width = 1000,
    height = 400,
    legend=dict(
    bgcolor='rgba(0,0,0,0)',
    yanchor="top",
    y=1.15,
    xanchor="right",
    font = dict( size = 10),
    x=1,
    ),
    margin=dict(l=0, r=0, t=60, b=30),
    hovermode = 'closest')
    fig = go.Figure(data=DATA,layout=layout)
    fig.update_xaxes(gridcolor='#e8e8e8'),
    fig.update_yaxes(gridcolor='#e8e8e8')
    return fig




def Img(src):
    fig = go.Figure()
    img_width = 50
    img_height = 50
    scale_factor = 0.5
    fig.add_trace(
        go.Scatter(
            x=[0, img_width * scale_factor],
            y=[0, img_height * scale_factor],
            mode="markers",
            marker_opacity=0
        )
    )

    fig.update_xaxes(
        visible=False,
        range=[0, img_width * scale_factor]
    )

    fig.update_yaxes(
        visible=False,
        range=[0, img_height * scale_factor],
        scaleanchor="x"
    )

    fig.add_layout_image(
        dict(
            x=0,
            sizex=img_width * scale_factor,
            y=img_height * scale_factor,
            sizey=img_height * scale_factor,
            xref="x",
            yref="y",
            opacity=1.0,
            layer="below",
            sizing="stretch",
            source=src)
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        width=img_width * scale_factor,
        height=img_height * scale_factor,
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )

    return fig




def gauge2():                   
    plot_bgcolor = '#ffffff'
    quadrant_colors = [plot_bgcolor ,'#253354','#365194','#B3BDD4','#E1E1E1'] 
    quadrant_text = ["", "<b>>35</b>", "<b>25-35</b>", "<b>15-25</b>","<b><15</b>"]
    n_quadrants = len(quadrant_colors) - 1

    current_value = np.random.randint(15,50)
    min_value = 10
    max_value = 40
    hand_length = np.sqrt(2) / 4
    hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))

    fig = go.Figure(
        data=[
            go.Pie(
                values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),
                rotation=90,
                hole=0.5,
                marker_colors=quadrant_colors,
                text=quadrant_text,
                textinfo="text",
                textposition='inside',
                textfont_size = 10, 
                hoverinfo="skip",
            ),
        ],
        layout=go.Layout(
            showlegend=False,
            margin_autoexpand=False,
            margin=dict(b=0,t=30,l=0,r=0),
            width=200,
            height=193,
            font=dict(family='Segoe UI',size=15),
            
            paper_bgcolor=plot_bgcolor,
            annotations=[
                go.layout.Annotation(
                    text=f"<b>Average BMI:</b><br><b>{current_value}</b>",
                    x=0.5, xanchor="center", xref="paper",
                    y=0, yanchor="bottom", yref="paper",
                    showarrow=False,
                )
            ],
            shapes=[
                go.layout.Shape(
                    type="circle",
                    x0=0.48, x1=0.52,
                    y0=0.48, y1=0.52,
                    fillcolor="#333",
                    line_color="#333",
                ),
                go.layout.Shape(
                    type="line",
                    x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                    y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                    line=dict(color="#333", width=4)
                )
            ]
        )
    )

    return fig

Quarters=['First Quarter','Second Quarter','Third Quarter','Forth Quarter','Year']





app.layout = html.Div(style=dict(backgroundColor='#ffffff'),children=[
        html.H1('This Dashboard visualizes demographics of a fake population ',style={'textAlign':'center',
                                    'color':'#6b6a6b', 'font-size':25,'font-family':'Segoe UI'}),
        html.H2('The data is randomly generated, so there is either no patterns or that patterns here dont make sense !',style={'textAlign':'center',
            'color':'#6b6a6b', 'font-size':15, 'font-family':'Segoe UI'}),
        html.Br(),
        html.H1('Gender & Obisity distributions in the population : ',style={'textAlign':'center',                                  
                                    'color':'#6b6a6b', 'font-size':20, 'font-family':'Segoe UI'}),
                                                                            


                                                    
        html.Div([dbc.Col(children=[
            dbc.Row(dcc.Graph(id='1',figure=bubble(['#E1E1E1','#B3BDD4' ,'#365194','#253354'],'Females'),style={'display': 'inline-block', 'border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'padding': '5px',
                                 'background-color' : '#ffffff',
                                 'margin-bottom': '10px',
                                 'verticalAlign': 'top',
                                 'margin-left': '20px'})),
            dcc.Graph(id='2',figure=bubble(['#E1E1E1','#B3BDD4' ,'#365194','#253354'],'Males'),style={'display': 'inline-block', 'border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'padding': '5px',
                                 'background-color' : '#ffffff',
                                'margin-bottom': '10px',
                                 'verticalAlign': 'top',
                                 'margin-left': '20px'})],
                                 style={'maxWidth': '800px','display': 'inline-block', 
                                 'verticalAlign': 'top',
                                'textAlign':'center',
                                'color':'#575757', 'font-size':25,'font-family':'Segoe UI',
                                 'margin-left': '5px'}
                                 )
                
                
                
                ,dbc.Col(children=[
            dbc.Row(dcc.Graph(id='6',figure=pie(''),style={'maxWidth': '800px','display': 'inline-block', 'border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'padding': '5px',
                                 'background-color' : '#ffffff',
                                 'margin-bottom': '10px',
                                 'verticalAlign': 'top',
                                 'margin-left': '5px' 
                              
                                })),dbc.Row(dcc.Graph(id='4',figure=doublebar(''),style={'maxWidth': '800px','display': 'inline-block','border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'padding': '5px',
                                 'background-color' : '#ffffff',
                                 'margin-left': '5px', 
                                 'margin-bottom': '10px',
                                 'verticalAlign': 'top'
                                 }))],style={'maxWidth': '800px','display': 'inline-block', 
                                 'verticalAlign': 'top',
                                'textAlign':'center',
                                'color':'#575757', 'font-size':25,'font-family':'Segoe UI',
                                 'margin-left': '5px'})
                                 
                                 ,
            dbc.Col(children=[
            dbc.Row(cards()),
            dbc.Row(dcc.Graph(id='99',figure=gauge2(),style={'maxWidth': '200px','display': 'inline-block', 'border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'height':'193px',
                                 'width':'200px',
                                 'padding': '5px',
                                'textAlign':'center',
                                 'background-color' : '#ffffff',
                                 'margin-bottom': '10px',
                                 'margin-left': '10px'}))],
            style={'maxWidth': '800px','display': 'inline-block', 
                                 'verticalAlign': 'top',
                                'textAlign':'center',
                                'color':'#575757', 'font-size':25,'font-family':'Segoe UI',
                                 'margin-left': '5px'})]),



        html.H1('Prevalence of fast food and healthy food consumption',style={'textAlign':'center',
                                    'color':'#6b6a6b', 'font-size':20, 'font-family':'Segoe UI'}),

        html.Div([dbc.Col(children=[
            dbc.Row((dcc.Dropdown(id='10',options=Quarters,value=[Quarters[-1]],searchable=False,placeholder="Select a quarter",
                            style={'display': 'inline-block', 
                                 'verticalAlign': 'top', 'font-size':15,'font-family':'Segoe UI',
                                 'width': '1020px',
                                 'margin-left': '10px',
                                 'margin-bottom':'5px'}))),

            dbc.Row(dcc.Graph(id='3',figure=scatter2(Quarters[-1],x,y1,y2),style={ 'display': 'inline-block','border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'padding': '10px',
                                 'margin-bottom': '10px',
                                 'verticalAlign': 'top',
                                 'background-color' : '#ffffff',
                                 'margin-left': '25px',
                                 'width':'1000px'}))], style={'maxWidth': '1100px','display': 'inline-block', 
                                 'verticalAlign': 'top',
                                'textAlign':'center',
                                'color':'#575757','font-family':'Segoe UI',
                                 'margin-left': '5px'}),
            dbc.Col(children=[
             dbc.Row(dcc.Graph(id='8',figure=pie2('Average Daily Calorie Consumption by the indivdual'),style={ 'display': 'inline-block','border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'padding': '10px',
                                 'verticalAlign': 'top',
                                 'background-color' : '#ffffff',
                                 'margin-left': '10px',
                                 'width':'400px'}),style={'display': 'inline-block', 
                                 'verticalAlign': 'top',
                                'textAlign':'center',
                                'color':'#575757','font-family':'Segoe UI',
                                'margin-bottom':'10px',
                                 'margin-left': '5px'}),
        dbc.Row(dbc.Card(
        dbc.CardBody(
            [html.Br(),      
            dbc.Row([dcc.Graph(figure=Img('https://cdn-icons-png.flaticon.com/128/61/61109.png'),style={'display': 'inline-block','verticalAlign': 'top','textAlign':'left'}), dcc.Link('Faisal-alageel',href='https://www.linkedin.com/in/faisal-alageel/',refresh=True,style={'display': 'inline-block','margin-left': '15px','font-family':'Segoe UI','font-size':'20px','verticalAlign': 'top','textAlign':'left',"text-decoration": "none",'color':'#575757'})],style={'display': 'inline-block','verticalAlign': 'top','textAlign':'left'}),            
            html.Br(), 
            html.Br(), 
            dbc.Row([dcc.Graph(figure=Img('https://cdn-icons-png.flaticon.com/128/3781/3781605.png'),style={'display': 'inline-block','verticalAlign': 'top','textAlign':'center'}), dcc.Link('FaisalAhemdAlageel@gmail.com',href='mailto:FaisalAhmedAlageel@gmail.com',refresh=True,style={'display': 'inline-block','margin-left': '15px','font-family':'Segoe UI','font-size':'20px','verticalAlign': 'top','textAlign':'center',"text-decoration": "none",'color':'#575757'})],style={'display': 'inline-block','verticalAlign': 'top','textAlign':'center'}),  
            html.Br(),                               
            html.Br(), 
            dbc.Row([dcc.Graph(figure=Img('https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'),style={'display': 'inline-block','verticalAlign': 'top','textAlign':'center'}), dcc.Link('Faisal-Alageel',href='https://github.com/Faisal-Alageel',refresh=True,style={'display': 'inline-block','margin-left': '15px','font-family':'Segoe UI','font-size':'20px','verticalAlign': 'top','textAlign':'center',"text-decoration": "none",'color':'#575757'})],style={'display': 'inline-block','verticalAlign': 'top','textAlign':'center'}),  
 ])  ,

    style={'maxWidth': '1000px','display': 'inline-block', 'border-radius': '0px','box-shadow': '0px 0px 2px 2px #dbdbdb',
                                 'height':'165px',
                                 'width':'400px',
                                 'background-color' : '#ffffff',
                                'textAlign':'left',

                                
                                'padding': '10px',
                                 'margin-left': '15px',
                                 'margin-bottom': '10px'
                                 }))],
                                 
                                 style=
                                 {'maxWidth': '1100px','display': 'inline-block', 
                                 'verticalAlign': 'top',
                                'textAlign':'center',
                                'color':'#575757','font-family':'Segoe UI',
})
                                 ])

])



@app.callback(Output('3','figure'),[Input('10','value')])
def update_scatter(quarter):
    return scatter2(quarter,x,y1,y2)



if __name__ == '__main__' :
    app.run_server()
    
