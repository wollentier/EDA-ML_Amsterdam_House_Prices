import pandas as pd
import numpy as np
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


# # # # # # # # # # # DATA FOR BINNED REGION PRICE ZIPS # # # # # # # # # # #

region_data = data[["Price","Area","Room","Region"]].copy()

# creating regions based on prices
new_regions_bins = [[0,300000],[300000,600000],[600000,900000],[900000,1200000],[1200000,1000000000]]
new_regions = ["0_to_300k","300k_to_600k","600k_to_900k","900k_to_1200k","more_than_1200000"]

# # creating dataframe that contains the actual region of each house sorted into the correct new column
df_data = [list(np.where(region_data["Price"].isin(region_data.loc[(region_data["Price"] > new_regions_bins[i][0]) & (region_data["Price"] <= new_regions_bins[i][1])]["Price"])==True,region_data["Region"].astype(int),0)) for i in range(0,len(new_regions_bins))]
temp_frame = pd.DataFrame(data=dict(zip(new_regions,df_data)), dtype="int32")

# add the new dataframe to the data
region_data = pd.concat([region_data.reset_index(),temp_frame], axis=1).drop(["index"], axis=1)

# label encoding
for t,i in enumerate(new_regions):
    region_data[i] = np.where(region_data[i] == 0,0,t+1)

region_data["price_cat_encoded"] = region_data[new_regions].sum(axis=1)
region_data = region_data.drop(new_regions, axis=1)

# creating encoding pattern for Label Encoding enabling to properly encode possible future data points for predictions
encode_pattern_var3 = region_data.copy()

encode_pattern_var3 = [(encode_pattern_var3
                    .query("Region == @i")
                    .groupby("price_cat_encoded")
                    .count()
                    .idxmax()["Region"]) 
                    
                    for i in encode_pattern_var3["Region"].unique()]

encode_pattern_var3 = pd.DataFrame({"Region":list(data["Region"].unique()),"most_frequent_cat":encode_pattern_var3})
encode_pattern_var3["most_frequent_cat"] = encode_pattern_var3["most_frequent_cat"].astype("category")

# translate the numeric label to the actual label just for later plotting
temp_for_plot = encode_pattern_var3.copy()
temp_for_plot["most_frequent_cat"] = temp_for_plot["most_frequent_cat"].replace([1,2,3,4,5],new_regions)

map_price_regions = temp_for_plot.copy()