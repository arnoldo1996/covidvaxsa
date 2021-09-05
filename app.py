import streamlit as st
import altair as alt
import pandas as pd

#Chart heading
st.title('Covid Vaccination Rollout over time in South Africa')

# Source file
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/South%20Africa.csv"

df = pd.read_csv(url)

# Create Altair chart
cv19 = alt.Chart(df).mark_bar().encode(
    x='date', y='people_vaccinated',color = 'people_fully_vaccinated',
    tooltip=['date', 'people_vaccinated','people_fully_vaccinated']).interactive().properties(
    width=1500,
    height=650
).configure_axis(
    labelFontSize=20,
    titleFontSize=20
)

#Display chart
st.write(cv19)
