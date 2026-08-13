from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional


def _age_adjustment(age: int) -> Decimal:
    if age <= 3:
        return Decimal("0")
    if 4 <= age <= 7:
        return Decimal("0.10")
    return Decimal("0.20")


def calculate_premium(vehicle_price: Decimal, vehicle_year: int, *, current_year: Optional[int] = None) -> Decimal:
    """
    Calculate and return the final yearly premium as a Decimal rounded to 2 decimals.

    Parameters:
    - vehicle_price: Decimal (must be provided by caller)
    - vehicle_year: int (manufacturing year)
    - current_year: optional int for the current year (defaults to today's year)

    Returns:
    - Decimal rounded to two decimal places.
    """
    if current_year is None:
        current_year = date.today().year

    age = current_year - vehicle_year
    # base premium = 3% of vehicle price
    base = vehicle_price * Decimal("0.03")
    adjustment = _age_adjustment(age)
    final = base * (Decimal("1") + adjustment)
    # round to two decimal places
    return final.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)