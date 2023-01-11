import streamlit as st

#market_cap = int(input('Enter the marketcap: '))
#if marketcap less than 5000cr, then penalty

#sector = input('Select your sector: ')
#IT
#FMCG
#BANKING
#FINANCE
#PHARMA
#INFRA
#COMMODITY
#AUTO
#PSU
#Others

#15%
#pe = 
#median_pe = #10year 
#sector_pe = 
#pe_points = 15*(0.67(median_pe-pe) + 0.33(sector_pe-pe))

#30%
#sales = [] #year 
#sales_growth = [] #atleast 3 times in 10 years, also factor of marketcap
#profit = []
#profit_growth = [] #atleast 3 times
#ebita = []

sales_points = 7*((sales-sales2)/sales2)
if(sales_points>=30)
   {sales_points=30}

#20%
#promotor_holding = [] #year and >50% except banking
#institutional_holding = []
#public_holding = []
holding_points1 = 15*(0.55*(promotor_holding) + 0.3*(institutional_holding) + 0.15*(public_holding))
holding_points2 = 5*(100*(promotor_holding_change) + 100*(institutional_holding_change) - 100*(public_holding_change))

#20%
#roc = [] #Not for banks, min 15 
#roce = [] 
roc_points = 20*((roc*0.45 + roce*0.55 - 15))

#15%
#borrowings = [] #must be less than 10% of marketcap
#interest_payment = [] 
#9trade_receivables = []


pe = st.number_input("Enter the current P/E: ")
median_pe = st.number_input("Enter the median P/E of last 10 years: ")
sector_pe = st.number_input("Enter the current sector P/E: ")
pe_points = 15*(0.67(median_pe-pe) + 0.33(sector_pe-pe))

market_cap = st.number_input("Enter the current marketcap: ")
sector = st.number_input("Enter the sector: ")

sales = st.number_input("Enter the recent sales(in crores): ")
sales2 = st.number_input("Enter the sales 10 years ago: ")
profit = st.number_input("Enter the recent profit: ")
profit2 = st.number_input("Enter the 10 years ago profit: ")

roc = st.number_input("Enter th ROC: ")
roce = st.number_input("Enter the ROCE: ")
roc_points = 20*(0.6*(roce-10) + 0.4*(roc-10))

promotor_holding = st.number_input("Enter the current promoter holdings: ")
institutional_holding  = st.number_input("Enter the current institutional holding: ")
public_holding = 100 - promotor_holding - institutional_holding

st.write("P/E points(out of 20) are: ", pe_points)
st.write("Sales points(out of 35) are: ", sales_points)
st.write("roc points(out of 25) are: ", roc_points)
st.write("holding points(out of 20) are: ", hollding_points)

total_points = pe_points + sales_points + roc_points + holding_points
st.write("Total rating of the company is: ", total_points)









