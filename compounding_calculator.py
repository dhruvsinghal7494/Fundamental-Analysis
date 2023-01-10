import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import math
from sympy import symbols, Eq, solve

initial_amount = st.number_input('Enter initial amount: ', 1000)
return_rate = st.number_input('Enter return rate yearly: ', 1)
return_rate = return_rate/100
no_of_years = st.number_input('Enter no. of years: ', 1)
current_year = 2023

time_duration = st.number_input('Enter the time duration between in which you want to invest (12 for yearly and 1 for monthly): ', 1)

investment_amount = st.number_input('Enter the regualr investment amount: ')
return_rate = (return_rate* time_duration)/12
no_of_duration = no_of_years*12/time_duration

final_amount = investment_amount * (((1 + return_rate) ** (no_of_duration)) - 1) * (1 + return_rate)/return_rate
initial_amount2 = (final_amount * return_rate) / (((1+return_rate)**no_of_duration - 1)*(1 + return_rate))
no_of_duration = math.log10(((final_amount * return_rate)/(initial_amount * (1 + return_rate)))+1) / math.log10(1 + return_rate)

investment_amount2 = symbols('investment_amount')
return_rate2 = symbols('return_rate')
time_duration2 = symbols('time_duration')
no_of_years2 = symbols('no_of_years')
no_of_duration2 = symbols('no_of_duration')
final_amount2 = symbols('final_amount')
# st.write(type(investment_amount))
a = ((solve(Eq((investment_amount2 * (((1 + return_rate2) ** (no_of_duration2)) - 1) * (1 + return_rate2)/return_rate2), final_amount2))))
st.write(a[0])
print(a)
print(a[0])
st.write('The final amount is: ', final_amount)

year_array = []
final_amount_array = []

for i in range(no_of_years):
    year_array.append(i+1+current_year)
    final_amount_yearwise = investment_amount * (((1 + return_rate) ** (i*12/time_duration)) - 1) * (1 + return_rate)/return_rate
    final_amount_array.append(final_amount_yearwise)
    
fig = px.line(x=year_array, y=final_amount_array)
fig = go.Figure(data=go.Scatter(x=year_array, y=final_amount_array))
st.plotly_chart(fig)
#Add a graph of capital yearwise and also add slider
