import pandas as pd
import plotly.graph_objs as go

def create_general_pie_chart(df):
    # יצירת גרף פאי עם הנתונים מהטבלה
    labels = df.columns  # שמות העמודות
    values = df.iloc[0]  # ערכים בשורה הראשונה

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

    # הגדרת תצוגת הגרף
    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white')
    )

    return fig
