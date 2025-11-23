"""
fix_sigma_ids.py

Walks the ./sigma directory and ensures every Sigma rule has a valid UUID v4
in the `id:` field.

- If `id:` is missing, it is inserted after `title:`.
- If `id:` has a known placeholder value (3333..., 5555..., TODO, etc.),
  it is replaced with a fresh UUID.
"""

import uuid
import re
from pathlib import Path

# Root of the repo = directory containing this script
ROOT = Path(__file__).parent
SIGMA_ROOT = ROOT / "sigma"

# Any IDs in this list will be treated as placeholders and replaced
PLACEHOLDER_IDS = {
    "33333333-4444-5555-6666-777777777777",
    "55555555-6666-7777-8888-999999999999",
    "00000000-0000-0000-0000-000000000000",
    "TODO",
    "todo",
}

UUID_REGEX = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)


def generate_uuid() -> str:
    return str(uuid.uuid4())


def is_placeholder(value: str) -> bool:
    value = value.strip()
    if value in PLACEHOLDER_IDS:
        return True
    # Very simple heuristic: obviously patterned fake IDs
    parts = value.split("-")
    if len(parts) == 5 and all(len(set(p)) == 1 for p in parts):
        return True
    return False


def process_file(path: Path) -> tuple[bool, str]:
    """
    Returns (changed: bool, message: str)
    """
    text = path.read_text(encoding="utf-8")

    # Look for `id:` line
    id_match = re.search(r"^id:\s*(.+)$", text, flags=re.MULTILINE)

    if id_match:
        current_id = id_match.group(1).strip()

        if UUID_REGEX.match(current_id) and not is_placeholder(current_id):
            # Already has a valid non-placeholder UUID
            return False, "id OK"

        # Replace placeholder or non-UUID with fresh UUID
        new_id = generate_uuid()
        new_text = (
            text[: id_match.start(1)] + new_id + text[id_match.end(1) :]
        )
        path.write_text(new_text, encoding="utf-8")
        return True, f"replaced id -> {new_id}"

    # No id: line at all → insert after title:
    title_match = re.search(r"^title:\s*.+$", text, flags=re.MULTILINE)
    new_id = generate_uuid()
    id_line = f"\nid: {new_id}"

    if title_match:
        insert_pos = title_match.end(0)
        new_text = text[:insert_pos] + id_line + text[insert_pos:]
    else:
        # No title, just prepend at top
        new_text = f"id: {new_id}\n" + text

    path.write_text(new_text, encoding="utf-8")
    return True, f"inserted id -> {new_id}"


def main() -> None:
    if not SIGMA_ROOT.exists():
        print(f"[!] Sigma directory not found: {SIGMA_ROOT}")
        return

    changed = 0
    total = 0

    for yml_path in SIGMA_ROOT.rglob("*.yml"):
        total += 1
        did_change, msg = process_file(yml_path)
        status = "CHANGED" if did_change else "OK"
        print(f"[{status}] {yml_path.relative_to(ROOT)} — {msg}")
        if did_change:
            changed += 1

    for yml_path in SIGMA_ROOT.rglob("*.yaml"):
        total += 1
        did_change, msg = process_file(yml_path)
        status = "CHANGED" if did_change else "OK"
        print(f"[{status}] {yml_path.relative_to(ROOT)} — {msg}")
        if did_change:
            changed += 1

    print("")
    print(f"Processed {total} Sigma files; updated IDs in {changed} of them.")


if __name__ == "__main__":
    main()
