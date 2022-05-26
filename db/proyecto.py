import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from Conexion_Consulta import Connection
import proyectosql as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Cantidad de personas por tipo de poblacion
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cantidadPoblacion(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["poblacion", "cantidad"])
# Grafico de barra
poblacion_cantidad_bar = px.bar(dfCases.head(24), x="poblacion", y="cantidad")
# grafico de pie
poblacion_cantidad_pie = px.pie(dfCases.head(24), names="poblacion", values="cantidad")

# Cantidad de personas por meses
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cantidadMeses(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["mes", "cantidad"])
# Grafico de barra
mes_cantidad_bar = px.bar(dfCases.head(24), x="mes", y="cantidad")
# grafico de pie
mes_cantidad_pie = px.pie(dfCases.head(24), names="mes", values="cantidad")

# Deportes
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cantidadDeporte(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["deporte", "total"])
# Grafico de barra
deporte_bar = px.bar(dfCases.head(24), x="deporte", y="total")
# grafico de pie
deporte_pie = px.pie(dfCases.head(24), names="deporte", values="total")

# provincia
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cantidadProvincia(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["nombre", "sum"])
# Grafico de barra
provincia_bar = px.bar(dfCases.head(24), x="nombre", y="sum")
# Grafico de pie
provincia_pie = px.pie(dfCases.head(24), names="nombre", values="sum")

# Programa 1
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cantidadProg1(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["mes", "cantidad"])
# Grafico de barra
prog1_bar = px.bar(dfCases.head(24), x="mes", y="cantidad")

# Programa 2
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cantidadProg2(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["mes", "cantidad"])
# Grafico de barra
prog2_bar = px.bar(dfCases.head(24), x="mes", y="cantidad")

# Programa 3
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.cantidadProg3(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["mes", "cantidad"])
# Grafico de barra
prog3_bar = px.bar(dfCases.head(24), x="mes", y="cantidad")

# Layout
app.layout = html.Div(children=[
    html.H1(children='  ', style={'text-align': 'center'}),
    html.H1(children='DASHBOARD - Observatorio plan de desarrollo', style={'padding-top': '50px','padding-bottom': '50px','text-align':'center'}),
    # html.H3(children='Por tipo de poblacion'),
    dcc.Graph(
        id='BarMeses',
        figure=mes_cantidad_bar
    ),
    html.Div(className="row", children=[
            # Col for vertical bars
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Tipo de poblaciòn'),
                    ]),
                    html.Div(className="Before Covid", children=[
                        html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                        dcc.Graph(
                            id='BarPoblacion',
                            figure=poblacion_cantidad_bar
                        ),
                        html.H6(children='Gráfico Circular',style={'text-align': 'center'}),
                        dcc.Graph(
                            id='PiePoblacion',
                            figure=poblacion_cantidad_pie
                        ),
                    ]),
                ]),
            ]),
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Poblacion por mes'),
                    ]),
                    html.Div(className="During Covid", children=[
                        html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                        dcc.Graph(
                            id='BarProv',
                            figure=provincia_bar
                        ),
                        html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                        dcc.Graph(
                            id='PieProv',
                            figure=provincia_pie
                        ),
                    ]),
                ]),
            ]),
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Por deporte'),
                    ]),
                    html.Div(className="After Covid", children=[
                        html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                        dcc.Graph(
                            id='BarDeportes',
                            figure=deporte_bar
                        ),
                        html.H6(children='Gráfico Circular', style={'text-align': 'center'}),
                        dcc.Graph(
                            id='PieDeportes',
                            figure=deporte_pie
                        ),
                    ]),
                ]),
            ]),
        ],style={'padding-left': '30px',   'padding-right': '30px', 'padding-bottom': '30px'}),
    html.Div(className="row", children=[
            # Col for vertical bars
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Programa CREEMOS FOMENTO Y PROMOCIÓN DEL DEPORTE, ACTIVIDAD FÍSICA Y RECREACIÓN PARA LA CONSTRUCCIÓN DE LA PAZ'),
                    ]),
                    html.Div(className="Before Covid", children=[
                        html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                        dcc.Graph(
                            id='BarProg1',
                            figure=prog1_bar
                        ),
                    ]),
                ]),
            ]),
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Programa CREEMOS EN BOYACA RAZA DE CAMPEONES'),
                    ]),
                    html.Div(className="During Covid", children=[
                        html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                        dcc.Graph(
                            id='BarProg2',
                            figure=prog2_bar
                        ),
                    ]),
                ]),
            ]),
            html.Div(className="col-10 col-xl-4", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header", children=[
                        html.H5(children='Programa GESTIÓN DEL CONOCIMIENTO'),
                    ]),
                    html.Div(className="After Covid", children=[
                        html.H6(children='Gráfico de Barras', style={'text-align': 'center', 'padding-top': '10px'}),
                        dcc.Graph(
                            id='BarProg3',
                            figure=prog3_bar
                        ),
                    ]),
                ]),
            ]),
        ],style={'padding-left': '30px',   'padding-right': '30px', 'padding-bottom': '30px'}),
])



if __name__ == '__main__':
    app.run_server(debug=True)
