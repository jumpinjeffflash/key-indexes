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

### VISUAL: DAT National Spot Rates

    st.write("""## National Spot Rates: Van, Flatbed & Reefer""")
    st.write("""(DAT Freight data)""")
    st.image("https://i.ibb.co/w7gV2J4/dat-april-jul-2021.png", width=900)
    
### VISUAL: DOLLARS PER GALLON (DPG)    
    
    st.write("""## US Regular Conventional Gas Price: Dollars per Gallon""")
    
    st.write("""This is a weighted average based on a sample of approx. 900 retail outlets and is provided by the Energy Information Administration.""")    

    dpg_edit = dpg.rename(columns = {"Value":"Dollars per gallon"})

    st.line_chart(data = dpg_edit, width=0, height=0, use_container_width=True)
    
      ### More details available on this Gas Price index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Gas Price Index"):
        st.write("""The price represents self-service (unless only full-service is available) and includes all taxes. It comprises both conventional gasoline and reformulated gasoline.""")
    
### VISUAL: Cass Truckload Linehaul

    st.write("""## Cass Truckload Linehaul Index""")
    
    st.write("""This index tracks market fluctuations in per-mile truckload pricing. Data is derived from actual freight invoices paid on behalf of Cass' clients""")
    
    st.line_chart(data=cassctli, width=0, height=0, use_container_width=True)
    
    ### More details available on this Linehaul index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Linehaul Index"):
        st.write("""The Cass Truckload Linehaul Index® is a measure of market fluctuations in per-mile truckload linehaul rates, independent of additional cost components such as fuel and accessorials. Calculation methodology for the index was developed by the University of Tennessee’s Global Supply Chain Institute in collaboration with Cass.""")
        st.write("""Cass is the nation's largest payer of freight bills and manages more than $26 billion annually in freight spend. Its client base represents a broad sampling of industries including consumer packaged goods, food, automotive, chemical, medical/pharma, OEM, retail and heavy equipment. Annual freight volume per organization ranges from $40 million to over $2 billion.""")
    
    
### VISUAL: Cass Shipments Index
    
    st.write("""## Cass Expenditures & Shipments Index""")
    
    st.write("""The Expenditures Index (blue line) measures total dollars spent on freight transportation, including contract & spot market rates.""")
    st.write("""The Shipments Index (orange line) tracks the number of freight shipments across North America.""")

    st.line_chart(data=casscfi, width=0, height=0, use_container_width=True)
    
     ### More details available on this index via clicking the text expander:
    
    with st.beta_expander("Click here for more details:"):
        st.write("""The Cass expenditures index is a measure of the total dollars spent on freight (which is a function of both shipment volumes and rates).""")
        st.write("""Their Shipments Index is a measure of the number of intra-continental freight shipments across North America, for everything from raw materials to finished goods. All domestic modes are included, with truckload moves accounting for more than 50% of shipments and LTL accounting for ~25%.""")


##################################################### END OF CARRIER DASHBOARD #########################################
    
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
    st.write("""This index is based on a rotating panel survey with a nationally representative sample. The survey asks consumers about their views of their own personal finances, as well as the short-term and long-term state of the U.S. economy:""")
    
    umich_edit = umich.rename(columns = {"Index":"Sentiment"})
    st.line_chart(data = umich_edit, width=0, height=0, use_container_width=True)
    
### More details available on this survey via clicking the text expander:

    with st.beta_expander("Click here for more details about this Consumer Sentiment Index"):
        st.write("""Each survey contains ~50 core questions. The answers to these questions form the basis of the index, which is calculated by subtracting the percentage of unfavorable consumer replies from the percentage of favorable ones.""")
        st.write("""This indicator is important to retailers, economists, and investors, and its rise and fall has historically helped predict economic expansions and contractions.""")
      
### VISUAL: Misery Index     
    
    st.write("""## The Misery Index""")
    st.write("""Created by the economist Arthur Okun, this index adds the unemployment & inflation rates together. It makes me miserable just looking at it...""")
    
    miz = quandl.get("USMISERY/INDEX", start_date='2000-01-01')
    
    st.line_chart(data = miz, width=0, height=0, use_container_width=True)
    
    ### More details available on this misery index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Misery Index"):
        st.write("""The index helps determine how the average citizen is doing economically and it is calculated by adding the seasonally adjusted unemployment rate to the annual inflation rate.""") 
        st.write("""It is assumed that both a higher rate of unemployment and a worsening of inflation create economic and social costs for a country.""")

        
### VISUAL: Used Vehicle Salles  

    st.write("""## Used Vehicle Sales Index""")
    st.write("""This index tracks used vehicle sales. The data is supplied by the Bureau of Labor Statistics.""")

    fred = quandl.get("FRED/PCU441110441110102", start_date='2000-01-01')
    
    fred_edit = fred.rename(columns = {"Value":"Used Vehicle Index"})
    st.line_chart(data = fred_edit, width=0, height=0, use_container_width=True)
    
    ### More details available on this used vehicle index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Index"):
        st.write("""This index is comprised of used cars and trucks from 2 through 7 years of age.""")
        st.write("""Included cars consist of subcompact, compact or sporty, intermediate, full, luxury or status cars.""")
        st.write("""Included light trucks consist of pickup trucks, vans, and specialty vehicles. Specialty vehicles include sport/cross utility vehicles.""")
    
