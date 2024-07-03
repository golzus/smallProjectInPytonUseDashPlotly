# ייבוא המודולים הדרושים
import pandas as pd  # ייבוא ספריית pandas לעבודה עם נתונים
import dash  # ייבוא ספריית dash ליצירת ממשק ויזואלי
from dash import dcc, html  # ייבוא רכיבי הליבה של dash
from dash.dependencies import Input, Output  # ייבוא רכיבי התלות לעדכון הגרף בזמן אמת
import plotly.express as px  # ייבוא ספריית plotly express ליצירת גרפים בצורה פשוטה

# קביעת הנתיב לקובץ ה-Excel
file_path = 'C:\\Users\\goldi\\Documents\\dataLoadsPeople.xlsx'
# קריאת הקובץ עם שימוש בשורה הראשונה ככותרת והעמודה הראשונה ככותרת השורות
df = pd.read_excel(file_path, header=0, index_col=0)

# המרת האינדקס לטיפוס מחרוזת כדי להבטיח תאימות מלאה
df.index = df.index.astype(str)

# הצגת מספר השורות ב-DataFrame כדי לבדוק את התוצאה
print("Number of rows in the DataFrame:", df.shape[0])
# הצגת חמשת השורות הראשונות ב-DataFrame (ניתן לשנות את המספר אם רוצים לראות יותר או פחות שורות)
print(df.head())

# יצירת אפליקציית Dash
app = dash.Dash(__name__)

# הגדרת מבנה האפליקציה
app.layout = html.Div([
    html.H1("The graphs of the number of people on the road"),  # כותרת האפליקציה
    dcc.Dropdown(  # תיבת בחירה לבחירת סוג הגרף
        id='chart-type',
        options=[
            {'label': 'Line Chart', 'value': 'line'},  # אפשרות לבחירת גרף קו
            {'label': 'Pie Chart', 'value': 'pie'}  # אפשרות לבחירת דיאגרמת עוגה
        ],
        value='line'  # ערך ברירת המחדל הוא גרף קו
    ),
    dcc.Dropdown(  # תיבת בחירה לבחירת השעה להצגה בגרף
        id='hour-selector',
        options=[{'label': hour, 'value': hour} for hour in df.index],  # יצירת רשימת אפשרויות מהשעות ב-DataFrame
        value=df.index[0]  # ערך ברירת המחדל הוא השעה הראשונה ב-DataFrame
    ),
    dcc.Graph(id='graph'),  # רכיב הגרף להצגת הגרפים שנבחרו
])

# פונקציה ליצירת גרף הקו
def create_line_chart():
    # יצירת גרף קו עם plotly express
    fig_line = px.line(df, x=df.index, y=df.columns, title='Line Chart of People on the Road')
    return fig_line

# פונקציה ליצירת דיאגרמת עוגה
def create_pie_chart(selected_hour):
    # יצירת דיאגרמת עוגה עם plotly express
    fig_pie = px.pie(names=df.columns, values=df.loc[selected_hour], title=f'Pie Chart of People at {selected_hour}')
    return fig_pie

# עדכון הגרף באפליקציה
@app.callback(
    Output('graph', 'figure'),  # פלט הפונקציה הוא רכיב הגרף
    [Input('chart-type', 'value'), Input('hour-selector', 'value')]  # הפונקציה מקבלת את סוג הגרף והשעה שנבחרו כקלט
)
def update_graph(graph_type, selected_hour):
    # בדיקה איזה סוג גרף נבחר
    if graph_type == 'line':
        return create_line_chart()  # החזרת גרף קו
    elif graph_type == 'pie':
        return create_pie_chart(selected_hour)  # החזרת דיאגרמת עוגה
    else:
        # ניתן להוסיף טיפול נוסף לסוגי גרפים נוספים כפי שנדרש
        return {}

# הרצת האפליקציה
if __name__ == '__main__':
    app.run_server(debug=True)  # הפעלת שרת ה-Dash במצב דיבוג


