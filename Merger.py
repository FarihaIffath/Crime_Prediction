import pandas as pd
import glob


li = []

all_file = [i for i in glob.glob("*.csv")]

print(all_file)

for i in range(0,len(all_file)):
    df = pd.read_csv(all_file[i],index_col = None)
    li.append(df)


combined  = pd.concat(li,sort =False)
print(combined)

combined.to_csv("Final.csv")




    
    
