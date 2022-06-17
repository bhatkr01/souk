import pandas as pd
import numpy as np
from processing import summarizer

path="/Users/kritibbhattarai/Desktop/souk/files/"

needed_columns=['Q17_1', 'Q17_2', 'Q17_3', 'Q17_4', 'Q17_5', 'Q17_6',
       'Q17_7', 'Q17_8', 'Q17_9', 'Q17_10', 'Q17_11', 'Q17_12', 'Q17_13',
       'Q17_14', 'Q17_15', 'Q17_16', 'Q17_17', 'Q17_18', 'Q17_19', 'Q17_20',
       'Q17_21', 'Q17_22', 'Q17_23', 'Q17_24', 'Q17_25', 'Q12_1', 'Q12_2',
       'Q12_3', 'Q12_4', 'Q12_5', 'Q12_6', 'Q12_7', 'Q12_8', 'Q12_9', 'Q12_10',
       'Q12_11', 'Q12_12', 'Q12_13', 'Q12_14', 'Q12_15', 'Q13_1', 'Q13_2',
       'Q13_3', 'Q13_4', 'Q13_5', 'Q13_6', 'Q13_7', 'Q13_8', 'Q13_9', 'Q13_10',
       'Q13_11', 'Q13_12', 'Q13_13', 'Q13_14', 'Q14_1', 'Q14_2', 'Q14_3',
       'Q14_4', 'Q14_5', 'Q14_6', 'Q14_7']

needed_columns_year17=['Q12_1', 'Q12_2',
       'Q12_3', 'Q12_4', 'Q12_5', 'Q12_6', 'Q12_7', 'Q12_8', 'Q12_9', 'Q12_10',
       'Q12_11', 'Q12_12', 'Q12_13', 'Q12_14', 'Q12_15', 'Q13_1', 'Q13_2',
       'Q13_3', 'Q13_4', 'Q13_5', 'Q13_6', 'Q13_7', 'Q13_8', 'Q13_9', 'Q13_10',
       'Q13_11', 'Q13_12', 'Q13_13', 'Q13_14', 'Q14_1', 'Q14_2', 'Q14_3',
       'Q14_4', 'Q14_5', 'Q14_6', 'Q14_7']


file_list={2017:"2017.csv", 2018:"2018.csv", 2019:"2019.csv", 2020:"2020.csv", 2022:"2022.csv"}

def fileReader(file_list):
    for key,value in file_list.items():
        file=pd.read_csv(path+value)
        true_data=file[file['Finished'].str.lower()=='true']
        if key==2017:
            true_data=true_data.dropna(subset=needed_columns_year17)
        else:
            true_data=true_data.dropna(subset=needed_columns)
        mean,std,per_total, summary_less_13, summary_14_to_26, summary_27_to_40,another_summary_13, another_summary_14_to_26, another_summary_27_to_40, correlation=summarizer(true_data,key)
        print("\n",value,"mean","\n",mean)
        mean.to_csv("output/"+value+"mean_file.csv")
        print("\n",value,"std","\n",std)
        std.to_csv("output/"+value+"std_file.csv")
        print("\n",value,"per_total","\n",per_total)
        # per_total.to_csv(per_total+"per_total.csv")
        print("\n",value,"summary_less_13","\n",summary_less_13)
        summary_less_13.to_csv("output/"+value+"summary_less_13.csv")
        print("\n",value,"summary_14_to_26","\n",summary_14_to_26)
        summary_14_to_26.to_csv("output/"+value+"summary_14_to_26.csv")
        print("\n",value,"summary_27_to_40","\n",summary_14_to_26)
        summary_27_to_40.to_csv("output/"+value+"summary_27_to_40.csv")
        print("\n",value,"another_summary_less_13","\n",another_summary_13)
        another_summary_13.to_csv("output/"+value+"another_summary_13.csv")
        print("\n",value,"another_summary_14_to_26","\n",another_summary_14_to_26)
        another_summary_14_to_26.to_csv("output/"+value+"another_summary_14_to_26.csv")
        print("\n",value,"another_summary_27_to_40","\n",another_summary_27_to_40)
        another_summary_27_to_40.to_csv("output/"+value+"another_summary_27_to_40.csv")
        print("\n",value,"correlation","\n",correlation)
        if key!=2017:
            correlation.to_csv("output/"+value+"correlation.csv")

fileReader(file_list)
