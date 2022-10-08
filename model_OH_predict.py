import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder


model = pickle.load(open("one_hot_enc_model.sav","rb"))
enc = pickle.load(open("one_hot_enc.sav","rb"))

def list_to_pandas(inputs: list) -> pd.DataFrame:

    temp = {"Area": [inputs[0]],"Room": [inputs[1]],"Region": [inputs[2]]}
    temp = pd.DataFrame(temp)

    return temp

# creating  Label Encoding function enabling to properly encode possible future data points for predictions
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