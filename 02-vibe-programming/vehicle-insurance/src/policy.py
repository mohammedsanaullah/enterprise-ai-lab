from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass
class Policy:
    """
    Vehicle insurance policy data model.

    Fields:
    - customer_name: name of the policyholder
    - vehicle_year: manufacturing year of the vehicle
    - vehicle_price: vehicle price (Decimal)
    - yearly_premium: yearly premium amount (Decimal)
    - policy_number: unique policy identifier
    - issue_date: date the policy was issued
    """
    customer_name: str
    vehicle_year: int
    vehicle_price: Decimal
    yearly_premium: Decimal
    policy_number: str
    issue_date: date