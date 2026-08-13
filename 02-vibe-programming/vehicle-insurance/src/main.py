from __future__ import annotations
from pathlib import Path
from datetime import date
import sys

from .validation import (
    validate_customer_name,
    validate_vehicle_year,
    validate_vehicle_price,
)
from .premium_calculator import calculate_premium
from .policy_number import generate_policy_number
from .policy import Policy
from .filename_utils import build_policy_filename, resolve_unique_filename
from .pdf_generator import generate_policy_pdf


def main() -> None:
    try:
        # 1. Collect inputs
        customer_input = input("Customer name: ")
        year_input = input("Vehicle manufacturing year: ")
        price_input = input("Vehicle price: ")

        # 2. Validate
        customer_name = validate_customer_name(customer_input)
        vehicle_year = validate_vehicle_year(year_input)
        vehicle_price = validate_vehicle_price(price_input)

        # 3. Calculate premium
        yearly_premium = calculate_premium(vehicle_price, vehicle_year)

        # 4. Generate policy number
        issue_date = date.today()
        policy_number = generate_policy_number(issue_year=issue_date.year)

        # 5. Create Policy object
        policy = Policy(
            customer_name=customer_name,
            vehicle_year=vehicle_year,
            vehicle_price=vehicle_price,
            yearly_premium=yearly_premium,
            policy_number=policy_number,
            issue_date=issue_date,
        )

        # 6. Build filename
        filename = build_policy_filename(customer_name)

        # 7. Resolve unique filename and generate PDF
        out_dir = Path.cwd() / "output"
        out_dir.mkdir(parents=True, exist_ok=True)
        
        target_path = resolve_unique_filename(out_dir, filename)
        pdf_path = generate_policy_pdf(policy, target_path)

        # 8. Success message
        print(f"Policy PDF created: {pdf_path}")
    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)


if __name__ == "__main__":
    main()