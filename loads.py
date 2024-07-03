import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# קריאת קובץ ה-Excel
file_path = 'C:\\Users\\goldi\\Practicum\\exelLoads.xlsx'
df = pd.read_excel(file_path)

# הצגת שמות העמודות כדי לוודא את המבנה
print(df.columns)

# המרת עמודת השעה ל-DataFrame שמתאים לפלוטלי
df_melted = df.melt(id_vars=[df.columns[0]], value_vars=[df.columns[1], df.columns[2], df.columns[3], df.columns[4], df.columns[5], df.columns[6], df.columns[7]], var_name='category', value_name='count')

# יצירת גרף נקודות עם אנימציה
fig_loads = px.scatter(df_melted, x="category", y="count", animation_frame=df.columns[0], color="category",
                       range_y=[0, df_melted['count'].max() + 5], title="Number of Women, Men, and Children Over Time",
                       size="count", size_max=30)

# הצגת הגרף - לא נדרש באפליקציה Dash
# fig_loads.show()
