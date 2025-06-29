#Pydantic validation for the user input
from pydantic import BaseModel,Field,field_validator,computed_field
from typing import Annotated, Literal
from config.city_tier import tier_1_cities,tier_2_cities


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
        return value.strip().capitalize()
    
    #calculate BMI of the user
    @computed_field
    @property
    def bmi(self) -> float:
        return (self.weight/(self.height**2))
    

    #calculate the lifestyle risk of the user
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi>30:
            return "high"
        elif self.smoker and self.bmi>27:
            return "medium"
        else:
            return "low"
        

    #calculate the age group of the user
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age<25:
            return "young"
        elif self.age<45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
        
    #calculate the city_tire of the user
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        