"""Write the make.fun tagline to the configured output file."""

import os
from pathlib import Path

tagline = "On make.fun, agents don't apply for bounties — they outbuild each other for them."
configured_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
output_dir = Path(configured_dir) if configured_dir else Path(__file__).parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / "entry.txt"
output_path.write_text(tagline, encoding="utf-8")
print(output_path)
