import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

#parse data
df2 = pd.read_csv("eggNOGprofile.csv")
del df2["seed_ortholog_evalue"]
del df2["seed_ortholog_score"]
del df2["num"]
df2= df2.set_index('index').T

df2.to_csv("eggnogProfile_transposed",header=True, index=True)

df1 = pd.read_csv("MetadataForAnalysis.csv")
df2 = pd.read_csv("eggnogProfile_transposed")
oxy_tmp = df1[["CTDOXY","index","CTDTMP"]]
df2 = df2.rename(columns={"Unnamed: 0": "index"})
merged_df = pd.merge(oxy_tmp, df2, how='inner', on= "index")
merged_df = merged_df[merged_df['CTDTMP'] != -999.0000]
oxy_tmp = merged_df[["CTDOXY","CTDTMP"]]
eggnog = merged_df.drop('CTDOXY', axis=1).drop('CTDTMP', axis=1).drop('index', axis=1)
df1= oxy_tmp
df2= eggnog
ndf1=df1.T.values
ndf2=df2.T.values
res=(1 - cdist(ndf1, ndf2, metric='correlation'))  
res=pd.DataFrame(res, index=df1.columns, columns=df2.columns)
res.to_csv("correlation_result.csv")
