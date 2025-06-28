from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator
import pickle
from typing import Annotated, Literal




# Load the trained model from the pickle file
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


app=FastAPI()    

#Pydantic validation for the user input
class InputData(BaseModel):
    age:Annotated[int, Field(...,gt=0,lt=120,description="Age of the user")]
    weight:Annotated[float, Field(...,gt=0,description="Weight of the user")]
    height:Annotated[float, Field(...,gt=0,lt=2.5,description="Height of the user")]
    income_lpa:Annotated[float, Field(...,gt=0,description="Annul Income of the user")]
    smoker:Annotated[bool, Field(...,description="Is user a smoker")]
    city:Annotated[str, Field(...,max_length=25,description="City of the user")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(...,max_length=25,description="Occupation of the user")]

    #Convert 1st letter of city to capital
    @field_validator("city")
    @classmethod
    def make_city_cap(cls, value):
        return value.capitalize()
    
   

