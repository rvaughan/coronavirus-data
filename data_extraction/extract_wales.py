import pandas as pd

rf = pd.read_excel('../uk/wales/Rapid COVID-19 surveillance data.xlsx', sheet_name='Tests by specimen date')
rf.to_csv('../data/uk/wales/tests.csv')

rf = pd.read_excel('../uk/wales/Rapid COVID-19 surveillance data.xlsx', sheet_name='Cases by MSOA')
rf.to_csv('../data/uk/wales/7_day_averages.csv')

rf = pd.read_excel('../uk/wales/Rapid COVID-19 surveillance data.xlsx', sheet_name='Age and sex distribution')
rf.to_csv('../data/uk/wales/sex.csv')

rf = pd.read_excel('../uk/wales/Rapid COVID-19 surveillance data.xlsx', sheet_name='Deaths by date')
rf.to_csv('../data/uk/wales/deaths.csv')

rf = pd.read_excel('../uk/wales/Rapid COVID-19 surveillance data.xlsx', sheet_name='Deaths by LHB')
rf.to_csv('../data/uk/wales/deaths_by_LHB.csv')
