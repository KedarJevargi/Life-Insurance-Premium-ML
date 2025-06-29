import pickle
import pandas as pd

# Load the trained model from the pickle file
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

MODEL_VERSION="1.0.0"

def predict_output(user_input:dict):
    input_df=pd.DataFrame([user_input])
    return model.predict(input_df)[0]