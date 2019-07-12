import pandas as pd

df = pd.DataFrame()
start = 723
end = 955
for i in range (start,end+1):
    print(i)
    if i == start:
        df = pd.read_csv("normalized_by_sum_" + str(i), names=["genes","abundance"])
    else:
        df_tmp = pd.read_csv("normalized_by_sum_" + str(i), names=["genes","abundance"])
        df = pd.merge(df,df_tmp,how='outer',on='genes')
        
df.fillna(0).to_csv('../merged_profile.csv')


