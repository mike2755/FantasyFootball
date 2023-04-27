#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:44:50 2023

Caution: Program may take ~4 hours to complete

@author: mike2755
"""

import pandas as pd
import itertools
import time

start = time.time()

rb_df = pd.read_csv('https://raw.githubusercontent.com/mike2755/FantasyFootball/main/RB_adp_ppr.csv')
rb_df = rb_df.rename(columns={'Unnamed: 0':'Player'})
rb_df = rb_df[:40]

RBs = []
i = 0
while i < len(rb_df):
    RBs.append(rb_df['Player'][i])
    i+=1
rb_combos = list(itertools.combinations(RBs,5))
rb_df.set_index('Player', inplace=True)

rb_combo_df = pd.DataFrame(columns = ['RB1', 'RB2', 'RB3', 'RB4','RB5', 'Total'])
j=0
def RB_Calc(rb1,rb2,rb3,rb4,rb5):
    i = 0
    temp = []
    while i < 17:
        temp_rb = []
        RB1_score = rb_df.loc[rb1][i]
        RB2_score = rb_df.loc[rb2][i]
        RB3_score = rb_df.loc[rb3][i]
        RB4_score = rb_df.loc[rb4][i]
        RB5_score = rb_df.loc[rb5][i]
        temp_rb.append(RB1_score)
        temp_rb.append(RB2_score)
        temp_rb.append(RB3_score)
        temp_rb.append(RB4_score)
        temp_rb.append(RB5_score)
        temp_rb.sort(reverse=True)
        max_score = temp_rb[0]+temp_rb[1]
        temp.append(max_score)
        i+=1
    total = sum(temp)
    rb_combo_df.loc[j] = {'RB1':rb1, 'RB2':rb2, 'RB3':rb3, 'RB4':rb4, 'RB5':rb5, 'Total':total}
#RB_Calc('Austin Ekeler', 'Miles Sanders', 'Nick Chubb', 'Tony Pollard', 'Kenneth Walker')

while j < len(rb_combos):
    RB1 = rb_combos[j][0]
    RB2 = rb_combos[j][1]
    RB3 = rb_combos[j][2]
    RB4 = rb_combos[j][3]
    RB5 = rb_combos[j][4]
    #RB_Calc(RB1,RB2,RB3,RB4,RB5)
    j+=1
    
print('Time elapsed in seconds: ' + str((time.time()-start)))
