import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# athelet = pd.read_csv('./data/athlete_events.csv')
# regions = pd.read_csv('./data/noc_regions.csv')

# athelet.head()
st.title("Olympics Analysis")

# def data_processor():
#     global athelet, regions
#     df = pd.merge(athelet , regions , on='NOC')
#     df.drop_duplicates(inplace=True)
#     df['Medal'].fillna('No_Medal',inplace=True)

#     summer = df[df['Season'] == 'Summer']
#     winter = df[df['Season'] == 'Winter']   
#     return summer , winter


# def duplicte_rows_remover(df1,df2):
#         df1 = df1.drop_duplicates(subset=['Team' , 'NOC', 'Games' , 'Year','City' ,'Sport' ,'Event'])
#         df2 = df2.drop_duplicates(subset=['Team' , 'NOC', 'Games' , 'Year','City' ,'Sport' ,'Event'])
#         return df1,df2



# def medal_tally_calculator(df):
      
#     medal_counts = df.groupby(["NOC", "Medal"]).size().reset_index(name='count')
    
#     medal_pivot = medal_counts.pivot(index='NOC', columns='Medal', values='count').fillna(0)
#     medal_pivot = medal_pivot.astype(int)


#     if "No_Medal" in medal_pivot.columns:
#         medal_pivot.drop(columns='No_Medal',inplace=True)
    
#     medal_pivot['Total_medal'] = medal_pivot[['Bronze' ,'Gold' , 'Silver']].sum(axis=1)

#     return medal_pivot
    

#     # medal_pivot_winter.sort_values(by=['Gold' , "Silver",'Bronze'] ,ascending=False).head(5)


# def fetch_noc(noc,pivot_table):
#     if noc in pivot_table.index:
#         details = {
#             "Gold":pivot_table.loc[noc,"Gold"],
#             "Sliver":pivot_table.loc[noc,"Silver"],
#             "Bronze":pivot_table.loc[noc,"Bronze"],
#             "Total Medal":pivot_table.loc[noc,"Total_medal"],


#         }
#         return details
#     else:
#         print("Not table Was given")





# summer , winter = data_processor()
# summer , winter = duplicte_rows_remover(summer,winter)



# st.sidebar.title("Menu")
# season = st.sidebar.radio("Choose The Season " , ['Summer' , "Winter"])
# options= st.sidebar.radio("options" , ('Medal-Tally' , 'Country-Wise') )


# #@ Medal-Tally 
# if season=="Summer"and options=="Medal-Tally":
#     st.header("Summer and Medal-Tally")
#     medal_pivot_summer = medal_tally_calculator(summer)
#     medal_pivot_summer = medal_pivot_summer.sort_values(by=['Gold' , "Silver",'Bronze'] ,ascending=False)
#     st.dataframe(medal_pivot_summer , width=800 , height=400)


# if season=="Winter"and options=="Medal-Tally":
#     st.header("Winter and Medal-Tally")
#     medal_pivot_summer = medal_tally_calculator(winter)
#     medal_pivot_summer = medal_pivot_summer.sort_values(by=['Gold' , "Silver",'Bronze'] ,ascending=False)
#     st.dataframe(medal_pivot_summer , width=800 , height=400)



# if season=="Summer"and options=="Country-Wise":
#     st.header("Summer and Country-Wise")
#     medal_pivot_summer = medal_tally_calculator(summer)

#     noc = st.selectbox("select noc" , medal_pivot_summer.index.to_list())
#     deatils = fetch_noc(noc , medal_pivot_summer)
#     st.dataframe(deatils , width=800 , height=400)


# if season=="Winter"and options=="Country-Wise":
#     st.header("Winter and Country-Wise")
#     medal_pivot_summer = medal_tally_calculator(winter)
#     noc = st.selectbox("select noc" , medal_pivot_summer.index.to_list())
#     deatils = fetch_noc(noc , medal_pivot_summer)
#     st.dataframe(deatils , width=800 , height=400)
