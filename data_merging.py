import csv
from dis import dis
from types import new_class
import pandas as pd

# df_1 = pd.read_csv("star_data.csv")
#df_2 = pd.read_csv("new_stars_data.csv")

dataset_1=[]
dataset_2=[]

with open("new_stars_data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        dataset_1.append(row)

del dataset_1[0]

with open("star_data.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        dataset_2.append(row)

del dataset_2[0]

dataset=dataset_2+dataset_1

name=[]
distance=[]
mass=[]
radius=[]

for row in dataset:
    name.append(row[0])
    distance.append(row[1])
    mass.append(row[2])
    radius.append(row[3])

new_dataset={"Name":name,"Distance":distance,"Mass":mass,"Radius":radius}

df = pd.DataFrame(new_dataset)
print(df.head(-1))

df.to_csv("final.csv",index=False)