import shutil
from datetime import datetime
from pathlib import Path

import pandas as pd


def ingest_csv(source_file: Path, bronze_dir: Path) -> int:
    """
    Read a CSV file from the source layer and copy it to Bronze.

    Returns:
        Number of records ingested.
    """

    if not source_file.exists():
        raise FileNotFoundError(
            f"Source file not found: {source_file}"
        )

    bronze_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    df = pd.read_csv(source_file)

    ingestion_time = datetime.now()

    df["ingestion_timestamp"] = ingestion_time

    destination_file = bronze_dir / source_file.name

    df.to_csv(
        destination_file,
        index=False,
    )

    print(
        f"Ingested {len(df)} records "
        f"from {source_file.name}"
    )

    print(
        f"Bronze file: {destination_file}"
    )

    return len(df)