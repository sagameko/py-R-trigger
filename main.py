from pathlib import Path
import pandas as pd
from run_r import run_r

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "outputs"
R_SCRIPTS = ROOT / "r_scripts"

OUT.mkdir(exist_ok=True)

# ---- 1) Call R to transform a CSV ----
input_csv = DATA / "input_example.csv"
output_csv = OUT / "result_from_r.csv"

rc = run_r(str(R_SCRIPTS / "process_data.R"), str(input_csv), str(output_csv))
if rc != 0:
    raise SystemExit(f"R step failed with exit code {rc}")

print("\n[Python] Reading R output back in…")
df = pd.read_csv(output_csv)
print(df.head())

# ---- 2) Call R to generate a report file ----
report_path = OUT / "snapshot_report.txt"
rc = run_r(str(R_SCRIPTS / "Snapshot_Report.R"), str(report_path))
if rc != 0:
    raise SystemExit(f"Report generation failed with exit code {rc}")

print(f"\n[Python] Report generated at: {report_path.resolve()}")
