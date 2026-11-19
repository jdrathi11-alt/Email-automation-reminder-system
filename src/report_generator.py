"""Report generation module."""
import pandas as pd
from pathlib import Path


def generate_report(results, output_path="outputs/report.csv"):
    """Save email results to a CSV report."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    return output_path
