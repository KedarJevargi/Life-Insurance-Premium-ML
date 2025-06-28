from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator,computed_field
import pickle
from typing import Annotated, Literal




# Load the trained model from the pickle file
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


tier_1_cities={"Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"}
tier_2_cities={"Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"}

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
    

    @field_validator("city")
    @classmethod
    def city_capital(cls,value):
        return value.capitalize()
    
    #calculate BMI of the user
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2),2)
    

    #calculate the lifestyle risk of the user
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi>30:
            return "High"
        elif self.smoker and self.bmi>27:
            return "Medium"
        else:
            return "Low"
        

    #calculate the age group of the user
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age<25:
            return "Young"
        elif self.age<45:
            return "Adult"
        else:
            return "Senior"
        
    #calculate the city_tire of the user
    @computed_field
    @property
    def city_tire(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3


        

        
    




    
    
   

