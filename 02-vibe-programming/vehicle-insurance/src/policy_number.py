from datetime import date
from typing import Optional
import secrets
import string


def generate_policy_number(issue_year: Optional[int] = None) -> str:
    """
    Generate a policy number in the form: VP-YYYY-XXXXXX
    - issue_year: optional int to control the issue year for testing;
      if omitted, the current calendar year is used.
    """
    year = issue_year if issue_year is not None else date.today().year
    year_str = f"{int(year):04d}"
    alphabet = string.ascii_uppercase + string.digits
    suffix = "".join(secrets.choice(alphabet) for _ in range(6))
    return f"VP-{year_str}-{suffix}"