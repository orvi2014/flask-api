import os
import json
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

import pandas as pd
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
def stdd(txt):
    stop_wd = [' ', '-', '/']
    for sw in stop_wd:
        txt = ''.join(txt.split(sw))
    return txt.lower()

def main(mycols, dct_filter, df_org,n):
    ### check input ###
    if len(dct_filter['skills'])>1:
        if dct_filter['skills_andor'] not in ['all', 'any']:
            return "key skills_andor should have value of either 'all' or 'any'"
    
    df_onboard = df_org.copy()
    print(df_onboard)
    df_onboard['professions'] = df_onboard['professions'].apply(eval)
    
    ##########################################################################################################
    for k in dct_filter.keys():
        if type(dct_filter[k]) is str:
            dct_filter[k] = dct_filter[k].split(',')
        if k=='skills':
            df_onboard[k] = df_onboard[k].astype(str)
            if dct_filter['skills_andor'] == '' or dct_filter['skills_andor'] == 'all':
                df_onboard = df_onboard[df_onboard.apply(lambda x: len([v for v in dct_filter[k] if v.lower() in 
                                                                    [t.strip().lower() for t in x[k].split(',')]])
                                                             ==len(dct_filter[k]),
                                                     axis=1)]
            elif dct_filter['skills_andor'] == 'any':
                df_onboard = df_onboard[df_onboard.apply(lambda x: len([v for v in dct_filter[k] if v.lower() in 
                                                                    [t.strip().lower() for t in x[k].split(',')]])
                                                             >0,
                                                     axis=1)]
        elif k=='industries':
            df_onboard[k] = df_onboard[k].astype(str)
            df_onboard = df_onboard[df_onboard.apply(lambda x: len([v for v in dct_filter[k] if stdd(v) in stdd(x[k])])
                                                             ==len(dct_filter[k]),
                                                     axis=1)]
        elif k=='professions':
            df_onboard[k] = df_onboard[k].astype(str).apply(eval)
            df_onboard = df_onboard[df_onboard.apply(lambda x: len([v for v in dct_filter[k] if v.lower() in 
                                                                    [t.split(',')[0].strip().lower() 
                                                                     for t in x[k]]])#.split(';')]])
                                                             ==len(dct_filter[k]),
                                                     axis=1)]
        elif k != 'skills_andor':
            df_onboard[k] = df_onboard[k].astype(str)
            df_onboard = df_onboard[df_onboard.apply(lambda x: len([v for v in dct_filter[k] if v.lower() in 
                                                                    [t.strip().lower() for t in x[k].split(',')]])
                                                             ==len(dct_filter[k]),
                                                     axis=1)]

    df_org['id'] = df_org['id'].astype(int)                   
    df_org = df_org.sort_values(by=['id'],ascending=True)

    return df_onboard[mycols][:n], df_org[mycols][:n]
@app.route('/info', methods=['GET'])

def name():
    mycolumns = ['id', 'firstname', 'lastname', 'email', 'country-2','Total Score', 'start_date', 'end_date', 'is_available', 'avail']
    args = request.args
    item_filter= args.get('item')
    n= args.get('rowsize')
    dct_filter = eval(item_filter)     
    df = pd.read_csv('simple_talent_csv_2022 - Sheet1.csv', dtype=str).fillna('') 
    a, b = main(mycolumns, dct_filter, df, int(n))
    a_json_list =a.to_json(orient = 'table')
    b_json_list= b.to_json(orient = 'table')
    return (b_json_list)

if __name__ == "__main__":	
    app.run()