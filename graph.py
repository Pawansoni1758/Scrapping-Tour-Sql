import streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3

db = sqlite3.connect("data.db")
cursor = db.cursor()

cursor.execute("select date from temp")
date = cursor.fetchall()
date = [item[0] for item in date]


cursor.execute("select temperature from temp")
temp = cursor.fetchall()
date = [item[0] for item in date]

df = pd.read_csv("temp.txt")
figure = px.line(x=date, y=temp, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)
