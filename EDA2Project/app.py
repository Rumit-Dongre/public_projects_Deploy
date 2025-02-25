import streamlit as st
import pandas as pd 
from helpers import * 


summer , winter = data_processor()
summer , winter = duplicte_rows_remover(summer,winter)



st.sidebar.title("Menu")
season = st.sidebar.radio("Choose The Season " , ['Summer' , "Winter"])
options= st.sidebar.radio("options" , ('Medal-Tally' , 'Country-Wise') )


#@ Medal-Tally 
if season=="Summer"and options=="Medal-Tally":
    st.header("Summer and Medal-Tally")
    medal_pivot_summer = medal_tally_calculator(summer)
    medal_pivot_summer = medal_pivot_summer.sort_values(by=['Gold' , "Silver",'Bronze'] ,ascending=False)
    st.dataframe(medal_pivot_summer , width=800 , height=400)


if season=="Winter"and options=="Medal-Tally":
    st.header("Winter and Medal-Tally")
    medal_pivot_summer = medal_tally_calculator(winter)
    medal_pivot_summer = medal_pivot_summer.sort_values(by=['Gold' , "Silver",'Bronze'] ,ascending=False)
    st.dataframe(medal_pivot_summer , width=800 , height=400)



if season=="Summer"and options=="Country-Wise":
    st.header("Summer and Country-Wise")
    medal_pivot_summer = medal_tally_calculator(summer)

    noc = st.selectbox("select noc" , medal_pivot_summer.index.to_list())
    deatils = fetch_noc(noc , medal_pivot_summer)
    st.dataframe(deatils , width=800 , height=400)


if season=="Winter"and options=="Country-Wise":
    st.header("Winter and Country-Wise")
    medal_pivot_summer = medal_tally_calculator(winter)
    noc = st.selectbox("select noc" , medal_pivot_summer.index.to_list())
    deatils = fetch_noc(noc , medal_pivot_summer)
    st.dataframe(deatils , width=800 , height=400)
