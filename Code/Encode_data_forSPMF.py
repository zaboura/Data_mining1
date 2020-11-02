# import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
# import matplotlib.pyplot as plt
# import seaborn as sns
import sys
import pickle
import re
import os


p=len(sys.argv)
print(p)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="out.txt"

# Construction du dictionnaire
dico={}
invdico={}
indice=1

data = pd.read_csv(sys.argv[1], sep = ';')

# Feature selection 
features = ['REGION', 'AGER20', 'ANARR', 'ANEMR', 'ASCEN', 'BAIN', 'BATI', 'CATL', 'CHOS',
            'CLIM', 'CMBL', 'COUPLE', 'CS1', 'CUIS', 'DEROU', 'DIPL_15', 'EAU', 'EGOUL',
            'ELEC', 'EMPL', 'ETUD', 'GARL', 'ILTUU', 'IMMI', 'INAT', 'INFAM', 'INPER',
            'MOCO', 'MODV', 'NA38', 'NATC', 'NATNC', 'NBPI', 'NPERR', 'RECH', 'SANI',
            'SEXE', 'SFM', 'STOCD', 'TACT', 'VOIT', 'WC']
# convert all the values to obeject
data = data[features].astype('str')
# select small set from data
data = data[features].iloc[:10]

for i, row in enumerate(data.values):
    for col, val in zip(features,row):
        key = col +"-"+ val
        data[col].iloc[i] = key
        if key not in dico.keys():
            dico[key] = indice
            invdico[indice] = key
            indice += 1
            
print("dictionary   :", dico)
print("Inverse dictionary    :", invdico)


    
with open('../Results/encoded_file.txt', 'w') as out: 

    for row in data.values:
        rows = []
        for val in row:

            rows.append(dico[val])
        rows.sort()
        l=[str(i) for i in rows]
        out.write(" ".join(l))
        out.write("\n")
    out.close()


fichier=open('../Results/invdico.dbm', 'wb')
pickle.dump(invdico,fichier)





