from pydantic import BaseModel, condecimal, conlist
from typing import List, Optional
# General information about the product
from typing import List, Optional
from pydantic import BaseModel
from typing import List, Optional, Dict 
from pydantic import BaseModel

from pydantic import BaseModel, Field
from typing import Optional

class LoadCapacity(BaseModel):
    primary_vertical_load: float = Field(..., description="Primary vertical load in Newtons (N)")
    lateral_load: float = Field(..., description="Lateral (horizontal) load in Newtons (N)")
    factor_of_safety: float = Field(..., description="Factor of safety (FOS), should be >= 2")

    class Config:
        schema_extra = {
            "example": {
                "primary_vertical_load": 3000,
                "lateral_load": 300,
                "factor_of_safety": 2.0
            }
        }

class DimensionsAndMounting(BaseModel):
    max_footprint: str = Field(..., description="Maximum plate footprint (length x width) in mm")
    plate_thickness: float = Field(..., description="Plate thickness in mm (max 10mm)")
    mounting_holes: int = Field(..., description="Number of mounting holes (should be 4)")
    hole_spacing: Optional[str] = Field(None, description="Mounting hole spacing pattern (e.g., center-to-center distance)")

    class Config:
        schema_extra = {
            "example": {
                "max_footprint": "200mm x 200mm",
                "plate_thickness": 10.0,
                "mounting_holes": 4,
                "hole_spacing": "even distribution within footprint"
            }
        }

class DeflectionConstraint(BaseModel):
    max_deflection: float = Field(..., description="Maximum allowed deflection at center or post location (mm)")

    class Config:
        schema_extra = {
            "example": {
                "max_deflection": 0.5
            }
        }

class WeightAndCost(BaseModel):
    max_weight: float = Field(..., description="Maximum weight in kilograms (kg)")
    estimated_cost: float = Field(..., description="Estimated material cost in USD")

    class Config:
        schema_extra = {
            "example": {
                "max_weight": 3.0,
                "estimated_cost": 20.0
            }
        }

class Manufacturability(BaseModel):
    fabrication_methods: list[str] = Field(..., description="List of fabrication methods (e.g., laser cutting, waterjet, etc.)")
    geometry_simplicity: bool = Field(..., description="Flag to indicate if geometry should be kept simple for fabrication")

    class Config:
        schema_extra = {
            "example": {
                "fabrication_methods": ["laser cutting", "waterjet cutting", "drilling"],
                "geometry_simplicity": True
            }
        }

class SafetyAndInstallation(BaseModel):
    sharp_edges: bool = Field(..., description="Should the plate have sharp edges?")
    rounded_corners: bool = Field(..., description="Flag for rounded or chamfered corners for safety")
    bolt_hole_reinforcement: bool = Field(..., description="Should bolt holes be reinforced to prevent tearing?")
    reference_mark: Optional[str] = Field(None, description="Type of mounting reference for positioning (e.g., center hole)")

    class Config:
        schema_extra = {
            "example": {
                "sharp_edges": False,
                "rounded_corners": True,
                "bolt_hole_reinforcement": True,
                "reference_mark": "center hole"
            }
        }

class BaseplateDesign(BaseModel):
    load_capacity: LoadCapacity
    dimensions_and_mounting: DimensionsAndMounting
    deflection_constraint: DeflectionConstraint
    weight_and_cost: WeightAndCost
    manufacturability: Manufacturability
    safety_and_installation: SafetyAndInstallation

    class Config:
        schema_extra = {
            "example": {
                "load_capacity": {
                    "primary_vertical_load": 3000,
                    "lateral_load": 300,
                    "factor_of_safety": 2.0
                },
                "dimensions_and_mounting": {
                    "max_footprint": "200mm x 200mm",
                    "plate_thickness": 10.0,
                    "mounting_holes": 4,
                    "hole_spacing": "even distribution within footprint"
                },
                "deflection_constraint": {
                    "max_deflection": 0.5
                },
                "weight_and_cost": {
                    "max_weight": 3.0,
                    "estimated_cost": 20.0
                },
                "manufacturability": {
                    "fabrication_methods": ["laser cutting", "waterjet cutting", "drilling"],
                    "geometry_simplicity": True
                },
                "safety_and_installation": {
                    "sharp_edges": False,
                    "rounded_corners": True,
                    "bolt_hole_reinforcement": True,
                    "reference_mark": "center hole"
                }
            }
        }
        