
import pandas as pd 
import dash  
from dash import dcc
from dash import html
from dash import dash_table as dt

df=pd.read_excel("MBA_data_1.xlsx")
app=dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1(children="Market-basket analysis and prediction",
        style={
            'textAlign': 'center',
            'color': "red"
        }),
    html.Div(children="Using Associative Data Mining and Apriori Algorithm",
            style={
                "textAlign":"center",
                "color":"red"
            }),
    html.Br(),
    html.Br(),
    html.Div([
        dcc.Textarea(
        id='textarea-state-example',
        value='Market basket analysis can increase sales and customer satisfaction\nUsing data to determine that products are often purchased together, retailers can optimize product placement, offer special deals and create new product bundles to encourage further sales of these combinations.\n\nThese improvements can generate additional sales for the retailer, while making the shopping experience more productive and valuable for customers. By using market basket analysis, customers may feel a stronger sentiment or brand loyalty toward the company.',
           style=
               {'width': '60%', 'height': 200}
            ),
    ]),
    html.Br(),
    html.Br(),
            dt.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)
])
         
  if __name__ == '__main__':
    app.run_server(debug=True)
