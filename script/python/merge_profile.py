import pandas as pd
import sys
df = pd.DataFrame()
start = 723
end = 955 #955
for i in range (start,end+1):
    print(i)
    print("size:"+ str(sys.getsizeof(df)))
    print(df.info())
    if i == start:
        df = pd.read_csv("/home/kumay/metagenome_data/mapping/tmp/normalized_by_sum_" + str(i), names=["genes", str(i)])
    else:
        df_tmp = pd.read_csv("/home/kumay/metagenome_data/mapping/tmp/normalized_by_sum_" + str(i), names=["genes", str(i)])
        df = pd.merge(df,df_tmp,how='outer',on='genes')
        
df.fillna(0).to_csv('/home/kumay/metagenome_data/mapping/merged_profile.csv')


