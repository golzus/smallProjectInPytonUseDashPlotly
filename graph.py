import pandas as pd
import plotly.express as px

def create_graph(selected_categories):
    file_path = 'C:\\Users\\goldi\\Practicum\\exelLoads.xlsx'
    df = pd.read_excel(file_path)

    df_melted = df.melt(id_vars=[df.columns[0]], value_vars=selected_categories, var_name='category',
                        value_name='count')

    fig = px.scatter(df_melted, x="category", y="count", animation_frame=df.columns[0],
                     range_y=[0, df_melted['count'].max() + 5], size="count", size_max=30)

    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white')
    )

    fig.update_traces(marker=dict(color='pink'))

    return fig
