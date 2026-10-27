import secrets
import string
from datetime import datetime, timezone

ALPHABET = string.ascii_uppercase + string.digits


def generate_reference_code() -> str:
    """Generate a hard-to-guess, human-shareable complaint reference."""
    date_part = datetime.now(timezone.utc).strftime("%Y%m%d")
    rand_part = "".join(
        secrets.choice(ALPHABET) for _ in range(12)
    )
    return f"CM-{date_part}-{rand_part}"