import streamlit as st

import pandas as pd

import quandl
quandl.ApiConfig.api_key = "39zaQuPVuxqWNiZ_gzpV"

option = st.sidebar.selectbox("Please make your selection:", ('Carrier dashboard', 'Shipper dashboard'), 0)

### CARRIER DASHBOARD ###

if option == 'Carrier dashboard':
    
    st.write("# Key Indexes for Carriers")
    st.write("## Summary:")
    st.write("""The cost of transporation continues to rise. The indexes below are all trending up and to the right, suggesting that it will take a while before expenses start to cool off.""")
    
### This fetches all the Quandl data    
    
## Dollars per gallon
    dpg = quandl.get("FRED/GASREGCOVW", start_date='2000-01-01')
## CASS Shipments Index
    casscfi = quandl.get('CASS/CFI', start_date='2000-01-01')
## CASS Truckload Linehaul Index
    cassctli = quandl.get("CASS/CTLI")


### VISUAL: DOLLARS PER GALLON (DPG)    
    
    st.write("""## US Regular Conventional Gas Price: Dollars per Gallon""")
    
    st.write("""This is a weighted average based on a sample of approx. 900 retail outlets and is provided by the Energy Information Administration.""")    

    dpg_edit = dpg.rename(columns = {"Value":"Dollars per gallon"})

    st.line_chart(data = dpg_edit, width=0, height=0, use_container_width=True)
    
    
### VISUAL: Cass Truckload Linehaul

    st.write("""## Cass Truckload Linehaul Index""")
    
    st.write("""This index tracks market fluctuations in per-mile truckload pricing. Data is derived from actual freight invoices paid on behalf of Cass' clients""")
    
    st.line_chart(data=cassctli, width=0, height=0, use_container_width=True)    
    
    
### VISUAL: Cass Shipments Index
    
    st.write("""## Cass Expenditures & Shipments Index""")
    
    st.write("""The Expenditures Index (blue line) measures total dollars spent on freight transportation, including contract & spot market rates.""")
    st.write("""The Shipments Index (orange line) tracks the number of freight shipments across North America.""")

    st.line_chart(data=casscfi, width=0, height=0, use_container_width=True)
    
    
### SHIPPER DASHBOARD ###
    
    
if option == 'Shipper dashboard':
    
    st.write("# Key Indexes for Shippers")
    st.write("## Summary:")
    st.write("""Consumers aren't as confident as they were pre-pandemic, but their optimism is gradually improving. Used vehicle sales are close to their peak of mid-2007, which creates transporation opportunities.""")

### This fetches all the Quandl data

## University of Michigan consumer sentiment (US)
    umich = quandl.get("UMICH/SOC1", start_date='2000-01-01')
## Misery Index   
    miz   = quandl.get("USMISERY/INDEX", start_date='2000-01-01')
## Used car prices (US) 
    fred  = quandl.get("FRED/PCU441110441110102", start_date='2000-01-01')

### VISUAL: University of Michigan consumer sentiment (US)

    st.write("""## University of Michigan's Consumer Sentiment Index""")
    st.write("""This index is based on a rotating panel survey with a nationally representative sample.""")
    
    umich_edit = umich.rename(columns = {"Index":"Sentiment"})
    st.line_chart(data = umich_edit, width=0, height=0, use_container_width=True)
      
### VISUAL: Misery Index     
    
    st.write("""## The Misery Index""")
    st.write("""Created by the economist Arthur Okun, this index adds the unemployment & inflation rates together. It makes me miserable just looking at it...""")
    
    miz = quandl.get("USMISERY/INDEX", start_date='2000-01-01')
    
    st.line_chart(data = miz, width=0, height=0, use_container_width=True)
        
### VISUAL: Used Vehicle Salles  

    st.write("""## Used Vehicle Sales Index""")
    st.write("""This index tracks used vehicle sales. The data is supplied by the Bureau of Labor Statistics.""")

    fred = quandl.get("FRED/PCU441110441110102", start_date='2000-01-01')
    
    fred_edit = fred.rename(columns = {"Value":"Used Vehicle Index"})
    st.line_chart(data = fred_edit, width=0, height=0, use_container_width=True)    
    
    
