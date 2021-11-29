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
## CASS Shipments Index - commenting out because they don't update any more
#    casscfi = quandl.get('CASS/CFI', start_date='2000-01-01')
## CASS Truckload Linehaul Index - commenting out because they don't update any more
#    cassctli = quandl.get("CASS/CTLI")
## Big Mac Index
    mac = quandl.get("ECONOMIST/BIGMAC_USA", qopts={"columns":"local_price"})


### LOGO & Links: DAT National Spot Rates

    st.write("""## Flatbed Rates""")
    st.image("https://www.dat.com/wp-content/uploads/2020/11/dat_logo_dat_f_a_vertical_digital_blue.279x0-is-hidpi.png", width=85)
    st.write("Click here for Flatbed Demand & Capacity: [link](https://www.dat.com/industry-trends/trendlines/flatbed/demand-and-capacity)")
    st.write("Click here for National Flatbed Rates: [link](https://www.dat.com/industry-trends/trendlines/flatbed/national-rates)")

### VISUAL: DOLLARS PER GALLON (DPG)    
    
    st.write("""## US Regular Conventional Gas Price: Dollars per Gallon""")
    
    st.write("""This is a weighted average based on a sample of approx. 900 retail outlets and is provided by the Energy Information Administration.""")    

    dpg_edit = dpg.rename(columns = {"Value":"$ per gallon"})

    st.line_chart(data = dpg_edit, width=0, height=0, use_container_width=True)
    
      ### More details available on this Gas Price index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Gas Price Index"):
        st.write("""The price represents self-service (unless only full-service is available) and includes all taxes. It comprises both conventional gasoline and reformulated gasoline.""")
    
### VISUAL: Cass Truckload Linehaul - using their website URL because they're not updating QUANDL any more...

    st.write("""## Cass Truckload Linehaul Index""")
    
    st.write("""This index tracks market fluctuations in per-mile truckload pricing. Data is derived from actual freight invoices paid on  behalf of Cass' clients""")
    
    st.image('https://www.cassinfo.com/hs-fs/hubfs/Freight%20Payment%20/Transportation%20Indexes/Indexes%202021/October%202021/Cass%20TL%20LH%20Index%20Oct%202021.png?width=1031&name=Cass%20TL%20LH%20Index%20Oct%202021.png', width=675)
    
    
#    st.line_chart(data=cassctli, width=0, height=0, use_container_width=True)
    
    ### More details available on this Linehaul index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Linehaul Index"):
        st.write("""The Cass Truckload Linehaul Index® is a measure of market fluctuations in per-mile truckload linehaul rates, independent of additional cost components such as fuel and accessorials. Calculation methodology for the index was developed by the University of Tennessee’s Global Supply Chain Institute in collaboration with Cass.""")
        st.write("""Cass is the nation's largest payer of freight bills and manages more than $26 billion annually in freight spend. Its client base represents a broad sampling of industries including consumer packaged goods, food, automotive, chemical, medical/pharma, OEM, retail and heavy equipment. Annual freight volume per organization ranges from $40 million to over $2 billion.""")
    
    
### VISUAL: Cass Shipments Index commenting out because it doesn't update regularly any more
    
#    st.write("""## Cass Expenditures & Shipments Index""")
    
#    st.write("""The Expenditures Index (blue line) measures total dollars spent on freight transportation, including contract & spot #market rates.""")
#    st.write("""The Shipments Index (orange line) tracks the number of freight shipments across North America.""")

#    st.line_chart(data=casscfi, width=0, height=0, use_container_width=True)
    
#     ### More details available on this index via clicking the text expander:
    
#    with st.beta_expander("Click here for more details:"):
#        st.write("""The Cass expenditures index is a measure of the total dollars spent on freight (which is a function of both shipment #volumes and rates).""")
#        st.write("""Their Shipments Index is a measure of the number of intra-continental freight shipments across North America, for #everything from raw materials to finished goods. All domestic modes are included, with truckload moves accounting for more than 50% of #shipments and LTL accounting for ~25%.""")


