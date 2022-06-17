import pandas as pd
import numpy as np
import functools 
import re

path="/Users/kritibbhattarai/Desktop/souk/files/"

file1=pd.read_csv(path+"2017.csv")
file2=pd.read_csv(path+"2018.csv")
file3=pd.read_csv(path+"2019.csv")
file4=pd.read_csv(path+"2020.csv")
file5=pd.read_csv(path+"2022.csv")
data=[file2,file3,file4,file5]
df_merged = functools.reduce(lambda  first,second: pd.merge(first,second,how='outer'), data)
# pd.DataFrame.to_csv(df_merged, 'files/merged.csv', sep=',', na_rep='.', index=False)

file=df_merged
needed_columns=['Q17_1', 'Q17_2', 'Q17_3', 'Q17_4', 'Q17_5', 'Q17_6',
       'Q17_7', 'Q17_8', 'Q17_9', 'Q17_10', 'Q17_11', 'Q17_12', 'Q17_13',
       'Q17_14', 'Q17_15', 'Q17_16', 'Q17_17', 'Q17_18', 'Q17_19', 'Q17_20',
       'Q17_21', 'Q17_22', 'Q17_23', 'Q17_24', 'Q17_25',  'Q13_1', 'Q13_2',
       'Q13_3', 'Q13_4', 'Q13_5', 'Q13_6', 'Q13_7', 'Q13_8', 'Q13_9', 'Q13_10',
       'Q13_11', 'Q13_12', 'Q13_13', 'Q13_14']

true_data=file[file['Finished'].str.lower()=='true']

true_data=true_data.dropna(subset=needed_columns)

pd.set_option('display.max_rows', None)

############################################Categorical to Numerical ###############################################

def matcher(column, replacing_dict):
    for key, replacer in replacing_dict.items():
        if key.lower() in column.lower():
            return replacer
    else:
        return np.nan



def summarizer(data):
    
    data_copy=data.copy()
    ###################################################question 17########################################

    replacing_dict_17={"not true":0, "rarely true":1, "sometimes true":2, "often true":3, "true at":4}


    column_list_17=[]
    for i in range(1,26):
        data_copy.loc[:,('Q17_'+str(i))]=data_copy['Q17_'+str(i)].apply(matcher, replacing_dict=replacing_dict_17)
        column_list_17.append('Q17_'+str(i))
         
    # print(data_copy[['Q17_1','Q17_2']])

    a=['Q17_24','Q17_11','Q17_12','Q17_25','Q17_10','Q17_23','Q17_17','Q17_16']
    b=['Q17_20','Q17_18','Q17_15','Q17_6','Q17_7','Q17_19','Q17_14']
    c=['Q17_8','Q17_2','Q17_5','Q17_4','Q17_1']
    d=['Q17_21','Q17_13','Q17_22']
    e=['Q17_9','Q17_3']
    data_copy['Q17_a']= data_copy[a].sum(axis=1)
    data_copy['Q17_b']= data_copy[b].sum(axis=1)
    data_copy['Q17_c']= data_copy[c].sum(axis=1)
    data_copy['Q17_d']= data_copy[d].sum(axis=1)
    data_copy['Q17_e']= data_copy[e].sum(axis=1)
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
         
    x=['Q13_1','Q13_2','Q13_3','Q13_8','Q13_11','Q13_12','Q13_14']
    y= ['Q13_4','Q13_5','Q13_6','Q13_7','Q13_9','Q13_10','Q13_13']
    z=['Q13']
    data_copy['Q13_total']= data_copy[column_list_13].sum(axis=1)
    data_copy['Q13_x']= data_copy[x].sum(axis=1)
    data_copy['Q13_y']= data_copy[y].sum(axis=1)
    # print(data_copy['Q13_total'])


    # print(data_copy[['Q13_1','Q13_2']])

    
    ####################correlation########################
    section_1=['Q13_x', 'Q13_x', 'Q13_total']
    section_2=['Q17_a', 'Q17_b', 'Q17_c', 'Q17_d', 'Q17_e','Q17_total']
    correlation=data_copy.corr().loc[section_1, section_2]
    correlation.to_csv("output/"+"combined_file_13_17"+"correlation.csv")

    return( correlation)

print(summarizer(true_data))


