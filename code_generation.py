from pydantic import BaseModel
from  typing import List
from pydantic import BaseModel, Field

class DesignCode(BaseModel):
    software_used: str = Field(..., description="The CAD software used for the design (e.g., SolidWorks).")
    design_id: str = Field(..., description="Unique identifier for the design (e.g., D001).")
    name: str = Field(..., description="Name of the design (e.g., Rectangular Baseplate with Reinforced Corners).")
    code_snippet: str = Field(..., description="Automated Code snippet or CAD scripting used for the design.")



class CodeOutput(BaseModel):
    code_output : List[DesignCode]



