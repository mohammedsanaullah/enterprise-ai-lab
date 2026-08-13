from datetime import date
from decimal import Decimal, InvalidOperation
from typing import Union


def validate_customer_name(name: str | None ) -> str:
    """
    Return the cleaned customer name or raise ValueError if empty/whitespace.
    """
    if name is None:
        raise ValueError("Customer name must be provided.")
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Customer name must not be empty or whitespace.")
    return cleaned


def validate_vehicle_year(year: Union[int, str]) -> int:
    """
    Validate and return the vehicle manufacturing year as an int.
    Accepts integers or digit strings. Raises ValueError on invalid input.
    """
    if isinstance(year, str):
        year_str = year.strip()
        if not year_str.isdigit():
            raise ValueError("Vehicle year must be numeric.")
        year_int = int(year_str)
    elif isinstance(year, int):
        year_int = year
    else:
        raise ValueError("Vehicle year must be an integer or numeric string.")

    current_year = date.today().year
    earliest_year = 1886
    if year_int < earliest_year or year_int > current_year:
        raise ValueError(
            f"Vehicle year must be between {earliest_year} and {current_year} (inclusive)."
        )
    return year_int


def validate_vehicle_price(price: Union[Decimal, int, str]) -> Decimal:
    """
    Validate and return the vehicle price as a Decimal.
    Accepts Decimal, int, or numeric string. Floats are rejected to avoid
    binary-floating imprecision; callers should provide Decimal or string.
    """
    if isinstance(price, Decimal):
        dec = price
    elif isinstance(price, int):
        dec = Decimal(price)
    elif isinstance(price, str):
        try:
            dec = Decimal(price.strip())
        except (InvalidOperation, ValueError):
            raise ValueError("Vehicle price must be numeric and convertible to Decimal.")
    else:
        # Reject floats and other types explicitly
        raise ValueError("Vehicle price must be a Decimal, int, or numeric string (floats not allowed).")

    if dec <= Decimal("0"):
        raise ValueError("Vehicle price must be greater than zero.")
    return dec