### VISUAL: BIG MAC INDEX    
    
    st.write("""## The Big Mac Index (USA)""")
    
    st.write("""This index tracks the cost of purchasing a Bic Mac (in US Dollars) over time.""")    

    dpg_edit = dpg.rename(columns = {"Value":"Big Mac price ($)"})

    st.line_chart(data = dpg_edit, width=0, height=0, use_container_width=True)
    
      ### More details available on this Gas Price index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Big Mac Index"):
        st.write("""Collected by The Economist magazine since 1986, this data shows the cost of a Big Mac (in US Dollars) over time to gauge purchasing power. It's also used as an informal measure of currency exchange rates.""") 
        st.write("""It measures the currency's value against a similar basket of goods and services, in this case a Big Mac. Differing prices at market exchange rates would imply that one currency is under or overvalued versus another.""")


##################################################### END OF CARRIER DASHBOARD #########################################
    
### SHIPPER DASHBOARD ###
    
    
if option == 'Shipper dashboard':
    
    st.write("# Key Indexes for Shippers")
    st.write("## Summary:")
    st.write("""Consumers aren't as confident as they were pre-pandemic. The Consumer Prices Index is at its highest for many decades. Used vehicle sales are also at all-time highs, which creates transporation opportunities.""")

### This fetches all the Quandl data

## University of Michigan consumer sentiment (US)
    umich = quandl.get("UMICH/SOC1", start_date='2000-01-01')

## Misery Index - unavilable on Quandl right now, so I'm commenting it out:
#    miz   = quandl.get("USMISERY/INDEX", start_date='2000-01-01')

## USA Consumer Price Index
    cons = quandl.get("RATEINF/CPI_USA", start_date='2000-01-01')

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
      
### VISUAL: Misery Index - this doesn't exist any more on Quandl, so I've commented it all out:     
    
#    st.write("""## The Misery Index""")
#    st.write("""Created by the economist Arthur Okun, this index adds the unemployment & inflation rates together. It makes me miserable just looking at it...""")
    
#    miz = quandl.get("USMISERY/INDEX", start_date='2000-01-01')
    
#    st.line_chart(data = miz, width=0, height=0, use_container_width=True)
    
#    ### More details available on this misery index via clicking the text expander:

#    with st.beta_expander("Click here for more details about this Misery Index"):
#        st.write("""The index helps determine how the average citizen is doing economically and it is calculated by adding the seasonally # adjusted unemployment rate to the annual inflation rate.""") 
#        st.write("""It is assumed that both a higher rate of unemployment and a worsening of inflation create economic and social costs  #for a country.""")


### VISUAL: USA Consumer Prices

    st.write("""## USA Consumer Prices Index""")
    st.write("""This measures the price of a selection of goods and services for a typical consumer. The data is supplied by the Bureau of Labor Statistics.""")
    
    cons = cons.rename(columns = {"Value":"Consumer Prices"})
    st.line_chart(data = cons, width=0, height=0, use_container_width=True)
    
    ### More details available on this used vehicle index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Consumer Prices Index"):
        st.write("""The Consumer Price Index (CPI) is a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services.""")
        st.write("""It is the most widely used measure of inflation and is sometimes viewed as an indicator of the effectiveness of government economic policy. It provides information about price changes in the Nation's economy to government, business, labor, and private citizens and is used by them as a guide to making economic decisions.""")
        st.write("""Additionally, the President, Congress, and the Federal Reserve Board use trends in the CPI to aid in formulating fiscal and monetary policies.""")

        
### VISUAL: Used Vehicle Sales  

    st.write("""## Used Vehicle Sales Index""")
    st.write("""This index tracks used vehicle sales. The data is also supplied by the Bureau of Labor Statistics.""")
    
    fred_edit = fred.rename(columns = {"Value":"Used Vehicle Index"})
    st.line_chart(data = fred_edit, width=0, height=0, use_container_width=True)
    
    ### More details available on this used vehicle index via clicking the text expander:

    with st.beta_expander("Click here for more details about this Index"):
        st.write("""This index is comprised of used cars and trucks from 2 through 7 years of age.""")
        st.write("""Included cars consist of subcompact, compact or sporty, intermediate, full, luxury or status cars.""")
        st.write("""Included light trucks consist of pickup trucks, vans, and specialty vehicles. Specialty vehicles include sport/cross utility vehicles.""")
    