# import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
# import matplotlib.pyplot as plt
# import seaborn as sns
import sys
import pickle
import re
import os
from time import sleep
from tqdm import tqdm
from progressbar import progressbar

p=len(sys.argv)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="../Results/encoded_data.txt"

# Construction du dictionnaire
dico={}
invdico={}
indice=1

data = pd.read_csv(sys.argv[1], sep = ';', low_memory=False)

# Feature selection 
features = ['AGER20', 'ANEMR', 'SFM', 'NPERR', 
              'VOIT', 'MODV', 'CS1', 'ILTUU', 'EMPL', 'MOCO']
# convert all the values to obeject
data = data[features].astype('str')
# select small set from data (change 10 to what ever you like)
#data = data[features].iloc[:100]
for i, row in progressbar(enumerate(data.values)):
    for col, val in zip(features,row):
        key = col +"-"+ val
        if key not in dico.keys():
            dico[key] = indice
            invdico[indice] = key
            indice += 1
            
for col in features:
    data[col] = data[col].apply(lambda x : dico[col +"-"+ x])

print("dictionary   :", dico)
print("Inverse dictionary    :", invdico)

    
with open(f_out, 'w') as out: 

    for row in progressbar(data.values):
        
        rows = []
        for val in row:
            rows.append(val)
        rows.sort()
        l=[str(i) for i in rows]
        out.write(" ".join(l))
        out.write("\n")
    out.close()


file = open('../Results/invdico.dbm', 'wb')
pickle.dump(invdico,file)





