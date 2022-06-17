import pandas as pd 
import numpy as np
import re

pd.set_option('display.max_rows', None)

############################################Categorical to Numerical ###############################################

def matcher(column, replacing_dict):
    for key, replacer in replacing_dict.items():
        if key.lower() in column.lower():
            return replacer
    else:
        return np.nan

def max_number(column):
    if isinstance(column, str):
        checker=[int(s) for s in re.split('-| ',column) if s.isdigit()]
        if len(checker)>0:
            return (max(checker))
        else:
            return 0
    else:
        return column


def summarizer(data, year):

    ############################################Question 12 ###############################################
    data_copy=data.copy()
    replacing_dict_12={ "almost always":1, "very frequently":2, "somewhat frequently":3, "somewhat infrequently":4, "very infrequently":5,"almost never":6}
    
    column_list_12=[]
    for i in range(1,16):
        data_copy.loc[:,('Q12_'+str(i))]=data_copy['Q12_'+str(i)].apply(matcher, replacing_dict=replacing_dict_12)
        column_list_12.append('Q12_'+str(i))
         

    data_copy['Q12_total']= data_copy[column_list_12].sum(axis=1)
    # print(data_copy['Q14_total'])


    # data_copy['Q12_total']= data_copy.iloc[:, 29:44].sum(axis=1)
    # print(data_copy[['Q12_1','Q12_2']])


    ####################################################Question14###########################################################
    replacing_dict_14={"not at":0, "several days":1, "over half the days":2, "nearly every day":3}

    column_list_14=[]
    for i in range(1,8):
        data_copy.loc[:,('Q14_'+str(i))]=data_copy['Q14_'+str(i)].apply(matcher, replacing_dict=replacing_dict_14)
        column_list_14.append('Q14_'+str(i))
         

    data_copy['Q14_total']= data_copy[column_list_14].sum(axis=1)
    # print(data_copy['Q14_total'])


    # print(data_copy[['Q14_1','Q14_2']])

    ###################################################question 17########################################
    if year!=2017:

        replacing_dict_17={"not true":0, "rarely true":1, "sometimes true":2, "often true":3, "true at":4}


        column_list_17=[]
        for i in range(1,26):
            data_copy.loc[:,('Q17_'+str(i))]=data_copy['Q17_'+str(i)].apply(matcher, replacing_dict=replacing_dict_17)
            column_list_17.append('Q17_'+str(i))
             
        # print(data_copy[['Q17_1','Q17_2']])

        data_copy['Q17_total']= data_copy[column_list_17].sum(axis=1)
        # print(data_copy['Q17_total'])



    ####################################################Question13###########################################################
    import itertools as it

    replacing_dict_13={"never":0, "almost never":1, "sometimes":2, "fairly often":3, "very often":4}
    replacing_dict_13_reverse={"never":4, "almost never":3, "sometimes":2, "fairly often":1, "very often":0}

    reversed_list=[4, 5, 6, 7, 9, 10,13]

    column_list_13=[]
    for i in range(1,15):
        if i in reversed_list:
            data_copy.loc[:,('Q13_'+str(i))]=data_copy['Q13_'+str(i)].apply(matcher, replacing_dict=replacing_dict_13_reverse)
        else:
            data_copy.loc[:,('Q13_'+str(i))]=data_copy['Q13_'+str(i)].apply(matcher, replacing_dict=replacing_dict_13)

        column_list_13.append('Q13_'+str(i))
         

    data_copy['Q13_total']= data_copy[column_list_13].sum(axis=1)
    # print(data_copy['Q13_total'])


    # print(data_copy[['Q13_1','Q13_2']])

    ####################################################Question9&10###########################################################
    data_copy['Q9'] = data_copy['Q9'].fillna(0)
    data_copy['Q10'] = data_copy['Q10'].fillna(0)
    data_copy.loc[:,('Q9')]=data_copy['Q9'].apply(max_number)
    data_copy.loc[:,('Q10')]=data_copy['Q10'].apply(max_number)
    # print(data_copy[['Q9','Q10']])

    ##########################################################summarize##############################################################

    #################################mean and std####################################
    if year!=2017:
        mean=data_copy.groupby(['Q4'])[['Q12_total','Q13_total', 'Q14_total', 'Q17_total']].mean()
        std=data_copy.groupby(['Q4'])[['Q12_total','Q13_total', 'Q14_total', 'Q17_total']].std()
    else:
        mean=data_copy.groupby(['Q4'])[['Q12_total','Q13_total', 'Q14_total']].mean()
        std=data_copy.groupby(['Q4'])[['Q12_total','Q13_total', 'Q14_total']].std()
    #######################calculate percentage of responder########################
    year_total={
            2017:{
                "First Year-level courses": 50,
                "Sophomore-level courses":39,
                "Junior-level courses": 40,
                "Senior-level courses": 26
                }, 
            2018:{
                "First Year-level courses": 64,
                "Sophomore-level courses":44,
                "Junior-level courses": 34,
                "Senior-level courses": 39
                }, 
            2019:{
                "First Year-level courses": 63,
                "Sophomore-level courses":46,
                "Junior-level courses": 39,
                "Senior-level courses": 34,
                },
             2020 :{
                "First Year-level courses": 57,
                "Sophomore-level courses":43,
                "Junior-level courses": 42,
                "Senior-level courses": 39,
                },
             2022:{
                "First Year-level courses": 59,
                "Sophomore-level courses":52,
                "Junior-level courses": 30,
                "Senior-level courses": 20,
                },
    } 
    total = data_copy.groupby(['Q4'])['Q4'].count()
    per_total=''
    for key,value in total.items():
        key,value=key,(value/year_total[year][key])*100
        per_total+=f"{key}, {value} \n"

    ######################################question_13_details###############################
    
    less_13=data_copy[data_copy['Q13_total']<=13]
    summary_less_13=less_13.groupby(['Q4'])[['Q9', "Q10",'Q12_total', 'Q14_total']].mean()
    another_summary_13=less_13.groupby(['Q4'])[['Q11', "Q5"]].count()
    data_14_to_26=data_copy[(data_copy['Q13_total']>13) &  (data_copy['Q13_total']<=26)]
    summary_14_to_26=data_14_to_26.groupby(['Q4'])[['Q9', "Q10",'Q12_total', 'Q14_total']].mean()
    another_summary_14_to_26=data_14_to_26.groupby(['Q4'])[['Q11', "Q5"]].count()
    data_27_to_40=data_copy[(data_copy['Q13_total']>26) & (data_copy['Q13_total']<=40)]
    summary_27_to_40=data_27_to_40.groupby(['Q4'])[['Q9', "Q10",'Q12_total', 'Q14_total']].mean()
    another_summary_27_to_40=data_27_to_40.groupby(['Q4'])[['Q11', "Q5"]].count()
    
    ####################correlation########################
    section_1=['Q13_1', 'Q13_2', 'Q13_3', 'Q13_4', 'Q13_5', 'Q13_6', 'Q13_7', 'Q13_8', 'Q13_9', 'Q13_10', 'Q13_11', 'Q13_12', 'Q13_13', 'Q13_14', 'Q13_total']
    section_2=['Q17_1', 'Q17_2', 'Q17_3', 'Q17_4', 'Q17_5', 'Q17_6', 'Q17_7', 'Q17_8', 'Q17_9', 'Q17_10', 'Q17_11', 'Q17_12', 'Q17_13', 'Q17_14', 'Q17_15', 'Q17_16', 'Q17_17', 'Q17_18', 'Q17_19', 'Q17_20', 'Q17_21', 'Q17_22', 'Q17_23', 'Q17_24', 'Q17_25','Q17_total']
    if year!=2017:
        # correlation=data_copy[section_1].corrwith(data_copy[section_2])
        correlation=data_copy.corr().loc[section_1, section_2]
        # correlation.to_csv("correlation_file.csv")
    else:
        correlation=None
    # correlation=data_copy.corr()
    # correlation.to_csv("correlation_file.csv")

    return(mean,std,per_total, summary_less_13, summary_14_to_26, summary_27_to_40, another_summary_13, another_summary_14_to_26, another_summary_27_to_40, correlation)


