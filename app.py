import dash
from dash import dcc, html
import dash_table
import plotly.express as px
import pandas as pd
from palmerpenguins import load_penguins

# Load the data
df = load_penguins()

# Create a simple plotly scatter plot
scatter_fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species",
                          title="Plotly Scatterplot - Bill Length vs Bill Depth")  # Add a title to the plot

# Create a simple plotly histogram
histogram_fig = px.histogram(df, x="bill_length_mm", color="species", 
                              title="Plotly Histogram - Bill Length Distribution")  # Add a title to the histogram

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    # Main Title
    html.H1("Elen's Palmer Penguin Dataset Exploration", style={'textAlign': 'center', 'marginTop': '20px'}),

    # Title for the Data Table
    html.H3("Data Table", style={'textAlign': 'center', 'marginTop': '40px'}),  # Title for the table
    
    # Data Table
    html.Div([
        dash_table.DataTable(
            id='penguin-table',
            columns=[
                {'name': col, 'id': col} for col in df.columns
            ],
            data=df.to_dict('records'),  # Convert dataframe to dictionary for the table
            style_table={'height': '300px', 'overflowY': 'auto'},  # Scrollable table
            style_cell={'textAlign': 'center', 'padding': '5px'},
        ),
    ], style={'padding': '20px'}),

    # Title for the Data Grid
    html.H3("Data Grid", style={'textAlign': 'center', 'marginTop': '40px'}),  # Title for the grid
    
    # Data Grid (same data table for this example)
    html.Div([
        dash_table.DataTable(
            id='penguin-grid',
            columns=[
                {'name': col, 'id': col} for col in df.columns
            ],
            data=df.to_dict('records'),
            style_table={'height': '300px', 'overflowY': 'auto'},
            style_cell={'textAlign': 'center', 'padding': '5px'},
        ),
    ], style={'padding': '20px'}),

    # Title for the Plotly Histogram
    html.H3("Plotly Histogram", style={'textAlign': 'center', 'marginTop': '40px'}),  # Title for the histogram
    
    # Plotly Histogram
    html.Div([
        dcc.Graph(
            id='histogram-plot',
            figure=histogram_fig  # Pass the histogram figure here
        )
    ], style={'padding': '20px'}),

    # Title for the Plotly Scatter Plot
    html.H3("Plotly Scatterplot", style={'textAlign': 'center', 'marginTop': '40px'}),  # Title for the scatter plot
    
    # Plotly Scatter Plot
    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure=scatter_fig  # Pass the scatter plot figure here
        )
    ], style={'padding': '20px'})
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)