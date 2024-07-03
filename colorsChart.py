import pandas as pd
import plotly.graph_objs as go

def create_bar_chart(df):
    colors = df.columns[0]
    categories = df.columns[1:]

    data = []
    for category in categories:
        trace = go.Bar(
            x=df[colors],
            y=df[category],
            name=category
        )
        data.append(trace)

    layout = go.Layout(
        barmode='stack',
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white')
    )

    fig = go.Figure(data=data, layout=layout)
    return fig
