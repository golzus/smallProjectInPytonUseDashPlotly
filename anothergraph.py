import dash  # ייבוא של ספריית Dash ליצירת אפליקציות רשת אינטראקטיביות
from dash import dcc, html  # ייבוא רכיבים ליצירת התוכן בדף (תפריטים, גרפים וכו')
from dash.dependencies import Input, Output  # ייבוא רכיבים ליצירת פונקציות callback
import pandas as pd  # ייבוא של pandas לעבודה עם קבצי נתונים
import graph  # ייבוא הפונקציות ליצירת גרפים (גרף עוגה)
import colorsChart as bar_graph  # ייבוא הפונקציות ליצירת גרפים (דיאגרמת מקלות)
import count_people_graph  # ייבוא הפונקציות ליצירת גרפים (גרף כמות אנשים)
import general_pie_chart  # ייבוא הפונקציות ליצירת גרף פאי כללי

# טעינת הנתונים מקובץ Excel
# file_path = 'C:\\Users\\goldi\\Practicum\\exelLoads.xlsx'
file_path='./exelsFiles/exelLoads.xlsx'
df = pd.read_excel(file_path)
column_names = df.columns[1:]  # שמירת שמות העמודות (למעט עמודת הזמן)

# bar_file_path = 'C:\\Users\\goldi\\Practicum\\exelLoasColorsPeople.xlsx'
bar_file_path='./exelsFiles/exelLoasColorsPeople.xlsx'
bar_df = pd.read_excel(bar_file_path)

count_people_file_path='./exelsFiles/exelCountPeople.xlsx'
# count_people_file_path = 'C:\\Users\\goldi\\Practicum\\exelCountPeople.xlsx'
count_people_df = pd.read_excel(count_people_file_path)

# general_pie_file_path = 'C:\\Users\\goldi\\Practicum\\exelCountGenerallyOfAllPeople.xlsx'
general_pie_file_path='./exelsFiles/exelCountGenerallyOfAllPeople.xlsx'
general_pie_df = pd.read_excel(general_pie_file_path)

# חישוב המדדים מהקובץ
total_people = count_people_df.iloc[0, 0]  # כמות האנשים סה"כ
avg_people = count_people_df.iloc[0, 1]  # ממוצע האנשים סה"כ
max_people_hour = count_people_df.iloc[0, 2]  # הכמות הכי גדולה בשעה

# יצירת האפליקציה של Dash
app = dash.Dash(__name__)

# הגדרת התצוגה של האפליקציה
app.layout = html.Div(
    className='main-container',  # מחלקה לתצוגה ראשית
    children=[
        html.Div(
            className='header-container',  # מחלקה לכותרת העליונה
            children=[
                html.Div(
                    className='metric-container',  # מחלקה לתצוגת מדד
                    children=[
                        html.Div('# of Visitors', className='metric-title'),  # כותרת מדד
                        html.Div(f'{total_people:.1f}k', className='metric-value')  # ערך המדד
                    ]
                ),
                html.Div(
                    className='metric-container',  # מחלקה לתצוגת מדד
                    children=[
                        html.Div('Avg Duration People', className='metric-title'),  # כותרת מדד
                        html.Div(f'{avg_people:.2f}', className='metric-value')  # ערך המדד
                    ]
                ),
                html.Div(
                    className='metric-container',  # מחלקה לתצוגת מדד
                    children=[
                        html.Div('Max Visitors/Hour', className='metric-title'),  # כותרת מדד
                        html.Div(f'{max_people_hour:.1f}k', className='metric-value')  # ערך המדד
                    ]
                ),
            ]
        ),
        html.Div(
            className='charts-container',  # מחלקה לתצוגת הגרפים
            children=[
                dcc.Graph(id='pie-selection', className='pie-chart'),  # גרף עוגה
                dcc.Graph(id='bar-chart', className='bar-chart'),  # דיאגרמת מקלות
                dcc.Graph(id='count-people-chart', className='count-people-chart')  # גרף כמות אנשים
            ]
        ),
        html.Div(
            className='general-pie-container',  # מחלקה לתצוגת גרף הפאי הכללי
            children=[
                dcc.Graph(id='general-pie-chart', className='general-pie-chart')  # גרף פאי כללי
            ]
        )
    ]
)


# פונקציית callback לעדכון הגרפים בהתבסס על הנתונים שנבחרו
@app.callback(
    [Output('pie-selection', 'figure'),
     Output('bar-chart', 'figure'),
     Output('count-people-chart', 'figure'),
     Output('general-pie-chart', 'figure')],
    [Input('pie-selection', 'clickData')]
)
def update_graphs(clickData):
    selected_categories = column_names.tolist()
    if clickData:
        selected_categories = [clickData['points'][0]['label']]

    pie_fig = graph.create_graph(selected_categories)  # יצירת גרף עוגה
    bar_fig = bar_graph.create_bar_chart(bar_df)  # יצירת דיאגרמת מקלות
    count_people_fig = count_people_graph.create_count_people_chart(count_people_df)  # יצירת גרף כמות אנשים
    general_pie_fig = general_pie_chart.create_general_pie_chart(general_pie_df)  # יצירת גרף פאי כללי
    return pie_fig, bar_fig, count_people_fig, general_pie_fig


# הרצת השרת
if __name__ == '__main__':
    app.run_server(debug=True)
