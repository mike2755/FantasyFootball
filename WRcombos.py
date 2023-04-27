#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:47:01 2023

@author: mpotterfield0089
"""

import pandas as pd
import itertools
import time

start = time.time()

wr_df = pd.read_csv('https://raw.githubusercontent.com/mike2755/FantasyFootball/main/WR_ppr_adp.csv')
wr_df = wr_df.rename(columns={'Unnamed: 0':'Player'})
wr_df = wr_df[:30]

WRs = []
i = 0
while i < len(wr_df):
    WRs.append(wr_df['Player'][i])
    i+=1

combos = list(itertools.combinations(WRs, 5))

wr_combo_df = pd.DataFrame(columns= ['WR1','WR2','WR3','WR4','WR5', 'Total'])

wr_df.set_index('Player', inplace= True)

def WR_Calc(wr1,wr2,wr3,wr4,wr5):
    i = 0
    temp = []
    while i < 17:
        temp_wr= []
        WR1_score = wr_df.loc[wr1][i]
        WR2_score = wr_df.loc[wr2][i]
        WR3_score = wr_df.loc[wr3][i]
        WR4_score = wr_df.loc[wr4][i]
        WR5_score = wr_df.loc[wr5][i]
        temp_wr.append(WR1_score)
        temp_wr.append(WR2_score)
        temp_wr.append(WR3_score)
        temp_wr.append(WR4_score)
        temp_wr.append(WR5_score)
        temp_wr.sort(reverse=True)
        max_score = temp_wr[0]+temp_wr[1]+temp_wr[2]
        temp.append(max_score)
        i +=1
    total = sum(temp)
    wr_combo_df.loc[j] = {'WR1':wr1, 'WR2':wr2,'WR3':wr3,'WR4':wr4,'WR5':wr5, 'Total':total}

j = 0
while j < len(combos):
    WR1 = combos[j][0]
    WR2 = combos[j][1]
    WR3 = combos[j][2]
    WR4 = combos[j][3]
    WR5 = combos[j][4]
    #print(WR1,WR2,WR3,WR4,WR5)
    WR_Calc(WR1,WR2,WR3,WR4,WR5)
    #print(wr_df.loc[WR1][3])
    j+=1

print("Time elapsed in seconds: " + str((time.time()-start)))
