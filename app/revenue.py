# -*- coding: utf-8 -*-
"""Company Revenue.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mp7rTwKI5Q28RTmRfqbSIzUnUwWQSx_d
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install yfinance==0.2.12 #install Yahoo Finance

import yfinance as yf

def get_revenue(ticker_symbol, years):
  ticker = yf.Ticker(ticker_symbol)
  financials = ticker.financials
  for year in years:
    try:
      revenue = financials.loc['Total Revenue', str(year)]
      formatted_revenue = "${:,.0f}".format(round(revenue.values[0])) # Format as currency
      print(f"Revenue for {year}: {formatted_revenue}")
    except:
      print(f"Revenue not found for {year}")

# Get input from the user
ticker_input = input("Enter the company's ticker symbol: ")
choice = input("Do you want to see revenue for (s)ingle year or (m)ultiple years? ")

if choice.lower() == 's':
  year_input = input("Enter the year: ")
  revenue = get_revenue(ticker_input, [year_input])
elif choice.lower() == 'm':
  num_years = int(input("Enter the number of years: "))
  years_to_print = []
  for i in range(num_years):
    year = input(f"Enter year {i+1}: ")
    years_to_print.append(year)
  get_revenue(ticker_input, years_to_print)
else:
  print("Invalid choice.")