"""Inspect public-source activation prerequisites without contacting Apple.

A passing result establishes source prerequisites only, never provider readiness.
No hardware identifiers, signing material or account credentials are read.
"""

import json
import re
from pathlib import Path


def inspect(root: Path) -> dict:
    engine = root / "rustpush"
    blockers = []
    validation = engine / "open-absinthe/src/nac.rs"
    if not validation.is_file():
        blockers.append("mac_validation_dependency_missing")
    else:
        source = validation.read_text(encoding="utf-8")
        if re.search(r"\b(?:todo|unimplemented)!\s*\(", source):
            blockers.append("mac_validation_dependency_is_placeholder")

    activation = engine / "src/activation.rs"
    if not activation.is_file():
        blockers.append("engine_submodule_missing")
    else:
        source = activation.read_text(encoding="utf-8")
        names = re.findall(r'include_cert!\("([0-9]+)"\)', source)
        if not names:
            blockers.append("activation_source_requires_manual_review")
        elif any(
            not (engine / "certs/fairplay" / f"{name}.{suffix}").is_file()
            for name in names
            for suffix in ("crt", "pem")
        ):
            blockers.append("activation_signing_material_missing")

    return {
        "schema": 1,
        "check": "source_prerequisites_only",
        "provider_qualified": False,
        "source_prerequisites_present": not blockers,
        "blockers": blockers,
    }


if __name__ == "__main__":
    result = inspect(Path(__file__).resolve().parents[1])
    print(json.dumps(result, indent=2))
    raise SystemExit(2 if result["blockers"] else 0)
