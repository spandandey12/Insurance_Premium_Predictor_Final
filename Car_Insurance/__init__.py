"""
Car Insurance Sub-Package
Provides functionality to compute car insurance risk factors and final premium estimates.
"""

from .training import CarInsurance, result
from .preprocessing import (
    age_factor,
    mileage_factor,
    car_age_factor,
    experience_factor,
    accident_factor,
    combined_factors
)

