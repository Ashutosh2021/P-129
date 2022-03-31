import pandas as pd

df= pd.read_csv("stars_data.csv")

df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

new_radius_list =[]

for element in df['Radius'] :

    new_element=float(element)*0.102763
    new_radius_list.append(new_element)

new_mass_list =[]

for element in df['Mass'] :

    new_element=float(element)*0.000954588
    new_mass_list.append(new_element)


# print(new_radius_list)
#print(len(new_radius_list))
# print(df.shape)

temp_json = {"Name":df["Star Name"],"Distance":df["Distance"],"Mass":new_mass_list,"Radius":new_radius_list}
new_df = pd.DataFrame(temp_json)

# print(new_df.shape)

df.to_csv("new_stars_data.csv",index=False)