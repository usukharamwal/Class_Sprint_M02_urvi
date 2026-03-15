#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

mkdir -p figs

echo "Running visualization pipeline"
python workflow/Final_1d.py
python workflow/Final_2d.py
python workflow/Final_MM.py
python workflow/Final_DD.py
echo "Done. Figures saved to ./figs"