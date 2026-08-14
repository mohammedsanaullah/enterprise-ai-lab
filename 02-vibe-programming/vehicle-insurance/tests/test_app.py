import sys
from pathlib import Path
from decimal import Decimal
from datetime import date
import re
from pypdf import PdfReader


from src.validation import (
    validate_customer_name,
    validate_vehicle_year,
    validate_vehicle_price,
)
from src.premium_calculator import calculate_premium
from src.policy_number import generate_policy_number
from src.filename_utils import sanitize_customer_name, build_policy_filename, resolve_unique_filename
from src.pdf_generator import generate_policy_pdf
from src.policy import Policy


# Validation: customer name
def test_validate_customer_name_valid():
    assert validate_customer_name(" Alice Smith ") == "Alice Smith"


import pytest


@pytest.mark.parametrize("bad", ["", "   ", "\n\t"])
def test_validate_customer_name_empty_whitespace(bad):
    with pytest.raises(ValueError):
        validate_customer_name(bad)


# Validation: vehicle year
def test_validate_vehicle_year_valid_current_and_past():
    cur = date.today().year
    assert validate_vehicle_year(str(cur)) == cur
    assert validate_vehicle_year("1999") == 1999


def test_validate_vehicle_year_non_numeric():
    with pytest.raises(ValueError):
        validate_vehicle_year("20X0")


def test_validate_vehicle_year_future():
    future = date.today().year + 1
    with pytest.raises(ValueError):
        validate_vehicle_year(str(future))


def test_validate_vehicle_year_too_early():
    with pytest.raises(ValueError):
        validate_vehicle_year("1800")


# Validation: vehicle price
def test_validate_vehicle_price_valid_positive():
    assert validate_vehicle_price("12345.67") == Decimal("12345.67")
    assert validate_vehicle_price(1000) == Decimal("1000")


@pytest.mark.parametrize("bad", ["0", "0.00", "-1", "-100.5"])
def test_validate_vehicle_price_zero_negative(bad):
    with pytest.raises(ValueError):
        validate_vehicle_price(bad)


def test_validate_vehicle_price_invalid_numeric():
    with pytest.raises(ValueError):
        validate_vehicle_price("12,345.67")


# Premium calculation
def test_premium_age_buckets_and_rounding():
    price = Decimal("10000")
    # age 0 => current_year == vehicle_year
    p0 = calculate_premium(price, date.today().year, current_year=date.today().year)
    # base = 300, adjustment 0% => 300.00
    assert p0 == Decimal("300.00")

    # age 5 => 10% adjustment => 330.00
    p5 = calculate_premium(price, date.today().year - 5, current_year=date.today().year)
    assert p5 == Decimal("330.00")

    # age 10 => 20% adjustment => 360.00
    p10 = calculate_premium(price, date.today().year - 10, current_year=date.today().year)
    assert p10 == Decimal("360.00")

    # rounding test with amounts that produce fractional cents
    price2 = Decimal("12345.67")
    final = calculate_premium(price2, date.today().year - 12, current_year=date.today().year)
    # compute expected with Decimal
    base = (price2 * Decimal("0.03"))
    expected = (base * Decimal("1.20")).quantize(Decimal("0.01"))
    assert final == expected


# Policy number
def test_generate_policy_number_format_and_year_and_suffix():
    pn = generate_policy_number(issue_year=2020)
    assert pn.startswith("VP-2020-")
    suffix = pn.split("-")[-1]
    assert re.fullmatch(r"[A-Z0-9]{6}", suffix)


# Filename handling
def test_sanitize_and_build_filename_basic():
    s = sanitize_customer_name("John Doe")
    assert s == "john-doe"
    fname = build_policy_filename("John Doe")
    assert fname == "john-doe-policy.pdf"


def test_sanitize_preserves_unicode_and_replaces_specials():
    inp = " Ana María O'Neil / .. "
    s = sanitize_customer_name(inp)
    # lowercase kebab-case, no slashes, no leading/trailing hyphens
    assert "/" not in s and "\\" not in s
    assert s == "ana-maría-o-neil"


def test_resolve_unique_filename(tmp_path):
    filename = "jane-doe-policy.pdf"

    # First file already exists
    (tmp_path / filename).write_text("dummy")

    resolved = resolve_unique_filename(tmp_path, filename)

    assert resolved.name == "jane-doe-policy-1.pdf"

    # Simulate the generated file now existing
    resolved.write_text("dummy")

    resolved2 = resolve_unique_filename(tmp_path, filename)

    assert resolved2.name == "jane-doe-policy-2.pdf"


# PDF generation
def test_generate_policy_pdf_creates_file_and_one_page(tmp_path):
    policy = Policy(
        customer_name="Test User",
        vehicle_year=2020,
        vehicle_price=Decimal("15000.00"),
        yearly_premium=Decimal("450.00"),
        policy_number="VP-2020-ABC123",
        issue_date=date.today(),
    )
    out = tmp_path / "test-policy.pdf"
    path = generate_policy_pdf(policy, out)
    assert path.exists()
    # data = path.read_bytes()
    # crude page count: count page objects
   #  pages = len(re.findall(rb"/Type\s*/Page", data))
    reader = PdfReader(path)
    assert len(reader.pages) == 1
   # assert pages == 1
    # Ensure returned path matches
    assert Path(path) == out

def test_generate_policy_pdf_contains_required_information(tmp_path):
    policy = Policy(
        customer_name="Test User",
        vehicle_year=2020,
        vehicle_price=Decimal("15000.00"),
        yearly_premium=Decimal("450.00"),
        policy_number="VP-2026-ABC123",
        issue_date=date(2026, 8, 14),
    )

    out = tmp_path / "test-policy.pdf"

    generate_policy_pdf(policy, out)

    reader = PdfReader(out)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    assert "Test User" in text
    assert "2020" in text
    assert "15000.00" in text
    assert "450.00" in text
    assert "VP-2026-ABC123" in text
    assert "2026-08-14" in text
    assert "FICTIONAL SAMPLE" in text
    assert "NOT A REAL INSURANCE CERTIFICATE" in text