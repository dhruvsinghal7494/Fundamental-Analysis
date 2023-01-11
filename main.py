import streamlit as st
import plotly_exppress as px

market_cap = int(input('Enter the marketcap: '))
#if marketcap less than 5000cr, then penalty

sector = input('Select your sector: ')
IT
FMCG
BANKING
FINANCE
PHARMA
INFRA
COMMODITY
AUTO
PSU
Others

#15%
pe = 
median_pe = #10year 
sector_pe = 
pe_points = 15*(0.67(median_pe/pe) + 0.33(sector_pe/pe))

#30%
sales = [] #year 
sales_growth = [] #atleast 3 times in 10 years, also factor of marketcap
profit = []
profit_growth = [] #atleast 3 times
ebita = []
sales_points = 30*(())


#20%
promotor_holding = [] #year and >50% except banking
institutional_holding = []
public_holding = []
holding_points1 = 15*(0.55*(promotor_holding) + 0.3*(institutional_holding) + 0.15*(public_holding))
holding_points2 = 5*(100*(promotor_holding_change) + 100*(institutional_holding_change) - 100*(public_holding_change))

#20%
roc = [] #Not for banks, min 15 
roce = [] 
roc_points = 20*((roc*0.45 + roce*0.55 - 15))

#15%
borrowings = [] #must be less than 10% of marketcap
interest_payment = [] 
trade_receivables = []


pe = st.number_input("Enter the current P/E: ")
median_pe = st.number_input("Enter the median P/E of last 10 years: ")
sector_pe = st.number_input("Enter the current sector P/E: ")

market_cap = st.number_input("Enter the current marketcap: ")
sector = st.number_input("Enter the sector: ")

sales = st.number_input("Enter the recent sales(in crores): ")
sales2 = st.number_input("Enter the sales 10 years ago: ")
profit = st.number_input("Enter the recent profit: ")
profit2 = st.number("Enter the 10 years ago profit: ")

roc = st.number_input("Enter th ROC: ")
roce = st.number_input("Enter the ROCE: ")

promotor_holding = st.number_input("Enter the current promoter holdings: ")
institutional_holding  = st.number_input("Enter the current institutional holding: ")
public_holding = 100 - promotor_holding - institutional_holding












