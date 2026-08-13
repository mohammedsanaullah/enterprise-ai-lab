from pathlib import Path
import re
from typing import Union


def sanitize_customer_name(name: str, separator: str = "-") -> str:
    """
    Return a filesystem-safe, lowercase kebab-case customer-name string.
    - Trim and normalize internal whitespace.
    - Replace runs of non-word characters with the separator (preserves Unicode letters/digits).
    - Convert underscores to the separator, collapse repeated separators, and strip edge separators/dots/spaces.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    # Trim and normalize whitespace
    cleaned = " ".join(name.strip().split())

    # Remove ASCII control chars and NUL
    cleaned = "".join(ch for ch in cleaned if ord(ch) >= 32 and ch != "\x00")

    # Replace runs of non-word chars (including punctuation, separators) with the separator
    cleaned = re.sub(r"[^\w]+", separator, cleaned, flags=re.UNICODE)

    # Normalize underscores to separator (underscores are part of \w)
    if separator != "_":
        cleaned = cleaned.replace("_", separator)

    # Lowercase for kebab-case
    cleaned = cleaned.lower()

    # Collapse multiple separators
    cleaned = re.sub(f"{re.escape(separator)}{{2,}}", separator, cleaned)

    # Strip leading/trailing separators, dots, and spaces
    cleaned = cleaned.strip(f"{separator}. ")

    # Limit length to a reasonable maximum
    if len(cleaned) > 200:
        cleaned = cleaned[:200].rstrip(separator)

    if not cleaned:
        raise ValueError("customer name sanitized to empty string")

    return cleaned


def build_policy_filename(customer_name: str) -> str:
    """
    Build a policy filename from a customer name: "<customer-name>-policy.pdf"
    """
    safe = sanitize_customer_name(customer_name)
    return f"{safe}-policy.pdf"


def resolve_unique_filename(directory: Union[str, Path], filename: str) -> Path:
    """
    Given a target directory and a filename, return a Path that does not
    collide with existing files by appending a numeric suffix if needed.
    """
    directory = Path(directory)
    candidate = directory / filename
    if not candidate.exists():
        return candidate

    stem = candidate.stem
    suffix = candidate.suffix

    i = 1
    while True:
        new_name = f"{stem}-{i}{suffix}"
        new_path = directory / new_name
        if not new_path.exists():
            return new_path
        i += 1