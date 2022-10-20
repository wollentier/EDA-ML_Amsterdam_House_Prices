import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder


model = pickle.load(open("src/one_hot_enc_model.sav","rb"))
enc = pickle.load(open("src/one_hot_enc.sav","rb"))
scaler = pickle.load(open("src/scaler_fit.sav","rb"))

model_label = pickle.load(open("src/label_enc_model.sav","rb"))
enc_label = pickle.load(open("src/label_enc.sav","rb"))

def list_to_pandas_scaled(inputs: list,to_scale: list) -> pd.DataFrame:

    temp = {"Area": [inputs[0]],"Room": [inputs[1]],"Region": [inputs[2]]}
    temp = pd.DataFrame(temp)
    temp[to_scale] = pd.DataFrame(scaler.transform(temp[to_scale]), columns=to_scale)
    

    return temp

# creating  Label Encoding function enabling to properly encode possible future data points for one hot predictions
def OH_encoding(transformData: pd.DataFrame, OH_Encoder: OneHotEncoder, encoderColumn: str) -> pd.DataFrame:

    if "index" in transformData.columns:
        transformData = transformData.drop(["index"], axis=1)
        transformData = transformData.reset_index()
    
    if "index" not in transformData.columns:
        transformData = transformData.reset_index()
    
    temp_frame = pd.DataFrame((OH_Encoder.transform(transformData[[encoderColumn]])).toarray())
    transformData = pd.concat([transformData,temp_frame], axis=1).drop([encoderColumn], axis=1)
    transformData = transformData.drop(["index"], axis=1)
    transformData.columns = transformData.columns.astype(str)
       
    return transformData

def OH_prediction(predict_input: pd.DataFrame) -> int:

    prediction = int(model.predict(predict_input)[0])

    return prediction

# creating  Label Encoding function enabling to properly encode possible future data points for label predictions
def label_encoding(transformData: pd.DataFrame, NewColumnName: str, encodePattern: pd.DataFrame, encoderColumn: str) -> pd.DataFrame:
    transformData["temp_col1"] = [int(encodePattern.query("Region == @i")[encoderColumn]) for i in transformData["Region"]]
    transformData = transformData.drop(["Region"], axis=1).rename(columns={"temp_col1" : NewColumnName})
    return transformData


def label_prediction(predict_input: pd.DataFrame) -> int:

    prediction = int(model_label.predict(predict_input)[0])

    return prediction