from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.inputdata import InputData 
from model.predict import predict_output,MODEL_VERSION





app=FastAPI()    

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message":"Health insurance predictor API"}

@app.get("/health")
def health_check():
    return {"status":"ok",
            "version":MODEL_VERSION}


@app.post("/predict")
def predict_premium(data: InputData):

    input_dict = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    prediction =predict_output(input_dict)
    return JSONResponse(status_code=200, content={'predicted_category': prediction})

