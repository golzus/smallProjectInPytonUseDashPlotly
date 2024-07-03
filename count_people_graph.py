import pandas as pd
import plotly.graph_objs as go

def create_count_people_chart(df):
    categories = df.columns

    data = []
    for category in categories:
        trace = go.Bar(
            x=[category],
            y=[df[category].sum()],
            name=category
        )
        data.append(trace)

    layout = go.Layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white')
    )

    fig = go.Figure(data=data, layout=layout)
    return fig
