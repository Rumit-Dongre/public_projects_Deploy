import pandas as pd 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

athelet = pd.read_csv('./athlete_events.csv')
regions = pd.read_csv('./noc_regions.csv')

athelet.head()


def data_processor():
    global athelet, regions
    df = pd.merge(athelet , regions , on='NOC')
    df.drop_duplicates(inplace=True)
    df['Medal'].fillna('No_Medal',inplace=True)

    summer = df[df['Season'] == 'Summer']
    winter = df[df['Season'] == 'Winter']   
    return summer , winter


def duplicte_rows_remover(df1,df2):
        df1 = df1.drop_duplicates(subset=['Team' , 'NOC', 'Games' , 'Year','City' ,'Sport' ,'Event'])
        df2 = df2.drop_duplicates(subset=['Team' , 'NOC', 'Games' , 'Year','City' ,'Sport' ,'Event'])
        return df1,df2



def medal_tally_calculator(df):
      
    medal_counts = df.groupby(["NOC", "Medal"]).size().reset_index(name='count')
    
    medal_pivot = medal_counts.pivot(index='NOC', columns='Medal', values='count').fillna(0)
    medal_pivot = medal_pivot.astype(int)


    if "No_Medal" in medal_pivot.columns:
        medal_pivot.drop(columns='No_Medal',inplace=True)
    
    medal_pivot['Total_medal'] = medal_pivot[['Bronze' ,'Gold' , 'Silver']].sum(axis=1)

    return medal_pivot
    

    # medal_pivot_winter.sort_values(by=['Gold' , "Silver",'Bronze'] ,ascending=False).head(5)


def fetch_noc(noc,pivot_table):
    if noc in pivot_table.index:
        details = {
            "Gold":pivot_table.loc[noc,"Gold"],
            "Sliver":pivot_table.loc[noc,"Silver"],
            "Bronze":pivot_table.loc[noc,"Bronze"],
            "Total Medal":pivot_table.loc[noc,"Total_medal"],


        }
        return details
    else:
        print("Not table Was given")


