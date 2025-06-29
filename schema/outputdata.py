from pydantic import BaseModel, Field
from typing import Dict

class OutputData(BaseModel):
    predicted_category: str = Field(
        description="The predicted insurance premium category"
    )
    confidence: float = Field(
        description="Model's confidence score for the predicted class (range: 0 to 1)"
    )
    class_probabilities: Dict[str, float] = Field(
        description="Probability distribution across all possible classes"
    )

