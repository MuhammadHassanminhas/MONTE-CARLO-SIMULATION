import streamlit as slt
import pandas as pd
import data
import time
import matplotlib.pyplot as mlt
import events

col1, col2, col3 = slt.columns([1, 3, 1])

col2.title(":red[MONTE CARLO SIMULATION]")


price = slt.number_input("#### ENTER THE PRICE YOU WANT TO SIMULATE IN MONTE CARLO SIMULATION ")
col1 , col2 , col3 , col4 , col5 = slt.columns(5)
min_percent=col1.slider("#### SLIDE TO CHOSE :red[MAXIMUM] PERCENTAGE(%)" , min_value = - 0.00 , max_value= - 100.00 )

max_percent=col3.slider("#### SLIDE TO CHOSE :red[MINIMUM] PERCENTAGE(%)" , min_value = 0.00 , max_value=100.00 )
issues = col5.multiselect('#### SELECT ANY :red[GLOGAL CRISES] TO SEE THE IMPACT ON THE SIMULATION',['Dot-com bubble burst (2000-2002)','September 11th attacks (2001)' , 'Enron scandal (2001)','Iraq War (2003-2011)','Subprime mortgage crisis', 'Great Recession (2007-2009)','European sovereign debt crisis (2010-2012)','COVID-19 pandemic (2020-present)'])
result = events.cases(issues)
with slt.spinner(text='SIMULATION UNDER PROCESS'):
    time.sleep(3)
    slt.success('COMPLETE')
data_year = data.YEAR(min_percent , max_percent , price,result)
data_half_decade = data.HALF_DECADE(min_percent , max_percent , price,result)
data_months = data.MONTHS(min_percent , max_percent , price,result)
data_day = data.DAY(min_percent , max_percent , price,result)

day_col , month_col = slt.columns(2)
day_col.write("### SIMULATION FOR ONE :red[DAY]")
day_col.line_chart(data_day)
month_col.write("### SIMULATION FOR :red[MONTHS]")

month_col.line_chart(data_months)


year_col , half_decade_col = slt.columns(2)
year_col.write("### SIMULATION FOR ONE :red[YEAR]")

year_col.line_chart(data_year)
half_decade_col.write("### SIMULATION FOR HALF :red[DECADE]")

half_decade_col.line_chart(data_half_decade)


