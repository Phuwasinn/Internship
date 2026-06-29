from __future__ import annotations

import os
import glob
import pandas as pd
import numpy as np

#LOADING
def load_all_csvs(data_dir: str) -> dict[str, pd.DataFrame]:
    dataframes={}
    csv_paths=sorted(glob.glob(os.path.join(data_dir, "*.csv")))

    for path in csv_paths:
        name=os.path.splitext(os.path.basename(path))[0]
        df=pd.read_csv(path, na_values=["\\N"])
        dataframes[name]=df

    return dataframes

#PROFILING
def profile_dataframe(df: pd.DataFrame, name: str, sample_rows: int=3) -> dict:
    n_rows, n_cols = df.shape
    missing_counts = df.isna().sum()
    missing_pct = (missing_counts / n_rows * 100).round(2)

    profile = {
        "name": name,
        "rows": n_rows,
        "columns": n_cols,
        "duplicate_rows": int(df.duplicated().sum()),
        "total_missing_cells": int(missing_counts.sum()),
        "pct_missing_cells": round(missing_counts.sum() / (n_rows * n_cols) * 100, 2),
        "columns_with_missing": missing_pct[missing_pct > 0].to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }
    return profile

#Run profile_dataframe() on every loaded file and return one
def summarize_all(dataframes: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for name, df in dataframes.items():
        p = profile_dataframe(df, name)
        rows.append({
            "file": p["name"],
            "rows": p["rows"],
            "columns": p["columns"],
            "duplicate_rows": p["duplicate_rows"],
            "missing_cells": p["total_missing_cells"],
            "missing_%": p["pct_missing_cells"],
            "cols_with_missing": len(p["columns_with_missing"]),
        })
    summary = pd.DataFrame(rows).sort_values("rows", ascending=False).reset_index(drop=True)
    return summary

#Return columns that actually have missing values
def missing_value_report(df: pd.DataFrame, name: str) -> pd.DataFrame:
    missing = df.isna().sum()
    missing = missing[missing > 0]
    if missing.empty:
        return pd.DataFrame(columns = ["file", "column", "missing_count", "missing_pct"])

    pct = (missing / len(df) * 100).round(2)
    report = pd.DataFrame({
        "file": name,
        "column": missing.index,
        "missing_count": missing.values,
        "missing_pct": pct.values,
    }).sort_values("missing_pct", ascending=False)
    return report

def missing_value_report_all(dataframes: dict[str, pd.DataFrame]) -> pd.DataFrame:
    reports = [missing_value_report(df, name) for name, df in dataframes.items()]
    return pd.concat(reports, ignore_index=True)

#Detect duplicate(Full-row dup or keys dup)
def duplicate_report(df: pd.DataFrame, name: str, key_cols: list[str] | None = None) -> dict:
    full_dupes = int(df.duplicated().sum())
    key_dupes = None
    if key_cols and all(c in df.columns for c in key_cols):
        key_dupes = int(df.duplicated(subset = key_cols).sum())

    return {
        "file": name,
        "full_row_duplicates": full_dupes,
        "key_columns": key_cols,
        "key_duplicates": key_dupes,
    }

#Suspicious (eg: negative lap times)
def numeric_outlier_scan(df: pd.DataFrame, name: str, cols: list[str]) -> pd.DataFrame:
    rows = []
    for col in cols:
        if col not in df.columns:
            continue
        series = pd.to_numeric(df[col], errors="coerce")
        rows.append({
            "file": name,
            "column": col,
            "min": series.min(),
            "max": series.max(),
            "negative_count": int((series < 0).sum()),
            "zero_count": int((series == 0).sum()),
        })
    return pd.DataFrame(rows)

#Check that every foreign key value in child_df exists in parent_df
def check_referential_integrity(
    child_df: pd.DataFrame,
    child_key: str,
    parent_df: pd.DataFrame,
    parent_key: str,
    child_name: str,
    parent_name: str,
) -> dict:
    child_ids = set(child_df[child_key].dropna().unique())
    parent_ids = set(parent_df[parent_key].dropna().unique())
    orphaned = child_ids - parent_ids

    return {
        "child_file": child_name,
        "parent_file": parent_name,
        "key": child_key,
        "orphaned_ids": len(orphaned),
        "sample_orphaned": list(orphaned)[:5],
    }
