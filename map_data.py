import pandas as pd
import plotly.express as px
import json

# # # # # # # # # # # DATA FOR 1. PLOT # # # # # # # # # # #

# Loading dataframe
data = pd.read_csv("./HousingPrices-Amsterdam-August-2021.csv")

# Renaming Unnamed column and drop NaN rows
data = data.rename(columns={"Unnamed: 0":"index"})
data = data.drop(data.loc[data["Price"].isna() == True,"Price"].index)

# check data types
data["Region"] = data["Zip"].str[0:4].astype(int)
data["Price"] = data["Price"].astype(float)
data["Area"] = data["Area"].astype(float)
data["Room"] = data["Room"].astype(int)

# loading geojson data
geodata=json.load(open("./georef-netherlands-postcode-pc4_simple.geojson","r"))

#plotly needs specificly "id" within features so we have to copy them from properties to features
for i in geodata["features"]:
    i["id"]=i["properties"]["pc4_code"]

#get zip codes from geojson data
zip_list = []
for i in geodata["features"]:
    zip_list.append(i["properties"]["pc4_code"])

# average data for plotting
avg_data = data.groupby(["Region"]).median().reset_index()[["Region","Price"]]

'''
# # # # # # # # # # # DATA FOR 2. PLOT # # # # # # # # # # #

# create bins/regions
new_regions = ["less_0","less_300000","less_600000","less_900000","less_1200000","more_1200000"]
binned_data = data[["Price","Region","Area","Room","index"]].copy()

# fit data to bins
for i in range(len(new_regions)):
    
    if (new_regions[i].split("_")[0]) == "less":
        binned_data[new_regions[i+1]] = binned_data.loc[(binned_data["Price"] <= int(new_regions[i+1].split("_")[1])) & (binned_data["Price"] > int(new_regions[i].split("_")[1])), "Price"]
        
    elif new_regions[i].split("_")[0] == "more":
        binned_data[new_regions[i]] = binned_data.loc[(binned_data["Price"] > int(new_regions[i].split("_")[1])), "Price"]
        
    else:
        break


# relabel prices to price bin
for i in new_regions[1:]:
    binned_data.loc[binned_data[i].isna() == False, i] = i
    binned_data.loc[binned_data[i].isna() == True, i] = ""
    if i != new_regions[1]:
        binned_data[new_regions[1]] += binned_data[i]
binned_data["Price_Region"] = binned_data[new_regions[1]]

# drop rows with equal Region
binned_data = (binned_data
    .drop_duplicates(subset="Region")
    .reset_index()
    .drop(columns={*new_regions[1:],"level_0"})
    )

# add average price column
binned_data["Avg_Price"] = avg_data["Price"]
print(binned_data)
'''
