from datetime import datetime
from pathlib import Path

import pandas as pd


def create_audit_record(
    batch_id: str,
    file_name: str,
    record_count: int,
    status: str,
    started_at: datetime,
    completed_at: datetime,
) -> dict:

    return {
        "batch_id": batch_id,
        "file_name": file_name,
        "record_count": record_count,
        "status": status,
        "started_at": started_at,
        "completed_at": completed_at,
    }


def write_audit_record(
    audit_record: dict,
    audit_dir: Path,
):

    audit_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    audit_file = audit_dir / "ingestion_audit.csv"

    audit_df = pd.DataFrame(
        [audit_record]
    )

    if audit_file.exists():

        audit_df.to_csv(
            audit_file,
            mode="a",
            header=False,
            index=False,
        )

    else:

        audit_df.to_csv(
            audit_file,
            index=False,
        )